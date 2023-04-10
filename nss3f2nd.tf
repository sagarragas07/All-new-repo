provider "aws" {
  region  =  "us-east-1"
  access_key = "AKIAWRFJHTO6KHEADNPF"
  secret_key =   "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"  
}  


resource "aws_s3_bucket" "mybucket123" {
  bucket = "my-tf-test-bucketsagar"
  acl    = "private"
  region = "us-east-1"

  tags = {
    Environment = "Dev"
  }
}
  
resource "aws_s3_bucket_object" "myfirstobject" {
  bucket = "${aws_s3_bucket.mybucket123.id}"
  key    = "testfile.txt"
  source = "C:\\Users\\SMUTHYALA\\Documents\\testfile.txt"
  etag = filemd5("C:\\Users\\SMUTHYALA\\Documents\\testfile.txt")
}
