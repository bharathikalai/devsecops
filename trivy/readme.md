# 🔍 Trivy Setup & Usage Guide

## 📦 Install Trivy on Your Local Machine

### Step 1: Download the Trivy Debian Package
```bash
wget https://github.com/aquasecurity/trivy/releases/download/v0.45.0/trivy_0.45.0_Linux-64bit.deb
```

### Step 2: Install the Downloaded Package
```bash
sudo dpkg -i trivy_0.45.0_Linux-64bit.deb
```

### Step 3: Fix Any Missing Dependencies
```bash
sudo apt-get install -f
```

### Step 4: Verify Trivy Installation
```bash
trivy --version
```

---

## 🐳 Docker Integration

### Build and Scan a Docker Image
```bash
docker build -t my-python-app .
trivy image my-python-app
```

---

## 🤖 Trivy in Jenkins (CI/CD)

### Use Trivy with Exit Codes in Jenkins Pipeline
```bash
trivy --no-progress --exit-code 1 --severity HIGH,CRITICAL your_docker_image
```

---

## 🧪 What Trivy Can Scan

### 1. Docker Image
```bash
trivy image my-docker-image
```

### 2. File Systems
```bash
trivy fs /path/to/directory
```

### 3. Git Repositories
```bash
trivy repo --format table https://github.com/bharathikalai/Docker
```

### 4. Infrastructure-as-Code (IaC) Files

- **Terraform**
```bash
trivy config -f terraform /path/to/terraform/files
```

- **CloudFormation**
```bash
trivy config -f cloudformation /path/to/cloudformation/files
```

- **Kubernetes**
```bash
trivy config -f kubernetes /path/to/kubernetes/manifests
```

### 5. Dependency Files
```bash
trivy fs --vuln-type=os,library --format json -o report.json /path/to/requirements.txt
```

---

## ☁️ AWS Scanning with Trivy

### 1. Scan EC2 Service
```bash
trivy aws --service ec2
```

### 2. Generate JSON Report
```bash
trivy aws --format json --output report.json
```

### 3. Scan Specific AWS AMI
```bash
trivy vm --scanners vuln ami:ami-022ce6f32988af5fa
```

### 4. Scan AWS EBS Snapshot
```bash
trivy vm ebs:${your_ebs_snapshot_id}
```