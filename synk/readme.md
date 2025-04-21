# Create a new account 
https://snyk.io/



snyk container monitor myapp:latest

snyk container test myapp:latest

```

Feature                      | Command           |        What It Scans
Source Code (SAST)           | snyk code test    | Vulnerabilities in code itself
Dependencies (SCA)           | snyk test         | Open-source libraries (CVEs)
Docker Images                | snyk container test | OS-level & installed packages
Kubernetes YAML              | snyk iac test     | K8s security issues
Terraform / CloudInfra       | snyk iac test     | IaC config (Terraform, etc.)
Full Git Repos | GitHub Integration | Everything above on every push

```