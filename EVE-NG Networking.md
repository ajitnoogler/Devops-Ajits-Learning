#### EVE-NG Networking:

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



