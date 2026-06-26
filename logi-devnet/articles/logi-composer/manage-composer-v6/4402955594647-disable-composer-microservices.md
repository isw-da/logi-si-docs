---
title: "Disable Composer Microservices"
id: 4402955594647
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955594647-Disable-Composer-Microservices
updated_at: 2021-08-07T17:31:11Z
---

# Disable Composer Microservices

# Disable Composer Microservices

This topic describes how to disable Composer microservices in CentOS 7 or 8 environments or in Ubuntu 16 or 18 environments.

The list of Composer microservices can be found in [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4402963037079-Composer-Microservice-Name-Reference).

You can also disable Composer microservices using the CLI. See [*Manage Composer v6 Microservices Using the Command Line Utility*](https://devnet.logianalytics.com/hc/en-us/articles/4402955438871-Manage-Composer-v6-Microservices-Using-the-Command-Line-Utility).

To disable all Composer microservices, enter the following command:

```
sudo systemctl disable $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
```

To disable a specific Composer microservice, enter the following command:

```
sudo systemctl disable <service>
```

Replace `<service>` with the name of the Composer microservice. See [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4402963037079-Composer-Microservice-Name-Reference).
