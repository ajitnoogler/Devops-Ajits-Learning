
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
$ ss -s
Total: 331
TCP:   22 (estab 10, closed 1, orphaned 0, timewait 1)

Transport Total     IP        IPv6
RAW       1         0         1        
UDP       2         2         0        
TCP       21        12        9        
INET      24        14        10       
FRAG      0         0         0

$ ss -tuna
Netid                State                    Recv-Q                 Send-Q                                      Local Address:Port                                            Peer Address:Port                 Process                
udp                  UNCONN                   0                      0                                           127.0.0.53%lo:53                                                   0.0.0.0:*                                           
udp                  UNCONN                   0                      0                                          10.0.3.67%eth0:68                                                   0.0.0.0:*                                           
tcp                  LISTEN                   0                      511                                             127.0.0.1:46737                                                0.0.0.0:*                                           
tcp                  LISTEN                   0                      4096                                            127.0.0.1:45221                                                0.0.0.0:*                                           
tcp                  LISTEN                   0                      4096                                        127.0.0.53%lo:53                                                   0.0.0.0:*                                           
tcp                  LISTEN                   0                      512                                             127.0.0.1:16635                                                0.0.0.0:*                                           
tcp                  LISTEN                   0                      512                                             127.0.0.1:16634                                                0.0.0.0:*                                           
tcp                  LISTEN                   0                      128                                               0.0.0.0:2000                                                 0.0.0.0:*                                           
tcp                  LISTEN                   0                      128                                               0.0.0.0:2222                                                 0.0.0.0:*                                           
tcp                  ESTAB                    0                      0                                               10.0.3.67:59464                                           91.189.91.43:443                                         
tcp                  TIME-WAIT                0                      0                                               10.0.3.67:46550                                           20.50.80.214:443                                         
tcp                  ESTAB                    0                      0                                               10.0.3.67:41632                                           20.209.56.33:443                                         
tcp                  ESTAB                    0                      0                                               127.0.0.1:46737                                              127.0.0.1:43526                                       
tcp                  ESTAB                    0                      0                                               127.0.0.1:46737                                              127.0.0.1:43514   
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
$ cat /proc/loadavg
0.24 0.39 0.39 1/493 7513

0.24  0.39  0.39   1/493   7513
│     │     │      │       │
│     │     │      │       └─> 5.  **Last Process ID**
│     │     │      └────────> 4.  **Processes running / total processes**
│     │     └──────────────> 3.  **15-minute load average**
│     └────────────────────> 2.  **5-minute load average**
└─────────────────────────> 1.  **1-minute load average**


💡 Interpretation:
A value of 1.00 means 1 process is using or waiting for CPU.
If you have 4 CPU cores, load of:
4.00 → Fully utilized
<4.00 → Underutilized
>4.00 → Overloaded


```

---

#### 📝 6. **Logs and Kernel Messages**

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

#### 🔍 7. **Process Tree & Zombie Check**

#### ✅ Show full process hierarchy

```bash
ps -eo pid,ppid,cmd --forest
```

#### ✅ Zombie processes

```bash
ps -eo stat,cmd | grep '^Z'
```

---

#### 📌 Summary Table

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

#### ✅ Example Output Interpretation

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


