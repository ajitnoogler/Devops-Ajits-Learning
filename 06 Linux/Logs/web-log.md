Here’s how a DevOps/cloud engineer typically slices and dices HTTP access logs—whether it’s Apache’s “combined” format, NGINX, or JSON‑structured logs—to extract just the columns you need, filter for errors or time windows, and generate quick stats.

---

## 1. Know Your Log Format & Field Positions

### Common “Combined” (Apache/NGINX) format

```
$remote_addr – $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"
```

| Field   | Position (awk `$n`)    | Example                        |
| ------- | ---------------------- | ------------------------------ |
| IP      | `$1`                   | `203.0.113.5`                  |
| Time    | `$4` (incl. `[` )      | `[06/Jul/2025:23:00:01 +0530]` |
| Request | `$6–$8` (split quotes) | `"GET /api/v1/users HTTP/1.1"` |
| Status  | `$9`                   | `200`                          |
| Bytes   | `$10`                  | `3456`                         |

---

## 2. Simple Column Extraction

### a) Using `awk`

```bash
# Print IP, timestamp, request, status
awk '{print $1, $4, $6, $7, $9}' /var/log/nginx/access.log
```

### b) Using `cut`

> Only works reliably when columns are truly space‑delimited (no embedded spaces).

```bash
cut -d' ' -f1,4,9 /var/log/apache2/access.log
```

---

## 3. Handling Quoted Fields & Custom Separators

Because the `"$request"` field contains spaces, it’s easier in `awk` to change the field separator:

```bash
# Use quote (") as an FS to isolate the request field in $2
awk -F\" '{ print $1, $2, $3 }' access.log \
  | awk '{print $1, $4}'   # then print IP ($1) and request ($4 after trimming)
```

Or combine into one:

```bash
awk -F'"' '{ split($1,a," "); ip=a[1]; time=a[4]; req=$2; split($3,b," "); status=b[2]; print ip, time, status, req }' access.log
```

---

## 4. Filtering by Status, Method, Time Range

### a) Only 5xx errors

```bash
awk '$9 ~ /^5/ { print $1, $4, $6, $7, $9 }' access.log
```

### b) Only `POST` requests

```bash
awk '$6 ~ /POST/ { print $1, $4, $6, $7, $9 }' access.log
```

### c) Last 24 hours (NGINX with ISO timestamps)

```bash
# If timestamps are ISO (e.g. 2025-07-06T23:00:01)
awk '$4 >= "[06/Jul/2025:00:00:00" && $4 <= "[06/Jul/2025:23:59:59"' access.log \
  | awk '{print $1, $4, $9}'
```

Or with `date` interpolation:

```bash
SINCE=$(date -d '1 day ago' '+[%d/%b/%Y:%H:%M:%S')
awk -v since="$SINCE" '$4 >= since { print $1, $4, $9 }' access.log
```

---

## 5. Aggregations & Top‑N Lists

### a) Top 10 client IPs

```bash
awk '{print $1}' access.log \
  | sort | uniq -c | sort -nr \
  | head -n 10
```

### b) Most requested URLs

```bash
awk '{print $7}' access.log \
  | sort | uniq -c | sort -nr \
  | head -n 10
```

### c) Count of status codes

```bash
awk '{print $9}' access.log \
  | sort | uniq -c | sort -nr
```

---

## 6. Parsing JSON‑Formatted Logs

If your service emits logs as JSON (e.g. containerized apps):

```bash
# Example JSON line:
# {"remote_addr":"203.0.113.5","time":"2025-07-06T23:00:01Z","request":"GET /health","status":200}

jq -r '. | "\(.remote_addr) [\(.time)] \(.status) \(.request)"' app.log
```

Filter on fields:

```bash
jq -r 'select(.status>=500) | "\(.time) \(.remote_addr) \(.status)"' app.log
```

---

## 7. Real‑Time Tail & Highlight

```bash
# Follow live and highlight “ERROR”
tail -F access.log \
  | grep --color=auto -i " 5[0-9][0-9] "    # catch any 5xx status
```

---

## 8. Interactive & Dashboarding

* **GoAccess**: TUI dashboard off a log file

  ```bash
  goaccess access.log --log-format=COMBINED --real-time-html -o report.html
  ```

* **ELK/EFK**: Ship via Filebeat/Fluent Bit → Elasticsearch → Kibana/Fluentd UI

* **Cloud Providers**:

  * AWS CloudWatch Logs Insights:

    ```sql
    fields @timestamp, @message
    | filter status >= 500
    | stats count(*) by status
    ```
  * Azure Monitor Log Analytics: Kusto queries similarly.

---

## 9. Sample “All‑in‑One” Pipelines

```bash
# Last hour 500-errors by URL, top 5
journalctl -u nginx --since "1 hour ago" \
  | awk '$9 ~ /^5/ { print $7 }' \
  | sort | uniq -c | sort -nr \
  | head -n 5
```

```bash
# Extract columns 1 (IP), 4 (time), 9 (status) and save CSV
awk '{print $1","substr($4,2)","$9}' access.log \
  > parsed_logs_$(date +%F).csv
```

```bash
# JSON log: count POSTs per minute
jq -r '[.time[0:16], .request] | "\(.[0]) \(.[1])"' app.log \
  | grep POST \
  | cut -d' ' -f1 \
  | sort | uniq -c
```

---

### Key Patterns

1. **Choose the right tool** (`cut` for simple, `awk` for power, `jq` for JSON).
2. **Handle embedded spaces** via custom field‑separators.
3. **Chain filters → transformations → aggregates** for quick stats.
4. **Automate & centralize** with GoAccess / ELK / CloudWatch.

With these recipes you can instantly pluck out any column, filter by status/method/time, and build both one‑liners and production pipelines for HTTP log analysis.
