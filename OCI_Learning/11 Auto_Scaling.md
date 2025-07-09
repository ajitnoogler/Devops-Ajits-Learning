

### Horizontal Scaling -  Add more instances (servers or nodes) to distribute the load.

   - Auto Scaling Group with 3 EC2 web servers behind an ALB
     
   - Amazon RDS Aurora with read replicas

### Vertical Scaling -  Increase the resources (CPU, RAM, IOPS) of a single instance or upgrade instance type

   - Resize EC2 instance from t3.small to c6i.4xlarge for compute-heavy task

   - RDS PostgreSQL upgraded from db.t3.medium to db.r6i.4xlarge

---

### 🔍 Summary

    - Horizontal scaling is better for high availability, distributed workloads, and cloud-native applications.

    - Vertical scaling is easier to implement but limited and often involves downtime.

---

### 📊 Comparison: Horizontal vs Vertical Scaling in AWS

| Feature                 | **Horizontal Scaling** (Scale Out/In)                        | **Vertical Scaling** (Scale Up/Down)                             |
| ----------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------- |
| **Definition**          | Add more instances/nodes to the system                       | Increase the size (CPU, RAM, etc.) of a single instance          |
| **How it works in AWS** | Add more EC2 instances behind a Load Balancer (Auto Scaling) | Change EC2 instance type to a more powerful one (e.g., t3 → m6i) |
| **Example**             | Add 3 EC2 web servers behind an ALB                          | Upgrade EC2 from `t3.medium` → `c7i.2xlarge`                     |
| **Scalability**         | High, near-infinite (e.g., AWS Auto Scaling Groups)          | Limited by the max size of a single instance                     |
| **Fault tolerance**     | High — if one instance fails, others take over               | Low — if one instance fails, whole service might go down         |
| **Cost**                | Can be cheaper for distributed loads                         | May become expensive quickly at higher sizes                     |
| **Performance gain**    | Improves throughput via parallelism                          | Improves performance on single-threaded workloads                |
| **Use Cases**           | Web servers, stateless microservices, distributed databases  | Single-threaded DBs, legacy apps, vertical-licensed software     |
| **AWS Services**        | EC2 Auto Scaling, ECS/Fargate, Lambda, RDS Aurora Cluster    | EC2 instance resizing, RDS instance class upgrade                |
| **Scaling Speed**       | Usually slower (provision time + warm-up)                    | Faster (restart instance with higher spec)                       |
| **Maintenance**         | Requires orchestration/load balancing (e.g., ALB/NLB)        | Simpler, but may require downtime for reboot                     |

---
---
