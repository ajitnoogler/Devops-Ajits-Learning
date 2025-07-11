#### SRE

Here's a clear summary of what a **Site Reliability Engineer (SRE)** does and their **day-to-day responsibilities**:

---

## 👨‍💻 What is the Job of a Site Reliability Engineer (SRE)?

A **Site Reliability Engineer (SRE)** ensures that large-scale systems are **reliable, scalable, and performant**. They bridge the gap between **development and operations**, applying **software engineering practices** to solve infrastructure and reliability problems.

> 🧠 Think of SREs as **DevOps Engineers with a focus on automation, resilience, and SLAs/SLOs**.


#### 📅 Day-to-Day Tasks of an SRE

| Category                         | Daily Tasks                                                                                                          |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| 🛠️ **Monitoring & Alerting**    | - Maintain dashboards (Grafana, Prometheus, etc.)  <br> - Tune alerts to reduce noise                                |
| 🚨 **Incident Response**         | - On-call rotation for production issues  <br> - Triage alerts, runbooks, RCA for outages                            |
| 🔁 **Automation & CI/CD**        | - Automate infra tasks using scripts or Terraform <br> - Maintain CI/CD pipelines (Jenkins, GitHub Actions)          |
| 💾 **Infrastructure Management** | - Manage Kubernetes, VMs, storage, databases <br> - Capacity planning and performance tuning                         |
| 📈 **Reliability Engineering**   | - Define and track SLOs/SLAs/Error Budgets <br> - Conduct Chaos testing and failover drills                          |
| 🧪 **Testing & Validation**      | - Load/stress testing for scalability <br> - Validate backup and DR procedures                                       |
| 🔐 **Security & Compliance**     | - Patch management, config audits <br> - Ensure systems comply with security baselines                               |
| 📚 **Documentation & Runbooks**  | - Create/update troubleshooting guides, SOPs <br> - Postmortem writing after incidents                               |
| 🧑‍🤝‍🧑 **Collaboration**       | - Work closely with Dev, QA, Infra teams <br> - Participate in design reviews for reliability impact                 |
| 📊 **Tooling & Observability**   | - Build internal tools to monitor or self-heal <br> - Improve log collection, traceability (e.g., ELK, Loki, Jaeger) |

---

## 🧰 Common Tools SREs Use

* **Monitoring**: Prometheus, Grafana, Datadog, CloudWatch
* **Incident Management**: PagerDuty, Opsgenie, Slack
* **Infra-as-Code**: Terraform, Ansible, Pulumi
* **Containers/Orchestration**: Docker, Kubernetes, Helm
* **CI/CD**: Jenkins, GitHub Actions, ArgoCD
* **Logging/Tracing**: ELK Stack, Loki, Jaeger, Zipkin
* **Scripting**: Python, Bash, Go

---

## 🎯 SRE Goals

* Keep systems **available** (meet SLAs)
* Reduce **manual toil** through automation
* Improve **mean time to recovery (MTTR)**
* Ensure systems can **scale** reliably
* Share **postmortems and learnings** openly

---
