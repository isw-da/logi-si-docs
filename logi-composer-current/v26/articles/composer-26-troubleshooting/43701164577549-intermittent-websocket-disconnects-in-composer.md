---
title: "Intermittent WebSocket Disconnects in Composer"
id: 43701164577549
section: "Composer 26 Troubleshooting"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701164577549-Intermittent-WebSocket-Disconnects-in-Composer
updated_at: 2026-05-29T14:09:35Z
---

# Intermittent WebSocket Disconnects in Composer

# Intermittent WebSocket Disconnects in Composer

## Resolutions

When experiencing intermittent or frequent WebSocket disconnects in Composer, check for the following:

* What version of Composer you are using? Consider upgrading to the latest available version. There have been various fixes and improvements to WebSocket behavior implemented that may address your issue.
* Follow-up with your network or IT team to verify if the issue is network-related. For example, traffic between Composer and your end users may be getting rerouted or there could be some other kind of network configuration that is causing skyrocket timeouts to occur in your environment on a frequent or regular basis.
* Check if there are any other applications (e.g. antivirus) that might be trying to block WebSocket sessions from establishing.
* Are these WebSocket disconnects only occurring in Composer or can these WebSocket disconnects be observed by the end-user when using other applications from the same browser machine?
* If you are using a load balancer with Composer, consider the following:
  + Review your load balancer configuration to determine the default session or WebSocket timeout value for your environment. Increase the timeout value if needed.
  + Your load balancer may not support protocol changes (HTTP/101), such as Amazon Web Services (AWS) Elastic Load Balancing (ELB). The Composer application, which uses a combination of HTTP, REST services, and WebSockets, requires a load balancer that supports protocol switching. In this case, consider using an alternative load balancer that supports protocol changes or configure it to function as a Layer-3 proxy if possible. If you are using ELB, you might find this
    [blog post](https://www.flux7.com/tutorial/web-apps-websockets-with-aws-elastic-load-balancing/) informative and a good starting point.
  + If you are using
    HAProxy version 1.5 or newer , please review your configured timeout setting for
    **tunnel mode** because it will override other server or client timeout settings. Thus, if set to a low value, this setting can cause frequent WebSocket disconnects to occur. For more information about tunnel mode, refer to the [HAProxy documentation](https://www.haproxy.com/blog/websockets-load-balancing-with-haproxy/).

**Note:** 
By default, the session timeout for the Composer server is
**30** minutes. If users are idle for extended periods of time, the existing WebSocket connections will timeout and this is expected behavior.
