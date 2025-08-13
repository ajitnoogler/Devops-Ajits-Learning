#### Performance Debugging on Linux

| 🧩 Category                 | 🔍 Command / Tool               | 💬 Description                                                                                                           |
|----------------------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| 🖥️ CPU Debugging           | `w`                             | Shows who is logged in and system load averages for 1, 5, and 15 minutes.                                                 |
| 🔍 Memory Debugging        | `free -m`                       | Displays used/free physical memory and buffers in MB.                                                                    |
| 🔍 Network Debugging       | `ifconfig`                      | Displays network interface details: RX/TX packets, errors, dropped packets. (Deprecated in favor of `ip` command.)       |
| 🔍 I/O or Disk Debugging   | `top`                           | Real-time view of processes; `wa` column shows CPU wait time for I/O.                                                     |
| 🔑 Limitation              | N/A                             | These commands show stats but don't pinpoint the exact process causing high usage.                                        |
| 🔍 CPU Debugging (Advanced)| `top` (press `1`)               | Breaks down CPU usage per individual CPU core in real-time.                                                               |
| 🔍 Memory Debugging (Adv.) | `top` (press `SHIFT+m`)         | Sorts processes by memory usage.                                                                                          |
| 🔍 Network Debugging (Adv.)| `dstat --net --top-io-adv`      | Shows network stats and most expensive I/O process. Requires separate installation.                                       |
| 🔍 I/O Debugging (Advanced)| `sudo iotop`                    | Shows I/O usage per process. Not preinstalled; requires root and separate installation.                                   |

---

Load Average is a metric that shows how busy your system's CPU(s) are. It reflects the average number of processes that are either:

   - Running

   - Waiting for CPU time
``` bash

$ w
 16:45:03 up 3 days,  5:01,  2 users,  load average: 0.75, 1.20, 0.90
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
ajit     pts/0    192.168.0.10     10:12    1.00s  0.10s  0.10s top
root     pts/1    192.168.0.20     09:45   10.00s  0.01s  0.01s bash

---

load average: 0.75, 1.20, 0.90
                ↑     ↑     ↑
            1 min  5 min  15 min

===============================================================================

$ uptime
 16:45:03 up 3 days,  5:01,  2 users,  load average: 20.15, 19.87, 18.45  <=== // High load average example

load average: 20.15, 19.87, 18.45 <=== // High load average example
                ↑     ↑     ↑
            1 min  5 min  15 min

✅ Interpreted as:

    20.15 processes waiting/running in the last 1 minute

    19.87 in the last 5 minutes

    18.45 in the last 15 minutes

👉 If the system only has 4 CPU cores, this is 5× overload!


```


==================================================

If your system has 4 cores:

    A load average of 4.00 means fully utilized
    A load average of 2.00 means 50% usage
    A load average of 6.00 means overloaded (some processes are waiting)

=========================================================================

🚦 Quick judgment guide:

| Load Avg (1m) | CPU Cores                                | Interpretation |
| ------------- | ---------------------------------------- | -------------- |
| ≤ CPU cores   | Balanced/Healthy load                    |                |
| > CPU cores   | Overloaded (processes waiting)           |                |
| >> CPU cores  | Heavily overloaded, potential bottleneck |much greater than|
| ≈ 0.00        | Very idle (may be underutilized)         |                |

---

#### 🖥️ CPU Debugging
The 'w' command presents a snapshot of the system's operations, offering load averages for 1, 5, and 15-minute periods:
$ w

#### 🔍 Memory Debugging
The 'free' command offers a clear picture of used and free physical memory y spaces, also shedding light on buffers utilized by the kernel. The '-m' flag provides the information in MB:
$ free -m

#### 🔍 Network Debugging
The 'ifconfig' command is an integral tool to display or configure a network interface, providing information about received and transmitted packets, errors, and dropped packets:
$ ifconfig

#### 💡 Note that many distributions no longer include the ifconfig command or net-tools package pre-installed. The 'ip' command is now favored over 'ifconfig', due to its extensive functionality and active maintenance.

#### 🔍 I/O or Disk Debugging
The 'top' command in Unix-like systems proffers a real-time, dynamic view of system processes. The 'wa' column is especially valuable for diagnosing performance issues as it displays the amount of time the CPU remains idle while awaiting I/O operations:
top

#### 🔑 Key limitation - these commands provide usage stats but don't specifically point out the process causing an issue. For example, the 'w' command portrays CPU utilization over time, but it doesn't identify the process responsible for high CPU usage.

#### 🔍 CPU Debugging with Tools
'top' command is a powerful command-line utility offering a real-time dynamic view of system processes. Pressing '1' will break down CPU usage per individual CPU:
top

#### 🔍 Memory Debugging with Tools
Typing SHIFT+m while running 'top', you can sort processes based on memory utilization:
top (then SHIFT+m)

#### 🔍 Network Debugging with Tools
'dstat' offers a versatile tool for monitoring systems during performance tuning tests or troubleshooting. The '--net' and '--top-io-adv' flags can monitor network stats and show the most expensive I/O process. Note that it requires separate installation:
$ dstat --net --top-io-adv

#### 🔍 I/O Debugging with Tools
The 'iotop' command monitors I/O usage information and presents a table of existing I/O utilization per process. However, it's not typically preinstalled and requires separate installation:

$ sudo iotop 
