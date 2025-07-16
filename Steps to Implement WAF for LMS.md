
#### End-to-End step-by-step implementation guide to deploy 

#### ModSecurity WAF on Ubuntu Linux to block parallel video downloads on your LMS portal.

---

#### 🛡️ Step-by-Step Guide: Block Parallel Video Downloads with ModSecurity on LMS (Ubuntu)

## 🧰 Prerequisites

| Item                  | Requirement                                    |
|-----------------------|------------------------------------------------|
| OS                    | Ubuntu 20.04 or 22.04                          |
| Web server            | Apache (httpd)                                 |
| ModSecurity           | v2.9+ (as Apache module)                       |
| LMS Portal            | Running on the same Apache server or proxied  |

---

## 🔧 Step 1: Install Apache + ModSecurity

```bash
sudo apt update
sudo apt install apache2 libapache2-mod-security2 -y
````

Enable the ModSecurity module:

```bash
sudo a2enmod security2
```

Restart Apache:

```bash
sudo systemctl restart apache2
```

---

### 🗂️ Step 2: Enable and Configure ModSecurity

#### Enable Detection Mode (Default)

```bash
sudo cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
sudo nano /etc/modsecurity/modsecurity.conf
```

✅ Set the engine to **On**:

```apache
SecRuleEngine On
```

Save and exit.

---

#### 📁 Step 3: Create Custom WAF Rules Directory

```bash
sudo mkdir -p /etc/modsecurity/rules
```

Include this line at the bottom of your `modsecurity.conf`:

```apache
Include /etc/modsecurity/rules/*.conf
```

---

#### 📝 Step 4: Add Custom WAF Rules for Blocking Parallel Downloads

Create and open the rule file:

```bash
sudo nano /etc/modsecurity/rules/block_parallel_downloads.conf
```

Paste the following:

```apache
# 🛑 Block Download Managers by User-Agent
SecRule REQUEST_HEADERS:User-Agent "@rx (wget|curl|python|scrapy|aria2|idm|Go-http-client|youtube-dl)" \
 "id:200001,phase:1,deny,status:403,log,msg:'Blocked suspicious User-Agent performing parallel download'"

# 📦 Initialize Per-IP Tracking
SecAction "id:200002,phase:1,nolog,pass,initcol:ip=%{REMOTE_ADDR},expirevar:ip.video_counter=60"

# 🎯 Track Requests to Video Endpoints (.mp4/.m3u8)
SecRule REQUEST_URI "@rx ^/videos/.*\.(mp4|m3u8)$" \
 "id:200003,phase:2,pass,nolog,ctl:ruleEngine=DetectionOnly,setvar:ip.video_counter=+1"

# 🚫 Block if More Than 5 Video Requests in 60 Seconds
SecRule IP:video_counter "@gt 5" \
 "id:200004,phase:2,deny,status:429,log,msg:'Too many parallel video download attempts from IP'"
```

> 📌 Adjust `/videos/.*\.(mp4|m3u8)$` to your LMS video path (e.g., `/stream/`, `/content/`, etc.)

Save and exit.

---

#### 🚀 Step 5: Restart Apache and Test

```bash
sudo systemctl restart apache2
```

####✅ Your WAF is now actively protecting the LMS video content from:

* Download manager abuse (aria2, IDM, etc.)
  
* Excessive parallel requests from the same IP

---

#### 🧪 Step 6: Simulate the Attack (From Client or Terminal)

#### Test with `aria2` or `curl`:

```bash
curl -A "aria2" http://your-lms.com/videos/lesson1.mp4 -o /dev/null
```

Should return: `403 Forbidden`

#### Test Rate Limit (More than 5 in 60s)

```bash
for i in {1..10}; do
  curl -s http://your-lms.com/videos/lesson1.mp4 -o /dev/null &
done
wait
```

Should block after 5 requests: `429 Too Many Requests`

---

#### 🔍 Step 7: View ModSecurity Logs

```bash
sudo tail -f /var/log/apache2/modsec_audit.log
```

Look for entries with your rule IDs (e.g., `200001`, `200004`).

---

#### 🧠 Optional Enhancements

| Enhancement                          | Command / Concept                                          |
| ------------------------------------ | ---------------------------------------------------------- |
| 🧩 OWASP CRS rules                   | Install: `sudo apt install modsecurity-crs`                |
| 📊 Logging to SIEM or ELK            | Forward logs from `/var/log/apache2/modsec_audit.log`      |
| 🔔 Alerting                          | Use tools like `fail2ban`, `Graylog`, or `Grafana Loki`    |
| 📦 Persistent storage of IP counters | Use `persistdb` with `SecPersistDB` for long-term tracking |

---

#### 📌 Notes

* This implementation uses **ModSecurity v2**, default with Apache on Ubuntu.
* For **Nginx**, you'd use ModSecurity with `modsecurity-nginx`.
* For **Cloud-based LMS**, apply similar logic using **Cloudflare WAF**, **AWS WAF**, etc.

---

#### ✅ Verification Checklist

| ✅ Task                          | Status  |
| ------------------------------- | ------- |
| ModSecurity installed           | ✅       |
| WAF rules written and included  | ✅       |
| Apache restarted                | ✅       |
| Blocking suspicious User-Agents | ✅ (403) |
| Rate-limiting video requests    | ✅ (429) |
| Logs available for monitoring   | ✅       |

```

---

Absolutely! Here's a **clean `.md`-formatted file** tailored specifically for **deploying a Grafana dashboard with ModSecurity logs via Loki** — ready to be added to your GitHub project as `README.md` or documentation.

---

````md
# 📊 Grafana Dashboard for ModSecurity Logs via Loki

This guide shows how to set up a **Grafana dashboard** using **Loki** to visualize and analyze **ModSecurity logs** from Apache HTTP Server.

---

#### 🧱 Architecture Overview

```text
[Apache + ModSecurity] --> [Promtail] --> [Loki] --> [Grafana Dashboard]
````

| Component   | Role                                    |
| ----------- | --------------------------------------- |
| ModSecurity | Generates WAF logs (`modsec_audit.log`) |
| Promtail    | Ships logs to Loki                      |
| Loki        | Stores and indexes logs                 |
| Grafana     | Visualizes WAF logs & alerts            |

---

## ✅ Prerequisites

* Ubuntu 20.04 / 22.04 system
* Apache2 + ModSecurity installed and logging to `/var/log/apache2/modsec_audit.log`
* Root or sudo privileges

---

#### ⚙️ Step 1: Install Loki, Promtail & Grafana

#### Add Grafana APT repo:

```bash
sudo apt install -y gnupg curl software-properties-common
curl -s https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
sudo apt update
```

#### Install components:

```bash
sudo apt install grafana loki promtail -y
```

---

#### 🗃️ Step 2: Configure Loki

Edit the Loki config file:

```bash
sudo nano /etc/loki/local-config.yaml
```

Paste the following:

```yaml
auth_enabled: false

server:
  http_listen_port: 3100

ingester:
  lifecycler:
    ring:
      kvstore:
        store: inmemory
      replication_factor: 1

schema_config:
  configs:
    - from: 2024-01-01
      store: boltdb-shipper
      object_store: filesystem
      schema: v11
      index:
        prefix: index_
        period: 24h

storage_config:
  boltdb_shipper:
    active_index_directory: /tmp/loki/index
    cache_location: /tmp/loki/cache
  filesystem:
    directory: /tmp/loki/chunks

limits_config:
  reject_old_samples: true
  reject_old_samples_max_age: 168h
```

---

#### 🚚 Step 3: Configure Promtail

Edit Promtail config:

```bash
sudo nano /etc/promtail/config.yml
```

Add this configuration to scrape ModSecurity logs:

```yaml
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://localhost:3100/loki/api/v1/push

scrape_configs:
  - job_name: modsec_logs
    static_configs:
      - targets:
          - localhost
        labels:
          job: apache_modsec
          __path__: /var/log/apache2/modsec_audit.log
```

---

#### ▶️ Step 4: Start Services

```bash
sudo systemctl enable --now loki
sudo systemctl enable --now promtail
sudo systemctl enable --now grafana-server
```

---

#### 🌐 Step 5: Access Grafana UI

* URL: [http://localhost:3000](http://localhost:3000)
* Default login:

  * **Username**: `admin`
  * **Password**: `admin` (change on first login)

---

#### 📡 Step 6: Add Loki as a Data Source in Grafana

1. Go to **Settings → Data Sources**
2. Click **Add data source**
3. Choose **Loki**
4. URL: `http://localhost:3100`
5. Click **Save & Test**

---

#### 📈 Step 7: Create Dashboard Panels

You can now build panels using LogQL queries.

### 🔍 Example Queries

#### 🔹 Total WAF Logs

```logql
{job="apache_modsec"}
```

#### 🔹 ModSecurity Blocks by Rule ID

```logql
{job="apache_modsec"} |= "id:200004"
```

#### 🔹 Suspicious User-Agents

```logql
{job="apache_modsec"} |= "Blocked suspicious"
```

#### 🔹 Count Requests Per IP

```logql
{job="apache_modsec"} | pattern `<ip>` | count_over_time(5m)
```

---

#### 💡 Recommended Panels

| Panel Title              | LogQL Query or Field Example                     |                               |
| ------------------------ | ------------------------------------------------ | ----------------------------- |
| Total WAF Events         | `{job="apache_modsec"}`                          |                               |
| Blocked IPs (Rate Limit) | \`                                               | = "id:200004"\` + count by IP |
| Suspicious User-Agents   | \`                                               | = "Blocked suspicious"\`      |
| Top Violated Paths       | Filter URI from audit log (e.g. `/videos/*.mp4`) |                               |
| Rule ID Distribution     | Parse `"id:xxxxx"` fields                        |                               |

---

#### 🔔 Optional: Alerts

* Go to **Alerting → Contact Points**
* Set up Slack, Email, etc.
* Trigger alerts for:

  * Spike in blocked events
  * Excessive downloads from one IP

---

#### 🧼 Maintenance Tips

| Task                | Frequency |
| ------------------- | --------- |
| Rotate modsec logs  | Weekly    |
| Review dashboards   | Weekly    |
| Update Grafana/Loki | Monthly   |
| Tune WAF rules      | As needed |

---

#### 🧪 Test Queries

```bash
curl -A "aria2" http://localhost/videos/sample.mp4
for i in {1..10}; do curl http://localhost/videos/sample.mp4 -o /dev/null & done; wait
sudo tail -f /var/log/apache2/modsec_audit.log
```

---

#### 📚 References

* [Grafana Loki Docs](https://grafana.com/docs/loki/latest/)
* [Promtail Docs](https://grafana.com/docs/loki/latest/clients/promtail/)
* [ModSecurity Docs](https://github.com/SpiderLabs/ModSecurity)
* [OWASP CRS](https://coreruleset.org/)

---

#### ✅ Result

* 🎯 Real-time ModSecurity log shipping with Promtail
* 📦 Logs stored in Loki
* 📊 Dashboard & alerting with Grafana
* 🔐 Security insight into WAF activity

```
---

#### 🧱 Loki, Promtail & Grafana Explained

| Component   | 🔍 What It Is                        | 🛠️ Purpose / Function                                                | ⚡ Key Features                                                   |
|-------------|--------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------|
| **Loki**    | Log aggregation system by Grafana    | Stores, indexes, and serves logs collected from Promtail             | - Scalable & efficient log storage <br> - Query via LogQL <br> - Integrates with Grafana |
| **Promtail**| Log shipping agent for Loki          | Reads local log files and pushes them to Loki                        | - Auto-labels logs <br> - Lightweight & fast <br> - Configurable scraping |
| **Grafana** | Visualization & alerting dashboard   | Visualizes logs and metrics using panels, graphs, and alerts         | - Supports Loki, Prometheus, and many other data sources <br> - Build real-time dashboards <br> - Create alerts on logs or metrics |

---

#### 🧪 Example Flow:

[ Apache + ModSecurity ]
           ↓
[ Promtail reads modsec_audit.log ]
           ↓
[ Loki stores the logs ]
           ↓
[ Grafana queries + visualizes logs ]

--- 
