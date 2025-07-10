
| Task                                    | Command Example                                                             |                              |
| --------------------------------------- | --------------------------------------------------------------------------- | ---------------------------- |
| **Show only ERROR lines**               | `grep -i error /var/log/app.log`                                            |                              |
| **Extract IP + status from access.log** | `awk '{print $1, $9}' access.log`                                           |                              |
| **Mask last octet of all IPs**          | `sed -E 's/([0-9]+\.[0-9]+\.[0-9]+\.)[0-9]+/\1xxx/g' access.log`            |                              |
| **Count unique URLs**                   | `awk '{print $7}' access.log \| sort \| uniq -c \| sort -nr`                |                              |
| **View last 100 lines, live**           | `tail -n 100 -F /var/log/nginx/access.log`                                  |                              |
| **Query 5xx errors in systemd logs**    | `journalctl -u nginx --since "1 hour ago" \| grep ' 5[0-9][0-9] '`          |                              |
| **Parse JSON errors**                   | `jq -r 'select(.level=="ERROR")                                             | "(.time) (.msg)"' app.json\` |
| **Interactive log browsing**            | `lnav /var/log/*.log`                                                       |                              |
| **HTML report of access.log**           | `goaccess access.log --log-format=COMBINED -o report.html --real-time-html` |                              |
| **Monitor log file with color**         | `multitail -c /var/log/app.log`                                             |                              |
| **Filter logs by date**                 | `awk '$0 ~ /2023-10-01/' /var/log/app.log`                                  |                              |
| **Count lines in log file**             | `wc -l /var/log/app.log`                                                    |                              |
| **Show last 50 lines of a file**        | `tail -n 50 /var/log/app.log`                                               |                              |
| **Search for a specific string**        | `grep "specific string" /var/log/app.log`                                   |                              |
| **Show lines with timestamps**          |`awk '{print $1, $2, $3}' /var/log/app.log`                                  |                              |
| **Extract specific fields**             | `awk '{print $1, $2, $3, $7}' /var/log/app.log`                             |                              |
| **Count occurrences of a word**         | `grep -o "word" /var/log/app.log | wc -l`                                   |                              |
| **Show lines with a specific pattern**  |`grep -E "pattern" /var/log/app.log`                                         |                              |
| **Show lines with a specific date**     | `grep "2023-10-01" /var/log/app.log`                                        |                              |
| **Show lines with a specific time**     | `grep "12:00:00" /var/log/app.log`                                          |                              |
| **Show lines with a specific user**     | `grep "username" /var/log/app.log`                                          |                              |
| **Show lines with a specific IPs**      | `grep "172.16.120.1" /var/log/app.log`                                      |                              |                         
| **Show lines with a specific status code** | `grep "200" /var/log/app.log`                                            |                              |
| **Show lines with a specific error code** | `grep "404" /var/log/app.log`                                             |                              |
| **Show lines with a specific URL**      | `grep "example.com" /var/log/app.log`                                       |                              |
| **Show lines with a specific method**   | `grep "GET" /var/log/app.log`                                               |                              |
| **Show lines with a specific response time** | `awk '$9 > 500' /var/log/app.log`                                      |                              |
| **Show lines with a specific user agent** | `grep "Mozilla" /var/log/app.log`                                         |                              |
| **Show lines with a specific referrer** | `grep "referrer.com" /var/log/app.log`                                      |                              |
| **Show lines with a specific request**  | `grep "POST /api" /var/log/app.log`                                         |                              |
| **Show lines with a specific response size** | `awk '$10 > 1000' /var/log/app.log`                                    |                              |
| **Show lines with a specific protocol** | `grep "HTTP/1.1" /var/log/app.log`                                          |                              |
| **Show lines with a specific content type** | `grep "application/json" /var/log/app.log`                              |                              |
| **Show lines with a specific status message** | `grep "OK" /var/log/app.log`                                          |                              |
| **Show lines with a specific error message**  | `grep "Not Found" /var/log/app.log`                                   |                              |
| **Show lines with a specific log level** | `grep "INFO" /var/log/app.log`                                             |                              |
| **Show lines with a specific log tag**  | `grep "TAG" /var/log/app.log`                                               |                              |
| **Show lines with a specific log source** | `grep "source" /var/log/app.log`                                          |                              |
| **Show lines with a specific log message** | `grep "message" /var/log/app.log`                                        |                              |
| **Show lines with a specific log ID**   | `grep "ID" /var/log/app.log`                                                |                              |
| **Show lines with a specific log timestamp** | `grep "2023-10-01T12:00:00" /var/log/app.log`                          |                              |
| **Show lines with a specific log level and message** | `grep "ERROR" /var/log/app.log | grep "specific message"`      |                              |
| **Show lines with a specific log level and user** | `grep "INFO" /var/log/app.log | grep "username"`                  |                              |
| **Show lines with a specific log level and IP** | `grep "DEBUG" /var/log/app.log | grep "