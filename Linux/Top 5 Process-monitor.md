
# ✅ Top 5 CPU & Memory -Consuming Processes

(.venv) @ajitnoogler ➜ ~ $  ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%mem | head -n 6

    PID    PPID CMD                         %CPU %MEM
    590     569 /vscode/bin/linux-x64/2901c 58.0 14.4
   2136     590 /vscode/bin/linux-x64/2901c 54.9  2.7
    569     560 /vscode/bin/linux-x64/2901c 10.7  2.3
   1011     569 /vscode/bin/linux-x64/2901c  1.8  0.8
     57       1 dockerd --dns 168.63.129.16  0.6  0.8



(.venv) @ajitnoogler ➜ ~ $ ps aux | awk 'NR>1 {print $0 | "sort -k4 -nr"}' | head -n 5

codespa+     590 24.7 12.2 65851412 999512 ?     Sl   09:01   0:21 /vscode/bin/linux-x64/2901c5ac6db8a986a5666c3af51ff804d05af0d4/node --dns-result-order=ipv4first /vscode/bin/linux-x64/2901c5ac6db8a986a5666c3af51ff804d05af0d4/out/bootstrap-fork --type=extensionHost --transformURIs --useHostProxy=false
codespa+    2136  9.1  5.3 12997932 433772 ?     Sl   09:01   0:05 /vscode/bin/linux-x64/2901c5ac6db8a986a5666c3af51ff804d05af0d4/node /home/codespace/.vscode-remote/extensions/ms-python.vscode-pylance-2025.6.2/dist/server.bundle.js --cancellationReceive=file:242b90db177092fa4a1c15f7dda0350c05977db877 --node-ipc --clientProcessId=590
codespa+     569  3.7  1.4 11833164 114016 ?     Sl   09:01   0:03 /vscode/bin/linux-x64/2901c5ac6db8a986a5666c3af51ff804d05af0d4/node /vscode/bin/linux-x64/2901c5ac6db8a986a5666c3af51ff804d05af0d4/out/server-main.js --log trace --force-disable-user-env --server-data-dir /home/codespace/.vscode-remote --accept-server-license-terms --host 127.0.0.1 --port 0 --connection-token-file /home/codespace/.vscode-remote/data/Machine/.connection-token-2901c5ac6db8a986a5666c3af51ff804d05af0d4 --extensions-download-dir /home/codespace/.vscode-remote/extensionsCache --start-server  --enable-remote-auto-shutdown --skip-requirements-check
codespa+     603  8.4  1.1 1261952 93508 ?       Sl   09:01   0:07 /vscode/bin/linux-x64/2901c5ac6db8a986a5666c3af51ff804d05af0d4/node /vscode/bin/linux-x64/2901c5ac6db8a986a5666c3af51ff804d05af0d4/out/bootstrap-fork --type=fileWatcher
root          57  0.2  0.8 1966712 69888 ?       Sl   09:01   0:00 dockerd --dns 168.63.129.16



more commands like below
ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%mem | head -n 6 


# ✅ Find All Running Java Processes
ps aux | grep java | grep -v grep | awk '{print $4, $2, $11}' | sort -k1 -nr

# ✅ Find All Zombie Processes
ps aux | awk '$8=="Z" {print $2, $11}'
Here, $8=="Z" → Zombie state in the STAT column

# ✅  Show Top 10 Processes by Threads
ps -eo pid,ppid,cmd,nlwp --sort=-nlwp | head -n 11
Here, nlwp = Number of threads

# ✅ Monitor Processes Using a Specific Port (e.g., 443)
lsof -i :443  or  netstat -tunlp | grep :443

# ✅ Find All Processes by a Specific User
ps -u username -o pid,cmd,%cpu,%mem --sort=-%cpu

# ✅ Monitor a Process in Real-Time Every 2 Seconds
watch -n 2 'ps -eo pid,cmd,%cpu,%mem --sort=-%cpu | head -n 6'

# ✅ Find All Stopped or Sleeping Processes
ps aux | awk '$8 ~ /S|T/ {print $1, $2, $8, $11}'
S = sleeping, T = stopped

# ✅ Count Running Instances of a Process
ps aux | grep -v grep | grep nginx | wc -l

# ✅ Total CPU & MEM Used by a Specific App
ps aux | grep nginx | grep -v grep | awk '{cpu+=$3; mem+=$4} END {print "CPU:", cpu, "MEM:", mem}'

# ✅ Identify High CPU Usage for More Than 1 Minute
ps -eo pid,etime,cmd,%cpu --sort=-%cpu | awk '$2 ~ /[0-9]+:[0-9][0-9]/ {print}'
Here, Filters processes running for more than 1 minute.

# ✅ List All User Names With Running Processes
ps -eo user= | sort | uniq

# ✅ Top Processes by Virtual Memory (VSZ)
ps -eo pid,cmd,vsz --sort=-vsz | head -n 6

# ✅ Show Parent-Child Process Tree
ps -ejH or pstree -p

# ✅ Show Processes That Exceed 500MB RAM
ps -eo pid,cmd,rss --sort=-rss | awk '$3 > 512000'
Here, rss is in KB; 512000 KB = 500 MB

# ✅ Kill Processes Consuming Too Much CPU
ps -eo pid,%cpu --sort=-%cpu | awk '$2>80 {print $1}' | xargs -r kill -9

# ✅ Show Only Running (R) Processes
ps aux | awk '$8=="R" {print $2, $11}'

# 🔧 Bonus Tip: Save to File for Logging
ps -eo pid,cmd,%cpu,%mem --sort=-%cpu | head -n 6 >> /var/log/proc_top.log

