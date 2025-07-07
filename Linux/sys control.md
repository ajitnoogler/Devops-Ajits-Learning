
## System Control & Services

| Command       | Description                | Common Switches                                           |
| ------------- | -------------------------- | --------------------------------------------------------- |
| `systemctl`   | Control systemd units      | `start`, `stop`, `restart`, `status`, `enable`, `disable` |
| `service`     | Init script control (SysV) | `start`, `stop`, `restart`, `status`                      |
| `journalctl`  | View systemd logs          | `-u` (unit), `-f` (follow), `--since`, `--until`          |
| `crontab`     | Schedule cron jobs         | `-e` (edit), `-l` (list), `-r` (remove)                   |
| `timedatectl` | Query & change system time | `set-time`, `set-timezone`, `status`                      |

---

