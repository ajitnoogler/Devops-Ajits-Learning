Here’s a concise Linux command cheatsheet tailored for a DevOps/cloud expert. For each command you’ll find a brief description, the most commonly used switches, and at the end a list of real‑world sample invocations.

---

## File & Directory Management

| Command | Description                 | Common Switches                                                     |
| ------- | --------------------------- | ------------------------------------------------------------------- |
| `ls`    | List directory contents     | `-l` (long), `-a` (all), `-h` (human‑readable), `-t` (sort by time) |
| `cp`    | Copy files or directories   | `-r` (recursive), `-u` (update only), `-v` (verbose)                |
| `mv`    | Move or rename              | `-v` (verbose), `-u` (update only)                                  |
| `rm`    | Remove files or directories | `-r` (recursive), `-f` (force), `-v` (verbose)                      |
| `mkdir` | Make directories            | `-p` (parents), `-v` (verbose)                                      |
| `rmdir` | Remove empty directories    | *(no common switches)*                                              |
| `find`  | Search for files/dirs       | `-name`, `-type`, `-mtime`, `-exec … {} \;`                         |

---

# File and folder permission: chmod 764 file.log | chmod -r /var/log
read = 4   | write = 2 | execute is 1

owner - 4+2+1 ----> 7  rwx
group - 4+0+1 ----> 6  rx
others- 4+0+0 ----> 4  r