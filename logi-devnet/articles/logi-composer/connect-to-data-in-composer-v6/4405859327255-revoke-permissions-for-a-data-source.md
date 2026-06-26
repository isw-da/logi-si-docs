---
title: "Revoke Permissions for a Data Source"
id: 4405859327255
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859327255-Revoke-Permissions-for-a-Data-Source
updated_at: 2021-09-21T01:28:19Z
---

# Revoke Permissions for a Data Source

# Revoke Permissions for a Data Source

You can revoke the data source configuration permissions you previously granted to your account, to groups in your account, or to specific users in your account.

To revoke permissions for a data source configuration:

1. Log into Composer as an administrator or a user belonging to a group that includes the **Can Administer Sources** or the **Can Manage Source Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).
2. Select **Sources** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner) or the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu), or select the **Sources** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The Sources page displays.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743821591/sources-page-permissions_768x301.png)
3. Locate the row for the data source configuration in the list and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747386135/permissions_16x16.png) in its Permissions column. The Source Permissions dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747423895/source-permissions1_288x222.png)
4. To completely revoke all source permissions for the account or for a group or user, locate the row for the account, group or user on the Source Permissions dialog and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743720599/trashcan-btn.png). The account, group, or user is removed from the dialog.

   You can also revoke specific permissions by changing the checkbox selections for the account or group on the Source Permissions dialog. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire data source configuration is revoked for the account, group, or user after you save. See [*Modify Permissions for a Data Source*](https://devnet.logianalytics.com/hc/en-us/articles/4405851031319-Modify-Permissions-for-a-Data-Source).
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743723159/save-blue2-btn_71x23.png). The Save Details dialog appears, listing the changes that you made.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743822359/source-permissions-saverevoke_288x225.png)
6. Review the changes and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743723799/ok-btn_72x24.png). The source permissions are set.
