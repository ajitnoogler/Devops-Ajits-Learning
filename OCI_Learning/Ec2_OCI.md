
# 🧠 What is an Oracle Compute Instance?
A Compute Instance in OCI is a customizable server you can launch from an image (like Oracle Linux, Ubuntu, Windows, etc.) 
with selected CPU, memory, network, and disk options. It's the foundational building block for: - Hosting applications

- Running microservices

- Deploying databases

- Building container clusters (OKE)

- Setting up DevOps pipelines

- Hosting backend APIs, frontends, etc.

# 🧩 OCI Capacity Types

| **Type**                                     | **Description**                                                                                                                                                  | **When to Use**                                                                                            |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **On‑Demand Capacity**                       |                                                                                                                                                                  | Use for unpredictable workloads, dev/test environments, or when flexibility is key. ([docs.oracle.com][1]) |
| **Preemptible Capacity**                     | - OCI’s “spot” instances at \~50 % discount.<br>- Instances may be reclaimed, with 2 minutes notice.                                                             | Ideal for batch jobs, CI/CD, fault‑tolerant apps, or transient workloads.                                  |
| **Reserved Capacity (Capacity Reservation)** | - Reserve capacity ahead of time.<br>- Ensures availability even during peak demand.<br>- Billed whether used or not, with reductions on idle reserved capacity. | Best for critical or scheduled workloads needing guaranteed slot availability.                             |
| **Dedicated Capacity (Dedicated VM Hosts)**  | - Entire host reserved exclusively for your tenancy.<br>- Suitable for compliance or licensing requirements.                                                     | Use for single‑tenant isolation, regulatory compliance, or special software licensing needs.               |

⚠️ Key Details

    Mixing Types: You can run instances from different capacity types within a compartment or node pool, 
    but reservations and host assignments are specific to regions and availability domains

    Billing Differences:

        On-Demand: Per-second billing only while instance is running.

        Preemptible: ~50 % cheaper than On-Demand, but can be terminated anytime.

        Reserved: Billed when allocated (used or not), but unused portion is charged at a reduced rate (~85 %).
        
        investopedia.com+2marketwatch.com+2en.wikipedia.org+2
        
        docs.oracle.com+6docs.oracle.com+6linkedin.com+6

        Dedicated: Charged at host level; all VMs on that host belong solely to you.

✅ Choosing the Right Capacity Type

    If you need flexible, ad-hoc capacity: On‑Demand

    If you have batch jobs or interruptible workloads: Preemptible

    If you require guaranteed capacity when demand is high: Reserved

    If you need isolation for compliance or licensing: Dedicated VM Hosts

# Creating OCI Instance

 Click on Hamburger Icon -> Compute -> Instances
   - Create Instance
       - Name: Demo_Instance
       - Compartment: Demo_Comparment
       - Placement: AD 1 | AD 2 | AD 3 |    Availibility Domain, Like AWS Availability Zones
           - Capacity Types: On Demand | Capacity Reservation | Dedicated Host | Shared Host | Compute Cluster | preemption capacity for dev test can be delete anytime (You can also enable Cluster / Partition Placement Group)
           - - Fault Domain: Fault Domain 1, 2, 3
       - Security: Sheilded Instance | Confidential Computing (Only for AMD based Instances)
       - Image and Shapes:
           - Image: Oracle Linux
           - Shapes: VM.Standard.E5.Flex  (Flex means CPU and Memory can be increased or descresed later)
       - VCN: Demo_VCN_1
       - Subnet: Demo_VCN_1_Private_Subnet
       - Primary vNIc Information:
           - Private IPv4 Assignment: Automatic | Manual Assignment - 10.0.0.180
           - Public IPv4 Assignement: Automatically assign Public IP
      - Add SSH Keys: Generate Key-Pair  | Upload public key file | Paste Public Key  | No SSH Keys
      - Boot Volume: Custom Boot Volume Size | Use-In Transit Encryption | Encrypt Volument with Key
              - Attach Boot Volume
      -  Create Instance...
    
     # Developer Tools

     - Click on Cloud Shell
          - Here our instance has only private IP "How do i access my instance via cloud shell using private ip ???"
          - Ans: Switch Network: From "Public" to "Private network defination list" from the Drop Down
                - Create private network defination:
                    - Name: Demo_Net_for_Cloud_Shell
                    - VCN in Demo_Compartment: Demo_VCN_1
                    - Subnet: Demo_VCN_1_Private_Subnet
                    - NSG: (Optional)
                    - Enable Use as active Network

#  Now Connect to Cloud Shell
  - Upload your Demo_Instnace Key-pair using upload option in left corner of cloud shell (key.pem file)
  - Change permission of key.pem file "chmod 400 key.pem"
  - From cloud shell "ssh -i key.pem opc@10.0.0.180"
  - This should land you in your instance cli via ssh.


            
       
     
          
             
