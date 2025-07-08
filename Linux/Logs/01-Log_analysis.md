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
