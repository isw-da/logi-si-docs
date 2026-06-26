---
title: "Analysis Chart - Adding Charts to Dashboards"
id: 4406816959255
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816959255-Analysis-Chart-Adding-Charts-to-Dashboards
updated_at: 2022-04-06T06:03:05Z
---

# Analysis Chart - Adding Charts to Dashboards

# Analysis Chart - Adding Charts to Dashboards

An exciting level of interaction between the Analysis Chart and the **Dashboard**
element is available. Users working with an Analysis Chart in one report, at
runtime, can generate a chart and then, with one mouse click,
add it as a new panel in an existing Dashboard in another report.

![](https://devnet.logianalytics.com/hc/article_attachments/4417591987095/workac_09.png)

When properly configured, the Analysis Chart will display an **Add To Dashboard** icon, as shown above.

## 

When the icon is clicked, the chart is added as a new panel
in the Dashboard, as shown above.

Behind the scenes, when the icon is clicked, the Analysis Chart writes the
underlying XML for its chart into the Dashboard's configuration file
(its "Save File"). In the Dashboard, the chart is inserted at the top of
Column 1; if Dashboard tabs are being used, the insertion occurs in the
currently active tab.

Just before panel insertion, the user will be prompted for the **Panel Title** and a description for display on
the Configuration Page.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584205975/workac_11.png)

The new chart panel thereafter appears in the Dashboard Configuration
Page, as shown above, just like any other panel, complete with a
thumbnail image. The new panel can be removed from the visible dashboard
panels and from the configuration page entirely, using the usual
controls.

The user can insert multiple tables and charts into a Dashboard using this technique.

![](https://devnet.logianalytics.com/hc/article_attachments/4417591987735/workac_12.png)

In the report definition, the developer makes this functionality available by adding a **Custom Dashboard Panels** element, shown above, beneath the Analysis Chart element. Its **Dashboard Save File** attribute value should be set to match the target dashboard's **Save File** attribute value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The Save File attribute values shown above have been shortened for
visual clarity. However, a fully-qualified path and file name, with .xml
extension, is required, so a realistic attribute value would be
something like:

@Function.AppPhysicalPath~\DashFiles\DashbdSave.xml

and the account the Logi application runs under must be given **Write**
permissions to the "DashFiles" folder. For experimentation purposes,
you can use the rdDownload folder, for which appropriate permissions
already exist (but its contents are periodically deleted, so don't use
it for anything but experimentation).

Dashboard Save Files are often named using a token, such as
@Function.UserName~, in order to create personalized dashboard
configurations and, in that case, the Custom Dashboard Panel attribute
would use the same token.

The Custom Dashboard Panels element has a new attribute, **Add Caption**, which sets the caption for the button used to save the data table or chart. If left blank, the caption is "Add to Dashboard".

For more information about Dashboards, see [Dashboard for End Users](https://devnet.logianalytics.com/hc/en-us/articles/4406817239447-Dashboard-for-End-Users).
