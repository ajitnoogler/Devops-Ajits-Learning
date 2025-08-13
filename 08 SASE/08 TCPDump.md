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
