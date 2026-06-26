---
title: "Load Balancing Configuration"
id: 4406817708567
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817708567-Load-Balancing-Configuration
updated_at: 2022-04-06T06:07:44Z
---

# Load Balancing Configuration

# Load Balancing Configuration

**Load balancing** is a technique used to distribute workload evenly across two or more web servers in order to optimize resource utilization, maximize throughput, minimize response time, and avoid overload. This topic discusses the configuration requirements for using Logi applications in load-balanced .NET and Java environments. If you need information about sizing, see [System Requirements - Logi Info](https://devnet.logianalytics.com/hc/en-us/articles/4406822529559-System-Requirements-Logi-Info).

The following topics discuss processes that you will use for two types of load balancing scenarios, sticky, and non-sticky:

* [Sticky Session Load Balancing](https://devnet.logianalytics.com/hc/en-us/articles/4406817710871-Sticky-Session-Load-Balancing#Load "Select to learn more about load balancing in a sticky session.")
* [Non-Sticky Session Load Balancing](https://devnet.logianalytics.com/hc/en-us/articles/4406817709847-Non-sticky-Session-Load-Balancing#Load2)
* [Application Resource Centralization](https://devnet.logianalytics.com/hc/en-us/articles/4406817707543-Application-Resource-Centralization#Addition "This process covers both types of load balancing.")

## About Load Balancing

In a standard environment, with one server, Logi Info establishes a session with the first HTTP request. That same server handles all subsequent requests. You can use multiple web servers in a "server pool" and control them using load balancing management software. This software monitors the port where external client browsers connect to access
services, and distributes requests among the available servers. Replies may be routed back through the management software, hiding the existence of multiple servers. This provides an additional security benefit, by preventing clients from contacting managed servers directly.

You can use two types of load balance session configuration, using sticky sessions and non-sticky sessions. Logi recommends using a sticky session configuration, because it is faster and easier to troubleshoot. The session configuration you use drives how you centralize shared resources. Remember that HTTP sessions are stateless, and that you may have to use cookies or some other tracker to make sure you maintain the proper stickiness when you use HTTP sessions.

Make sure you read the sections of this topic describing [Application Resource Centralization](#Addition), as it applies to both sticky and non-sticky sessions.
