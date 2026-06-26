---
title: "Screenshot Microservice Prerequisites"
id: 34933013736589
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933013736589-Screenshot-Microservice-Prerequisites
updated_at: 2026-05-26T22:07:28Z
---

# Screenshot Microservice Prerequisites

# Screenshot Microservice Prerequisites

Before you can install and use the Screenshot microservice, consider the following [browser](#Browser), [memory](#Memory), [thread count](#Thread), and [software](#Obtain) prerequisites.

## Browser Requirements

The Screenshot microservice uses headless Google Chrome. Chrome-based screenshots include the entire dashboard and can be exported in PNG or PDF formats.

## Memory Configuration Considerations

If your use of Composer includes [scheduling dashboard reports](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932793437325-About-Scheduled-Dashboard-Reports), you may need to update this memory setting. The default memory configuration is suitable for handling up to 10 concurrent dashboard reports (different dashboard reports scheduled for the same time). If you need to schedule more concurrent dashboard reports, increase the memory allocation to about one gigabyte (1GB) more for every 15 concurrent reports. See [Configure Memory Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932637063437-Configure-Memory-Settings).

### Thread Count Considerations

If your use of Composer includes [scheduling dashboard reports](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932793437325-About-Scheduled-Dashboard-Reports), update the Screenshot microservice `pool.thread.size` setting so it is greater than the number of concurrent reports (see [screenshot-service.properties Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932703048333-screenshot-service-properties-Properties)). This setting controls the thread count for Screenshot microservice requests.

## Obtain the Software

Before you can install the Screenshot microservice, contact Composer [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) to obtain a download link for the Screenshot microservice installation software. Be sure you specify the operating system you are using so the appropriate software is provided.
