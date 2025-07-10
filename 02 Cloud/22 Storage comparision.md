# Cloud Storage Comparison Table (AWS vs OCI)

| **Storage Type**   | **Purpose**                                    | **Key Characteristics**                                                                   | **common use-cases**
| ------------------ | ---------------------------------------------- |-------------------------------------------------------------------------------------------|--------------------------------------------------|
| **Object Storage** | Store unstructured data S3(e.g. media, logs)   | - Access via HTTP(S) API<br>- Not mountable<br>- Key-based access<br>- Highly durable     | - Static websites<br>- Logs & backups<br>- Media storage<br>- App uploads   |
| **Block Storage**  | EBS Persistent storage for VMs and databases   | - Mountable to VMs<br>- Acts like a disk<br>- High IOPS<br>- Used for root/app volumes    | - OS boot disk<br>- Databases (PostgreSQL, Oracle)<br>- Application data    |
| **File Storage**   | Shared file system over NFS/SMB EFS FSx        | - NFS/SMB protocol<br>- Mountable on multiple VMs<br>- Shared access<br>- POSIX-compliant | - Shared workspace<br>- Lift-and-shift apps<br>- Media processing pipelines |

# Recommendations

| Requirement                              | Suggested Storage Type    |
| ---------------------------------------- | ------------------------- |
| Store images/logs/media                  | Object Storage (S3 / OCI) |
| VM boot disk or Oracle DB                | Block Storage             |
| Shared file system (multi-VM access)     | File Storage              |
| Archival of old compliance data          | Archive Storage           |
| Transfer 100TB+ of on-prem data to cloud | Data Transfer Appliance   |


🔍 Feature Summary

| Feature            | **Object**   | **Block**     | **File**    | **Archive**       | **Data Transfer**     |
| ------------------ | ------------ | ------------- | ----------- | ----------------- | --------------------- |
| Access Type        | API (HTTP/S) | Mount (disk)  | NFS/SMB     | API (Delayed)     | CLI / Physical Device |
| Example File Types | Logs, Media  | DB Files, OS  | Shared Docs | Long-term backups | Any                   |
| Latency            | Medium       | Low (Fast)    | Medium      | High              | Depends               |
| Cost               | Low          | Medium        | Medium      | Very Low          | One-time or metered   |
| Durability         | 11 9’s       | 99.99–99.999% | 99.9–99.99% | 11 9’s            | n/a                   |
