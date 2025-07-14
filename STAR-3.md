Situation:

“At VMware, I was handling a critical escalation for a Fortune 500 client who was running a multi-site SDN environment using NSX-T and HCX to connect on-prem to VMware Cloud on AWS. 

They were facing frequent packet drops and intermittent downtime after a bulk VM migration.”

⸻

🛠 Task:

“The client was losing confidence due to ongoing impact. Leadership escalated the case, and 
I was tasked with owning the issue end-to-end and restoring platform stability while coordinating across engineering, cloud, and support teams.”

⸻

⚙ Action:
	•	Conducted deep packet analysis using Wireshark on interconnects and found MTU mismatches across the NSX-T edge path.
 
	•	Discovered a misconfigured DF bit and Path MTU discovery failure on intermediate appliances.
 
	•	Correlated NSX-T logs, HCX metrics, and BGP peer state across regions to isolate the issue.
 
	•	Led multiple war-room calls with VMware Engineering, AWS support, and the customer’s network/security team.
 
	•	Proposed a custom workaround to adjust MTU + DF bit handling and requested a patch fix from NSX engineering.

⸻

✅ Result:

“We restored full service availability within 48 hours, documented a global advisory for similar environments, and the customer upgraded their support tier due to confidence in our resolution.

Personally, this gave me deep exposure to cloud path MTU handling, cross-team coordination, and reinforced the importance of observability in hybrid networks.”
