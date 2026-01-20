# Kubernetes Examples

Working Kubernetes configuration examples for common deployment patterns.

## Prerequisites

- kubectl CLI installed
- Access to a Kubernetes cluster (minikube, kind, or cloud provider)

## Usage

```bash
# Apply a configuration
kubectl apply -f examples/deployment.yaml

# View resources
kubectl get pods
kubectl get services
```

## Examples

| File | Description |
|------|-------------|
| `deployment.yaml` | Basic Deployment with replicas |
| `service.yaml` | ClusterIP and LoadBalancer services |
| `configmap.yaml` | Configuration management |
| `secret.yaml` | Sensitive data handling |
| `ingress.yaml` | HTTP routing with Ingress |
| `pvc.yaml` | Persistent storage |
| `hpa.yaml` | Horizontal Pod Autoscaler |

## Structure

```
kubernetes/
├── README.md
└── examples/
    ├── deployment.yaml
    ├── service.yaml
    ├── configmap.yaml
    └── ...
```

## Reference

See the full cheatsheet at: [skola.dev/cheatsheets/kubernetes](https://skola.dev/cheatsheets/kubernetes)
