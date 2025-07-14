NSX-T Upgrade Broke East-West Routing

🟦 Situation:

During a planned NSX-T upgrade in a multi-VDI VMC environment, the customer reported that east-west traffic between certain internal VMs stopped immediately after the upgrade.

⸻

❌ What Went Wrong:
	•	I validated Tier-1 and Tier-0 Uplink status, BGP, and Edge node health—all looked green.
 
	•	I ignored Distributed Firewall (DFW) logging, assuming rules remained intact post-upgrade.
 
	•	Reality: A security tag in the DFW rule set was not preserved correctly after the upgrade due to a bug in tag replication between NSX Manager nodes.

⸻

🛠 Recovery:
	•	Reproduced the bug in a nested lab.
	•	Opened a high-priority bug escalation with NSX Engineering.
 
	•	Helped customer implement a workaround using static grouping.
 
	•	Documented upgrade pre-check scripts for similar customer environments.

⸻

✅ Lesson:

“It reminded me that routing isn’t always the problem, even if pings don’t pass. NSX-T is policy-driven, and DFW/Group tags can break silently. 
I now treat DFW validation as a core part of post-upgrade checklists.”
