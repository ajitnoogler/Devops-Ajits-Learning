**Configuring two interfaces (public and private)** in Oracle Linux using the **legacy method** (without `nmcli`), using `ifcfg-*` files only — ideal for OCI VMs where `NetworkManager` is disabled or not used.

---

````markdown
# 🖧 Oracle Linux – Two NIC Configuration (Public + Private IP) using Legacy `ifcfg-*` Files

> ✅ Use this if you're managing a VM with two interfaces in OCI and NOT using `nmcli` or `NetworkManager`.

---

## 📋 Example Setup

| Interface | IP Address      | Gateway      | Role           |
|-----------|------------------|--------------|----------------|
| `eth0`    | `10.0.0.10`      | `10.0.0.1`   | Public Subnet  |
| `eth1`    | `192.168.0.10`   | *None*       | Private Subnet |

> ⚠️ Only `eth0` (Public) should have the default gateway.

---

## 🪛 Configuration Steps

### 1️⃣ Find your interface names  
→ `ip link` or `ip a`

---

### 2️⃣ Go to the network scripts directory  
→ `cd /etc/sysconfig/network-scripts/`

---

### 3️⃣ Edit config file for `eth0` (public interface)

```ini
# vi ifcfg-eth0
DEVICE=eth0
BOOTPROTO=static
ONBOOT=yes
IPADDR=10.0.0.10
NETMASK=255.255.255.0
GATEWAY=10.0.0.1
DNS1=8.8.8.8
DEFROUTE=yes
````

---

### 4️⃣ Edit config file for `eth1` (private interface)

```ini
# vi ifcfg-eth1
DEVICE=eth1
BOOTPROTO=static
ONBOOT=yes
IPADDR=192.168.0.10
NETMASK=255.255.255.0
DEFROUTE=no
```

---

### 5️⃣ Disable NetworkManager (if running)

```bash
systemctl stop NetworkManager
systemctl disable NetworkManager
systemctl enable network
systemctl start network
```

---

### 6️⃣ Restart the network service

```bash
systemctl restart network
```

---

### 7️⃣ Verify IP and routes

```bash
ip a
ip route
```

Expected route table:

```
default via 10.0.0.1 dev eth0
10.0.0.0/24 dev eth0 proto kernel scope link src 10.0.0.10
192.168.0.0/24 dev eth1 proto kernel scope link src 192.168.0.10
```

---

## 🧪 Troubleshooting

* **No internet access?** → Check `GATEWAY` is set only on public interface.
* **Duplicate routes?** → Ensure `DEFROUTE=no` is present in `eth1` file.
* **DNS resolution fails?** → Make sure `DNS1` is set only in `eth0` config or `/etc/resolv.conf`.

---

## 📝 Notes

* You can also use `RESOLV_CONF=no` in `ifcfg-eth1` to prevent override.
* You may also configure routing tables and rules manually using `ip rule` and `ip route` for advanced traffic separation (policy routing).

---
now if you want the same in a downloadable `.md` file or a companion diagram for VCN/Subnet layout in OCI.
```
