# OCI DNS (Like AWS Route-53)

DNS - Domain Name System, For Name resolution (dns-name to IP-add)
DNS works on UDP 53 for queries and TCP 53 for Zone Transfer above 512 Bytes.

DNS uses zones to hold trusted DNS Records that will resides in Oracle Cloud Infra.
You can create Public and Private zone for Public and Private visibility.

OCI DNS also provides Traffic mgmt and Steering Policies:
It help you guide traffic to your endpoint, that includes endpoint health and geographic origin.

# DNS Resolver:
The DNS Resolver in OCI is a built-in DNS service that provides name resolution for VCNs (Virtual Cloud Networks).
The OCI DNS Resolver is:
    - A highly available, regional DNS service
    - Automatically configured for each VCN
    - Used by instances in subnets to resolve domain names
    - Customizable via Resolver Rules, Views, and DNS forwarding


🔧 Key Concepts of OCI DNS Resolver:

| Feature                 | Description                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------- |
| **Default Resolver**    | Every VCN gets a default DNS resolver automatically (resolves `oraclecloud.com`, internal hostnames)  |
| **Custom DNS Resolver** | Lets you create custom forwarding rules, attach private views, and define how DNS queries are handled |
| **Views**               | Logical containers for DNS zones (can be attached to resolvers for internal DNS resolution)           |
| **Rules**               | Define how DNS queries are resolved or forwarded (to on-premises or another cloud)                    |
| **Forwarding**          | Forward DNS queries to on-prem DNS servers or cloud-native DNS resolvers                              |
| **Listening Endpoints** | Private IP addresses (within your VCN subnet) where the resolver listens for DNS queries              |
| **Rulesets**            | Routing logic for domain names (e.g., forward `corp.example.com` to on-prem DNS)                      |
-----------------------------------------------------------------------------------------------------------------------------------

# 🧪 Sample Resolver Rule Setup:

- To forward internal domain to on-prem DNS server:

    - Go to VCN → DNS Resolvers
        - Create or edit a Resolver
        - Add a Rule:
        - Rule Type: Forward
        - Domain: corp.example.com
        - Target IP: 10.10.1.10 (on-prem DNS)

Now any query like server1.corp.example.com is routed to your on-prem DNS.

# ✅ What is a DNS Resolver Endpoint in OCI?
A DNS Resolver Endpoint is a configurable IP listener inside your VCN/subnet that enables instances or on-prem systems to send DNS queries to OCI’s DNS resolver. 
It’s used when you create a custom DNS resolver.

# 📦 Types of DNS Resolver Endpoints:

| Endpoint Type           | Description                                                         | Use Case                               |
| ----------------------- | ------------------------------------------------------------------- | -------------------------------------- |
| **Listening Endpoint**  | A private IP inside a VCN subnet where DNS queries are accepted     | Your instances send queries to this IP |
| **Forwarding Endpoint** | Sends DNS queries to another DNS server (e.g., on-prem or upstream) | OCI forwards DNS to external resolver  |
-------------------------------------------------------------------------------------------------------------------------------------------

# How to access DNS Management in OCI

Hamburger-Icon -> Networking -> DNS Management <Click-it>
 - <Click-On> Zones  , Here, you have Public and Private Zone Tabs. 
* 1st Register your domain with external public DNS Registrar Like Go-Daddy or Big-Rock.
 - <Click-On> Create Zone Button.
    - Method: Manual | Import  (Import means you can import a valid zone file for importing DNS Records.)
    - Zone-Type: Primary(Rw)| Secondary(Ro) Primary - DNS Provider to control zone file modification.
                                            Secondary - Its a Ro copy sync with Upstream Master DNS Server IP.
    - Zone-Name: Demo_Zone
    - Compartment: Demo_Compartment
    - <Click-On> Create

For Adding Record:
    - Name: Demo_web_Server
    - Type: A - IPv4 Address
    - TTL in Sec - 3600
    - RDATA/ANS - 10.1.2.101


# 🔒 Security and Monitoring: vv-IMP to allow DNS ports in Security Group:

Security Lists/NSGs must allow UDP/TCP on port 53 for resolver endpoints
DNS queries can be monitored via VNIC flow logs
Resolver rules are regional — ensure consistency across regions for DR

===================================================================================================

Private Zones - It contains DNS data only accessible from within a VCN, such as Private IP address.

A Record - IPv4 Address, here you give DNS Name
AAAA Record - IPv4 Address
CNAME - Canonical name | Pet or short name or Alias
PTR - Pointer Here you give IP.
SRV - Service Location
TXT - Text
CAA - Certificate Authority Authorization.

🔍 Explanation of Records:

| Record  | Purpose                                                       |
| ------- | ------------------------------------------------------------- |
| `SOA`   | Start of Authority, contains domain's primary DNS server info |
| `NS`    | Lists authoritative DNS servers                               |
| `A`     | Maps domain to IPv4 address                                   |
| `AAAA`  | Maps domain to IPv6 address                                   |
| `CNAME` | Alias of another domain                                       |
| `MX`    | Mail server for the domain                                    |
| `TXT`   | Text info (e.g., SPF, DMARC)                                  |
| `SRV`   | Service location (used in VoIP, SIP, etc.)                    |
| `PTR`   | Reverse lookup for IP address                                 |
---------------------------------------------------------------------------

============================================================================
Sample Zone-File:
============================================================================
$TTL 3600
@       IN      SOA     ns1.example.com. admin.example.com. (
                        2025070801 ; Serial
                        3600       ; Refresh
                        1800       ; Retry
                        604800     ; Expire
                        86400 )    ; Minimum TTL

; Name servers
        IN      NS      ns1.example.com.
        IN      NS      ns2.example.com.

; A Records
@       IN      A       192.0.2.10
www     IN      A       192.0.2.10
mail    IN      A       192.0.2.20

; AAAA Records
www     IN      AAAA    2001:db8::10
mail    IN      AAAA    2001:db8::20

; CNAME Records
ftp     IN      CNAME   www.example.com.

; MX Records
@       IN      MX 10   mail.example.com.

; TXT Records
@       IN      TXT     "v=spf1 a mx ip4:192.0.2.0/24 -all"
_dmarc  IN      TXT     "v=DMARC1; p=none; rua=mailto:dmarc@example.com"
_domainkey IN   TXT     "o=~;"

; SRV Record (e.g., for SIP)
_sip._tcp IN    SRV     10 60 5060 sipserver.example.com.

; PTR Record (for reverse DNS - in reverse zone file)
; 10.2.0.192.in-addr.arpa. IN PTR www.example.com.
=========================================================================================
