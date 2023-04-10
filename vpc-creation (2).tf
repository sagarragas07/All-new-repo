provider "aws" {
    access_key = "AKIAWRFJHTO6KHEADNPF"
    secret_key = "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"
    region = "ap-south-1"
}

# 1. vpc create:

resource "aws_vpc" "my-vpc" {
  cidr_block = "10.0.0.0/16"

  
  tags = {
    Name = "prod-vpc"
  }
}

# 2. create internet gateway:

resource "aws_internet_gateway" "my-igw" {
  vpc_id = aws_vpc.my-vpc.id

  tags = {
    Name = "prod-igw"
  }
}

# 3. create custom route table:

resource "aws_route_table" "prod-route-table" {
    vpc_id = aws_vpc.my-vpc.id
  
    route {
      cidr_block = "0.0.0.0/0"
      gateway_id = aws_internet_gateway.my-igw.id
    }
  
    route {
      ipv6_cidr_block        = "::/0"
      gateway_id = aws_internet_gateway.my-igw.id
    }
  
    tags = {
      Name = "prod-rt"
    }
  }


# 4. create subnet:

resource "aws_subnet" "subnet-1" {
  vpc_id     = aws_vpc.my-vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "ap-south-1a"

  tags = {
    Name = "prod-subnet"
  }
}

# 5. Associate subnet with route table:

resource "aws_route_table_association" "aaa" {
    subnet_id      = aws_subnet.subnet-1.id
    route_table_id = aws_route_table.prod-route-table.id
  }


  # 6. create security group to allow port 22, 80, 443:

  resource "aws_security_group" "allow_web" {
    name        = "allow_web_traffic"
    description = "Allow web inbound traffic"
    vpc_id      = aws_vpc.my-vpc.id
  
    ingress {
      description      = "HTTPS from VPC"
      from_port        = 443
      to_port          = 443
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]
    }
    ingress {
        description      = "HTTP from VPC"
        from_port        = 80
        to_port          = 80
        protocol         = "tcp"
        cidr_blocks      = ["0.0.0.0/0"]
      }
      ingress {
        description      = "SSH from VPC"
        from_port        = 22
        to_port          = 22
        protocol         = "tcp"
        cidr_blocks      = ["0.0.0.0/0"]
      }
  
    egress {
      from_port        = 0
      to_port          = 0
      protocol         = "-1"
      cidr_blocks      = ["0.0.0.0/0"]
    }
  
    tags = {
      Name = "allow_web"
    }
  }

  # 7. create a network interface with an ip in the subnet that was created in step4:

  resource "aws_network_interface" "web-server-nic" {
    subnet_id       = aws_subnet.subnet-1.id
    private_ips     = ["10.0.1.50"]
    security_groups = [aws_security_group.allow_web.id]
     }

# 8. Assign an elastic IP to the network interface created in step7:

resource "aws_eip" "my-eip" {
    vpc                       = true
    network_interface         = aws_network_interface.web-server-nic.id
    associate_with_private_ip = "10.0.1.50"
    depends_on                = [aws_internet_gateway.my-igw]
}

# 9. create linux server and install/enable apache2:

resource "aws_instance" "ec2-server" {
    ami = "ami-0e6329e222e662a52"
    instance_type = "t2.micro"
    availability_zone = "ap-south-1a"
    key_name = "mumbai"

    network_interface{
        device_index = 0
        network_interface_id = aws_network_interface.web-server-nic.id
    }

    user_data = <<-EOF
                  #!/bin/bash
                  sudo yum update -y
                  sudo yum install httpd -y
                  sudo systemctl start httpd
                  sudo bash -c 'echo my first web server > /var/www/html/index.html'
                  EOF
    tags = {
        Name = "web-server"
    }
                
}

output "server_public_ip" {
  value = aws_eip.my-eip.public_ip
}

output "server_private_ip" {
  value = aws_instance.ec2-server.private_ip
}

output "server_id" {
  value = aws_instance.ec2-server.id 
}