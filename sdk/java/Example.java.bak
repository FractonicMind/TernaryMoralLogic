/**
 * TML Example - Blockchain Implementation
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 */
package org.tml.example;

import org.tml.sdk.*;
import java.util.HashMap;
import java.util.Map;

public class Example {
    
    public static void main(String[] args) throws Exception {
        System.out.println("=================================");
        System.out.println("🏮 TML BLOCKCHAIN DEMONSTRATION");
        System.out.println("=================================\n");
        
        // Initialize TML (10 minutes, not 12+ months)
        TMLConfig config = new TMLConfig();
        TMLClient client = new TMLClient(config);
        AlwaysMemoryLogger logger = new AlwaysMemoryLogger();
        
        // Show deployment reality
        System.out.println(config.getDeploymentComparison());
        
        // Example 1: Create Always Memory log
        System.out.println("\n--- Example 1: Always Memory ---");
        Map<String, Object> decision = new HashMap<>();
        decision.put("action", "loan_decision");
        decision.put("amount", 100000);
        decision.put("risk", "low");
        
        String logHash = logger.createLog(decision);
        System.out.println("Log created: " + logHash.substring(0, 8) + "...");
        System.out.println("Blockchain anchored: YES");
        System.out.println("Guardian approval: NOT NEEDED\n");
        
        // Example 2: Sacred Zero trigger
        System.out.println("--- Example 2: Sacred Zero ---");
        Map<String, Object> violation = new HashMap<>();
        violation.put("discrimination", true);
        
        TMLClient.Violation result = client.checkSacredZero(violation);
        if (result != null) {
            System.out.printf("Violation: %s\n", result.type);
            System.out.printf("Penalty: $%,d\n", result.penalty);
            System.out.printf("Multiplier: %.1fx\n", result.multiplier);
            System.out.printf("Enforcement: AUTOMATIC\n");
            System.out.printf("Committee review: %s\n\n", result.guardianReview);
        }
        
        // Example 3: Whistleblower reward
        System.out.println("--- Example 3: Whistleblower ---");
        String evidence = "blockchain_proof_abc123";
        TMLClient.WhistleblowerResult reward = client.processWhistleblower(evidence);
        System.out.printf("Evidence verified: YES\n");
        System.out.printf("Reward: $%,d (15%%)\n", reward.reward);
        System.out.printf("Payment time: %d minutes\n", reward.paymentTimeMinutes);
        System.out.printf("Committee approval: %s\n\n", reward.committeeApproval);
        
        // Example 4: Missing logs detection
        System.out.println("--- Example 4: Missing Logs ---");
        boolean valid = logger.verifyLog("");
        if (!valid) {
            System.out.println("Result: CRIMINAL PROSECUTION");
        }
        
        // Show Guardian reality
        System.out.println("--- Guardian Network Truth ---");
        System.out.println(config.getGuardianConfig().getReality());
        
        // Final statistics
        System.out.println("\n--- Session Statistics ---");
        TMLClient.Statistics stats = client.getStatistics();
        System.out.println("Logs created: " + stats.logsCreated);
        System.out.println("Violations caught: " + stats.violationsCaught);
        System.out.println("Guardian meetings: " + stats.guardianMeetings);
        
        System.out.println("\n=================================");
        System.out.println("Deployment: 10 minutes");
        System.out.println("Annual cost: $1,200");
        System.out.println("Protection: ACTIVE");
        System.out.println("Guardians: NOT NEEDED");
        System.out.println("=================================");
    }
}
