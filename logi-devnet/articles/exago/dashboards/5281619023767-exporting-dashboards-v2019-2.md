---
title: "Exporting Dashboards (v2019.2+)"
id: 5281619023767
section: "Dashboards"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281619023767-Exporting-Dashboards-v2019-2
updated_at: 2022-05-03T22:09:10Z
---

# Exporting Dashboards (v2019.2+)

# Exporting Dashboards (*v2019.2+*)

Dashboards can be exported, scheduled and emailed as:

* **[Chained Reports](#Chained)** to any of the available export types (*Excel, PDF, RTF, CSV*). Each tile appears on a separate page in the output file.
* **[Snapshots](#Snapshot)** with a likeness of the Dashboard as it appears on screen in a single page PDF

In the examples below, consider this sample Dashboard:

![n8fhDuwAz0.png](https://devnet.logianalytics.com/hc/article_attachments/5432353048471/n8fhduwaz0.png)

Sample Dashboard in the Dashboard Viewer

## Chained Report Output Mode

Dashboards exported in this mode consist only of report and visualization tiles. Filter tiles are excluded from the Chained Report output but the default filter values apply to their affected tiles.

For a Dashboard exported as a Microsoft Excel Workbook, each tile appears as a separate worksheet tab in the output. For CSV exports, each report tile’s output will be in the output file, one right after the next. Visualization tiles will be blank lines.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The default values of the filters are reflected in the exported Dashboard even if the filter tiles have been adjusted before exporting.

When exported in Chained Report mode, the sample Dashboard looks like this:

![vHHkfH1mVm.png](https://devnet.logianalytics.com/hc/article_attachments/5432358941719/vhhkfh1mvm.png)

Each report or visualization tile appears in its own page of this PDF Chained Report output

## Snapshot Output Mode v2021.2+

Dashboards exported in this mode resemble a screenshot of the entire canvas, with a few exceptions:

* scroll bars, the Tile Menu icon, Refresh icon, Move handle, report page buttons and search bar on each tile do not appear in the output
* the floating Refresh, Filter and Parameters icons of the [Dashboard Viewer (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281602922903-Dashboard-Viewer-v2019-2-) do not appear in the output
* ExpressView Existing Report tiles appear in their exported view style, not as they do in the ExpressView Designer or on the Dashboard canvas
* Interactive Filter tiles appear with a summary of the tile’s filter settings

When exported as a Dashboard Snapshot, the sample Dashboard looks like this:

![](https://devnet.logianalytics.com/hc/article_attachments/5432211293847/foxitphantompdf_wua7f6xk4r.png)

The sample Dashboard exported as a Dashboard Snapshot

## How to Export a Dashboard

Dashboards may be exported from the ![MainLeftPaneViewReports.png](https://devnet.logianalytics.com/hc/article_attachments/5432210088471/mainleftpaneviewreports.png)**Report Tree** and the ![TabDashboardSelected.png](https://devnet.logianalytics.com/hc/article_attachments/5432340543255/tabdashboardselected.png)**Dashboard Designer**.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If at least one report tile on the Dashboard has no export types selected, exporting of the Dashboard is disabled.

### From the Report Tree

From the ![MainLeftPaneViewReports.png](https://devnet.logianalytics.com/hc/article_attachments/5432210088471/mainleftpaneviewreports.png)**Report Tree** by right-click the Dashboard name or by first select the report in the tree, then click the **Menu** ![hamburgermenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432296211479/hamburgermenu.png) icon, hover over ![ExportSmall.png](https://devnet.logianalytics.com/hc/article_attachments/5432331503255/exportsmall.png)**Export As** and then choose the preferred export type from the list.

![firefox_Vy3kcgUn9h.png](https://devnet.logianalytics.com/hc/article_attachments/5432225884183/firefox_vy3kcgun9h.png)

### From the Dashboard Designer

Export from the Dashboard Designer by clicking the **Export** ![Export.png](https://devnet.logianalytics.com/hc/article_attachments/5432274715543/export.png) icon in the toolbar then choosing an export file type.

![5h0alafxCt.png](https://devnet.logianalytics.com/hc/article_attachments/5432299957911/5h0alafxct.png)

If some export types shown here are not available, they may be restricted by the system administrator, or one or more of the component reports may restrict them in their respective **General Report Options**.

## Scheduling or emailing Dashboards

See [Scheduling Reports](https://devnet.logianalytics.com/hc/en-us/articles/5281531476375-Scheduling-Reports).
