 AWS WAF Blocking Access to Cloud vCenter During Specific Hours

🟦 Situation:

A VMC environment was accessed via onprem fronted by AWS WAF in security VPC. 

Users reported timeout or 403 errors when accessing vCenter only during 9 PM–12 AM IST, especially from a DevOps pipeline.

⸻

🛠 Root Cause Analysis:
	•	Used AWS CloudWatch + WAF logs to correlate access logs with time windows.
 
	•	Found a WAF rule matching against User-Agent + rate-limit rule being triggered during pipeline runs (CI/CD tool).

	•	WAF considered traffic suspicious due to:
 
	•	Frequent polling by CI jobs (every 5 sec)
 
	•	Non-browser user agents (curl, custom Python clients)
 
	•	WAF rule was applying a rate-based block for this traffic profile.

⸻

🔧 Fix Applied:
	•	Created a WAF exception rule for known DevOps IPs + relaxed rate-limits during CI pipeline windows.
 
	•	Whitelisted CI tool User-Agent string temporarily for /ui and /rest paths.

⸻

✅ Lesson Learned:

“Even infrastructure-facing portals like vCenter can be unintentionally blocked by cloud security automation (like WAF). 

It’s important to analyze behavioral rules and rate limits, especially when automation tools or monitoring probes are involved.”
