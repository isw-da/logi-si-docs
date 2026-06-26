---
title: "Supported Cross-Visual Subscribe JavaScript Properties"
id: 43701125866253
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701125866253-Supported-Cross-Visual-Subscribe-JavaScript-Properties
updated_at: 2026-05-29T14:09:10Z
---

# Supported Cross-Visual Subscribe JavaScript Properties

# Supported Cross-Visual Subscribe JavaScript Properties

The properties for the `subscribe` method of the `Zoomdata` class are described in the following table.

| Property/Object | Description |
| --- | --- |
| `<linkName>` | The link (channel) name to which the subscription handler should subscribe.  The link name is defined when you define a cross-source link. See [Define Cross-Source Links](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027315597-Define-Cross-Source-Links). It is published for use by a dashboard as a cross-visual filter. See [Publish a Link](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701125510541-Publish-a-Link). The link name represents the channel from which the message should be subscribed. It is typically called a *topic* in standard publish/subscribe systems.  **Important:**  There is a one-to-one relationship between cross-source link names and your data fields. You cannot use the same link name for multiple data fields. In you cannot create multiple cross-source links for the same data field.  Type: string |
| `subscriptionHandler` | The handler that will be called upon new messages. This handler will be provided with the published message as the first argument and the ID of the publisher as the second argument.  Type: function |
