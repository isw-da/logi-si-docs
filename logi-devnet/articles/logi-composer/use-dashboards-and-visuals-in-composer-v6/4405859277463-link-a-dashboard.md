---
title: "Link a Dashboard"
id: 4405859277463
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859277463-Link-a-Dashboard
updated_at: 2021-12-23T15:33:27Z
---

# Link a Dashboard

# Link a Dashboard

While working with your dashboard, you may need to analyze data from other dashboards.
You can link a visual from your dashboard to another dashboard. This allows you to quickly access other dashboards with related information. To link dashboards, you must have permissions to share and link dashboards. When linking one dashboard to another, you can elect to have the target dashboard inherit the filters from the source dashboard.

To link a dashboard visual to another dashboard
:

1. Open the dashboard you want to link.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743755031/dash-link.png) on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar). The Dashboard Links dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747435799/dashboard-links-dialog_192x116.png)
3. In the Dashboard Links dialog, select the plus sign next to the visual that you want to link. The section for the selected visual expands.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743862167/dashboard-links-dialog-exp_192x139.png)
4. Select **Choose a dashboard** and select the desired dashboard from the list.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743862551/dashboard-links-exp2_192x159.png)
5. By default, **Inherit Visual Filter** is on, meaning that the dashboard passes the filters currently used on the dashboard (or the filters applied based on what is selected when the dashboard link occurs) to the linked dashboard. If you do not want the filters from the dashboard carried over, switch off **Inherit Visual Filter**.

   The filters are only carried over if the dashboards are using the same data source configuration.
6. Close the dialog.
7. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4405850986647-Save-a-Dashboard) the dashboard to save the dashboard link settings for its visuals.
8. On the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) for the linked visual, a new option in the following format appears:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743862807/link-new.png)**Go to "<dashboard>"**

   Select this option to jump to the linked dashboard.

To navigate to a linked dashboard:

* Select the ![](https://devnet.logianalytics.com/hc/article_attachments/4406743862807/link-new.png)**Go to "<dashboard>"** link on the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu).
* You can also navigate to the linked dashboard by selecting **LINK** on the dashboard [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu).

To delete a dashboard link:

1. Open the dashboard containing the visual you want to unlink.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743755031/dash-link.png) on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar). The Dashboard Links dialog appears showing the links to other dashboards.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743862551/dashboard-links-exp2_192x159.png)
3. On the Dashboard Links dialog, select the visual and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743863063/delete-red_18x18.png). The link is removed.

   You must remove all links to a dashboard before you can delete the dashboard.
4. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4405850986647-Save-a-Dashboard) the dashboard to save the dashboard link settings for its visuals.
