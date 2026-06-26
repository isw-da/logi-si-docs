---
title: "Supported Zoomdata Methods"
id: 4405859428759
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859428759-Supported-Zoomdata-Methods
updated_at: 2021-09-21T01:29:18Z
---

# Supported Zoomdata Methods

# Supported `Zoomdata` Methods

The following methods for the `Zoomdata` class can be used to manage embedded settings for published and subscribed cross-visual links in a dashboard. Sample code showing the use of these methods in an application are provided. See [*Embedded Dashboard Cross-Visual Publish and Subscribe Example*](https://devnet.logianalytics.com/hc/en-us/articles/4405851132183-Embedded-Dashboard-Cross-Visual-Publish-and-Subscribe-Example).

| Method | Description |
| --- | --- |
| `publish()` | The `publish` method publishes a message (filter) for a specific cross-source or same-source link (channel). Publishing a link filter causes any subscribing handlers for the link to be called and passed the filter message. There is no registration process for a link, simply call the `publish` method with a link name and it will be created. No value is returned.  The filter message structure is described in [*Published Cross-Visual JavaScript Message Structure*](https://devnet.logianalytics.com/hc/en-us/articles/4405859429783-Published-Cross-Visual-JavaScript-Message-Structure).  The properties for the `publish` method are described in [*Supported Cross-Visual Publish JavaScript Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405851133463-Supported-Cross-Visual-Publish-JavaScript-Properties). |
| `subscribe()` | The `subscribe` method attaches a subscription handler to a cross-source or same-source link (filter). Each time a new cross-visual filter is published to the link, the subscription handler is called and passed the newly published filter.  When you call the `subscribe` method, the `unsubscribe` function is returned. Run the `unsubscribe` function to remove the handler for the link. This guarantees that the handler will no longer be notified when new messages are published for the link.  Messages passed on the channel can be an arbitrary message object or `null`. Because the message objects are not restricted, the subscription handler should never assume its structure and always check that the message is in the structure the handler is expecting.  Messages that are `null` are interpreted as a clearing of the channel and should be handled by undoing any actions taken based on the last messages received by the handler. For example, when a Composer visual receives a `null` message in its filtering logic, it removes any filters created by previous messages on the given channel (link).  If a message is published to the channel before the `subscribe` method is called, the subscription handler is executed immediately with the latest message that was published on the channel.  The properties for the `subscribe` method are described in [*Supported Cross-Visual Subscribe JavaScript Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405851134487-Supported-Cross-Visual-Subscribe-JavaScript-Properties). |
