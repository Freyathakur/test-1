provider "aws" {
region = "us-east-1"
}

resource "aws_instance" "web" {
  instance_type   =  "t3.micro"
}
