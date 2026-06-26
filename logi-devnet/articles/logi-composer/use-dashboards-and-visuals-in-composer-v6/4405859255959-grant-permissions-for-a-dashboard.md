---
title: "Grant Permissions for a Dashboard"
id: 4405859255959
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859255959-Grant-Permissions-for-a-Dashboard
updated_at: 2021-09-21T01:27:41Z
---

# Grant Permissions for a Dashboard

# Grant Permissions for a Dashboard

You can grant read, write, or delete dashboard permissions for your account, groups in your account, or specific users in your account.

To grant permissions for a dashboard:

1. Log into Composer as an administrator or a user belonging to a group that includes the **Can Administer Dashboards** or the **Can Manage Dashboard Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).
2. Select **Library** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner) or the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu), or select the **Dashboards** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The dashboard library displays.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747437079/library_768x200.png)
3. Locate the row for the dashboard in the list and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747386135/permissions_16x16.png) in its Permissions column. The Dashboard Permissions dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747442967/dashboard-permissions_288x234.png)

   Initially, this dialog is empty.
4. Select **Add** on the Dashboard Permissions dialog and then select **Groups**, **Users**, or **Account** on the drop-down menu. If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your account. If you select **Users**, the Add Users dialog appears, listing all the users available in your account. If you select **Account**, Read permission is selected for your account on the Dashboard Permissions dialog.
5. Select the account or any specific groups or users you want to permit to read, write, or delete the dashboard and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743724055/apply-btn_70x23.png). The Dashboard Permissions dialog lists your selections.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743887127/dashboard-permissions1_288x234.png)

   Note that you cannot set dashboard permissions for the supplied group Administrators. Members of the Administrators group have read, write, and delete permissions for every dashboard in the account. Note also that the user who created the dashboard is automatically selected and has **Read**, **Write**, and **Delete** permissions.
6. Select the **Read**, **Write**, or **Delete** checkboxes for the account, groups, or users to indicate what users in them can do with the dashboard. **Read** permission is assumed and is always selected. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire dashboard is revoked for the account, group, or user after you save.
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743723159/save-blue2-btn_71x23.png). The Save Details dialog appears, listing the changes that you made.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743888023/dash-save-details_288x235.png)
8. Review the changes and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743723799/ok-btn_72x24.png). The dashboard permissions are set.
