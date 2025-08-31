"""
Ternary Moral Logic (TML) Framework
Sacred Pause Logging Infrastructure for AI Accountability

Post-audit investigation model where organizations control thresholds
and TML provides mandatory logging infrastructure.
"""

__version__ = "2.0.0-TRANSITION"
__author__ = "Lev Goukassian"
__email__ = "leogouk@gmail.com"
__license__ = "MIT with Mandatory Logging"

from .core import (
    TMLFramework,
    TernaryState,
    BatchLogger,
    verify_tml_compliance,
    PatternCategory,
    ImmutableStorage
)

# Quick setup function for standard configuration
def create_tml_framework(
    sprl_threshold=0.7,
    domain="general",
    calculate_risk_on="all",
    retention_days=None,
    risk_categories=None,
    stakeholder_methodology=None
):
    """
    Quick setup function for TML Framework
    
    Organizations control ALL decision thresholds and risk calculations.
    TML only mandates logging infrastructure and minimum retention periods.
    
    Args:
        sprl_threshold: YOUR Sacred Pause trigger threshold (0-1)
                       This is YOUR decision based on YOUR domain expertise
        domain: Application domain (affects only retention requirements)
        calculate_risk_on: When YOU want to evaluate risk (all, samples, threshold)
        retention_days: Log retention period (must meet legal minimums)
        risk_categories: YOUR domain-specific risk definitions (optional)
        stakeholder_methodology: YOUR method for identifying affected parties
    
    Returns:
        Configured TMLFramework instance
    
    Examples:
        # Medical organization might choose high sensitivity
        framework = create_tml_framework(
            sprl_threshold=0.3,  # Their choice for medical caution
            domain="medical"
        )
        
        # Financial organization might choose different threshold
        framework = create_tml_framework(
            sprl_threshold=0.7,  # Their choice for financial operations
            domain="financial"
        )
        
        # Each organization decides what works for them
    """
    # MANDATORY: Minimum retention for legal/regulatory compliance
    # These are MINIMUMS for evidence preservation, not suggestions
    minimum_retention = {
        'medical': 3650,    # 10 years - medical record requirements
        'financial': 2555,  # 7 years - financial audit requirements
        'autonomous': 1825, # 5 years - accident investigation requirements
        'general': 1095     # 3 years - general evidence preservation
    }
    
    if retention_days is None:
        retention_days = minimum_retention.get(domain, 1095)
    elif retention_days < minimum_retention.get(domain, 1095):
        raise ValueError(
            f"Retention period must be at least {minimum_retention.get(domain, 1095)} "
            f"days for {domain} domain (legal requirement)"
        )
    
    # Organization's configuration - COMPLETELY under their control
    config = {
        'sprl_threshold': sprl_threshold,  # Organization decides
        'risk_categories': risk_categories or {},  # Organization defines
        'stakeholder_methodology': stakeholder_methodology or 'organization_defined',
        'calculate_risk_on': calculate_risk_on,  # Organization's choice
        'retention_days': retention_days,
        'domain': domain
    }
    
    return TMLFramework(config)


# Example configurations (NOT prescriptions)
class ExampleConfigurations:
    """
    EXAMPLE configurations showing how organizations MIGHT implement TML.
    These are NOT requirements or recommendations, just illustrations.
    
    Each organization must determine appropriate thresholds for their domain,
    risk tolerance, and operational requirements.
    """
    
    @staticmethod
    def get_example_config(domain):
        """
        Get an EXAMPLE configuration for demonstration purposes.
        
        WARNING: These are NOT recommended values. Each organization must
        determine appropriate settings based on their expertise, risk analysis,
        and operational requirements.
        
        Args:
            domain: Domain for example ('medical', 'financial', 'autonomous')
            
        Returns:
            Dict with EXAMPLE configuration (not for production use)
        """
        examples = {
            'medical': {
                'description': 'Example: Conservative medical setting',
                'sprl_threshold': 0.3,  # Low threshold example
                'note': 'Medical organizations must determine appropriate thresholds'
            },
            'financial': {
                'description': 'Example: Balanced financial setting',
                'sprl_threshold': 0.6,  # Medium threshold example
                'note': 'Financial institutions must assess their own risk tolerance'
            },
            'autonomous': {
                'description': 'Example: Safety-critical autonomous system',
                'sprl_threshold': 0.4,  # Safety-focused example
                'note': 'Autonomous system developers must evaluate safety requirements'
            },
            'general': {
                'description': 'Example: General purpose AI',
                'sprl_threshold': 0.7,  # Higher threshold example
                'note': 'Each application requires domain-specific calibration'
            }
        }
        
        example = examples.get(domain, examples['general'])
        example['warning'] = (
            "This is an EXAMPLE only. Do not use in production. "
            "Your organization must determine appropriate values."
        )
        
        return example


# Convenience decorators for adding TML to existing systems
def tml_protected(sprl_threshold=None, domain="general", **kwargs):
    """
    Decorator to add TML logging to existing functions
    
    Organizations must specify their own threshold - no defaults imposed.
    
    Args:
        sprl_threshold: YOUR threshold for Sacred Pause (required)
        domain: Your domain (affects only retention requirements)
        **kwargs: Additional configuration you want to pass
    
    Usage:
        @tml_protected(sprl_threshold=0.6)  # Your threshold
        def make_decision(data):
            # your existing decision logic
            return decision
    """
    if sprl_threshold is None:
        raise ValueError(
            "You must specify sprl_threshold. "
            "TML does not impose default thresholds - this is your decision."
        )
    
    def decorator(func):
        framework = create_tml_framework(sprl_threshold, domain, **kwargs)
        
        def wrapper(*args, **kwargs):
            # Extract context from function arguments
            context = {
                'function': func.__name__,
                'args': args,
                'kwargs': kwargs,
                'domain': domain
            }
            
            # Process with TML
            result = framework.process_decision(
                context=context,
                ai_decision_func=lambda c: func(*args, **kwargs)
            )
            
            # Return original function result
            return result['decision']
        
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.tml_framework = framework  # Expose framework for inspection
        
        return wrapper
    
    return decorator


# Async version for high-performance systems
def tml_protected_async(sprl_threshold=None, domain="general", **kwargs):
    """
    Async decorator for TML logging without blocking
    
    Organizations must specify their own threshold - no defaults imposed.
    
    Args:
        sprl_threshold: YOUR threshold for Sacred Pause (required)
        domain: Your domain (affects only retention requirements)
        **kwargs: Additional configuration you want to pass
    
    Usage:
        @tml_protected_async(sprl_threshold=0.8)  # Your threshold
        async def process_transaction(data):
            # your async decision logic
            return await decision
    """
    if sprl_threshold is None:
        raise ValueError(
            "You must specify sprl_threshold. "
            "TML does not impose default thresholds - this is your decision."
        )
    
    def decorator(func):
        framework = create_tml_framework(sprl_threshold, domain, **kwargs)
        
        async def wrapper(*args, **kwargs):
            context = {
                'function': func.__name__,
                'args': args,
                'kwargs': kwargs,
                'domain': domain
            }
            
            # Process with async TML
            result = await framework.process_decision_async(
                context=context,
                ai_decision_func=lambda c: func(*args, **kwargs)
            )
            
            return result['decision']
        
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.tml_framework = framework
        
        return wrapper
    
    return decorator


# Compliance checking utilities
class ComplianceChecker:
    """
    Utility class for verifying TML infrastructure compliance.
    
    Checks ONLY infrastructure requirements, not organizational decisions.
    Your thresholds and risk calculations are YOUR responsibility.
    """
    
    @staticmethod
    def check_framework(framework):
        """
        Check TML infrastructure compliance (not threshold appropriateness)
        
        This verifies:
        - Logging infrastructure is present
        - Retention meets legal minimums
        - Audit trail is immutable
        - Investigation API works
        
        This does NOT judge:
        - Whether your SPRL threshold is appropriate
        - Whether your risk calculation is correct
        - Whether your stakeholder mapping is complete
        
        Returns:
            Dict with infrastructure compliance status
        """
        issues = []
        warnings = []
        info = []
        
        # Check MANDATORY infrastructure capabilities
        if not framework.logging_enabled:
            issues.append("Logging capability is disabled (MANDATORY)")
        if not framework.audit_immutable:
            issues.append("Audit trail is not immutable (MANDATORY)")
        if not framework.investigation_api:
            issues.append("Investigation API is not available (MANDATORY)")
        
        # Check that threshold exists (not whether it's "correct")
        if framework.sprl_threshold is None:
            issues.append("No SPRL threshold configured (you must set one)")
        elif framework.sprl_threshold < 0 or framework.sprl_threshold > 1:
            issues.append(f"Invalid SPRL threshold: {framework.sprl_threshold} (must be 0-1)")
        else:
            info.append(f"SPRL threshold: {framework.sprl_threshold} (your choice)")
        
        # Check MANDATORY retention minimums
        min_retention = {
            'medical': 3650,
            'financial': 2555,
            'autonomous': 1825,
            'general': 1095
        }
        
        domain = getattr(framework, 'domain', 'general')
        required_retention = min_retention.get(domain, 1095)
        
        if framework.retention_days < required_retention:
            issues.append(
                f"Retention period ({framework.retention_days} days) "
                f"below legal minimum for {domain} domain ({required_retention} days)"
            )
        
        # Performance info (not compliance issues)
        stats = framework.get_performance_report()
        if stats['average_logging_time_ms'] > 100:
            warnings.append(
                f"High logging latency: {stats['average_logging_time_ms']:.1f}ms "
                "(consider optimization)"
            )
        
        # Verify integrity
        if not framework.immutable_storage.verify_integrity():
            issues.append("Audit trail integrity verification failed")
        
        return {
            'infrastructure_compliant': len(issues) == 0,
            'issues': issues,
            'warnings': warnings,
            'info': info,
            'stats': stats,
            'note': (
                "This checks TML infrastructure only. "
                "Your organization is responsible for appropriate thresholds."
            )
        }
    
    @staticmethod
    def generate_compliance_report(framework):
        """
        Generate infrastructure compliance report.
        
        Reports on infrastructure compliance, not threshold appropriateness.
        """
        check = ComplianceChecker.check_framework(framework)
        stats = framework.get_performance_report()
        
        report = f"""
TML INFRASTRUCTURE COMPLIANCE REPORT
Generated: {__import__('datetime').datetime.now().isoformat()}

INFRASTRUCTURE STATUS: {'✓ COMPLIANT' if check['infrastructure_compliant'] else '✗ NON-COMPLIANT'}

Note: This verifies TML infrastructure only. Your organization is responsible
for determining appropriate SPRL thresholds and risk calculations.

YOUR CONFIGURATION:
- SPRL Threshold: {framework.sprl_threshold} (your choice)
- Retention Period: {framework.retention_days} days
- Risk Calculation: {framework.calculate_risk_on}

INFRASTRUCTURE PERFORMANCE:
- Total Decisions: {stats['total_decisions']}
- Sacred Pause Triggers: {stats['sacred_pause_triggers']} ({stats['trigger_rate']:.1f}%)
- Average Log Time: {stats['average_logging_time_ms']:.1f}ms
- Storage Optimization: {stats['storage_optimization']}
- Integrity Verified: {stats['integrity_verified']}

"""
        
        if check['issues']:
            report += "INFRASTRUCTURE ISSUES (must fix):\n"
            for issue in check['issues']:
                report += f"  ✗ {issue}\n"
        
        if check['warnings']:
            report += "\nPERFORMANCE WARNINGS (consider addressing):\n"
            for warning in check['warnings']:
                report += f"  ⚠ {warning}\n"
        
        if check['info']:
            report += "\nYOUR SETTINGS:\n"
            for item in check['info']:
                report += f"  ℹ {item}\n"
        
        report += "\n" + check['note']
        
        return report


# Integration guide
class IntegrationGuide:
    """
    Guidance for organizations implementing TML.
    
    These are suggestions to consider, not requirements to follow.
    Your organization must make decisions based on your domain expertise.
    """
    
    @staticmethod
    def get_integration_steps():
        """Get suggested integration steps (advisory only)"""
        return """
SUGGESTED TML INTEGRATION STEPS (Advisory Only)

1. ASSESS your domain requirements
   - What decisions does your AI make?
   - Who are your stakeholders?
   - What are your risk factors?
   
2. DETERMINE your thresholds (this is YOUR decision)
   - Low threshold = more logging, more accountability
   - High threshold = less logging, more efficiency
   - Only YOU know the right balance for your domain
   
3. IMPLEMENT the infrastructure
   - Add TML logging capability
   - Ensure retention meets legal minimums
   - Test investigation access
   
4. VALIDATE your choices
   - Monitor trigger rates
   - Adjust based on YOUR experience
   - Document YOUR rationale

Remember: TML provides infrastructure. You provide judgment.
"""


# Export all public components
__all__ = [
    # Core framework
    'TMLFramework',
    'TernaryState',
    'BatchLogger',
    'PatternCategory',
    'ImmutableStorage',
    
    # Setup utilities
    'create_tml_framework',
    'verify_tml_compliance',
    
    # Decorators
    'tml_protected',
    'tml_protected_async',
    
    # Compliance
    'ComplianceChecker',
    
    # Guidance (advisory only)
    'ExampleConfigurations',
    'IntegrationGuide',
    
    # Metadata
    '__version__',
    '__author__',
    '__email__',
    '__license__'
]

"""
Contact Information
- Email: leogouk@gmail.com 
- Successor Contact: support@tml-goukassian.org 
- See Succession Charter: /TML-SUCCESSION-CHARTER.md
"""
