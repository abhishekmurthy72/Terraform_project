
Terraform AWS EC2 Instance Setup
================================

This Terraform project automates the deployment of an EC2 instance on Amazon Web Services (AWS) using Ubuntu Linux as the default operating system and t2.micro as the default instance type. Users can easily customize the deployment by editing variables in the `terraform.tfvars` file and adding more resources in the `main.tf` file..

Prerequisites
-------------

Before using this Terraform project, ensure you have the following prerequisites installed:

*   [Terraform](https://www.terraform.io/downloads.html)

Usage
-----

1.  **Clone the Repository:** Clone this repository to your local machine.

    git clone https://github.com/your-username/terraform-ec2-setup.git

3.  **Initialize Terraform:** Navigate to the project directory and initialize Terraform.

    cd terraform-ec2-setup
    terraform init

5.  **Edit Variables:** Open the `terraform.tfvars` file and edit the variables according to your requirements. You can change the AMI image, instance type, and any other variables defined in the file.
6.  **Review Terraform Plan:** Run `terraform plan` to review the execution plan and ensure everything looks correct. 

    terraform plan

8.  **Deploy EC2 Instance:** If the plan looks satisfactory, apply the changes to deploy the EC2 instance.

    terraform apply

10.  **Access EC2 Instance:** Once the deployment is complete, you can access your EC2 instance using the provided public IP or DNS name.
11.  **Destroy Resources (Optional):** To destroy the deployed resources and terminate the EC2 instance, run:

    terraform destroy

Files
-----

*   `main.tf`: Contains the Terraform configuration for defining AWS resources. Users can add more resources or customize existing ones in this file.
*   `input.tf`: Defines input variables used in the Terraform configuration.
*   `output.tf`: Defines output variables that are displayed after Terraform applies changes.
*   `terraform.tfvars`: Contains variable definitions used in the Terraform configuration. Users can customize variables such as AMI image and instance type in this file.

Contributing
------------

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or submit a pull request.
