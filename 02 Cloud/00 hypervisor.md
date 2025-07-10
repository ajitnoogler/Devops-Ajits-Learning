### 🧱 What is a Hypervisor? (Type 1 vs Type 2 Explained)

---

### 🧠 What is a Hypervisor?

A **hypervisor** is software or firmware that creates and runs **virtual machines (VMs)**. It allows multiple operating systems to share a single physical host by abstracting and allocating the hardware resources (CPU, memory, storage, etc.) to each VM.

Each VM runs its own OS and applications as if it were a separate physical machine.

---

### 🧩 Types of Hypervisors

---

### 🔹 Type 1 Hypervisor (Bare-Metal)

A **Type 1 hypervisor** runs directly on the physical hardware (bare metal). It does not require a host OS. It’s typically used in **enterprise data centers** for performance, security, and scalability.

#### ✅ Examples:
- VMware ESXi
- Microsoft Hyper-V (in server mode)
- KVM (when used on bare metal)
- Oracle VM Server
- Xen Hypervisor

#### 📌 Use Cases:
- Cloud infrastructure (OCI, AWS EC2, Azure)
- Production virtualization in data centers
- High-performance, secure VM environments

---

### 🔹 Type 2 Hypervisor (Hosted)

A **Type 2 hypervisor** runs **on top of a host operating system**. It's more user-friendly but adds overhead because the hypervisor shares system resources with the host OS.

#### ✅ Examples:
- Oracle VirtualBox
- VMware Workstation / Fusion
- Parallels Desktop (Mac)
- QEMU (when run in user mode)

#### 📌 Use Cases:
- Local development and testing
- Desktop virtualization
- Learning labs (GNS3, penetration testing VMs)

---

## 🔁 Type 1 vs Type 2 – Comparison Table

| Feature               | Type 1 (Bare-Metal)        | Type 2 (Hosted)             |
|------------------------|-----------------------------|-----------------------------|
| Runs on               | Hardware directly            | Host operating system       |
| Performance           | ✅ High                       | ❌ Lower (more overhead)     |
| Stability             | ✅ More stable                | ❌ Depends on host OS        |
| Use Case              | Enterprise / Cloud / Servers | Desktops / Labs / Testing   |
| Examples              | VMware ESXi, KVM, Xen        | VirtualBox, VMware Workstation |
| OS Dependency         | ❌ No (standalone)            | ✅ Yes (needs host OS)       |
| Ideal for             | Production / HA / DR         | Dev/Test / Personal use     |

---

## 📌 Summary

- A **hypervisor** lets you run multiple VMs on a single physical machine.
- **Type 1** is enterprise-grade and runs directly on the hardware.
- **Type 2** is easy to use for personal or dev/test environments but runs on top of an OS.

---
