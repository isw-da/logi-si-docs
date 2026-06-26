---
title: "Disable and Enable Alerts"
id: 43701022538253
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701022538253-Disable-and-Enable-Alerts
updated_at: 2026-05-29T14:11:40Z
---

# Disable and Enable Alerts

# Disable and Enable Alerts

You can easily enable or disable an alert temporarily using the Alerts work area.

To disable alerts, you must be logged in as a user belonging to a group with the [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) **Administer Alerts** or **Create Alerts**.

* Users with the privilege **Administer Alerts** and `DATA ACCESS` to the underlying data sources can manage all aspects of alerts associated with a dashboard.
* Users with the privilege **Create Alerts** can only manage the alerts they created for a dashboard.

## Disable an Alert

1. Open a dashboard that contains one or more visuals that support alerts.
2. Select **Manage Alerts** from the dashboard. The Alerts work area opens, listing existing alerts for this dashboard.

   ![Create, enable, disable, edit, or delete alerts for a dashboard](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243352344333 "Manage Alerts work area")
3. Slide the Enabled toggle to the left for an alert to grey the toggle out, disabling the alert.
4. Logi Composer automatically updates the alert definition, and updates the Last Modified field with the current date and time.

   No alerts are run or sent while the alert is disabled.

## Enable an Alert

1. Open a dashboard that contains one or more visuals that support alerts.
2. Select **Manage Alerts** from the dashboard. The Alerts work area opens, listing existing alerts for this dashboard.

   ![Create, enable, disable, edit, or delete alerts for a dashboard](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242760174989 "Manage Alerts work area")
3. Slide the Enabled toggle to the right for an alert to enable the alert.
4. Logi Composer automatically updates the alert definition, and updates the Last Modified field with the current date and time.

   Alerts will now run and be sent when threshold conditions are met.
