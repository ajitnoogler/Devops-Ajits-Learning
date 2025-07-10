# 🖧 Assigning a Permanent Static IP on Oracle Linux (Without `nmcli`)

> ✅ Works on Oracle Linux 7/8/9 when **NetworkManager is disabled**, using traditional `ifcfg-*` files.

---

## 📋 Example Configuration

- Interface: `ens33`
- Static IP: `192.168.1.100`
- Gateway: `192.168.1.1`
- Subnet: `255.255.255.0`
- DNS: `8.8.8.8`

---

## 🪛 Steps to Configure Static IP

### 1️⃣ Find your interface name  
→ `ip a`  
(e.g., `ens33`, `eth0`)

---

### 2️⃣ Go to the network scripts directory  
→ `cd /etc/sysconfig/network-scripts/`

---

### 3️⃣ Edit the configuration file for your interface  
→ `vi ifcfg-ens33`  
*(Replace `ens33` with your actual interface name)*

---

### 4️⃣ Modify the file with the following content:

```ini
DEVICE=ens33
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.1.100
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8
