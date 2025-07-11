
````markdown
# 🧬 How to Identify an Application Memory Leak in Linux

A memory leak occurs when an application keeps allocating memory but fails to release it,
causing RAM usage to grow over time — eventually leading to slowdowns, swapping, or OOM (Out-Of-Memory) kills.

OOM (Out-Of-Memory) Kill is a Linux kernel mechanism that activates when the system runs out of available RAM and can't free up enough memory.  
To prevent a total system crash, the kernel forcibly terminates one or more processes — usually the one consuming the most memory.
---

## 🔍 Symptoms of a Memory Leak

| ⚠️ Symptom                     | 💡 Description                                                   |
|-------------------------------|--------------------------------------------------------------------|
| 🚀 Gradual increase in `%MEM` | Process uses more RAM over time without freeing it                 |
| 🧊 App becomes sluggish        | Garbage collector pauses (in Java/Python), delayed response       |
| 💥 OOM kills                   | Kernel kills the app when memory exhausts                         |
| 💾 High swap usage            | System starts swapping due to memory pressure                      |
| 🕒 Restart fixes it temporarily| Memory resets after process restarts (but issue comes back later) |


#### 🧬 Summary: How to Identify an Application Memory Leak in Linux

| 🔢 Step | 🔍 What to Check                        | 🛠️ Tool/Command Example                                        | 📌 Key Indicator                                     |
|--------|----------------------------------------|----------------------------------------------------------------|----------------------------------------------------------|
| 1️⃣     | Monitor memory usage over time         | `watch "ps -eo pid,comm,%mem --sort=-%mem | head"`            | `%MEM` keeps increasing for the same process             |
| 2️⃣     | Check actual resident memory (RSS)     | `smem -r -k | sort -k 4 -nr | head`                         | RSS keeps growing even when app is idle                    |
| 3️⃣     | Verify swap activity                   | `free -m` or `vmstat 1 5`                                      | High swap usage despite low available RAM               |
| 4️⃣     | Check for OOM (Out Of Memory) kills     | `dmesg | grep -i 'killed process'` or `journalctl -k | grep -i oom` | OOM killer logs show app being terminated         |
| 5️⃣     | Use language-specific leak tools       | `valgrind`, `tracemalloc`, `objgraph`, `jmap`, `jvisualvm`    | Reports of unreleased memory or growing object counts    |

> ✅ A memory leak is confirmed when memory usage grows continuously and is not reclaimed even under idle conditions.


#### 🛠️ Steps to Detect a Memory Leak

#### 🔁 1. **Monitor Memory Over Time**

Use `top` or `ps` to track memory growth.

```bash
watch -n 5 "ps -eo pid,comm,%mem,%cpu --sort=-%mem | head"
````

#### 📋 Sample Output (After 1 Hour):

```
PID   COMMAND  %MEM  %CPU
1234  python   3.0   2.5
1234  python   7.5   4.1
1234  python   14.3  5.2
```

> 📌 Memory keeps growing even with similar usage → suspicious of leak.

---

#### 🧠 2. **Use `smem` to Track Real RSS Usage**

```bash
smem -r -k | sort -k 4 -nr | head
```

Shows actual memory mapped and used by processes.

---

#### 🧪 3. **Check for Swap Usage**

```bash
free -m
vmstat 1 5
```

Sample `free -m` output:

```
Swap:       2048     1800      248
```

> 📌 High swap + growing app memory = memory pressure.

---

#### 🧼 4. **Check for OOM Kill History**

```bash
dmesg | grep -i 'killed process'
journalctl -k | grep -i oom
```

> 📌 Confirms memory exhaustion events in past.

---

#### 🔍 5. **Use Tools for Deeper Leak Detection**

| Tool                               | Language | Purpose                          |
| ---------------------------------- | -------- | -------------------------------- |
| `valgrind --leak-check=full ./app` | C/C++    | Finds exact malloc/free issues   |
| `tracemalloc` (Python)             | Python   | Traces memory allocation by line |
| `memory_profiler`, `objgraph`      | Python   | Tracks object count over time    |
| `jmap`, `jvisualvm`                | Java     | Heap dump & GC info              |
| `massif`, `heaptrack`              | C/C++    | Memory usage profiling           |

---

#### ✅ How to Confirm It's a Leak (Checklist)

* [x] Memory grows with usage, doesn't drop
* [x] Restart resets memory usage
* [x] GC logs show minimal collection (for Java/Python)
* [x] No file caches or kernel buffers involved
* [x] Tools like `valgrind` or `tracemalloc` confirm retained allocations

---

#### 🧼 What a Healthy App Looks Like

* Memory grows briefly under load, then stabilizes
* `ps` and `top` show consistent %MEM over time
* Swap usage is low or zero
* No OOM messages in logs

---
