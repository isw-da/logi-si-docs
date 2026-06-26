---
title: "Supported Composer v6 Embedded Events"
id: 4402955573911
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955573911-Supported-Composer-v6-Embedded-Events
updated_at: 2022-03-09T16:41:41Z
---

# Supported Composer v6 Embedded Events

# Supported Composer v6 Embedded Events

Events can be used in your JavaScript to control an embedded Composer component when specific events occur.

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) The ability for your end-users to perform some of the events listed here is controlled by the permissions granted to them with their Composer credentials. See [*Embedded Composer Component Controls*](https://devnet.logianalytics.com/hc/en-us/articles/4402955570327-Embedded-Composer-Component-Controls).

Embedded events are described in the following tables:

* [*Document Events*](#Document)
* [*Dashboard Events*](#Dashboard)
* [*Visual Authoring Events*](#VisAuth)
* [*Visual Events*](#Visual)

Sample code showing how to subscribe to the events that trigger the event listeners is provided in each description. In these examples, when the event is triggered, a log message is written to the console. You can alter this behavior using custom JavaScript appropriate for your installation. For example, you can trigger a pop-up message (instead of a log message) using the Javascript `alert()` method instead of the `console.log()` method. For example: `alert("Dashboard has been loaded !!!");`

![](https://devnet.logianalytics.com/hc/article_attachments/4404952805911/criticalicon.gif) The event detail payload that is passed to the event listener is **experimental** and might be changed. Mutating the detail object (`e.detail.*`) will not update the UI; the object is read-only.

## Document Events

| Event | Description |
| --- | --- |
| `composer-init-failed` | Triggered by document if the component fails to initialize. No data is passed in the event.   ``` document.addEventListener("composer-init-failed", () => {      console.log("composer-init-failed"); }); ``` |
| `composer-unauthorized` | Triggered by document when the authorization token expires. No data is passed in the event.   ``` document.addEventListener("composer-unauthorized", () => {      console.log("composer-unauthorized"); }); ``` |

## Dashboard Events

| Event | Description |
| --- | --- |
| `composer-dashboard-changed` | Triggered by the dashboard when there is any change in the dashboard configuration. This is useful for tracking the active state of the dashboard. The data passed in the event includes the dashboard and dashboard data (`e.detail.dashboard`).   ``` dashboard.addEventListener("composer-dashboard-changed", (e) => {      console.log(e.detail.dashboard); }); ``` |
| `composer-dashboard-deleted` | Triggered by the dashboard when the dashboard is deleted. The data passed in the event includes the dashboard and dashboard data (`e.detail.dashboard`).   ``` dashboard.addEventListener("composer-dashboard-deleted", (e) => {      console.log(e.detail.dashboard); }); ``` |
| `composer-dashboard-failed` | Triggered by the dashboard when the dashboard fails to load. The data passed in the event includes the failure reason (`failedReason`).  ``` dashboard.addEventListener("composer-dashboard-failed", (e) => {      console.log(e.detail.failedReason); }); ``` |
| `composer-dashboard-loaded` | Triggered when a dashboard resource is loaded. The data passed in the event includes the dashboard and dashboard data (`e.detail.dashboard`).   ``` dashboard.addEventListener("composer-dashboard-loaded", (e) => {      console.log(e.detail.dashboard); }); ``` |
| `composer-dashboard-ready` | Triggered by the dashboard when all visuals on the dashboard have been rendered. The data passed in the event includes the dashboard and dashboard data (`e.detail.dashboard`).   ``` dashboard.addEventListener("composer-dashboard-ready", (e) => {           console.log(e.detail.dashboard); }); ``` |
| `composer-dashboard-saved` | Triggered by the dashboard when a dashboard resource has been successfully saved. The data passed in the event includes the dashboard and dashboard data (`e.detail.dashboard`).   ``` dashboard.addEventListener("composer-dashboard-saved", (e) => {      console.log(e.detail.dashboard); }); ``` |
| `composer-dashboard-widget-added` | Triggered by the dashboard when a visual is added to the dashboard. The data passed in the event includes the visual and visual data (`e.detail.visual`).   ``` dashboard.addEventListener("composer-dashboard-widget-added", (e) => {             console.log(e.detail.visual); }); ``` |
| `composer-dashboard-widget-removed` | Triggered by the dashboard when a visual is removed from the dashboard. The data passed in the event includes the visual and visual data (`e.detail.visual`).   ``` dashboard.addEventListener("composer-dashboard-widget-removed", (e) => {      console.log(e.detail.visual); }); ``` |

## Visual Authoring Events

| Event | Description |
| --- | --- |
| `composer-visual-builder-changed` | Triggered when there is any change in the nested visual or the visual authoring configuration. The data passed in the event includes the visual authoring configuration (`e.detail.visualBuilder`).   ``` embeddedComponent.addEventListener("composer-visual-builder-changed", (e) => {      console.log(e.detail.visualBuilder); }); ``` |
| `composer-visual-builder-failed` | Triggered when visual authoring fails to load. The data passed in the event includes the visual builder data as well as the failure reason (`e.detail.failedReason`).   ``` embeddedComponent.addEventListener("composer-visual-builder-failed", (e) => {      console.log(e.detail.visualBuilder);      console.log(e.detail.failedReason); }); ``` |
| `composer-visual-builder-loaded` | Triggered when visual authoring is loaded and the visual authoring shell is rendered. The data passed in the event includes the visual authoring configuration (`e.detail.visualBuilder`).   ``` embeddedComponent.addEventListener("composer-visual-builder-loaded", (e) => {      console.log(e.detail.visualBuilder); }); ``` |
| `composer-visual-builder-ready` | Triggered when the nested visual is rendered. The data passed in the event includes the visual authoring configuration (`e.detail.visualBuilder`).   ``` embeddedComponent.addEventListener("composer-visual-builder-ready", (e) => {      console.log(e.detail.visualBuilder); }); ``` |

## Visual Events

| Event | Description |
| --- | --- |
| `composer-visual-failed` | Triggered by the dashboard or by visual authoring when a visual within the dashboard fails to load. The data passed in the event includes the visual and visual data as well as the failure reason (`failedReason`).   ``` embeddedComponent.addEventListener("composer-visual-failed", (e) => {      console.log(e.detail.visual);      console.log(e.detail.failedReason); }); ``` |
| `composer-visual-loaded` | Triggered by the dashboard or visual authoring when a visual within the dashboard is loaded. The data passed in the event includes the visual and visual data as well as the visualization instance ID (`e.detail.visual`).   ``` embeddedComponent.addEventListener("composer-visual-loaded", (e) => {      console.log(e.detail.visual); }); ``` |
| `composer-visual-rendered` | Triggered by the dashboard or visual authoring when a visual within the dashboard is fully rendered. The data passed in the event includes the visual and visual data as well as the visualization instance ID (`e.detail.visual`).   ``` embeddedComponent.addEventListener("composer-visual-rendered", (e) => {      console.log(e.detail.visual); }); ``` |
| `composer-visual-saved` | Triggered when visual authoring has been successfully saved. The data passed in the event includes the visual authoring configuration (`e.detail.visual`).   ``` vb.addEventListener("composer-visual-saved", (e) => {      console.log(e.detail.visual); }); ``` |
