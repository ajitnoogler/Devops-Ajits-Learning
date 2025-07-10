
## Process & System Monitoring

| Command         | Description                   | Common Switches                               |
| --------------- | ----------------------------- | --------------------------------------------- |
| `ps`            | Snapshot of current processes | `-aux`, `-ef`                                 |
| `top`/`htop`    | Live resource monitoring      | *(interactive: sort columns, kill processes)* |
| `kill`          | Send signal to process        | `-9` (SIGKILL), `-15` (SIGTERM)               |
| `nice`/`renice` | Adjust process priority       | `-n` (priority level), `-p` (pid)             |
| `df`            | Disk filesystem usage         | `-h` (human‑readable), `-T` (fs type)         |
| `du`            | Directory space usage         | `-h` (human‑readable), `-s` (summary)         |
| `free`          | Memory usage                  | `-h` (human‑readable), `-m` (MB), `-g` (GB)   |
| `vmstat`        | System performance stats      | `interval [count]`                            |
| `iostat`        | I/O statistics                | `-x` (extended), `interval [count]`           |

---

