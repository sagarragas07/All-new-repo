provider "aws" {
    region = "ap-south-1"
    profile = "sagar-terraform"
}    

variable "vpcid" {
    type   = string
    default = "vpc-03113555228ef0a3a"
}
resource "aws_security_group" "terraform_ec2_sg" {
    name         = "terraform_ec2_sg"
    description  = "terraform course sg for ec2 instance"
    vpc_id       = "${var.vpcid}"

    ingress {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"] 
    }

    egress {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

variable "amiid" {
    default = "ami-0e6329e222e662a52"
}

resource "aws_instance" "terraform_ec2_instance" {
    ami               =  "${var.amiid}"
    instance_type     =  "t2.micro"
    key_name          =   "window-dlt.kpair"
    vpc_security_group_ids  = ["${aws_security_group.terraform_ec2_sg.id}"]
}