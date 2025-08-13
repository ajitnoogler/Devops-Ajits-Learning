#### 🛠️ Cloud Support Ticket Handling Workflow (Oracle/AWS)

| **Step** | **Phase**                              | **Action**                                                                  | **Best Practices**                                                       |
| -------- | -------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 1        | **Ticket Intake**                      | Review new ticket: severity, customer impact, affected service              | Confirm urgency, SLA category, and completeness of issue details         |
| 2        | **Acknowledge and Communicate**        | Acknowledge customer within SLA time                                        | Set expectations clearly with next update time, ask clarifying questions |
| 3        | **Initial Triage**                     | Categorize issue (e.g., network, compute, storage, LB)                      | Use known error codes, logs, keywords to route faster                    |
| 4        | **Environment Validation**             | Confirm if issue is in AWS/OCI cloud infra, customer config, or third-party | Use tools like `OCI CLI`, `AWS CLI`, CloudShell, metrics dashboards      |
| 5        | **Reproduce / Simulate (if needed)**   | Recreate the issue in a test environment if reproducible                    | Helps confirm issue scope and eliminate external noise                   |
| 6        | **Data Collection**                    | Gather logs, metrics, resource IDs, route tables, security configs          | Use automation/scripts to collect relevant info faster                   |
| 7        | **Root Cause Analysis**                | Isolate the issue layer: DNS, VPC/Subnet, Route, NSG/SG, App                | Follow layered approach: DNS > Network > OS > App                        |
| 8        | **Apply Fix / Recommend Action**       | Fix issue or suggest config changes                                         | Use validated KB articles, approved scripts, or internal tooling         |
| 9        | **Validate with Customer**             | Confirm issue is resolved in customer’s environment                         | Ask customer to retest and confirm functionality                         |
| 10       | **Close with Summary**                 | Close ticket with RCA, steps taken, and prevention tips                     | Add KB reference, CLI commands used, and note if escalation needed       |
| 11       | **Postmortem & RCA (Major Incidents)** | For SEV-1/SEV-2 tickets, write internal RCA or postmortem                   | Identify gaps in monitoring, automation, process, or documentation       |
| 12       | **Knowledge Sharing**                  | Update internal KB, runbooks, or SOPs based on new findings                 | Prevent future recurrence and help teammates via docs or brown bags      |


#### 👩‍💻 Example Tools Used:

| **Cloud** | **Tools**                                                                  |
| --------- | -------------------------------------------------------------------------- |
| AWS       | AWS CLI, CloudWatch, VPC Reachability Analyzer, Flow Logs, Trusted Advisor |
| OCI       | OCI CLI, Logging service, VCN Flow Logs, Service Connector Hub, Monitoring |
