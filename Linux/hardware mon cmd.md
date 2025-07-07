

🧠 System Health Check Commands for Linux (Cloud & Bare-Metal)

| 🔍 Area            | ✅ Command                      | 💬 Description                                    | 🏷️ Notes                                  |                                 |
| ------------------ | ------------------------------ | ------------------------------------------------- | ------------------------------------------ | ------------------------------- |
| **CPU Usage**      | `top`                          | Live view of processes and CPU usage              | Use `htop` for a better UI                 |                                 |
|                    | `mpstat -P ALL 1`              | CPU usage per core                                | Part of `sysstat` package                  |                                 |
| **Memory Usage**   | `free -h`                      | Human-readable RAM and swap stats                 | Use `-m` for MB output                     |                                 |
|                    | `cat /proc/meminfo`            | Detailed memory stats                             | Helpful for tuning                         |                                 |
| **Swap Usage**     | `swapon --show`                | Shows active swap devices                         |                                            |                                 |
| **Disk Space**     | `df -h`                        | Disk usage of file systems in human-readable form | Look for `/` and `/var`                    |                                 |
| **Disk I/O**       | `iostat -xz 1`                 | Detailed disk I/O stats per second                | Install `sysstat`                          |                                 |
| **Disk Health**    | `sudo smartctl -a /dev/sda`    | SMART health status of disk                       | Requires `smartmontools`; not on cloud VMs |                                 |
| **Thermal**        | `sensors`                      | Shows CPU/GPU temps, fan speeds                   | Requires `lm-sensors`; may not work in VMs |                                 |
| **CPU Info**       | `lscpu`                        | Shows CPU model, cores, threads                   |                                            |                                 |
| **Memory Details** | `sudo dmidecode --type memory` | Shows physical RAM slot info                      | Helpful on bare-metal servers              |                                 |
| **Quick Summary**  | \`top -b -n 1                  | head -20 && df -h && free -h\`                    | Combined CPU, disk, and memory snapshot    | Good for reporting/log snapshot |
| **All-in-One**     | `glances`                      | Real-time multi-resource monitor                  | Install via `sudo apt install glances`     |                                 |
| **Realtime Stats** | `dstat -cdnm`                  | CPU, disk, net, and memory usage                  | Install with `dstat` package               |                                 |



Here are the **essential Linux commands** to check **CPU, memory, swap, disk, and system cooling** (thermal/temperature), 
especially useful for **Cloud Engineers** monitoring VMs or bare-metal instances.

---

## ✅ 1. **Check CPU Usage**

```bash
top
```

Or:

```bash
mpstat -P ALL 1
```

> Shows CPU usage per core (install via `sysstat` package if needed).

---

## ✅ 2. **Check Memory and Swap Usage**

```bash
free -h
```

> Summary of total, used, free, buffer/cache, and swap memory.

Or more detailed:

```bash
cat /proc/meminfo
```

---

## ✅ 3. **Check Disk Usage**

### 🔹 Disk space usage:

```bash
df -h
```

> Shows filesystem usage in human-readable format.

### 🔹 Disk I/O usage:

```bash
iostat -x 1
```

> Gives IOPS, utilization, and latency (install via `sysstat`).

---

## ✅ 4. **Check Disk Health (SMART)**

```bash
sudo smartctl -a /dev/sda
```

> Requires `smartmontools`; works only on bare-metal or passthrough disks (not typical for cloud VMs).

---

## ✅ 5. **Check Thermal (CPU/GPU cooling temperature)**

```bash
sensors
```

> Shows temperatures of CPU cores, fan speeds, etc.
> Needs package:

```bash
sudo apt install lm-sensors
sudo sensors-detect
```

---

## ✅ 6. **Check Hardware (CPU/Memory info)**

### 🔹 CPU Info:

```bash
lscpu
```

### 🔹 Memory Info (DIMM slots, size):

```bash
sudo dmidecode --type memory
```

---

## ✅ 7. **One-Liner for Summary**

```bash
top -b -n 1 | head -n 20 && df -h && free -h
```

> Combines CPU, memory, and disk usage in one shot.

---

## ✅ 8. **Optional Cloud-Friendly Tools**

* **Glances**: All-in-one system monitor

  ```bash
  sudo apt install glances
  glances
  ```

* **Dstat**: Realtime CPU, memory, disk, and net usage

  ```bash
  dstat -cdnm
  ```

---

### 🔧 Notes for Cloud Engineers:

* In **cloud VMs**, thermal sensors (`sensors`) may not work unless it's a **bare-metal** or **dedicated host**.
* For cloud-native metrics, use:

  * **AWS CloudWatch**
  * **OCI Monitoring**
  * **Azure Monitor**

---

Let me know your cloud provider or distro (Ubuntu, RHEL, etc.), and I’ll tailor the commands for your environment.
