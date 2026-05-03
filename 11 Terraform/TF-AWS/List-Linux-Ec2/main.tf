provider "aws" {
  region = "us-west-2"
}

variable "instance_types" {
    description = "List of EC2 instance types to create."
    type        = list(string)
    default     = ["t2.micro", "t2.small"] # You can modify this list to include the desired instance types     
  
}

resource "aws_instance" "windows_ec2" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Windows Server 2019 Base
  instance_type = var.instance_types[0] # Use the first instance type from the list
  key_name      = "my-linux-key-pair" # Replace with your key pair name

  tags = {
    Name = "My-Linux"
  }
}