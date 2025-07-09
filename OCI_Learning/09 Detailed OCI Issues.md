
# 🛠️ Common Virtualization Issues in OCI – Full Resolution Guide with Commands & Logs

---

### 🟥 1. **VM Boot Failure**

**Symptoms:** VM stuck in “Starting”, “Terminated”, or blank screen on console.

#### ✅ Steps:

1. 🔌 **Connect via Console Connection**:

   ```bash
   ssh -i ~/.ssh/id_rsa opc@169.254.0.2
   ```

2. 📄 **Check boot logs**:

   ```bash
   journalctl -xb | head -50
   dmesg | grep -i error
   ```

   **Sample Error:**

   ```
   [FAILED] Failed to mount /boot
   [DEPEND] Dependency failed for Local File Systems
   ```

3. 🧱 **Check boot volume**:

   ```bash
   lsblk
   df -h
   ```

   **Sample Output:**

   ```
   NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
   sda      8:0    0  50G  0 disk 
   └─sda1   8:1    0  50G  0 part /
   ```

4. 🔄 **Recover by attaching boot volume to another instance**:

   * Detach and attach using OCI Console or:

     ```bash
     oci compute boot-volume-attachment detach --boot-volume-id <ocid>
     oci compute boot-volume-attachment attach --instance-id <rescue-vm> --boot-volume-id <ocid>
     ```

---

### 🟥 2. **No SSH Access**

**Symptoms:** “Permission denied”, “Connection refused”, or timeout on SSH.

#### ✅ Steps:

1. 🔌 **Use Console Connection** (see above)

2. 🔐 **Check SSHD logs and status**:

   ```bash
   sudo systemctl status sshd
   sudo tail -n 20 /var/log/secure
   ```

   **Sample Error:**

   ```
   Authentication refused: bad ownership or modes for directory /home/opc
   ```

3. 🧑‍💻 **Fix permissions & authorized\_keys**:

   ```bash
   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/authorized_keys
   cat ~/.ssh/authorized_keys
   ```

4. 🛡️ **Verify NSG and Security Lists** (Port 22):

   * Must allow `TCP 22` from your IP range
   * Use Console or:

     ```bash
     oci network security-list list --vcn-id <vcn-id>
     ```

---

### 🟥 3. **High CPU Usage**

**Symptoms:** Sluggish VM, high CPU in OCI monitoring.

#### ✅ Steps:

1. 📊 **Check CPU load inside VM**:

   ```bash
   top -n 1
   ps aux --sort=-%cpu | head
   ```

   **Sample Output:**

   ```
   PID  USER  %CPU COMMAND
   1234 apache  98  /usr/sbin/httpd -k start
   ```

2. 🔪 **Kill problematic process** (if needed):

   ```bash
   sudo kill -9 1234
   ```

3. 📈 **Resize instance (Console or CLI)**:

   ```bash
   oci compute instance update --instance-id <ocid> --shape VM.Standard3.Flex
   ```

4. ⚙️ **Optimize app config (e.g., reduce Apache workers)**

---

### 🟥 4. **Network Latency**

**Symptoms:** Slow app access, high ping times, or packet drops.

#### ✅ Steps:

1. 🔍 **Ping and traceroute test**:

   ```bash
   ping 10.0.2.10 -c 5
   traceroute 10.0.2.10
   ```

   **Sample Output:**

   ```
   1  10.0.1.1  1.12 ms
   2  10.0.2.10  6.03 ms
   ```

2. 🚦 **Run iperf3 test**:
   On web server:

   ```bash
   iperf3 -s
   ```

   On client:

   ```bash
   iperf3 -c 10.0.2.10 -P 4
   ```

   **Sample Output:**

   ```
   [SUM]   0.00-10.00 sec   108 MBytes  90.3 Mbits/sec
   ```

3. 🖧 **Check NIC driver**:

   ```bash
   ethtool ens3 | grep driver
   ```

   **Expect:** `driver: virtio_net`

4. ⚙️ **Switch to paravirtual NIC** in OCI Console if emulated is used

---

### 🟥 5. **Disk I/O Bottleneck**

**Symptoms:** App stalling, disk operations slow

#### ✅ Steps:

1. 📉 **Check I/O stats**:

   ```bash
   iostat -xz 1 3
   ```

   **Sample Output:**

   ```
   Device:    %util     r/s     w/s
   sda        98.0     2000    1500
   ```

2. 📤 **Check IOPS in OCI Block Volume Metrics**

3. 🛠️ **Upgrade performance tier**:

   ```bash
   oci bv volume update --volume-id <ocid> --performance "Higher Performance"
   ```

4. ⚖️ **Distribute load across multiple volumes (RAID or LVM)**

---

### 🟥 6. **Cloud-init Failures**

**Symptoms:** Public key missing, instance config skipped.

#### ✅ Steps:

1. 🔍 **View logs**:

   ```bash
   cat /var/log/cloud-init.log
   cat /var/log/cloud-init-output.log
   ```

   **Sample Error:**

   ```
   Failed to fetch instance metadata from http://169.254.169.254
   ```

2. 📝 **Check and reapply user-data script**:
   Example:

   ```bash
   #!/bin/bash
   echo "Hello from OCI" > /tmp/test.txt
   ```

3. 🔁 **Reboot or re-launch with fixed cloud-init**

---

### 🟥 7. **Incorrect Time Sync**

**Symptoms:** Logs show incorrect time, time drift issues.

#### ✅ Steps:

1. 🕒 **Install chrony**:

   ```bash
   sudo yum install chrony -y
   ```

2. 📝 **Set Oracle NTP server**:

   ```bash
   echo "server ntp.OracleCloud.com iburst" | sudo tee -a /etc/chrony.conf
   ```

3. 🔄 **Restart service**:

   ```bash
   sudo systemctl restart chronyd
   chronyc tracking
   ```

   **Sample Output:**

   ```
   Reference ID    : 132.163.97.1
   System time     : 0.000004671 seconds fast of NTP time
   ```

---

### 🟥 8. **Instance Stuck in Stopping/Terminating**

**Symptoms:** Instance won’t stop or terminate from console.

#### ✅ Steps:

1. 🔄 **Use OCI CLI to force reset**:

   ```bash
   oci compute instance action --instance-id <ocid> --action RESET
   ```

2. ⏳ **Wait 5–10 minutes** and retry termination

3. 🆘 **If still stuck:** Raise a service request via OCI Support

---

### 🟥 9. **Metadata Access Failure**

**Symptoms:** cloud-init fails to retrieve SSH key or user data.

#### ✅ Steps:

1. 🔌 **Test metadata access from inside VM**:

   ```bash
   curl http://169.254.169.254/opc/v1/instance/
   ```

   **Sample Output:**

   ```json
   {
     "region": "ap-mumbai-1",
     "displayName": "MyInstance",
     ...
   }
   ```

2. 🔥 **Check for firewalld/iptables rules**:

   ```bash
   sudo iptables -L -n
   sudo systemctl status firewalld
   ```

3. ✅ **Ensure NIC is configured correctly and has route to 169.254.169.254**

---
