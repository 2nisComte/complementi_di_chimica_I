FROM mcr.microsoft.com/devcontainers/base:jammy

# Install basic packages
RUN apt-get update && apt-get install -y wget cmake git vim nano python3-pip

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh

ENV PATH="/opt/conda/bin:$PATH"

# Install Psi4
RUN conda install -y psi4 python=3.10 -c conda-forge
