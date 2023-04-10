provider "aws" {
  region  =  "us-east-1"
  access_key = "AKIAWRFJHTO6KHEADNPF"
  secret_key =   "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"  
}  

resource "aws_instance" "ins" {
    ami            =   "ami-09d3b3274b6c5d4aa"
    subnet_id      =   "subnet-00f6e9a297a836e5a" 
    instance_type  =   "t2.micro"
    tags  = {
       Name =  "my-first-ins.tf"
      } 
}     