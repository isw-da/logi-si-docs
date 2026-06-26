---
title: "Embedded Dashboard Cross-Visual Publish and Subscribe Example"
id: 4402955640855
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955640855-Embedded-Dashboard-Cross-Visual-Publish-and-Subscribe-Example
updated_at: 2021-08-07T17:32:48Z
---

# Embedded Dashboard Cross-Visual Publish and Subscribe Example

# Embedded Dashboard Cross-Visual Publish and Subscribe Example

The following JavaScript example uses methods, properties, and embedded events of the `Zoomdata` and `EmbedManager` classes to publish and subscribe cross-visual links and filters in an embedded dashboard.

```
// An embedding application should listen for the 'composer-dashboard-ready' event 
// before attempting to publish or subscribe

const DASHBOARD_READY_EVENT = 'composer-dashboard-ready';
const pubSubReady = new Promise((resolve) => {
   function resolvePubSubReady() {
      resolve();
      document.removeEventListener(DASHBOARD_READY_EVENT, resolvePubSubReady);
   }
   document.addEventListener(DASHBOARD_READY_EVENT, resolvePubSubReady);
});

// This represents a drop-down field on the embedding application's page that 
// lists a set of countries the user can filter by. After selecting a value,
// the embedding application calls its 'publishValue' function, defined
// below with the link name '<linkname> and the selected country value.
// The link name is defined in the dashboard. To clear the value filter,
// make sure you pass a null value as shown below.


const countrySelect = document.getElementById('country-select');
countrySelect.addEventListener('change', (event) => {
   const value = event.target.value;
   pubSubReady.then(() => publishValue('<linkname>', value));
});

// The sample function publishValue below takes a link name and single string value
// and publishes the value on the link name. This causes all visuals on any loaded
// dashboards that are subscribed to the given link to filter themselves by the
// selected value. A visual can be set to subscribe to an arbitrary link name
// by adding a cross-source link using that link name and assigning any relevant
// field to that link.

// PUBLISHER_ID is an arbitrary string that subscribers can use to associate a message
// with who sent it.

const PUBLISHER_ID = 'Embedding Application';
function publishValue(<linkName>, <value>) {
   const <message> = {
      type: 'selection',
      valueType: 'ATTRIBUTE',
      ranges: [
         {
            operation: '<operation>',
            value: '<value>'
         }
      ]
   };
   const <options> = {
      publisherId: 'PUBLISHER_ID'
   };
   window.Zoomdata.publish(
      '<linkName>',
      '<message>',
      '<options>'
   );
}

// The following code provides an example of how to subscribe to a linkname and receive
// the latest value published. It also provides appropriate pop-up messages in
// the embedding application.

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
```
