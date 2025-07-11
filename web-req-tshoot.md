

#### 🧪 Sequential Troubleshooting of Web App slowness Performance (Based on Linux Resource Activation)

Follow this sequence to identify performance bottlenecks using the **actual resource activation order** during an HTTP request.

---

#### 🧭 Step-by-Step Resource-Aware Troubleshooting Guide

| ⏱️ Order | 🔍 Resource Area | ✅ What to Check | 🛠️ Tools/Commands |
|----------|------------------|------------------|-------------------|
| 1️⃣ | 🌐 **Network Ingress** | - Packet loss, latency, dropped connections<br> - NIC errors or interface overload | `ping`, `mtr`, `iftop`, `ip -s link`, `ethtool -S eth0` |
| 2️⃣ | 🖥️ **CPU (Initial Interrupts)** | - High interrupt or softirq usage<br> - Context switch storm<br> - Uneven CPU load | `top`, `htop`, `vmstat 1`, `mpstat -P ALL`, `sar -I ALL 1` |
| 3️⃣ | 💾 **Memory Allocation** | - High memory usage or swapping<br> - Kernel buffer exhaustion<br> - OOM kills | `free -m`, `vmstat -s`, `dmesg | grep -i oom`, `slabtop`, `smem` |
| 4️⃣ | 💽 **Disk I/O (optional)** | - Slow file/database access<br> - Disk wait time (`iowait`) high<br> - Log bottlenecks | `iotop`, `iostat -xz 1`, `dstat -dny`, `df -h`, `du -sh *` |
| 5️⃣ | 💾 **Memory (Response Building)** | - Application memory leaks<br> - Slow JSON or template rendering<br> - GC pauses (Java/Python) | App profiler, `ps -o pid,%mem,cmd -p <pid>`, custom logging |
| 6️⃣ | 🌐 **Network Egress** | - Slow response delivery<br> - Socket errors or TCP retransmits<br> - MTU mismatch or drops | `ss -s`, `netstat -s`, `tcpdump`, `iftop`, `ip route get` |
| 7️⃣ | 🖥️ **CPU (Final Cleanup)** | - CPU saturation due to many threads or blocking calls | `pidstat -wt`, `strace -T -p <pid>`, `perf top` |

---

#### 🛡️ General Troubleshooting Best Practices

- 📌 **Replicate the issue** using tools like `ab`, `wrk`, or `curl`.
- 📈 **Monitor over time** (not just once): use `sar`, `collectl`, or `dstat`.
- 📋 **Log analysis**: Check `/var/log/syslog`, Nginx/Apache logs, and app logs for clues.
- 🧠 **Compare healthy vs unhealthy state**: snapshot top/ps/vmstat before and after issue.

---

#### 🚦 Quick Health Check Command Set

```bash
#### Network Health
ping -c 10 8.8.8.8
mtr -rwzbc100 google.com
ss -s
ip -s link

#### CPU & Load
top -n 1
vmstat 1 5
mpstat -P ALL 1 3

#### Memory
free -m
dmesg | grep -i oom
slabtop

#### Disk I/O
iotop -aoP
iostat -xz 1
df -hT

#### Application Process
ps -eo pid,ppid,%cpu,%mem,cmd --sort=-%cpu | head
strace -T -p <pid>

```
---

### Always follow the resource sequence: 

🌐 Network → 🖥️ CPU → 💾 Memory → 💽 Disk → 💾 Memory → 🌐 Network → 🖥️ CPU — and eliminate the bottlenecks one by one.
