---
title: "Copy a Dashboard"
id: 4405859260183
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859260183-Copy-a-Dashboard
updated_at: 2021-09-21T01:27:42Z
---

# Copy a Dashboard

# Copy a Dashboard

When you attempt to copy a dashboard, Composer determines whether any of the pre-existing visuals on the dashboard have changed since the dashboard was last saved and whether any new visuals have been added. You can copy a dashboard only if your user account has been granted the **Can Create Dashboards** [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) (via one or more groups to which your use account belongs).

An option to also create copies of all the pre-existing dashboard visuals may also be available. This option is only available if your user account has been granted the **Can Create Visuals** (or **Can Administer Visuals**) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

The following factors affect a user's ability to copy a dashboard and its visuals.

* The visuals on the dashboard will only be saved if write [permission](https://devnet.logianalytics.com/hc/en-us/articles/4405851253271-About-Visual-Permissions) for the visual has been granted to the user, one of the user's groups, or the user's Composer account. See [*About Visual Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851253271-About-Visual-Permissions).

To copy a dashboard:

1. In the dashboard header, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743886103/save-as_23x26.png) on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar). (The ![](https://devnet.logianalytics.com/hc/article_attachments/4406743886743/dash-save_19x19.png) icon allows you to [save](https://devnet.logianalytics.com/hc/en-us/articles/4405850986647-Save-a-Dashboard) the dashboard.)

   The Save As Options dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747442455/dash-save-as-dialog_288x240.png)
2. In the **Name** box, enter a **new** name for your dashboard. If you do not, an error will occur when you select **Save** at the end of this procedure.
3. If you want to provide details about your dashboard, do this in the **Description** box. A maximum of 255 characters can be specified. Leading and trailing spaces are not allowed.
4. Use the checkbox to indicate whether you also want to create copies of all pre-existing visuals on the dashboard.

   * If you select this option, copies of all the pre-existing visuals are made along with the copy of the dashboard. You will be able to edit the copies of the visuals.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) New unsaved visuals on the dashboard will not be copied when this option is selected. New visuals must first be saved before they can be copied. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4405850986647-Save-a-Dashboard) the dashboard and the new visual first.
   * If you do not select this option, a warning on the dialog indicates that any changes made to the pre-existing visuals will be carried over to the new dashboard and, if you have appropriate permissions, you can save or undo the visual changes on the new dashboard.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) New unsaved visuals on the dashboard will be removed from the copied dashboard. New visuals must first be saved before they can be used on another dashboard. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4405850986647-Save-a-Dashboard) the dashboard and the new visual first.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743882391/save-blue-btn_42x23.png) to copy the dashboard.
