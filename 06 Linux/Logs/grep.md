### grep: Search and Filter Text with Regex

#### Description:
- grep is the most widely used command for searching text patterns in files or command output using regular expressions. 
- It is indispensable for log analysis, troubleshooting, and automation.

#### Common Use Cases:

Log Analysis: Search for errors, warnings, or specific events in system or application logs.

Example: grep -i "error\|warning" /var/log/messages

Filtering Output: Extract lines matching a pattern from command output.

Example: ps aux | grep "java"

Counting Matches: Count how many times a pattern appears.

Example: grep -c "404" /var/log/nginx/access.log

Case-Insensitive Search: Ignore case while searching.

Example: grep -i "failed" /var/log/auth.log

Recursive Search: Search across all files in a directory and subdirectories.

Example: grep -r "pattern" /etc/

Invert Match: Show lines that do NOT match a pattern.

Example: grep -v "^#" /etc/fstab

### Most Important Use Case:
Log Analysis and Troubleshooting:

- Searching for specific error messages, failed login attempts, or security events in log files is the most critical use case. 
- It allows administrators to quickly identify issues and respond to incidents.​

### VMware Specific Commands

#### Find all error or warning messages across VMware logs:
grep -Ei 'error|warning|fail|critical' /var/log/vmware/*.log

#### Search for specific disk or storage IO errors in vmkernel.log:
grep -E 'Disk I/O error|NMP path change|SCSI failure' /var/log/vmkernel.log
This targets known storage-related problem messages important for troubleshooting.

#### Extract IP addresses involved in connections or errors from vCenter/ESXi logs:
grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' /var/log/vmware/hostd.log | sort | uniq
This extracts unique IPv4 addresses for auditing network activity.

#### Search for VM power-on or power-off events in vmware.log:
grep -E 'PowerOn|PowerOff' /vmfs/volumes/datastore_name/vm_name/vmware.log

#### Filter for authentication audit events (successful and failed logins):
grep -Ei 'authentication failure|login.*success' /var/log/vmware/*.log



