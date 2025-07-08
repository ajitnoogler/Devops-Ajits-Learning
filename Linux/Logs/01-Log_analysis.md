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

$ ifconfig | grep -i inet | awk '{print $1, $2, $4}'

$ ifconfig | grep -i "inet" | awk '{print $1, $2, $4}'
inet 172.17.0.1 255.255.0.0
inet 10.0.0.134 255.255.0.0
inet6 fe80::7e1e:52ff:fe05:adab 64
inet 127.0.0.1 255.0.0.0
inet6 ::1 128

$ ifconfig | grep -i "inet" | grep -v "inet6" | awk '{print $1, $2, $4}'   // -v Excludes line containing inet6
inet 172.17.0.1 255.255.0.0
inet 10.0.0.134 255.255.0.0
inet 127.0.0.1 255.0.0.0


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



# Access.log Analysis:

# 🚨 Top IPs making requests:

$ cut -d' ' -f1 access.log | sort | uniq -c | sort -nr | head

482 66.249.73.135

364 46.105.14.53

| Count | IP Address    | Meaning                                        |
| ----- | ------------- | ---------------------------------------------- |
| 482   | 66.249.73.135 | This IP made 482 requests (likely a Googlebot) |
| 364   | 46.105.14.53  | Made 364 requests                              |
| ...   | ...           | ...                                            |


$ grep -E '404|500|timeout' access.log

$ grep -e '404' -e '500' -e 'timeout' access.log    // e for multiple options

$ grep -iE 'error|fail|timeout' access.log    //  Case-insensitive multiple patterns

$ grep --color=always -E '500|timeout|fail' access.log  // Search and highlight matches

$ grep -rE '500|404|timeout' /var/log/ // Search recursively in log directory

$ grep -E '500|timeout' access*.log // Grep from multiple files

$ grep -oE '404|500|timeout' access.log  // Get only matched part (not whole line)

$ grep -oE '404|500|timeout' access.log | sort | uniq -c | sort -nr   // Count how many times each term appeared 🔹 Get frequency of each match — great for dashboards or alerts.

$ grep -E '2025:14:[0-9]{2}:[0-9]{2}.*(404|500)' access.log    // Match patterns with timestamps (combined filtering) 🔹 Extract 404/500 errors during 2025:14:XX:XX time.

$ grep -E '404|500' access.log | awk '{print $1, $4, $9}'  // Bonus: Combine with awk for field-level filtering 🔹 Shows IP, timestamp, and HTTP status.

$ grep -i "GET" | awk -F '-' '{print $1}' access.log 

$ grep -i "GET" | awk -F '-' '{print $1, $2, $3, $4, $5}' access.log 
180.76.6.56     [20/May/2015:21:05:56 +0000] "GET /robots.txt HTTP/1.1" 200   " " "Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2"
46.105.14.53     [20/May/2015:21:05:15 +0000] "GET /blog/tags/puppet?flav=rss20 HTTP/1.1" 200 14872 " " "UniversalFeedParser/4.2 pre

$ grep -i "GET" | awk -F '-' '{print $1}' access.log | uniq     // -F Field Separator.

180.76.6.56 

46.105.14.53 

$ egrep -i 'GET|POST' access.log

$ egrep -i 'GET|POST' access.log | awk -F '-' '{print $1, $2, $3, $4, $5}' access.log 
66.249.73.135     [20/May/2015:21:05:00 +0000] "GET /?flav=atom HTTP/1.1" 200 32352 " " "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" 
180.76.6.56     [20/May/2015:21:05:56 +0000] "GET /robots.txt HTTP/1.1" 200   " " "Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2"

$ egrep -i 'GET|POST' access.log | awk -F '-' '{print $1, $2, $3, $4, $5}' | uniq -c access.log 


# Use a pattern file for large search lists
Create a patterns.txt: write below in file

  404
  
  500
  
  timeout
  
  unauthorized

$ grep -Ff patterns.txt access.log
🔹 -F: fixed string search (no regex)
🔹 -f: read patterns from file
  
