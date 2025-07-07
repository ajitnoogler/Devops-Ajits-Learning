**Linux commands** used to **mount file systems like NFS, EFS, and equivalents on AWS, Azure, GCP, and OCI**. It includes **required packages**, **mount commands**, and **cloud-specific notes**.

---

### 🗂️ General NFS Mount (Any Platform)

#### 🔧 Install NFS utilities (if not present)

```bash
sudo apt update && sudo apt install nfs-common -y     # Debian/Ubuntu
sudo yum install nfs-utils -y                          # RHEL/CentOS/Amazon Linux
```

#### 📌 Mount NFS manually

```bash
sudo mount -t nfs <NFS_SERVER_IP_OR_DNS>:/exported/path /mnt/mountpoint
```

#### 📘 Example:

```bash
sudo mount -t nfs 10.0.0.100:/data /mnt/data
```

#### 📌 Mount permanently via `/etc/fstab`

```
<NFS_SERVER_IP_OR_DNS>:/exported/path  /mnt/mountpoint  nfs  defaults,_netdev  0  0
```

### ✅ Summary Table

| Cloud | Service      | Type | Mount Example                                                                |
| ----- | ------------ | ---- | ---------------------------------------------------------------------------- |
| AWS   | EFS          | NFS  | `sudo mount -t efs -o tls fs-xxxx:/ /mnt/efs`                                |
| AWS   | EFS (manual) | NFS  | `sudo mount -t nfs4 -o nfsvers=4.1 fs-xxx.efs.<region>.amazonaws.com:/ /mnt` |
| Azure | Azure Files  | CIFS | `sudo mount -t cifs //<storage>.file...`                                     |
| Azure | NetApp Files | NFS  | `sudo mount -t nfs <ip>:/export /mnt/anf`                                    |
| GCP   | Filestore    | NFS  | `sudo mount -t nfs <filestore_ip>:/share /mnt`                               |
| OCI   | File Storage | NFS  | `sudo mount -t nfs -o vers=3... <ip>:/share /mnt`                            |

---
