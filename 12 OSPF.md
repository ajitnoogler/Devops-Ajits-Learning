Problem :OSPF full neighborship is not coming up between routers
Cause :
1. Hello and Dead timer or Area ID, Authentication password/type/key or Area type are  mismatches between router.
2. Trying to build OSPF neighborship on the secondary address.
4.  OSPF is not enabled on correct interface or network command is wrong.
5. Network type is NBMA and no neighbour map configured with a broadcast option.
6. High CPU  or OSPF packet is dropped by interface due to queuing or high rate or hardware issue from the interface to CPU path.
7. Mismatch Subnet mask is configured.
8. "passive interface <> " is configured under "router ospf"for the interface.
9.  Mismatch Network type is configured.
10. Router is configured with  ip ospf priority 0 on the router.
11. Neighborship is getting built over a virtual link on stub area.

OSPF stuck in INIT (one way hello) 
 Multicast is broken or layers 2 problems.
Access-list is blocking OSPF multicast address.
OSPF hello packet getting NAT translated.
 Layer 2 is broken.
   
OSPF stuck in 2-WAY
 Normal on ethernet broadcast.
 Layer 2 is broken.
All routers are configured with priority 0 so there will not be any election.

OSPF stuck in EXSTART/EXCHANGE
 MTU mismatch between neighbor
 Duplicate router-ID between routers.
 Packet loss can also cause to stuck.
 Access-list is blocking unicast communication between router.

OSPF stuck in LOADING
 Neighbor is sending bad packet or corrupt packet due to memory.
 LS request packet is not accepting by a neighbor and ignoring.

Debug command :
debug ip ospf adj

Solution:
a) Make sure hello-dead/ area id, area type,authentication type/password are correct and same.
b) Make sure MTU is same on both router.
c) Make sure neigbor command is configured on remote router with broadcast.
d) Make sure OSPF neigborship build on primary address.
e) Access-list /control plane is not dropping the packet and allowing OSPF multicast and interface ip address communication.
f) Subnet mask should be same on the router.
g) Make sure no corrupted OSPF packet received.
h) Make sure passive interface is not configured under "router ospf".
i) Make sure Virtual -link is not configured over stub area.
