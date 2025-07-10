## Networking & Connectivity

| Command                  | Description                   | Common Switches                                          |
| ------------------------ | ----------------------------- | -------------------------------------------------------- |
| `ssh`                    | Secure shell login            | `-i` (identity file), `-p` (port), `-o` (options)        |
| `scp`                    | Secure copy over SSH          | `-r` (recursive), `-P` (port)                            |
| `rsync`                  | Remote sync                   | `-avz` (archive, verbose, compress), `--delete`          |
| `curl`                   | Transfer data with URLs       | `-X` (method), `-H` (header), `-d` (data), `-I` (head)   |
| `wget`                   | Non‑interactive download      | `-q` (quiet), `-O` (output file), `-c` (continue)        |
| `netstat`/`ss`           | Network connections & sockets | `-t` (TCP), `-u` (UDP), `-l` (listening), `-n` (numeric) |
| `ping`                   | ICMP echo                     | `-c` (count), `-i` (interval)                            |
| `traceroute`/`tracepath` | Path to host                  | `-m` (max hops), `-p` (port)                             |
| `iptables`/`nft`         | Firewall rules                | `-L` (list), `-A` (append), `-D` (delete)                |

---

