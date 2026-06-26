---
title: "Configure the Tracing Microservice Port"
id: 4405851044887
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851044887-Configure-the-Tracing-Microservice-Port
updated_at: 2021-09-21T01:28:27Z
---

# Configure the Tracing Microservice Port

# Configure the Tracing Microservice Port

The Composer tracing microservice is accessible by a web browser on port 9411 (by default), however, the interface does not require authentication at this time and access can only be restricted at the firewall.

To change the port of the tracing microservice, specify the `server.port=<port>` property in the `/etc/zoomdata/tracing-server.properties` file and [restart the tracing microservice](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

Composer uses microservice discovery to detect devices and microservices used in your computer network. If you would like to point a custom tracing server, that is not registered in the Consul, to the Composer microservices, edit the properties file for every installed Composer microservice and specify the following property:

```
tracing.export.baseUrl=http:/<hostname>:<port>
```

Edit the properties file with a text editor and replace `<hostname>` with the appropriate tracing microservice host name or IP address and replace `<port>` with the tracing microservice port that should be used. A complete list of Composer's property files can be found in [*Configuration Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850888599-Configuration-Property-Files). If you cannot locate a properties file in `/etc/zoomdata/`, copy it from `/opt/zoomdata/conf`.

When you have finished, save each properties file and restart the associated microservice. See [*Manage Composer v6 Microservices Using the Command Line Utility*](https://devnet.logianalytics.com/hc/en-us/articles/4405850885527-Manage-Composer-v6-Microservices-Using-the-Command-Line-Utility).
