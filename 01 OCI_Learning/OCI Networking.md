# OCI Networking 

# VCN (Virtual cloud network) Like VPC in AWS.

**Create VCN:**
Hamburger-Icon -> Networking -> Virtual Cloud Networks (VCN)
    Click Create VCN:
        - Name        - Demo_VCN
        - Compartment - Demo_Compartment
        - CIDR        - 192.168.0.0/16
        - USE DNS hostnames in this VCN <Enable it>
        - DNS Label - Demo_VCN i.e Demo_VCN.oraclevcn.com
        - Create VNC <Click it>

**Create Subnet**

# Create Public Subnet

Hamburger-Icon -> Networking -> Virtual Cloud Networks (VCN) -> Demo_VCN <Click-it>
    Click Subnet and Create Subnet
        - Name - My_demo_Private_Subnet
        - Compartment - Demo_Compartment
        - Subnet Type - Regional (Recommended)
        - IPv4 CIDR Block - 192.168.1.0/24
        - Route Table - Default Route Table
        - Subnet Access - Private Subnet  // (Here Public or Private Subnet)
        - DNS Resolution - Enable "Use DNS hostname in this subnet"
        - DHCP Options - 
        - Security Lists - Default Security List for VCN (Its like Security Group)
        - Resource Logging - Enable for Resource Tracking, Tshoot & Data Insight.
        >> Create Subnet <Click-it>

# Create Public Subnet

Hamburger-Icon -> Networking -> Virtual Cloud Networks (VCN) -> Demo_VCN <Click-it>
    Click Subnet and Create Subnet
        - Name - My_demo_Private_Subnet
        - Compartment - Demo_Compartment
        - Subnet Type - Regional (Recommended)
        - IPv4 CIDR Block - 192.168.1.0/24
        - Route Table - Default Route Table
        - Subnet Access - Public Subnet
        - DNS Resolution - Enable "Use DNS hostname in this subnet"
        - DHCP Options - 
        - Security Lists - Default Security List for VCN (Its like Security Group)
        - Resource Logging - Enable for Resource Tracking, Tshoot & Data Insight.
        >> Create Subnet <Click-it>


