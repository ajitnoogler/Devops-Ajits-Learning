
#### How to Find the Cause of an Unexpected Shutdown on Windows 11

From Power-Shell (admin)

Get-WinEvent -FilterHashtable @{ LogName = 'System'; Id = 41, 1074, 6006, 6605, 6008; } | Format-List Id, LevelDisplayName, TimeCreated, Message


#### Windows Event Log Codes Table

| **Event ID** | **Log Source**             | **Meaning**                                   | **Common Causes**                           | **Recommended Actions**                                                         |
| ------------ | -------------------------- | --------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------- |
| **41**       | Kernel-Power               | System rebooted without clean shutdown        | Power loss, crash, hard reset, BSOD         | Check power supply, overheating, driver issues, run memory and disk diagnostics |
| **1074**     | USER32                     | Shutdown/restart initiated by user or process | Windows Update, admin shutdown, app restart | Check initiator details in log, review update settings                          |
| **6006**     | EventLog                   | Event Log service stopped (clean shutdown)    | Normal shutdown                             | Indicates graceful shutdown; no action needed                                   |
| **6008**     | EventLog                   | Previous shutdown was unexpected              | Crash, freeze, sudden power off             | Investigate logs before this time, check hardware and OS health                 |
| **6605**     | Microsoft-Windows-Eventlog | Event Log service successfully started        | System boot process                         | Normal log entry; usually follows startup                                       |

---

Diagnostic Tips:

    Use Event Viewer → Windows Logs → System to filter by these Event IDs.
    
    Use Reliability Monitor (perfmon /rel) for crash timeline.

    Check Minidump folder or use tools like BlueScreenView or WinDbg for BSOD analysis.
---

#### Windows **Event ID/code** you've listed—these are typically found in the **Event Viewer** under **System Logs** and help troubleshoot shutdowns, reboots, or power issues:

---

#### ✅ **Event ID 41 — Kernel-Power**

**Meaning:** The system has rebooted without cleanly shutting down first.

* **Cause:** System crash, power loss, pressing the reset/power button, overheating.
* **Common in:** Unexpected shutdowns (e.g., power failure or hardware issue).
* **Check for:**

  * PSU (Power Supply Unit) issues
  * Overheating (check CPU/GPU temps)
  * Memory issues (run `mdsched.exe`)
  * Drivers causing kernel panic (use `Driver Verifier`)

---

#### ✅ **Event ID 1074 — USER32**

**Meaning:** System shutdown/restart initiated by a user or process.

* **Details include:**

  * Who/what initiated shutdown (e.g., `svchost.exe`, `Windows Update`, `User`)
  * Reason for shutdown
* **Used for:** Graceful or scheduled reboots (e.g., `Windows Updates`, software installs).

---

#### ✅ **Event ID 6006 — EventLog**

**Meaning:** "The Event log service was stopped."

* **Indicates:** A **clean shutdown**.
* **Useful for:** Tracking when the system shuts down properly.
* Often paired with `6005`.

---

#### ✅ **Event ID 6605 — Microsoft-Windows-Eventlog**

**Meaning:** The Event Log service has **successfully started**.

* **Generally benign.** Part of startup.
* **May appear after improper shutdown recovery.**

---

#### ✅ **Event ID 6008 — EventLog**

**Meaning:** "The previous system shutdown at \[time] was unexpected."

* **Triggered by:** Crashes, power loss, BSODs.
* **Usually follows:** Event ID 41 (Kernel-Power).
* Use this to timestamp the unexpected shutdown.

---

#### 🔍 Summary Table:

| **Event ID** | **Meaning**                           | **Cause / Action**                          |
| ------------ | ------------------------------------- | ------------------------------------------- |
| 41           | Unexpected reboot (no clean shutdown) | Power issue, crash, freeze, hardware/driver |
| 1074         | Controlled shutdown by user/process   | Admin/user-initiated, Windows Updates       |
| 6006         | Event log service stopped (normal)    | Clean shutdown                              |
| 6008         | Unexpected shutdown                   | Crash, BSOD, power loss                     |
| 6605         | Event log service started             | Normal startup event                        |

---

#### 🔧 Recommendations:

1. **Check Event Viewer:** Look for errors before `Event ID 41` or `6008`.
2. **Run Diagnostics:**

   * `sfc /scannow` – System file check
   * `chkdsk /f /r` – Disk check
   * `memtest86` or `mdsched.exe` – RAM test
3. **Review Reliability Monitor:**

   * Type `Reliability Monitor` in Start → Gives a timeline of crashes.
4. **Disable Fast Startup:** Sometimes causes improper shutdowns.
5. **Update Drivers and BIOS.**
6. **Look at `C:\Windows\Minidump\`** – If BSOD occurred, analyze using `BlueScreenView` or WinDbg.
---
