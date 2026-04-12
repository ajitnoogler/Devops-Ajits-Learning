
```markdown
# Linux & Cloud – Linux Interview Q&A

## Linux Basics (Beginner Level)

### 1. What is Linux and how is it different from Unix?

Linux is a free, open‑source, Unix‑like operating system kernel developed by Linus Torvalds. It powers many distributions (such as Ubuntu, RHEL, CentOS, Debian) that include the kernel plus userland tools and package management.

Unix is an older operating system family created at AT&T Bell Labs. Traditional Unix systems were mostly proprietary and ran on specific hardware platforms, while Linux runs on a huge range of hardware and is community‑developed.

### 2. What is the difference between Linux and Windows?

Linux is open‑source and follows a Unix‑like design, with everything represented as files under a single root (`/`). It typically uses file systems like ext4 or XFS and is heavily oriented around the command line.

Windows is proprietary, uses NTFS by default, presents disks as drive letters (`C:`, `D:`), and focuses more on a GUI‑driven administration model, even though it also provides PowerShell and CMD.

### 3. What is the Linux file system hierarchy?

Linux follows the Filesystem Hierarchy Standard. Everything starts from the root directory `/`.

Important directories include:

- `/bin` – essential binaries
- `/sbin` – system binaries
- `/etc` – system configuration
- `/var` – variable data such as logs and spool
- `/home` – user home directories
- `/boot` – bootloader and kernel files
- `/dev` – device files
- `/tmp` – temporary files

### 4. What is a shell? What are some common types of shells?

A shell is a command‑line interpreter that accepts commands from the user, executes them, and displays output. It is the main interface between the user and the operating system in a text environment.

Common shells include `sh` (Bourne shell), `bash` (Bourne Again Shell), `zsh`, `ksh` (Korn shell), and `fish`. On most Linux distributions, `bash` is the default user shell.

### 5. What are runlevels in Linux?

In traditional SysV init, a runlevel represents a particular operating state of the system, such as single‑user mode, multi‑user mode without GUI, or multi‑user mode with GUI.

Typical runlevels:

- `0` – halt
- `1` – single‑user
- `3` – multi‑user, text
- `5` – multi‑user, graphical
- `6` – reboot

On modern systems that use `systemd`, runlevels are mapped to `systemd` targets like `multi-user.target` and `graphical.target`, but the concept of system states and which services are active is similar.

### 6. How do you check the current working directory?

Use the `pwd` command:

```bash
pwd
```

It prints the full path of the directory you are currently in, for example `/home/username/projects`.

### 7. How do you view hidden files?

Hidden files in Linux start with a dot (`.`). To list them, use `ls` with the `-a` option:

```bash
ls -a
```

To see detailed information including permissions and ownership:

```bash
ls -la
```

### 8. What is the difference between `>` and `>>`?

Both operators redirect command output to a file.

- `>` overwrites the file if it exists (or creates it if it does not).
- `>>` appends the output to the end of the file, preserving existing content.

### 9. How do you search for a string in a file?

Use the `grep` command. For example:

```bash
grep "pattern" file.txt
grep -n "pattern" file.txt      # show line numbers
grep -r "pattern" /path/dir     # search recursively in a directory
```

### 10. How do you check memory usage?

Common ways:

```bash
free -h           # summary of RAM and swap
top               # live per‑process memory usage
htop              # nicer interactive view (if installed)
```

These tools show total, used, and free memory, plus which processes are consuming the most.

### 11. What command shows disk usage per directory?

Use the `du` command for directory‑level usage:

```bash
du -sh /path/*    # summary per item under /path
du -sh .          # total for the current directory
```

Use `df -h` when you want filesystem‑level space usage.

### 12. How do you find a file by name?

Use `find` or `locate`. Examples:

```bash
find /path -name "filename.txt" -type f
find / -iname "*.log" 2>/dev/null
```

Faster, index‑based search:

```bash
locate filename
```

### 13. What is cron and how do you schedule a job?

`cron` is a time‑based job scheduler in Unix‑like systems. It runs commands at specified times and intervals.

Edit the crontab with:

```bash
crontab -e
```

Add a line like:

```bash
0 2 * * * /usr/local/bin/backup.sh
```

This runs `backup.sh` every day at 02:00.

### 14. What is the use of `top`, `ps`, and `kill` commands?

- `top`: Interactive, real‑time view of processes, CPU, memory, and load.
- `ps`: Snapshot of current processes (for example, `ps aux`) with details such as PID, CPU, and memory usage.
- `kill`: Sends signals to processes by PID (for example, `kill PID` for SIGTERM, or `kill -9 PID` for SIGKILL).

---

## Intermediate Linux Interview Questions

### 15. How do you check which process is using the most CPU/memory?

Use `top` or `htop` and look at the `%CPU` and `%MEM` columns to see the heaviest processes.

You can also use:

```bash
ps aux --sort=-%cpu | head
ps aux --sort=-%mem | head
```

### 16. What’s the difference between `nice` and `renice`?

`nice` starts a new process with a specified scheduling priority (niceness value), where a higher nice value means lower priority:

```bash
nice -n 10 command
```

`renice` changes the niceness of an already running process:

```bash
renice 5 -p 1234
```

### 17. What’s the difference between `kill`, `pkill`, and `killall`?

- `kill`: Sends a signal to a specific process ID (PID), e.g. `kill -TERM 1234`.
- `pkill`: Sends a signal to processes that match a pattern, e.g. `pkill nginx`.
- `killall`: Sends a signal to all processes with the exact given name, e.g. `killall httpd`.

### 18. How do you analyze and troubleshoot a system that is running slowly?

- Check CPU, memory, and load using `top`, `htop`, `vmstat`, and `uptime`.
- Check disk and I/O with `iostat`, `iotop`, and `df -h`.
- Check network usage with `ss`, `netstat`, `iftop`, or `nload`.
- Review logs in `/var/log` and with `journalctl` and `dmesg`.

### 19. How do you check logs for a failed service?

On a `systemd`‑based system:

```bash
systemctl status service_name
journalctl -u service_name -xe
```

### 20. What is the use of `netstat`, `ss`, and `lsof`?

- `netstat`: Shows network connections, routing tables, and listening ports.
- `ss`: Newer, faster tool to inspect sockets and listening ports.
- `lsof`: Lists open files, including sockets (e.g. `lsof -i :80`).

### 21. How do you check if a port is open and listening?

```bash
ss -tulpn | grep :PORT
netstat -tulpn | grep :PORT
```

Client‑side checks:

```bash
telnet host PORT
nc -vz host PORT
```

### 22. Difference between `scp` and `rsync`?

- `scp`: Simple, full file copy over SSH.
- `rsync`: Incremental, resumable sync over SSH with compression and many options.

### 23. How do you configure a static IP address?

- Older systems: edit `/etc/sysconfig/network-scripts/ifcfg-eth0` (RHEL) or `/etc/network/interfaces` (Debian) and restart networking.
- Modern systems: use netplan (`/etc/netplan/*.yaml` + `netplan apply`) or NetworkManager (`nmcli`, `nmtui`).

### 24. How do you flush DNS cache?

Examples:

```bash
# systemd-resolved
sudo systemd-resolve --flush-caches

# BIND
sudo rndc flush

# nscd
sudo systemctl restart nscd
```

### 25. How do hard links differ from soft links?

- Hard link: another name pointing to the same inode; deleting one name does not remove data as long as another hard link exists.
- Soft link (symlink): a file containing a path to the target; can cross filesystems, breaks if the target is removed.

### 26. How do you mount and unmount file systems?

```bash
sudo mount /dev/sdX1 /mnt
sudo umount /mnt
```

Persistent mounts go into `/etc/fstab`.

---

## Advanced Linux Interview Questions

### 27. What happens during the Linux boot process (BIOS → GRUB → init → systemd)?

1. BIOS/UEFI performs POST and finds a boot device.
2. Bootloader (GRUB) is loaded and started.
3. GRUB loads the Linux kernel + `initrd`/`initramfs`.
4. Kernel initializes hardware, memory, and mounts the initial root.
5. Kernel mounts the real root filesystem and starts PID 1 (`systemd`).
6. `systemd` starts services/targets and brings the system to login.

### 28. What is initrd or initramfs?

An initial root filesystem in RAM that contains tools, drivers, and scripts to:

- Detect hardware
- Assemble RAID/LVM
- Decrypt disks
- Mount the real root filesystem

After that, control goes to the normal init system.

### 29. What are cgroups and namespaces? How do they work?

- **cgroups**: limit, prioritize, and account for CPU, memory, I/O, etc. per group of processes.
- **namespaces**: isolate views of global resources (PIDs, mounts, network, IPC, hostname, users).

Together they provide isolation and resource control for containers (e.g. Docker).

### 30. How does Linux handle process scheduling?

- Uses **CFS (Completely Fair Scheduler)** for normal processes.
- Tracks each process’s virtual runtime.
- Picks the task that has run the least (smallest virtual runtime).
- Uses a red‑black tree per CPU.
- Real‑time classes (`SCHED_FIFO`, `SCHED_RR`) exist for time‑critical tasks.

---

## Security & Access

### 31. What is SELinux/AppArmor? How do you troubleshoot permission issues related to them?

- SELinux: label‑based MAC, common on RHEL/Fedora.
- AppArmor: path‑based MAC, common on Ubuntu/SUSE.

Troubleshooting:

- Check audit logs (`ausearch`, `sealert`) or `journalctl`, `dmesg`.
- Adjust policy/profile or switch to permissive/complain mode while testing.

### 32. How do you securely copy files between Linux systems?

```bash
# scp
scp file user@host:/path

# rsync over SSH
rsync -avz -e ssh src/ user@host:/dest/
```

### 33. How do you set up SSH key-based authentication?

```bash
ssh-keygen -t ed25519          # on client
ssh-copy-id user@server        # or append to ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

Optionally disable password auth in `sshd_config`.

---

## Performance & Tuning

### 34. How do you identify and resolve a memory leak?

1. Detect with `free -h`, `top`, `htop`, `vmstat`.
2. Identify the growing process.
3. Inspect with `pmap`, `smem`, `ps_mem.py`, or profilers (`valgrind`, etc.).
4. Mitigate: restart service, add limits (cgroups, `systemd`), and fix application code.

### 35. What tools would you use for profiling a system under heavy load?

- High‑level: `top`, `htop`, `atop`, `dstat`
- CPU/syscalls: `perf`, `pidstat`, `oprofile`, `strace`
- Disk/I/O: `iostat`, `iotop`, `vmstat`, `sar`

### 36. How do you analyze I/O wait using tools like `iostat`, `vmstat`, or `iotop`?

```bash
iostat -x      # await, %util per device
vmstat 1       # wa column = I/O wait
iotop          # per‑process read/write
```

High `%util` and `await` + high `wa` indicate I/O bottlenecks.

### 37. What are kernel modules? How do you manage them?

- Code units (drivers, filesystems) that can be loaded/unloaded at runtime.

Commands:

```bash
lsmod          # list modules
modinfo MOD    # info
sudo modprobe MOD      # load
sudo modprobe -r MOD   # remove
```

### 38. How do you tune kernel parameters with `sysctl`?

```bash
sysctl vm.swappiness
sudo sysctl -w vm.swappiness=10
```

Persistent:

```bash
# /etc/sysctl.conf or /etc/sysctl.d/*.conf
sudo sysctl -p
```

---

## Bonus: Real-World Scenario-Based Questions

### 39. A process is stuck in uninterruptible sleep (D state). How do you investigate it?

- Check with `top` or:

  ```bash
  ps -o pid,stat,cmd
  ```

- Look at `/proc/<pid>/stack` and `/proc/<pid>/io`.
- Use `strace -p <pid>` if possible.
- Check `dmesg`/`journalctl` for disk/NFS/storage errors.

Often caused by hung disks or network filesystems; fix the underlying I/O issue or reboot if necessary.

### 40. A cron job isn’t running. What steps would you take to debug it?

- `crontab -l` or check `/etc/crontab`, `/etc/cron.d`.
- Ensure cron daemon is running: `systemctl status cron` or `crond`.
- Log output/errors from the job to a file.
- Check `/var/log/cron`, `/var/log/syslog`, or `journalctl -u cron`.
- Verify PATH, permissions, executable bit on scripts.

### 41. A service fails to start after a reboot. How do you trace the problem?

```bash
systemctl status service_name
journalctl -u service_name -xe
```

```
