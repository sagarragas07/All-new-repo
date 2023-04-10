
provider "aws" {}



resource "aws_vpc" "vpc" {
  cidr_block       = var.cidr_blocks[0]
  instance_tenancy = "default"

  tags = {
    Name = "demo_vpc"
  }
}


resource "aws_subnet" "pub" {
  vpc_id     = aws_vpc.vpc.id
  cidr_block = var.cidr_blocks

  tags = {
    Name = "public_ sub"
  }
}

 variable "cidr_blocks" {
    type = list(string)
}