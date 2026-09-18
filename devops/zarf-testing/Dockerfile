FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ARG K3S_VERSION=v1.30.2+k3s1
ARG ZARF_VERSION=v0.38.2

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        iptables \
        kmod \
        procps \
        tar \
    && rm -rf /var/lib/apt/lists/*

# Install k3s binary directly to avoid init-system checks in image builds.
RUN curl -fL "https://github.com/k3s-io/k3s/releases/download/${K3S_VERSION}/k3s" -o /usr/local/bin/k3s \
    && chmod +x /usr/local/bin/k3s

# Install Zarf binary for air-gap/package deployments into k3s.
RUN curl -fL "https://github.com/zarf-dev/zarf/releases/download/${ZARF_VERSION}/zarf_${ZARF_VERSION}_Linux_amd64" \
        -o /usr/local/bin/zarf \
    && chmod +x /usr/local/bin/zarf

COPY k3s-entrypoint.sh /usr/local/bin/k3s-entrypoint.sh
# Strip Windows CRLF line endings so the shebang and commands run cleanly on Linux.
RUN sed -i 's/\r$//' /usr/local/bin/k3s-entrypoint.sh \
    && chmod +x /usr/local/bin/k3s-entrypoint.sh

EXPOSE 6443
VOLUME ["/var/lib/rancher/k3s", "/etc/rancher/k3s"]

ENTRYPOINT ["/usr/local/bin/k3s-entrypoint.sh"]
