 # CloudWatch, Auto Scaling, Elastic Recovery

🧠 What It Does:

🔸 CloudWatch

    Monitors CPU, memory, network, disk, logs.

    Set alarms on thresholds (e.g., CPU > 80%).

🔸 Auto Scaling

    Dynamically adds/removes EC2 instances based on load.

    Helps handle traffic spikes or failures.

🔸 Elastic Recovery

    Automatically recovers EC2 from hardware failures.

    You can configure auto-reboot or replacement.

📦 Use Case:

    EC2 instance CPU > 80% → Auto Scaling adds more instances.

    EC2 instance fails → AWS Elastic Recovery replaces or restarts the instance.

    CloudWatch monitors logs and triggers alerts to Slack/SNS/email. Jira ticket can be created for manual intervention if needed.
