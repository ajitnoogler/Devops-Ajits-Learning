BGP Troubleshooting.

#### Problem 1: BGP peer is not getting establish between routers.
Cause :
1) Peer ip address is not reachable .
2) port 179 is blocked by firewall or access-list.
3) BGP configuration is not correct like wrong peer address local-as or remote-as, wrong AS number, wrong authentication/MD5 password or wrong update-source loopback.
4) static route is missing for loopback address end to end.
5) TTL=1 for ebgp neigbor. ebgp-multihop is not configured.
6) MD5 authentication has "space" in password.
7)Duplicate router-id between BGP neighbors.

Debugging command :
debug ip bgp
debug ip tcp transaction
debug ip bgp events

Solution:
a) Ensure BGP local and remote AS configuration is correct.
b) MD5 authentication password is correct on both sides without spaces.
c)Verify update-source loopbak and ebgp-multihop.
d) port 179 is allowed in the path boh end via access-list. Ensure firwall is not blocking.


---

#### Problem 2 : BGP neighbor ship is flapping and getting reset.

Cause:
1. Keep alive mismatch
2. MTU mismatch.
3. Hellos are stuck in OutQ behind update packets.
4. Remote router rebooting continually (typical with a 3-5 minute BGP peering cycle time)
5. Remote router BGP process unstable, restarting
6.Traffic Shaping & Rate Limiting parameters
7.MTU incorrectly set on links, PMTU discovery disabled on router.
8. Output drops on the interface or congestion on the queue.
9. High CPU on the router or CPU spike on router.

Solution :
a) Make sure you  have same keep alive on both routes.
b) Make sure you  have same MTU  and can ping MTU 1500 with df bit set.
c) If MTU mismatch can not be fixed, can use path-mtu discovery to overcome. 

Tip: BGP update packets are packed to the size of the MTU – keepalives and BGP OPEN packets are not packed to the size of the MTU ⇒ Path MTU problem.

---

#### Problem 2: Router is not installing routes in RIB and ignoring.

Cause :
1. Paths that are marked as not synchronized in the show ip bgp longer-prefixes output
2.Paths for which the NEXT_HOP is inaccessible
3.Paths from an external BGP (eBGP) neighbor if the local autonomous system (AS) appears in the AS_PATH
4.If you enabled bgp enforce-first-as and the UPDATE does not contain the AS of the neighbor as the first AS number in the AS_SEQUENCE
5.Paths that are marked as (received-only) in the show ip bgp longer-prefixes output


Solution:
a) Be sure that there is an Interior Gateway Protocol (IGP) route to the NEXT_HOP that is associated with the path.

---

#### Problem 3: Router is not installing routes in BGP Table.
Cause:
1. No router in global routing table for the network command configured in BGP.
2.  No matching route in BGP table for the aggregate-command configured in BGP.
3. Same router-ID in routes coming from Router-reflector in Originator-ID attributes.
4. Same router-IS in routes coming from router-reflector from same cluster-ID. 

---

#### Problem 4: Router is not advertising route to another BGP peer

**Cause:**
1. No matching route in the routing table (RIB).
2. BGP outbound route-policy/filter (e.g., prefix-list, route-map, policy-statement) is discarding the route.

**Solution:**
- Ensure the route exists in the routing table (`show ip route` / `show route`).
- Check if the network is being originated via `network` command, redistribution, or aggregate.
- Verify outbound filter/policy is not suppressing the route (`show ip bgp neighbor X.X.X.X advertised-routes`).
- Use `debug ip bgp` or logging to trace filter actions.
- Clear BGP session or soft reset after fixing the policy:
  ```bash
  clear ip bgp [peer-ip] soft out

  ---

####  Problem: Peering changes

Cause:

    Configuration mismatch (ASN, password, timers, update source).

    Physical link or interface down.

    BGP session reset due to ACLs, CPU load, or MTU issues.

Solution:

    Verify BGP configuration on both ends (remote-as, neighbor, update-source).

    Check logs for BGP session flaps (show log / show ip bgp summary).

    Confirm reachability to peer IP (ping, traceroute).

    Inspect ACLs, firewalls, or TCP port 179 issues.

    Use debug ip bgp or show bgp neighbors to troubleshoot.

---

#### Problem: Route flapping

Cause:

    Instability in underlying interface or recursive next-hop.

    Route changes due to IGP instability or misconfiguration.

    Flap damping incorrectly penalizing stable routes.

Solution:

    Identify flapping routes using show ip bgp flap-statistics.

    Stabilize underlying links/interfaces or IGP convergence.

    Disable or tune route dampening parameters if misapplied:

no bgp dampening

Use hold timers and BFD to avoid premature session flaps.

---

#### Problem: DDoS mitigation

Cause:

    Excessive traffic from spoofed sources or malformed BGP advertisements.

    Prefix hijack or route advertisement to blackhole victim.

Solution:

    Use Remote Triggered Black Hole (RTBH) routing.

    Apply BGP Flowspec if supported to drop flows based on Layer 3/4 rules.

    Rate-limit TCP/UDP connections and ICMP.

    Coordinate with upstream providers to filter or sinkhole malicious traffic.

    Monitor with NetFlow/sFlow and automate detection via BGP communities.

---


BGP Reference Materials.
https://tools.ietf.org/html/rfc1998 
https://transition.fcc.gov/bureaus/pshs/advisory/csric3/CSRIC_III_WG4_Report_March_%202013.pdf
https://www.nanog.org/meetings/nanog51/presentations/Sunday/NANOG51.Talk3.peering-nanog51.pdf 
ftp://ftp.registro.br/pub/gter/gter30/TutorialBGP/7%20-%20Transit.pdf
http://ftp.ines.ro/doc/isp-workshops/Classroom%20Modules%203.0/07-bgp-route-filtering.pdf 
https://www.nanog.org/meetings/nanog40/presentations/BGPcommunities.pdf
https://www.nanog.org/meetings/nanog41/presentations/BGPMultihoming.pdf
http://conference.apnic.net/__data/assets/pdf_file/0011/58745/apricot2013-bgp-multihoming_1361675367.pdf
