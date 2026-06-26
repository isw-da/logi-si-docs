---
title: "Obtain Additional Connector Servers"
id: 43701024898061
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024898061-Obtain-Additional-Connector-Servers
updated_at: 2026-05-29T14:07:31Z
---

# Obtain Additional Connector Servers

# Obtain Additional Connector Servers

Several data connector servers are installed by default in your Composer environment, but a number of other connector servers are also available. The new connector server can be added via HTTP or Socket protocols. For a complete list of all supported connector servers, see [Data Connector Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference).

**Obtain one or more of these connector servers**

1. Contact Composer [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support). You will receive a `yum` or `apt` command that downloads and sets up the connector server in the Composer environment. After running the command, the connector microservice is installed and enabled in the Composer environment, allowing it to be discoverable as a new connector microservice.
2. Register the connector server. Connector servers are started and run as separate processes, and accept requests on a specific TCP/IP port. See [Register a New Connector Server](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042690957-Register-a-New-Connector-Server).

After you have obtained, installed, and registered the connector server, you need to add and enable at least one connector for it. See [Define a New Connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993403661-Define-a-New-Connector) and [Enable and Disable Connectors](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024705037-Enable-and-Disable-Connectors).
