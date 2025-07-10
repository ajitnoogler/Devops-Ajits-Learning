

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

### 🔧 Example: Read and Filter Error Logs

## 🔍 Parse `/var/log/syslog` for Error Patterns

This Python script scans the syslog for lines containing `"ERROR"`, `"fail"`, or `"critical"` (case-insensitive).

```python
import re

with open("/var/log/syslog", "r") as file:
    for line in file:
        if "ERROR" in line or re.search(r"\b(fail|critical)\b", line, re.IGNORECASE):
            print(line.strip())

```python code explained:
import re  # Import the 're' module for regular expression support

# Open the syslog file in read mode
with open("/var/log/syslog", "r") as file:  # 'with' ensures the file is closed automatically
    for line in file:  # Loop through each line in the log file
        # Check if the line contains "ERROR" OR matches the regex pattern for "fail" or "critical"
        if "ERROR" in line or re.search(r"\b(fail|critical)\b", line, re.IGNORECASE):
            print(line.strip())  # Print the matched line after stripping extra whitespace/newline
```
```

---

✅ **Use Case**:  
Helpful for basic log parsing or integrating into monitoring scripts.

            

###  🔁 Example: Rotate Log Based on Size
### 📄 Log Rotation Script (Python)

Automatically rotate `app.log` if it exceeds **5 MB**.

```python
import os
import shutil

log_file = "app.log"
max_size = 5 * 1024 * 1024  # 5MB

# Check if log exists and exceeds size
if os.path.exists(log_file) and os.path.getsize(log_file) > max_size:
    shutil.move(log_file, f"{log_file}.backup")  # Archive the old log
    open(log_file, "w").close()  # Create a fresh empty log file
```

---

✅ **Usage Tip**:  
Schedule this with a cron job or run before your app starts to keep logs manageable.


