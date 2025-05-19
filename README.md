> ⚠️ This application is **intentionally vulnerable**. It is built for demonstration purposes only. Do not deploy this in production environments.


## 🔐 Secure CI/CD Pipeline Project with Flask, Docker, Semgrep & Trivy

This project demonstrates a complete **DevSecOps workflow** that integrates security best practices into a CI/CD pipeline using:

- A containerized Python Flask app
- Static and dynamic analysis tools (Semgrep & Trivy)
- GitHub Actions for automated scans
- Custom Semgrep rules for GDPR compliance
- SARIF integration for GitHub Code Scanning Alerts

---

## 🚀 Project Overview

This pipeline catches:

- **Insecure code** patterns (e.g., `eval()`, `os.system`, hardcoded secrets)
- **Dockerfile misconfigurations** (e.g., root user, ENV secrets)
- **Container vulnerabilities** (e.g., CVEs in OS or dependencies)
- **GDPR non-compliant IaC configurations** (e.g., public S3 buckets)

---

## 🧱 Tech Stack

| Component       | Purpose                                       |
|-----------------|-----------------------------------------------|
| Python (Flask)  | Lightweight web application                   |
| Docker          | Containerization of the Flask app             |
| GitHub Actions  | CI/CD pipeline automation                     |
| Semgrep         | Static Application Security Testing (SAST)    |
| Trivy           | Container & dependency vulnerability scanner  |
| SARIF           | Standard output format for security results   |

---

## 🧪 Security Tooling

### 🔹 Semgrep

- Scans Python code for:
    - Use of `eval()`, `os.system()`, `subprocess.run()`
    - Flask `debug=True`
    - Hardcoded secrets like `password = "..."` or `api_key = "..."`

- Uses **custom GDPR rules** defined in `semgrep-rules/`
- Generates **SARIF output** to show results in GitHub's **Code Scanning** tab

### 🔹 Trivy

- Scans Docker image for vulnerabilities
- Targets **HIGH** and **CRITICAL** CVEs
- Generates `trivy-report.json` for detailed results

To run locally:

```bash
trivy image --severity HIGH,CRITICAL --format json --output trivy-report.json app-sec-demo
```

---

## ⚙️ GitHub Actions Workflow

**Trigger:** On every `push` or `pull_request` to `main`

**Key steps:**

- Set up Python and dependencies
- Run Semgrep with GDPR rules
- Upload results to GitHub Code Scanning (SARIF)
- Build Docker image
- Run Trivy to scan image for CVEs

---

## 📂 Project Structure

```
secure-ci-pipeline/
├── app/
│   ├── main.py
│   ├── requirements.txt
├── Dockerfile
├── semgrep-rules/
│   ├── gdpr-python.yaml
│   ├── gdpr-docker.yaml
│   └── gdpr-iac.yaml
├── .github/
│   └── workflows/
│       └── security.yml
├── trivy-report.json
└── README.md
```

---

## 📸 Results Preview

- ✅ GitHub Actions: CI/CD pipeline runs on commit
- 📤 Semgrep SARIF findings shown in GitHub's Security tab
- 📄 `trivy-report.json`: exported local scan with CVEs

---

## 🧠 What I Taught

- End-to-end DevSecOps setup in a real-world pipeline
- Writing custom Semgrep rules for AppSec and GDPR
- Automating fail-fast gates with Trivy and SARIF integration
- CI/CD security scanning with GitHub Actions

---

## 👤 Author

**Paul D.**  
Security Automation Engineer
