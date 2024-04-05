output "public_ip_value" {
  value = aws_instance.instance1.public_ip
}

output "subnet" {
  value = aws_instance.instance1.subnet_id
}