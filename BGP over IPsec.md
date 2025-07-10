### Problem: BGP Neighbor Not Coming Up Over IPSec Site-to-Site VPN

**Cause:**
1. IPSec tunnel is down or unstable.
2. BGP packets (TCP port 179) are not allowed through VPN/firewall.
3. Incorrect BGP configuration (e.g., remote-as, source IP).
4. MTU mismatch or fragmentation issues due to encryption overhead.
5. Routing or NAT issues for the BGP peer IPs.
6. Dead Peer Detection (DPD) or keepalive mismatch in IPSec.
7. Overlapping subnets or incorrect crypto ACLs (for policy-based VPNs).

**Solution:**
- ✅ **Verify IPSec tunnel status:**
  - Check `show crypto ikev2 sa`, `show crypto ipsec sa`, or equivalent.
  - Confirm tunnel is UP and encrypt/decrypt counters are increasing.

- ✅ **Ensure BGP packets are allowed:**
  - Allow **TCP port 179** bi-directionally in VPN/firewall rules.
  - For policy-based VPN, ensure crypto ACL includes BGP source IPs.

- ✅ **Check BGP configuration:**
  - Use loopback as source? Then configure `update-source loopback` on both ends.
  - Ensure correct `remote-as` and neighbor IP.
  - Command:
    ```bash
    show ip bgp summary
    show ip tcp brief | include 179
    ```

- ✅ **MTU/fragmentation fix:**
  - Lower BGP TCP MSS (e.g., 1350) to avoid fragmentation:
    ```bash
    neighbor X.X.X.X transport connection-mode active
    ip tcp adjust-mss 1350
    ```

- ✅ **Check NAT traversal (if used):**
  - Use `NAT-T` (UDP 4500) and avoid NATing peer BGP IPs.

- ✅ **Enable Keepalive and Hold Timers:**
  - Ensure timers are consistent on both sides.
  - Tune them if VPN flaps frequently:
    ```bash
    neighbor X.X.X.X timers 10 30
    ```

- ✅ **Debug and logs:**
  - On Cisco/Juniper:
    ```bash
    debug ip bgp
    debug ip tcp transactions
    show logging
    ```

- ✅ **General tip:**
  - Use static routes (or IGP) to ensure BGP source IPs are reachable over the IPSec tunnel.

---

**Optional Enhancements:**
- Use BFD for fast failure detection if supported.
- Monitor via SNMP or syslog for tunnel/BGP flaps.
- In dual-site VPNs, consider GRE-over-IPSec to simplify routing and neighbor establishment.

---
