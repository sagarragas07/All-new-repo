provider "aws" {
    access_key = "AKIAWRFJHTO6KHEADNPF"
    secret_key = "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"
    region = "ap-south-1"
}

module "s3_bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket = "my-s3-bucket798944bucket"
  acl    = "private"

  versioning = {
    enabled = true
  }

}

module "s3_bucket_for_logs" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket = "my-s3-bucket-for-logs"
  acl    = "log-delivery-write"

  # Allow deletion of non-empty bucket
  force_destroy = true

  attach_elb_log_delivery_policy = true
}

