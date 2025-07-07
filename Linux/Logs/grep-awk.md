

Sample Log


$1 = remote host (IP address)
$2 = remote logname (identd) 
$3 = remote user (authenticated user, if any)
$4 = [timestamp]
$5 = “-” (literal, separates timestamp and request)
$6 = HTTP method (with leading quote)
$7 = URL path
$8 = HTTP version (with trailing quote)
$9 = status code
… etc.

So $2 is the remote logname, as provided by the identd service on the client machine. In almost all real‑world setups, identd isn’t used, so you’ll almost always see a dash (-) in that position:


# Example log line (Apache “combined”):
203.0.113.5 - john [06/Jul/2025:23:00:01 +0530] "GET /index.html HTTP/1.1" 200 3456 "-" "Mozilla/5.0"

# Here:
# $1 = 203.0.113.5
# $2 = -           ← remote logname (identd; typically “-”)
# $3 = john        ← authenticated user (if HTTP auth was used)
# $4 = [06/Jul/2025:23:00:01
# …and so on.

# Here’s a one‑liner that uses grep to filter for HTTP requests (e.g. GET or POST) and then awk to pull out the remote host ($1), timestamp ($4), HTTP method ($6) and status code ($9):

grep -E '"(GET|POST|PUT|DELETE)' access.log | awk '{host=$1; time=substr($4,2); method=substr($6,2); status=$9; print host, time, method, status}'

awk '$6 ~ /"(GET|POST|PUT|DELETE)/ { host=$1; time=substr($4,2); method=substr($6,2); status=$9; print host, time, method, status }' access.log

# Print IP, timestamp, request, status
awk '{print $1, $4, $6, $7, $9}' /var/log/nginx/access.log


grep -E '"(GET|POST|PUT|DELETE)' access.log \
  | awk '{ 
      host   = $1; 
      time   = substr($4,2);      # drop leading “[“
      method = substr($6,2);      # drop leading “"”
      status = $9; 
      print host, time, method, status 
    }'


# Tool Comparison & Use Cases

| Tool     | Primary Role                                  | When to use
| -------- | --------------------------------------------- |-------------------------------------------------------------------------------------------------------| 
| **grep** | Fast text‑matching                            |  • You need to quickly **filter** lines by a simple pattern (e.g. status code, method).<br>           |
|===================================================================================================================================================================
|                                                          |  • You don’t care about extracting fields—just about inclusion/exclusion.                             |
| **awk**  | Field‑oriented processing & simple arithmetic |  • You want to **extract**, **reorder**, or **aggregate** columns (fields).<br>                       |
|==================================================================================================================================================================|
|                                                          |  • You need basic logic (if‑statements), counters, math (e.g. summing bytes).                         |
| **sed**  | Stream editing (substitute, delete, insert)   |  • You need to **transform** text inside each line (e.g. mask IPs, normalize timestamps).<br>         |
|                                                          |  • You want to **delete** or **insert** entire lines matching patterns.                               |
|==================================================================================================================================================================|