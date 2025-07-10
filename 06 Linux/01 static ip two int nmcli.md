 **`nmcli` version** of configuring **two NICs (public + private)** in Oracle Linux, formatted in `.md` with **step → command** style:

---

```markdown
# 🖧 Configure Two NICs (Public + Private) in Oracle Linux using `nmcli`

> ✅ For Oracle Linux 7/8/9 with `NetworkManager` enabled  
> 🎯 Goal: eth0 → public IP + gateway; eth1 → private IP only, no default route

---

## 🪛 Configuration Steps

### 1️⃣ Show all network interfaces → `nmcli device status`

---

### 2️⃣ Set static IP on public interface (`eth0`)  
→ `nmcli con mod eth0 ipv4.addresses 10.0.0.10/24`

---

### 3️⃣ Set default gateway on `eth0`  
→ `nmcli con mod eth0 ipv4.gateway 10.0.0.1`

---

### 4️⃣ Set DNS for `eth0`  
→ `nmcli con mod eth0 ipv4.dns 8.8.8.8`

---

### 5️⃣ Set IP assignment method to manual on `eth0`  
→ `nmcli con mod eth0 ipv4.method manual`

---

### 6️⃣ Enable autoconnect for `eth0`  
→ `nmcli con mod eth0 connection.autoconnect yes`

---

### 7️⃣ Set static IP on private interface (`eth1`)  
→ `nmcli con mod eth1 ipv4.addresses 192.168.0.10/24`

---

### 8️⃣ Disable default route on `eth1`  
→ `nmcli con mod eth1 ipv4.never-default yes`

---

### 9️⃣ Set IP assignment method to manual on `eth1`  
→ `nmcli con mod eth1 ipv4.method manual`

---

### 🔟 Enable autoconnect for `eth1`  
→ `nmcli con mod eth1 connection.autoconnect yes`

---

### 1️⃣1️⃣ Bring down and up both interfaces to apply changes  
→ `nmcli con down eth0 && nmcli con up eth0`  
→ `nmcli con down eth1 && nmcli con up eth1`

---

### 1️⃣2️⃣ Verify IPs and routes  
→ `ip a`  
→ `ip route`

---

## ✅ Expected Output (Route Table)

```

default via 10.0.0.1 dev eth0

10.0.0.0/24 dev eth0 ...

192.168.0.0/24 dev eth1 ...

```


