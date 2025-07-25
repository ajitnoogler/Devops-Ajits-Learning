#### What happens in Linux from CPU Memory IO and Network perspective
#### When user try to access http://webapp 

| 🔢 Step | 📝 Description                                         | 🖥️ CPU                                    | 💾 Memory                          | 💽 Disk I/O                   | 🌐 Network              |
| ------- | ------------------------------------------------------ | ------------------------------------------ | ---------------------------------- | ----------------------------- | ----------------------- |
| 1       | **HTTP request received via NIC**                      | Interrupt handling, TCP/IP stack (softirq) | Socket buffer allocation           | –                             | RX Queue receives data  |
| 2       | **Web server handles request (Nginx, Apache)**         | Parses headers, spawns/fork workers        | Request object buffers             | Read static files, log writes | –                       |
| 3       | **Backend app processes logic (e.g., Flask, Node.js)** | Executes code, templating, API calls       | Allocates session/response buffers | Access config files, logs     | Internal API/DB calls   |
| 4       | **Database query executed (if needed)**                | Query execution and index scans            | Buffer pool, temp results          | Read/write data/index files   | –                       |
| 5       | **Response sent back to user**                         | Kernel copies response to socket           | Response content buffers           | –                             | TX Queue transmits data |

---

#### 🧭 Sequence of Resource Activation

# 🌐 HTTP Request: Linux Resource Activation Sequence

When a user accesses a web app via HTTP, the Linux system activates resources in the following order:

| ⏱️ Order | 💡 Resource     | 🔁 Why It’s Triggered                                                 | 🧠 Example                                             |
|----------|------------------|------------------------------------------------------------------------|--------------------------------------------------------|
| 1st      | 🌐 Network        | Request arrives via NIC → triggers a hardware interrupt                | Packet from browser hits server on port 80/443         |
| 2nd      | 🖥️ CPU           | CPU handles interrupt → runs softirq → TCP/IP stack → socket           | Kernel processes packet, passes to Nginx/Apache        |
| 3rd      | 💾 Memory         | Buffers request, allocates memory for HTTP parsing and session data    | Store headers, cookies, app variables in RAM           |
| 4th      | 💽 Disk I/O (optional) | Access disk if static files, DB queries, or logs are involved        | Read HTML files, write logs, or fetch DB records       |
| 5th      | 💾 Memory         | Allocates memory to build the HTTP response                            | Store JSON/HTML response before sending                |
| 6th      | 🌐 Network        | Response is sent out via NIC (TX queue)                                | Web server writes to socket → packets go to user       |
| 7th      | 🖥️ CPU           | Post-processing and preparing for next request                         | Frees memory, handles next connection                  |

---

## ✅ Summary Flow:

**🌐 Network** → **🖥️ CPU** → **💾 Memory** → **💽 Disk I/O (if needed)** → **💾 Memory (response)** → **🌐 Network (send)** → **🖥️ CPU (wrap up)**

---

#### ⚡ What is an Interrupt (in Linux or any OS)?

An interrupt is a signal sent to the CPU by hardware or software indicating that something needs immediate attention.

#### 🧠 Think of it Like:

    📬 "Hey CPU, stop what you're doing and check this out!"

#### Types of Interupt:
| Type                   | Description                                     | Example                                 |
| ---------------------- | ----------------------------------------------- | --------------------------------------- |
| **Hardware Interrupt** | Sent by physical devices (NIC, keyboard, disk)  | New packet arrives on NIC, key pressed  |
| **Software Interrupt** | Generated by programs to request kernel service | System calls like `read()`, `write()`   |
| **Timer Interrupt**    | Periodic signal from system timer               | Used for time-slicing between processes |

---

####  1. Interrupt Handling

    What: Hardware (like NIC or disk) sends a signal (interrupt) to the CPU when it needs attention — e.g., new network packet arrived.

    Example: When a user sends an HTTP request, the NIC triggers an interrupt to let the CPU know, "Data received!"

#### 2. TCP/IP Stack (softirq)

    What: The Linux kernel processes network packets using a lightweight mechanism called softirq (software interrupt).

    Why: Fast processing of things like packet routing, acknowledgment, and TCP state tracking without full context switches.

    Example: After interrupt, the packet is processed (e.g., parsed for IP address, port, TCP flags) before being handed to the web server process.

#### 3. Socket Buffer Allocation

    What: Temporary memory where incoming/outgoing network data is stored in the kernel (part of a socket).

    Types:

        Receive buffer (recv): Holds incoming data

        Send buffer (send): Holds data to be sent out

    Example: When a request comes in, it sits in the socket receive buffer until the server reads it.

#### 4. Response Buffer

    What: Memory where the web server or backend stores the HTTP response before sending it out.

    Example: App builds HTTP/1.1 200 OK\nContent-Type: text/html..., stores in buffer, then writes to socket for sending.

#### 5. Buffer Pool (Database Term)

    What: RAM area used by databases (like MySQL/PostgreSQL) to cache frequently accessed data and indexes.

    Why: Avoid slow disk reads by keeping hot data in memory.

    Example: Query for a product list? The database might fetch it from the buffer pool instead of reading from disk.

---

#### Visual Analogy:

| 🧠 **Tech Term**    | 🇮🇳 **Indian Analogy**                                                                                                                                                |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Interrupt**       | 🔔 *Doorbell rings* — The **watchman (security guard)** or **Swiggy delivery guy** rings the bell to notify someone is at the gate.                                    |
| **softirq**         | 🧑‍🍳 *Househelp or assistant* quickly checks who's at the door, notes it's just the milkman, and lets the main person (CPU) know without causing too much disruption. |
| **Socket buffer**   | 📥 *Letterbox outside your flat* — Incoming letters (packets) are dropped here by the postman (NIC), waiting to be read.                                               |
| **Response buffer** | 📤 *Out-tray near the front door* — Replies or documents (responses) are kept here to be picked up by the courier (TCP/IP).                                            |
| **Buffer pool**     | 📚 *Bookshelf in your drawing room* — Frequently used books (data) are stored here for quick access, instead of walking to the archive room (disk).                    |
