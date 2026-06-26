---
title: "Creating Dashboards"
id: 4402537741463
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537741463-Creating-Dashboards
updated_at: 2021-09-15T02:20:54Z
---

# Creating Dashboards

# Creating Dashboards

Visuals and dashboards allow you to analyze your data in a variety of ways.

* A visual is a single view of data source data. They can be stored and added to dashboards using the Visual Gallery.
* A dashboard is a collection of one or more visuals. The visuals in a dashboard can be based on one data source or multiple data sources. For example, a single dashboard can contain two visuals using Solr, one using Impala, one using Elasticsearch, and another using a [fused data source](https://devnet.logianalytics.com/hc/en-us/articles/4402552819607-Fuse-Data-Sources). When you create a dashboard, you must also create at least one visual.

To create a dashboard and its initial visual:

1. Log into Composer as an administrator or a user who has been assigned to a group with the [**Can Administer Dashboards** privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402537668503-Group-Privilege-Reference).
2. Select **Library** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4402552863383-The-Top-Level-Navigation-Banner) or the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537848215-The-Composer-UI-Menu), or select the **Dashboards** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4402552851095-Home-Page). The dashboard library displays.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753498647/new-btn_104x22.png). A blank dashboard appears showing options to add a new visual or place an existing visual.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764036119/dashboard-new_480x211.png)
4. Select **Add Visual** to add a new visual to the dashboard. Select **Place Existing Visual** to place an existing visual on the dashboard.

   * If you select **Add Visual**, follow the procedure described in [*Adding New Visuals to a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402552936087-Adding-New-Visuals-to-a-Dashboard)
   * If you select **Place Existing Visual**, follow the procedure described in [*Placing Existing Visuals on a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402537946135-Placing-Existing-Visuals-on-a-Dashboard).
5. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4402537747863-Saving-a-Dashboard) your dashboard. You are prompted to supply a name for the dashboard. After it is saved, the dashboard is a single-visual dashboard until you add additional visuals to it. To add additional visuals to the dashboard, see [Adding New Visuals to a Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4402552936087-Adding-New-Visuals-to-a-Dashboard) and [*Placing Existing Visuals on a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402537946135-Placing-Existing-Visuals-on-a-Dashboard).

After a dashboard is created, you can explore its data and work directly with its various visuals. You can modify, copy, export or delete its visuals. In addition, the data on the visual can be filtered (see [*Filter Data*](https://devnet.logianalytics.com/hc/en-us/articles/4402552815383-Filter-Data)). Finally, you can share, export, or delete the dashboard (see [*Manage Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4402552774423-Manage-Dashboards)).
