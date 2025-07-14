SSH Connections Dropping Randomly After 5 Minutes – TCP Idle Timeout

🟦 Situation:

Admins accessing Linux VMs in VMC noticed that idle SSH sessions dropped exactly after 300 seconds (5 mins).

🔍 Root Cause:

	•	NSX Edge firewall (northbound) had TCP idle timeout set to 300s
 
	•	On-prem jump host did not send keepalives
 
	•	Linux VMs had default SSHD ClientAliveInterval not set

🔧 Fix:
	•	Updated /etc/ssh/sshd_config:

ClientAliveInterval 60

ClientAliveCountMax 3

Restarted sshd, sessions stayed stable

✅ Lesson:

“TCP idle timeouts between NSX Edge and on-prem can kill SSH. Always tune SSH keepalives for hybrid admin workflows.”
