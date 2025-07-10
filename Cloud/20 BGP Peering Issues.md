
## 🔗 eBGP Peering Issues

1. **Session stuck in Idle/Active**

   * Test: `show ip bgp summary`, ping/telnet peer on TCP 179
   * Fix: Ensure reachability, correct remote-AS/IP, open port 179, set `ebgp-multihop` and `update-source` if using loopbacks

2. **ACL / Firewall blocking**

   * Test: `telnet <peer-IP> 179`
   * Fix: Add `permit tcp host <peer> eq 179 any` in ACLs 

3. **Multihop / loopback peering**

   * Test: Ping from loopback to loopback
   * Fix: `neighbor X ebgp-multihop N` and `neighbor X update-source Loopback0` 

4. **MTU/TCP MSS mismatches**

   * Test: `ping <peer> df-bit size 1500`
   * Fix: `interface X; ip mtu 1500; ip tcp adjust-mss 1460` 

5. **Slow convergence on link failure**

   * Test: Fail link, monitor BGP timer behavior
   * Fix: Use BFD or tune BGP timers (e.g., `timers bgp 5 15`) 

6. **High CPU / large route load**

   * Test: `show processes cpu`, check update bursts
   * Fix: Use aggregates, prefix-lists, damping, `bgp maxas-limit` 
7. **Route leaks or hijacks**

   * Test: Inspect AS\_PATH, origin
   * Fix: Apply AS-path filters, prefix-lists, and deploy RPKI 

---

## 🔄 iBGP Peering Issues

1. **Session not forming**

   * Test: `show ip bgp all summary`, ping neighbor loopback
   * Fix: Configure `neighbor X update-source Loopback0`, ensure loopbacks reachable via IGP 

2. **Missing routes due to next-hop**

   * Test: `show ip bgp <prefix>` and check next-hop with `show ip route <next-hop>`
   * Fix: Use `next-hop-self`, or ensure IGP reachability 

3. **Split-horizon rule (no transit over iBGP)**

   * Understand: Routes from one iBGP peer are not sent to another unless using route reflectors or full mesh 

4. **Missing internal route because sync enabled**

   * Test: Check synchronization (`show ip protocols`)
   * Fix: Disable sync (`no synchronization`) or re-enable IGP&#x20;

5. **Route reflector misconfig**

   * Test: Check reflector-client status, `show ip bgp all summary`
   * Fix: Properly define `route-reflector-client` peers 

6. **Recursive lookup causing peering issues**

   * Test: `show route` for recursive errors
   * Fix: Ensure loopback routes are via IGP, not BGP-redistributed 
7. **Route loops via mutual redistribution**

   * Test: Check ping failures and routing loops
   * Fix: Use tags, communities, or avoid redistributing iBGP into IGP without controls 

8. **Route not forwarded without next-hop changes**

   * Test: `show route`, check if external routes are hidden
   * Fix: Set next-hop-self on RR or clients 

---

# 🧭 Quick Reference Table

| Peer Type | Issue                         | Test Command                          | Remedial Action                             |
| --------- | ----------------------------- | ------------------------------------- | ------------------------------------------- |
| eBGP      | ACL or TCP blocking           | `telnet <peer> 179`                   | Allow TCP/179 in ACLs                       |
| eBGP      | Multihop via loopbacks        | `ping lo <peer>`                      | `ebgp-multihop`, `update-source lo0`        |
| eBGP      | MTU/MSS mismatches            | `ping df-bit 1500`                    | Adjust MTU, `ip tcp adjust-mss`             |
| eBGP      | Slow failover                 | remove link, observe reconvergence    | Tune timers, enable BFD                     |
| iBGP      | Lost session                  | `show ip bgp all summary`, pings      | `neighbor X update-source`, IGP on loopback |
| iBGP      | No route advertised           | `show ip bgp prefix`, `show ip route` | `next-hop-self`, ensure IGP reachability    |
| iBGP      | No transit route              | `show ip bgp all summary`             | Use full mesh or route reflectors           |
| iBGP      | Recursive lookup fail         | `show route`                          | Fix IGP loopback reachability               |
| iBGP      | Unwanted redistribution loops | Monitor traffic loops                 | Use tags, avoid unsupervised redistribution |

