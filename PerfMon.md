**performance monitoring tools in Linux**, categorized by function:

---

## 🧠 **Essential Performance Monitoring Tools in Linux**

### 📊 **CPU Monitoring**

| Tool      | Description                             | Sample Command    |
| --------- | --------------------------------------- | ----------------- |
| `top`     | Real-time CPU, memory, process usage    | `top`             |
| `htop`    | Enhanced version of top with UI         | `htop`            |
| `mpstat`  | Per-CPU usage stats                     | `mpstat -P ALL 1` |
| `pidstat` | Per-process CPU usage                   | `pidstat 1`       |
| `sar`     | Historic CPU stats (part of sysstat)    | `sar -u 1 3`      |
| `vmstat`  | CPU, memory, IO, context switch summary | `vmstat 1`        |
| `dstat`   | Versatile CPU, disk, net, memory stats  | `dstat -cdngyt`   |

---

### 💾 **Memory Monitoring**

| Tool         | Description                     | Sample Command |
| ------------ | ------------------------------- | -------------- |
| `free`       | Memory usage summary            | `free -m`      |
| `vmstat`     | Memory and swap stats           | `vmstat 1`     |
| `top`/`htop` | Live memory and swap monitoring | `top`          |
| `smem`       | Detailed memory per process     | `smem`         |
| `sar`        | Historical memory usage         | `sar -r 1 3`   |

---

### 🧵 **Process and Load Monitoring**

| Tool         | Description                        | Sample Command        |
| ------------ | ---------------------------------- | --------------------- |
| `top`/`htop` | View processes consuming resources | `htop`                |
| `ps`         | Snapshot of running processes      | `ps aux --sort=-%cpu` |
| `uptime`     | Load average overview              | `uptime`              |
| `w`          | Users and what they’re doing       | `w`                   |

---

### 📶 **Disk and I/O Monitoring**

| Tool       | Description                  | Sample Command      |
| ---------- | ---------------------------- | ------------------- |
| `iostat`   | I/O stats by device and CPU  | `iostat -xz 1`      |
| `iotop`    | Top-like tool for I/O        | `sudo iotop`        |
| `df`       | Disk usage per mount point   | `df -h`             |
| `du`       | Disk usage per directory     | `du -sh /var/*`     |
| `lsblk`    | Block devices and mount info | `lsblk`             |
| `blktrace` | Low-level I/O tracing        | `blktrace /dev/sda` |

---

### 🌐 **Network Monitoring**

| Tool              | Description                                 | Sample Command            |
| ----------------- | ------------------------------------------- | ------------------------- |
| `ifconfig` / `ip` | View IP, interface status                   | `ip a`                    |
| `ss`              | Socket statistics (replacement for netstat) | `ss -tulnp`               |
| `netstat`         | Old-school connections & ports              | `netstat -tulnp`          |
| `iftop`           | Real-time bandwidth per connection          | `sudo iftop -i eth0`      |
| `nload`           | Graphical view of incoming/outgoing traffic | `nload`                   |
| `bmon`            | Bandwidth monitor with graph                | `bmon`                    |
| `vnstat`          | Historical traffic monitoring               | `vnstat`                  |
| `tcpdump`         | Packet capture                              | `tcpdump -i eth0 port 80` |

---

### 📈 **System-Wide and Visual Dashboards**

| Tool       | Description                                 | Sample Command |
| ---------- | ------------------------------------------- | -------------- |
| `glances`  | Cross-resource real-time monitoring         | `glances`      |
| `dstat`    | Versatile for disk, net, CPU, memory        | `dstat`        |
| `nmon`     | Full system performance capture             | `nmon`         |
| `atop`     | Advanced top with disk/network/process info | `atop`         |
| `collectl` | Lightweight performance collection          | `collectl`     |
| `perf`     | Profiling & performance counters            | `perf top`     |

---

### 📦 **Logging & Visualization Tools**

| Tool              | Description                               |
| ----------------- | ----------------------------------------- |
| **Prometheus**    | Metrics collection and alerting           |
| **Grafana**       | Dashboards and visualization              |
| **Netdata**       | Real-time web-based performance dashboard |
| **Nagios/Zabbix** | Traditional monitoring systems            |
| **ELK Stack**     | Logging and search with Kibana dashboards |

---

