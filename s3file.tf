provider "aws" {
    access_key = "AKIAWRFJHTO6KHEADNPF"
    secret_key = "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"
    region = "ap-south-1"
}

resource "aws_s3_bucket" "my-bucket" {
  bucket = "my-bucket-23-2022893439"
  acl    = "private"

  tags = {
    Environment = "Dev"

  }
  
  versioning {
    enabled = true
  }
}

# .........single file upload..........

resource "aws_s3_bucket_object" "file_upload"{
  bucket = "my-bucket-23-2022893439"
  key    = "student.xlsx"
  source = "C:\\Users\\SMUTHYALA\\Desktop\\sreenshot-folder\\2222.png"
  etag   = filemd5("C:\\Users\\SMUTHYALA\\Desktop\\sreenshot-folder\\2222.png")
}

# .............multi file upload...........
resource "aws_s3_bucket_object" "multi-file-upload" {
  for_each = fileset("C:\\Users\\SMUTHYALA\\Desktop\\sreenshot-folder", "*")

  bucket = "my-bucket-23-2022893439"
  key    = each.value
  source = "C:\\Users\\SMUTHYALA\\Desktop\\sreenshot-folder\\${each.value}"
  etag   = filemd5("C:\\Users\\SMUTHYALA\\Desktop\\sreenshot-folder\\${each.value}")
}

