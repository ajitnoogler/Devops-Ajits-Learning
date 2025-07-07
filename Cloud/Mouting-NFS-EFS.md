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

---

## ☁️ AWS (Amazon Web Services)

### 📦 Amazon EFS (Elastic File System)

#### 🔧 Install Amazon EFS helper

```bash
sudo yum install -y amazon-efs-utils      # Amazon Linux 2 / RHEL
sudo apt install -y amazon-efs-utils      # Ubuntu/Debian
```

#### 📌 Mount using EFS helper (preferred for TLS)

```bash
sudo mount -t efs -o tls <EFS_FS_ID>:/ /mnt/efs
```

#### 📌 Mount using NFS directly

```bash
sudo mount -t nfs4 -o nfsvers=4.1 <EFS_FS_ID>.efs.<region>.amazonaws.com:/ /mnt/efs
```

#### 📘 Example:

```bash
sudo mount -t efs -o tls fs-12345678:/ /mnt/efs
```

---

## ☁️ Azure (Microsoft Azure)

### 📦 Azure Files (SMB)

```bash
sudo apt install cifs-utils       # Debian/Ubuntu
sudo yum install cifs-utils       # RHEL/CentOS
```

#### 📌 Mount Azure Files (SMB/CIFS)

```bash
sudo mount -t cifs //<storage_account>.file.core.windows.net/<share_name> /mnt/azfiles \
  -o vers=3.0,username=<storage_account>,password=<account_key>,dir_mode=0777,file_mode=0777,serverino
```

#### 📦 Azure NetApp Files (NFS)

```bash
sudo mount -t nfs <NetApp_IP>:/<export_path> /mnt/anf
```

---

## ☁️ GCP (Google Cloud Platform)

### 📦 Filestore (NFS)

#### 📌 Mount GCP Filestore (NFSv3 or v4)

```bash
sudo mount -t nfs <filestore_ip>:/<share_name> /mnt/filestore
```

#### 📘 Example:

```bash
sudo mount -t nfs 10.240.0.10:/vol1 /mnt/gcpfilestore
```

---

## ☁️ OCI (Oracle Cloud Infrastructure)

### 📦 OCI File Storage (NFS)

#### 📌 Mount OCI File Storage (NFS v3)

```bash
sudo mount -t nfs -o vers=3,tcp,noresvport <mount_target_ip>:/<export_path> /mnt/oci
```

#### 📘 Example:

```bash
sudo mount -t nfs -o vers=3,tcp,noresvport 10.0.0.20:/myfs /mnt/oci
```

#### 📌 Mount via `/etc/fstab`

```
<mount_target_ip>:/myfs  /mnt/oci  nfs  defaults,_netdev  0  0
```

---

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

### 🛠️ Tips

* Always test mounts manually before adding to `/etc/fstab`.
* For **auto-mount**, ensure NFS service is installed and running.
* Add `_netdev` in fstab to avoid boot-time errors due to missing network.

Would you like an Ansible playbook or shell script to automate NFS/EFS mount per cloud?
