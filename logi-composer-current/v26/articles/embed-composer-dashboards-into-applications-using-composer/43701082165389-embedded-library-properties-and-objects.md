---
title: "Embedded Library Properties and Objects"
id: 43701082165389
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701082165389-Embedded-Library-Properties-and-Objects
updated_at: 2026-05-29T14:08:30Z
---

# Embedded Library Properties and Objects

# Embedded Library Properties and Objects

The library embed feature also includes pre-defined actions for adding a dashboard and opening a dashboard.

Here's what you can do with pre-defined actions:

* Specify an action for embed action
* Specify an action for navigate to link
* Change a cursor if a column has onClick action specified
* Pass an item id to the link ("https://dashboards.company.com/edit/${inventoryitemId}")
* Filter dashboards by dashboard tags (See [Embed Composer Components Using JavaScript and Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108006413-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access))

The following Actions are supported:

| Action |
| --- |
| Embed |
| Open |

Below is a code sample for using the onClick property:

| Type | Example |
| --- | --- |
| FunctionClickHandler | (data?: InventoryItem) => console.log(data) |
| EmbedClickHandler | { type: "embed", parentElement: "#editor-container", // OR document.querySelector("#editor-container") replaceComponent: true, componentParams: { ... } } |
| LinkClickHandler | { type: "link", href: "https://dashboards.com/edit/${inventoryItemId}", target: "\_blank" } |
