---
title: "Screenshot Microservice Prerequisites"
id: 4405859381655
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859381655-Screenshot-Microservice-Prerequisites
updated_at: 2021-09-21T01:28:55Z
---

# Screenshot Microservice Prerequisites

# Screenshot Microservice Prerequisites

Before you can install and use the Screenshot microservice, consider the following [browser](#Browser), [memory](#Memory), [thread count](#Thread), and [software](#Obtain) prerequisites.

## Browser Requirements

The Screenshot microservice uses headless Google Chrome. Chrome-based screenshots include the entire dashboard and can be exported in PNG or PDF formats.

## Memory Configuration Considerations

If your use of Composer includes [scheduling dashboard reports](https://devnet.logianalytics.com/hc/en-us/articles/4405850989335-About-Scheduled-Dashboard-Reports), you may need to update this memory setting. The default memory configuration is suitable for handling up to 10 concurrent dashboard reports (different dashboard reports scheduled for the same time). If you need to schedule more concurrent dashboard reports, increase the memory allocation to about one gigabyte (1GB) more for every 15 concurrent reports. See [*Configure Memory Settings*](https://devnet.logianalytics.com/hc/en-us/articles/4405850891287-Configure-Memory-Settings).

### Thread Count Considerations

If your use of Composer includes [scheduling dashboard reports](https://devnet.logianalytics.com/hc/en-us/articles/4405850989335-About-Scheduled-Dashboard-Reports), update the Screenshot microservice `pool.thread.size` setting so it is greater than the number of concurrent reports (see [*screenshot-service.properties Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405850904471-screenshot-service-properties-Properties)). This setting controls the thread count for Screenshot microservice requests.

## Obtain the Software

Before you can install the Screenshot microservice, contact Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) to obtain a download link for the Screenshot microservice installation software. Be sure you specify the operating system you are using so the appropriate software is provided.
