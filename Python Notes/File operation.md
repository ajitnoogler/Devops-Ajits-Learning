

✅ Common File Operations for Logs in Python

| Operation                | Python Code / Function                 | Use Case                       |
| ------------------------ | -------------------------------------- | ------------------------------ |
| **Open a file**          | `open("logfile.log", "r")`             | To read logs                   |
| **Read file**            | `.read()`, `.readlines()`              | Read full file or line-by-line |
| **Write to file**        | `open("logfile.log", "w")`, `.write()` | Write new logs                 |
| **Append to file**       | `open("logfile.log", "a")`             | Add new log entries            |
| **Check if file exists** | `os.path.exists()`                     | Avoid file errors              |
| **File size check**      | `os.path.getsize()`                    | For log rotation               |
| **Loop through logs**    | `for line in open():`                  | Process line-by-line           |
| **Pattern match**        | `re.search()`                          | Filter logs with regex         |
| **Timestamp match**      | `datetime.strptime()`                  | Filter logs by date/time       |
| **Compress logs**        | `gzip`, `shutil.make_archive()`        | Log rotation and archival      |
| **Move/copy logs**       | `shutil.move()`, `shutil.copy()`       | Archiving or backup            |
| **Delete old logs**      | `os.remove()`                          | Clean-up automation            |

# 🔧 Example: Read and Filter Error Logs
import re

with open("/var/log/syslog", "r") as file:
    for line in file:
        if "ERROR" in line or re.search(r"\b(fail|critical)\b", line, re.IGNORECASE):
            print(line.strip())

# 🔁 Example: Rotate Log Based on Size
import os
import shutil

log_file = "app.log"
max_size = 5 * 1024 * 1024  # 5MB

if os.path.exists(log_file) and os.path.getsize(log_file) > max_size:
    shutil.move(log_file, f"{log_file}.backup")
    open(log_file, "w").close()  # Create fresh empty log


