

#### NAT-D (NAT Discovery):
This occurs in IKEv1 Phase 1, messages 3 and 4 (Main Mode).
The NAT-D payload contains a hash of the IP address and port from the original packet.
By exchanging these hashes, the devices can detect if the source/destination IP addresses and ports have been altered by a NAT device.

#### NAT-T (NAT Traversal):
Once a NAT device is detected using NAT-D, the UDP encapsulation begins in IKEv1 Phase 1, messages 5 and 6, changing the UDP port from 500 to 4500.
All subsequent IKE Phase 1 and the entire IKE Phase 2 (Quick Mode) exchange will then use UDP port 4500 for the ISAKMP/IKE traffic.
Even the IPsec data packets that follow the tunnel setup are encapsulated in UDP port 4500. 

#### For IKEv2:
IKEv2 has built-in NAT-T functionality, and while the exact message numbering isn't as detailed for NAT-T as IKEv1, 
the same process of NAT detection and UDP encapsulation occurs within its four-message exchange.
The detection and negotiation happen within the initial IKE Phase 1 messages, after which all subsequent IKE and IPsec traffic is encapsulated in UDP port 4500. 
