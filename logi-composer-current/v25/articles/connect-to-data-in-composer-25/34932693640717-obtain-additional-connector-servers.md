---
title: "Obtain Additional Connector Servers"
id: 34932693640717
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932693640717-Obtain-Additional-Connector-Servers
updated_at: 2026-05-26T22:06:22Z
---

# Obtain Additional Connector Servers

# Obtain Additional Connector Servers

Several data connector servers are installed by default in your Composer environment, but a number of other connector servers are also available. The new connector server can be added via HTTP or Socket protocols. For a complete list of all supported connector servers, see [Data Connector Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933117968525-Data-Connector-Reference).

**Obtain one or more of these connector servers**

1. Contact Composer [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support). You will receive a `yum` or `apt` command that downloads and sets up the connector server in the Composer environment. After running the command, the connector microservice is installed and enabled in the Composer environment, allowing it to be discoverable as a new connector microservice.
2. Register the connector server. Connector servers are started and run as separate processes, and accept requests on a specific TCP/IP port. See [Register a New Connector Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932742145165-Register-a-New-Connector-Server).

After you have obtained, installed, and registered the connector server, you need to add and enable at least one connector for it. See [Define a New Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932709865869-Define-a-New-Connector) and [Enable and Disable Connectors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932710074509-Enable-and-Disable-Connectors).
