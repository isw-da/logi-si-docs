---
title: "Multiple Scheduler Instances"
id: 4419707691927
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707691927-Multiple-Scheduler-Instances
updated_at: 2022-07-17T02:07:14Z
---

# Multiple Scheduler Instances

# Multiple Scheduler Instances

Support for storing task data in networked databases allows
**multiple instances** of the Scheduler service to run at the same
time, on multiple servers, creating a fault-tolerant configuration. If one
of the Scheduler instances goes down, the remaining instances will
continue to function. Having multiple Scheduler service instances will
*not* result in a task being run more often than its designated
frequency. The Scheduler service can be installed independently of the
full Logi Info product.

A multi-instance configuration is *not* supported when using the
standard embedded VistaDB (.NET) or Derby (Java) databases.

For the purposes of interacting with multiple Scheduler service instances
from a Logi application, the application's \_Settings definition must be
properly configured to address all of the instances. This is discussed in
 [Using Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/4419723264407-Using-Logi-Scheduler).
