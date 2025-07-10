
### Monitoring

### 🔍 Prometheus – Monitoring & Alerting Tool (Metric collection & alerting)

    - Purpose: Collects and stores metrics (like CPU usage, memory, disk, HTTP requests).

    - Data model: Time-series data with labels (e.g., cpu_usage{instance="server1"})

    Function:

       - Scrapes metrics from targets (like Node Exporter, cAdvisor, etc.)

       - Stores them in its time-series database

       -  Evaluates alert rules and sends alerts (via Alertmanager)

✅ Think of Prometheus as the backend data collector.

---

### 📊 Grafana – Visualization & Dashboard Tool port 3000 (Data visualization)

    - Purpose: Creates dashboards to visualize data from many sources, including Prometheus.

    Function:

       - Connects to Prometheus as a data source

       - Provides rich graphs, charts, alerts, and panels

       - Supports many data sources (Prometheus, InfluxDB, Elasticsearch, MySQL, etc.)

       - It can work with Cloud watch as data source.

✅ Think of Grafana as the frontend visualizer.

--- 

### Port Details:

| Component         | Port | Protocol | Description                         |
| ----------------- | ---- | -------- | ----------------------------------- |
| **Prometheus**    | 9090 | **TCP**  | Prometheus web UI & API             |
| **Grafana**       | 3000 | **TCP**  | Grafana web interface               |
| Alertmanager      | 9093 | **TCP**  | For Prometheus alerts               |
| Node Exporter     | 9100 | **TCP**  | Exposes system metrics              |
| cAdvisor          | 8080 | **TCP**  | Container metrics                   |
| Blackbox Exporter | 9115 | **TCP**  | Endpoint probing (HTTP, ICMP, etc.) |

---
