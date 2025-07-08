# OCI Gateways:
1. Internet Gw
2. NAT Gw
3. Service Gw

=====================================================================================

# 1. Internet Gateway (igw)
Provide access to the internet from VCN.
Its a igw construct attached to VPC / VCN.
Its for Egress Traffic.
Admin need to update the route table 0.0.0.0/0 via igw.

Hamburger-Icon -> Networking -> Virtual Cloud Networks (VCN) -> Demo_VCN <Click-it>
    - <Click on> Demo_VCN
    - <Click on> Internet Gateways
        - Create Internet Gateways:
            - Name: demo_igw
            - compartment Demo_Compartment
            - <Click> Create Intenet Gateway
        - Update Route Table:
            - Create or use "Default Route Table for Demo VCN"
                - <Click> Default Route Table for Demo VCN
                - Create Route Rules: Target Type == For Internet Gateway
                    - Destination CIDR Block: 0.0.0.0/0
                    - Target Internet Gateway : demo_igw 
                    - Desc - For Internet Traffic
                    <Click> Add Route Rules

=====================================================================================
 
 # 2 NAT Gateway: 
A NAT Gateway is used to provide internet access to resources without public IP address, access to the Internet without exposing these resources to the incoming internet connections.

- NAT gateway is added to give instances in private subnet access to the internet.
- With the NAT gateway, these instances can initiate connections to the internet and receive responses, but they are not able to receive any incoming connections initiated from the internet.
- NAT gateways are highly available and support TCP, UDP, and ICMP ping traffic.

Hamburger-Icon -> Networking -> Virtual Cloud Networks (VCN) -> Demo_VCN <Click-it>
    - <Click-on> Demo_VCN
    - Then <Click-on> Nat Gateways
        - Create NAT Gateway
            - Name: Demo_NAT_Gw
            - Compartment: Demo_Compartment
            - Ephemeral or Reserved Public IP address.
            <Click on> Create Nat Gateway.
    - Update Route Table: 0.0.0.0/0 to Nat-Gw
            - Create or use "Default Route Table for Demo_VCN"
                - <Click> Default Route Table for Demo_VCN
                - Create Route Rules: Target Type == For Internet Gateway
                    - Destination CIDR Block: 0.0.0.0/0
                    - Target Internet Gateway : Demo_Nat_Gw 
                    - Desc - For Internet Traffic Egress-Only
                    <Click> Add Route Rules
# IMP:
* Ephemeral Public IP: The Public IP address Lifetime is bound to lifetime NAT Gw.
* Reserved Public IP: You control the public IP lifetime. You can associate and deassociate to another resources in the "**Same Region**"

=====================================================================================

# Service Gateway
It allows VCN to privately access OCI Services with exposing any data to the internet.

**To Create Service Gw:**

Hamburger-Icon -> Networking -> Virtual Cloud Networks (VCN) -> Demo_VCN <Click-it>
    - <Click-on> Demo_VCN
    - Then <Click-on> Service Gateways
        - Create Service Gateway
            - Name: Demo_Service_Gw
            - Compartment: Demo_Compartment
            - Services: All PHX Services in Oracle Service Network.
            - <Click-on> Create Service Gateway.
            - Associate Route Table in Demo_Service_Gw pointing to Default Route Table for Demo VCN.

Here, Services two options: (PHX-phoenix Network)
    All PHX Services in Oracle Services Network. 
    OCI PHX Object Storage.

=======================================================================================================

# Dynamic Routing Gateway (DRGw)
Allows you to connects multiple VCN/VPC
You can connect Fast Connect | IPSEC Site to Site VPN with ON-Premise.
OCI DRG-gw Provide Static and Dynamic Routing capability including BGP.

**To Create DRGw:**

Hamburger-Icon -> Networking -> Customer Connectivity -> Dynamic Routing Gateway <Click-it>
    - <Click-on> Create Dynamic Routing Gateway
                - Name: Demo_Service_DRGw
                - Compartment: Demo_Compartment
                - Services: All PHX Services in Oracle Service Network.
                - <Click-on> Create Dynamic Routing Gateway.
                - Attach DRGw to VCN - Demo_VCN <Click> Create virtual Cloud network attachment.
                    - Attachment Name:
                    - Virtual Cloud network: Demo_VCN
                    - DRG Route Table: Choose Route Table - Auto Generated.
                    - VCN Route Table: None or Existing.
                    - VCN Route Type Subnet CIDR or VCN / VPC CIDR (i.e 192.168.1.0/24 or 192.168.0.0/16)
                    - <Click-on> Create VCN Attachment.



# Attachement Types:

FastConnect - Virtual Circuit Attachement
IPsec- IPsec Tunnel Attachments
Remote Peering Connection Attachment - VCN or VPC Peering
Loop Back Attachments -
Cross Tenency Attachments - 

DRG Route Tables
Import Route Redistriution.
Export Route Redistribution.

# Route Table:
Local - Subnet is locally attached to VCN hence Target is Local
----------------------------------------------
Destination           Target
----------------------------------------------
0.0.0.0/0             igw-0349833948bh493
192.168.1.0/24        local <--- VCN Subnet
192.168.0.0/16        local <--- VCN CIDR
-----------------------------------------------

# Create Route Tables:

Hamburger-Icon -> Networking -> Virtual Cloud Networks (VCN) -> Demo_VCN <Click-it>
    -> Create Route Table:
        - Name: MyDemo_Route_Table
        - Compartment: Demo_Compartment
        - <Click-On> Create.
    -> Lets add Few Routes in Route Table using Route Rules:
        - <Click-on> MyDemo_Route_Table
            - Add Route Rules: For Nat Gw
                - Target Type: Nat Gw
                - Dest CIDR Block: 0.0.0.0/0
                - Target Nat Gw: Demo_Nat_Gw
                - Desc: Traffic for Private Subnet to Internet.
                - <Click-on> Add Route Rules.
            
            - Add Route Rules: For Internet Gw
                - Target Type: Internet Gw
                - Dest CIDR Block: Public CIDR Block.
                - Target Nat Gw: Demo_Internet_Gw
                - Desc: Traffic for Public Subnet to Internet and Vice Versa !!!
                - <Click-on> Add Route Rules.
        -> Lets Associate Route Table with VCN/VPC:
            - <Go-To> Hamburger-Icon -> Networking -> Virtual Cloud Networks (VCN) -> Demo_VCN <Click-it>
            - <>Click-on> Private Subnet <Edit>
                - Route Table in Demo_Compartment: Select My_Demo_Route_Table.
                - <Click-on> Save.
                

# Imp: Source/Dest Check:
For Route Rule that Target a Private IP, You must first enable "Skip Src/Dest Check" on vNic that the Private IP is Assigned.

