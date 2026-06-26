---
title: "Supported Cross-Visual Publish JavaScript Properties"
id: 4405851133463
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851133463-Supported-Cross-Visual-Publish-JavaScript-Properties
updated_at: 2021-09-21T01:29:19Z
---

# Supported Cross-Visual Publish JavaScript Properties

# Supported Cross-Visual Publish JavaScript Properties

The properties for the `publish` method of the `Zoomdata` class are described in the following table.

| Property/Object | Description |
| --- | --- |
| `<linkName>` | The link (channel) name. Link names can be custom names, specified when a cross-source link is created, or names in the format `<source-name>.<field-name>`, automatically generated for every field in a data source for same-source links.  The link name is defined when you define a cross-source link. See [*Define Cross-Source Links*](https://devnet.logianalytics.com/hc/en-us/articles/4405859236887-Define-Cross-Source-Links). It is published for use by a dashboard as a cross-visual filter. See [*Publish a Link*](https://devnet.logianalytics.com/hc/en-us/articles/4405859420823-Publish-a-Link). The link name represents the channel into which the message should be published. It is typically called a *topic* in standard publish/subscribe systems.  There is a one-to-one relationship between cross-source link names and your data fields. You cannot use the same link name for multiple data fields. In addition, you cannot create multiple cross-source links for the same data field.  Type: string |
| `<message>` | The message sent with the link. The message published can either be an arbitrary object or null. An object published to a link channel is not restricted to any particular structure but a Composer dashboard only recognizes messages in the structure described in [*Published Cross-Visual JavaScript Message Structure*](https://devnet.logianalytics.com/hc/en-us/articles/4405859429783-Published-Cross-Visual-JavaScript-Message-Structure).  Publishing a null message can clear the last published message from the channel. If the last published message's `publisherId` matches the null message's `publisherId`, the last message is removed from the channel and subscribers receive a null message. If the `publisherId` of the last published message on the channel does not match the null message's `publisherId`, nothing happens.  The most recently published message on each channel is stored and sent to new subscribers at the time of subscription.  Type: object or null |
| `<options>` | Options for how the link should be applied. All values are optional. Options include:   * `options.publisherId`: An arbitrary sting identifying the publisher of the link. This can be used to handle subscriptions differently based on publisher. For example, a subscriber may decide not to apply messages they posted themselves. * `options.timestamp`: A number representing the time at which the link is published. It defaults to `Date.now()`. * `options.targetComponents`: A string that allows the publisher to target only specific dashboards when more than one dashboard is embedded on a page. If not provided, it applies the link to all embedded dashboards. To target a component, add its `componentInstanceId` (provided in the return from the call to `embedManager.createComponent`).   Type: object |
