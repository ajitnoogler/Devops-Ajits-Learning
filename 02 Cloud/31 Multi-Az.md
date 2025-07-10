Multi-AZ EC2 + RDS (Read Replicas / Aurora Global DB)
🧠 What It Does:

    Multi-AZ EC2: Deploy web/app servers in at least 2 Availability Zones (AZs) for high availability.

    Multi-AZ RDS: Automatically replicates DB to a standby instance in another AZ.

    Aurora Global DB: Multi-region write + read replication. Near-zero failover time.

📦 Use Case:

A web app runs in 2 AZs with EC2.

    DB is in RDS (Multi-AZ) – if the master fails, it auto-fails over to the standby.

    For global scale, use Aurora Global DB to serve US and Europe with read replicas.

🔧 Configuration Example:

# EC2 in Auto Scaling Group across AZs
Launch Template → Auto Scaling Group → 2 AZs

# RDS:
- Primary in us-east-1a
- Standby in us-east-1b (automatic failover)
