---
title: "Modify Permissions for a Data Source"
id: 4405851031319
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851031319-Modify-Permissions-for-a-Data-Source
updated_at: 2021-09-21T01:28:18Z
---

# Modify Permissions for a Data Source

# Modify Permissions for a Data Source

You can modify the data source configuration permissions you granted to your account, to groups in your account, or to specific users in your account.

To modify permissions for a data source configuration:

1. Log into Composer as an administrator or a user belonging to a group that includes the **Can Administer Sources** or the **Can Manage Source Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).
2. Select **Sources** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner) or the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu), or select the **Sources** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The Sources page displays.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743821591/sources-page-permissions_768x301.png)
3. Locate the row for the data source configuration in the list and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747386135/permissions_16x16.png) in its Permissions column. The Source Permissions dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747423895/source-permissions1_288x222.png)
4. If you want to add permissions for all users in your account or for additional groups or users in your account, select **Add** on the Source Permissions dialog and then select **Groups**, **Users**, or **Account** on the drop-down menu. If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your account. If you select **Users**, the Add Users dialog appears, listing all the users available in your account. If you select **Account**, Read permission is selected for your account on the Source Permissions dialog. When finished, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743724055/apply-btn_70x23.png).

   Note that you cannot set source permissions for the supplied group Administrators. Members of the Administrators group have read, write, and delete permissions for every data source configuration in the account. Note also that the user who created the data source configuration is automatically selected and has **Read**, **Write**, and **Delete** permissions, although these permissions can be changed.
5. Modify the **Read**, **Write**, or **Delete** checkbox selections for the accounts or any of the users or groups on the Source Permissions dialog to indicate what users in them can do with the data source. **Read** permission is assumed and is always selected. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire data source is revoked for the account, group, or user after you save.
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743723159/save-blue2-btn_71x23.png). The Save Details dialog appears, listing the changes that you made.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743825815/source-permissions-savemod_288x223.png)
7. Review the changes and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743723799/ok-btn_72x24.png). The source permissions are set.
