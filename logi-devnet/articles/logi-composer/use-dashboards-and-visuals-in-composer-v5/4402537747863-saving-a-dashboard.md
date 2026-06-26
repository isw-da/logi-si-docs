---
title: "Saving a Dashboard"
id: 4402537747863
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537747863-Saving-a-Dashboard
updated_at: 2021-09-15T02:20:57Z
---

# Saving a Dashboard

# Saving a Dashboard

When you have added at least one visual, you can save it as a dashboard. After your dashboard is saved, you can share it with other users in your account, allowing them to view and make edits to the dashboard. You can share the dashboard with other users in the same account. See [*Share a Dashboard with Users Inside Your Account*](https://devnet.logianalytics.com/hc/en-us/articles/4402552777623-Share-a-Dashboard-with-Users-Inside-Your-Account).

You can also save a dashboard with a new name. This creates a copy of the dashboard. See [*Copying a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402537740823-Copying-a-Dashboard).

To view your saved dashboards, you navigate back to the [dashboard library](https://devnet.logianalytics.com/hc/en-us/articles/4402537752983-Using-the-Dashboard-Library).

When you save a dashboard, only the last time bar field you were using and its range and playback configuration are saved.

Saving a dashboard requires one (or both) of the following authorization settings:

* The Can Create Dashboards [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402537668503-Group-Privilege-Reference) is enabled for the user (via one or more groups to which the user belongs).
* Write [permission](https://devnet.logianalytics.com/hc/en-us/articles/4402537739927-About-Dashboard-Authorization) is granted to the user, one of the user's groups, or the user's account.

To save a dashboard:

1. In the dashboard header, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753438615/dash-save.png) in the upper right corner of the dashboard.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406753495575/dash-save-dialog_192x106.png)
2. Select **Save** on the dialog. The Save Options dialog appears. (For information on what happens when you select the Save As option, see [*Copying a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402537740823-Copying-a-Dashboard).)

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764028439/save-options_288x240.png)

   The first time you save a dashboard or if you have made changes to the visuals on the dashboard, a list of the visuals that will also be saved in the Visual Gallery is shown on this dialog, so you can determine whether you want to save the dashboard. If no changes are made, the list of visuals does not appear on the dialog.

   The possible options for saving dashboards are described below:

   * **Save**: Saves the dashboard, overwriting the original dashboard with the same name. The original dashboard in the Library is updated with any changes made to the dashboard.
   * **Save As**: Saves the dashboard, with the applied changes, under a new name. A new dashboard appears in the Library with the new name. The original dashboard in the Library remains unchanged.
3. In the **Name** box, enter a title for your dashboard. This is the name by which the dashboard will be saved.

   * If you want to save the dashboard using a different name, change it here. The original dashboard is renamed. See [*Renaming a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402537747223-Renaming-a-Dashboard)
   * If you want to make a copy of a dashboard using a different name, see [*Copying a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402537740823-Copying-a-Dashboard).
4. If you want to provide details about your dashboard, do this in the **Description** box. A maximum of 750 characters can be specified. Leading and trailing spaces are not allowed.
5. Decide the save option for each visual in the dashboard.

   When you attempt to save or copy a dashboard, Composer determines whether any of the pre-existing visuals on the dashboard have changed since they were last saved. New visuals you have added to a dashboard will always be saved. Options for saving individual visuals on a dashboard are presented to you on the Save and Save As dialogs, based on the state of each visual (changed or unchanged), whether or not you authored (created) the visuals, and on the authorization settings of the user, as shown in the following table.

   | Authorization Settings | | Dashboard Save Option | Visual Save Options  (default in bold) |
   | --- | --- | --- | --- |
   | User Type | Can Manage Visuals PrivilegeSetting |
   | User with Administrator privileges (in the **Administrators**[group](https://devnet.logianalytics.com/hc/en-us/articles/4402552704919-About-Supplied-Group-Definitions)) | Enabled | **Save** | **Save** Save a Copy  Undo Changes |
   | **Save As** | Save  **Save a Copy** Undo Changes |
   | Author of the dashboard, but not the visual | Enabled | **Save** | **Save** Save a Copy Undo Changes |
   | **Save As** | Save **Save a Copy** Undo Changes |
   | Disabled | **Save** | Save a Copy **Undo Changes** |
   | **Save As** | **Save a Copy** Undo Changes |
   | Author of the visual, but not the dashboard | Enabled | **Save** | **Save** Save a Copy Undo Changes |
   | **Save As** | Save **Save a Copy** Undo Changes |
   | Disabled | **Save As** | Save **Save a Copy** Undo Changes |
   | Author of the dashboard and the visual | N/A | **Save** | **Save** Save a Copy Undo Changes |
   | **Save As** | Save **Save a Copy** Undo Changes |
   | User with whom the dashboard is [shared](https://devnet.logianalytics.com/hc/en-us/articles/4402537739927-About-Dashboard-Authorization) (read only authorization) | Enabled | **Save As** | Save **Save a Copy** Undo Changes |
   | Disabled | **Save As** | **Save a Copy** Undo Changes |
   | User with whom the dashboard is [shared](https://devnet.logianalytics.com/hc/en-us/articles/4402537739927-About-Dashboard-Authorization) (read and write authorization or read, write, and delete authorization) | Enabled | **Save** | **Save** Save a Copy Undo Changes |
   | **Save As** | Save **Save a Copy** Undo Changes |
   | Disabled | **Save** | Save a Copy **Undo Changes** |
   | **Save As** | **Save a Copy** Undo Changes |

   The possible options for saving visuals are described below:

   * **Save**: Saves the visual, overwriting the original visual with the same name. The original visual in the Visual Gallery is updated with any changes made for the visual in the dashboard.
   * **Save a Copy**: Saves the visual, with the applied changes, under a new name. A new visual appears in the Visual Gallery with the new name. The original visual in the Visual Gallery remains unchanged.
   * **Undo Changes**: Removes the changes made in the dashboard for the visual before saving the dashboard. The original visual in the Visual Gallery remains unchanged.
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753495831/save-blue-btn_42x23.png) to save the dashboard or ![](https://devnet.logianalytics.com/hc/article_attachments/4406764029335/cancel-btn_51x23.png) to cancel.
