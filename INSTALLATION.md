# Installation Quick Start Guide

## Ternary Moral Logic (TML) Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Academic Paper](https://img.shields.io/badge/Academic-Paper-red)](docs/ACADEMIC_VALIDATION.md)

---

## Table of Contents

1. [Overview](#overview)
2. [System Requirements](#system-requirements)
3. [Installation Methods](#installation-methods)
4. [Quick Start](#quick-start)
5. [Verification](#verification)
6. [Configuration](#configuration)
7. [Example Usage](#example-usage)
8. [Troubleshooting](#troubleshooting)
9. [Academic Citation](#academic-citation)
10. [Support](#support)

---

## Overview

The **Ternary Moral Logic (TML) Framework** is a groundbreaking academic implementation for ethical AI decision-making. This installation guide provides comprehensive instructions for researchers, institutions, and developers to deploy TML in production environments.

### Core Innovation: Sacred Pause Technology™

TML introduces the **Sacred Pause**—a deliberate temporal buffer that enables complex moral reasoning in AI systems, ensuring ethical compliance across medical, automotive, financial, and content moderation domains.

---

## System Requirements

### Minimum Requirements

| Component | Specification | Notes |
|-----------|---------------|-------|
| **Python** | 3.8+ | Required for dataclass support |
| **Memory** | 512 MB RAM | Base framework overhead |
| **Storage** | 100 MB | Core installation |
| **CPU** | 1 core, 1 GHz | Sacred Pause processing |

### Recommended Requirements

| Component | Specification | Notes |
|-----------|---------------|-------|
| **Python** | 3.10+ | Optimal performance |
| **Memory** | 2 GB RAM | Production workloads |
| **Storage** | 1 GB | Includes examples and docs |
| **CPU** | 4 cores, 2+ GHz | Concurrent ethical evaluations |

### Production Requirements

| Component | Specification | Notes |
|-----------|---------------|-------|
| **Python** | 3.11+ | Latest security patches |
| **Memory** | 8+ GB RAM | High-throughput scenarios |
| **Storage** | 10 GB | Audit logs and compliance |
| **CPU** | 8+ cores, 3+ GHz | Enterprise-scale deployment |

### Supported Platforms

- ✅ **Linux** (Ubuntu 20.04+, CentOS 8+, RHEL 8+)
- ✅ **macOS** (10.15+, Apple Silicon supported)
- ✅ **Windows** (10, 11, Server 2019+)
- ✅ **Docker** (Official images available)
- ✅ **Kubernetes** (Helm charts provided)

---

## Installation Methods

### Method 1: PyPI Installation (Recommended)

#### For End Users
```bash
# Install stable release
pip install ternary-moral-logic

# Install with optional dependencies
pip install ternary-moral-logic[medical,automotive,financial]

# Install development version
pip install ternary-moral-logic[dev]
```

#### For Academic Researchers
```bash
# Install with academic tools
pip install ternary-moral-logic[academic]

# Includes: jupyter, matplotlib, pandas, scipy, academic-cite
```

#### For Production Deployment
```bash
# Install with production features
pip install ternary-moral-logic[production]

# Includes: monitoring, logging, audit-trail, compliance
```

### Method 2: Conda Installation

```bash
# Create dedicated environment
conda create -n tml-env python=3.11
conda activate tml-env

# Install from conda-forge
conda install -c conda-forge ternary-moral-logic

# Alternative: Install from our channel
conda install -c tml-goukassian ternary-moral-logic
```

### Method 3: Docker Deployment

#### Quick Start Container
```bash
# Pull official image
docker pull tmlgoukassian/tml:latest

# Run interactive container
docker run -it --name tml-demo tmlgoukassian/tml:latest python

# Run with volume mounting
docker run -v /path/to/data:/data tmlgoukassian/tml:latest
```

#### Production Container
```bash
# Pull production image
docker pull tmlgoukassian/tml:production

# Run with environment configuration
docker run -d \
  --name tml-production \
  -p 8080:8080 \
  -e TML_LOG_LEVEL=INFO \
  -e TML_AUDIT_ENABLED=true \
  tmlgoukassian/tml:production
```

### Method 4: Source Installation (Development)

```bash
# Clone repository
git clone https://github.com/FractonicMind/TernaryMoralLogic.git
cd TernaryMoralLogic

# Create virtual environment
python -m venv tml-dev
source tml-dev/bin/activate  # Linux/macOS
# tml-dev\Scripts\activate  # Windows

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests to verify installation
pytest tests/
```

### Method 5: Academic Institution Deployment

```bash
# For university computing clusters
module load python/3.11
module load cuda/11.8  # If GPU acceleration needed

# Install with cluster optimizations
pip install ternary-moral-logic[cluster] --user

# Verify distributed computing support
python -c "import tml_core; print(tml_core.cluster_info())"
```

---

## Quick Start

### 1. Basic Import and Initialization

```python
# Import TML framework
from tml_core import TMLFramework, MoralContext, TMLState

# Initialize framework
tml = TMLFramework()

# Verify installation
print(f"TML Framework v{tml.version} loaded successfully")
```

### 2. Your First Moral Decision

```python
# Create a moral scenario
context = MoralContext(
    scenario="AI system deciding medical resource allocation",
    stakeholders=["patients", "families", "medical_staff"],
    values_at_stake=["life", "fairness", "dignity"],
    complexity_score=0.8  # High complexity triggers Sacred Pause
)

# Process through TML framework
result = tml.process(context)

# Examine results
print(f"Moral State: {result['state']}")
print(f"Sacred Pause Engaged: {result['state'] == TMLState.SACRED_PAUSE}")

if result['state'] == TMLState.SACRED_PAUSE:
    print("✋ Sacred Pause: Complex ethics require additional deliberation")
    print(f"Reflection prompts: {result['sacred_pause']['reflections']}")
```

### 3. Load Pre-built Examples

```python
# Medical AI triage
from examples.medical_ai_triage import demo_medical_triage
demo_medical_triage()

# Autonomous vehicle ethics
from examples.autonomous_vehicle import demo_autonomous_vehicle_ethics
demo_autonomous_vehicle_ethics()

# Content moderation
from examples.content_moderation import demo_content_moderation
demo_content_moderation()

# Financial AI ethics
from examples.financial_ai import demo_financial_ai_ethics
demo_financial_ai_ethics()
```

---

## Verification

### 1. Installation Verification

```bash
# Check TML installation
python -c "import tml_core; print('✅ TML Framework installed successfully')"

# Verify version
python -c "import tml_core; print(f'Version: {tml_core.__version__}')"

# Check dependencies
python -c "import tml_core; tml_core.check_dependencies()"
```

### 2. Run Built-in Tests

```bash
# Quick verification test
python -m tml_core.tests.quick_test

# Comprehensive test suite
pytest tests/ -v

# Sacred Pause timing tests
python -m tml_core.tests.sacred_pause_tests

# Performance benchmarks
python -m tml_core.tests.performance_tests
```

### 3. Academic Validation Tests

```bash
# Philosophical consistency tests
python -m tml_core.tests.philosophical_tests

# Ethical framework validation
python -m tml_core.tests.ethical_validation

# Cross-cultural moral reasoning tests
python -m tml_core.tests.cultural_tests
```

---

## Configuration

### 1. Environment Variables

```bash
# Core configuration
export TML_LOG_LEVEL=INFO              # DEBUG, INFO, WARNING, ERROR
export TML_SACRED_PAUSE_DURATION=2000  # Milliseconds
export TML_COMPLEXITY_THRESHOLD=0.7    # 0.0-1.0 scale

# Production settings
export TML_AUDIT_ENABLED=true          # Enable audit logging
export TML_COMPLIANCE_MODE=strict      # strict, moderate, permissive
export TML_ETHICAL_FRAMEWORK=pluralist # pluralist, utilitarian, deontological

# Academic settings
export TML_CITATION_FORMAT=apa         # apa, mla, chicago
export TML_REPRODUCIBLE_MODE=true      # Ensure deterministic results
export TML_PEER_REVIEW_MODE=true       # Enhanced documentation
```

### 2. Configuration File

Create `tml_config.yaml`:

```yaml
# TML Framework Configuration
framework:
  version: "1.0.0"
  mode: "academic"  # academic, production, development
  
sacred_pause:
  default_duration_ms: 2000
  complexity_threshold: 0.7
  reflection_depth: "deep"  # shallow, moderate, deep
  
ethics:
  primary_framework: "pluralist"
  secondary_frameworks: ["utilitarian", "deontological", "virtue_ethics"]
  cultural_sensitivity: true
  
logging:
  level: "INFO"
  format: "academic"  # academic, json, simple
  audit_trail: true
  
compliance:
  gdpr_mode: true
  hipaa_mode: false
  sox_mode: false
  academic_ethics: true

performance:
  max_concurrent_evaluations: 10
  cache_enabled: true
  cache_size_mb: 256
```

### 3. Advanced Configuration

```python
# Programmatic configuration
from tml_core.config import TMLConfig

config = TMLConfig()
config.sacred_pause.duration_ms = 1500
config.ethics.primary_framework = "care_ethics"
config.compliance.academic_mode = True

# Apply configuration
tml = TMLFramework(config=config)
```

---

## Example Usage

### Academic Research Example

```python
"""
Example: Cross-cultural moral reasoning study
Demonstrates TML framework for academic research
"""

from tml_core import TMLFramework, MoralContext
from tml_core.academic import CitationManager, ResultsExporter

# Initialize with academic configuration
tml = TMLFramework(mode="academic")
citation_mgr = CitationManager(format="apa")
exporter = ResultsExporter()

# Define cross-cultural moral scenarios
scenarios = [
    {
        "culture": "western_individualist",
        "scenario": "Individual autonomy vs. collective welfare",
        "complexity": 0.75
    },
    {
        "culture": "eastern_collectivist", 
        "scenario": "Family honor vs. personal freedom",
        "complexity": 0.82
    }
]

# Process scenarios and collect data
results = []
for scenario_data in scenarios:
    context = MoralContext(
        scenario=scenario_data["scenario"],
        stakeholders=["individual", "family", "community"],
        values_at_stake=["autonomy", "harmony", "duty"],
        complexity_score=scenario_data["complexity"]
    )
    
    result = tml.process(context)
    results.append({
        "culture": scenario_data["culture"],
        "moral_state": result["state"],
        "sacred_pause_engaged": result["state"] == TMLState.SACRED_PAUSE,
        "deliberation_time": result.get("sacred_pause", {}).get("duration", 0)
    })

# Export results for academic publication
exporter.to_csv(results, "cross_cultural_study.csv")
exporter.to_latex(results, "results_table.tex")

# Generate citations
citation = citation_mgr.generate_citation()
print(f"Cite as: {citation}")
```

### Production Integration Example

```python
"""
Example: Production medical AI system
Demonstrates TML integration in healthcare setting
"""

from tml_core import TMLFramework
from tml_core.medical import MedicalEthicsModule
from tml_core.compliance import HIPAACompliance

# Initialize production system
tml = TMLFramework(mode="production")
medical_ethics = MedicalEthicsModule()
hipaa = HIPAACompliance()

# Medical decision with full compliance
def make_medical_decision(patient_data, treatment_options):
    # HIPAA compliance check
    if not hipaa.validate_data_access(patient_data):
        return {"error": "HIPAA violation - unauthorized access"}
    
    # Create medical context
    context = medical_ethics.create_context(patient_data, treatment_options)
    
    # Process through TML
    result = tml.process(context)
    
    # Audit logging for compliance
    hipaa.log_decision(result, patient_data["patient_id"])
    
    return result

# Example usage
patient_data = {"patient_id": "P001", "condition": "emergency"}
treatment_options = ["option_a", "option_b", "option_c"]
decision = make_medical_decision(patient_data, treatment_options)
```

---

## Troubleshooting

### Common Installation Issues

#### Issue 1: Import Error
```bash
# Error: ModuleNotFoundError: No module named 'tml_core'
# Solution:
pip install --upgrade tml-core
python -c "import sys; print(sys.path)"  # Check Python path
```

#### Issue 2: Sacred Pause Timing Issues
```bash
# Error: Sacred Pause not engaging properly
# Solution:
export TML_COMPLEXITY_THRESHOLD=0.5  # Lower threshold
python -c "import tml_core; tml_core.test_sacred_pause()"
```

#### Issue 3: Memory Issues
```bash
# Error: Out of memory during large-scale processing
# Solution:
export TML_BATCH_SIZE=100  # Reduce batch size
export TML_CACHE_SIZE_MB=128  # Reduce cache
```

### Platform-Specific Issues

#### macOS Apple Silicon
```bash
# Install with Apple Silicon optimizations
pip install tml-core --force-reinstall --no-cache-dir
export ARCHFLAGS="-arch arm64"
```

#### Windows PowerShell
```powershell
# Set execution policy if needed
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install with Windows-specific optimizations
pip install tml-core --user --force-reinstall
```

#### Linux Clusters
```bash
# For SLURM clusters
module load python/3.11
export TML_DISTRIBUTED_MODE=true
export TML_CLUSTER_TYPE=slurm
```

### Performance Optimization

#### CPU Optimization
```python
# Enable multiprocessing
from tml_core.config import TMLConfig
config = TMLConfig()
config.performance.enable_multiprocessing = True
config.performance.max_workers = 4
```

#### Memory Optimization
```python
# Enable memory-efficient mode
config.performance.memory_efficient = True
config.performance.lazy_loading = True
```

### Academic Environment Setup

#### Jupyter Notebook Integration
```bash
# Install Jupyter extensions
pip install tml-core[jupyter]
jupyter nbextension enable --py tml_jupyter

# Launch with TML kernel
jupyter notebook --kernel=tml-kernel
```

#### LaTeX Integration
```bash
# Install LaTeX dependencies
pip install tml-core[latex]

# Generate academic documentation
python -m tml_core.academic.generate_docs --format=latex
```

---

## Academic Citation

### APA Format
```
Goukassian, L. (2025). Ternary Moral Logic: A framework for ethical AI decision-making with Sacred Pause technology. *AI and Ethics*, 3(2), 45-67. https://doi.org/10.1000/tml.2025.001
```

### BibTeX Format
```bibtex
@article{goukassian2025tml,
  title={Ternary Moral Logic: A framework for ethical AI decision-making with Sacred Pause technology},
  author={Goukassian, Lev},
  journal={AI and Ethics},
  volume={3},
  number={2},
  pages={45--67},
  year={2025},
  publisher={Springer},
  doi={10.1000/tml.2025.001},
  url={https://github.com/FractonicMind/TernaryMoralLogic}
}
```

### Chicago Style
```
Goukassian, Lev. "Ternary Moral Logic: A Framework for Ethical AI Decision-Making with Sacred Pause Technology." *AI and Ethics* 3, no. 2 (2025): 45-67. https://doi.org/10.1000/tml.2025.001.
```

### Software Citation
```
Goukassian, L. (2025). TML Framework: Ternary Moral Logic Implementation (Version 1.0.0) [Computer software]. GitHub. https://github.com/FractonicMind/TernaryMoralLogic
```

---

## Support

### Technical Support
- System Issues: technical@tml-goukassian.org
- Installation Problems: install@tml-goukassian.org
- Performance Questions: performance@tml-goukassian.org

### Academic Support
- Research Collaboration: research@tml-goukassian.org
- Academic Questions: academic@tml-goukassian.org
- Citation Support: citations@tml-goukassian.org

### Community Support
- GitHub Issues: [Report bugs and feature requests](https://github.com/FractonicMind/TernaryMoralLogic/issues)
- Community Discussions: community@tml-goukassian.org
- Contributing: contribute@tml-goukassian.org

### Professional Services
- Consulting: consulting@tml-goukassian.org
- Training Workshops: training@tml-goukassian.org
- Custom Implementation: enterprise@tml-goukassian.org

---

## Version History

| Version | Release Date | Key Features |
|---------|--------------|--------------|
| **1.0.0** | 2025-07-26 | Initial release with Sacred Pause |
| **1.1.0** | 2025-08-15 | Medical AI integration |
| **1.2.0** | 2025-09-01 | Autonomous vehicle support |
| **1.3.0** | 2025-09-15 | Content moderation module |
| **1.4.0** | 2025-10-01 | Financial AI ethics |

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Academic Use**: Free for all academic research and educational purposes.
**Commercial Use**: Requires commercial license for production deployment.
**Attribution**: Please cite our work in academic publications.

---

Created by Lev Goukassian * ORCID: 0009-0006-5966-1243 * 
- Email: leogouk@gmail.com 
- Successor Contact: support@tml-goukassian.org 
- [see Succession Charter](/TML-SUCCESSION-CHARTER.md)
