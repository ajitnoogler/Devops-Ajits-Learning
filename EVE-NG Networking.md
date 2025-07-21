#### EVE-NG Networking:

#### VMware Network Types:

<img width="1772" height="855" alt="image" src="https://github.com/user-attachments/assets/59b1eca6-6963-42fc-9e2d-5af6511419b5" />


``` bash

Bridged Networking:
In this mode, your VM acts as an independent device on your physical network, directly connecting to your host's network adapter and obtaining an IP address from your network's DHCP server. 
This allows your VM to be fully accessible to other devices on the same network and vice-versa. The default virtual network adapter for this is VMnet0. 

NAT (Network Address Translation) Networking:
This mode allows your VMs to share the IP address of your host machine to access the external network. VMs in a NAT network are typically not directly accessible from the external network without port forwarding, 
and they get their IP addresses from a private DHCP server managed by Workstation. The default virtual network adapter for this is VMnet8. 

Host-Only Networking:
This creates a private network solely between your host machine and its virtual machines. VMs in a host-only network can communicate with each other and with the host, 
but they cannot reach the external network. The default virtual network adapter for this is VMnet1. 

Custom Networks:
VMware Workstation allows you to create custom virtual networks where you can define specific IP addressing schemes and configurations, offering more flexibility than the default options. 

LAN Segments:
This feature allows you to create completely private, isolated networks for your VMs, without any connection to the host or the external network. 
This is useful for scenarios where you need to simulate network environments without external dependencies or for isolating potentially problematic VMs. 

```

#### Eve-NG Network Types:

<img width="967" height="636" alt="image" src="https://github.com/user-attachments/assets/50bf3911-e1db-4406-bd5b-45bb95e81fa7" />


### Bridge
<img width="807" height="166" alt="image" src="https://github.com/user-attachments/assets/77a92ce3-01dd-4793-ac56-4abdf0d652fa" />

#### Mgmt and NAT
<img width="902" height="517" alt="image" src="https://github.com/user-attachments/assets/7169e99c-f861-48a8-a8f7-ea8fb4702f37" />


``` bash
#### Bridge Network: 
The EVE Bridge interface acts like an unmanaged Switch. It supports passing along tagged dot1q 
packets. We have to connect many nodes in a flat (dot1q) network. Right-clicking on the 
topology area and selecting “Add Network” or in the sidebar click “Add an Object” and
then select “Network.”. Name/prefix can be changed in order to rename your Bridge network. 
Make sure your network type is set to bridge.

#### Management Cloud0 Interface: 
EVE management interface is also known as the Cloud0 network for labs. The Cloud0 interface 
is bridged with your EVEs first NIC. “Cloud” is used as an alias to Pnet. Cloud0 is commonly used 
inside EVE labs to get management access to nodes running inside EVE from a host machine 
external to EVE.

#### Other Cloud Interfaces: 
Other cloud interfaces can be used to extend a lab connection inside of EVE or bridged with
other EVE interfaces to connect external networks or devices.

```

```bash
+---------------------------------------------------+
|               Your Windows Laptop                 |
|           (VMware Workstation Host)               |
+----------------------------+----------------------+
                             |
                             |
            +----------------+----------------+
            |             EVE-NG VM           |
            |          (Ubuntu Linux)         |
            |  eth0: Bridged to Host Network  |
            |  IP: 192.168.1.100              |
            +--------+----------+-------------+
                     |          |           
              +------+--+   +---+---+     +--------+
              | Cloud0 |   |  NAT  |     |  NET1  |
              |Bridge  |   | Host  |     |Internal|
              +---+----+   +---+---+     +---+----+
                  |   |           |
                  |   |_____      |
        +---------+---+    |      |           
        | Mgmt VM (Win) |  |      |           
        | eth0 → Cloud0 |  |      |___________      
        +---------------+  |                 |
                           |                 | g0/1
                           |          +------+-------+
                           |          | Cisco Router |
                           |          | Gi0/1 → NAT  |
                           |          | Gi0/0 → NET2 |
                           |          +------+-------+
                           |                | p2
                           |          +-----+------+
                           |          |  FortiGate  |
                           |          | port2 → NET2|
                           |    mgmt  | port1 → NET1|
                           ---+------→| mgmt → Cloud0
                                       +-----+------+
                                             | p1
                                       +-----+------+
                                       |  Ubuntu VM  |
                                       | eth0 → NET1 |
                                       +-------------+

```

* Fortigate mgmt connecting to bridge so your laptop can access fortigate GUI
* Cisco Router G0/1 get ip from eve-ng nat subnet.



