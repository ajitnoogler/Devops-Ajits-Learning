# 1. Parent “my_app” (PID 1000) starts a child “worker”:

   my_app (1000)
       │ fork()
       ▼
   worker (1001)

# 2. “worker” finishes and exits, but parent hasn’t waited yet → becomes a zombie: Z means Zombie -- <defunct> means the process is dead but not yet cleaned up

   my_app (1000)
       │
       ├─ worker (1001) [<defunct>]   ← zombie: exit status held -- ps aux | grep defunct -- output -- " root     2501  0.0  0.0  0     0 ?     Z    10:30   0:00 [httpd] <defunct> " 
       │         CMD=worker
       │         STAT=Z

# 3. Parent calls wait() (or is killed) → “worker” is reaped and removed:

   my_app (1000)
       │ wait()
       ▼
   (no more entry for 1001; PID freed)

—or if “my_app” crashes——

   my_app (1000) ✖
       │
   init (1) adopts and reaps:
       └─ worker (1001) [<defunct>] → cleaned up

==============================================================================================================

# Key points in this example for Zombie process:

    “worker” is the child process that does some task.

    Once it exits, it shows up as <defunct> with STAT = Z in ps.

    Calling wait() in the parent (“my_app”) or killing the parent lets init (PID 1) remove the zombie entry.

| Feature      | Explanation                      |
| ------------ | -------------------------------- |
| Uses CPU?    | ❌ No                             |
| Uses memory? | ❌ Almost none                    |
| Dangerous?   | ❌ One or two is fine             |
| Problem?     | ✅ Too many can exhaust PID table |

🧟‍♂️ A zombie process = dead but not buried.
🪦 A process grave waiting for cleanup!

===============================================================================================================

# 🧟 What is a Zombie Process?

A zombie process is a dead process that is still listed in the system.

Imagine a child process finishes its work and dies, but its parent doesn’t notice it.

So the system keeps a small "note" (called an exit status) about the dead child, waiting for the parent to come and "pick it up".

Until that happens, the process stays in the process table as a zombie.


# 🧠 Why it happens:

    A parent process (like httpd, bash, or python) creates a child.

    The child finishes and exits.

    The system waits for the parent to call wait() and clean it up.

    If the parent forgets, the zombie stays in the process list.