
                +------------+
                |  Router A  |  
                | 10.0.0.1   |
                +------------+
                      |
                      |  
                +------------+
                |  Router B  |
                | 192.0.2.1  |
                +------------+
                      |
                      |
                +------------+
                |  Router C  |
                |203.0.113.1 |
                +------------+
                      |
                      |
               ~~~ LOOP STARTS ~~~
                      |
                      v
                +------------+
                |  Router B  | ←───+
                +------------+     |
                      |            |
                      v            |
                +------------+     |
                |  Router C  |─────+
                +------------+


---
🔁 Scenario: Misconfigured Static Routes or Routing Protocols

    Router B thinks the best route to 198.51.100.1 is via Router C.

    Router C thinks the best route to 198.51.100.1 is via Router B.

    So when Router B receives the packet, it forwards it to C.

    Router C receives it and sends it back to B.

    The packet loops infinitely between them.
---
🔁 Why This Causes a Routing Loop

    Both routers have two static routes each pointing back to the other for 198.51.100.0/24.

    If the destination 198.51.100.1 is not available, packets loop:

        B ➝ C via Link 1

        C ➝ B via Link 2

        and repeat...

---
✅ To Stop the Loop add Blackhole Route to Null0

    Use ip route 198.51.100.0 255.255.255.0 null0 on Router C to blackhole.
---

```text
traceroute to 198.51.100.1, 30 hops max
 1  10.0.0.1             (Router A)
 2  192.0.2.1            (Router B)
 3  203.0.113.1          (Router C)
 4  192.0.2.1            (Router B)
 5  203.0.113.1          (Router C)
 6  192.0.2.1            (Router B)
 7  203.0.113.1          (Router C)
 8  192.0.2.1            (Router B)
 9  203.0.113.1          (Router C)
10  192.0.2.1            (Router B)
11  203.0.113.1          (Router C)
12  192.0.2.1            (Router B)
13  203.0.113.1          (Router C)
14  192.0.2.1            (Router B)
15  203.0.113.1          (Router C)
```

---

🔁 What It Shows:

    Packets are looping between Router B and Router C.

    There's likely a misconfigured static route or a dynamic routing protocol issue.

    The destination is never reached (no 198.51.100.1).

---

🧠 Tip for DevOps/Network Engineers:

    Use traceroute or mtr to visualize loops.

    Check route tables and BGP/OSPF configurations at the looping routers.

    Use debug ip routing, show ip route, or show ip cef on Cisco-like devices.
