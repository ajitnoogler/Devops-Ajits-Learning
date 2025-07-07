# 1. Route 53 with Health Checks + Geolocation or Latency-Based Routing

🧠 What It Does:

    Route 53 is AWS's global DNS service.

    It can route users based on:

        Latency (fastest region for user),

        Geolocation (specific region for specific country),

        Health Checks (automatically avoids unhealthy endpoints).

📦 Use Case:

You have two regions: US-East and Singapore.

    US users → US-East ALB

    Asia users → Singapore ALB

    If Singapore region fails, traffic is automatically rerouted to US-East using health check failover.

🔧 Example Routing Policy:

US-East alias record:
- Type: A (Alias to ALB)
- Geolocation: North America
- Health Check: Enabled

Singapore alias record:
- Type: A (Alias to ALB)
- Geolocation: Asia
- Health Check: Enabled