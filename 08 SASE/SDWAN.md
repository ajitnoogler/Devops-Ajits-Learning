### SDWAN
- Analytics
- Orchestration
- Controllers
- Dataplane appliances

#### Benefits of SDWAN:
- Centralised mgmt
- Ease of Deployment - controller push config to branch or sites using zero touch.
- Reduced Cost
- Improved connectivity to the Branch and Cloud

#### Traditional Network:
It only routes based on metrics like cost and hop count or policy, but not app aware or latency based.

### Connectivity:
- Over Internet Broadband | 4G-5G | Mpls

 ### SDWAN features:
 - Traffic Steering based on Service and APPs
 - Application Aware Routing
 - Pktloss: 1% | Latency 10 ms | Jitter 3 ms

#### Packetloss
Packet loss occurs when one or more packets of data traveling across a network fail to reach their destination.
Measurement: Percentage of lost packets

<img width="550" height="100" alt="image" src="https://github.com/user-attachments/assets/cb3c342b-21f7-4bec-a924-55eb8b10725f" />


#### Latency 
Latency is the time it takes for a packet to travel from source to destination.
Measurement: RTT in millisec

#### Jitter
Jitter is the variation in packet arrival times. Even if average latency is low, inconsistent arrival can affect performance.
Measurement: Calculated as the difference in latency between consecutive packets

#### Summary 
| Metric      | What it is                       | Unit | Effect on Real-time Apps     | Example Tool           |
| ----------- | -------------------------------- | ---- | ---------------------------- | ---------------------- |
| Packet Loss | Lost packets on the network      | %    | Gaps, skips, retransmissions | ping, iperf, Wireshark |
| Latency     | Time for a packet to reach dest  | ms   | Delay in conversation, lag   | ping, traceroute       |
| Jitter      | Variation in packet arrival time | ms   | Choppy voice/video           | ping, iperf, Wireshark |
