---
title: "Supported Cross-Visual Subscribe JavaScript Properties"
id: 4405851134487
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851134487-Supported-Cross-Visual-Subscribe-JavaScript-Properties
updated_at: 2021-09-21T01:29:18Z
---

# Supported Cross-Visual Subscribe JavaScript Properties

# Supported Cross-Visual Subscribe JavaScript Properties

The properties for the `subscribe` method of the `Zoomdata` class are described in the following table.

| Property/Object | Description |
| --- | --- |
| `<linkName>` | The link (channel) name to which the subscription handler should subscribe.  The link name is defined when you define a cross-source link. See [*Define Cross-Source Links*](https://devnet.logianalytics.com/hc/en-us/articles/4405859236887-Define-Cross-Source-Links). It is published for use by a dashboard as a cross-visual filter. See [*Publish a Link*](https://devnet.logianalytics.com/hc/en-us/articles/4405859420823-Publish-a-Link). The link name represents the channel from which the message should be subscribed. It is typically called a *topic* in standard publish/subscribe systems.  There is a one-to-one relationship between cross-source link names and your data fields. You cannot use the same link name for multiple data fields. In addition, you cannot create multiple cross-source links for the same data field.  Type: string |
| `subscriptionHandler` | The handler that will be called upon new messages. This handler will be provided with the published message as the first argument and the ID of the publisher as the second argument.  Type: function |
