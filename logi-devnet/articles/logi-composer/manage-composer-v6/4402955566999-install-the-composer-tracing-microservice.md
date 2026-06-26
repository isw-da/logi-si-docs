---
title: "Install the Composer Tracing Microservice"
id: 4402955566999
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955566999-Install-the-Composer-Tracing-Microservice
updated_at: 2021-08-07T17:30:59Z
---

# Install the Composer Tracing Microservice

# Install the Composer Tracing Microservice

To install and start the tracing microservice:

1. Open your SSH client.
2. Use the following command to install the Composer tracing microservice in a CentOS environment:

   ```
   sudo yum install zoomdata-tracing-server -y
   ```

   Use the following command to install the Composer tracing microservice in an Ubuntu environment:

   ```
   sudo apt install zoomdata-tracing-server
   ```
3. Composer recommends that you set up an Elasticsearch persistent store to save the trace files, because trace files are not retained in memory for very long. See [*Persist Traces*](https://devnet.logianalytics.com/hc/en-us/articles/4402962978839-Persist-Traces) for more information.
4. Start the microservice. For example, use the following command to start the Composer tracing microservice using `systemd` in a CentOS or Ubuntu environment:

   ```
   sudo systemctl start zoomdata-tracing-server
   ```

   See [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4402955609751-Start-Composer-Microservices).
