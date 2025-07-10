
# Common BGP issues and their recommended solutions

| **Issue**                                   | **Symptoms / Cause**                                                           | **Solution**                                                                                                 | **Source(s)**                                                                                 |
| ------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| Session establishment failure               | TCP handshake failures, idle/active states, wrong AS/IP, ACL/firewall blocking | Verify AS numbers, peer IPs, port 179 open, multihop TTL, MD5 auth; check TCP connectivity (ping/nc/netstat) | Cisco ([cisco.com][1], [cisco.com][2], [extreme-networks.my.site.com][3]); Arista/Catchpoint  |
| MTU mismatch / TCP MSS issues               | Large packets dropped, BGP session stuck or reset                              | Adjust MTU or TCP MSS settings to match path requirements                                                    | Catchpoint                                                                                    |
| Wrong Next-hop / missing routes             | Routes not installed due to unreachable next-hop                               | Ensure IGP or static route to BGP next-hop exists; use route‑maps/import‑route commands                      | H3C                                                                                           |
| RIB insertion failure / RIB-failure         | Routes not accepted into RIB, `%BGP…ROUTEINSERTERROR`                          | Check memory, timers, interface status, route limits; adjust filters                                         | Cisco FAQ  `%BGP-…ROUTEINSERTERROR`                                                          |
| Adjacency flaps / session bouncing          | Frequent neighbor up/down, CPU/memory issues, interface flaps                  | Stabilize interface, clear flap sources, use dampening, ensure neighbor/router stability                     | Cisco                                                                                         |
| Route flapping / instability                | Constant announcement/withdrawal causing convergence delays                    | Enable BGP flap damping, optimize timers, inspect IGP/BGP policies & hardware                                | Wikipedia + Cisco best practices                                                              |
| BGP slow peer / performance lag             | High CPU, slow convergence, delayed updates                                    | Monitor peer, adjust timers/policy, reload configs, inspect memory & processor load                          | Cisco                                                                                         |
| AFI/SAFI mismatches                         | Neighbor fails for IPv4 vs IPv6 session                                        | Match AFI/SAFI config on both sides, advertise correct capabilities                                          | Cisco                                                                                         |
| Misc. errors (e.g. hold‐time expired)       | Session drops with `%BGP‑3‑NOTIFICATION` messages                              | Align timers, debug logs, adjust hold/keepalive parameters                                                   | Cisco FAQ / tech notes                                                                        |
| Route propagation / policy misconfiguration | Routes received but not forwarded                                              | Review prefix-lists, route-maps, filters, ORF settings; soft resets; check neighbor output                   | Catchpoint & NetSecCloud                                                                      |
| BGP hijacking / route leaks                 | Unwanted prefix announcements (altered traffic paths), leaks to other ASes     | Deploy RPKI/ROA, prefix filters, peerlock; realtime monitoring tools like ARTEMIS                            | Wikipedia, academia & research                                                                |



# Diagnostics and Remediation:

| **Issue**                                                                        | **Test / Diagnose Command**                                       | **Fix / Remedial Command**                                                   |                     |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------- |
| **Session not forming**                                                          | `show ip bgp summary`; `show tcp brief`                           | \`\`\`router bgp <ASN>                                                       |                     |
| neighbor X.X.X.X remote-as <ASN>                                                 |                                                                   |                                                                              |                     |
| neighbor X.X.X.X update-source <intf>                                            |                                                                   |                                                                              |                     |
| neighbor X.X.X.X timers 30 90\`\`\`                                              |                                                                   |                                                                              |                     |
| **MTU / TCP MSS mismatch**                                                       | \`show interface                                                  | include MTU`; `ping <peer> df-bit size 1500\`                                | \`\`\`interface <X> |
| ip mtu 1500                                                                      |                                                                   |                                                                              |                     |
| ip tcp adjust-mss 1460\`\`\`                                                     |                                                                   |                                                                              |                     |
| **Next-hop unreachable**                                                         | `show ip bgp <prefix>`; `show ip route <next-hop>`                | \`\`\`router bgp <ASN>                                                       |                     |
| neighbor X.X.X.X next-hop-self                                                   |                                                                   |                                                                              |                     |
| router ospf 1                                                                    |                                                                   |                                                                              |                     |
| network <next-hop-subnet> area 0\`\`\`                                           |                                                                   |                                                                              |                     |
| **Route flap instability**                                                       | `show ip bgp dampening flap-statistics`; `debug ip bgp dampening` | **Global dampening**: \`\`\`router bgp <ASN>                                 |                     |
| bgp dampening\`\`\`                                                              |                                                                   |                                                                              |                     |
| **Per-route**: use prefix-list + route-map + `bgp dampening route-map DAMPENING` |                                                                   |                                                                              |                     |
| **Hold/keepalive timer expired**                                                 | `show ip bgp neighbors X.X.X.X`                                   | \`\`\`router bgp <ASN>                                                       |                     |
| neighbor X.X.X.X timers 60 180\`\`\` or adjust both values as needed             |                                                                   |                                                                              |                     |
| **Session flapping (adjacency)**                                                 | `show ip bgp neighbors`; `show logging`                           | Use `clear ip bgp X.X.X.X`, increase hold/timers, verify interface stability |                     |
| **Policy/filter misconfiguration**                                               | `show ip bgp neighbors X.X.X.X received-routes`; `show route-map` | Update route-map/prefix-list, then run `clear ip bgp X.X.X.X soft in`        |                     |
| **AFI/SAFI mismatch (e.g. IPv6)**                                                | `show bgp ipv6 summary`; `show ip bgp neighbors`                  | \`\`\`router bgp <ASN>                                                       |                     |
| address-family ipv6                                                              |                                                                   |                                                                              |                     |
| neighbor X.X.X.X activate\`\`\`                                                  |                                                                   |                                                                              |                     |
| **BGP RIB insertion failure**                                                    | `%BGP…ROUTEINSERTERROR`, `show ip bgp rib-failure`                | Check resources, clear or limit memory flags, remove unnecessary filters     |                     |



# 🛠️ More BGP Issues, Diagnostics, and Fixes

| **Issue**                          | **Test / Diagnose Commands**                                    | **Fix / Remedial Commands**                                                                                                                                      |
| ---------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TCP issues (ACL/Port blocked)**  | `telnet <peer> 179`; `show access-lists`; `show firewall`       | Open port 179 in ACL/firewall or add `permit tcp host X.X.X.X eq 179 any`                                                                                        |
| **EBGP multihop/loopback peering** | `show ip bgp neigh <peer>`, `ping <peer> source <self-loop>`    | In BGP config: `neighbor X.X.X.X ebgp-multihop <n>`, `neighbor X.X.X.X update-source Loopback0` ([networklessons.com][1], [catchpoint.com][2], [reuters.com][3]) |
| **IBGP synchronization issues**    | `show ip protocols` (Cisco before modern IOS)                   | Disable sync: `no synchronization` within `router bgp` context                                                                                                   |
| **Slow convergence**               | `show ip bgp`: track prefix arrival; `debug ip bgp events`      | Tune timers: `timers bgp 30 90`; adjust IGP timers; use `bgp fast-external-fallover`                                                                             |
| **Update burst overload**          | `show bgp flap-statistics`; `show bgp updates`                  | Enable damping: `bgp dampening`; consider suppressing update bursts                                                                                              |
| **RPKI validation failure**        | `show bgp rpki summary`; check `bgp update-group` logs          | Configure RPKI: `bgp rpki server x.x.x.x`, then `neighbor X.X.X.X route-validation`                                                                              |
| **Route leak detection**           | `show ip bgp neighbors X received-paths`, `show route leak log` | Use Peerlock/policies: prefix lists + `neighbor send-community route-map`, or implement Peerlock                                                                 |
| **Resource exhaustion / high CPU** | `show processes cpu`, `show memory`; `debug bgp updates`        | Limit prefixes: `bgp maxas-limit`, `bgp soft-reconfiguration`, disable unnecessary meshes                                                                        |
| **BGP hijack (prefix hijacking)**  | Inspect origin: `show bgp <prefix>`, check AS path(s)           | Filter invalid: `ip prefix-list approved seq X permit A.B.C.0/24`, `neighbor X prefix-list approved in`; deploy RPKI                                             |
| **AFI/SAFI mismatches**            | `show bgp ipv6 neighbors`, `show bgp vpnv4 summary`             | Enable specific families: `address-family ipv6`, `neighbor X activate`                                                                                           |


# 🔍 Summary of Key Additions

    TCP connectivity & ACL validation using telnet 179

    Multihop and loopback issues: ebgp-multihop, update-source commands
    
    IBGP synchronization: disable legacy sync

    Convergence tuning with timer adjustments
    
    Update bursts via damping settings
    
    Security hardening: RPKI, prefix filters, Peerlock against leaks and hijacks
    
