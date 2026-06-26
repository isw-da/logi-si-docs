---
title: "Widgets and Load Balancing"
id: 4406818126999
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818126999-Widgets-and-Load-Balancing
updated_at: 2022-04-06T06:10:19Z
---

# Widgets and Load Balancing

# Widgets and Load Balancing

Because they're actually embeddable JavaScript code, Widget definitions behave
slightly differently than standard report definitions: their images are
temporarily stored on the web server in a browser-accessible directory, which is
the rdDownload folder.

This can be tricky when used with load-balancing, since the location (rdDownload) is
specific to the individual server. It can be problematic for round-robin
load-balance scenarios and may depend on the type of load balancer you're using
and what type of persistence there is, if any, across unique requests. The
only certain way to ensure problem-free operation is to enable
"sticky sessions", or session affinity, for the load balancer. In this case, there
would never be a file/request conflict or missing file error.

If you
don't use complete session affinity, it may be possible to configure the load
balancer "sticky time", also called "persistence", so that, for any
request/session duration, you attach to one server node to ensure the operations
that take longer to happen, or that require multiple requests, don't
automatically jump to the next node. That means the user is persistent or sticky
for a given time duration, and then can be sent to a different server for
requests outside of the time duration. This setup would allow for multiple
sequential requests to be made to the same server.

More information about load-balancing in general can be found in [Load Balancing Configuration](https://devnet.logianalytics.com/hc/en-us/articles/4406817708567-Load-Balancing-Configuration).
