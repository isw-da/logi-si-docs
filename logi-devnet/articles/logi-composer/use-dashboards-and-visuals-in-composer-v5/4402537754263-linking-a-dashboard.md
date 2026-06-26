---
title: "Linking a Dashboard"
id: 4402537754263
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537754263-Linking-a-Dashboard
updated_at: 2021-09-15T02:21:01Z
---

# Linking a Dashboard

# Linking a Dashboard

While working with your dashboard, you may need to analyze data from other dashboards.
You can link a visual from your dashboard to another dashboard. This allows you to quickly access other dashboards with related information. To link dashboards, you must have permissions to share and link dashboards. When linking one dashboard to another, you can elect to have the target dashboard inherit the filters from the source dashboard.

To link a dashboard visual to another dashboard
:

1. Open the dashboard you want to link.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406764015383/dash-link.png) on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4402537752343-Using-the-Dashboard-Icon-Bar). A drop-down menu allows you to select the kind of link you want to perform.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764015767/dash-link-options_192x96.png)
3. Select **Dashboard Links** on the menu. The Dashboard Links dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406753490839/dashboard-links-dialog_192x116.png)
4. In the Dashboard Links dialog, select the plus sign next to the visual that you want to link. The section for the selected visual expands.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764016279/dashboard-links-dialog-exp_192x139.png)
5. Select **Choose a dashboard** and select the desired dashboard from the list.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764016535/dashboard-links-exp2_192x159.png)
6. By default, **Inherit Visual Filter** is on, meaning that the dashboard passes the filters currently used on the dashboard (or the filters applied based on what is selected when the dashboard link occurs) to the linked dashboard. If you do not want the filters from the dashboard carried over, toggle off **Inherit Visual Filter**.

   The filters are only carried over if the dashboards are using the same data source configuration.
7. Close the dialog.
8. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4402537747863-Saving-a-Dashboard) the dashboard to save the dashboard link settings for its visuals.
9. On the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu) for the linked visual, a new option in the following format appears:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764016791/link-new.png)**Go to "<dashboard>"**

   Select this option to jump to the linked dashboard.

To navigate to a linked dashboard:

* Select the ![](https://devnet.logianalytics.com/hc/article_attachments/4406764016791/link-new.png)**Go to "<dashboard>"** link on the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu).
* You can also navigate to the linked dashboard by selecting **LINK** on the dashboard [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537934359-Using-the-Radial-Menu).

To delete a dashboard link:

1. Open the dashboard containing the visual you want to unlink.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406764015383/dash-link.png) on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4402537752343-Using-the-Dashboard-Icon-Bar). A drop-down menu allows you to select the kind of link you want to perform.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764015767/dash-link-options_192x96.png)
3. Select **Dashboard Links** on the menu. The Dashboard Links dialog appears showing the links to other dashboards.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764016535/dashboard-links-exp2_192x159.png)
4. On the Dashboard Links dialog, choose the visual and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753491351/delete-red_18x18.png). The link is removed.

   You must remove all links to a dashboard before you can delete the dashboard.
5. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4402537747863-Saving-a-Dashboard) the dashboard to save the dashboard link settings for its visuals.
