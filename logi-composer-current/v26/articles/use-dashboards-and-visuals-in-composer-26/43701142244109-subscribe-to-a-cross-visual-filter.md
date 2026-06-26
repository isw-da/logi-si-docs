---
title: "Subscribe to a Cross-Visual Filter"
id: 43701142244109
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701142244109-Subscribe-to-a-Cross-Visual-Filter
updated_at: 2026-05-29T14:09:07Z
---

# Subscribe to a Cross-Visual Filter

# Subscribe to a Cross-Visual Filter

When a visual subscribes to a cross-visual filter, the visual is filtered by the link field in the filter if another visual creates a cross-visual filter for the same field.

When a visual publishes a link, that visual can apply cross-visual filters using the link field to other dashboard visuals that have subscribed to the link. Cross-visual filters can only be applied if the associated link is published. In addition, they can only be applied using the **Filter** option on the [context menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701212059021-Use-the-Context-Menu).

The following example shows how to subscribe to a cross-visual filter:

// An embedding application should listen for the 'composer-dashboard-ready' event
// before attempting to publish or subscribe
const DASHBOARD\_READY\_EVENT = 'composer-dashboard-ready';
const pubSubReady = new Promise((resolve) => {
function resolvePubSubReady() {
resolve();
document.removeEventListener(DASHBOARD\_READY\_EVENT, resolvePubSubReady);
}
document.addEventListener(DASHBOARD\_READY\_EVENT, resolvePubSubReady);
});
// The following covers an example of how to subscribe to a linkName and receive
// the latest value published
function subscriptionHandler(<message>, <publisherId>) {
if (<message> === null) {
alert(<publisherId> + ' cleared its publication');
} else {
const value = message.ranges[0].value;
alert(<publisherId> + ' published ' + value);
}
}
let unsubscribe;
pubSubReady.then(() => {
// The returned unsubscribe function should be stored and called when the
// subscriber should stop receiving messages.
unsubscribe = window.Zoomdata.subscribe('<linkname>', subscriptionHandler);
});

## The `subscribe` Method

The `subscribe` method attaches a subscription handler to a cross-source or same-source link (filter). Each time a new cross-visual filter is published to the link, the subscription handler is called and passed the newly published filter.

When you call the `subscribe` method, the `unsubscribe` function is returned. Run the `unsubscribe` function to remove the handler for the link. This guarantees that the handler will no longer be notified when new messages are published for the link.

Messages passed on the channel can be an arbitrary message object or `null`. Because the message objects are not restricted, the subscription handler should never assume its structure and always check that the message is in the structure the handler is expecting.

Messages that are `null` are interpreted as a clearing of the channel and should be handled by undoing any actions taken based on the last messages received by the handler. For example, when a visual receives a `null` message in its filtering logic, it removes any filters created by previous messages on the given channel (link).

If a message is published to the channel before the `subscribe` method is called, the subscription handler is executed immediately with the latest message that was published on the channel.

## The `subscribe` Properties

The properties for the `subscribe` method of the `Zoomdata` class are described in the following table.

| Property/Object | Description |
| --- | --- |
| `<linkName>` | The link (channel) name to which the subscription handler should subscribe.  The link name is defined when you define a cross-source link. See [Define Cross-Source Links](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027315597-Define-Cross-Source-Links). It is published for use by a dashboard as a cross-visual filter. See [Publish a Link](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701125510541-Publish-a-Link). The link name represents the channel from which the message should be subscribed. It is typically called a *topic* in standard publish/subscribe systems.  **Important:**  There is a one-to-one relationship between cross-source link names and your data fields. You cannot use the same link name for multiple data fields. In you cannot create multiple cross-source links for the same data field.  Type: string |
| `subscriptionHandler` | The handler that will be called upon new messages. This handler will be provided with the published message as the first argument and the ID of the publisher as the second argument.  Type: function |
