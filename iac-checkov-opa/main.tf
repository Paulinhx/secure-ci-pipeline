provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "insecure_bucket" {
  bucket = "iac-checkov-opa-demo-bucket-1234"
  acl    = "public-read"  # 🚨 Deliberately insecure for demo/testing

  tags = {
    Name        = "Insecure S3 Bucket"
    Environment = "Dev"
  }
}
