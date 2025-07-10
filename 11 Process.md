
#### ✅ 1. What is Severity?

Severity (or "Sev") defines the impact level of a technical issue on the customer's business or services. 
It's crucial during triage because it determines how fast and how seriously the cloud provider responds.

---
#### ☁️ AWS Severity & SLA

| **Severity** | **Name**            | **Description**                                         | **Initial Response Time (SLA)**   |
| ------------ | ------------------- | ------------------------------------------------------- | --------------------------------- |
| **Sev 1**    | Business-Critical   | Production down or severely impacted. No workaround.    | < 15 minutes (Enterprise Support) |
| **Sev 2**    | Production Impaired | High impact issue; degradation of production services.  | < 1 hour                          |
| **Sev 3**    | System Impaired     | Moderate impact; production not significantly affected. | < 4 hours                         |
| **Sev 4**    | General Guidance    | Low impact; how-to or configuration guidance.           | < 24 hours                        |

#### 🧠 AWS allows customers to choose severity per ticket via AWS Support Center, based on real-time business impact.
---

#### ☁️ OCI Severity & SLA

| **Severity** | **Name** | **Description**                                      | **Initial Response Time (SLA)** |
| ------------ | -------- | ---------------------------------------------------- | ------------------------------- |
| **Sev 1**    | Critical | Full service outage or major impact, no workaround   | < 1 hour (for Paid Support)     |
| **Sev 2**    | High     | Service severely impaired; limited workaround exists | < 2 hours                       |
| **Sev 3**    | Medium   | Service moderately impaired; workaround available    | < 8 hours                       |
| **Sev 4**    | Low      | Minor issues or general usage questions              | < 24 hours                      |

#### 🧠 OCI assesses severity based on customer input and engineer validation, and may downgrade severity if impact is lower than claimed.

---

####  🎯 Key Differences Between AWS and OCI

| **Aspect**                   | **AWS**                               | **OCI**                              |
| ---------------------------- | ------------------------------------- | ------------------------------------ |
| **Sev 1 Response SLA**       | 15 min (Enterprise)                   | 1 hour                               |
| **Self-assignable Severity** | Yes, via Support Center               | Yes, but OCI may adjust              |
| **Support Plans Required**   | Developer, Business, Enterprise tiers | Paid Support SKU required            |
| **24/7 Sev 1 Support**       | Yes (Business & Enterprise tiers)     | Yes (Paid Support only)              |
| **Multi-channel Support**    | Web, phone, chat (based on plan)      | Web, phone (no live chat by default) |

---

#### 📌 Best Practices for Setting Severity

- Use high severity only for real outages (e.g., app down, VPN broken, LB not routing).

- Clearly state business impact in ticket description.

- Update severity if the issue is resolved or mitigated.

- Include logs, resource IDs, timestamps to help engineers respond faster.

---
