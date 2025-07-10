
### Troubleshooting performance issues on Oracle Linux but:

❌ Cannot use top

❌ Cannot use free

❌ Cannot install any new packages (yum, dnf, etc.)

You’ll need to rely on built-in tools and /proc files, which are always available on any standard Linux system including Oracle Linux.

### 🧰 Minimal Toolset for Performance Troubleshooting (No top, free, or installs)

---

### 🧠 1. **Check Memory Usage (Without `free`)**

#### ✅ `/proc/meminfo`

```bash
cat /proc/meminfo | egrep 'MemTotal|MemFree|Buffers|Cached|SwapTotal|SwapFree'
cat /proc/meminfo | egrep 'MemTotal|MemFree|Buffers|Cached|SwapTotal|SwapFree' | awk '{printf "%s %10.2f MB\n", $1, $2/1024}'
```

Look for:

* `MemFree` very low (but check `Buffers` and `Cached` too — they're reclaimable)
* `SwapFree` very low = swap pressure = memory issue

#### ✅ ps 

Check memory usage for a specific process:

```bash
ps -eo pid,comm,%mem --sort=-%mem | grep your_process_name | head -1
```

---

### 🔥 2. **Check CPU Usage**

#### ✅ `/proc/stat`

```bash
head -n 5 /proc/stat
```

* First line shows total CPU time in different modes.
* You can write a quick script to calculate %CPU usage over time (let me know if needed).

#### ✅ `ps` built-in sorting

```bash
ps -eo pid,ppid,user,cmd,%cpu,%mem --sort=-%cpu | head
```

* Lists high CPU-consuming processes.

---

### 💽 3. **Check Disk I/O and Wait**

#### ✅ `/proc/diskstats`

```bash
cat /proc/diskstats | grep -i 'sd\|vd'
```

#### ✅ `ps` for I/O Wait

Check processes in uninterruptible sleep (`D` state = likely I/O wait):

```bash
ps -eo pid,stat,cmd | grep '^.\{6\}D'
```

---

### 🌐 4. **Check Network Issues**

#### ✅ `/proc/net/dev`

```bash
cat /proc/net/dev
```

* Shows RX/TX per interface. Look for packet drops or errors.

#### ✅ `ss` (Socket Statistics, built-in)

```bash
ss -s
ss -tuna
```

* Active TCP/UDP sockets, listening ports.

---

### 📈 5. **System Load and Pressure**

#### ✅ `uptime`

```bash
uptime
```

* Shows 1, 5, 15 minute load averages.
* Load > CPU core count = possible CPU/memory bottleneck.

#### ✅ `/proc/loadavg`

```bash
cat /proc/loadavg
```

---

### 📝 6. **Logs and Kernel Messages**

#### ✅ `dmesg`

```bash
dmesg | tail -n 30
```

* Look for `oom-killer`, disk errors, network drops.

#### ✅ `journalctl` (if systemd is present)

```bash
journalctl -xe | tail
```

---

### 🔍 7. **Process Tree & Zombie Check**

#### ✅ Show full process hierarchy

```bash
ps -eo pid,ppid,cmd --forest
```

#### ✅ Zombie processes

```bash
ps -eo stat,cmd | grep '^Z'
```

---

## 📌 Summary Table

| Area      | Command                                      | What It Shows                    |
| --------- | -------------------------------------------- | -------------------------------- |
| CPU       | `cat /proc/stat`, `ps -eo %cpu`              | CPU usage                        |
| Memory    | `cat /proc/meminfo`, `ps -eo %mem`           | RAM usage                        |
| Disk      | `cat /proc/diskstats`, `ps -eo stat`         | Disk I/O, D state                |
| Network   | `ss -s`, `cat /proc/net/dev`                 | Network throughput, open sockets |
| Load Avg  | `uptime`, `cat /proc/loadavg`                | Load trend                       |
| Logs      | `dmesg`, `journalctl -xe`                    | Kernel and system logs           |
| Processes | `ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu` | High resource processes          |

---

## ✅ Example Output Interpretation

```bash
cat /proc/meminfo | egrep 'MemTotal|MemFree|Buffers|Cached'
MemTotal:       16391424 kB
MemFree:         1234567 kB
Buffers:          234567 kB
Cached:          4567890 kB
```

👉 High `Cached` + `Buffers` is good — not a memory leak.

```bash
ps -eo pid,stat,cmd | grep '^.\{6\}D'
```

👉 If many processes are in `D` state = likely I/O wait.

```bash
cat /proc/loadavg
0.85 0.70 0.90 2/150 12345
```

👉 Load average < CPU core count = likely OK.


