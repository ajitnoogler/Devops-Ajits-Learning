provider "aws" {
  region = "us-west-2"
}


variable "instances" {
  type = map(string)
  default = {
    "instanceA" = "t2.micro"
    "instanceB" = "t2.small"
  }

}


resource "aws_instance" "my_linux_instance" {
  for_each               = var.instances
  ami                    = "ami-0c55b159cbfafe1f0" # Amazon Linux 2 AMI
  instance_type          = each.value
  key_name               = "my-linux-key-pair" # Replace with your key pair name
  vpc_security_group_ids = [aws_security_group.linux_sg.id]

  root_block_device {
    volume_size = 8
  }

  tags = {
    Name = each.key # This will set the Name tag to the key of the instance in the map (e.g., instanceA, instanceB)
  }

}

# Create a security group to allow SSH access
resource "aws_security_group" "linux_sg" {
  name        = "linux_sg"
  description = "Allow SSH access"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"            # tcp udp all
    cidr_blocks = [var.cidr_block] # Allow SSH from anywhere (not recommended for production)
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # Allow all outbound traffic
    cidr_blocks = [var.cidr_block]
  }
}

# Output the public IP of the instance
output "instances_public_ip" {
  description = "Public IP addresses of the Linux EC2 instances"
  value       = { for k, v in aws_instance.my_linux_instance : k => v.public_ip } # This will output a map of instance names to their public IP addresses after you apply the Terraform configuration. 
}

# Output the private IP of the instance
output "instances_private_ip" {
  description = "Private IP addresses of the Linux EC2 instances"
  value       = { for k, v in aws_instance.my_linux_instance : k => v.private_ip } # This will output a map of instance names to their private IP addresses after you apply the Terraform configuration. 
} 