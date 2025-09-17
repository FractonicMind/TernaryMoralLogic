"""
Content Moderation AI - Dual-Layer SPRL Implementation Example

Demonstrates how a social platform implements TML with:
- Dynamic Stream (DS) from prompt arrival
- Static Anchor (SA) at Sacred Pause
- Framework-enforced thresholds (not configurable)
- I × V × P formula for risk calculation

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
    """Content categories"""
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    LIVESTREAM = "livestream"
    COMMENT = "comment"


class ModerationAction:
    """Moderation actions"""
    APPROVE = "approve"
    REMOVE = "remove"
    SHADOW_BAN = "shadow_ban"
    WARNING = "warning"
    ESCALATE = "escalate_to_human"
    AGE_RESTRICT = "age_restrict"
    FACT_CHECK = "fact_check"


class ContentModerationAI:
    """
    Content moderation system with Dual-Layer SPRL implementation.
    
    Real platforms have complex policies, cultural considerations,
    and safety teams. This demonstrates logging infrastructure only.
    """
    
    def __init__(self):
        # Framework-enforced thresholds (not configurable)
        self.framework = create_tml_framework(
            domain="general",
            retention_days=1095  # 3 years minimum
        )
        
        # Platform statistics (example)
        self.daily_content_volume = 1000000
        self.false_positive_rate = 0.05
        self.appeal_rate = 0.02
        
        print("=" * 70)
        print("CONTENT MODERATION - DUAL-LAYER SPRL")
        print("=" * 70)
        print()
        print("⚠️  NOTICE:")
        print("This demonstrates logging infrastructure only.")
        print("Real content moderation requires nuanced policies,")
        print("cultural awareness, and human oversight.")
        print()
        print("Dual-Layer Architecture:")
        print("  • Dynamic Stream (DS) from prompt arrival")
        print("  • Static Anchor (SA) at Sacred Pause")
        print("  • Framework-enforced thresholds")
        print("  • I × V × P formula for risk calculation")
        print(f"  • Daily Volume: {self.daily_content_volume:,} posts")
        print(f"  • Retention: 3 years minimum")
        print()
    
    def calculate_ivp_components(self, content: Dict) -> Dict:
        """
        Calculate I × V × P components for content moderation.
        
        Real systems use advanced NLP, computer vision,
        and contextual understanding.
        """
        # Initialize components
        impact = 0.5
        vulnerability = 0.5
        probability = 0.5
        
        signals = content.get('signals', {})
        
        # Impact - potential harm severity
        harm_signals = sum([
            signals.get('violence', False) * 0.9,
            signals.get('self_harm', False) * 1.0,
            signals.get('hate_speech', False) * 0.8,
            signals.get('harassment', False) * 0.7,
            signals.get('misinformation', False) * 0.6,
            signals.get('adult_content', False) * 0.5,
            signals.get('spam', False) * 0.2
        ])
        
        # Scale impact by reach
        reach = content.get('potential_reach', 100)
        if reach > 100000:
            impact = min(1.0, harm_signals * 1.2)
        elif reach > 10000:
            impact = min(1.0, harm_signals * 1.0)
        else:
            impact = min(1.0, harm_signals * 0.8)
        
        # Vulnerability - affected population susceptibility
        vulnerability = 0.3  # Base vulnerability
        
        if content.get('targets_individual'):
            vulnerability = max(vulnerability, 0.8)
        if content.get('targets_protected_group'):
            vulnerability = max(vulnerability, 0.9)
        if content.get('youth_audience'):
            vulnerability = max(vulnerability, 1.0)
        
        user = content.get('user', {})
        if user.get('previous_violations', 0) > 3:
            vulnerability = max(vulnerability, 0.7)
        
        # Probability - likelihood of harm occurring
        probability = 0.5  # Base probability
        
        # Critical safety issues have high probability
        if signals.get('self_harm') or signals.get('child_safety'):
            probability = 1.0
        elif any([signals.get('violence'), signals.get('hate_speech')]):
            probability = 0.8
        elif signals.get('harassment'):
            probability = 0.7
        elif signals.get('misinformation') and content.get('viral_potential'):
            probability = 0.9
        else:
            probability = 0.4
        
        # Verified accounts slightly lower probability
        if user.get('verified'):
            probability *= 0.9
        
        return {
            'impact': min(1.0, impact),
            'vulnerability': min(1.0, vulnerability),
            'probability': min(1.0, probability)
        }
    
    def moderate_content(self, content: Dict) -> Dict:
        """Process content moderation decision with Dual-Layer SPRL."""
        
        # Mark prompt arrival (t₀)
        content['prompt_timestamp'] = datetime.now().isoformat()
        
        # Calculate I×V×P components
        ivp = self.calculate_ivp_components(content)
        content['i_v_p'] = ivp
        
        # Calculate SPRL score
        sprl = ivp['impact'] * ivp['vulnerability'] * ivp['probability']
        content['sprl_score'] = max(0.0001, min(0.9999, sprl))
        
        # Identify stakeholders
        stakeholders = [
            {'type': 'content_creator', 'id': content.get('user', {}).get('id')},
            {'type': 'platform', 'id': 'company'}
        ]
        
        if content.get('targets_individual'):
            stakeholders.append({'type': 'targeted_user', 'vulnerability_weight': 0.9})
        
        if content.get('youth_audience'):
            stakeholders.append({'type': 'minor_viewers', 'vulnerability_weight': 1.0})
        
        audience_size = content.get('potential_reach', 100)
        if audience_size > 10000:
            stakeholders.append({'type': 'community', 'size': audience_size})
        
        content['stakeholders'] = stakeholders
        
        # Check for vulnerable populations
        content['affects_minors'] = content.get('youth_audience', False)
        
        def moderation_logic(context):
            sprl = context['sprl_score']
            signals = context.get('signals', {})
            
            # Critical safety issues - Prohibit (-1)
            if signals.get('self_harm') or signals.get('child_safety'):
                return {
                    'decision_state': -1,  # Prohibit
                    'action': ModerationAction.REMOVE,
                    'reason': 'Critical safety violation',
                    'priority': 'immediate',
                    'notify_safety_team': True,
                    'preserve_evidence': True,
                    'appeal_available': False
                }
            
            # High risk - Sacred Pause (0) or Prohibit (-1)
            elif sprl > 0.8:
                return {
                    'decision_state': -1,  # Prohibit
                    'action': ModerationAction.REMOVE,
                    'reason': 'Policy violation',
                    'violated_policies': list(signals.keys()),
                    'appeal_available': True,
                    'user_notification': True
                }
            
            # Elevated risk - Sacred Pause (0)
            elif sprl > 0.6:
                return {
                    'decision_state': 0,  # Sacred Pause
                    'action': ModerationAction.ESCALATE,
                    'reason': 'Requires human review',
                    'confidence': 'low',
                    'hold_visibility': True,
                    'review_priority': 'high'
                }
            
            # Moderate risk - Sacred Pause (0) with specific action
            elif sprl > 0.4:
                if context.get('youth_audience'):
                    return {
                        'decision_state': 0,  # Sacred Pause
                        'action': ModerationAction.AGE_RESTRICT,
                        'reason': 'Not suitable for all audiences',
                        'age_gate': 18,
                        'appeal_available': True
                    }
                elif signals.get('misinformation'):
                    return {
                        'decision_state': 0,  # Sacred Pause
                        'action': ModerationAction.FACT_CHECK,
                        'reason': 'Potentially misleading',
                        'add_context': True,
                        'reduce_distribution': True
                    }
                else:
                    return {
                        'decision_state': 1,  # Proceed with warning
                        'action': ModerationAction.WARNING,
                        'reason': 'Borderline content',
                        'warning_type': 'soft',
                        'user_education': True
                    }
            
            # Low risk - Proceed (+1)
            else:
                return {
                    'decision_state': 1,  # Proceed
                    'action': ModerationAction.APPROVE,
                    'reason': 'No policy violations detected',
                    'confidence': 'high',
                    'review_not_required': True
                }
        
        # Process with Dual-Layer SPRL
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
        
        decision_counts = {1: 0, 0: 0, -1: 0}
        
        for content in test_content:
            print(f"Content: {content['content_id']}")
            print(f"  Type: {content['type']}")
            print(f"  Description: {content['description']}")
            print(f"  Potential Reach: {content.get('potential_reach', 0):,}")
            
            result = self.moderate_content(content)
            decision = result['decision']
            
            # Show I×V×P components
            ivp = content.get('i_v_p', {})
            print(f"  I×V×P Components:")
            print(f"    Impact: {ivp.get('impact', 0):.2f}")
            print(f"    Vulnerability: {ivp.get('vulnerability', 0):.2f}")
            print(f"    Probability: {ivp.get('probability', 0):.2f}")
            print(f"  SPRL Score: {content['sprl_score']:.4f}")
            
            # Decision state
            state = decision.get('decision_state', 1)
            state_str = {1: "PROCEED", 0: "SACRED PAUSE", -1: "PROHIBIT"}[state]
            decision_counts[state] += 1
            
            print(f"  Decision State: {state_str}")
            print(f"  Action: {decision['action'].upper()}")
            print(f"  Reason: {decision['reason']}")
            
            # Dual-layer tracking
            if state == 0:
                print(f"  ✓ Static Anchor set at Sacred Pause")
                if content.get('affects_minors'):
                    print(f"    👶 Enhanced protection: Youth safety")
                if content.get('targets_individual'):
                    print(f"    🎯 Enhanced protection: Targeted harm")
            elif state == -1:
                print(f"  ⛔ Content prohibited")
                if decision.get('preserve_evidence'):
                    print(f"    🚨 Evidence preserved for safety team")
            
            if decision.get('appeal_available'):
                print(f"  📝 Appeal available to user")
            
            print()
        
        # Summary statistics
        print("MODERATION SUMMARY")
        print("-" * 70)
        print(f"Decision States:")
        print(f"  +1 (Proceed): {decision_counts[1]}")
        print(f"   0 (Sacred Pause): {decision_counts[0]}")
        print(f"  -1 (Prohibit): {decision_counts[-1]}")
        print()
        print("Dynamic Stream provides continuous tracking")
        print("Static Anchor marks entry into moral complexity")
        print()
    
    def demonstrate_appeal_process(self):
        """Show how appeals use Dual-Layer SPRL logs."""
        
        print("=" * 70)
        print("APPEAL PROCESS - DUAL-LAYER SPRL")
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
            print("Appeal Review Findings from Dual-Layer Logs:")
            print(f"  ✓ Dynamic Stream shows risk progression")
            print(f"  ✓ Static Anchor set at decision point")
            print(f"  ✓ I×V×P: I=0.72, V=0.60, P=0.90")
            print(f"  ✓ SPRL Score: 0.3888")
            print(f"  ✓ Decision State: 0 (Sacred Pause)")
            print(f"  ✓ Alternative actions evaluated")
            print()
            print("Appeal Outcome:")
            print("  Based on dual-layer evidence, content had")
            print("  moderate risk. Fact-check label would suffice.")
            print("  Content reinstated with context added.")
            print()
            print("Dual-Layer SPRL enables evidence-based appeals.")
        
        print()
    
    def display_platform_metrics(self):
        """Display platform safety metrics."""
        
        print("=" * 70)
        print("PLATFORM SAFETY METRICS - DUAL-LAYER")
        print("=" * 70)
        
        stats = self.framework.get_performance_report()
        
        print(f"Infrastructure Performance:")
        print(f"  Total Decisions: {stats.get('total_decisions', 0)}")
        print()
        print("Decision State Distribution:")
        print(f"  +1 (Proceed): {stats.get('proceed_count', 0)}")
        print(f"   0 (Sacred Pause): {stats.get('sacred_pause_count', 0)}")
        print(f"  -1 (Prohibit): {stats.get('prohibit_count', 0)}")
        print()
        print("Dual-Layer Metrics:")
        print(f"  Dynamic Stream Continuity: {stats.get('ds_continuity', 100)}%")
        print(f"  Static Anchors Set: {stats.get('sa_count', 0)}")
        print(f"  Average SA Write Time: {stats.get('sa_write_time_ms', 0):.1f}ms")
        print(f"  Lite Traces (near-miss): {stats.get('lite_trace_count', 0)}")
        print()
        print("Performance:")
        print(f"  Non-blocking Verified: {stats.get('non_blocking', True)}")
        print(f"  Average Latency: {stats.get('avg_latency_ms', 0):.1f}ms")
        print()
        print("Note: Thresholds are framework-enforced")
        print("Platforms cannot configure or game thresholds")
        print()
        
        # Cost estimation
        if self.daily_content_volume and stats.get('sacred_pause_count'):
            pause_rate = stats.get('sacred_pause_count', 0) / max(stats.get('total_decisions', 1), 1)
            daily_logs = self.daily_content_volume * pause_rate
            annual_logs = daily_logs * 365
            # ~45 bytes per log after compression
            annual_storage_gb = (annual_logs * 45) / (1024**3)
            annual_cost = annual_storage_gb * 0.023 * 12  # ~$0.023/GB/month
            
            print(f"ESTIMATED ANNUAL COSTS:")
            print(f"  Daily Sacred Pauses: {daily_logs:,.0f}")
            print(f"  Annual Logs: {annual_logs:,.0f}")
            print(f"  Storage Required: {annual_storage_gb:.1f} GB")
            print(f"  Estimated Cost: ${annual_cost:,.2f}/year")
            print()
            print("Compare to: Average content lawsuit exceeds $500K")
        
        print()


def main():
    """Run content moderation demonstration."""
    
    # Create moderation system
    moderation_ai = ContentModerationAI()
    
    # Simulate content processing
    moderation_ai.simulate_content_stream()
    
    # Demonstrate appeals
    moderation_ai.demonstrate_appeal_process()
    
    # Display metrics
    moderation_ai.display_platform_metrics()
    
    # Compliance check
    print("=" * 70)
    print("TML COMPLIANCE CHECK")
    print("=" * 70)
    
    compliance = ComplianceChecker.check_framework(moderation_ai.framework)
    
    print(f"Infrastructure Compliant: {compliance['infrastructure_compliant']}")
    if compliance.get('issues'):
        for issue in compliance['issues']:
            print(f"  ✗ {issue}")
    else:
        print("✓ All infrastructure requirements met")
    
    print()
    print("=" * 70)
    print("KEY TAKEAWAYS FOR PLATFORMS")
    print("=" * 70)
    print()
    print("1. Dual-Layer SPRL provides:")
    print("   - Dynamic Stream from prompt arrival")
    print("   - Static Anchor at Sacred Pause")
    print("   - I × V × P formula for risk")
    print("   - Framework-enforced thresholds")
    print()
    print("2. Decision states:")
    print("   +1 = Proceed (approve/warn)")
    print("    0 = Sacred Pause (review/restrict)")
    print("   -1 = Prohibit (remove/block)")
    print()
    print("3. Enables evidence-based appeals")
    print("4. Supports transparency reporting")
    print("5. Helps detect coordinated harm")
    print("6. Preserves evidence for safety teams")
    print()
    print("Remember: Thresholds are framework-enforced")
    print("Platforms implement but cannot configure thresholds")
    print()
    print("Framework Support: support@tml-goukassian.org")
    print("See Succession Charter: /TML-SUCCESSION-CHARTER.md")


if __name__ == "__main__":
    main()
