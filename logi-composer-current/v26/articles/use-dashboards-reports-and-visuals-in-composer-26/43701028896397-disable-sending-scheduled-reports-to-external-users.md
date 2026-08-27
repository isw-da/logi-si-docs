---
title: "Disable Sending Scheduled Reports to External Users"
id: 43701028896397
section: "Use Dashboards, Reports  and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701028896397-Disable-Sending-Scheduled-Reports-to-External-Users
updated_at: 2026-08-26T07:09:32Z
---

# Disable Sending Scheduled Reports to External Users

# Disable Sending Scheduled Reports to External Users

You can send scheduled self service reports and dashboard reports, by default, to both users with Composer accounts, and email addresses outside of Composer.

Disable the sending of scheduled reports by disabling the toggle `allow-sending-reports-to-external-emails`.See [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables).

## Logi Composer Scheduled Report Options - External Recipients Disabled

By default, you can send reports to external users by adding their email address to the Recipient field when creating a schedule for a report. When you disable sending reports to external users:

* Users can no longer add external email addresses to report schedules.
* External users included in an existing schedule remain, with an added warning that the report will not be sent to external users. This does not prevent the report from being sent to Composer users.
* If you remove an external user from a scheduled report, they can not be re-added to the recipient list.
* Reports that include external users in the recipient list are sent to Composer users only, not external users.
