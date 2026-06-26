---
title: "Install the Composer Tracing Microservice"
id: 4405851043991
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851043991-Install-the-Composer-Tracing-Microservice
updated_at: 2021-09-21T01:28:26Z
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
3. Composer recommends that you set up an Elasticsearch persistent store to save the trace files, because trace files are not retained in memory for very long. See [*Persist Traces*](https://devnet.logianalytics.com/hc/en-us/articles/4405851040407-Persist-Traces) for more information.
4. Start the microservice. For example, use the following command to start the Composer tracing microservice using `systemd` in a CentOS or Ubuntu environment:

   ```
   sudo systemctl start zoomdata-tracing-server
   ```

   See [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices).
