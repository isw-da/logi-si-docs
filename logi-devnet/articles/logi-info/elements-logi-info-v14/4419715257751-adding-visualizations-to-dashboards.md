---
title: "Adding Visualizations to Dashboards"
id: 4419715257751
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715257751-Adding-Visualizations-to-Dashboards
updated_at: 2022-07-17T02:24:32Z
---

# Adding Visualizations to Dashboards

# Adding Visualizations to Dashboards

An exciting level of interaction between the **Dimension Grid** and the **Dashboard** element is available. Users working with an Dimension Grid in one report, at runtime, can generate a table or chart and then, with one mouse click, add it as a new panel in an existing Dashboard in another report.

![](https://devnet.logianalytics.com/hc/article_attachments/7522814759831/xolapwork_16.png)

When properly configured, Dimension Grid table and charts will display an **Add To Dashboard** icon, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522814808983/xolapwork_17.png)

When the icon is clicked, the table or chart is added as a *new panel* in the Dashboard, as shown above. When the resizing control is used to resize a chart, the widths of the Dashboard columns and other panels will adjust dynamically.

Behind the scenes, when the icon is clicked, the Dimension Grid writes the underlying XML for its chart into the Dashboard's configuration file (its "Save File"). In the Dashboard, the chart is inserted at the top of Column 1; if Dashboard tabs are being used, the insertion occurs in the currently active tab.

Just before panel insertion, the user will be prompted for the **Panel Title** and a description for display on
the Configuration Page.

![](https://devnet.logianalytics.com/hc/article_attachments/7522829612567/xolapwork_18.png)

The new chart panel thereafter appears in the Dashboard Configuration Page, as shown above, just like any other panel, complete with a thumbnail image. The new panel can be removed from the visible Dashboard panels and from the configuration page entirely, using the usual controls.

The user can insert multiple tables and charts into a Dashboard using this technique.

![](https://devnet.logianalytics.com/hc/article_attachments/7522825733143/xolapwork_19.png)

To enable this functionality, the developer adds a **Custom Dashboard Panels** element, shown above, beneath an Dimension Grid element. Its **Dashboard Save File** attribute value should be set to match the target Dashboard's **Save File** attribute value.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The Save File attribute values shown above have been shortened for visual clarity. However, a fully-qualified path and file name, with .xml extension, is required, so a realistic attribute value would be something like:

@Function.AppPhysicalPath~\DashFiles\DashbdSave.xml

Dashboard Save Files are often named using a token, such as @Function.UserName~, in order to create personalized Dashboard configurations and, in that case, the Custom Dashboard Panel attribute would use the same token.

The Custom Dashboard Panels element's **Add Caption** attribute specifies the caption for the *button* used to save the Data Table or chart. If left blank, the default caption is "Add to Dashboard".

For more information about Dashboards, see [Logi Info Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4419723074839-Logi-Info-Dashboard-).
