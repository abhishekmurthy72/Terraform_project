provider "aws" {
  region = "us-east-1"
}



resource "aws_instance" "instance1" {
  ami = var.ami_value
  instance_type = var.instance_type_value
    # Ensure associate_public_ip_address is defined explicitly
  associate_public_ip_address = true  # or false, based on your requirement
}

resource "aws_s3_bucket" "abhishekmurthy72_bucket" {
    bucket = "abhishekmurthy-bucket-xyz"
    force_destroy = true
}
# nothing just test...
