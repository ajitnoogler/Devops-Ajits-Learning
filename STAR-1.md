 VMC Route Advertisement Broke Due to Route Limit in AWS TGW

🟦 Situation:

Large VMC customer advertised ~900 routes into AWS Transit Gateway (TGW) from NSX-T Tier-0 via BGP.

⸻

❌ What Went Wrong:
	•	AWS TGW route limit per VPC was 50 (soft limit) and silently dropped routes beyond that.
	•	Customer’s branch offices lost reachability to key subnets post-advertisement.
	•	I was unaware of AWS TGW limits and spent hours looking at BGP state, assuming route filters or NSX bugs.

⸻

🛠 Recovery:
	•	Escalated to AWS support and confirmed route table overflow.
	•	Split advertised routes into summarized blocks.
	•	Worked with AWS TAM to raise route limit.

⸻

✅ Lesson:

“Cloud platforms have invisible guardrails. 
You can’t assume BGP routes are accepted just because they’re advertised. Always validate route propagation in the cloud provider (in this case, AWS TGW CLI/API).”
