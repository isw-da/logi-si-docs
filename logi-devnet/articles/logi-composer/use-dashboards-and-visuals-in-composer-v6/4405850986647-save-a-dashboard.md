---
title: "Save a Dashboard"
id: 4405850986647
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850986647-Save-a-Dashboard
updated_at: 2021-09-21T01:27:47Z
---

# Save a Dashboard

# Save a Dashboard

After you have added or placed at least one visual on a dashboard, you can save it. To view your saved dashboards, navigate to the [dashboard library](https://devnet.logianalytics.com/hc/en-us/articles/4405859273751-Use-the-Dashboard-Library).

When you attempt to save a dashboard, Composer determines whether any of the pre-existing visuals on the dashboard have changed on the dashboard since it was last saved and whether any new visuals have been added. A checkbox allows you to indicate whether to save existing visuals with unsaved changes when you save the dashboard. The default is not to save them. (New visuals you have added to a dashboard will always be saved with the dashboard.)

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) This is different from Composer dashboard save behavior in releases prior to 6.9. In older versions, all changed visuals were automatically saved with the dashboard. Effective with Composer 6.9, you must explicitly elect to save them on the dashboard Save Options dialog or they will not be saved.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) When you save a dashboard, only the last time bar field you were using and its range and playback configuration are saved.

The following factors affect a user's ability to save a dashboard and its visuals.

* The **Can Create Dashboards** [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) must be granted for the user (via one or more groups to which the user belongs).
* Write [permission](https://devnet.logianalytics.com/hc/en-us/articles/4405859259159-About-Dashboard-Permissions) for the dashboard must be granted to the user, one of the user's groups, or the user's Composer account. See [*About Dashboard Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859259159-About-Dashboard-Permissions).
* The visuals on the dashboard will only be saved if the user has been granted the **Can Create Visuals** (or **Can Administer Visuals**) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).
* The visuals on the dashboard will only be saved if write [permission](https://devnet.logianalytics.com/hc/en-us/articles/4405851253271-About-Visual-Permissions) for the visual has been granted to the user, one of the user's groups, or the user's Composer account. See [*About Visual Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851253271-About-Visual-Permissions).

To save a dashboard:

1. In the dashboard header, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743710231/dash-save.png) on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar). (The ![](https://devnet.logianalytics.com/hc/article_attachments/4406743877911/save-as_20x21.png) icon allows you to make a [copy](https://devnet.logianalytics.com/hc/en-us/articles/4405859260183-Copy-a-Dashboard) of the dashboard.)

   The Save Options dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743878935/save-options_288x245.png)

   The dialog contains two tabs: one listing existing visuals with unsaved changes and one listing new visuals that have been added since the last time the dashboard was saved.
2. In the **Name** box, enter a title for your dashboard. This is the name by which the dashboard will be saved.

   * If you want to save the dashboard using a different name, change it here. The original dashboard is renamed. See [*Rename a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859266583-Rename-a-Dashboard)
   * If you want to make a copy of a dashboard using a different name, see [*Copy a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859260183-Copy-a-Dashboard).
3. If you want to provide details about your dashboard, do this in the **Description** box. A maximum of 750 characters can be specified. Leading and trailing spaces are not allowed.
4. Review the list of existing visuals with unsaved changes on the **Existing Visuals** tab, if there are any.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743881879/existingvisuals_384x148.png)

   Select the checkbox on this tab to save the changes to the visuals. Leave the checkbox cleared if you do not want to save the changes to the existing visuals. When you save them, the visuals are changed on every dashboard on which they are used. If you do not save the visuals, your changes will be discarded when you close the dashboard (a warning dialog displays first).
5. Optionally, review the list of new visuals on the New Visuals tab, if there are any. New visuals are always saved when the dashboard is saved.
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743882391/save-blue-btn_42x23.png) to save the dashboard or ![](https://devnet.logianalytics.com/hc/article_attachments/4406747440279/cancel-btn_51x23.png) to cancel.
