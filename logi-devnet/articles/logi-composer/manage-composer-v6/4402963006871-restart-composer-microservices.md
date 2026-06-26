---
title: "Restart Composer Microservices"
id: 4402963006871
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963006871-Restart-Composer-Microservices
updated_at: 2021-08-07T17:31:19Z
---

# Restart Composer Microservices

# Restart Composer Microservices

This topic describes how to restart Composer microservices in CentOS 7 or 8 environments or in Ubuntu 16 or 18 environments.

The list of Composer microservices can be found in [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4402963037079-Composer-Microservice-Name-Reference).

You can also restart Composer microservices using the CLI. See [*Manage Composer v6 Microservices Using the Command Line Utility*](https://devnet.logianalytics.com/hc/en-us/articles/4402955438871-Manage-Composer-v6-Microservices-Using-the-Command-Line-Utility).

To restart all Composer microservices, enter the following command:

```
sudo systemctl restart $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')
```

To restart a specific Composer microservice, enter the following command:

```
sudo systemctl restart <service>
```

Replace `<service>` with the name of the Composer microservice. See [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4402963037079-Composer-Microservice-Name-Reference).
