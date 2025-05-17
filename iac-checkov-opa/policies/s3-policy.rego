package policy

deny[msg] {
  input.resource_type == "aws_s3_bucket"
  input.config.acl == "public-read"
  msg = "S3 bucket should not use public-read ACL"
}
