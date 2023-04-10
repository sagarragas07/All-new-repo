provider "aws" {
    region = "ap-south-1"
    profile = "sagar-terraform"
}    

resource "aws_s3_bucket" "mybucket" {
    bucket = "mybucket-tf-2022-05-1076"
    acl = "private"
}

resource "aws_s3_bucket_object" "file_upload"{
    bucket = "mybucket-tf-2022-05-1076"
    key    = "sampleobject.txt"
    source = "C:\\Users\\SMUTHYALA\\Desktop\\sampletest.txt"
    etag   = "filemd5("C:\\Users\\SMUTHYALA\\Desktop\\sampletest.txt")
}
  