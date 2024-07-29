terraform {
  backend "s3" {
    bucket = "abhishekmurthy-bucket-xyz"
    region = "us-east-1"
    key = "terraform.tfstate"

  }
}


