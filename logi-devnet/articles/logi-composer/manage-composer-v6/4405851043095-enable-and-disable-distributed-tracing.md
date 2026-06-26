---
title: "Enable and Disable Distributed Tracing"
id: 4405851043095
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851043095-Enable-and-Disable-Distributed-Tracing
updated_at: 2021-09-21T01:28:25Z
---

# Enable and Disable Distributed Tracing

# Enable and Disable Distributed Tracing

Distributed tracing for all Composer microservices is enabled by default. You can enable or disable tracing using the `tracing.enabled` property in the properties file for each Composer microservice. When this property is set to `true`, tracing is enabled, when it is set to `false`, tracing is disabled.

A complete list of the property files in Composer can be found in [*Configuration Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850888599-Configuration-Property-Files). If you cannot locate a properties file in `/etc/zoomdata/`, copy it from `/opt/zoomdata/conf`.

To enable or disable tracing in a properties file, edit the file using a text editor. After changing the `tracing.enabled` property, save the file and restart the microservice. See [*Manage Composer v6 Microservices Using the Command Line Utility*](https://devnet.logianalytics.com/hc/en-us/articles/4405850885527-Manage-Composer-v6-Microservices-Using-the-Command-Line-Utility).
