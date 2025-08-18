"""
Content Moderation AI System - TML Framework Implementation
==========================================================

This example demonstrates how the Ternary Moral Logic framework handles
complex content moderation decisions using Sacred Pause for morally
ambiguous posts requiring human-level ethical reasoning.

Real-world use case: Social media platform content evaluation
"""

from tml import TMLEvaluator, TMLState, TMLEvaluation
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import json
import re

class ContentType(Enum):
    """Types of content being moderated"""
    TEXT_POST = "text_post"
    IMAGE = "image"
    VIDEO = "video"
    COMMENT = "comment"
    LIVE_STREAM = "live_stream"

class ContentCategory(Enum):
    """Content categories for classification"""
    HATE_SPEECH = "hate_speech"
    MISINFORMATION = "misinformation"
    VIOLENCE = "violence"
    HARASSMENT = "harassment"
    ADULT_CONTENT = "adult_content"
    SELF_HARM = "self_harm"
    POLITICAL = "political"
    RELIGIOUS = "religious"
    SATIRICAL = "satirical"
    EDUCATIONAL = "educational"
    NEWS = "news"
    PERSONAL = "personal"

class ModerationAction(Enum):
    """Possible moderation actions"""
    APPROVE = "approve"
    REMOVE = "remove"
    WARN_USER = "warn_user"
    RESTRICT_REACH = "restrict_reach"
    REQUIRE_WARNING_LABEL = "require_warning_label"
    ESCALATE_TO_HUMAN = "escalate_to_human"
    TEMPORARY_SUSPEND = "temporary_suspend"
    PERMANENT_BAN = "permanent_ban"

@dataclass
class User:
    """User information for context"""
    user_id: str
    age: int
    follower_count: int
    account_age_days: int
    previous_violations: int
    verification_status: str  # "verified", "unverified", "public_figure"
    location: str

@dataclass
class Content:
    """Content item for moderation"""
    content_id: str
    content_type: ContentType
    text: str
    author: User
    engagement_metrics: Dict[str, int]  # likes, shares, comments, views
    report_count: int
    content_category: Optional[ContentCategory] = None
    contains_sensitive_topics: List[str] = None
    language: str = "en"
    timestamp: datetime = None

class ContentModerationSystem:
    """AI system for content moderation using TML framework"""
    
    def __init__(self):
        self.tml_evaluator = TMLEvaluator()
        self.moderation_log = []
        
        # Keyword patterns for different content types
        self.harmful_patterns = {
            "explicit_hate": [r"\b(kill|murder|die)\s+(all\s+)?(jews|muslims|blacks|whites|gays)", 
                            r"\b(burn|gas|lynch|hang)\s+.*\b(jews|muslims|blacks|whites|gays)"],
            "threats": [r"\bi\s+(will|am\s+going\s+to)\s+(kill|hurt|attack)", 
                       r"\byou\s+(will|are\s+going\s+to)\s+die"],
            "harassment": [r"\bkys\b", r"\bkill\s+yourself", r"\bgo\s+die"],
            "misinformation": [r"\bvaccines?\s+cause\s+autism", r"\bearth\s+is\s+flat",
                              r"\bcovid\s+is\s+(fake|hoax)", r"\belection\s+was\s+stolen"],
            "self_harm": [r"\bi\s+want\s+to\s+(die|kill\s+myself)", r"\bsuicide\s+methods?",
                         r"\bhow\s+to\s+(die|kill\s+myself)"]
        }
        
        self.sensitive_topics = [
            "abortion", "immigration", "gun_control", "climate_change", 
            "gender_identity", "racial_issues", "religious_extremism",
            "conspiracy_theories", "mental_health", "suicide"
        ]
    
    def moderate_content(self, content: Content) -> Dict[str, Any]:
        """
        Moderate content using TML framework
        
        Returns:
        - moderation_action: ModerationAction enum
        - moral_state: TML state for this decision
        - sacred_pause_engaged: Whether complex ethics required pause
        - reasoning: Detailed explanation of decision
        - confidence_score: How confident the system is (0.0-1.0)
        """
        
        # Analyze content for harmful patterns and complexity
        content_analysis = self._analyze_content(content)
        
        # Calculate moral complexity
        complexity_analysis = self._assess_moderation_complexity(content, content_analysis)
        
        # Create context for TML evaluation
        context = {
            "scenario": f"Moderate {content.content_type.value}: {content.text[:100]}...",
            "stakeholders": self._identify_stakeholders(content),
            "values_at_stake": ["safety", "free_speech", "dignity", "truth", "community_welfare"],
            "complexity_score": complexity_analysis["total_complexity"],
            "content_analysis": content_analysis,
            "user_context": {
                "follower_count": content.author.follower_count,
                "verification_status": content.author.verification_status,
                "previous_violations": content.author.previous_violations
            }
        }
        
        # Evaluate using TML framework
        evaluation_text = f"Content moderation: {content.content_type.value} with {content.report_count} reports"
        tml_result = self.tml_evaluator.evaluate(evaluation_text, context)
        
        # Generate moderation decision based on moral state
        if tml_result.state == TMLState.SACRED_PAUSE:
            decision = self._sacred_pause_moderation(content, content_analysis, tml_result)
        elif tml_result.state == TMLState.AFFIRMATION:
            decision = self._standard_moderation(content, content_analysis)
        else:  # RESISTANCE - content clearly violates policies
            decision = self._clear_violation_action(content, content_analysis)
        
        result = {
            "content_id": content.content_id,
            "moderation_action": decision["action"],
            "moral_state": tml_result.state,
            "sacred_pause_engaged": tml_result.state == TMLState.SACRED_PAUSE,
            "complexity_analysis": complexity_analysis,
            "content_analysis": content_analysis,
            "reasoning": decision["reasoning"],
            "confidence_score": decision["confidence"],
            "user_impact": decision.get("user_impact", "none"),
            "timestamp": datetime.now().isoformat(),
            "requires_human_review": decision.get("human_review", False)
        }
        
        # Log decision for audit
        self.moderation_log.append(result)
        
        return result
    
    def _analyze_content(self, content: Content) -> Dict[str, Any]:
        """Analyze content for harmful patterns and characteristics"""
        
        text_lower = content.text.lower()
        analysis = {
            "harmful_matches": {},
            "sensitive_topics": [],
            "content_characteristics": {},
            "risk_factors": []
        }
        
        # Check for harmful patterns
        for category, patterns in self.harmful_patterns.items():
            matches = []
            for pattern in patterns:
                if re.search(pattern, text_lower, re.IGNORECASE):
                    matches.append(pattern)
            if matches:
                analysis["harmful_matches"][category] = matches
        
        # Check for sensitive topics
        for topic in self.sensitive_topics:
            if topic.replace("_", " ") in text_lower:
                analysis["sensitive_topics"].append(topic)
        
        # Content characteristics
        analysis["content_characteristics"] = {
            "word_count": len(content.text.split()),
            "contains_caps": bool(re.search(r'[A-Z]{3,}', content.text)),
            "contains_profanity": self._contains_profanity(content.text),
            "engagement_velocity": self._calculate_engagement_velocity(content),
            "viral_potential": self._assess_viral_potential(content)
        }
        
        # Risk factors
        if content.author.previous_violations > 0:
            analysis["risk_factors"].append("previous_violations")
        if content.report_count > 10:
            analysis["risk_factors"].append("high_report_count")
        if content.author.account_age_days < 30:
            analysis["risk_factors"].append("new_account")
        if content.author.follower_count > 100000:
            analysis["risk_factors"].append("high_influence_account")
        
        return analysis
    
    def _assess_moderation_complexity(self, content: Content, analysis: Dict) -> Dict[str, float]:
        """Calculate moral complexity score for moderation decision"""
        
        # Factor 1: Harmful content severity
        harmful_severity = len(analysis["harmful_matches"]) / 5  # Max 5 categories
        
        # Factor 2: Context ambiguity (satirical, educational, news)
        context_factors = 0.0
        if content.content_category in [ContentCategory.SATIRICAL, ContentCategory.EDUCATIONAL, ContentCategory.NEWS]:
            context_factors = 0.7  # High complexity for contextual content
        
        # Factor 3: Sensitive topic involvement
        sensitive_factor = min(1.0, len(analysis["sensitive_topics"]) / 3)
        
        # Factor 4: Free speech vs. safety tension
        speech_tension = 0.8 if (analysis["harmful_matches"] and 
                               content.content_category == ContentCategory.POLITICAL) else 0.2
        
        # Factor 5: User influence and reach
        influence_factor = min(1.0, content.author.follower_count / 1000000)  # 1M+ followers = max
        
        # Factor 6: Engagement and viral potential
        viral_factor = analysis["content_characteristics"]["viral_potential"]
        
        # Factor 7: Cultural and contextual nuance
        cultural_factor = 0.6 if content.language != "en" else 0.2
        
        # Weighted combination
        total_complexity = (
            harmful_severity * 0.25 +
            context_factors * 0.20 +
            sensitive_factor * 0.15 +
            speech_tension * 0.15 +
            influence_factor * 0.10 +
            viral_factor * 0.10 +
            cultural_factor * 0.05
        )
        
        return {
            "total_complexity": total_complexity,
            "harmful_severity": harmful_severity,
            "context_ambiguity": context_factors,
            "sensitive_topics": sensitive_factor,
            "free_speech_tension": speech_tension,
            "user_influence": influence_factor,
            "viral_potential": viral_factor,
            "cultural_nuance": cultural_factor
        }
    
    def _identify_stakeholders(self, content: Content) -> List[str]:
        """Identify all stakeholders affected by moderation decision"""
        stakeholders = [
            "content_author", "platform_users", "advertiser_community", 
            "platform_company", "regulatory_bodies", "society"
        ]
        
        # Add specific stakeholder groups based on content
        if content.author.verification_status == "public_figure":
            stakeholders.append("public_discourse")
        
        if content.author.follower_count > 100000:
            stakeholders.append("influencer_ecosystem")
        
        if content.content_category == ContentCategory.NEWS:
            stakeholders.append("journalism_community")
        
        if content.content_category == ContentCategory.POLITICAL:
            stakeholders.append("democratic_institutions")
            
        return stakeholders
    
    def _sacred_pause_moderation(self, content: Content, analysis: Dict, tml_result: TMLEvaluation) -> Dict[str, Any]:
        """
        Complex moderation decision requiring Sacred Pause deliberation
        Balances free speech, safety, context, and platform responsibility
        """
        print(" Sacred Pause Engaged - Complex Content Moderation Ethics")
        print("⏱  Enhanced deliberation time: 2000ms")
        
        # Sacred Pause ethical considerations
        ethical_principles = [
            "Free Speech: Protect legitimate expression and diverse viewpoints",
            "User Safety: Prevent harm, harassment, and dangerous misinformation",
            "Context Sensitivity: Consider satirical, educational, or news context",
            "Cultural Awareness: Respect different cultural perspectives and norms", 
            "Platform Responsibility: Balance legal compliance with ethical duty",
            "Community Standards: Maintain healthy discourse environment"
        ]
        
        print(" Ethical Principles Under Consideration:")
        for principle in ethical_principles:
            print(f"   • {principle}")
        
        # Multi-factor decision analysis
        action_scores = self._score_moderation_actions(content, analysis)
        
        # Select action with highest ethical balance
        best_action = max(action_scores, key=action_scores.get)
        confidence = action_scores[best_action]
        
        # Generate detailed reasoning
        reasoning = self._generate_sacred_pause_reasoning(best_action, content, analysis, action_scores)
        
        # Determine if human review is needed
        human_review = (confidence < 0.7 or 
                       content.author.follower_count > 500000 or
                       "high_report_count" in analysis.get("risk_factors", []))
        
        return {
            "action": best_action,
            "confidence": confidence,
            "reasoning": reasoning,
            "human_review": human_review,
            "user_impact": self._assess_user_impact(best_action),
            "action_scores": {str(k): v for k, v in action_scores.items()}
        }
    
    def _score_moderation_actions(self, content: Content, analysis: Dict) -> Dict[ModerationAction, float]:
        """Score each possible moderation action across multiple ethical dimensions"""
        
        scores = {}
        
        # Factors for scoring
        has_harmful_content = bool(analysis["harmful_matches"])
        high_influence = content.author.follower_count > 100000
        educational_context = content.content_category == ContentCategory.EDUCATIONAL
        satirical_context = content.content_category == ContentCategory.SATIRICAL
        sensitive_topics = len(analysis["sensitive_topics"]) > 0
        
        # Score APPROVE
        approve_score = 0.8
        if has_harmful_content:
            approve_score -= 0.6
        if educational_context or satirical_context:
            approve_score += 0.2
        scores[ModerationAction.APPROVE] = max(0.0, approve_score)
        
        # Score REMOVE
        remove_score = 0.3
        if has_harmful_content:
            remove_score += 0.5
        if educational_context or satirical_context:
            remove_score -= 0.3
        if high_influence:
            remove_score += 0.1  # Higher stakes for influential accounts
        scores[ModerationAction.REMOVE] = max(0.0, remove_score)
        
        # Score WARNING LABEL
        warning_score = 0.6
        if sensitive_topics:
            warning_score += 0.3
        if has_harmful_content and (educational_context or satirical_context):
            warning_score += 0.2
        scores[ModerationAction.REQUIRE_WARNING_LABEL] = max(0.0, warning_score)
        
        # Score RESTRICT REACH
        restrict_score = 0.5
        if has_harmful_content and not educational_context:
            restrict_score += 0.3
        if high_influence:
            restrict_score += 0.1
        scores[ModerationAction.RESTRICT_REACH] = max(0.0, restrict_score)
        
        # Score ESCALATE TO HUMAN
        escalate_score = 0.4
        if sensitive_topics and high_influence:
            escalate_score += 0.4
        if educational_context and has_harmful_content:
            escalate_score += 0.3
        scores[ModerationAction.ESCALATE_TO_HUMAN] = max(0.0, escalate_score)
        
        return scores
    
    def _standard_moderation(self, content: Content, analysis: Dict) -> Dict[str, Any]:
        """Standard moderation for clear-cut cases (no Sacred Pause needed)"""
        
        # Simple rule-based moderation
        if analysis["harmful_matches"]:
            if "explicit_hate" in analysis["harmful_matches"] or "threats" in analysis["harmful_matches"]:
                action = ModerationAction.REMOVE
                confidence = 0.95
            elif "harassment" in analysis["harmful_matches"]:
                action = ModerationAction.WARN_USER
                confidence = 0.85
            else:
                action = ModerationAction.REQUIRE_WARNING_LABEL
                confidence = 0.80
        else:
            action = ModerationAction.APPROVE
            confidence = 0.90
        
        reasoning = f"Standard content policy application. "
        if analysis["harmful_matches"]:
            reasoning += f"Detected harmful patterns: {list(analysis['harmful_matches'].keys())}. "
        reasoning += f"Action: {action.value.replace('_', ' ').title()}."
        
        return {
            "action": action,
            "confidence": confidence,
            "reasoning": reasoning,
            "human_review": False,
            "user_impact": self._assess_user_impact(action)
        }
    
    def _clear_violation_action(self, content: Content, analysis: Dict) -> Dict[str, Any]:
        """Handle clear policy violations (RESISTANCE state)"""
        
        # Severe violations get immediate action
        if ("explicit_hate" in analysis["harmful_matches"] or 
            "threats" in analysis["harmful_matches"]):
            if content.author.previous_violations > 2:
                action = ModerationAction.PERMANENT_BAN
            else:
                action = ModerationAction.TEMPORARY_SUSPEND
        else:
            action = ModerationAction.REMOVE
        
        reasoning = f"Clear policy violation detected. Harmful content patterns: " \
                   f"{list(analysis['harmful_matches'].keys())}. Immediate action required."
        
        return {
            "action": action,
            "confidence": 0.98,
            "reasoning": reasoning,
            "human_review": action == ModerationAction.PERMANENT_BAN,
            "user_impact": self._assess_user_impact(action)
        }
    
    def _generate_sacred_pause_reasoning(self, action: ModerationAction, content: Content, 
                                       analysis: Dict, scores: Dict) -> str:
        """Generate detailed reasoning for Sacred Pause moderation decisions"""
        
        reasoning = " SACRED PAUSE MODERATION ANALYSIS:\n\n"
        reasoning += "This content triggered enhanced ethical deliberation due to:\n"
        reasoning += f"• Complex balance between free speech and user safety\n"
        reasoning += f"• Contextual ambiguity requiring nuanced interpretation\n"
        reasoning += f"• Significant potential impact on community discourse\n"
        reasoning += f"• Multiple ethical frameworks in tension\n\n"
        
        reasoning += f"SELECTED ACTION: {action.value.replace('_', ' ').title()}\n\n"
        
        # Content analysis summary
        reasoning += "CONTENT ANALYSIS:\n"
        if analysis["harmful_matches"]:
            reasoning += f"• Harmful patterns detected: {list(analysis['harmful_matches'].keys())}\n"
        if analysis["sensitive_topics"]:
            reasoning += f"• Sensitive topics: {', '.join(analysis['sensitive_topics'])}\n"
        reasoning += f"• Content category: {content.content_category.value if content.content_category else 'uncategorized'}\n"
        reasoning += f"• Author influence: {content.author.follower_count:,} followers\n"
        reasoning += f"• Report count: {content.report_count}\n\n"
        
        # Ethical framework scores
        reasoning += "ACTION EVALUATION SCORES:\n"
        for act, score in scores.items():
            reasoning += f"• {act.value.replace('_', ' ').title()}: {score:.3f}\n"
        
        reasoning += f"\nETHICAL CONSIDERATIONS BALANCED:\n"
        reasoning += f"1. Free Speech Protection: Preserving legitimate discourse\n"
        reasoning += f"2. User Safety: Preventing harm and harassment\n"
        reasoning += f"3. Context Sensitivity: Educational/satirical value consideration\n"
        reasoning += f"4. Platform Responsibility: Community standards enforcement\n"
        reasoning += f"5. Proportional Response: Matching action to violation severity\n"
        
        return reasoning
    
    def _contains_profanity(self, text: str) -> bool:
        """Simple profanity detection"""
        profane_words = ["fuck", "shit", "damn", "bitch", "asshole"]  # Simplified list
        return any(word in text.lower() for word in profane_words)
    
    def _calculate_engagement_velocity(self, content: Content) -> float:
        """Calculate how quickly content is gaining engagement"""
        if not content.timestamp:
            return 0.0
        
        hours_since_post = (datetime.now() - content.timestamp).total_seconds() / 3600
        if hours_since_post == 0:
            return 0.0
        
        total_engagement = sum(content.engagement_metrics.values())
        return total_engagement / hours_since_post
    
    def _assess_viral_potential(self, content: Content) -> float:
        """Assess potential for content to go viral"""
        engagement_rate = sum(content.engagement_metrics.values()) / max(1, content.author.follower_count)
        viral_score = min(1.0, engagement_rate * 10)  # Normalize
        
        # Boost for controversial content
        if content.report_count > 5:
            viral_score += 0.2
        
        return min(1.0, viral_score)
    
    def _assess_user_impact(self, action: ModerationAction) -> str:
        """Assess impact of moderation action on user"""
        impact_map = {
            ModerationAction.APPROVE: "none",
            ModerationAction.REQUIRE_WARNING_LABEL: "minimal",
            ModerationAction.RESTRICT_REACH: "moderate",
            ModerationAction.WARN_USER: "moderate",
            ModerationAction.REMOVE: "significant",
            ModerationAction.TEMPORARY_SUSPEND: "severe",
            ModerationAction.PERMANENT_BAN: "extreme",
            ModerationAction.ESCALATE_TO_HUMAN: "pending"
        }
        return impact_map.get(action, "unknown")
    
    def get_moderation_history(self) -> List[Dict]:
        """Return audit trail of all moderation decisions"""
        return self.moderation_log
    
    def export_decisions(self, filename: str) -> None:
        """Export moderation log to JSON file for audit/analysis"""
        with open(filename, 'w') as f:
            json.dump(self.moderation_log, f, indent=2, default=str)


def demo_content_moderation():
    """Demonstration of content moderation system with various complexity scenarios"""
    
    print(" Content Moderation AI System - TML Framework Demo")
    print("=" * 55)
    
    moderation_system = ContentModerationSystem()
    
    # Test user accounts
    regular_user = User("user_001", 25, 500, 365, 0, "unverified", "US")
    influencer = User("user_002", 30, 2000000, 1200, 1, "verified", "US") 
    new_user = User("user_003", 19, 50, 15, 0, "unverified", "UK")
    
    # Scenario 1: Clear harmful content (should be RESISTANCE)
    print("\n SCENARIO 1: Clear Policy Violation (Low Complexity)")
    print("-" * 45)
    
    harmful_content = Content(
        content_id="post_001",
        content_type=ContentType.TEXT_POST,
        text="All Muslims should die and burn in hell. Kill them all!",
        author=regular_user,
        engagement_metrics={"likes": 50, "shares": 20, "comments": 30},
        report_count=25
    )
    
    result1 = moderation_system.moderate_content(harmful_content)
    print(f"Action: {result1['moderation_action'].value}")
    print(f"Moral State: {result1['moral_state'].value}")
    print(f"Sacred Pause: {result1['sacred_pause_engaged']}")
    print(f"Complexity: {result1['complexity_analysis']['total_complexity']:.3f}")
    
    # Scenario 2: Satirical content with sensitive topics (should trigger Sacred Pause)
    print("\n SCENARIO 2: Satirical Content with Sensitive Topics (High Complexity)")
    print("-" * 65)
    
    satirical_content = Content(
        content_id="post_002",
        content_type=ContentType.TEXT_POST,
        text="Breaking: Local man discovers that vaccines cause adults. Scientists baffled by this groundbreaking research showing 100% correlation between childhood vaccines and becoming grown-ups.",
        author=influencer,
        engagement_metrics={"likes": 15000, "shares": 8000, "comments": 2000},
        report_count=500,
        content_category=ContentCategory.SATIRICAL,
        contains_sensitive_topics=["vaccines", "misinformation"],
        timestamp=datetime.now()
    )
    
    result2 = moderation_system.moderate_content(satirical_content)
    print(f"Action: {result2['moderation_action'].value}")
    print(f"Moral State: {result2['moral_state'].value}")
    print(f"Sacred Pause: {result2['sacred_pause_engaged']}")
    print(f"Complexity: {result2['complexity_analysis']['total_complexity']:.3f}")
    print(f"Human Review Required: {result2['requires_human_review']}")
    
    if result2['sacred_pause_engaged']:
        print(f"\n Sacred Pause Reasoning:")
        print(result2['reasoning'])
    
    # Scenario 3: Educational content about sensitive topics
    print("\n SCENARIO 3: Educational Content on Sensitive Topics")
    print("-" * 50)
    
    educational_content = Content(
        content_id="post_003",
        content_type=ContentType.TEXT_POST,
        text="Mental health awareness: If you're having thoughts of self-harm, please reach out. Here are suicide prevention resources and warning signs to watch for in friends and family.",
        author=User("health_org", 35, 500000, 2000, 0, "verified", "US"),
        engagement_metrics={"likes": 25000, "shares": 15000, "comments": 3000},
        report_count=50,
        content_category=ContentCategory.EDUCATIONAL,
        contains_sensitive_topics=["mental_health", "suicide"]
    )
    
    result3 = moderation_system.moderate_content(educational_content)
    print(f"Action: {result3['moderation_action'].value}")
    print(f"Moral State: {result3['moral_state'].value}")
    print(f"Sacred Pause: {result3['sacred_pause_engaged']}")
    print(f"Complexity: {result3['complexity_analysis']['total_complexity']:.3f}")
    
    # Export audit trail
    moderation_system.export_decisions("content_moderation_audit.json")
    print(f"\n Moderation audit trail exported to: content_moderation_audit.json")
    
    print(f"\n Demo completed! TML framework moderated {len(moderation_system.moderation_log)} content items.")
    print("Sacred Pause engaged for complex ethical scenarios requiring nuanced judgment.")


if __name__ == "__main__":
    demo_content_moderation()

# Created by Lev Goukassian • ORCID: 0009-0006-5966-1243 • Email: leogouk@gmail.com • Successor Contact: support@tml-goukassian.org • [see Succession Charter](/TML-SUCCESSION-CHARTER.md)
