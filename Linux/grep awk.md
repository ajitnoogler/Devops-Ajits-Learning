ps | awk '{print $1}'

ps | grep | grep bash | awk '{print $1}'

grep "GET /index.html" /var/log/httpd/access_log | awk '{print $1}'


grep "GET /index.html" /var/log/httpd/access_log | awk '{print $1, $4, $5, $6, $7, $9}'
sample output
192.168.0.1 [07/Jul/2025:10:11:23 +0530] "GET /index.html 200


192.168.0.1 - - [07/Jul/2025:10:11:23 +0530] "GET /index.html HTTP/1.1" 200 512

    $1 = IP Address → 192.168.0.1
    $4 = Timestamp Start → [07/Jul/2025:10:11:23
    $5 = Timestamp Zone → +0530]
    $6 = HTTP Method (with quote) → "GET
    $7 = Requested Path → /index.html
    $9 = HTTP Status Code → 200

    