> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Alerts

Use alerts to alert your end users when a metric reaches a specified threshold. Use the [user interface](#manage-alerts) or API to manage your alert definitions. These definitions describe an alert condition, determine a schedule to evaluate the alert condition, and how notifications are handled when an alert condition is met. See [Manage Alerts](#manage-alerts), [Create an Alert Definition](#create-an-alert-definition) and [Alerts API](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/alerts/alerts-api).

## Prerequisites

* Configure the mail service for Self-Service Analytics.
* Configure [dashboard alert link redirection](#configure-dashboard-alert-links).
* Ensure intended recipients have valid email addresses specified in their user account (user definitions).
* Grant the group privilege **Administer Alerts** or **Create Alerts** to users who you want to enable to create or administer alerts. Administrative users are granted these privileges' by default. See [Group Privilege Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).
* Grant users who receive alerts read access to the data sources used in alert conditions. If a user does not have read permission for a data source will not receive any alert notifications. The corresponding alert messages also appear in the scheduler report and the job scheduler. See [About Source Permissions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions).

<h2 id="manage-alerts">
  Manage Alerts
</h2>

Use the Alerts work area to manage all of the alerts associated with a dashboard. [Create](#create-an-alert-definition), [edit](#edit-alerts), and [delete](#delete-alerts) alerts, or temporarily [enable and disable](#disable-and-enable-alerts) alerts as needed.

To manage alerts, you must be logged in as a user belonging to a group with the [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) **Administer Alerts** or **Create Alerts**.

* Users with the privilege **Administer Alerts** and `DATA ACCESS` to the underlying data sources can manage all aspects of alerts associated with a dashboard.
* Users with the privilege **Create Alerts** can only manage the alerts they created for a dashboard.

### Access the Alerts Work Area

1. Open or [create a dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards) that contains one or more alerts. If you are creating an alert on a new dashboard, save the dashboard first to enable the Manage Alerts option.

2. Select **Manage Alerts** from the dashboard. The Alerts work area opens, listing existing alerts for this dashboard you can manage. Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/manage-alerts-dashboard.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=73f4a078ce9a98ed33861c675e0ed7c2" alt="Create, enable, disable, edit, or delete alerts for a dashboard" width="866" height="609" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/manage-alerts-dashboard.png" />

3. [Create](#create-an-alert-definition), [edit](#edit-alerts), and [delete](#delete-alerts) alerts, or temporarily [enable and disable](#disable-and-enable-alerts) alerts as needed.

   * Select **Create Alert** to create a new alert. See [Create an Alert Definition](#create-an-alert-definition).
   * Select the name of an alert to edit the alert. See [Edit Alerts](#edit-alerts).
   * Select the delete (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan-black.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=136b6c4981ae0ce343d31bfd990f10e8" alt="" width="17" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan-black.png" />) icon to delete the alert. See [Delete Alerts](#delete-alerts).
   * Select the toggle for an alert to enable or disable the alert. See [Disable and Enable Alerts](#disable-and-enable-alerts).

### Search Box

Use the search box to filter the alerts shown by Name. For example, if you type a **C** in the search box, only alerts that include the letter *C* in the selected field searched are shown in the working area.

### Buttons

The buttons in this work area allow you to create new alerts.

| Button | Description |
| - | - |
| Create Alert | Allows you to create a new alert. See [Create an Alert Definition](#create-an-alert-definition). |

### The Alerts List

Each column in the table is described below. The Name, Data Source, Last Modified, and Frequency columns are sortable.

| Column | Description |
| - | - |
| Enabled | Indicates if an alert is enabled or disabled. See [Disable and Enable Alerts](#disable-and-enable-alerts). |
| Name | The name you assigned to an alert. This name does not need to be unique. Select to edit the alert. See [Edit Alerts](#edit-alerts). |
| Data Source | The name of the data source used by the visual for an alert. |
| Last Modified | The time stamp indicating the last date and time the alert was modified. This can indicate the creation date if no modifications have been made since creation, the last time an edit was saved to an alert definition, or the last time an alert was enabled or disabled. |
| Frequency | How often an alert is run, as indicated in an alert definition’s schedule. See [Create an Alert Definition](#schedule) . |
| Delete | Delete an alert. See [Delete Alerts](#delete-alerts). |

<h2 id="create-an-alert-definition">
  Create an Alert Definition
</h2>

Use alerts to alert yourself and other users when a metric reaches a specified threshold. Use the user interface to create alert definitions. These definitions describe an alert condition, determine a schedule to evaluate the alert condition, and how notifications are handled when an alert condition is met.

To create an alert definition using the API, see [Create an Alert Definition - Alerts API](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/alerts/alerts-api#create-an-alert-definition-alerts-api).

Visuals that support alerts:

* Arc Gauge
* Bars
* Bars: Multiple Metrics
* Donut
* KPI
* Line Trend: Multiple Metrics
* Pie

### Create an Alert Definition from the Dashboard

To create an alert, you must be logged in as a user belonging to a group with the [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) **Administer Alerts** or **Create Alerts**.

1. Open or [create a dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards) that contains one or more visuals that support alerts. If you are creating an alert on a new dashboard, save the dashboard first to enable the Manage Alerts option.

2. Select **Manage Alerts** from the dashboard. The Alerts work area opens, listing existing alerts for this dashboard, if any. Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/manage-alerts-dashboard.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=73f4a078ce9a98ed33861c675e0ed7c2" alt="Create, enable, disable, edit, or delete alerts for a dashboard" width="866" height="609" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/manage-alerts-dashboard.png" />

3. Select **Create Alert** to create a new alert. The Select Visual for Alert work area opens.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/select-visual.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=2129b0d603b6314864fe4377b75208b8" alt="Select a supported visual to create an alert" width="864" height="608" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/select-visual.png" />

4. Select a supported visual to create a new alert for that visual. The Create Alert work area opens.

5. Enter a **Name** and optional **Description** for this alert in the Alert Details work area.

6. Accept the default Conditions, or select the edit icon to edit and **Apply** to apply your changes.

7. Accept the default Schedule, or select the edit icon to edit and **Apply** to apply your changes.

8. Accept the default Notification details, or select the edit icon to edit and **Apply** to apply your changes.

9. Select **Save** to save your alert. The Alerts work area opens, including your alert in the list.

### Create an Alert Definition from the Visual Menu

<Note>
  To create an alert, you must be logged in as a user belonging to a group with the [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) **Administer Alerts** or **Create Alerts**.
</Note>

<Note>
  If you create an alert definition using the Visual Menu, this alert is associated with the dashboard that contains the visual. If you use a visual in another dashboard, the alert does not carry over to the new dashboard.
</Note>

1. Open or [create a dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards) that contains one or more visuals that support alerts. If you are creating an alert on a new dashboard, save the dashboard first to enable the Manage Alerts option.

2. Select **Create Alert** from the [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) to create a new alert. The Create Alert work area opens. See [Alert Definition Fields and Options](#alert-definition-fields-and-options) for information about adjusting these fields to suit your organization's needs.

   <img src="https://mintcdn.com/insightsoftware/RaVF-aNRILP5orh5/simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/create-alert.png?fit=max&auto=format&n=RaVF-aNRILP5orh5&q=85&s=e7497e9cefd2f7f67166996b9947aaa7" alt="Use this work area to define the conditions and other details for alerts" width="859" height="608" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/create-alert.png" />

3. Enter a **Name** and optional **Description** for this alert in the Alert Details work area.

4. Accept the default Conditions, or select the edit icon to edit and **Apply** to apply your changes.

5. Accept the default Schedule, or select the edit icon to edit and **Apply** to apply your changes.

6. Accept the default Notification details, or select the edit icon to edit and **Apply** to apply your changes.

7. Select **Save** to save your alert.

<h2 id="edit-alerts">
  Edit Alerts
</h2>

Edit alerts directly on the dashboard. To edit alerts, you must be logged in as a user belonging to a group with the [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) **Administer Alerts** or **Create Alerts**.

* Users with the privilege **Administer Alerts** and `DATA ACCESS` to the underlying data sources can manage all aspects of alerts associated with a dashboard.
* Users with the privilege **Create Alerts** can only manage the alerts they created for a dashboard.

### Edit an Alert

1. Open a dashboard that contains one or more visuals that support alerts.

2. Select **Manage Alerts** from the dashboard. The Alerts work area opens, listing existing alerts for this dashboard. Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/manage-alerts-dashboard.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=73f4a078ce9a98ed33861c675e0ed7c2" alt="Create, enable, disable, edit, or delete alerts for a dashboard" width="866" height="609" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/manage-alerts-dashboard.png" />

3. Select the name of an alert to edit it. The Edit Alert work area opens.

4. You can edit any of the sections of the alert definition as needed. After you select **Apply** to apply your changes to the definition, you must save your edits for the alert.

   * Alert Details : Edit the **Name** and **Description** fields directly here.
   * Conditions: Select the edit icon to open the Edit Condition work area. Edit the conditions for this alert, then select **Apply** to apply your changes.
   * Schedule: Select the edit icon to open the Edit Schedule work area. Edit the schedule for this alert, then select **Apply** to apply your changes.
   * Notification: Select the edit icon to open the Edit Notification work area. Edit the notification information for this alert, then select **Apply** to apply your changes.

5. Select **Save** to save your alert. The Alerts work area opens, including your updated alert in the list.

<h2 id="delete-alerts">
  Delete Alerts
</h2>

If you no longer need an alert for a dashboard, use the Alerts work area to delete the alert permanently. Alternatively, [disable an alert](#disable-and-enable-alerts) temporarily if you're not sure if you will need an alert again later.

<Note>
  When you delete a dashboard permanently, all alerts associated with the dashboard are deleted as well.
</Note>

To delete alerts, you must be logged in as a user belonging to a group with the [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) **Administer Alerts** or **Create Alerts**.

* Users with the privilege **Administer Alerts** and `DATA ACCESS` to the underlying data sources can manage all aspects of alerts associated with a dashboard.
* Users with the privilege **Create Alerts** can only manage the alerts they created for a dashboard.

### Delete an Alert

1. Open a dashboard that contains one or more visuals that support alerts.

2. Select **Manage Alerts** from the dashboard. The Alerts work area opens, listing existing alerts for this dashboard. Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/manage-alerts-dashboard.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=73f4a078ce9a98ed33861c675e0ed7c2" alt="Create, enable, disable, edit, or delete alerts for a dashboard" width="866" height="609" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/manage-alerts-dashboard.png" />

3. Select the delete icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan-black.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=136b6c4981ae0ce343d31bfd990f10e8" alt="" width="17" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan-black.png" />) of an alert to delete it. A confirmation message opens.

4. Select **Delete** to confirm deletion of this alert.

<h2 id="disable-and-enable-alerts">
  Disable and Enable Alerts
</h2>

You can easily enable or disable an alert temporarily using the Alerts work area.

To disable alerts, you must be logged in as a user belonging to a group with the [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) **Administer Alerts** or **Create Alerts**.

* Users with the privilege **Administer Alerts** and `DATA ACCESS` to the underlying data sources can manage all aspects of alerts associated with a dashboard.
* Users with the privilege **Create Alerts** can only manage the alerts they created for a dashboard.

### Disable an Alert

1. Open a dashboard that contains one or more visuals that support alerts.

2. Select **Manage Alerts** from the dashboard. The Alerts work area opens, listing existing alerts for this dashboard. Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/manage-alerts-dashboard.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=73f4a078ce9a98ed33861c675e0ed7c2" alt="Create, enable, disable, edit, or delete alerts for a dashboard" width="866" height="609" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/manage-alerts-dashboard.png" />

3. Slide the Enabled toggle to the left for an alert to grey the toggle out, disabling the alert.

4. Self-Service Analytics automatically updates the alert definition, and updates the Last Modified field with the current date and time.

   No alerts are run or sent while the alert is disabled.

### Enable an Alert

1. Open a dashboard that contains one or more visuals that support alerts.

2. Select **Manage Alerts** from the dashboard. The Alerts work area opens, listing existing alerts for this dashboard.

   <img src="https://mintcdn.com/insightsoftware/RaVF-aNRILP5orh5/simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/manage-alerts-dashboard-disable.png?fit=max&auto=format&n=RaVF-aNRILP5orh5&q=85&s=e71d06c4b72db69311105b8bd1d9a45a" alt="Create, enable, disable, edit, or delete alerts for a dashboard" width="866" height="609" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/alerts/manage-alerts-dashboard-disable.png" />

3. Slide the Enabled toggle to the right for an alert to enable the alert.

4. Self-Service Analytics automatically updates the alert definition, and updates the Last Modified field with the current date and time.

   Alerts will now run and be sent when threshold conditions are met.

## Tracking Scheduled Alert Status

Use the [Console of Refreshing Jobs](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/console) to view scheduled alert jobs. Optionally, use the `/api/jobs` endpoint to list all jobs, including alert related jobs. For example:

```
http://<host:port>/composer/api/jobs?limit=1000&sort=-lastExecutionEndTime
```

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<h2 id="configure-dashboard-alert-links">
  Configure Dashboard Alert Links
</h2>

When you create an alert definition and set up email notification for alerts, Self-Service Analytics sends recipients your customized alerts message, which includes a link to the dashboard associated with the alert.

<Note>
  In all environments, `{Dashboard.id}` is resolved at run time for an alert's email notification.
</Note>

### Stand Alone Environment

Include the static fully qualified domain name for your Self-Service Analytics environment:

```properties theme={null}
alert.dashboard.link.template=${composer.schema}${zoomdata.base-url}/visualization/#{'$'}{Dashboard.id}
```

Where `{composer.schema}=#{${server.ssl.enabled}?'https':'http'}://` and `zoomdata.base-url=${server.address:localhost}:${server.port:8080}${server.servlet.context-path}`.

<h2 id="alert-definition-fields-and-options">
  Alert Definition Fields and Options
</h2>

Self-Service Analytics populates default field information and defines options related to the alert. This information is summarized in the [Create Alert](#create-an-alert-definition) and [Edit Alert](#edit-alerts) work areas. Select the edit icon to edit the information for each section.

#### Alert Details

| Field | Description |
| - | - |
| Name | Enter a name for the alert, shown in the Alerts work area. Must be unique. |
| Description | Optionally, enter a short description of this alert. 255 character maximum. |

#### Condition

| Field | Description |
| - | - |
| Time Range | Select a time range for this alert from [preset time ranges](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#preset-time-ranges). |
| Description | Optionally, enter a short description of this alert. 255 character maximum. |
| Metric | The metric, used in your visual, you are creating this alert condition about. |
| Group | The attribute, used in your visual, you are creating this alert condition about. |
| Operator | Select an available [operator](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#operators) for this alert. Not all operators may be available. |
| Value | Define the value of the metric that triggers this alert to be triggered. |

<h4 id="schedule">
  Schedule
</h4>

| Field | Description |
| - | - |
| Frequency | Select a frequency for the scheduled dashboard report using the arrows in the Frequency selection box. Frequencies of **Daily**, **Weekly**, **Monthly**, and **Run Once** are supported. Depending on the frequency you select, additional fields appear. |
| Run Time | This field only appears if the **Daily**, **Weekly**, or **Monthly** frequencies are selected. Specify the hour and minute of the day at which the alert should be generated and sent. Type the hour of the day on the left side of the colon and the minute of the day on the right side of the colon. Use the arrows in the box to the far right to select AM or PM. |
| From | This field only appears if the **Daily**, **Weekly**, or **Monthly** frequencies are selected. Select the starting date for the alert. Click in the box to bring up a calendar in which you can select the date. |
| To | This field only appears if the **Daily**, **Weekly**, or **Monthly** frequencies are selected. Select the ending date for the alert. Click in the box to bring up a calendar in which you can select the date. |
| Run on | This field only appears if the **Weekly** or **Monthly** frequencies are selected. When **Weekly** is selected, use the arrows in this selection box to select the day of the week on which the alert should run (Sunday, Monday, Tuesday, etc.). When **Monthly** is selected, use the arrows in this selection box to select the date in the month on which the alert should run (valid values range from 1 through 31). |
| Date | This field only appears if you select the **Run Once** frequency. Select the date for the alert. Click in the box to bring up a calendar in which you can select the date. |

#### Email Notification

<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>To</td>

      <td>
        The To text box contains your user name. Add more recipients here by typing their name or email address in this box. As you type in characters, Self-Service Analytics searches for and returns users that match your entry. Users must be defined in your environment to be added. See [Manage Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage).

        <br />

        You can also set up user attributes and use the [Recipient Rules API](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule#configure-recipient-rules) to specify who your users can see in the recipients list, and select from those users who to send the report to.

        <br />

        <Note>
          You must have at least one name in this field. An error message is returned if this field is blank.
        </Note>
      </td>
    </tr>

    <tr>
      <td>Subject</td>
      <td>Specify a subject for the email that will be sent containing the alert. By default, a subject of **Notification from \<alert-name>** is used.</td>
    </tr>

    <tr>
      <td>Message</td>
      <td>Optionally provide a message for the email. By default, a message of **A data threshold was crossed for \<alert-name>** is used.</td>
    </tr>
  </tbody>
</table>
