---
title: "Logi Info Dashboard  "
id: 4419723074839
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723074839-Logi-Info-Dashboard
updated_at: 2022-07-17T02:23:54Z
---

# Logi Info Dashboard  

# Logi Info Dashboard

Dashboards provide an organized arrangement of visualizations in tabs and panels. Like all super-elements, they have a built-in user interface and specialized functionality.

The following topics introduce Logi Info *developers* to one of the "super-elements", the **Dashboard**:

* [Using the Dashboard Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707744535-Using-the-Dashboard-Element-#DashElement)
* [Using the Panel and Panel Content Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419707745559-Using-the-Panel-and-Panel-Content-Elements#PanelContent)
* [Working with Dashboard Tabs](https://devnet.logianalytics.com/hc/en-us/articles/4419707746711-Working-with-Dashboard-Tabs-#WorkTabs)
* [Saving Dashboard Settings](https://devnet.logianalytics.com/hc/en-us/articles/4419723075735-Saving-Dashboard-Settings-#SaveSettings)
* [Creating a Default Panel Arrangement](https://devnet.logianalytics.com/hc/en-us/articles/4419707741335-Creating-a-Default-Panel-Arrangement-#StarterFile)
* [Using Analysis Filters with Dashboards](https://devnet.logianalytics.com/hc/en-us/articles/4419723076759-Using-Analysis-Filters-with-Dashboards-#AnalysisFilters)
* [Using the Panel Parameters Element](https://devnet.logianalytics.com/hc/en-us/articles/4419715413911-Using-the-Panel-Parameters-Element-#PanelParameters)
* [Using the Refresh Element Timer](https://devnet.logianalytics.com/hc/en-us/articles/4419715414807-Using-the-Refresh-Element-Timer-#RefreshTimer)
* [Using Action.Add Dashboard Panel](https://devnet.logianalytics.com/hc/en-us/articles/4419707743255-Using-Action-Add-Dashboard-Panel-#AddDashPanel)
* [Customizing Dashboard Appearance](https://devnet.logianalytics.com/hc/en-us/articles/4419707742231-Customizing-Dashboard-Appearance-#Appearance)

Information about *using* a Dashboard, intended for *end-users*, is available in [Dashboard for End Users](https://devnet.logianalytics.com/hc/en-us/articles/4419715194903-Dashboard-for-End-Users).

## About the Dashboard

A Logi "Dashboard" is a collection of *Dashboard panels*, each containing a data visualization (table, chart, gauge, etc.). A Dashboard can be configured to allow end-users to customize it at runtime by
adding, removing, or rearranging its panels. A Dashboard can also be configured to have tabbed pages, so that different collections of Dashboard panels can be viewed. 
Dashboard panel content is interactive and end-users can be allowed to vary the data criteria for them at runtime. Links within the panels and visualizations can be used to drill-down and drill-through to supporting data.
Dashboards present a very flexible way of presenting a range of information that's easy to take in with a single glance.

![](https://devnet.logianalytics.com/hc/article_attachments/7522838405015/introdash_01.png)

A simple Dashboard, with no user customization features, styled using the standard *Signal* theme, is shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522838426135/introdash_02.png)

In the example above, we see a more complex Dashboard which includes tabs and has end-user customization enabled.
Dashboards are created using the **Dashboard** element, and its child elements, and they provide attributes that control customization features. AJAX-based techniques are used for web server interactions, allowing selective updates of Dashboard panels. There's also a mechanism for saving runtime customizations between sessions, on an individual-user basis.

### Dashboard Layout

A Dashboard or tab's layout usually consists of one or more *columns*
and, if the Dashboard is configured to be adjustable, users can
drag-and-drop the panels into the columns and the arrangement of their
choice.

![](https://devnet.logianalytics.com/hc/article_attachments/7522821883287/introdash_25.png)

If the Dashboard is adjustable, then using the Dashboard or tab's gear
icon and Settings menu, users can change the number of columns in a tab or
Dashboard, as shown above.
Depending on your application's configuration, a "Free-form Layout"
option may also available. If it's enabled, users can resize and rearrange
Dashboard panels without regard to any predetermined columns.

### Dashboard Panels

Dashboard panels are the basic building blocks of the Dashboard and can be added programmatically or dynamically at runtime.

![](https://devnet.logianalytics.com/hc/article_attachments/7522838457495/introdash_14.png)

As shown above, panels have a **Caption** and **content**, and may be configurable by users at runtime in other ways. If the Dashboard is adjustable, a panel can have its caption changed or be removed from its Dashboard via its Settings menu. If the panel has been created with parameters, users can adjust the parameter values, affecting the panel content.
In the definition, the **Panel** element creates a Dashboard panel. Its **Panel Content** and **Panel Parameters** child elements are used to create and configure the panel.

![](https://devnet.logianalytics.com/hc/article_attachments/7522792685591/introdash_26.png)

At runtime, users can drag a panel to a new location by clicking on its caption bar, as shown above (note the cursor change). As the panel is dragged into a different column or position, a yellow "drop zone" indicator appears to help snap the panel into its new location.
In a columnar layout, panels will automatically resize based on the
width of the column they're dropped into, and the column's width is
determined by the *widest panel* it contains. If the contents of a panel are widened, then the panel and its column will widen, too.
*This is a change from panel behavior in previous versions!* In a columnar layout, panels will automatically resize based on the width of the column they're dropped into. Column width is a *fixed width*,
determined by the layout chosen and screen width. Panel content will
be automatically scaled up to the maximum width that fits in the panel.
In support of this change, charts in panels in columnar layouts no
longer have horizontal resizing handles.

### The Dashboard Wizard

The "Create a Dashboard" wizard is one of Logi Studio's collection of wizards. This wizard assists developers in creating Dashboards by populating the report definition with the necessary Dashboard-related elements. More information about this wizard is available in our [Dashboard Wizard for Developers](https://devnet.logianalytics.com/hc/en-us/articles/4419700051607-Dashboard-Wizard-for-Developers).
