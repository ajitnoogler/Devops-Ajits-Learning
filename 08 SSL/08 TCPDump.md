#### On Linux (Harmony Connect or Harmony Client)

| Command                                                                             | Description                                             |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------- |
| `sudo tcpdump -i eth0 -nn -s 0 -w /tmp/harmony.pcap`                                | Capture all packets on eth0 without truncation.         |
| `sudo tcpdump -i tun0 -nn -s 0 -w /tmp/harmony_tunnel.pcap`                         | Capture VPN/SASE tunnel traffic (if Harmony uses tun0). |
| `sudo tcpdump -i any port 443 or port 4500 -nn -s 0 -w /tmp/harmony_ssl_ipsec.pcap` | Focus on HTTPS and IPsec/DTLS ports.                    |
| `sudo tcpdump -r /tmp/harmony.pcap`                                                 | Read the saved capture.                                 |


#### On Windows (Harmony Endpoint or Harmony SASE Client)

| Tool / Method                    | Command / Steps                                                                  | Notes                                                                                    |
| -------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Wireshark**                    | Start GUI → Select NIC → Apply capture filter (e.g., `host 10.1.1.1`)            | Best for interactive packet inspection.                                                  |
| **dumpcap** (CLI from Wireshark) | `dumpcap -i 3 -w capture.pcap`                                                   | `-i 3` = interface index (check with `dumpcap -D`)                                       |
| **Npcap + WinDump**              | `windump -i 3 -w capture.pcap`                                                   | WinDump is the Windows port of `tcpdump`.                                                |
| **Harmony Client Debug**         | `C:\Program Files (x86)\CheckPoint\Endpoint Security\EPClient\tracer.exe /start` | Captures Harmony-specific logs (not full PCAP, but useful for endpoint troubleshooting). |

#### Harmony Client Packet Capture:

| Scenario                              | Windows Command                                                                                                                                     | Linux Command                                                          |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Full Traffic Capture**              | `"C:\Program Files (x86)\CheckPoint\Endpoint Security\EPClient\tracer.exe" /start /file "C:\Temp\full_traffic.cap"`                                 | `sudo tcpdump -i eth0 -w /tmp/full_traffic.pcap`                       |
| **Office 365 Traffic Capture**        | `"C:\Program Files (x86)\CheckPoint\Endpoint Security\EPClient\tracer.exe" /start /filter "host outlook.office365.com" /file "C:\Temp\o365.cap"`    | `sudo tcpdump -i eth0 host outlook.office365.com -w /tmp/o365.pcap`    |
| **SSL Handshake Issues**              | `"C:\Program Files (x86)\CheckPoint\Endpoint Security\EPClient\tracer.exe" /start /filter "port 443" /file "C:\Temp\ssl_handshake.cap"`             | `sudo tcpdump -i eth0 port 443 -w /tmp/ssl_handshake.pcap`             |
| **DNS Issues**                        | `"C:\Program Files (x86)\CheckPoint\Endpoint Security\EPClient\tracer.exe" /start /filter "port 53" /file "C:\Temp\dns_trace.cap"`                  | `sudo tcpdump -i any port 53 -w /tmp/dns_trace.pcap`                   |
| **Split Tunnel – Non-Tunnel Traffic** | `"C:\Program Files (x86)\CheckPoint\Endpoint Security\EPClient\tracer.exe" /start /filter "not host <gateway_IP>" /file "C:\Temp\split_tunnel.cap"` | `sudo tcpdump -i eth0 not host <gateway_IP> -w /tmp/split_tunnel.pcap` |
| **Stop Capture**                      | `"C:\Program Files (x86)\CheckPoint\Endpoint Security\EPClient\tracer.exe" /stop`                                                                   | `sudo pkill tcpdump`                                                   |


#### Harmony Client Packet Capture:
- "C:\Program Files (x86)\CheckPoint\Endpoint Security\EPClient\tracer.exe" /start /file "C:\Temp\full_traffic.cap"
- sudo tcpdump -i eth0 host outlook.office365.com -w /tmp/o365.pcap
- "C:\Program Files (x86)\CheckPoint\Endpoint Security\EPClient\tracer.exe" /start /filter "port 443" /file "C:\Temp\ssl_handshake.cap"   (SSL Handshake issues)
- sudo tcpdump -i eth0 port 443 -w /tmp/ssl_handshake.pcap (SSL Handshake issues)
- "C:\Program Files (x86)\CheckPoint\Endpoint Security\EPClient\tracer.exe" /start /filter "port 53" /file "C:\Temp\dns_trace.cap" (DNS Issues)
- sudo tcpdump -i any port 53 -w /tmp/dns_trace.pcap (DNS Issues)
- "C:\Program Files (x86)\CheckPoint\Endpoint Security\EPClient\tracer.exe" /start /filter "not host <gateway_IP>" /file "C:\Temp\split_tunnel.cap"  (Capture non Tunnel Pkts)
- sudo tcpdump -i eth0 not host <gateway_IP> -w /tmp/split_tunnel.pcap  (Capture non Tunnel Pkts)

#### Stopping the capture - "C:\Program Files (x86)\CheckPoint\Endpoint Security\EPClient\tracer.exe" /stop   | sudo pkill tcpdump


### More TCPDump Examples.

tcpdump -n -i eth0

tcpdump -c 5 -n -i eth0

tcpdump -D  -- display available interfaces

tcpdump -n -i eth0 port 22        specific port

tcpdump -n -i eth0 port22 src 192.168.0.2    specific source

tcpdump -n -i eth0 port22 dst 192.168.0.2    destination port

tcpdump src host 192.168.114.100 and dst host 192.168.1.1

tcpdump src host 192.168.114.1 and dst host 192.168.114.200 and dst port 80

tcpdump -w capture.pcap -i eth0  save as a file

tcpdump -tttt -r cature.pcap

tcpdump -i eth0 icmp   specific protocol

#### In tcpdump command, you can give “and”, “or” and “not” condition to filter the packets accordingly.
$ tcpdump -i eth0 not arp and not rarp

#### To view the traffic on a specific VLAN:
tcpdump -i Internal-VLAN

#### To view the traffic on a single specific interface:
tcpdump -i 1.1

#### To view the traffic on the management interface:
tcpdump -i eth0

#### To view the traffic on all TMM interfaces:
tcpdump -i 0.0

#### To view all packets that are traveling to or from a specific IP address:
tcpdump host 192.168.114.100

#### To view all packets that are traveling from a specific IP address:
tcpdump src host 192.168.114.1

#### To view all packets that are traveling to a particular IP address:
tcpdump dst host 192.168.1.1

#### View packets traveling through LTM & are either sourced from or destined to specific port
tcpdump port 80

#### View all packets that are traveling through LTM and sourced from a specific port:
tcpdump src port 80

#### View all packets that are traveling through the LTM and destined to a specific port:
tcpdump dst port 80

#### View all packets that from specific host with specific port number
tcpdump host 192.168.114.100 and port 80

#### View all packets that from source specific host with destination specific port number
tcpdump src host 192.168.114.100 and dst port 80

#### View all packets that from source specific host with destination specific host
tcpdump src host 192.168.114.100 and dst host 192.168.1.1
