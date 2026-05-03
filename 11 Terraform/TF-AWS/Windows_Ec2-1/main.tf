provider "aws" {
  region = "us-west-2"
}


resource "aws_instance" "my_windows_instance" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Windows Server 2019 Base
  instance_type = "t2.micro"
  key_name      = "my-win-key-pair" # Replace with your key pair name
  vpc_security_group_ids = [aws_security_group.windows_sg.id]

# Root Block Device Configuration
root_block_device {
  volume_size = 8
}

#Tags helps to identify the resource in AWS console and also helps in cost allocation 
# and management.   
  tags = {
    Name = "My-Win"
  }

}

# Create a security group to allow RDP access
resource "aws_security_group" "windows_sg" {
  name        = "windows_sg"
  description = "Allow RDP access"

  ingress {
    from_port   = 3389
    to_port     = 3389
    protocol    = "tcp" # tcp udp all
    cidr_blocks = [var.cidr_block]  # Allow RDP from anywhere (not recommended for production )
        }


    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1" # Allow all outbound traffic
        cidr_blocks = [var.cidr_block]
        }
    }   


# Output the public IP of the instance
output "instance_public_ip" {
  description = "Public IP address of the Windows EC2 instance"  
  value = aws_instance.my_windows_instance.public_ip    # This will output the public IP address of the created Windows EC2 instance after you apply the Terraform configuration.  
    }

# Output the private IP of the instance
output "instance_private_ip" {
  description = "Private IP address of the Windows EC2 instance"  
  value = aws_instance.my_windows_instance.private_ip   # This will output the private IP address of the created Windows EC2 instance after you apply the Terraform configuration. 

}

