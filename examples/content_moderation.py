"""
Content Moderation AI TML Implementation Example

Demonstrates how a social platform MIGHT implement TML for content
moderation decisions. All thresholds are EXAMPLES ONLY. Each platform
must determine appropriate values based on their community standards
and user safety requirements.

This is a demonstration of logging infrastructure, not actual moderation logic.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from implementations.python_library import create_tml_framework, ComplianceChecker
import random
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import hashlib


class ContentType:
    """Example content categories"""
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    LIVESTREAM = "livestream"
    COMMENT = "comment"


class ModerationAction:
    """Example moderation actions"""
    APPROVE = "approve"
    REMOVE = "remove"
    SHADOW_BAN = "shadow_ban"
    WARNING = "warning"
    ESCALATE = "escalate_to_human"
    AGE_RESTRICT = "age_restrict"
    FACT_CHECK = "fact_check"


class ContentModerationAI:
    """
    EXAMPLE content moderation system with TML integration.
    
    Real platforms have complex policies, cultural considerations,
    and safety teams. This demonstrates logging infrastructure only.
    """
    
    def __init__(self):
        # EXAMPLE CONFIGURATION - Platform determines actual values
        self.framework = create_tml_framework(
            sprl_threshold=0.5,  # EXAMPLE: Medium threshold
            domain="general",
            calculate_risk_on="all",
            retention_days=1095  # 3 years minimum
        )
        
        # Platform statistics (example)
        self.daily_content_volume = 1000000
        self.false_positive_rate = 0.05
        self.appeal_rate = 0.02
        
        print("=" * 70)
        print("CONTENT MODERATION AI TML EXAMPLE")
        print("=" * 70)
        print()
        print("⚠️  NOTICE:")
        print("This demonstrates logging infrastructure only.")
        print("Real content moderation requires nuanced policies,")
        print("cultural awareness, and human oversight.")
        print()
        print("Example Configuration:")
        print(f"  SPRL Threshold: {self.framework.sprl_threshold} (platform's choice)")
        print(f"  Daily Volume: {self.daily_content_volume:,} posts")
        print(f"  Retention: 3 years minimum")
        print()
    
    def assess_content_risk(self, content: Dict) -> float:
        """
        EXAMPLE risk assessment for content.
        
        Real systems use advanced NLP, computer vision,
        and contextual understanding.
        """
        risk_score = 0.0
        
        # Content signals (simplified examples)
        signals = content.get('signals', {})
        
        # Harm potential
        if signals.get('violence'):
            risk_score += 0.7
        if signals.get('self_harm'):
            risk_score += 0.9
        if signals.get('hate_speech'):
            risk_score += 0.8
        if signals.get('harassment'):
            risk_score += 0.6
        if signals.get('misinformation'):
            risk_score += 0.5
        if signals.get('spam'):
            risk_score += 0.3
        if signals.get('adult_content'):
            risk_score += 0.4
        
        # Context factors
        if content.get('targets_individual'):
            risk_score += 0.3
        if content.get('targets_protected_group'):
            risk_score += 0.4
        if content.get('viral_potential'):
            risk_score += 0.2
        
        # User factors
        user = content.get('user', {})
        if user.get('new_account'):
            risk_score += 0.1
        if user.get('previous_violations', 0) > 3:
            risk_score += 0.3
        if user.get('verified'):
            risk_score *= 0.8  # Slightly lower risk for verified
        
        # Audience factors
        if content.get('youth_audience'):
            risk_score += 0.4
        if content.get('sensitive_topic'):
            risk_score += 0.2
        
        return min(risk_score, 1.0)
    
    def moderate_content(self, content: Dict) -> Dict:
        """Process content moderation decision with TML logging."""
        
        # Calculate risk
        content['calculated_risk'] = self.assess_content_risk(content)
        
        # Identify stakeholders
        stakeholders = [
            {'type': 'content_creator', 'id': content.get('user', {}).get('id')},
            {'type': 'platform', 'id': 'company'}
        ]
        
        if content.get('targets_individual'):
            stakeholders.append({'type': 'targeted_user', 'vulnerability': 1.5})
        
        if content.get('youth_audience'):
            stakeholders.append({'type': 'minor_viewers', 'vulnerability': 2.0})
        
        audience_size = content.get('potential_reach', 100)
        if audience_size > 10000:
            stakeholders.append({'type': 'community', 'size': audience_size})
        
        content['stakeholders'] = stakeholders
        
        # Check for vulnerable populations
        content['affects_minors'] = content.get('youth_audience', False)
        
        def moderation_logic(context):
            risk = context['calculated_risk']
            signals = context.get('signals', {})
            
            # Critical safety issues
            if signals.get('self_harm') or signals.get('child_safety'):
                return {
                    'action': ModerationAction.REMOVE,
                    'reason': 'Critical safety violation',
                    'priority': 'immediate',
                    'notify_safety_team': True,
                    'preserve_evidence': True,
                    'appeal_available': False
                }
            
            # High risk content
            elif risk > 0.8:
                return {
                    'action': ModerationAction.REMOVE,
                    'reason': 'Policy violation',
                    'violated_policies': list(signals.keys()),
                    'appeal_available': True,
                    'user_notification': True
                }
            
            # Elevated risk
            elif risk > 0.6:
                return {
                    'action': ModerationAction.ESCALATE,
                    'reason': 'Requires human review',
                    'confidence': 'low',
                    'hold_visibility': True,
                    'review_priority': 'high'
                }
            
            # Moderate risk
            elif risk > 0.4:
                if context.get('youth_audience'):
                    return {
                        'action': ModerationAction.AGE_RESTRICT,
                        'reason': 'Not suitable for all audiences',
                        'age_gate': 18,
                        'appeal_available': True
                    }
                elif signals.get('misinformation'):
                    return {
                        'action': ModerationAction.FACT_CHECK,
                        'reason': 'Potentially misleading',
                        'add_context': True,
                        'reduce_distribution': True
                    }
                else:
                    return {
                        'action': ModerationAction.WARNING,
                        'reason': 'Borderline content',
                        'warning_type': 'soft',
                        'user_education': True
                    }
            
            # Low risk
            else:
                return {
                    'action': ModerationAction.APPROVE,
                    'reason': 'No policy violations detected',
                    'confidence': 'high',
                    'review_not_required': True
                }
        
        # Process with TML
        result = self.framework.process_decision(
            context=content,
            ai_decision_func=moderation_logic
        )
        
        return result
    
    def simulate_content_stream(self):
        """Simulate processing a stream of content."""
        
        print("CONTENT MODERATION SIMULATION")
        print("-" * 70)
        print()
        
        test_content = [
            {
                'content_id': 'POST-001',
                'type': ContentType.TEXT,
                'user': {'id': 'USER-A', 'verified': True, 'followers': 50000},
                'signals': {},
                'potential_reach': 50000,
                'description': 'Verified user sharing news article'
            },
            {
                'content_id': 'POST-002',
                'type': ContentType.IMAGE,
                'user': {'id': 'USER-B', 'new_account': True},
                'signals': {'spam': True, 'commercial': True},
                'potential_reach': 100,
                'description': 'New account posting spam'
            },
            {
                'content_id': 'POST-003',
                'type': ContentType.VIDEO,
                'user': {'id': 'USER-C', 'previous_violations': 2},
                'signals': {'misinformation': True},
                'viral_potential': True,
                'potential_reach': 100000,
                'description': 'Viral misinformation video'
            },
            {
                'content_id': 'POST-004',
                'type': ContentType.TEXT,
                'user': {'id': 'USER-D'},
                'signals': {'harassment': True},
                'targets_individual': True,
                'description': 'Targeted harassment'
            },
            {
                'content_id': 'POST-005',
                'type': ContentType.VIDEO,
                'user': {'id': 'USER-E'},
                'signals': {'adult_content': True},
                'youth_audience': True,
                'potential_reach': 10000,
                'description': 'Adult content in youth space'
            },
            {
                'content_id': 'POST-006',
                'type': ContentType.COMMENT,
                'user': {'id': 'USER-F'},
                'signals': {'self_harm': True},
                'description': 'Crisis content requiring immediate action'
            },
            {
                'content_id': 'POST-007',
                'type': ContentType.LIVESTREAM,
                'user': {'id': 'USER-G', 'verified': False},
                'signals': {'hate_speech': True},
                'targets_protected_group': True,
                'potential_reach': 5000,
                'description': 'Hate speech in livestream'
            }
        ]
        
        approved = 0
        removed = 0
        escalated = 0
        other_actions = 0
        
        for content in test_content:
            print(f"Content: {content['content_id']}")
            print(f"  Type: {content['type']}")
            print(f"  Description: {content['description']}")
            print(f"  Potential Reach: {content.get('potential_reach', 0):,}")
            
            result = self.moderate_content(content)
            decision = result['decision']
            
            print(f"  Action: {decision['action'].upper()}")
            print(f"  Reason: {decision['reason']}")
            print(f"  Risk Score: {content['calculated_risk']:.2f}")
            print(f"  SPRL Score: {result['sprl_score']:.2f}")
            
            # Count actions
            if decision['action'] == ModerationAction.APPROVE:
                approved += 1
            elif decision['action'] == ModerationAction.REMOVE:
                removed += 1
            elif decision['action'] == ModerationAction.ESCALATE:
                escalated += 1
            else:
                other_actions += 1
            
            if result['sacred_pause_triggered']:
                print(f"  ✓ Decision logged for accountability")
                print(f"    Log Hash: {result['storage_hash'][:12]}...")
                if content.get('affects_minors'):
                    print(f"    👶 Enhanced logging: Youth safety")
                if content.get('targets_individual'):
                    print(f"    🎯 Enhanced logging: Targeted harm")
                if decision.get('preserve_evidence'):
                    print(f"    🚨 Evidence preserved for safety team")
            else:
                print(f"  - Below logging threshold")
            
            if decision.get('appeal_available'):
                print(f"  📝 Appeal available to user")
            
            print()
        
        # Summary statistics
        print("MODERATION SUMMARY")
        print("-" * 70)
        print(f"Approved: {approved}")
        print(f"Removed: {removed}")
        print(f"Escalated: {escalated}")
        print(f"Other Actions: {other_actions}")
        print()
    
    def demonstrate_appeal_process(self):
        """Show how appeals use TML logs."""
        
        print("=" * 70)
        print("APPEAL PROCESS DEMONSTRATION")
        print("=" * 70)
        print()
        
        print("Scenario: User appeals content removal")
        print()
        
        # Original decision that user is appealing
        original_content = {
            'content_id': 'POST-003',
            'decision_id': 'DEC-12345',
            'user': {'id': 'USER-C'},
            'removal_time': (datetime.now() - timedelta(hours=2)).isoformat(),
            'removal_reason': 'Misinformation'
        }
        
        print(f"Original Decision:")
        print(f"  Content ID: {original_content['content_id']}")
        print(f"  Removed: {original_content['removal_time']}")
        print(f"  Reason: {original_content['removal_reason']}")
        print()
        
        # Request logs for appeal review
        appeal_investigation = {
            'id': 'APPEAL-2025-08-001',
            'decision_id': original_content['decision_id'],
            'timeframe': (
                (datetime.now() - timedelta(hours=3)).isoformat(),
                datetime.now().isoformat()
            )
        }
        
        # Trust & Safety team reviews logs
        investigation = self.framework.provide_investigation_access(
            institution='un_human_rights',  # Example appeals body
            incident=appeal_investigation
        )
        
        if investigation:
            print("Appeal Review Findings from TML Logs:")
            print(f"  ✓ Decision logged at time of action")
            print(f"  ✓ Risk score: 0.65 (above threshold)")
            print(f"  ✓ Signals detected: ['misinformation']")
            print(f"  ✓ Viral potential considered: Yes")
            print(f"  ✓ Alternative actions evaluated: fact-check, age-restrict")
            print()
            print("Appeal Outcome:")
            print("  Based on logged evidence, original decision was")
            print("  consistent with platform policies. However, fact-check")
            print("  label might have been sufficient. Content reinstated")
            print("  with fact-check context added.")
            print()
            print("TML logs enable consistent, evidence-based appeals.")
        
        print()
    
    def demonstrate_transparency_report(self):
        """Generate transparency report using TML data."""
        
        print("=" * 70)
        print("QUARTERLY TRANSPARENCY REPORT")
        print("=" * 70)
        print()
        
        # Simulated quarterly statistics
        stats = self.framework.get_performance_report()
        
        # Extrapolate for quarter (example)
        quarterly_decisions = stats['total_decisions'] * 1000
        quarterly_logged = stats['sacred_pause_triggers'] * 1000
        
        print("Platform Transparency Metrics:")
        print(f"  Total Content Reviewed: {quarterly_decisions:,}")
        print(f"  Decisions Logged: {quarterly_logged:,}")
        print(f"  Logging Rate: {stats['trigger_rate']:.1f}%")
        print()
        
        # Simulated category breakdown
        print("Content Actions (Example):")
        print(f"  Removed for Violence: 2,341")
        print(f"  Removed for Hate Speech: 1,892")
        print(f"  Removed for Misinformation: 5,234")
        print(f"  Age-Restricted: 8,921")
        print(f"  Fact-Checked: 12,456")
        print(f"  Human Review: 3,421")
        print()
        
        print("Accountability Metrics:")
        print(f"  Appeals Filed: {int(quarterly_logged * 0.02):,}")
        print(f"  Appeals Successful: {int(quarterly_logged * 0.02 * 0.3):,}")
        print(f"  Average Appeal Resolution: 48 hours")
        print(f"  Youth Safety Actions: {int(quarterly_logged * 0.15):,}")
        print()
        
        print("TML enables detailed transparency reporting while")
        print("preserving user privacy through aggregation.")
        print()
    
    def demonstrate_coordinated_harm_detection(self):
        """Show how TML helps detect coordinated harmful behavior."""
        
        print("=" * 70)
        print("COORDINATED HARM DETECTION")
        print("=" * 70)
        print()
        
        print("Scenario: Detecting coordinated harassment campaign")
        print()
        
        # Simulate pattern detection across multiple decisions
        print("Pattern Analysis from TML Logs:")
        print("  Time Window: Last 24 hours")
        print("  Target: USER-X")
        print()
        print("  Detected Pattern:")
        print("    - 47 accounts posted similar content")
        print("    - All targeted same individual")
        print("    - Temporal clustering: 85% within 2 hours")
        print("    - Account similarities: 73% created < 7 days ago")
        print("    - Content similarity: 91% using same phrases")
        print()
        print("  Action Taken:")
        print("    ✓ Coordinated harm protocol activated")
        print("    ✓ All related content removed")
        print("    ✓ Accounts suspended pending investigation")
        print("    ✓ Target user offered additional protection")
        print("    ✓ Evidence package prepared for law enforcement")
        print()
        print("TML logs enable detection of coordinated harmful")
        print("behavior that individual decisions might miss.")
        print()
    
    def display_platform_metrics(self):
        """Display platform safety metrics."""
        
        print("=" * 70)
        print("PLATFORM SAFETY METRICS")
        print("=" * 70)
        
        stats = self.framework.get_performance_report()
        
        print(f"Infrastructure Performance:")
        print(f"  Total Decisions: {stats['total_decisions']}")
        print(f"  Logged Decisions: {stats['sacred_pause_triggers']}")
        print(f"  Logging Rate: {stats['trigger_rate']:.1f}%")
        print(f"  Average Log Time: {stats['average_logging_time_ms']:.1f}ms")
        print(f"  Storage Optimization: {stats['storage_optimization']}")
        print()
        
        # Platform-specific guidance
        print("CALIBRATION GUIDANCE FOR PLATFORMS:")
        print()
        
        if stats['trigger_rate'] < 3:
            print("⚠️  Very low logging rate")
            print("  - May miss harmful content patterns")
            print("  - Appeals lack sufficient evidence")
            print("  - Consider lowering threshold")
        elif stats['trigger_rate'] > 40:
            print("⚠️  High logging rate")
            print("  - Storage costs may be significant")
            print("  - Many routine decisions logged")
            print("  - Consider raising threshold")
        else:
            print("✓ Logging rate appears balanced")
            print("  - Continue monitoring for harmful patterns")
            print("  - Regular calibration recommended")
        
        print()
        
        # Cost estimation
        if self.daily_content_volume and stats['trigger_rate']:
            daily_logs = self.daily_content_volume * (stats['trigger_rate'] / 100)
            annual_logs = daily_logs * 365
            # ~45 bytes per log after compression
            annual_storage_gb = (annual_logs * 45) / (1024**3)
            annual_cost = annual_storage_gb * 0.023 * 12  # ~$0.023/GB/month
            
            print(f"ESTIMATED ANNUAL COSTS:")
            print(f"  Daily Logs: {daily_logs:,.0f}")
            print(f"  Annual Logs: {annual_logs:,.0f}")
            print(f"  Storage Required: {annual_storage_gb:.1f} GB")
            print(f"  Estimated Cost: ${annual_cost:,.2f}/year")
            print()
            print("Compare to: Average content lawsuit exceeds $500K")
        
        print()


def main():
    """Run content moderation demonstration."""
    
    # Create example moderation system
    moderation_ai = ContentModerationAI()
    
    # Simulate content processing
    moderation_ai.simulate_content_stream()
    
    # Demonstrate appeals
    moderation_ai.demonstrate_appeal_process()
    
    # Show transparency reporting
    moderation_ai.demonstrate_transparency_report()
    
    # Demonstrate coordinated harm detection
    moderation_ai.demonstrate_coordinated_harm_detection()
    
    # Display metrics
    moderation_ai.display_platform_metrics()
    
    # Compliance check
    print("=" * 70)
    print("TML COMPLIANCE CHECK")
    print("=" * 70)
    
    compliance = ComplianceChecker.check_framework(moderation_ai.framework)
    
    print(f"Infrastructure Compliant: {compliance['infrastructure_compliant']}")
    if compliance['issues']:
        for issue in compliance['issues']:
            print(f"  ✗ {issue}")
    else:
        print("✓ All infrastructure requirements met")
    
    print()
    print("=" * 70)
    print("KEY TAKEAWAYS FOR PLATFORMS")
    print("=" * 70)
    print()
    print("1. TML provides accountability infrastructure")
    print("2. Platforms determine their own thresholds")
    print("3. Enables evidence-based appeals")
    print("4. Supports transparency reporting")
    print("5. Helps detect coordinated harm")
    print("6. Preserves evidence for safety teams")
    print()
    print("Remember: Each platform must calibrate based on:")
    print("  - Community standards")
    print("  - User safety requirements")
    print("  - Regulatory obligations")
    print("  - Operational constraints")
    print()
    print("This example uses arbitrary thresholds.")
    print("Your platform must determine appropriate values.")
    print()
    print("Contact Information:")
    print("- Email: leogouk@gmail.com")
    print("- Successor Contact: support@tml-goukassian.org")
    print("- See Succession Charter: /TML-SUCCESSION-CHARTER.md")


if __name__ == "__main__":
    main()
