# DOI Application Status

## Ternary Moral Logic (TML) Framework

**Digital Object Identifier (DOI) Application Documentation**

---

## Current Status

**Application Status**: 🟡 **Preparation Phase**  
**Target DOI Provider**: Zenodo (CERN)  
**Expected Timeline**: 2-4 weeks post-submission  
**Application Type**: Software + Dataset DOI

---

## DOI Application Strategy

### Primary Application: Software DOI

**Target**: `10.5281/zenodo.tml-framework`  
**Provider**: [Zenodo](https://zenodo.org) - Recommended for open source academic software  
**Content**: Complete TML Framework codebase with examples  

**Requirements for Submission**:
- ✅ Stable release version (v1.0.0)
- ✅ Complete documentation
- ✅ Open source license (MIT)
- ✅ Comprehensive README
- ⏳ Final code review and testing
- ⏳ Release notes preparation

### Secondary Application: Academic Paper DOI

**Target**: Journal-assigned DOI upon acceptance  
**Provider**: CrossRef (via journal publisher)  
**Timeline**: 6-12 months (peer review + publication process)

**Target Journals**:
1. **Primary**: Nature Machine Intelligence
2. **Secondary**: Artificial Intelligence Journal  
3. **Tertiary**: Journal of AI Ethics

---

## DOI Application Checklist

### Technical Requirements

#### Software Package Requirements
- [x] **Version Control**: Complete Git history with semantic versioning
- [x] **Licensing**: MIT License for maximum academic accessibility
- [x] **Documentation**: Comprehensive API docs and user guides
- [x] **Testing**: Full test suite with >90% code coverage
- [x] **Examples**: Four domain implementation examples
- [x] **Installation**: Multi-platform installation instructions
- [x] **Dependencies**: Clearly specified and minimal
- [ ] **Release Notes**: Detailed changelog and version documentation
- [ ] **Citation File**: CITATION.cff for proper academic citation

#### Metadata Requirements
```yaml
# Required Zenodo metadata
title: "Ternary Moral Logic (TML) Framework"
description: "A three-state ethical AI framework with Sacred Zero technology"
creators:
  - name: "Goukassian, Lev"
    orcid: "0009-0006-5966-1243"
keywords:
  - "AI Ethics"
  - "Moral Reasoning"  
  - "Sacred Zero"
  - "Algorithmic Fairness"
  - "Regulatory Compliance"
license: "MIT"
version: "1.0.0"
language: "en"
```

### Academic Requirements

#### ORCID Registration
**Status**: ✅ **Completed**  
**ORCID ID**: 0009-0006-5966-1243  
**Required For**: Author identification in DOI metadata  
**Registration Status**: Active and verified

#### Institutional Affiliation
**Current**: Independent Researcher  
**Future**: TML Research Institute (to be established)  
**Impact**: Enhances credibility for DOI application

---

## Zenodo Submission Process

### Step 1: Repository Preparation
```bash
# Create release-ready repository
git tag -a v1.0.0 -m "Initial stable release for DOI application"
git push origin v1.0.0

# Generate release archive
git archive --format=zip --prefix=tml-framework-1.0.0/ v1.0.0 > tml-framework-1.0.0.zip
```

### Step 2: Zenodo Upload
1. **Create Zenodo Account**: Link with GitHub for automatic integration
2. **Enable Repository**: Activate Zenodo integration for TML repository
3. **Upload Release**: Automatic DOI generation on new GitHub releases
4. **Complete Metadata**: Fill all required academic metadata fields
5. **Submit for Review**: Zenodo moderation (typically 1-2 business days)

### Step 3: DOI Verification
- **DOI Registration**: Automatic upon Zenodo approval
- **Metadata Propagation**: 24-48 hours for full indexing
- **Citation Updates**: Update all documentation with official DOI

---

## Citation Preparation

### Pre-DOI Citation Format
```
Goukassian, L. (2025). Ternary Moral Logic (TML) Framework: 
A three-state ethical AI framework with Sacred Zero technology 
(Version 1.0.0) [Computer software]. GitHub. 
https://github.com/FractonicMind/TernaryMoralLogic
```

### Post-DOI Citation Format
```
Goukassian, L. (2025). Ternary Moral Logic (TML) Framework: 
A three-state ethical AI framework with Sacred Zero technology 
(Version 1.0.0) [Computer software]. Zenodo. 
https://doi.org/10.5281/zenodo.XXXXXX
```

### BibTeX Template (Post-DOI)
```bibtex
@software{goukassian2025tml,
  author       = {Goukassian, Lev},
  title        = {{Ternary Moral Logic (TML) Framework: A three-state 
                   ethical AI framework with Sacred Zero technology}},
  month        = jul,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.XXXXXX},
  url          = {https://doi.org/10.5281/zenodo.XXXXXX}
}
```

---

## Academic Impact Strategy

### Post-DOI Actions

#### Immediate (Week 1)
- [ ] Update all repository documentation with official DOI
- [ ] Submit to major software registries (PyPI, Conda)
- [ ] Announce on academic social media (Twitter, LinkedIn)
- [ ] Contact AI ethics research groups for awareness

#### Short-term (Months 1-3)
- [ ] Submit abstracts to AI ethics conferences
- [ ] Reach out to potential research collaborators
- [ ] Begin formal peer review submission process
- [ ] Document usage and adoption metrics

#### Long-term (Months 6-12)
- [ ] Publish peer-reviewed academic paper
- [ ] Present at major conferences (NeurIPS, ICML, AIES)
- [ ] Establish research partnerships with universities
- [ ] Track citations and academic impact

---

## DOI Benefits for TML Framework

### Academic Credibility
- **Permanent Identifier**: Ensures long-term accessibility
- **Version Tracking**: Links specific versions to citations
- **Metadata Standards**: Facilitates academic discovery
- **Citation Tracking**: Enables impact measurement

### Regulatory Compliance
- **Audit Trails**: Permanent record for compliance documentation
- **Version Control**: Required for regulated industry deployments
- **Reproducibility**: Essential for scientific validation
- **Legal Protection**: Timestamped IP evidence

### Community Building
- **Discoverability**: Academic search engines and databases
- **Credibility**: Professional DOI signals serious research
- **Collaboration**: Easier for researchers to cite and build upon
- **Legacy**: Permanent contribution to AI ethics literature

---

## Next Steps

### Immediate Actions Required
1. **Complete ORCID Registration** (1-2 days)
2. **Finalize Release Notes** (3-5 days)
3. **Create CITATION.cff File** (1 day)
4. **GitHub Release v1.0.0** (1 day)
5. **Zenodo Submission** (1 day)

### Timeline
```
Week 1: ORCID + Release Preparation
Week 2: GitHub Release + Zenodo Submission
Week 3: DOI Approval + Documentation Updates
Week 4: Academic Announcement + Outreach
```

### Success Metrics
- **DOI Obtained**: Official Zenodo DOI assigned
- **Metadata Quality**: Complete and accurate academic metadata
- **Discoverability**: Indexed in academic databases
- **Citation Readiness**: All documentation updated with DOI

---

## Contact Information

**DOI Application Inquiries**: research@tml-framework.org  
**Technical Questions**: support@tml-framework.org  
**Academic Collaboration**: academic@tml-framework.org

---

- Email: leogouk@gmail.com 
- Successor Contact: support@tml-goukassian.org 
- [See Succession Charter](/TML-SUCCESSION-CHARTER.md)
