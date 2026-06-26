---
title: "Modify Permissions for a Visual"
id: 4402963107223
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963107223-Modify-Permissions-for-a-Visual
updated_at: 2021-08-07T17:33:04Z
---

# Modify Permissions for a Visual

# Modify Permissions for a Visual

You can modify the visual permissions you granted to your account, to groups in your account, or to specific users in your account.

To modify permissions for a visual:

1. Log into Composer as an administrator or a user belonging to a group that includes the **Can Administer Visuals** or the **Can Manage Visual Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference).
2. Access the Visual Permissions dialog. There are two ways to do this.

   * Select **Visual Gallery** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4402963039639-The-Top-Level-Navigation-Banner) or the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4402963040407-The-Composer-UI-Menu), or select the **Visuals** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4402963020951-Home-Page). The Visuals page appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404952782231/visual-gallery_576x243.png)

     Then locate the row for the visual in the list and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959485079/permissions_16x16.png) in its Permissions column.
   * Select **Permissions** on the More (![](https://devnet.logianalytics.com/hc/article_attachments/4404952786071/three-dots-menu.png)) menu of the visual in a dashboard.

   The Visual Permissions dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952790807/visual-permissions_288x224.png)
3. If you want to add permissions for all users in your account or for additional groups or users in your account, select **Add** on the Visual Permissions dialog and then select **Groups**, **Users**, or **Account** on the drop-down menu. If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your account. If you select **Users**, the Add Users dialog appears, listing all the users available in your account. If you select **Account**, Read permission is selected for your account on the Visual Permissions dialog. When finished, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952791575/apply-btn_70x23.png).

   Note that you cannot set visual permissions for the supplied group Administrators. Members of the Administrators group have read, write, and delete permissions for every visual in the account. Note also that the user who created the visual is automatically selected and has **Read**, **Write**, and **Delete** permissions, although these permissions can be changed.
4. Modify the **Read**, **Write**, or **Delete** checkbox selections for the accounts or any of the users or groups on the Visual Permissions dialog to indicate what users in them can do with the visual. **Read** permission is assumed and is always selected. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire visual is revoked for the account, group, or user after you save.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952791063/save-blue2-btn_71x23.png). The Save Details dialog appears, listing the changes that you made.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404959486359/visual-permissions-savemod_288x224.png)
6. Review the changes and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952791319/ok-btn_72x24.png). The visual permissions are set.
