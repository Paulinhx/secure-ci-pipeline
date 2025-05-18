# ✅ Project 2: Secure Infrastructure-as-Code Pipeline with Terraform + Checkov + OPA

This project demonstrates how to secure Infrastructure-as-Code (IaC) using:

- **Terraform** to provision AWS resources (e.g., S3 buckets)
- **Checkov** to scan Terraform code for misconfigurations
- **OPA (Open Policy Agent)** with custom Rego policies
- **GitHub Actions** to run automated security scans on push

---

## 📁 Project Structure

```
iac-checkov-opa/
├── main.tf                      # Insecure AWS S3 bucket (demo)
├── policies/
│   └── s3-policy.rego           # OPA policy to block public-read buckets
├── .github/
│   └── workflows/
│       └── iac-security.yml     # CI pipeline for Checkov + OPA
├── requirements.txt             # Checkov version pin
├── dev-requirements.txt         # Optional: pre-commit, opa-python, etc.
└── README.md
```

---

## 🛠 Setup (Local)

```bash
# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Checkov
pip install -r requirements.txt

# Run Checkov scan
checkov -d .
```

Install OPA binary (macOS):

```bash
brew install opa
opa eval --input main.tf --data policies --format pretty "data.policy"
```

---

## 🧪 GitHub Actions Workflow

CI/CD pipeline runs on push to `feature/iac-security`:

- Installs Checkov and runs scan
- Installs OPA and runs policy evaluation
- Blocks merge on failure (via `exit-code 1`)

```bash
checkov -d ./iac-checkov-opa --framework terraform --exit-code 1
opa eval --input ./iac-checkov-opa/main.tf --data ./iac-checkov-opa/policies --format pretty 'data.policy'
```

---

## 📌 Compliance Logic

The following insecure Terraform config is used for testing:

```hcl
acl = "public-read"
```

OPA policy to block it:

```rego
deny[msg] {
  input.resource_type == "aws_s3_bucket"
  input.config.acl == "public-read"
  msg = "S3 bucket should not use public-read ACL"
}
```

---

## 🔄 Next Steps

- Add more Rego policies for versioning, encryption, tagging
- Convert `terraform plan` into JSON input for deeper analysis
- Integrate SARIF output for GitHub Security dashboard

---

## 👨‍💻 Author

**Paul D.**  
Security Automation Engineer  
🔗 [github.com/Paulinhx](https://github.com/Paulinhx)
