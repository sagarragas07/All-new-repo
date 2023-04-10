provider "aws" {
  region  =  "us-east-1"
  access_key = "AKIAWRFJHTO6KHEADNPF"
  secret_key =   "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"  
}  

# creating VPC
resource "aws_vpc" "demovpc" {
  cidr_block = "10.0.0.0/16"
  instance_tenancy = "default"
  tags = {
    Name = "Demo VPC"
}
}

# creating 1st web subnet
resource "aws_subnet" "public-subnet-1" {
  vpc_id = "${aws_vpc.demovpc.id}"
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone = "us-east-1a"
  tags = {
    Name = "Web Subnet 1"
}
}
# creating 2nd web subnet
resource "aws_subnet" "public-subnet-2" {
  vpc_id = "${aws_vpc.demovpc.id}"
  cidr_block = "10.0.2.0/24"
  map_public_ip_on_launch = true
  availability_zone = "us-east-1b"
  tags = {
    Name = "Web Subnet 2"
}
}
# creating 1st application subnet
resource "aws_subnet" "application-subnet-1" {
  vpc_id = "${aws_vpc.demovpc.id}"
  cidr_block = "10.0.3.0/24"
  map_public_ip_on_launch = false
  availability_zone = "us-east-1a"
  tags = {
    Name = "Application Subnet 1"
}
}

# creating 2nd application subnet
resource "aws_subnet" "application-subnet-2" {
  vpc_id = "${aws_vpc.demovpc.id}"
  cidr_block = "10.0.4.0/24"
  map_public_ip_on_launch = false
  availability_zone = "us-east-1b"
  tags = {
    Name = "Application Subnet 2"
}
}
# Create Database Private Subnet
resource "aws_subnet" "database-subnet-1" {
  vpc_id = "${aws_vpc.demovpc.id}"
  cidr_block = "10.0.5.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "Database Subnet 1"
}
}
# Create Database Private Subnet
resource "aws_subnet" "database-subnet-2" {
  vpc_id = "${aws_vpc.demovpc.id}"
  cidr_block = "10.0.6.0/24"
  availability_zone = "us-east-1b"
  tags = {
    Name = "Database Subnet 1"
}
}

# creating Internet Gateway
resource "aws_internet_gateway" "demogateway" {
  vpc_id = "${aws_vpc.demovpc.id}"
   tags ={
     Name ="IGW"
}
}

# creating Route Table
resource "aws_route_table" "route" {
  vpc_id = "${aws_vpc.demovpc.id}"
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.demogateway.id}"
 }
  tags = {
    Name = "Route to internet"
 }
}
# Associating Route Table
resource "aws_route_table_association" "rt1" {
  subnet_id = "${aws_subnet.public-subnet-1.id}"
  route_table_id = "${aws_route_table.route.id}"
}
# Associating Route Table
resource "aws_route_table_association" "rt2" {
  subnet_id = "${aws_subnet.public-subnet-2.id}"
  route_table_id = "${aws_route_table.route.id}"
}

# creating Security Group
resource "aws_security_group" "demosg" {
  vpc_id = "${aws_vpc.demovpc.id}"
# Inbound Rules

# HTTP access from anywhere
  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
}

# HTTPS access from anywhere
ingress {
  from_port = 443
  to_port = 443
  protocol = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
}

# SSH access from anywhere
ingress {
  from_port = 22
  to_port = 22
  protocol = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
}
# Outbound Rules

# Internet access to anywhere
egress {
  from_port = 0
  to_port = 0
   protocol = "-1"
  cidr_blocks = ["0.0.0.0/0"]
}
  tags = {
    Name = "Web SG"
}
}

# Create Database Security Group
resource "aws_security_group" "database-sg" {
  name = "Database SG"
  description = "Allow inbound traffic from application layer"
  vpc_id = aws_vpc.demovpc.id
  ingress {
    description = "Allow traffic from application layer"
    from_port = 3306
    to_port = 3306
    protocol = "tcp"
    security_groups = [aws_security_group.demosg.id]
}
  egress {
    from_port = 32768
    to_port = 65535
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
}
  tags = {
    Name = "Database SG"
}
}

# Create Database Security Group
resource "aws_security_group" "database-sg1" {
  name = "Database SG1"
  description = "Allow inbound traffic from application layer"
  vpc_id = aws_vpc.demovpc.id
  ingress {
    description = "Allow traffic from application layer"
    from_port = 3306
    to_port = 3306
    protocol = "tcp"
    security_groups = [aws_security_group.demosg.id]
}
  egress {
    from_port = 32768
    to_port = 65535
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
}
  tags = {
    Name = "Database SG"
}
}

# creating 1st EC2 instance in Public Subnet
resource "aws_instance" "demoinstance" {
  ami = "ami-09d3b3274b6c5d4aa"
  instance_type = "t2.micro"
  count = 1
  key_name = "dlta123"
  vpc_security_group_ids = ["${aws_security_group.demosg.id}"]
  subnet_id = "${aws_subnet.public-subnet-1.id}"
  associate_public_ip_address = true
  user_data = <<-EOF
                  #!/bin/bash
                  sudo yum update -y
                  sudo yum install httpd -y
                  sudo systemctl start httpd
                  sudo bash -c 'echo my first app server > /var/www/html/index.html'
                  EOF
  tags = {
   Name = "My Public Instance"
}
}
# creating 2nd EC2 instance in Public Subnet
resource "aws_instance" "demoinstance1" {
  ami = "ami-0c4e4b4eb2e11d1d4"
  instance_type = "t2.micro"
  count = 1
  key_name = "dlta123"
  vpc_security_group_ids = ["${aws_security_group.demosg.id}"]
  subnet_id = "${aws_subnet.public-subnet-2.id}"
  associate_public_ip_address = true
  user_data = <<-EOF
                  #!/bin/bash
                  sudo yum update -y
                  sudo yum install httpd -y
                  sudo systemctl start httpd
                  sudo bash -c 'echo my first web server > /var/www/html/index.html'
                  EOF
  tags = {
    Name = "My Public Instance 1"
}
}




# creating RDS Instance
resource "aws_db_subnet_group" "default" {
  name = "main"
  subnet_ids = [aws_subnet.database-subnet-1.id, aws_subnet.database-subnet-2.id]
  tags = {
    Name = "My DB subnet group"
}
}
resource "aws_db_instance" "default" {
  allocated_storage = 10
  db_subnet_group_name = aws_db_subnet_group.default.id
  engine = "mysql"
  engine_version = "8.0.30"
  instance_class = "db.t2.micro"
  multi_az = true
  db_name = "db_1"
  username = "SagarRagas"
  password = "sagar1080"
  skip_final_snapshot = true
  vpc_security_group_ids = [aws_security_group.database-sg.id]
  tags = {
    DB_identifier= "DB-1"
  }
}