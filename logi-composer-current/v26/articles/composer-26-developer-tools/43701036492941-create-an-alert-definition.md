---
title: "Create an Alert Definition"
id: 43701036492941
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036492941-Create-an-Alert-Definition
updated_at: 2026-05-29T14:11:41Z
---

# Create an Alert Definition

# Create an Alert Definition

Use alerts to alert yourself and other users when a metric reaches a specified threshold. Use the Logi Composer UI to create alert definitions. These definitions describe an alert condition, determine a schedule to evaluate the alert condition, and how notifications are handled when an alert condition is met.

To create an alert definition using the Logi Composer API, see [Create an Alert Definition - Alerts API](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701052414221-Create-an-Alert-Definition-Alerts-API).

Visuals that support alerts:

* Arc Gauge
* Bars
* Bars: Multiple Metrics
* Donut
* KPI
* Line Trend: Multiple Metrics
* Pie

## Create an Alert Definition from the Dashboard

To create an alert, you must be logged in as a user belonging to a group with the [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) **Administer Alerts** or **Create Alerts**.

1. Open or [create a dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076467981-Create-Dashboards) that contains one or more visuals that support alerts. If you are creating an alert on a new dashboard, save the dashboard first to enable the Manage Alerts option.
2. Select **Manage Alerts** from the dashboard. The Alerts work area opens, listing existing alerts for this dashboard, if any.

   ![Create, enable, disable, edit, or delete alerts for a dashboard](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243376823309 "Manage Alerts work area")
3. Select **Create Alert** to create a new alert. The Select Visual for Alert work area opens.

   ![Select a supported visual to create an alert](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242745003149 "Select Visual work area")
4. Select a supported visual to create a new alert for that visual. The Create Alert work area opens.
5. Enter a **Name** and optional **Description** for this alert in the Alert Details work area.
6. Accept the default Conditions, or select the edit icon to edit and **Apply** to apply your changes.
7. Accept the default Schedule, or select the edit icon to edit and **Apply** to apply your changes.
8. Accept the default Notification details, or select the edit icon to edit and **Apply** to apply your changes.
9. Select **Save** to save your alert. The Alerts work area opens, including your alert in the list.

## Create an Alert Definition from the Visual Menu

**Note:** 
To create an alert, you must be logged in as a user belonging to a group with the [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) **Administer Alerts** or **Create Alerts**.

**Note:**  If you create an alert definition using the Visual Menu, this alert is associated with the dashboard that contains the visual. If you use a visual in another dashboard, the alert does not carry over to the new dashboard.

1. Open or [create a dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076467981-Create-Dashboards) that contains one or more visuals that support alerts. If you are creating an alert on a new dashboard, save the dashboard first to enable the Manage Alerts option.
2. Select **Create Alert** from the [visual sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) to create a new alert. The Create Alert work area opens. See [Alert Definition Fields and Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701022616717-Alert-Definition-Fields-and-Options) for information about adjusting these fields to suit your organization's needs.

   ![Use this work area to define the conditions and other details for alerts](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242773743117 "Create Alert work area")
3. Enter a **Name** and optional **Description** for this alert in the Alert Details work area.
4. Accept the default Conditions, or select the edit icon to edit and **Apply** to apply your changes.
5. Accept the default Schedule, or select the edit icon to edit and **Apply** to apply your changes.
6. Accept the default Notification details, or select the edit icon to edit and **Apply** to apply your changes.
7. Select **Save** to save your alert.
