# Log Analysis Commands Linux

Sample Log:

025-05-30 12:49:43 status half-configured libc-bin:amd64 2.39-0ubuntu8.4
2025-05-30 12:49:43 status installed libc-bin:amd64 2.39-0ubuntu8.4

$1 2025-05-30 
$2 12:49:43
$3 status
$4 installed
$5 libc-bin:amd64
$6 2.39-0ubuntu8.4

$ awk '{print $1, $2}' /var/log/dpkg.log
2025-05-30 12:49:43
2025-05-30 12:49:43

$ awk '{print $1, $2, $5, $6}' dpkg.log 
2025-05-30 12:49:43 libc-bin:amd64 2.39-0ubuntu8.4
2025-05-30 12:49:43 libc-bin:amd64 2.39-0ubuntu8.4

$ awk '{print $1, $2, $3, $5, $6}' dpkg.log | grep 'status'
2025-05-30 12:49:43 status libc-bin:amd64 2.39-0ubuntu8.4
2025-05-30 12:49:43 status libc-bin:amd64 2.39-0ubuntu8.4

$ cut -d" " -f6 dpkg.log 
2.39-0ubuntu8.4
2.39-0ubuntu8.4

$ cut -d" " -f6 dpkg.log | sort

$ cut -d" " -f6 dpkg.log | sort | uniq

$ cut -d" " -f6 dpkg.log | sort | uniq -c // with count.



$ grep -E 'error|fail|critical' /var/log/access.log      // Extended regex

$ grep -rEi 'error|fail|critical' /var/log/access.log    // Search recursively in all .log files

$ grep -iE 'error|fail|critical' /var/log/access.log

$ grep --color=always -Ei 'error|fail|critical' /var/log/access.log    //  Highlight matches

$ grep -nE 'error|fail|critical' /var/log/access.log    //  Show matching lines with line numbers

# Search using a pattern file (for many strings)
Create a file called patterns.txt: Write below pattern.
error
fail
critical
timeout

$ grep -Ff patterns.txt log.txt

# 📌 Summary Table

| Purpose                     | Command                       |                  |               |
| --------------------------- | ----------------------------- | ---------------- | ------------- |
| Match multiple strings      | \`grep -E 'one                | two              | three' file\` |
| Use multiple `-e` flags     | `grep -e 'one' -e 'two' file` |                  |               |
| Case-insensitive            | \`grep -iE 'one               | two' file\`      |               |
| Use pattern file            | `grep -Ff patterns.txt file`  |                  |               |
| Show line numbers           | \`grep -nE 'one               | two' file\`      |               |
| Search all logs recursively | \`grep -rEi 'one              | two' /var/log/\` |               |
| Highlight matches           | \`grep --color=always -E 'one | two' file\`      |               |


# Whereis and which cmd:

| Command   | What it does                                                      | Use Case Example                            |
| --------- | ----------------------------------------------------------------- | ------------------------------------------- |
| `which`   | Shows the **exact path** of a command in your `PATH`              | `which python` → `/usr/bin/python`          |
| `whereis` | Locates **binary**, **source**, and **man page** files            | `whereis ls` → `/bin/ls /usr/share/man/...` |
| `type`    | Tells you **how a command is interpreted** (builtin, alias, etc.) | `type cd` → `cd is a shell builtin`         |


