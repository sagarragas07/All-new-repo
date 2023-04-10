provider "aws" {
  region  =  "us-east-1"
  access_key = "AKIAWRFJHTO6KHEADNPF"
  secret_key =   "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"  
}  


module "ec2module" {
    source = "./ec2module"  
}