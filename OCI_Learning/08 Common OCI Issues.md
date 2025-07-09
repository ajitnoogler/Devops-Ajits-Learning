
# 🛠️ Common Virtualization Issues in OCI and How to Resolve Them

| **Issue**                                         | **Troubleshooting Steps**                                                                                                                                                                                                                        |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **VM Boot Failure**                               | - Use **Serial Console** to connect and check boot logs<br>- Ensure **boot volume is attached**<br>- Check **boot diagnostics** in OCI console                                                                                                   |
| **No SSH Access**                                 | - Verify **NSG/Security Lists** allow port `22` inbound<br>- Confirm **correct public key** is added during instance creation<br>- Check **cloud-init** logs via serial console (`/var/log/cloud-init.log`)                                      |
| **High CPU Usage**                                | - Review **CPU metrics** in Monitoring<br>- **Resize instance** to a higher shape (e.g., VM.Standard3.Flex)<br>- Optimize **application performance** and offload background tasks                                                               |
| **Network Latency**                               | - Use **Paravirtualized NIC (VNIC) driver** for better performance<br>- Verify **routing tables**, NSGs, and security lists<br>- Use **traceroute, ping, iperf3** to test latency<br>- Use **regional placement groups** to reduce cross-AD hops |
| **Disk I/O Bottleneck**                           | - Check **Block Volume performance metrics**<br>- Use **multi-pathing** and **iSCSI tuning**<br>- Attach block volumes with **higher performance tiers**                                                                                         |
| **Cloud-init Failures**                           | - Use serial console to check `/var/log/cloud-init.log` and `/var/log/messages`<br>- Validate **user data script syntax**<br>- Reboot instance after fixing                                                                                      |
| **Incorrect Time Sync**                           | - Ensure **Chrony** or **NTP** is installed and synced with OCI NTP service: `ntp.OracleCloud.com`<br>- Check if outbound port `123` is allowed                                                                                                  |
| **Instance Stuck in “Stopping” or “Terminating”** | - Use **OCI CLI**: `oci compute instance action --action RESET`<br>- Contact OCI Support if instance doesn’t respond                                                                                                                             |
| **Metadata Access Failure**                       | - Verify that **metadata service (169.254.169.254)** is reachable from inside the instance<br>- Ensure no iptables/firewalld rules block it                                                                                                      |


# 🔧 Step-by-Step: Use iperf3 in OCI

| Purpose                       | Command                                         | Explanation                           |
| ----------------------------- | ----------------------------------------------- | ------------------------------------- |
| **Bidirectional test**        | `iperf3 -c <server-ip> -d`                      | Test send/receive in both directions  |
| **Reverse test**              | `iperf3 -c <server-ip> -R`                      | Test from server → client             |
| **Longer test duration**      | `iperf3 -c <server-ip> -t 30`                   | 30 seconds duration                   |
| **Set parallel streams**      | `iperf3 -c <server-ip> -P 4`                    | Use 4 simultaneous connections        |
| **UDP test (latency/jitter)** | `iperf3 -c <server-ip> -u -b 100M`              | UDP test with 100 Mbps bandwidth      |
| **Custom port**               | `iperf3 -s -p 8888`<br>`iperf3 -c <ip> -p 8888` | Use custom port (open it in NSG!)     |
| **JSON output (for logging)** | `iperf3 -c <server-ip> -J > result.json`        | Useful for automation and log parsing |


# 🔍 Interpreting Results

  -  Bandwidth (sender/receiver): Throughput in Mbps or Gbps

  -  Jitter (UDP): Packet timing variation — high jitter = bad for voice/video

  -  Retransmissions (TCP): Sign of packet loss or congestion

  -   CPU Utilization (if high): May impact results; use Flex shape with sufficient vCPUs

    

# 🧱 NSG & Routing Checklist for iperf3

- Allow TCP port 5201 (or custom port) in NSG and Security List

- Ensure private subnet routing between instances (via DRG, LPG, or VCN peering)

- Use private IP for internal testing to avoid internet latency


---

### 🔧 Step-by-Step: Use `iperf3` in OCI

#### ✅ Step 1: Install iperf3 on both instances

```bash
sudo yum install iperf3 -y      # Oracle Linux / CentOS / RHEL
# or
sudo apt install iperf3 -y      # Debian / Ubuntu
```

---

### 🖥️ On the **Server Instance** (listener side)

```bash
iperf3 -s
```

* Runs iperf3 in **server mode**, listening on port **5201**
* Ensure **port 5201** is **open in NSG/Security List**

---

### 💻 On the **Client Instance** (tester side)

```bash
iperf3 -c <server-private-ip>
```

* Runs a **default 10-second test** for **throughput**
* Output includes **bandwidth (Mbps)** and **retransmissions**

---


# Here's a **sample scenario** with simulated `iperf3` usage and output to troubleshoot latency between a client and a web application hosted in OCI:

---

### 📘 **Scenario: Web App Latency in OCI**

#### 🧑‍💼 **User Complaint:**

> “The web application hosted in the OCI private subnet is **very slow**. Pages take 5–10 seconds to load from my Linux client in another subnet/VPN-connected site.”

---

### 🧪 **Objective:**

Use `iperf3` to test **network throughput and latency** between:

* **Client instance**: `10.0.1.5` (User's machine or test Linux VM)
* **Web server instance**: `10.0.2.10` (Private IP of OCI Web App host)

---

### 🔧 Step-by-Step Testing with iperf3

#### On **Web App VM (Server Mode):**

```bash
iperf3 -s
```

*Output:*

```
-----------------------------------------------------------
Server listening on 5201
-----------------------------------------------------------
```

---

#### On **Client VM (Client Mode):**

```bash
iperf3 -c 10.0.2.10
```

---

### 🧾 Sample Output:

```
Connecting to host 10.0.2.10, port 5201
[  5] local 10.0.1.5 port 50432 connected to 10.0.2.10 port 5201
[ ID] Interval           Transfer     Bandwidth       Retr
[  5]   0.00-1.00   sec   2.50 MBytes  21.0 Mbits/sec    3
[  5]   1.00-2.00   sec   2.35 MBytes  19.7 Mbits/sec    2
[  5]   2.00-3.00   sec   2.60 MBytes  21.8 Mbits/sec    1
[  5]   3.00-4.00   sec   2.42 MBytes  20.3 Mbits/sec    4
[  5]   4.00-5.00   sec   2.20 MBytes  18.5 Mbits/sec    5
[  5]   5.00-6.00   sec   2.10 MBytes  17.6 Mbits/sec    4
[  5]   6.00-7.00   sec   2.00 MBytes  16.8 Mbits/sec    6
[  5]   7.00-8.00   sec   2.00 MBytes  16.8 Mbits/sec    7
[  5]   8.00-9.00   sec   2.10 MBytes  17.6 Mbits/sec    6
[  5]   9.00-10.00  sec   2.15 MBytes  18.0 Mbits/sec    4
- - - - - - - - - - - - - - - - - - - - - - - - - -
[  5]  0.00-10.00  sec  22.5 MBytes  18.9 Mbits/sec   42             sender
[  5]  0.00-10.00  sec  22.0 MBytes  18.4 Mbits/sec                  receiver
```

---

### 🧠 **Analysis:**

* **Low throughput (18 Mbps)** and **42 retransmissions** over 10 seconds
* Suggests **packet loss, congestion**, or **sub-optimal path**
* Possibly caused by:

  * **Overloaded subnet gateway**
  * **VPN/DRG latency**
  * **Incorrect MTU or misconfigured NIC**

---

### ✅ **Next Steps:**

1. **Enable Paravirtual NIC** in web server
2. Check **Security Lists/NSG** for any connection throttling
3. Use `traceroute` or `mtr` from client to web server
4. Consider testing with:

   ```bash
   iperf3 -c 10.0.2.10 -t 30 -P 4
   iperf3 -c 10.0.2.10 -u -b 100M
   ```

# 🧪 Suggested iperf3 Commands for Gigabit Link Testing

# Run longer test with parallel streams
iperf3 -c 10.0.2.10 -t 60 -P 4

# Use a larger TCP window (better for high-BW links)
iperf3 -c 10.0.2.10 -w 1M

# UDP test for jitter/loss
iperf3 -c 10.0.2.10 -u -b 1G

# 🔍 Possible Causes on a Gigabit Link

| Category                 | Root Cause                                                                           | Resolution                                                  |
| ------------------------ | ------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| **NIC Type**             | Using **emulated NIC** instead of **paravirtualized (VFIO)**                         | Check and switch to **paravirtual NIC** in OCI console      |
| **Security Rules**       | NSG/Security List throttling via **improper egress rules**                           | Ensure no **unintended blocking or rate-limiting**          |
| **DRG/VPN bottleneck**   | If traffic crosses **DRG/IPSec VPN**, tunnel overhead or **throttle** may apply      | Run iperf **within the same VCN** to isolate VPN issue      |
| **Instance Shape**       | Using a shape with **low bandwidth quota** (e.g., VM.Standard.E2.1.Micro = 480 Mbps) | Check shape bandwidth limits on OCI docs; try resizing      |
| **CPU Limitations**      | High CPU steal/wait due to small or busy instance                                    | Use `top`, `sar`, or `vmstat` to analyze CPU                |
| **TCP Window Size**      | Insufficient TCP buffer size or congestion control issues                            | Use `iperf3 -w 512K` or adjust sysctl TCP settings          |
| **MTU mismatch**         | MTU not set correctly (especially over VPN)                                          | Run `ping -M do -s 1472 <target>` to test for fragmentation |
| **Background Processes** | Other traffic on NIC consuming bandwidth                                             | Monitor with `iftop`, `nload`, or `netstat -s`              |
