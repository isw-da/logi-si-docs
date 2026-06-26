---
title: "Scheduled Dashboard Report Permissions and Behavior"
id: 34932823947149
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932823947149-Scheduled-Dashboard-Report-Permissions-and-Behavior
updated_at: 2026-05-26T22:06:57Z
---

# Scheduled Dashboard Report Permissions and Behavior

# Scheduled Dashboard Report Permissions and Behavior

Users who create scheduled dashboard reports require specific permissions to perform these tasks. When you make changes to user accounts, these changes also affect scheduled reports in specific ways. This topic describes actions and Composer behaviors.

To create a scheduled dashboard report, you must be an administrator or assigned to a group with the **Create Scheduled Reports** and **Administer Scheduled Reports**[privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).

The following table describes the scheduled dashboard report behaviors that occur when users are removed or disabled in Composer or in a Composer account.

| Who | Action | From | Behavior |
| --- | --- | --- | --- |
| Report creator | Disabled | Tenant | The scheduled dashboard report remains in the system. Composer recipients continue to receive scheduled reports. All recipients included only by email address are removed from the report recipient list. |
| Removed | Tenant |
| Deleted | System | The scheduled dashboard report is removed from the system. |
| Report recipient | Disabled | Tenant | The Composer recipient remains on the recipients list but the recipient no longer receives the report. A warning message is logged. |
| Removed | Tenant |
| Removed | System | The Composer recipient is removed from the recipients list. |

Log messages related to scheduled dashboard reports are stored in the `zoomdata.log`[log file](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933097277069-Composer-Log-Files-Reference).
