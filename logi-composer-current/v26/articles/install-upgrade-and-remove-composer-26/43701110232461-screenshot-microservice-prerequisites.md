---
title: "Screenshot Microservice Prerequisites"
id: 43701110232461
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110232461-Screenshot-Microservice-Prerequisites
updated_at: 2026-05-29T14:08:48Z
---

# Screenshot Microservice Prerequisites

# Screenshot Microservice Prerequisites

Before you can install and use the screenshot microservice, consider the following [browser](#Browser), [memory](#Memory), [thread count](#Thread), and [software](#Obtain) prerequisites.

## Browser Requirements

The screenshot microservice uses headless Google Chrome. Chrome-based screenshots include the entire dashboard and can be exported in PNG or PDF formats.

## Memory Configuration Considerations

If your use of Composer includes [scheduling dashboard reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700998266509-About-Scheduled-Dashboard-Reports), you may need to update this memory setting. The default memory configuration is suitable for handling up to 10 concurrent dashboard reports (different dashboard reports scheduled for the same time). If you need to schedule more concurrent dashboard reports, increase the memory allocation to about one gigabyte (1GB) more for every 15 concurrent reports. See [Configure Memory Settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040681613-Configure-Memory-Settings).

### Thread Count Considerations

If your use of Composer includes [scheduling dashboard reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700998266509-About-Scheduled-Dashboard-Reports), update the screenshot microservice `pool.thread.size` setting so it is greater than the number of concurrent reports (see [screenshot-service.properties Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054295053-screenshot-service-properties-Properties)). This setting controls the thread count for screenshot microservice requests.

## Obtain the Software

Before you can install the screenshot microservice, contact Composer [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) to obtain a download link for the screenshot microservice installation software. Be sure you specify the operating system you are using so the appropriate software is provided.
