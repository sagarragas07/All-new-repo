provider "aws" {
  region  =  "us-east-1"
  access_key = "AKIAWRFJHTO6KHEADNPF"
  secret_key =   "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"  
}  

resource "aws_instance" "server" {
  ami           = "ami-09d3b3274b6c5d4aa"
  instance_type = "t2.micro"
  subnet_id = "subnet-0bda7db1edad90dad"
  security_groups = ["sg-0dc5c035891b5091f"]
  key_name = aws_key_pair.key_id

  tags = {
    name = "terraform.server"
  }
}

resource "aws_key_pair" "key" {
    key_name  =  "sample"
    public_key  = "-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----"
}
                                                                                                                                                                                                                            -----BEGIN OPENSSH PRIVATE KEY-----
