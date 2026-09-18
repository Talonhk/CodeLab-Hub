#!/usr/bin/env sh
set -eu

mkdir -p /run /var/run /var/lib/rancher/k3s /etc/rancher/k3s

exec /usr/local/bin/k3s server \
  --https-listen-port=6443 \
  --write-kubeconfig=/etc/rancher/k3s/k3s.yaml \
  --write-kubeconfig-mode=644 \
  --disable=traefik \
  "$@"
