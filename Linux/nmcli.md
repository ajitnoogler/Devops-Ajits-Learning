# nmcli is a **command-line tool** for **managing Network-Manager** 
— a daemon that handles network connections (Ethernet, Wi-Fi, VPN, etc.) on many modern Linux distros.

---

## 🔧 What is `nmcli`?

* `nmcli` = NetworkManager Command Line Interface
* Useful for **headless systems**, **scripts**, and **automating network configuration**
* Supports Ethernet, Wi-Fi, bonding, bridging, VLANs, and more

---

## 🔍 Basic `nmcli` Structure

```bash
nmcli [OPTIONS] OBJECT { COMMAND | help }
```

**OBJECTS**: `device`, `connection`, `networking`, `radio`, `general`, etc.

---

## 📦 Common Use Cases with Commands & Sample Output

---

### ✅ 1. **Check Network Status**

```bash
nmcli general status
```

📘 **Output:**

```
STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
connected  full          enabled  enabled  enabled  enabled
```

---

### ✅ 2. **List Devices**

```bash
nmcli device
```

📘 **Output:**

```
DEVICE  TYPE      STATE      CONNECTION         
eth0    ethernet  connected  Wired connection 1
wlan0   wifi      connected  MyWiFiNetwork
lo      loopback  unmanaged  --
```

---

### ✅ 3. **Show IP Address of Active Interfaces**

```bash
nmcli device show eth0 | grep IP4
```

📘 **Output:**

```
IP4.ADDRESS[1]:                         192.168.1.100/24
IP4.GATEWAY:                            192.168.1.1
```

---

### ✅ 4. **List All Saved Connections**

```bash
nmcli connection show
```

📘 **Output:**

```
NAME               UUID                                  TYPE      DEVICE 
Wired connection 1 6f663d3f-54d9-4a82-9c17-f0c8ff4e1d2e  ethernet  eth0
MyWiFiNetwork      e45a34c2-c1cb-4a70-81e3-eaac93a9a874  wifi      wlan0
```

---

### ✅ 5. **Connect to a Wi-Fi Network**

```bash
nmcli device wifi list
nmcli device wifi connect "MyWiFiNetwork" password "mypassword"
```

📘 **Output:**

```
Device 'wlan0' successfully activated with 'e45a34c2-c1cb-4a70-81e3-eaac93a9a874'.
```

---

### ✅ 6. **Assign Static IP to Ethernet Interface**

```bash
nmcli con mod "Wired connection 1" ipv4.addresses 192.168.1.200/24
nmcli con mod "Wired connection 1" ipv4.gateway 192.168.1.1
nmcli con mod "Wired connection 1" ipv4.dns "8.8.8.8 1.1.1.1"
nmcli con mod "Wired connection 1" ipv4.method manual
nmcli con up "Wired connection 1"
```

---

### ✅ 7. **Create a New Ethernet Connection**

```bash
nmcli con add type ethernet ifname eth0 con-name static-lan ip4 192.168.1.250/24 gw4 192.168.1.1
```

---

### ✅ 8. **Set DNS Servers**

```bash
nmcli con mod static-lan ipv4.dns "8.8.8.8 1.1.1.1"
```

---

### ✅ 9. **Bring a Connection Up or Down**

```bash
nmcli connection down static-lan
nmcli connection up static-lan
```

---

### ✅ 10. **Delete a Connection**

```bash
nmcli connection delete static-lan
```

---

## 🛠️ Real-World Use Cases

| Scenario                   | Command                      | Purpose                         |
| -------------------------- | ---------------------------- | ------------------------------- |
| Cloud VM with no GUI       | `nmcli device` + `nmcli con` | Check IP, configure interfaces  |
| Static IP assignment       | `nmcli con mod ...`          | Avoid DHCP for servers          |
| Wi-Fi troubleshooting      | `nmcli device wifi list`     | Check signal, retry connections |
| Headless Raspberry Pi      | `nmcli dev wifi connect`     | Set up wireless without GUI     |
| Network restart via script | `nmcli networking off && on` | Automate network bounce         |

---

## 📌 Tips

* Use `nmcli` over editing `/etc/sysconfig/network-scripts` or `/etc/network/interfaces` in **NetworkManager-enabled distros** (RHEL7+, CentOS7+, Ubuntu 18.04+).
* Combine with `bash` for scripting or cron automation.

---

🧾 Script: set_static_ip.sh  (Interactive Version)

# 🖧 Static IP Configuration Script using `nmcli`

This interactive bash script uses `nmcli` to configure a static IP address for a network interface on Linux systems that use **NetworkManager** (e.g., RHEL 7+, CentOS 7+, Ubuntu 18.04+).

---

## 🔧 Features

- Interactive prompts for:
  - Interface name
  - Static IP address
  - Gateway
  - DNS servers
  - Connection name
- Deletes existing connection if name conflicts
- Uses `nmcli` to configure and activate the connection
- Colored success message for easy visibility

---

## 📜 Script: `set_static_ip.sh`

```bash
#!/bin/bash

# 🛑 Exit on any error
set -e

echo "🔧 Configure Static IP Using nmcli"
echo "----------------------------------"

# 🖧 Ask for interface name
read -rp "Enter network interface name (e.g., eth0): " IFACE

# 🌐 Ask for static IP and subnet
read -rp "Enter static IP address with CIDR (e.g., 192.168.1.100/24): " IPADDR

# 🚪 Ask for default gateway
read -rp "Enter default gateway (e.g., 192.168.1.1): " GATEWAY

# 📡 Ask for DNS servers
read -rp "Enter DNS servers (space separated, e.g., 8.8.8.8 1.1.1.1): " DNS_SERVERS

# 🔁 Ask for connection name
read -rp "Enter connection name to create (default: static-connection): " CON_NAME
CON_NAME=${CON_NAME:-static-connection}

echo ""
echo "📝 Summary:"
echo "Interface  : $IFACE"
echo "IP Address : $IPADDR"
echo "Gateway    : $GATEWAY"
echo "DNS        : $DNS_SERVERS"
echo "Connection : $CON_NAME"
echo ""

# ⚠️ Delete if existing connection with same name
nmcli connection delete "$CON_NAME" 2>/dev/null || true

# ➕ Add new connection
nmcli connection add type ethernet ifname "$IFACE" con-name "$CON_NAME" ip4 "$IPADDR" gw4 "$GATEWAY"

# 🌐 Set DNS and manual method
nmcli connection modify "$CON_NAME" ipv4.dns "$DNS_SERVERS"
nmcli connection modify "$CON_NAME" ipv4.method manual

# 🔄 Bring up connection
nmcli connection up "$CON_NAME"

# ✅ Success
echo -e "\n✅ \e[32mStatic IP configured and applied successfully on $IFACE using '$CON_NAME'.\e[0m"

# End of Script
-----------------------------------------------------------------------------------------------------------------------------------

# Run with ...
chmod +x set_static_ip.sh
sudo ./set_static_ip.sh

# 📌 Optional: Set to Run at Boot (Just Once)
(crontab -l ; echo "@reboot /path/to/set_static_ip.sh") | crontab -

# 🧪 Sample Run: sudo ./set_static_ip.sh

🔧 Configure Static IP Using nmcli
----------------------------------
Enter network interface name (e.g., eth0): eth0
Enter static IP address with CIDR (e.g., 192.168.1.100/24): 192.168.1.250/24
Enter default gateway (e.g., 192.168.1.1): 192.168.1.1
Enter DNS servers (space separated, e.g., 8.8.8.8 1.1.1.1): 8.8.8.8 1.1.1.1
Enter connection name to create (default: static-connection): static-lan

📝 Summary:
Interface  : eth0
IP Address : 192.168.1.250/24
Gateway    : 192.168.1.1
DNS        : 8.8.8.8 1.1.1.1
Connection : static-lan

Connection 'static-lan' (e4d24279-1234-4f9d-aabe-1111f4ed8bd1) successfully added.
Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/5)

✅ Static IP configured and applied successfully on eth0 using 'static-lan'.

