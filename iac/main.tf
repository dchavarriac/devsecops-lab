provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "public_bucket" {
  bucket = "devsecops-test-public"
  acl    = "public-read"
}
