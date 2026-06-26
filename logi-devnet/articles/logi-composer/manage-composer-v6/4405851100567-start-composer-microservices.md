---
title: "Start Composer Microservices"
id: 4405851100567
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices
updated_at: 2021-09-21T01:28:57Z
---

# Start Composer Microservices

# Start Composer Microservices

This topic describes how to start Composer microservices in CentOS 7 or 8 environments or in Ubuntu 16 or 18 environments.

The list of Composer microservices can be found in [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405851149591-Composer-Microservice-Name-Reference). The order in which microservices should be started is described in [*Composer Microservice Startup Order*](https://devnet.logianalytics.com/hc/en-us/articles/4405851150615-Composer-Microservice-Startup-Order).

You can also start Composer microservices using the CLI. See [*Manage Composer v6 Microservices Using the Command Line Utility*](https://devnet.logianalytics.com/hc/en-us/articles/4405850885527-Manage-Composer-v6-Microservices-Using-the-Command-Line-Utility).

To start all Composer microservices, enter the following command:

```
sudo systemctl start $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')
```

To start a specific Composer microservice, enter the following command:

```
sudo systemctl start <service>
```

Replace `<service>` with the name of the Composer microservice. See [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405851149591-Composer-Microservice-Name-Reference).
