
### ✅ Steps to Add a Shell Script in Crontab (All-in-One Format)

---

🔹 **Step 1: Create your shell script** – `nano /home/ajit/backup.sh`

🔹 **Step 2: Add content to the script** – paste below lines inside the file:

```bash
#!/bin/bash
echo "Backup started at $(date)" >> /home/ajit/backup.log
```

Save and exit (`Ctrl + O`, then `Enter`, then `Ctrl + X`).

---

🔹 **Step 3: Make the script executable** – `chmod +x /home/ajit/backup.sh`

---

🔹 **Step 4: Open crontab for editing** – `crontab -e`

---

🔹 **Step 5: Add cron job entry at the bottom** –
`30 2 * * * /home/ajit/backup.sh >> /home/ajit/backup.log 2>&1`

(This runs the script daily at **2:30 AM**, logging output.)

---

🔹 **Step 6: Save and exit crontab** – (in nano: `Ctrl + O`, `Enter`, then `Ctrl + X`)

---

🔹 **Step 7: Verify the crontab entry is added** – `crontab -l`

**Sample Output:**

```
30 2 * * * /home/ajit/backup.sh >> /home/ajit/backup.log 2>&1
```

---

🔹 **Step 8: Check log after execution (or test manually)** – `cat /home/ajit/backup.log`

**Sample Output:**

```
Backup started at Tue Jul  9 02:30:01 IST 2025
```

---

🔹 **Optional: Test the script now** – `bash /home/ajit/backup.sh`

🔹 **Optional: View latest log output** – `tail /home/ajit/backup.log`



## 🕒 Cron Timing Examples (Modify Step 5 Accordingly)

---

### ✅ 1. Run **every minute**

```bash
* * * * * /home/ajit/backup.sh >> /home/ajit/backup.log 2>&1
```

---

### ✅ 2. Run **every 5 minutes**

```bash
*/5 * * * * /home/ajit/backup.sh >> /home/ajit/backup.log 2>&1
```

---

### ✅ 3. Run **every day at 2:30 AM** (original example)

```bash
30 2 * * * /home/ajit/backup.sh >> /home/ajit/backup.log 2>&1
```

---

### ✅ 4. Run **every Monday at 6:00 AM**

```bash
0 6 * * 1 /home/ajit/backup.sh >> /home/ajit/backup.log 2>&1
```

---

### ✅ 5. Run **on reboot/startup**

*(Note: `@reboot` only works for non-root users with cron properly configured)*

```bash
@reboot /home/ajit/backup.sh >> /home/ajit/backup.log 2>&1
```

---

### ✅ 6. Run **on the 1st of every month at midnight**

```bash
0 0 1 * * /home/ajit/backup.sh >> /home/ajit/backup.log 2>&1
```

---

## ℹ️ To Use These:

Replace **Step 5** from earlier:

> Add cron job entry at the bottom –
> `30 2 * * * /home/ajit/backup.sh >> /home/ajit/backup.log 2>&1`

With whichever cron timing format fits your use case.

---
