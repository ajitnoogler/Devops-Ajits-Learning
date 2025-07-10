
## Sample Commands

```bash
# File listing
ls -lah /var/log

# Copy website files recursively
cp -rv ~/projects/site /srv/www/

# Find and delete old core dumps
find / -type f -name 'core.*' -mtime +7 -exec rm -fv {} \;

# Stream logs and filter errors
tail -f /var/log/nginx/access.log | grep --line-buffered -i "error"

# Archive /opt/data into gzip tarball
tar czvf backup-$(date +%F).tar.gz /opt/data

# Sync code to remote server
rsync -avz --delete ./app/ deploy@10.0.0.5:/opt/app/

# Check open listening ports (numeric)
ss -tuln

# Create a new user and add to sudo group
useradd -m -s /bin/bash -G sudo devopsuser

# Install Docker on Ubuntu
sudo apt-get update && sudo apt-get install -y docker.io

# View last hour of syslog
journalctl -u syslog.service --since "1 hour ago" | less

# Launch EC2 instance via AWS CLI (example)
aws ec2 run-instances --image-id ami-0abcd1234efgh5678 --count 1 --instance-type t3.micro --key-name mykey --security-group-ids sg-0123456789abcdef0 --subnet-id subnet-6e7f829e
```

Use this sheet as a quick reference during daily operations, automation scripting, and troubleshooting in cloud‑native environments.
