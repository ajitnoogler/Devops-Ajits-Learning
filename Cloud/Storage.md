
🗄️ Storage & Data Transfer

| Service Area   | AWS                                           | OCI                                       |
| -------------- | --------------------------------------------- | ----------------------------------------- |
| Object Storage | S3 (including Glacier) ([docs.oracle.com][1]) | Object Storage, Archive Storage           |
| Block / File   | EBS, EFS                                      | Block Volumes, File Storage               |
| Data Transfer  | Snowball, Storage Gateway                     | Data Transfer Appliance, Storage Gateway  |

# Summary Table of Storage Services

| Storage Type    | AWS Service                         | OCI Service                          | Notes                                                    |
| --------------- | ----------------------------------- | ------------------------------------ | -------------------------------------------------------- |
| Object Storage  | S3, Glacier, Glacier Deep Archive   | Object Storage, Archive Storage      | OCI is cost-optimized, S3 has broader integrations       |
| Block Storage   | EBS                                 | Block Volumes                        | OCI supports dynamic performance adjustment              |
| File Storage    | EFS (Linux), FSx (Windows, Lustre)  | File Storage (NFS)                   | EFS is elastic; OCI better for traditional NFS workloads |
| Archive Storage | Glacier, Glacier Deep Archive       | Archive Storage                      | OCI offers lower-cost archival in many regions           |
| Data Transfer   | Snowball, DataSync, Transfer Family | Data Transfer Appliance, FastConnect | Similar capabilities, different naming                   |

🧠 Which One to Choose?

| Scenario                               | Recommended                             |
| -------------------------------------- | --------------------------------------- |
| Low-cost cold storage                  | ✅ **OCI Archive Storage**              |
| Dynamic scaling shared FS              | ✅ **AWS EFS**  / **OCI NFS**           |
| Enterprise-grade Oracle workloads      | ✅ **OCI Block / Object Storage**       |
| Complex S3 integrations (e.g., Athena) | ✅ **AWS S3**                           |
| Multicloud NFS sharing                 | ✅ **OCI File Storage + Mount Targets** |



# 1. OBJECT STORAGE - Both offer durable (11 9s), highly available storage. OCI is cost-optimized, while AWS S3 has a richer ecosystem.

| Feature                  | **AWS S3**                                                | **OCI Object Storage**                     |
| ------------------------ | --------------------------------------------------------- | ------------------------------------------ |
| Use Case                 | Store images, logs, backups, static content, big data     | Same use case                              |
| Access via               | REST API, AWS CLI, SDK, S3FS, IAM policies                | REST API, OCI CLI, SDK, FUSE, IAM policies |
| Tiers / Classes          | Standard, Intelligent-Tiering, Infrequent Access, Glacier | Standard, Infrequent Access, Archive       |
| Versioning               | ✅ Yes                                                     | ✅ Yes                                      |
| Lifecycle Policies       | ✅ Yes (automated tiering, expiry)                         | ✅ Yes                                      |
| Cross-region Replication | ✅ Yes                                                     | ✅ Yes                                      |
| Object Lock / WORM       | ✅ Yes (compliance mode)                                   | ✅ Yes (retention rules / governance mode)  |
| Cost Model               | Pay-per-use: GB stored + request count + egress           | Lower cost than S3, similar pricing model  |


# 2. BLOCK STORAGE - Both provide scalable, encrypted block storage. OCI offers dynamic performance tuning without detaching the disk, unlike AWS.

| Feature             | **AWS EBS (Elastic Block Store)**                  | **OCI Block Volumes**                                |
| ------------------- | -------------------------------------------------- | ---------------------------------------------------- |
| Use Case            | Persistent volumes for EC2 (VMs), DBs, filesystems | Persistent volumes for Compute Instances             |
| Volume Types        | gp3, gp2, io1/io2, st1, sc1                        | Balanced, Higher Performance, Ultra-High Performance |
| Max Size per Volume | 64 TiB                                             | 32 TiB per volume                                    |
| Encryption          | ✅ Default at rest                                  | ✅ Always encrypted at rest                           |
| Backups & Snapshots | ✅ Snapshots (EBS Snapshots)                        | ✅ Automatic / Manual Backups                         |
| Performance Scaling | ✅ Based on IOPS, throughput tier                   | ✅ Dynamic performance tuning                         |
| Multi-attach        | ✅ io1/io2 volumes (multi-AZ supported)             | ✅ Multi-attach supported                             |

# 3. FILE STORAGE - EFS is more elastic, while OCI’s File Storage is high-throughput and more manual in scaling, suited for enterprise NFS needs.

| Feature            | **AWS EFS / FSx**                               | **OCI File Storage Service**           |
| ------------------ | ----------------------------------------------- | -------------------------------------- |
| Use Case           | Shared filesystem for Linux VMs, NFS            | NFS v3/v4-based shared filesystem      |
| Protocol Support   | NFS (EFS), SMB (FSx for Windows)                | NFS v3/v4 only                         |
| Scalability        | EFS: scales automatically                       | Manual scaling / quota increase needed |
| Throughput Modes   | General Purpose, Max I/O (EFS)                  | Performance tiers (Standard, Higher)   |
| Multi-AZ/AD Access | ✅ Yes (EFS is regional)                         | ✅ Yes (across ADs in region)           |
| Encryption         | ✅ Yes (at rest & in transit)                    | ✅ Yes                                  |
| Mount Targets      | Region-level endpoints (EFS), VPC mount targets | Mount targets per subnet               |

# 4. ARCHIVE STORAGE - Both are cold storage, but OCI Archive Storage is often cheaper and integrates directly with standard object APIs.

| Feature          | **AWS Glacier / Glacier Deep Archive**            | **OCI Archive Storage**                          |
| ---------------- | ------------------------------------------------- | ------------------------------------------------ |
| Use Case         | Long-term, infrequently accessed backups and data | Same                                             |
| Retrieval Time   | Minutes to hours (Glacier), hours (Deep Archive)  | \~1–4 hours                                      |
| Cost             | Lowest AWS storage cost                           | Extremely low – cheaper than AWS in many regions |
| Write / Read API | S3 API                                            | Object Storage API                               |
| Use in Lifecycle | S3 lifecycle policies to move to Glacier          | OCI lifecycle rules to archive tier              |
