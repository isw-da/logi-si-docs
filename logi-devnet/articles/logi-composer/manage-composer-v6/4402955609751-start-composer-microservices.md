---
title: "Start Composer Microservices"
id: 4402955609751
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955609751-Start-Composer-Microservices
updated_at: 2021-08-07T17:31:21Z
---

# Start Composer Microservices

# Start Composer Microservices

This topic describes how to start Composer microservices in CentOS 7 or 8 environments or in Ubuntu 16 or 18 environments.

The list of Composer microservices can be found in [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4402963037079-Composer-Microservice-Name-Reference). The order in which microservices should be started is described in [*Composer Microservice Startup Order*](https://devnet.logianalytics.com/hc/en-us/articles/4402963037847-Composer-Microservice-Startup-Order).

You can also start Composer microservices using the CLI. See [*Manage Composer v6 Microservices Using the Command Line Utility*](https://devnet.logianalytics.com/hc/en-us/articles/4402955438871-Manage-Composer-v6-Microservices-Using-the-Command-Line-Utility).

To start all Composer microservices, enter the following command:

```
sudo systemctl start $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')
```

To start a specific Composer microservice, enter the following command:

```
sudo systemctl start <service>
```

Replace `<service>` with the name of the Composer microservice. See [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4402963037079-Composer-Microservice-Name-Reference).
