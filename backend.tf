terraform {
  backend "s3" {
    bucket = "abhishekmurthy-bucket-xyz"
    region = "us-east-1"
    key = "terraform.tfstate"

  }
}
# This is a test file
