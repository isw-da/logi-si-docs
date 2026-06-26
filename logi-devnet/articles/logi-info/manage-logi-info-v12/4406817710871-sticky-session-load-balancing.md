---
title: "Sticky Session Load Balancing"
id: 4406817710871
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817710871-Sticky-Session-Load-Balancing
updated_at: 2022-04-06T06:10:40Z
---

# Sticky Session Load Balancing

# Sticky Session Load Balancing

In a load balanced environment with multiple servers, Logi Info establishes sessions based on server availability, and the assigned server handles all subsequent requests. This is called using *session affinity* or "sticky" sessions. Logi Info requires resource consolidation to work in a multi-server deployment.

To deploy a sticky environment, follow these steps:

1. Configure Load Balancer to be set to sticky (session affinity)
2. Prepare environment for centralization of resources (see [Application Resource Centralization](https://devnet.logianalytics.com/hc/en-us/articles/4406817707543-Application-Resource-Centralization#Addition))
3. Configure Logi Info application
4. Deploy application to all web servers
