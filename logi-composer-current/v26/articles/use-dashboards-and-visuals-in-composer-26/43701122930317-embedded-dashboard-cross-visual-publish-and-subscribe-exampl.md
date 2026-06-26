---
title: "Embedded Dashboard Cross-Visual Publish and Subscribe Example"
id: 43701122930317
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701122930317-Embedded-Dashboard-Cross-Visual-Publish-and-Subscribe-Example
updated_at: 2026-05-29T14:09:09Z
---

# Embedded Dashboard Cross-Visual Publish and Subscribe Example

# Embedded Dashboard Cross-Visual Publish and Subscribe Example

The following JavaScript example uses methods, properties, and embedded events of the `Zoomdata` and `EmbedManager` classes to publish and subscribe cross-visual links and filters in an embedded dashboard.

// EmbedManager is a singleton and `initComposerEmbedManager` can create a new
// manager or return an existing one. See other samples for howto properly
// initialize the embed manager.
const getEmbedManager = async () => window.initComposerEmbedManager();
// An embedding application should listen for the 'composer-dashboard-loaded'
// event before attempting to publish or subscribe. If multiple dashboards are
// added to the page, listeners can be added the object returned upon embedding
// to specifically target an individual dashboard
const DASHBOARD\_LOADED\_EVENT = 'composer-dashboard-loaded';
const pubSubReady = new Promise((resolve) => {
function resolvePubSubReady() {
resolve();
document.removeEventListener(DASHBOARD\_LOADED\_EVENT, resolvePubSubReady);
}
document.addEventListener(DASHBOARD\_LOADED\_EVENT, resolvePubSubReady);
});
// `countrySelect` represents a drop-down field on the embedding application's
// page that lists a set of countries the user can filter by. After selecting a
// value, the embedding application calls its 'publishValue' function, defined
// below with the link name 'country' and the selected country value. The
// link name is defined in the dashboard. To clear the value filter, make sure
// you pass a null value as shown below.
const countrySelect = document.getElementById('country-select');
countrySelect.addEventListener('change', (event) => {
const value = event.target.value;
publishValue('country', value);
});
// The sample function publishValue below takes a link name and single string
// value and publishes the value on the link name. This causes all visuals on
// any loaded dashboards that are subscribed to the given link to filter
// themselves by the selected value. A visual can be set to subscribe to an
// arbitrary link name by adding a cross-source link using that link name and
// assigning any relevant field to that link.
// PUBLISHER\_ID is an arbitrary string that subscribers can use to associate a
// message with who sent it.
const PUBLISHER\_ID = 'Embedding Application';
async function publishValue(linkName, value) {
const embedManager = await getEmbedManager();
const message = {
type: 'selection',
valueType: 'ATTRIBUTE',
ranges: [
{
operation: 'IN',
value: value
}
]
};
const options = {
publisherId: 'PUBLISHER\_ID'
};
await pubSubReady;
embedManager.publish(
linkName,
message,
options
);
}
// This sample function reates a subscription to the linkname provided using the
// handler provided. The returned unsubscribe function should be stored and
// called when the subscriber should stop receiving messages.
async function subscribe(linkname, handler) {
const embedManager = await getEmbedManager();
await pubSubReady;
return embedManager.subscribe(linkname, handler);
}
// The following code provides an example of how to subscribe to a linkname on
// page load and receive the latest value published. It creates a simple alert
// popup on receipt of each message.
function subscriptionHandler(message, publisherId) {
if (message === null) {
alert(`${publisherId} cleared its publication`);
} else {
const value = message.ranges[0].value;
alert(`${publisherId} published ${value}`);
}
}
const countryUnsubscribe = subscribe('country', subscriptionHandler);
