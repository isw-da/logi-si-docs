---
title: "Performance Considerations"
id: 4406817613847
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817613847-Performance-Considerations
updated_at: 2022-04-06T06:07:13Z
---

# Performance Considerations

# Performance Considerations

For a variety of reasons, connectivity to mobile devices may be more sensitive to bandwidth limitations and performance issues than a PC. Developers who wish to improve performance have several measures they may care to use:

Actual transmission performance can be enhanced using HTTP compression to reduce network bandwidth usage. Administrators can configure their web servers so that application and/or file output is compressed. Microsoft offers [this information](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771003(v=ws.10)?redirectedfrom=MSDN) about enabling compression on IIS 7, and numerous sources are available online describing the same for Apache Tomcat.

In addition, there are a number of things developers can do to ensure good Mobile Report performance. For example, limiting the amount of data being delivered to the device in any one request, and breaking complex reports into a number of simpler reports.

There are examples of complete Mobile Report definitions in [Working with Logi Mobile Reports](https://devnet.logianalytics.com/hc/en-us/articles/4406818075287-Working-with-Logi-Mobile-Reports).
