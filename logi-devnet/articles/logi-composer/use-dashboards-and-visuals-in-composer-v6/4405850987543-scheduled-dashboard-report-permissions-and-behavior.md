---
title: "Scheduled Dashboard Report Permissions and Behavior"
id: 4405850987543
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850987543-Scheduled-Dashboard-Report-Permissions-and-Behavior
updated_at: 2021-12-28T21:07:44Z
---

# Scheduled Dashboard Report Permissions and Behavior

# Scheduled Dashboard Report Permissions and Behavior

Specific permissions are required to create a scheduled dashboard report. In addition, specific things occur when the user who created the scheduled dashboard report is removed from the account or from the system and specific things occur when the report recipient is removed from the account or system.

To create a scheduled dashboard report, you must be an administrator or assigned to a group with the **Can Create Scheduled Reports** [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

The following table describes the scheduled dashboard report behaviors that occur when users are removed or disabled in Composer or in a Composer account.

| Who | Action | From | Behavior |
| --- | --- | --- | --- |
| Report creator | Disabled | Account | The scheduled dashboard report remains in the system and continues to be scheduled and delivered. |
| Removed | Account |
| Deleted | System | The scheduled dashboard report is removed from the system. |
| Report recipient | Disabled | Account | The recipient is not removed from the recipients list, however the recipient no longer receives the report. A warning message is logged. |
| Removed | Account |
| Removed | System | The recipient is removed from the recipients list. |

Log messages related to scheduled dashboard reports are stored in the `zoomdata.log`[log file](https://devnet.logianalytics.com/hc/en-us/articles/4405851142167-Composer-Log-Files).
