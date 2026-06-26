---
title: "Exporting Dashboards (pre-v2019.2)"
id: 5281610715287
section: "Dashboards"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281610715287-Exporting-Dashboards-pre-v2019-2
updated_at: 2022-05-03T22:09:11Z
---

# Exporting Dashboards (pre-v2019.2)

# Exporting Dashboards (*pre-v2019.2*)

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> This topic applies to *pre-v2019.2* of the application. For current Dashboard documentation, see [Dashboard Designer (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281580652951-Dashboard-Designer-v2019-2-).

You can export Dashboards in the form of Chained Reports**,** single multi-page documents. Each tile on the Dashboard is displayed on a single, separate page in the Chained Report. Dashboards can be exported to all export types (*Excel, PDF, RTF, CSV*) and can be emailed or scheduled. See [Chained Reports](https://devnet.logianalytics.com/hc/en-us/articles/5281546622615-Chained-Reports).

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Each tile displays in a separate worksheet tab in Excel exports.

## Export Options

Export options for Dashboards are found in both the Report Tree and the Dashboard Designer.

Export a Dashboard from the Report Tree by right-clicking the Dashboard name or highlighting it and clicking the ![hamburgermenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432296211479/hamburgermenu.png) menu, then open the *Export As* dropdown and choose the preferred export type.

![treexportoptions.png](https://devnet.logianalytics.com/hc/article_attachments/5432353488279/treexportoptions.png)

Export a**Dashboard** from the designer by clicking the ![dashexportoptionicon.png](https://devnet.logianalytics.com/hc/article_attachments/5432225923095/dashexportoptionicon.png) icon next to the **Run Dashboard** button and selecting an export type. See **[Dashboard Designer (pre-v2019.2)](https://devnet.logianalytics.com/hc/en-us/articles/5281595912983-Dashboard-Designer-pre-v2019-2-)**.

![dashdesignerexportoptions.png](https://devnet.logianalytics.com/hc/article_attachments/5432359221783/dashdesignerexportoptions.png)

If some export types shown here are not available, they may be restricted by the system administrator or one or more of the reports on the Dashboard may have export restrictions set in the **General Report Options**:

![EXPORToptions.png](https://devnet.logianalytics.com/hc/article_attachments/5432359244567/exportoptions.png)

Allowed Export Types in the Report Options dialog

## Dashboard Filters

Exported Dashboards consist only of visualization and report tiles. Filter tiles will be excluded from the Chained Report, but the default values set for each of the filters will apply to the relevant reports in the exported Dashboard.

In the example shown below, there is a filter tile controlling all of the reports and visualizations on the Dashboard with an “Is Between” filter on *Orders.OrderDate* with the default values of *01-01-2016* and *31-01-2016.* When this Dashboard is exported, the visualizations and reports in the export only display values between those dates.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The default values of the filters are reflected in the exported **Dashboard** even if the filter tiles have been adjusted in the executed **Dashboard**.

Filter settings:

![defaultvaluesfilterpane.png](https://devnet.logianalytics.com/hc/article_attachments/5432370570519/defaultvaluesfilterpane.png)

Filter settings

Exported Dashboard tiles as displayed in PDF format:

![exportedvisualizationfiltered.png](https://devnet.logianalytics.com/hc/article_attachments/5432370675095/exportedvisualizationfiltered.png)

![exportedtabularreportwdashfilterdfautls.png](https://devnet.logianalytics.com/hc/article_attachments/5432225987735/exportedtabularreportwdashfilterdfautls.png)

## Scheduling Dashboards

You also have the ability to schedule or email Dashboards. Scheduled Dashboards are stored as Chained Reports on the Scheduler with the same name or ID as the Dashboard. For example, the Dashboard titled “Revenue by Date Dashboard” will display as the same in the Schedule Manager.

![exportingdashboardsexportypes.png](https://devnet.logianalytics.com/hc/article_attachments/5432359381015/exportingdashboardsexportypes.png)

email a Dashboard

![schedulemanagerdashboardname.png](https://devnet.logianalytics.com/hc/article_attachments/5432331803799/schedulemanagerdashboardname.png)

How the previously emailed Dashboard appears in the Schedule Manager
