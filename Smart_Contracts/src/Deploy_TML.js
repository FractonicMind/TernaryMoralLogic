// Deploy_TML.js
// Script to deploy the Ternary Moral Logic Ecosystem

const hre = require("hardhat");

async function main() {
  console.log("--- Starting TML Moral Engine Deployment ---");

  // 1. Deploy the Moral Storage (Memory)
  const StorageFactory = await hre.ethers.getContractFactory("TML_Storage");
  const storage = await StorageFactory.deploy();
  await storage.waitForDeployment();
  console.log(`[+] TML_Storage deployed to: ${await storage.getAddress()}`);

  // 2. Deploy the Moral Core (Conscience), linking to Storage
  const CoreFactory = await hre.ethers.getContractFactory("TML_Core");
  const core = await CoreFactory.deploy(await storage.getAddress());
  await core.waitForDeployment();
  console.log(`[+] TML_Core deployed to:    ${await core.getAddress()}`);

  // 3. Link them: Authorize Core to write to Storage
  const tx = await storage.setMoralKernel(await core.getAddress());
  await tx.wait();
  console.log("[+] Storage linked. Core authorized to write Moral Logs.");

  console.log("--- Deployment Complete ---");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
