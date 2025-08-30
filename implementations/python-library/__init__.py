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
    retention_days=None
):
    """
    Quick setup function for TML Framework
    
    Args:
        sprl_threshold: Organization's Sacred Pause trigger threshold (0-1)
        domain: Application domain (medical, financial, autonomous, general)
        calculate_risk_on: When to evaluate risk (all, samples, threshold)
        retention_days: Log retention period (uses domain defaults if None)
    
    Returns:
        Configured TMLFramework instance
    """
    # Domain-specific retention requirements
    domain_retention = {
        'medical': 3650,    # 10 years
        'financial': 2555,  # 7 years  
        'autonomous': 1825, # 5 years
        'general': 1095     # 3 years
    }
    
    if retention_days is None:
        retention_days = domain_retention.get(domain, 1095)
    
    # Standard risk categories by domain
    risk_categories = {
        'medical': {
            'life_threatening': 1.0,
            'treatment_affecting': 0.8,
            'diagnostic': 0.6,
            'administrative': 0.3
        },
        'financial': {
            'large_transaction': 0.9,
            'credit_decision': 0.7,
            'investment': 0.6,
            'inquiry': 0.2
        },
        'autonomous': {
            'safety_critical': 1.0,
            'navigation': 0.5,
            'comfort': 0.2,
            'entertainment': 0.1
        },
        'general': {
            'high': 0.8,
            'medium': 0.5,
            'low': 0.2
        }
    }
    
    config = {
        'sprl_threshold': sprl_threshold,
        'risk_categories': risk_categories.get(domain, risk_categories['general']),
        'stakeholder_methodology': 'standard',
        'calculate_risk_on': calculate_risk_on,
        'retention_days': retention_days,
        'domain': domain
    }
    
    return TMLFramework(config)


# Convenience decorators for adding TML to existing systems
def tml_protected(sprl_threshold=0.7, domain="general"):
    """
    Decorator to add TML logging to existing functions
    
    Usage:
        @tml_protected(sprl_threshold=0.6, domain="medical")
        def make_medical_decision(patient_data):
            # existing decision logic
            return decision
    """
    def decorator(func):
        framework = create_tml_framework(sprl_threshold, domain)
        
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
def tml_protected_async(sprl_threshold=0.7, domain="general"):
    """
    Async decorator for TML logging without blocking
    
    Usage:
        @tml_protected_async(sprl_threshold=0.8)
        async def process_transaction(data):
            # async decision logic
            return await decision
    """
    def decorator(func):
        framework = create_tml_framework(sprl_threshold, domain)
        
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
    """Utility class for verifying TML compliance"""
    
    @staticmethod
    def check_framework(framework):
        """
        Comprehensive compliance check
        
        Returns:
            Dict with compliance status and any issues found
        """
        issues = []
        warnings = []
        
        # Check mandatory capabilities
        if not framework.logging_enabled:
            issues.append("Logging capability is disabled")
        if not framework.audit_immutable:
            issues.append("Audit trail is not immutable")
        if not framework.investigation_api:
            issues.append("Investigation API is not available")
        
        # Check configuration
        if framework.sprl_threshold is None:
            issues.append("SPRL threshold not configured")
        elif framework.sprl_threshold < 0 or framework.sprl_threshold > 1:
            issues.append(f"Invalid SPRL threshold: {framework.sprl_threshold}")
        
        # Check retention
        min_retention = {
            'medical': 3650,
            'financial': 2555,
            'autonomous': 1825,
            'general': 1095
        }
        
        domain = framework.risk_categories.get('domain', 'general')
        required_retention = min_retention.get(domain, 1095)
        
        if framework.retention_days < required_retention:
            issues.append(
                f"Retention period ({framework.retention_days} days) "
                f"below minimum for {domain} domain ({required_retention} days)"
            )
        
        # Check performance
        stats = framework.get_performance_report()
        if stats['average_logging_time_ms'] > 100:
            warnings.append(
                f"High logging latency: {stats['average_logging_time_ms']:.1f}ms"
            )
        
        # Verify integrity
        if not framework.immutable_storage.verify_integrity():
            issues.append("Audit trail integrity verification failed")
        
        return {
            'compliant': len(issues) == 0,
            'issues': issues,
            'warnings': warnings,
            'stats': stats
        }
    
    @staticmethod
    def generate_compliance_report(framework):
        """Generate detailed compliance report"""
        check = ComplianceChecker.check_framework(framework)
        stats = framework.get_performance_report()
        
        report = f"""
TML COMPLIANCE REPORT
Generated: {__import__('datetime').datetime.now().isoformat()}

COMPLIANCE STATUS: {'✓ COMPLIANT' if check['compliant'] else '✗ NON-COMPLIANT'}

CONFIGURATION:
- SPRL Threshold: {framework.sprl_threshold}
- Retention Period: {framework.retention_days} days
- Risk Calculation: {framework.calculate_risk_on}

PERFORMANCE:
- Total Decisions: {stats['total_decisions']}
- Sacred Pause Triggers: {stats['sacred_pause_triggers']} ({stats['trigger_rate']:.1f}%)
- Average Log Time: {stats['average_logging_time_ms']:.1f}ms
- Storage Optimization: {stats['storage_optimization']}
- Integrity Verified: {stats['integrity_verified']}

"""
        
        if check['issues']:
            report += "CRITICAL ISSUES:\n"
            for issue in check['issues']:
                report += f"  ✗ {issue}\n"
        
        if check['warnings']:
            report += "\nWARNINGS:\n"
            for warning in check['warnings']:
                report += f"  ⚠ {warning}\n"
        
        return report


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
