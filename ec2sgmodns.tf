provider "aws" {
    region = "ap-south-1"
    profile = "sagar-terraform"
}    

module "tttapp-subnet" {
    source = "./modules/subnet"
}    