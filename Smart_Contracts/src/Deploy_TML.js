const hre = require("hardhat");
const fs = require("fs");

async function main() {
  console.log("🚀 Deploying TML Constitutional Infrastructure...");

  // 1. Get the Contract Factory
  const TMLCore = await hre.ethers.getContractFactory("TML_Core");

  // 2. Deploy
  const tml = await TMLCore.deploy();
  await tml.waitForDeployment();

  const tmlAddress = await tml.getAddress();
  console.log(`✅ TML_Core deployed to: ${tmlAddress}`);

  // 3. Authorize the Deployer as the first Agent (for testing)
  const [deployer] = await hre.ethers.getSigners();
  const tx = await tml.authorizeAgent(deployer.address);
  await tx.wait();
  console.log(`👤 Agent Authorized: ${deployer.address}`);

  // 4. Save Config for the Python Bridge
  const config = {
    address: tmlAddress,
    abi: JSON.parse(TMLCore.interface.formatJson())
  };
  
  fs.writeFileSync("src/TML_Config.json", JSON.stringify(config, null, 2));
  console.log("💾 Configuration saved to TML_Config.json");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
