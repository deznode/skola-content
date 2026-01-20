# Kubernetes Cheat Sheet (v1.30/1.31)

**Persona/Use Context:** DevOps engineers, SREs, and developers for daily cluster operations, debugging, and incident response
**Tested/Assumptions:** Kubernetes 1.30-1.31, kubectl 1.30+, bash/zsh shell, cluster-admin or equivalent RBAC
**Last Validated:** January 2025

## Do / Don't Summary

**Do:**
- Always verify context before destructive commands: `kubectl config current-context`
- Use `--dry-run=client -o yaml` to preview changes before applying
- Set resource requests AND limits on all production workloads

**Don't:**
- Run `kubectl delete` without `--dry-run=client` first in production
- Use `latest` image tags in production (breaks reproducibility, caching issues)
- Store secrets in plain ConfigMaps (use Secrets or external secret managers)

---

## 1) Quick Start / Golden Path

```bash
# 1. Verify cluster connection
kubectl cluster-info
kubectl config current-context

# 2. Check node health
kubectl get nodes -o wide

# 3. Set default namespace (avoid repeating -n flag)
kubectl config set-context --current --namespace=<NAMESPACE>

# 4. Deploy an application
kubectl apply -f deployment.yaml
# OR imperatively:
kubectl create deployment nginx --image=nginx:1.27 --replicas=3

# 5. Expose it
kubectl expose deployment nginx --port=80 --type=ClusterIP

# 6. Verify rollout
kubectl rollout status deployment/nginx

# 7. Check pods
kubectl get pods -l app=nginx -o wide
```

---

## 2) Core Concepts (1-liners)

| Term | Meaning |
|------|---------|
| **Pod** | Smallest deployable unit; one or more containers sharing network/storage |
| **Deployment** | Declarative pod management with rollout/rollback |
| **Service** | Stable network endpoint for pod sets |
| **ConfigMap** | Non-sensitive configuration data |
| **Secret** | Sensitive data (base64 encoded, NOT encrypted by default) |
| **Namespace** | Virtual cluster for resource isolation |
| **ReplicaSet** | Ensures N pod replicas are running (managed by Deployment) |
| **DaemonSet** | Runs one pod per node (logs, monitoring agents) |
| **StatefulSet** | Pods with stable identity and persistent storage |
| **Job / CronJob** | Run-to-completion / scheduled workloads |
| **Ingress** | HTTP/S routing rules to Services |
| **PV / PVC** | PersistentVolume / PersistentVolumeClaim for storage |
| **HPA** | Horizontal Pod Autoscaler |
| **NetworkPolicy** | Pod-level firewall rules |

---

## 3) Core Syntax / Commands

### Context & Configuration

```bash
# List all contexts
kubectl config get-contexts

# Show current context
kubectl config current-context

# Switch context
kubectl config use-context <CONTEXT_NAME>

# Set default namespace for context
kubectl config set-context --current --namespace=<NAMESPACE>

# View merged kubeconfig
kubectl config view --minify

# SAFETY: Always verify before destructive ops
kubectl config current-context && kubectl get nodes
```

### Cluster Information

```bash
kubectl cluster-info                             # Display cluster endpoint info
kubectl get nodes -o wide                        # List nodes with details
kubectl top nodes                                # Node resource usage (requires metrics-server)
kubectl api-resources                            # List all resource types + short names
kubectl api-versions                             # List API versions
kubectl explain <RESOURCE>                       # Documentation for resource
kubectl explain pod.spec.containers              # Nested field docs
```

### Namespace Operations

```bash
# List namespaces
kubectl get ns

# Create namespace
kubectl create ns <NAME>

# Delete namespace (DANGER: deletes all resources in it)
kubectl delete ns <NAME>  # Add --dry-run=client first!

# Run command in specific namespace
kubectl -n <NAMESPACE> get pods
```

### Get Resources (Read Operations)

```bash
# Basic listing
kubectl get pods|deployments|services|nodes|all

# Wide output with node info
kubectl get pods -o wide

# All namespaces
kubectl get pods -A
kubectl get pods --all-namespaces

# Watch for changes
kubectl get pods -w

# Show labels
kubectl get pods --show-labels

# Filter by label
kubectl get pods -l app=nginx,env=prod
kubectl get pods -l 'env in (prod,staging)'

# Filter by field
kubectl get pods --field-selector=status.phase=Running
kubectl get pods --field-selector=spec.nodeName=<NODE>

# Output formats
kubectl get pod <NAME> -o yaml
kubectl get pod <NAME> -o json
kubectl get pods -o name                    # Just names
kubectl get pods -o jsonpath='{.items[*].metadata.name}'

# Custom columns
kubectl get pods -o custom-columns=NAME:.metadata.name,STATUS:.status.phase,NODE:.spec.nodeName

# Sort by field
kubectl get pods --sort-by='.status.startTime'
kubectl get pods --sort-by='.metadata.creationTimestamp'
```

### Describe & Inspect

```bash
# Detailed resource info (events, conditions)
kubectl describe pod <POD_NAME>
kubectl describe node <NODE_NAME>
kubectl describe deployment <NAME>

# Get specific field with jsonpath
kubectl get pod <NAME> -o jsonpath='{.status.podIP}'
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}'

# Resource usage (requires metrics-server)
kubectl top pods
kubectl top nodes
kubectl top pods --containers  # Per-container

# View events (sorted by time)
kubectl get events --sort-by='.lastTimestamp'
kubectl get events -A --sort-by='.lastTimestamp'
```

### Create & Apply

```bash
# Imperative creation
kubectl create deployment nginx --image=nginx:1.27
kubectl create service clusterip nginx --tcp=80:80
kubectl create configmap app-config --from-file=config.properties
kubectl create secret generic db-creds --from-literal=password=<VALUE>

# Declarative (preferred for production)
kubectl apply -f manifest.yaml
kubectl apply -f ./manifests/           # Directory
kubectl apply -f https://example.com/manifest.yaml
kubectl apply -k ./kustomize-dir/       # Kustomize

# Dry run and diff (ESSENTIAL for safety)
kubectl apply -f manifest.yaml --dry-run=client -o yaml
kubectl diff -f manifest.yaml           # Show what would change

# Generate YAML (don't create)
kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > deployment.yaml
kubectl run nginx --image=nginx --dry-run=client -o yaml > pod.yaml
```

### Edit & Patch

```bash
# Interactive edit (opens $EDITOR)
kubectl edit deployment/<NAME>

# Strategic merge patch
kubectl patch deployment nginx -p '{"spec":{"replicas":5}}'

# JSON patch
kubectl patch deployment nginx --type='json' \
  -p='[{"op":"replace","path":"/spec/replicas","value":5}]'

# Update image
kubectl set image deployment/nginx nginx=nginx:1.27

# Scale
kubectl scale deployment nginx --replicas=5

# Add/update labels
kubectl label pod <POD> env=prod
kubectl label pod <POD> env=staging --overwrite

# Remove label
kubectl label pod <POD> env-

# Add annotation
kubectl annotate pod <POD> description="My app"
```

### Delete Resources

```bash
# Delete by name
kubectl delete pod <POD_NAME>
kubectl delete -f manifest.yaml

# Delete by label
kubectl delete pods -l app=nginx

# Force delete stuck pod (use sparingly!)
kubectl delete pod <POD> --grace-period=0 --force

# Delete all pods in namespace
kubectl delete pods --all -n <NAMESPACE>

# SAFETY: Always dry-run first
kubectl delete deployment nginx --dry-run=client
```

**WARNING:** Force delete (`--grace-period=0 --force`) can cause data loss and skip cleanup. Use only for truly stuck pods.

### Rollouts

```bash
# Watch rollout progress
kubectl rollout status deployment/<NAME>

# View rollout history
kubectl rollout history deployment/<NAME>

# Rollback to previous version
kubectl rollout undo deployment/<NAME>

# Rollback to specific revision
kubectl rollout undo deployment/<NAME> --to-revision=2

# Pause/resume rollout
kubectl rollout pause deployment/<NAME>
kubectl rollout resume deployment/<NAME>

# Restart deployment (triggers new rollout with same config)
kubectl rollout restart deployment/<NAME>
```

---

## 4) Common Tasks (Copy/Paste)

### Task: Debug a CrashLooping Pod

```bash
# 1. Check pod status and restart count
kubectl get pod <POD> -o wide

# 2. View recent events
kubectl describe pod <POD> | grep -A 20 "Events:"

# 3. Check logs (current container)
kubectl logs <POD>

# 4. Check previous container logs (after crash)
kubectl logs <POD> --previous

# 5. Check specific container in multi-container pod
kubectl logs <POD> -c <CONTAINER_NAME>

# 6. Stream logs
kubectl logs -f <POD>

# 7. Logs with timestamps and last N lines
kubectl logs <POD> --timestamps --tail=100

# 8. Check exit code
kubectl get pod <POD> -o jsonpath='{.status.containerStatuses[0].lastState.terminated}'
```

### Task: Debug with Ephemeral Container (K8s 1.25+)

```bash
# Attach debug container to running pod
kubectl debug -it <POD> --image=busybox --target=<CONTAINER>

# Create copy of pod for debugging (preserves original)
kubectl debug <POD> -it --copy-to=<POD>-debug --container=debug -- /bin/sh

# Debug with network tools
kubectl debug -it <POD> --image=nicolaka/netshoot --target=<CONTAINER>
```

### Task: Execute Commands in Pod

```bash
# Interactive shell
kubectl exec -it <POD> -- /bin/bash
kubectl exec -it <POD> -- /bin/sh      # If bash not available

# Specific container
kubectl exec -it <POD> -c <CONTAINER> -- /bin/sh

# Single command
kubectl exec <POD> -- cat /etc/config/app.properties
kubectl exec <POD> -- env | grep -i database

# Copy files to/from pod
kubectl cp <POD>:/path/to/file ./local-file
kubectl cp ./local-file <POD>:/path/to/file
kubectl cp <POD>:/path/to/file ./local-file -c <CONTAINER>
```

### Task: Port Forwarding

```bash
# Forward local port to pod
kubectl port-forward pod/<POD> 8080:80

# Forward to service
kubectl port-forward svc/<SERVICE> 8080:80

# Forward to deployment (picks a pod)
kubectl port-forward deployment/<NAME> 8080:80

# Listen on all interfaces (for remote access)
kubectl port-forward --address 0.0.0.0 pod/<POD> 8080:80

# Background
kubectl port-forward svc/my-service 8080:80 &
```

### Task: Deploy with Rolling Update

```bash
# Update image (triggers rolling update)
kubectl set image deployment/<NAME> <CONTAINER>=<IMAGE>:<TAG>

# Watch rollout progress
kubectl rollout status deployment/<NAME>

# View rollout history
kubectl rollout history deployment/<NAME>

# Rollback to previous version
kubectl rollout undo deployment/<NAME>

# Rollback to specific revision
kubectl rollout undo deployment/<NAME> --to-revision=2

# Restart deployment (triggers new rollout)
kubectl rollout restart deployment/<NAME>
```

### Task: Create and Use ConfigMaps

```bash
# From literal values
kubectl create configmap app-config \
  --from-literal=DB_HOST=postgres.default.svc \
  --from-literal=LOG_LEVEL=info

# From file
kubectl create configmap app-config --from-file=config.properties

# From env file
kubectl create configmap app-config --from-env-file=.env

# View ConfigMap
kubectl get configmap app-config -o yaml

# Edit ConfigMap
kubectl edit configmap app-config
```

**Mount as environment variables:**
```yaml
envFrom:
  - configMapRef:
      name: app-config
```

**Mount as volume:**
```yaml
volumes:
  - name: config-volume
    configMap:
      name: app-config
volumeMounts:
  - name: config-volume
    mountPath: /etc/config
```

### Task: Manage Secrets

```bash
# Create from literals (auto base64-encodes)
kubectl create secret generic db-creds \
  --from-literal=username=admin \
  --from-literal=password='S3cr3t!'

# Create from file
kubectl create secret generic tls-certs \
  --from-file=tls.crt --from-file=tls.key

# Create TLS secret
kubectl create secret tls my-tls --cert=tls.crt --key=tls.key

# Create Docker registry secret
kubectl create secret docker-registry regcred \
  --docker-server=<REGISTRY> \
  --docker-username=<USER> \
  --docker-password=<PASSWORD>

# View secret (base64 encoded)
kubectl get secret db-creds -o yaml

# Decode secret value
kubectl get secret db-creds -o jsonpath='{.data.password}' | base64 -d
```

### Task: Horizontal Pod Autoscaler

```bash
# Create HPA (requires metrics-server)
kubectl autoscale deployment nginx --min=2 --max=10 --cpu-percent=80

# View HPA status
kubectl get hpa

# Describe HPA (shows scaling events)
kubectl describe hpa nginx

# Delete HPA
kubectl delete hpa nginx
```

**HPA YAML example:**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 80
```

---

## 5) Service Types Reference

| Type | Scope | Use Case | Access |
|------|-------|----------|--------|
| **ClusterIP** | Internal | Default; inter-service communication | `<service>.<namespace>.svc.cluster.local` |
| **NodePort** | External | Dev/test; direct node access | `<NodeIP>:<NodePort>` (30000-32767) |
| **LoadBalancer** | External | Production; cloud provider LB | External IP assigned by cloud |
| **ExternalName** | External | Alias to external DNS | Returns CNAME record |

```yaml
# NodePort example
apiVersion: v1
kind: Service
metadata:
  name: myapp-nodeport
spec:
  type: NodePort
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080  # Optional; auto-assigned if omitted (30000-32767)
---
# LoadBalancer example
apiVersion: v1
kind: Service
metadata:
  name: myapp-lb
spec:
  type: LoadBalancer
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080
```

---

## 6) Pitfalls & Anti-Patterns

| Don't | Why | Fix |
|-------|-----|-----|
| Use `latest` image tag | Breaks reproducibility; unclear what's deployed | Pin specific version: `nginx:1.27.3` |
| Skip resource limits | Pod can consume all node resources, cause OOM | Always set `resources.requests` AND `resources.limits` |
| Put secrets in ConfigMaps | ConfigMaps are not encrypted | Use Secrets + consider external secret managers |
| Delete namespace without checking | Deletes ALL resources inside | Run `kubectl get all -n <NS>` first |
| Use `kubectl edit` in CI/CD | Not reproducible, no audit trail | Use `kubectl apply -f` with version-controlled manifests |
| Run as root in containers | Security risk if container escapes | Set `securityContext.runAsNonRoot: true` |
| Ignore Pod resource requests | Scheduler can't make good placement decisions | Set requests = typical usage, limits = max allowed |
| Hard-code service IPs | IPs can change | Use DNS: `<service>.<namespace>.svc.cluster.local` |
| Use `--force --grace-period=0` casually | Can cause data loss, skip cleanup | Only for truly stuck pods; investigate root cause |
| Forget `--context` in scripts | Could run against wrong cluster | Always specify `--context=<NAME>` in automation |
| Ignore liveness/readiness probes | Traffic to unhealthy pods; slow rollouts | Configure appropriate probes for all workloads |

---

## 7) Debugging / Troubleshooting

### Symptom: Pod stuck in `Pending`

**Likely causes:**
- Insufficient cluster resources (CPU/memory)
- No nodes match pod's nodeSelector/affinity
- PersistentVolumeClaim not bound
- ImagePullSecrets missing for private registry

**Fast checks:**
```bash
kubectl describe pod <POD> | grep -A 10 "Events:"
kubectl get nodes -o wide
kubectl describe nodes | grep -A 5 "Allocated resources"
kubectl get pvc
```

**Fix:** Scale cluster, adjust resource requests, fix PVC, or relax node constraints.

---

### Symptom: Pod stuck in `ContainerCreating`

**Likely causes:**
- Image pull failure (wrong image, no credentials)
- Volume mount failure
- ConfigMap/Secret not found

**Fast checks:**
```bash
kubectl describe pod <POD> | grep -A 10 "Events:"
kubectl get events --sort-by='.lastTimestamp' | grep <POD>
```

**Fix:** Check image name, create missing secrets/configmaps, verify volume claims.

---

### Symptom: Pod in `CrashLoopBackOff`

**Likely causes:**
- Application error/crash on startup
- Missing environment variables or config
- Liveness probe failing immediately
- OOMKilled (memory limit exceeded)
- Command/entrypoint misconfiguration

**Fast checks:**
```bash
# Check logs from crashed container
kubectl logs <POD> --previous

# Check exit code and state
kubectl describe pod <POD> | grep -E "(State|Reason|Exit Code|OOMKilled)"
kubectl get pod <POD> -o jsonpath='{.status.containerStatuses[0].lastState}'

# Debug with ephemeral container
kubectl debug -it <POD> --image=busybox --target=<CONTAINER>
```

**Fix:** Check logs for app errors, verify config, adjust resource limits if OOMKilled.

---

### Symptom: `ImagePullBackOff` / `ErrImagePull`

**Likely causes:**
- Image name/tag typo
- Private registry without imagePullSecrets
- Registry rate limits (Docker Hub)
- Network connectivity to registry

**Fast checks:**
```bash
kubectl describe pod <POD> | grep -A 5 "Events:"
kubectl get pod <POD> -o jsonpath='{.spec.containers[0].image}'
```

**Fix:**
```bash
# Verify image exists locally
docker pull <IMAGE>

# Create/update registry secret
kubectl create secret docker-registry regcred \
  --docker-server=<REGISTRY> \
  --docker-username=<USER> \
  --docker-password=<PASSWORD>

# Add to pod spec: spec.imagePullSecrets: [{name: regcred}]
```

---

### Symptom: Service not reachable

**Likely causes:**
- Selector doesn't match pod labels (no endpoints)
- Pod not Ready (readiness probe failing)
- NetworkPolicy blocking traffic
- Wrong port configuration

**Fast checks:**
```bash
# Check service has endpoints
kubectl get endpoints <SERVICE>

# Verify selector matches pod labels
kubectl get svc <SERVICE> -o wide
kubectl get pods --show-labels

# Test from within cluster
kubectl run debug --rm -it --image=busybox -- wget -qO- http://<SERVICE>:<PORT>

# Check NetworkPolicies
kubectl get networkpolicies -A
```

**Fix:** Fix label selectors, check readiness probes, review NetworkPolicies.

---

### Symptom: Node `NotReady`

**Likely causes:**
- Kubelet not running
- Node resource pressure (disk, memory, PID)
- Network connectivity issues
- Container runtime issues

**Fast checks:**
```bash
kubectl describe node <NODE> | grep -A 10 "Conditions:"
kubectl get events --field-selector involvedObject.name=<NODE>

# SSH to node if accessible
systemctl status kubelet
journalctl -u kubelet -f
```

**Fix:** Restart kubelet, clear disk space, investigate network.

---

### Symptom: OOMKilled

**Fast checks:**
```bash
kubectl describe pod <POD> | grep -i oom
kubectl get pod <POD> -o jsonpath='{.status.containerStatuses[0].lastState.terminated.reason}'
```

**Fix:** Increase memory limits, fix memory leak in application, or tune JVM/runtime heap.

---

### Universal Debug Commands

```bash
# All events sorted by time
kubectl get events -A --sort-by='.lastTimestamp'

# Resource usage
kubectl top pods
kubectl top nodes

# DNS debugging
kubectl run dnstest --rm -it --image=busybox --restart=Never -- nslookup kubernetes.default

# Network debugging (comprehensive tools)
kubectl run nettest --rm -it --image=nicolaka/netshoot --restart=Never -- /bin/bash

# Check permissions
kubectl auth can-i --list
kubectl auth can-i create pods --as=system:serviceaccount:default:mysa
```

---

## 8) Production-Ready Examples

### Deployment with Best Practices

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    app: my-app
    version: v1.2.3
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0  # Zero downtime
  template:
    metadata:
      labels:
        app: my-app
        version: v1.2.3
    spec:
      serviceAccountName: my-app  # Dedicated SA, not default
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 1000
      containers:
        - name: my-app
          image: my-registry/my-app:v1.2.3  # Pinned version
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8080
              name: http
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi
          livenessProbe:
            httpGet:
              path: /healthz
              port: http
            initialDelaySeconds: 15
            periodSeconds: 10
            timeoutSeconds: 5
            failureThreshold: 3
          readinessProbe:
            httpGet:
              path: /ready
              port: http
            initialDelaySeconds: 5
            periodSeconds: 5
            timeoutSeconds: 3
            failureThreshold: 3
          env:
            - name: LOG_LEVEL
              valueFrom:
                configMapKeyRef:
                  name: my-app-config
                  key: LOG_LEVEL
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: my-app-secrets
                  key: db-password
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL
          volumeMounts:
            - name: tmp
              mountPath: /tmp
      volumes:
        - name: tmp
          emptyDir: {}
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchLabels:
                    app: my-app
                topologyKey: kubernetes.io/hostname
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: ScheduleAnyway
          labelSelector:
            matchLabels:
              app: my-app
---
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-app-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: my-app
```

### Service + Ingress

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app
spec:
  selector:
    app: my-app
  ports:
    - port: 80
      targetPort: 8080
  type: ClusterIP
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-app
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - my-app.example.com
      secretName: my-app-tls
  rules:
    - host: my-app.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-app
                port:
                  number: 80
```

### NetworkPolicy (Default Deny + Allow Specific)

```yaml
# Default deny all ingress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress
---
# Allow specific traffic
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: my-app-network-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: my-app
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
        - namespaceSelector:
            matchLabels:
              name: ingress-nginx
      ports:
        - port: 8080
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: postgres
      ports:
        - port: 5432
    - to:  # Allow DNS
        - namespaceSelector: {}
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - port: 53
          protocol: UDP
```

---

## 9) Safety / Security Notes

### RBAC Best Practices

```bash
# Check your permissions
kubectl auth can-i --list

# Check specific permission
kubectl auth can-i create pods

# Check as another user/SA
kubectl auth can-i create pods --as=system:serviceaccount:default:mysa
```

- Use least-privilege: avoid `cluster-admin` for regular operations
- Prefer namespace-scoped Roles over ClusterRoles
- Never use `system:masters` group for users after bootstrapping
- Audit RBAC regularly

### RBAC Example

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-app
  namespace: production
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: my-app-role
  namespace: production
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get", "list"]
- apiGroups: [""]
  resources: ["secrets"]
  resourceNames: ["my-app-secrets"]  # Named resources only
  verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: my-app-binding
  namespace: production
subjects:
- kind: ServiceAccount
  name: my-app
  namespace: production
roleRef:
  kind: Role
  name: my-app-role
  apiGroup: rbac.authorization.k8s.io
```

### Secret Management

- Secrets are base64-encoded, NOT encrypted by default
- Enable encryption at rest: configure `EncryptionConfiguration`
- Consider external secret managers: HashiCorp Vault, AWS Secrets Manager, sealed-secrets

### Pod Security

- Use Pod Security Standards (PSS): `restricted`, `baseline`, `privileged`
- Enforce with Pod Security Admission (PSA) labels on namespaces:
  ```yaml
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/warn: restricted
  ```

### Security Checklist

- [ ] Enable RBAC; avoid `system:masters` group for users
- [ ] Use namespaces for isolation
- [ ] Set `runAsNonRoot: true` and drop all capabilities
- [ ] Enable `readOnlyRootFilesystem` where possible
- [ ] Use NetworkPolicies to restrict pod-to-pod traffic
- [ ] Scan images for vulnerabilities (Trivy, Snyk)
- [ ] Enable audit logging
- [ ] Encrypt secrets at rest
- [ ] Use Pod Security Standards (restricted profile for prod)
- [ ] Rotate certificates before expiry (< 1 year recommended)

---

## 10) Useful Aliases & Shortcuts

Add to `~/.bashrc` or `~/.zshrc`:

```bash
# Essential aliases
alias k='kubectl'
alias kgp='kubectl get pods'
alias kgpa='kubectl get pods -A'
alias kgs='kubectl get svc'
alias kgd='kubectl get deployments'
alias kga='kubectl get all'
alias kgn='kubectl get nodes'
alias kd='kubectl describe'
alias kdp='kubectl describe pod'
alias kl='kubectl logs'
alias klf='kubectl logs -f'
alias ke='kubectl exec -it'
alias kaf='kubectl apply -f'
alias kdf='kubectl delete -f'
alias kccc='kubectl config current-context'
alias kcuc='kubectl config use-context'

# Quick namespace switching
alias kns='kubectl config set-context --current --namespace'

# Get current namespace
alias kn='kubectl config view --minify -o jsonpath="{..namespace}"'

# Get all resources in namespace
kall() { kubectl get all,cm,secret,ing,pvc -n "${1:-default}"; }

# Watch pods
alias kwp='kubectl get pods -w'

# Quick debug pod
kdebug() { kubectl run debug-$RANDOM --rm -it --image=nicolaka/netshoot --restart=Never -- /bin/bash; }

# Dry run helper
alias kdry='kubectl apply --dry-run=client -o yaml -f'
```

### Enable Shell Completion

```bash
# Bash
echo 'source <(kubectl completion bash)' >> ~/.bashrc
echo 'complete -o default -F __start_kubectl k' >> ~/.bashrc  # For alias

# Zsh
echo 'source <(kubectl completion zsh)' >> ~/.zshrc
```

---

## 11) Versioning & Maintenance Metadata

| Field | Value |
|-------|-------|
| **Doc version** | 2.0.0 |
| **K8s versions covered** | 1.30, 1.31 |
| **Validated on** | 2025-01-08 |
| **Author** | CheatSheetForge |

### Drift Risks (check quarterly)

- Gateway API graduating may change Ingress patterns
- Pod Security Admission replacing PodSecurityPolicy (PSP removed in 1.25)
- kubectl plugins ecosystem evolving (Krew)
- New autoscaling/v2 features
- Security context requirements may change

### Revalidation Checklist

- [ ] Check Kubernetes release notes for deprecated commands
- [ ] Verify `kubectl api-resources` output on target cluster
- [ ] Test all example YAML against target cluster version
- [ ] Review security recommendations against CIS benchmarks
- [ ] Check if new admission controllers affect examples
- [ ] Validate NetworkPolicy syntax changes

---

## 12) Further Reading

| Resource | Link |
|----------|------|
| Official kubectl Reference | https://kubernetes.io/docs/reference/kubectl/ |
| Kubernetes Quick Reference | https://kubernetes.io/docs/reference/kubectl/quick-reference/ |
| API Reference | https://kubernetes.io/docs/reference/kubernetes-api/ |
| Pod Security Standards | https://kubernetes.io/docs/concepts/security/pod-security-standards/ |
| Security Checklist | https://kubernetes.io/docs/concepts/security/security-checklist/ |
| Network Policies | https://kubernetes.io/docs/concepts/services-networking/network-policies/ |
| kubectl Plugins (Krew) | https://krew.sigs.k8s.io/ |

---

## Quick Reference Card

```
CRUD Operations:
  get, describe, create, apply, edit, patch, delete, scale

Output Formats:
  -o wide | yaml | json | name | jsonpath='{...}' | custom-columns=...

Scope:
  -n <namespace>    Specific namespace
  -A                All namespaces
  -l key=value      Filter by label

Safety:
  --dry-run=client  Preview without executing
  kubectl diff -f   Show what would change

Debug:
  logs [-f] [--previous] [-c container] [--tail=N]
  exec -it <pod> -- /bin/sh
  debug -it <pod> --image=busybox --target=<container>
  port-forward <pod|svc> <local>:<remote>
  describe <resource>

Context:
  config get-contexts
  config use-context <name>
  config current-context
  config set-context --current --namespace=<ns>

Rollouts:
  rollout status|history|undo|restart deployment/<name>

Resource Short Names:
  po=pods  svc=services  deploy=deployments  rs=replicasets
  ns=namespaces  cm=configmaps  pv=persistentvolumes
  pvc=persistentvolumeclaims  ing=ingresses  netpol=networkpolicies
```
