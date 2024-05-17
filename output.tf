output "public_ip_value" {
  value = aws_instance.instance1.public_ip
}

output "subnet" {
  value = aws_instance.instance1.subnet_id
}

output "s3_bucket" {
  value = aws_s3_bucket.abhishekmurthy72_bucket
}

#output "s3_bucket" {
 # value = aws_s3_bucket.abhishekmurthy72_bucket
#}
