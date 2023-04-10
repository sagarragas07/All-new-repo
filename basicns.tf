provider "aws" {
    region = "ap-south-1"
    profile = "sagar-terraform"
}

//this is a string variable

variable "firststring" {
    type = string
    default = "this is my first string"
}

output "myfirstoutput" {
    value = "${var.firststring}"
}

output "mymultilineoutput" {
    value = "$${var.multilinestring newline}"
}

#myfirstoutput = "this is my first string"
#mymultilineoutput = "${var.multilinestring newline}"


//this is my maps example
 
variable "mapexample" {
    type = map
    default = {
        "useast" = "ami1"
        "euwest" = "ami2"
    }
}

output "mapoutput" {
    value = "${var.mapexample["useast"]}"
}

#mapoutput = "ami1"
#myfirstoutput = "this is my first string"
#mymultilineoutput = "${var.multilinestring newline}"

//this is array/lists

variable "mysecuritygrouplist" {
    type = list
    default = ["sg1", "sg2", "sg3"]
}

output "sgoutput" {
    value = "${var.mysecuritygrouplist[0]}"
}

#mapoutput = "ami1"
#myfirstoutput = "this is my first string"
#mymultilineoutput = "${var.multilinestring newline}"
#sgoutput = "sg1"

//this is booleans

variable "testbool"  {
    default = true
}

output "booloutput"{
    value = "${var.testbool}"
}

#booloutput = true
#mapoutput = "ami1"
#myfirstoutput = "this is my first string"
#mymultilineoutput = "${var.multilinestring newline}"
#sgoutput = "sg1"

//input and output variables in powershell

variable "myinputvariable" {
    type = string
}

output "myoutputvariable" {
    value ="${var.myinputvariable}"
}

#myoutputvariable = "this is my test input"

variable "myinputvariable1" {
    type = string
}

output "myoutputvariable1" {
    sensitive = true
    value ="${var.myinputvariable1}"
}

#myoutputvariable1 = <sensitive>
