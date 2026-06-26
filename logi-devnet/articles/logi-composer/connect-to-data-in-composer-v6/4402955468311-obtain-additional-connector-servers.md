---
title: "Obtain Additional Connector Servers"
id: 4402955468311
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955468311-Obtain-Additional-Connector-Servers
updated_at: 2021-08-07T17:29:48Z
---

# Obtain Additional Connector Servers

# Obtain Additional Connector Servers

Several data connector servers are installed by default in your Composer environment, but a number of other connector servers are also available. The new connector server can be added via HTTP or Socket protocols. For a complete list of all supported connector servers, see [*Composer Data Connector Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4402963033623-Composer-Data-Connector-Reference).

To obtain one or more of these connector servers:

1. Contact Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4402955592087-Contact-Technical-Support). You will receive a `yum` or `apt` command that downloads and sets up the connector server in the Composer environment. After running the command, the connector microservice is installed and enabled in the Composer environment, allowing it to be discoverable as a new connector microservice.
2. Register the connector server. Connector servers are started and run as separate processes, and accept requests on a specific TCP/IP port. See [*Register a New Connector Server*](https://devnet.logianalytics.com/hc/en-us/articles/4402962903831-Register-a-New-Connector-Server).

After you have obtained, installed, and registered the connector server, you need to add and enable at least one connector for it. See [*Define a New Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4402962897815-Define-a-New-Connector) and [*Enable and Disable Connectors*](https://devnet.logianalytics.com/hc/en-us/articles/4402962899351-Enable-and-Disable-Connectors).
