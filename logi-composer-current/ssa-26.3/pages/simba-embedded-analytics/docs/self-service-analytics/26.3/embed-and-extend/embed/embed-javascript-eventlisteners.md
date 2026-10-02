> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Embedded Events

Events can be used in your JavaScript to control an embedded component when specific events occur.

<Note>
  The ability for your end users to perform some of the events listed here is controlled by the permissions granted to them with their Self-Service Analytics credentials. See [Embedded Self-Service Analytics Component Controls](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed-controls).
</Note>

Embedded events are described in the following tables:

* [Document Events](#document-events)
* [Dashboard Events](#dashboard-events)
* [Visual Authoring Events](#visual-authoring-events)
* [Visual Events](#visual-events)

Sample code showing how to subscribe to the events that trigger the event listeners is provided in each description. In these examples, when the event is triggered, a log message is written to the console. You can alter this behavior using custom JavaScript appropriate for your installation. For example, you can trigger a pop-up message (instead of a log message) using the Javascript `alert()` method instead of the `console.log()` method. For example: `alert("Dashboard has been loaded !!!");`

<Warning>
  The event detail payload that is passed to the event listener is **experimental** and might be changed. Mutating the detail object (`e.detail.*`) will not update the UI; the object is read-only.
</Warning>

<Note>
  Self-Service Analytics provides a `componentInstanceId` provides a as part of event details for dashboard, source, and visual events.
</Note>

<h2 id="document-events">
  Document Events
</h2>

<table>
  <thead>
    <tr>
      <th>Event</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`composer-init-failed`</td>

      <td>
        Triggered by document if the component fails to initialize. No data is passed in the event.

        <br />

        ```javascript theme={null}
        document.addEventListener("composer-init-failed", () => {
             console.log("composer-init-failed");
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-unauthorized`</td>

      <td>
        Triggered by document when the authorization token expires. No data is passed in the event.

        <br />

        ```javascript theme={null}
        document.addEventListener("composer-unauthorized", () => {
             console.log("composer-unauthorized");
        });
        ```
      </td>
    </tr>
  </tbody>
</table>

<h2 id="dashboard-events">
  Dashboard Events
</h2>

<table>
  <thead>
    <tr>
      <th>Event</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`composer-dashboard-changed`</td>

      <td>
        The trigger behavior of `composer-dashboard-changed` is defined by the setting `fireOnEveryChange`.

        <br />

        When `fireOnEveryChange` is enabled, dashboards and reports send out change events every time something is modified by user events, such as sorting, filtering, visual settings, and more. This expanded granularity makes it easier to track and respond to all user interactions within a dashboard or report. Events are sent as change events: `dashboard-level updates`, `visual-level updates`.

        <br />

        When `fireOnEveryChange` is disabled, only changes in the dashboard configuration are captured and passed. This is useful for tracking the active state of the dashboard. The data passed in the event includes the dashboard and dashboard data (`e.detail.dashboard`).

        <br />

        ```javascript theme={null}
        dashboard.addEventListener("composer-dashboard-changed", (e) => {
             console.log(e.detail.dashboard);
        });
        ```

        <br />

        Enable in the embed SDK configuration. See example.

        <br />

        ```javascript theme={null}
        const componentConfig = {
            // "originId": "",
            //"dashboardId": "XYZ",
            "fireOnEveryChange": false,
             //"reportId": "6926a66420d7ee252b297520",
           // "interactivityProfileName":"interactive",
          //  "theme":"__platform__",
           // "editor": { "placement": "modals" },
            "header": {
                "showActions": true,
                "showTitle": true,
                "visible": true
            },
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-dashboard-deleted`</td>

      <td>
        Triggered by the dashboard when the dashboard is deleted. The data passed in the event includes the dashboard and dashboard data (`e.detail.dashboard`).

        <br />

        ```javascript theme={null}
        dashboard.addEventListener("composer-dashboard-deleted", (e) => {
             console.log(e.detail.dashboard);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-dashboard-failed`</td>

      <td>
        Triggered by the dashboard when the dashboard fails to load. The data passed in the event includes the failure reason (`failedReason`).

        <br />

        ```javascript theme={null}
        dashboard.addEventListener("composer-dashboard-failed", (e) => {
             console.log(e.detail.failedReason);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-dashboard-loaded`</td>

      <td>
        Triggered when a dashboard resource is loaded. The data passed in the event includes the dashboard and dashboard data (`e.detail.dashboard`).

        <br />

        ```javascript theme={null}
        dashboard.addEventListener("composer-dashboard-loaded", (e) => {
             console.log(e.detail.dashboard);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-dashboard-ready`</td>

      <td>
        Triggered by the dashboard when all visuals on the dashboard have been rendered. The data passed in the event includes the dashboard and dashboard data (`e.detail.dashboard`).

        <br />

        ```javascript theme={null}
        dashboard.addEventListener("composer-dashboard-ready", (e) => {
             console.log(e.detail.dashboard);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-dashboard-saved`</td>

      <td>
        Triggered by the dashboard when a dashboard resource has been successfully saved. The data passed in the event includes the dashboard and dashboard data (`e.detail.dashboard`).

        <br />

        ```javascript theme={null}
        dashboard.addEventListener("composer-dashboard-saved", (e) => {
             console.log(e.detail.dashboard);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-dashboard-widget-added`</td>

      <td>
        Triggered by the dashboard when a visual is added to the dashboard. The data passed in the event includes the visual and visual data (`e.detail.visual`).

        <br />

        ```javascript theme={null}
        dashboard.addEventListener("composer-dashboard-widget-added", (e) => {
             console.log(e.detail.visual);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-dashboard-widget-removed`</td>

      <td>
        Triggered by the dashboard when a visual is removed from the dashboard. The data passed in the event includes the visual and visual data (`e.detail.visual`).

        <br />

        ```javascript theme={null}
        dashboard.addEventListener("composer-dashboard-widget-removed", (e) => {
             console.log(e.detail.visual);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-dashboard-pristine`</td>

      <td>
        Triggered by the dashboard when changes are made but not saved. The data passed in the event includes the dashboard and dashboard data (`e.detail.dashboard`).

        <br />

        ```javascript theme={null}
        dashboard.addEventListener("composer-dashboard-pristine", (e) => {
             console.log(e.detail.dashboard);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-dashboard-dirty`</td>

      <td>
        Triggered by the dashboard when there are no unsaved changes to the dashboard. The data passed in the event includes the dashboard and dashboard data (`e.detail.dashboard`).

        <br />

        ```javascript theme={null}
        dashboard.addEventListener("composer-dashboard-widget-removed", (e) => {
             console.log(e.detail.dashboard);
        });
        ```
      </td>
    </tr>
  </tbody>
</table>

<h2 id="visual-authoring-events">
  Visual Authoring Events
</h2>

<table>
  <thead>
    <tr>
      <th>Event</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`composer-visual-builder-changed`</td>

      <td>
        The trigger behavior of `composer-visual-builder-changed` is defined by the setting `fireOnEveryChange`.

        <br />

        When `fireOnEveryChange` is enabled, dashboards and reports send out change events every time something is modified by user events, such as sorting, filtering, visual settings, and more. This expanded granularity makes it easier to track and respond to all user interactions within a dashboard or report. Events are sent as change events: `dashboard-level updates`, `visual-level updates`.

        <br />

        When `fireOnEveryChange` is disabled, only changes in the nested visual or the visual authoring configuration are captured and passed. The data passed in the event includes the visual authoring configuration (`e.detail.visualBuilder`).

        <br />

        ```javascript theme={null}
        embeddedComponent.addEventListener("composer-visual-builder-changed", (e) => {
             console.log(e.detail.visualBuilder);
        });
        ```

        <br />

        Enable in the embed SDK configuration. See example.

        <br />

        ```javascript theme={null}
        const componentConfig = {
            // "originId": "",
            //"dashboardId": "XYZ",
            "fireOnEveryChange": false,
             //"reportId": "6926a66420d7ee252b297520",
           // "interactivityProfileName":"interactive",
          //  "theme":"__platform__",
           // "editor": { "placement": "modals" },
            "header": {
                "showActions": true,
                "showTitle": true,
                "visible": true
            },
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-visual-builder-failed`</td>

      <td>
        Triggered when visual authoring fails to load. The data passed in the event includes the visual builder data as well as the failure reason (`e.detail.failedReason`).

        <br />

        ```javascript theme={null}
        embeddedComponent.addEventListener("composer-visual-builder-failed", (e) => {
             console.log(e.detail.visualBuilder);
             console.log(e.detail.failedReason);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-visual-builder-loaded`</td>

      <td>
        Triggered when visual authoring is loaded and the visual authoring shell is rendered. The data passed in the event includes the visual authoring configuration (`e.detail.visualBuilder`).

        <br />

        ```javascript theme={null}
        embeddedComponent.addEventListener("composer-visual-builder-loaded", (e) => {
             console.log(e.detail.visualBuilder);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-visual-builder-ready`</td>

      <td>
        Triggered when the nested visual is rendered. The data passed in the event includes the visual authoring configuration (`e.detail.visualBuilder`).

        <br />

        ```javascript theme={null}
        embeddedComponent.addEventListener("composer-visual-builder-ready", (e) => {
             console.log(e.detail.visualBuilder);
        });
        ```
      </td>
    </tr>
  </tbody>
</table>

<h2 id="visual-events">
  Visual Events
</h2>

<table>
  <thead>
    <tr>
      <th>Event</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`composer-visual-failed`</td>

      <td>
        Triggered by the dashboard or by visual authoring when a visual within the dashboard fails to load. The data passed in the event includes the visual and visual data as well as the failure reason (`failedReason`).

        <br />

        ```javascript theme={null}
        embeddedComponent.addEventListener("composer-visual-failed", (e) => {
             console.log(e.detail.visual);
             console.log(e.detail.failedReason);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-visual-loaded`</td>

      <td>
        Triggered by the dashboard or visual authoring when a visual within the dashboard is loaded. The data passed in the event includes the visual and visual data as well as the visualization instance ID (`e.detail.visual`).

        <br />

        ```javascript theme={null}
        embeddedComponent.addEventListener("composer-visual-loaded", (e) => {
             console.log(e.detail.visual);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-visual-rendered`</td>

      <td>
        Triggered by the dashboard or visual authoring when a visual within the dashboard is fully rendered. The data passed in the event includes the visual and visual data as well as the visualization instance ID (`e.detail.visual`).

        <br />

        ```javascript theme={null}
        embeddedComponent.addEventListener("composer-visual-rendered", (e) => {
             console.log(e.detail.visual);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-visual-saved`</td>

      <td>
        Triggered when visual authoring has been successfully saved. The data passed in the event includes the visual authoring configuration (`e.detail.visual`).

        <br />

        ```javascript theme={null}
        vb.addEventListener("composer-visual-saved", (e) => {
             console.log(e.detail.visual);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-visual-series-mousemove`</td>

      <td>
        Triggered when a user hovers over one item in a series, such as a bar on a bar chart, or sector in a pie visual. The data passed in the event includes `componentInstanceId`, `visualApi`, and the current series in `e.detail`.

        <br />

        ```javascript theme={null}
        embeddedComponent.addEventListener("composer-visual-series-mousemove", (e) => {
        	console.log(e.detail.componentInstanceId);
        	console.log(e.detail.visualApi);
        	console.log(e.detail.data);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-visual-series-mouseout`</td>

      <td>
        Triggered when a user stops hovering over an item in a series, such as a bar on a bar chart, or sector in a pie visual.

        <br />

        ```javascript theme={null}
        embeddedComponent.addEventListener("composer-visual-series-mouseout", (e) => {
        	console.log(e.detail.componentInstanceId);
        	console.log(e.detail.visualApi);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-visual-mousemove`</td>

      <td>
        Triggered when a user hovers over a space that is empty but related to a visual, such as between the bars of a visual, or in a blank spot on a pie visual.

        <br />

        ```javascript theme={null}
        embeddedComponent.addEventListener("composer-visual-series-mousemove", (e) => {
        	console.log(e.detail.componentInstanceId);
        	console.log(e.detail.visualApi);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-visual-mouseout`</td>

      <td>
        Triggered when a user stops hovering the visual.

        <br />

        ```javascript theme={null}
        embeddedComponent.addEventListener("composer-visual-series-mouseout", (e) => {
        	console.log(e.detail.componentInstanceId);
        	console.log(e.detail.visualApi);
        });
        ```
      </td>
    </tr>
  </tbody>
</table>

## Source Editor Events

<table>
  <thead>
    <tr>
      <th>Event</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`composer-source-editor-ready`</td>

      <td>
        Triggered when the source editor is rendered the first time. The data passed in the event is `undefined`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-editor-ready", (e) =>{			console.log(e);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-source-definition-ready`</td>

      <td>
        Triggered when a source is loaded on Source Creation tab. The data passed in the event include the source definition: `e.detail.source`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-definition-ready", (e) => {	console.log(e.detail.source);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-source-fields-ready`</td>

      <td>
        Triggered when source fields are loaded on the Fields tab. The data passed in the event includes the source fields:`e.detail.fields`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-fields-ready", (e) => {
        	console.log(e.detail.fields);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-source-cache-ready`</td>

      <td>
        Triggered when source cache settings are loaded on the Cache tab. The data passed in the event includes the source cache settings: `e.detail.cache`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-cache-ready", (e) => {
        	console.log(e.detail.cache);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-source-settings-ready`</td>

      <td>
        Triggered when source global settings are loaded on the Global Settings tab. The data passed in the event includes the source global settings: `e.detail.settings`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-settings-ready", (e) => {
        	console.log(e.detail.settings);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-source-created`</td>

      <td>
        Triggered when a source is created. The data passed in the event includes the source definition: `e.detail.source`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-created", (e) => {
        	console.log(e.detail.source);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-source-saved`</td>

      <td>
        Triggered when a source is saved. The data passed in the event includes the source definition: `e.detail.source`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-saved", (e) => {
        	console.log(e.detail.source);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-source-field-created`</td>

      <td>
        Triggered when a source field is created. The data passed in the event includes the source field: `e.detail.field`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-field-created", (e) => {
        	console.log(e.detail.field);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-source-field-saved`</td>

      <td>
        Triggered when a source field is saved. The data passed in the event includes the source field: `e.detail.field`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-field-saved", (e) => {
        	console.log(e.detail.field);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-source-field-deleted`</td>

      <td>
        Triggered when a source field is deleted. The data passed in the event includes the source field: `e.detail.field`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-field-deleted", (e) => {
        	console.log(e.detail.field);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-source-metric-created`</td>

      <td>
        Triggered when a source metric is created. The data passed in the event includes the source metric: `e.detail.metric`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-metric-created", (e) => {
        	console.log(e.detail.metric);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-source-metric-saved`</td>

      <td>
        Triggered when a source metric is saved. The data passed in the event includes the source metric: `e.detail.metric`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-metric-saved", (e) => {
        	console.log(e.detail.metric);
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`composer-source-metric-deleted`</td>

      <td>
        Triggered when a source metric is deleted. The data passed in the event includes the source metric: `e.detail.metric`.

        <br />

        ```javascript theme={null}
        sourceEditor.addEventListener("composer-source-metric-deleted", (e) => {
        	console.log(e.detail.metric);
        });
        ```
      </td>
    </tr>
  </tbody>
</table>

## Embedded Library Events

Events can be used in your JavaScript to control an embedded Self-Service Analytics component when specific events occur.

<Note>
  The ability for your end-users to perform some of the events listed here is controlled by the permissions granted to them with their Self-Service Analytics credentials. See [Embedded Self-Service Analytics Component Controls](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed-controls).
</Note>

You can subscribe using .addEventListener() to embedded inventory component events so that you can execute your own logic when an event occurs.

<Note>
  Self-Service Analytics provides a `componentInstanceId` provides a as part of event details for dashboard, source, and visual events.
</Note>

The following events are supported:

<table>
  <thead>
    <tr>
      <th>Event</th>
      <th>Data Passed</th>
      <th>Example</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>composer-inventory-ready</td>
      <td>undefined</td>

      <td>
        ```javascript theme={null}
        inventory.addEventListener("composer-inventory-ready", (e) => { console.log(e); });
        ```
      </td>
    </tr>

    <tr>
      <td>composer-inventory-loaded</td>

      <td>
        Inventory items

        <br />

        e.detail.inventoryItems
      </td>

      <td>
        ```javascript theme={null}
        inventory.addEventListener("composer-inventory-loaded", (e) => { console.log(e.detail.inventoryItems); );
        ```
      </td>
    </tr>

    <tr>
      <td>composer-inventory-failed</td>

      <td>
        Failed reason

        <br />

        e.detail.failedReason
      </td>

      <td>
        ```javascript theme={null}
        inventory.addEventListener("composer-inventory-failed", (e) => { console.log(e.detail.failedReason); });
        ```
      </td>
    </tr>

    <tr>
      <td>composer-inventory-item-deleted</td>

      <td>
        Inventory item data

        <br />

        `e.detail.inventoryItem`
      </td>

      <td>
        ```javascript theme={null}
        inventory.addEventListener("composer-inventory-item-deleted", (e) => {
          console.log(e.detail.inventoryItem);
        }};
        ```
      </td>
    </tr>
  </tbody>
</table>
