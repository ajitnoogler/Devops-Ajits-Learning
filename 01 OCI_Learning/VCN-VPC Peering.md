# VCN Peering - Accessing Other VCN's via VCN Peering.

- VCN Pering allows a network connectivity betwen two VCN/VPC
- Enables you to use IPv4 and IPv6 Addresses.
- VCN peering can be done between two VPN in different account
- The VCN can be in different Region.
- Each VCN can have upto 10 local Peering gateway's attached to only one DRGw. 
- A Single DRGw supports upto 300 VCN/VPC Attachment.

# VCN Peering Types:
- Local VCN Peering - Within Region using Local Peering Gateway (LPG's)
- Remote VCN Peering- Across Region using Remote Peering Connections (RPC's)

- Local VCN Peering Through Upgraded DRGw (Dynamic Routing Gw)
- Remote VCN Peering Through Upgraded DRGw (Dynamic Routing Gw)


# Lets Peer two VCN within Region: 
Demo_VCN - 192.168.0.0/16
Demo_VCN_2 - 10.0.0.0/16

Hamburger-Icon -> Networking -> Virtual Cloud Networks (VCN) -> Demo_VCN <Click-it>
    - <Click-on> Under Resource, Local Peering Gateway
        - <Click-on> Create Local Peering Gateway
            - Name: LPG_For_Demo_VCN
            - Compartment: Demo_Compartment
            - <Click-on> Create Local Peering Gateway.

Hamburger-Icon -> Networking -> Virtual Cloud Networks (VCN) -> Demo_VCN_2<Click-it>
    - <Click-on> Under Resource, Local Peering Gateway
        - <Click-on> Create Local Peering Gateway
            - Name: LPG_For_Demo_VCN_2
            - Compartment: Demo_Compartment
            - <Click-on> Create Local Peering Gateway.

    -- Lets Establish Peering connections 
        - <Click-on> 3 DOT next to "LPG_For_Demo_VCN_2" and <Click> Establish Peering connection from Drop-Down.
            - Establish Peering Connection
                - Specify the Local Peering Gateway: Browse Below or Enter Local Peering Gateway "OC-ID".
                    - VCN Compartment: Demo_Compartment
                    - Virtual Cloud Network: Demo_VCN
                    - Local Peering Gateway Compartment: Demo_Compartment
                    - Unpeered Peer Gateway: LPG_For_Demo_VCN
                    - <Click-on> Establish Peering Connection.

    -> Lets add Routes for Demo_VCN_2 in Route Table using Route Rules:
    Hamburger-Icon -> Networking -> Virtual Cloud Networks (VCN) -> Demo_VCN<Click-it>
        - <Click-on> MyDemo_VCN_Route_Table
            - Add Route Rules: For VCN Peering
                - Target Type: Local Peering Gateway
                - Dest CIDR Block: 10.0.0.0/16
                - Target Local Peering Gw: LPG_For_Demo_VCN
                - Desc: Traffic from Demo_VCN to Demo_VCN_2
                    
    -> Lets add Routes for Demo_VCN_2 in Route Table using Route Rules:
    Hamburger-Icon -> Networking -> Virtual Cloud Networks (VCN) -> Demo_VCN_2<Click-it>
        - <Click-on> MyDemo_VCN_2_Route_Table
            - Add Route Rules: For VCN Peering
                - Target Type: Local Peering Gateway
                - Dest CIDR Block: 192.168.0.0/16
                - Target Local Peering Gw: LPG_For_Demo_VCN_2
                - Desc: Traffic from Demo_VCN_2 to Demo_VCN.
================================================================================================================

# Lets Peer two VCN in Different Region: Remote Peering


Demo_VCN - 192.168.0.0/16 - Australia Southeast Melbourn 
Demo_VCN_2 - 10.0.0.0/16 US-Phoenix-1
Create DRGw for Both Region.

**Create Remote Peering Connection:**

-> Switch-To: US_East_Pheonix Region

Hamburger-Icon -> Networking -> Customer Connectivity -> Dynamic Routing Gateway <Click-it>
    - <Click-on> Dynamic Routing Gateway: demo-drg-US
        - <From Resources> Select Remote Peering Connection Attachments.
            - Create Remote Peering Connection
                - Name: RPC_For_Pheonix
                - VCN Compartment: Demo_Compartment

-> Switch-To: Australia Southeast Melbourn Region (Mel)

Hamburger-Icon -> Networking -> Customer Connectivity -> Dynamic Routing Gateway <Click-it>
    - <Click-on> Dynamic Routing Gateway: demo-drg-Mel
        - <From Resources> Select Remote Peering Connection Attachments.
            - Create Remote Peering Connection
                - Name: RPC_For_Mel
                - VCN Compartment: Demo_Compartment

-> Lets Establish the Remote Peering Connection
-> Switch-To: Australia Southeast Melbourn Region (Mel)

    - <Click-on> Remote Peering Attachment
        - <Click on> DRG_Attachment_for_RPC:RPC_For_Mel
            - <Click on> Establish Connection Button
                - Region: US-Phoenix-1
                - Remote Peering connection OCID: <OCID of RPC_For_Pheonix>
