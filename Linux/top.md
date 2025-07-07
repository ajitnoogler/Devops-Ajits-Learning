



To interpret Load Average, you need to understand what those three numbers mean in context with your system’s CPU core count.

# What are the 3 numbers?
These are the system load averages over:

load average: 0.75, 1.20, 0.90
                ↑     ↑     ↑
            1 min  5 min  15 min

==================================================

If your system has 4 cores:

    A load average of 4.00 means fully utilized
    A load average of 2.00 means 50% usage
    A load average of 6.00 means overloaded (some processes are waiting)

=========================================================================

🚦 Quick judgment guide:

| Load Avg (1m) | CPU Cores                                | Interpretation |
| ------------- | ---------------------------------------- | -------------- |
| ≤ CPU cores   | Balanced/Healthy load                    |                |
| > CPU cores   | Overloaded (processes waiting)           |                |
| >> CPU cores  | Heavily overloaded, potential bottleneck |much greater than|
| ≈ 0.00        | Very idle (may be underutilized)         |                |


✅ Examples:

Example 1:

Load average: 1.50, 1.20, 0.90   # On a 4-core CPU

    System is running well
    All 4 cores are not fully loaded (below 4.00).
    Load has slightly increased over the last 15 minutes.

Example 2:

Load average: 6.00, 5.50, 4.50   # On a 2-core CPU

    System is heavily overloaded.
    Processes are waiting for CPU.
    Might cause performance degradation.