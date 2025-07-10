

# 🚀 Full Guide: Add or Resize Disk in OCI for Oracle Linux 

---

## 🧱 Scenario 1: Resize an Existing Disk (Boot or Block Volume)

1. Log in to the OCI Console. → *(Via browser: [https://cloud.oracle.com](https://cloud.oracle.com))*
2. Navigate to your compute instance. → *(Compute → Instances → \[Your Instance])*
3. Select the Boot Volume or Attached Block Volume. → *(Click “Boot Volume” or “Attached Block Volumes”)*
4. Edit the volume and increase its size. → *(Actions → Edit → Set new size → Save)*
5. Save changes. → *(Wait until the resize completes)*
6. SSH into the Oracle Linux instance. → `ssh opc@<public-ip>`
7. Check the current disk and partition layout. → `lsblk`
8. Install the required tool to resize the partition. → `sudo yum install cloud-utils-growpart -y`
9. Resize the partition to match the new disk size. → `sudo growpart /dev/sda 3`
10. Resize the filesystem to utilize the expanded partition.
      → For XFS: `sudo xfs_growfs /`
      → For ext4: `sudo resize2fs /dev/sda3`
11. Verify that the new space is available. → `df -h`

---

## ➕ Scenario 2: Add a New Block Volume (Additional Disk)

1. Create a new block volume in OCI. → *(Block Storage → Block Volumes → Create Block Volume)*
2. Choose availability domain and size. → *(Select AD same as instance, set size, click Create)*
3. Attach the volume to the instance. → *(Attach to instance → Paravirtualized mode → Attach)*
4. SSH into the Oracle Linux instance. → `ssh opc@<public-ip>`
5. Check that the new disk is visible. → `lsblk`
6. Create a partition on the new disk. → `sudo parted /dev/sdb --script mklabel gpt mkpart primary xfs 0% 100%`
7. Format the new partition. → `sudo mkfs.xfs /dev/sdb1`
8. Create a mount point. → `sudo mkdir /mnt/data`
9. Mount the new disk. → `sudo mount /dev/sdb1 /mnt/data`
10. Make the mount persistent. → `echo "/dev/sdb1 /mnt/data xfs defaults 0 0" | sudo tee -a /etc/fstab`
11. Verify the disk is mounted and usable. → `df -h` and `lsblk`

---

## 📋 Summary of Common Commands

| Command                      | Purpose                                 |
| ---------------------------- | --------------------------------------- |
| `lsblk`                      | List block devices and partitions       |
| `df -h`                      | View mounted filesystems and usage      |
| `growpart /dev/sdX N`        | Resize partition number N on device sdX |
| `xfs_growfs /mount`          | Grow XFS filesystem                     |
| `resize2fs /dev/sdXN`        | Grow ext4 filesystem                    |
| `mkfs.xfs /dev/sdXN`         | Format partition as XFS                 |
| `parted`                     | Disk partitioning tool                  |
| `mount /dev/sdXN /mnt/point` | Temporarily mount disk                  |
| `echo >> /etc/fstab`         | Make disk mount permanent               |

---

