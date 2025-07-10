To test your monitoring tool, you can simulate various stress conditions on a Linux machine using the **`stress`** and **`stress-ng`** tools. These tools allow you to apply controlled CPU, memory, disk I/O, and network stress.

---

### ✅ **Installing the Tools**

**On RHEL/CentOS/Oracle Linux:**

```bash
sudo dnf install epel-release -y
sudo dnf install stress stress-ng -y
```

**On Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install stress stress-ng -y
```

---

## 🔧 Using `stress` to Create Load

### 1. **CPU Stress**

```bash
stress --cpu 4 --timeout 60
# Uses 4 CPU workers for 60 seconds
```

### 2. **Memory Stress**

```bash
stress --vm 2 --vm-bytes 512M --timeout 60
# Spawns 2 memory-hogging processes using 512MB each for 60 seconds
```

### 3. **Disk I/O Stress**

```bash
stress --io 2 --timeout 60
# 2 processes continuously sync data to disk
```

### 4. **Combined CPU + Memory + I/O**

```bash
stress --cpu 2 --io 2 --vm 2 --vm-bytes 256M --timeout 60
```

---

### 🔧 Using `stress-ng` for Advanced Testing

### 1. **CPU Burn (All Cores)**

```bash
stress-ng --cpu 0 --timeout 60s
# 0 = all logical cores
```

### 2. **I/O Stress**

```bash
stress-ng --hdd 2 --hdd-bytes 1G --timeout 60s
```

### 3. **Memory Stress**

```bash
stress-ng --vm 2 --vm-bytes 75% --timeout 60s
# Use 75% of system memory
```

### 4. **Network Stress (using sockets)**

```bash
stress-ng --sock 2 --timeout 60s
```

### 5. **Fork Bomb Simulation (Safely)**

```bash
stress-ng --fork 50 --timeout 60s
```

### 6. **All Stressors Together**

```bash
stress-ng --cpu 2 --io 2 --vm 2 --vm-bytes 256M --hdd 1 --timeout 60s
```

---

### 🧪 Use Cases to Monitor

| Scenario           | Metric to Watch               | Tool Used               |
| ------------------ | ----------------------------- | ----------------------- |
| High CPU           | CPU usage %                   | `stress` or `stress-ng` |
| Memory Leak        | Memory usage, swap usage      | `stress`, `stress-ng`   |
| I/O Bottleneck     | Disk latency, IOPS            | `stress`, `stress-ng`   |
| Fork Bomb          | Process count, load avg       | `stress-ng`             |
| Network Saturation | TCP connections, bytes in/out | `stress-ng`             |
| File Descriptor    | Open file descriptors         | `stress-ng --fd N`      |

---

### 📈 Monitoring Suggestions

While running these tests, use tools like:

* `top`, `htop`, `iotop`, `vmstat`, `iostat`, `dstat`
* Monitoring stack: **Prometheus + Grafana**, **Netdata**, **Nagios**, **Zabbix**

---

### ✅ Safety Tips

* Always test on non-production systems.
* Limit stress test duration using `--timeout`.
* Monitor system health (`loadavg`, `memory`, `disk`) in real-time.
* Stop with `Ctrl+C` or use `timeout` to auto-stop:

```bash
timeout 60s stress --cpu 2
```

---

📜 interactive_stress_test.sh

### 🧪 Interactive Linux Stress Test Script (DevOps/Monitoring Validation)

This script allows you to simulate multiple types of resource stress on a Linux system using `stress-ng`. Useful for testing Prometheus, Grafana, Netdata, Nagios, and other monitoring tools.

---

### 📜 Script: `interactive_stress_test.sh`

```bash
#!/bin/bash

echo "🧪 Interactive Linux Stress Test Tool"
echo "--------------------------------------"
read -p "Enter duration for each stress test (in seconds): " DURATION

echo
echo "Select stress tests to run (y/n):"

read -p "🔥 CPU stress? " cpu
read -p "💾 Memory stress? " mem
read -p "🖴 Disk I/O stress? " disk
read -p "🌐 Network socket stress? " net
read -p "📁 File Descriptor (FD) stress? " fd
read -p "👥 Fork Bomb (safe)? " fork
read -p "🧪 Full system combo stress? " full

echo
echo "🚀 Running selected stress tests..."
echo "📅 Start Time: $(date)"
echo

[[ "$cpu" =~ ^[Yy]$ ]] && {
  read -p "  → Number of CPU workers (0 for all cores): " cpu_workers
  stress-ng --cpu "$cpu_workers" --timeout ${DURATION}s
}

[[ "$mem" =~ ^[Yy]$ ]] && {
  read -p "  → Number of VM stressors: " mem_vm
  read -p "  → Memory usage per VM (e.g., 512M or 70%): " mem_size
  stress-ng --vm "$mem_vm" --vm-bytes "$mem_size" --timeout ${DURATION}s
}

[[ "$disk" =~ ^[Yy]$ ]] && {
  read -p "  → Number of HDD stressors: " hdd_count
  read -p "  → Total I/O size per stressor (e.g., 1G): " hdd_bytes
  stress-ng --hdd "$hdd_count" --hdd-bytes "$hdd_bytes" --timeout ${DURATION}s
}

[[ "$net" =~ ^[Yy]$ ]] && {
  read -p "  → Number of socket stressors: " sock_count
  stress-ng --sock "$sock_count" --timeout ${DURATION}s
}

[[ "$fd" =~ ^[Yy]$ ]] && {
  read -p "  → Number of file descriptors to open: " fd_count
  stress-ng --fd "$fd_count" --timeout ${DURATION}s
}

[[ "$fork" =~ ^[Yy]$ ]] && {
  read -p "  → Number of fork processes: " fork_count
  stress-ng --fork "$fork_count" --timeout ${DURATION}s
}

[[ "$full" =~ ^[Yy]$ ]] && {
  stress-ng --cpu 2 --io 2 --vm 2 --vm-bytes 256M --hdd 1 --timeout ${DURATION}s
}

echo
echo "✅ All selected tests completed."
echo "📅 End Time: $(date)"

---

### 🧪 Sample Output

$ sudo ./interactive_stress_test.sh
🧪 Interactive Linux Stress Test Tool
--------------------------------------
Enter duration for each stress test (in seconds): 30

Select stress tests to run (y/n):
🔥 CPU stress? y
💾 Memory stress? y
🖴 Disk I/O stress? n
🌐 Network socket stress? y
📁 File Descriptor (FD) stress? n
👥 Fork Bomb (safe)? y
🧪 Full system combo stress? n

🚀 Running selected stress tests...
📅 Start Time: Tue Jul 9 23:59:01 IST 2025

  → Number of CPU workers (0 for all cores): 2
stress-ng: info:  [4179] dispatching hogs: 2 cpu
stress-ng: info:  [4179] successful run completed in 30.00s

  → Number of VM stressors: 2
  → Memory usage per VM (e.g., 512M or 70%): 70%
stress-ng: info:  [4185] dispatching hogs: 2 vm
stress-ng: info:  [4185] successful run completed in 30.00s

  → Number of socket stressors: 4
stress-ng: info:  [4192] dispatching hogs: 4 sock
stress-ng: info:  [4192] successful run completed in 30.00s

  → Number of fork processes: 50
stress-ng: info:  [4201] dispatching hogs: 50 fork
stress-ng: info:  [4201] successful run completed in 30.00s

✅ All selected tests completed.
📅 End Time: Tue Jul 9 23:59:56 IST 2025

---
