Key issues that can occur between **eBGP** and **iBGP** neighbors—and how to resolve them:

---

## 🧩 1. Session Establishment Failures

**Issues**

* **Interface/TCP reachability**: Layer‑1/2 down, wrong IP, ACL or firewall blocking TCP 179 ([networklessons.com][1]).
* **TTL problems**: eBGP uses TTL=1 by default, so neighbors via loopback or multi-hop require `ebgp-multihop`; iBGP needs `update-source` set to loopback ([networklessons.com][1]).

**Solutions**

* Ensure interfaces are up, IPs match, ACLs permit TCP 179.
* For eBGP over non-direct links: `neighbor X ebgp-multihop N`.
* For loopback peering: `neighbor X update-source loopback0`.

---

## 2. Missing Route Advertisement

**Issues**

* iBGP does **not** forward routes learned from one iBGP neighbor to another (split-horizon rule) ([fr.wikipedia.org][2], [pynetlabs.com][3]).
* Learned eBGP routes may not be distributed via iBGP if next-hop is unreachable internally ([networkengineering.stackexchange.com][4]).

**Solutions**

* Use **route reflectors** or **full‑mesh iBGP** to ensure all routers share routes.
* Use next-hop-self on eBGP edge routers so iBGP peers can reach next-hops:
  `neighbor X next-hop-self`.

---

## 3. RIB Installation Conflicts

**Issues**

* A redistributed IGP route might win over an eBGP route due to administrative distance (IGP < eBGP) and default BGP weight settings ([noction.com][5], [cisco.com][6]).

**Solutions**

* Increase BGP weight for desired eBGP-learned routes (e.g. `neighbor X weight 40000`).
* Or adjust administrative distance or prefer using route maps/prefix-lists to control route preference.

---

## 4. Slow Convergence / Flapping

**Issues**

* iBGP full-mesh scalability N²; route reflectors or confederations can help but add complexity and potential convergence delay ([cisco.com][6], [synchronet.net][7], [en.wikipedia.org][8]).
* Frequent route flaps lead to instability ([en.wikipedia.org][8]).

**Solutions**

* Deploy **route reflectors** or **BGP confederations** to avoid full mesh requirements.
* Use **route flap damping** or **BFD** to mitigate flapping, though damping is less recommended nowadays.

---

## 5. Attribute & Path Selection Mismatches

**Issues**

* eBGP adds its AS to the AS\_PATH and changes next-hop; iBGP does not ([en.wikipedia.org][8], [pynetlabs.com][3]).
* Due to administrative distance (20 for eBGP, 200 for iBGP), routers prefer eBGP paths ([pynetlabs.com][3]).
* Best‑path selection may not align with policy expectations (e.g., iBGP path chosen over eBGP) ([community.cisco.com][9]).

**Solutions**

* Tune BGP attributes: weight, local-preference, MED, AS‑path prepending to influence path selection.
* Use `bgp bestpath as-path ignore` or modify admin distance if desired.

---

### ✅ Summary Table

| Category                    | Issue                                                                 | Solution                                               |
| --------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------ |
| **Session Setup**           | Interface down, TTL, update-source mismatches                         | Up interfaces, ACLs, `ebgp-multihop`, `update-source`  |
| **Route Advertisement**     | iBGP split-horizon, unreachable next-hop                              | Full-mesh or reflectors, `next-hop-self`               |
| **RIB Conflicts**           | IGP route preferred over eBGP, weight defaults                        | Adjust weight, AD, use route filtering                 |
| **Scalability & Stability** | Full-mesh N², flapping, slow convergence                              | Reflectors/confederations, flap damping/BFD            |
| **Path Attributes**         | AS\_PATH differences, admin-distance bias, unexpected best-path picks | Tune weight, localPref, MED, AS‑prepends, or adjust AD |

---

By understanding these issues and applying the appropriate configuration fixes—interface and TCP checks, TTL and source settings, route-sharing designs, attribute tuning, and stability mechanisms—you can ensure robust and efficient BGP neighbor relationships.

Let me know if you'd like detailed configuration examples for a specific router platform!

[1]: https://networklessons.com/bgp/troubleshooting-bgp-neighbor-adjacency?utm_source=chatgpt.com "Troubleshooting BGP Neighbor Adjacency - NetworkLessons.com"
[2]: https://fr.wikipedia.org/wiki/Border_Gateway_Protocol?utm_source=chatgpt.com "Border Gateway Protocol"
[3]: https://www.pynetlabs.com/ibgp-vs-ebgp-whats-the-difference/?utm_source=chatgpt.com "iBGP vs eBGP - What's the Difference? - PyNet Labs"
[4]: https://networkengineering.stackexchange.com/questions/5748/learned-ebgp-routes-not-distributed-to-ibgp-neighbors?utm_source=chatgpt.com "Learned eBGP routes not distributed to iBGP neighbors"
[5]: https://www.noction.com/knowledge-base/bgp-network-troubleshooting?utm_source=chatgpt.com "BGP Network Troubleshooting Best Practices - Noction"
[6]: https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/218027-troubleshoot-border-gateway-protocol-bas.html?utm_source=chatgpt.com "Troubleshoot Border Gateway Protocol Basic Issues - Cisco"
[7]: https://synchronet.net/ebgp-vs-ibgp/?utm_source=chatgpt.com "Understanding eBGP vs iBGP: Key Differences - SynchroNet"
[8]: https://en.wikipedia.org/wiki/Border_Gateway_Protocol?utm_source=chatgpt.com "Border Gateway Protocol"
[9]: https://community.cisco.com/t5/routing/ebgp-vs-ibgp-path-selection-vs-admin-distance/td-p/497657?utm_source=chatgpt.com "eBGP vs iBGP (Path selection vs Admin Distance) - Cisco Community"
