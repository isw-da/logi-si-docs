---
title: "Sample Architecture"
id: 4406817865623
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817865623-Sample-Architecture
updated_at: 2022-04-06T06:08:45Z
---

# Sample Architecture

# Sample Architecture

The architecture below represents a deployment of Logi Info and the Logi Scheduler service to AWS. In this example, the Logi Info application and the parent application in which it’s embedded are hosted in a Virtual Private Cloud behind a load balancer. EC2 instances hosting the Logi Info application can be spun up or down according to user demand.

This example also assumes that shared resources (such as Bookmark files and SecureKey references) are managed in a database accessible to each EC2 instance. An alternative approach is to configure a network share in place of the database.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575541399/sample_architecture_870x397.png)
