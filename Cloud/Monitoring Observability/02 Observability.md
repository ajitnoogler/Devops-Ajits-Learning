

![image](https://github.com/user-attachments/assets/91a4b79f-0118-4092-be12-81121a948877)

## Prometheus: used for metric tracing. (monitoring, metric and tracing)

- Purpose: Collects and stores metrics (like CPU usage, memory, disk, HTTP requests).

- Data model: Time-series data with labels (e.g., cpu_usage{instance="server1"})

---

### Grafana – Visualization & Dashboard Tool port 3000 (Data visualization)

- Purpose: Creates dashboards to visualize data from many sources, including Prometheus.

Function:

   - Connects to Prometheus as a data source

   - Provides rich graphs, charts, alerts, and panels

   - Supports many data sources (Prometheus, InfluxDB, Elasticsearch, MySQL, etc.)
   
---

### What you want to monitor? Node Metrics
- web app  up | reachable 
- Instance running web app ( instance / node, load metric - CPU | RAM | Disk-Usage | Network| Disk IO )

---

### Prometheus -- Data Source (Kind - TSD) Time Series Data. Live and months of Data, collect metric every 10 sec
- node exporter
- blackbox exporter
- DB TSDB (Time Series Database) stores all collected metrics in DB.
- Prometheues Query DB using Prom-QL

### Prometheus Metric collection:
- Collect metrics from instance / node i.e "xyz.com/.../metrics" or "IP:xxx/.../metrics"
- Exporters, collects the metric and keep it on instance | VM under xyz.com/metrics folder for Promethues to collect metric (common exporter: node exporter | Blackbox exporter)
- node-exporter is installed on the vm | server | instance | container. TCP Port 9100.
- Blackbox exporter can be installed on vm | server | instance | container. It send request / probe to webapp via url. It looks for HTTP 200 Response.
- Prometheus access /metric folder to collect metric of the server. /metrics is also called metrics endpoint.
- Prometheus collects raw metric which is difficult to understand hence so in order to get raw data in proper format Graphana comes into picture.
- Graphana is visualisation tool, The data collected by Prometheus is shared to Graphana for visualisation, for creating charts, graphs etc. Now it is human understandable format.
- Graphana Dashboard: Node Exporter Full Dashboard ID | Cloud Watch | Prometheus Blackbox Exporter Dashboard
  
--- 

                 +----------------+
                 |     Server     |
                 |    (webapp)    |  ← Node Exporter (/metrics) runs on this server TCP port 9100
                 +----------------+
                          |
       Blackbox Exporter (/metrics) — runs on a separate VM or instance TCP Port 9115
                          |
             +------------+------------+
                          |
                    +-------------+
                    |  Prometheus  |  ← Collects raw metrics
                    +-------------+
                          |
                    +-------------+
                    |   Grafana    |  ← Converts raw metrics into visualizations
                    +-------------+
                     /     |      \
            +-----------+ +--------+ +----------+
            |  Tables   | | Charts | |  Graphs  |
            +-----------+ +--------+ +----------+


---


