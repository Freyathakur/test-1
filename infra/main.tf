provider "aws" {
region = "us-east-1"
}

resource "aws_instance" "web" {
  instance_type   =  "t3.micro"
  ami = "ami-0c55b159cbfafe1f0"
}
