FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

ENV DEBIAN_FRONTEND=noninteractive

# Core tools and language runtimes used by the Coding Lab workflow.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        gnupg \
        jq \
        lsb-release \
        mysql-client \
        python3 \
        python3-pip \
        php-cli \
        golang-go \
        openjdk-21-jdk \
        maven \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js 20.x.
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get update \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

# Install kubectl.
RUN curl -fsSL "https://dl.k8s.io/release/$(curl -fsSL https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" -o /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl

# Install Helm.
RUN curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Install PowerShell.
RUN wget -q https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb \
    && apt-get update \
    && apt-get install -y --no-install-recommends powershell \
    && rm -rf /var/lib/apt/lists/*

USER vscode
WORKDIR /workspaces/Test_Codes/devops/zarf-testing
