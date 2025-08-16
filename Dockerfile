# Ternary Moral Logic (TML) Framework - Docker Container
# Author: Lev Goukassian (ORCID: 0009-0006-5966-1243)
# Sacred Pause Technology for Ethical AI Decision-Making
#
# This Dockerfile provides a complete, reproducible environment for
# academic reviewers and researchers to test the TML framework
# in under 30 seconds.
#
# Build: docker build -t tml-goukassian .
# Run:   docker run -it tml-goukassian

# Use official Python runtime as base image
FROM python:3.11-slim

# Set maintainer information
LABEL maintainer="Lev Goukassian <leogouk@gmail.com>"
LABEL version="1.0.0"
LABEL description="Ternary Moral Logic Framework with Sacred Pause Technology"
LABEL org.opencontainers.image.source="https://github.com/FractonicMind/TernaryMoralLogic"
LABEL org.opencontainers.image.documentation="https://github.com/FractonicMind/TernaryMoralLogic/blob/main/README.md"
LABEL org.opencontainers.image.url="https://tml-goukassian.org"
LABEL org.opencontainers.image.vendor="TML Framework"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.title="Ternary Moral Logic Framework"
LABEL org.opencontainers.image.created="2025-08-16"

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=42 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set working directory in container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    git \
    curl \
    vim \
    nano \
    tree \
    less \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN groupadd -r tml && useradd -r -g tml tml

# Copy requirements files first (for Docker layer caching)
COPY requirements.txt requirements-dev.txt ./

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip setuptools wheel

# Install production dependencies
RUN pip install -r requirements.txt

# Install development dependencies (for academic testing)
RUN pip install -r requirements-dev.txt

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p /app/logs /app/data /app/output

# Set ownership to non-root user
RUN chown -R tml:tml /app

# Switch to non-root user
USER tml

# Set up TML environment variables
ENV TML_ENV=docker \
    TML_LOG_LEVEL=INFO \
    TML_SACRED_PAUSE_DURATION=2000 \
    TML_COMPLEXITY_THRESHOLD=0.7 \
    TML_ETHICS_MODE=strict \
    TML_CREATOR_ATTRIBUTION=enabled \
    TML_INTEGRITY_MONITORING=enabled

# Creator information for framework
RUN echo "# Ternary Moral Logic Framework" > /home/tml/.tml_info && \
    echo "# Created by Lev Goukassian (ORCID: 0009-0006-5966-1243)" >> /home/tml/.tml_info && \
    echo "# Sacred Pause Technology for Ethical AI Decision-Making" >> /home/tml/.tml_info && \
    echo "# Contact: leogouk@gmail.com" >> /home/tml/.tml_info && \
    echo "# Successor Contact: support@tml-goukassian.org" >> /home/tml/.tml_info && \
    echo "# Website: https://tml-goukassian.org" >> /home/tml/.tml_info && \
    echo "" >> /home/tml/.tml_info && \
    echo "\"The sacred pause between question and answer—this is where wisdom begins," >> /home/tml/.tml_info && \
    echo "for humans and machines alike.\" — Lev Goukassian" >> /home/tml/.tml_info && \
    echo "" >> /home/tml/.tml_info && \
    echo "Created by Lev Goukassian * ORCID: 0009-0006-5966-1243 *" >> /home/tml/.tml_info && \
    echo "- Email: leogouk@gmail.com" >> /home/tml/.tml_info && \
    echo "- Successor Contact: support@tml-goukassian.org" >> /home/tml/.tml_info && \
    echo "- [see Succession Charter](/TML-SUCCESSION-CHARTER.md)" >> /home/tml/.tml_info

# Expose port for potential web interfaces
EXPOSE 8080

# Health check to verify TML framework is working
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.path.append('/app'); from tests.isolated_test import test_immoral_identification; print('TML Health Check: PASSED')" || exit 1

# Default command: Interactive shell with TML information
CMD ["/bin/bash", "-c", "cat /home/tml/.tml_info && echo && echo 'TML Framework Ready! Try these commands:' && echo '  python tests/isolated_test.py              # Run basic TML tests' && echo '  python tests/test_tml_core.py              # Run comprehensive test suite' && echo '  python examples/medical_ai_triage.py       # Medical AI demo' && echo '  python examples/autonomous_vehicle.py      # Autonomous vehicle demo' && echo '  python examples/content_moderation.py      # Content moderation demo' && echo '  python examples/financial_ai.py            # Financial AI demo' && echo '  pytest tests/ -v                          # Run full test suite' && echo '  python -c \"from tml_core import *; print(\\\"TML imported successfully\\\")\"' && echo && echo 'Quick Start Guide: docs/QUICK_START.md' && echo 'Complete API Reference: docs/api/complete_api_reference.md' && echo 'Academic Validation: docs/ACADEMIC_VALIDATION.md' && echo && echo 'For interactive exploration:' && echo '  python                                     # Start Python REPL' && echo '  jupyter notebook --ip=0.0.0.0 --no-browser # Start Jupyter (if needed)' && echo && /bin/bash"]

# Alternative: Direct demo command
# Uncomment to run immediate demo instead of interactive shell
# CMD ["python", "examples/medical_ai_triage.py"]
