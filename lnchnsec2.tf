provider "aws" {
  region  =  "us-east-1"
  access_key = "AKIAWRFJHTO6KHEADNPF"
  secret_key =   "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"  
} 

variable "vpcid" {
    type = string
    default = "vpc-028af64e3368b2ae2"
}
resource "aws_security_group" "terraformec2-sg" {
  name        = "terraformec2-sg"
  description = "terraformec2-sg for ec2 instance"
  vpc_id      = "${var.vpcid}"

  ingress {
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
}

  egress {
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]

}

  tags = {
    Name = "allow_tls"
  }
} 

variable "amiid" {
    default = "ami-09d3b3274b6c5d4aa"
}

resource "aws_instance" "terraform_ec2_instance" {
  ami           = "${var.amiid}"
  instance_type = "t2.micro"
  key_name ="dlta123"
  security_groups = ["${aws_security_group.terraformec2-sg.id}

  tags = {
    Name = "terraform ec2 ins"
  }
}