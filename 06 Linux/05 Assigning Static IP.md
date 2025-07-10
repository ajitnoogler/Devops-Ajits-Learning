# 🖧 Assigning a Permanent Static IP using `nmcli` on Oracle Linux

> ✅ Tested on Oracle Linux 7/8/9 (requires NetworkManager)

---

## 📋 Example Configuration

- Interface: `ens33`
- Static IP: `192.168.1.100`
- Gateway: `192.168.1.1`
- Subnet: `/24` (i.e., `255.255.255.0`)
- DNS: `8.8.8.8`

---

## 🪛 Steps to Configure Static IP

### 1️⃣ Identify your network interface name → `nmcli con show`

### 2️⃣ Set static IP address → `nmcli con mod ens33 ipv4.addresses 192.168.1.100/24`

### 3️⃣ Set default gateway → `nmcli con mod ens33 ipv4.gateway 192.168.1.1`

### 4️⃣ Set DNS server → `nmcli con mod ens33 ipv4.dns 8.8.8.8`

### 5️⃣ Set IP method to manual (static) → `nmcli con mod ens33 ipv4.method manual`

### 6️⃣ Enable auto-connect on boot → `nmcli con mod ens33 connection.autoconnect yes`

### 7️⃣ Apply changes (restart connection) → `nmcli con down ens33 && nmcli con up ens33`

### 8️⃣ Verify IP and interface status → `ip a show ens33`

---

## 🧪 (Optional) Restart NetworkManager service → `systemctl restart NetworkManager`

---

## 🔁 To revert to DHCP → `nmcli con mod ens33 ipv4.method auto`

---
