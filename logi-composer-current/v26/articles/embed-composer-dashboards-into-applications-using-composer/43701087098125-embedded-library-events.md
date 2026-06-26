---
title: "Embedded Library Events"
id: 43701087098125
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701087098125-Embedded-Library-Events
updated_at: 2026-05-29T14:08:32Z
---

# Embedded Library Events

# Embedded Library Events

Events can be used in your JavaScript to control an embedded Composer component when specific events occur.

**Note:** The ability for your end-users to perform some of the events listed here is controlled by the permissions granted to them with their Composer credentials. See [Embedded Composer Component Controls](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081977869-Embedded-Composer-Component-Controls).

You can subscribe using .addEventListener() to embedded inventory component events so that you can execute your own logic when an event occurs.

**Note:** Composer provides a `componentInstanceId` provides a as part of event details for dashboard, source, and visual events.

The following events are supported:

| Event | Data Passed | Example |
| --- | --- | --- |
| composer-inventory-ready | undefined | inventory.addEventListener("composer-inventory-ready", (e) => { console.log(e); }); |
| composer-inventory-loaded | Inventory items  e.detail.inventoryItems | inventory.addEventListener("composer-inventory-loaded", (e) => { console.log(e.detail.inventoryItems); ); |
| composer-inventory-failed | Failed reason  e.detail.failedReason | inventory.addEventListener("composer-inventory-failed", (e) => { console.log(e.detail.failedReason); }); |
| composer-inventory-item-deleted | Inventory item data  `e.detail.inventoryItem` | inventory.addEventListener("composer-inventory-item-deleted", (e) => { console.log(e.detail.inventoryItem); }}; |
