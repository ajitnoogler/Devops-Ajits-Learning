
### Grep and Awk

ps | awk '{print $1}'

ps | grep | grep bash | awk '{print $1}'

grep "GET /index.html" /var/log/httpd/access_log | awk '{print $1}'


grep "GET /index.html" /var/log/httpd/access_log | awk '{print $1, $4, $5, $6, $7, $9}'
sample output
192.168.0.1 [07/Jul/2025:10:11:23 +0530] "GET /index.html 200

$ grep -i "GET" | awk -F '-' '{print $1}' access.log

$ grep -i "GET" | awk -F '-' '{print $1, $2, $3, $4, $5}' access.log 

180.76.6.56 [20/May/2015:21:05:56 +0000] "GET /robots.txt HTTP/1.1" 200 " " "Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2" 

46.105.14.53 [20/May/2015:21:05:15 +0000] "GET /blog/tags/puppet?flav=rss20 HTTP/1.1" 200 14872 " " "UniversalFeedParser/4.2 pre

$ grep -i "GET" | awk -F '-' '{print $1}' access.log | uniq // -F Field Separator.

180.76.6.56

46.105.14.53

$ egrep -i 'GET|POST' access.log | awk -F '-' '{print $1, $2, $3, $4, $5}' | uniq -c access.log

---

### Cut

192.168.0.1 - - [07/Jul/2025:10:11:23 +0530] "GET /index.html HTTP/1.1" 200 512

    $1 = IP Address → 192.168.0.1
    $4 = Timestamp Start → [07/Jul/2025:10:11:23
    $5 = Timestamp Zone → +0530]
    $6 = HTTP Method (with quote) → "GET
    $7 = Requested Path → /index.html
    $9 = HTTP Status Code → 200

    $ cut -d'"' -f3 access.log | cut -d' ' -f2 | sort | uniq -c | sort -nr  // n-numeric r-reverse

    $ cut -d'"' -f3 access.log | cut -d' ' -f2 | sort | uniq -c | sort -nr  200 

445 304
Count 	Status Code 	Meaning
9126 	200 	OK (successful request)
445 	304 	Not Modified (cached)
123 	404 	Not Found
89 	500 	Internal Server Error

$ grep -E '404|500|timeout' access.log

$ grep -e '404' -e '500' -e 'timeout' access.log // e for multiple options

$ grep -iE 'error|fail|timeout' access.log // Case-insensitive multiple patterns

$ grep --color=always -E '500|timeout|fail' access.log // Search and highlight matches

$ grep -rE '500|404|timeout' /var/log/ // Search recursively in log directory

$ grep -E '500|timeout' access*.log // Grep from multiple files

$ grep -oE '404|500|timeout' access.log // Get only matched part (not whole line)

$ grep -oE '404|500|timeout' access.log | sort | uniq -c | sort -nr // Count how many times each term appeared 🔹 Get frequency of each match — great for dashboards or alerts.

$ grep -E '2025:14:[0-9]{2}:[0-9]{2}.*(404|500)' access.log // Match patterns with timestamps (combined filtering) 🔹 Extract 404/500 errors during 2025:14:XX:XX time.

$ grep -E '404|500' access.log | awk '{print $1, $4, $9}' // Bonus: Combine with awk for field-level filtering 🔹 Shows IP, timestamp, and HTTP status.

$ grep -i "GET" | awk -F '-' '{print $1}' access.log

$ grep -i "GET" | awk -F '-' '{print $1, $2, $3, $4, $5}' access.log 

180.76.6.56 [20/May/2015:21:05:56 +0000] "GET /robots.txt HTTP/1.1" 200 " " "Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2" 

46.105.14.53 [20/May/2015:21:05:15 +0000] "GET /blog/tags/puppet?flav=rss20 HTTP/1.1" 200 14872 " " "UniversalFeedParser/4.2 pre

$ grep -i "GET" | awk -F '-' '{print $1}' access.log | uniq // -F Field Separator.

180.76.6.56

46.105.14.53

$ egrep -i 'GET|POST' access.log

$ egrep -i 'GET|POST' access.log | awk -F '-' '{print $1, $2, $3, $4, $5}' access.log 

66.249.73.135 [20/May/2015:21:05:00 +0000] "GET /?flav=atom HTTP/1.1" 200 32352 " " "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" 180.76.6.56 [20/May/2015:21:05:56 +0000] "GET /robots.txt HTTP/1.1" 200 " " "Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2"

$ egrep -i 'GET|POST' access.log | awk -F '-' '{print $1, $2, $3, $4, $5}' | uniq -c access.log
