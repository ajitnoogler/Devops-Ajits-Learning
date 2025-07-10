# 🐙 Problem: OSPF Full Neighborship is Not Coming Up Between Routers

## 🔍 Cause:

1. Hello and Dead timer or Area ID, Authentication password/type/key or Area type are mismatches between router.
2. Trying to build OSPF neighborship on the secondary address.
3. *(Intentionally skipped, no item 3 in original list)*
4. OSPF is not enabled on correct interface or network command is wrong.
5. Network type is NBMA and no neighbour map configured with a broadcast option.
6. High CPU or OSPF packet is dropped by interface due to queuing or high rate or hardware issue from the interface to CPU path.
7. Mismatch Subnet mask is configured.
8. `passive-interface <interface>` is configured under `router ospf` for the interface.
9. Mismatch Network type is configured.
10. Router is configured with `ip ospf priority 0` on the router.
11. Neighborship is getting built over a virtual link on stub area.

---

## 🧯 OSPF Stuck States

### 🔄 OSPF Stuck in INIT (One-Way Hello)

- Multicast is broken or Layer 2 problems.
- Access-list is blocking OSPF multicast address.
- OSPF hello packet getting NAT translated.
- Layer 2 is broken.

### 🔄 OSPF Stuck in 2-WAY

- Normal on Ethernet broadcast.
- Layer 2 is broken.
- All routers are configured with priority 0 so there will not be any election.

### 🔄 OSPF Stuck in EXSTART / EXCHANGE

- MTU mismatch between neighbor.
- Duplicate router-ID between routers.
- Packet loss can also cause it to get stuck.
- Access-list is blocking unicast communication between routers.

### 🔄 OSPF Stuck in LOADING

- Neighbor is sending bad packet or corrupt packet due to memory.
- LS Request packet is not accepted by a neighbor and is being ignored.

---

## 🛠️ Debug Command

```bash
debug ip ospf adj

---
#### ✅ Solution

- **a)** Make sure Hello-Dead timers, Area ID, Area Type, and Authentication type/password are correct and same.
- **b)** Make sure MTU is same on both routers.
- **c)** Make sure neighbor command is configured on remote router with broadcast.
- **d)** Make sure OSPF neighborship is built on primary address.
- **e)** Access-list / control plane is not dropping the packet and is allowing OSPF multicast and interface IP address communication.
- **f)** Subnet mask should be same on both routers.
- **g)** Make sure no corrupted OSPF packet is received.
- **h)** Make sure `passive-interface` is not configured under `router ospf`.
- **i)** Make sure Virtual-Link is not configured over stub area.
