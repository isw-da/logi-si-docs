---
title: "ReportCenter Menu"
id: 4406822493207
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822493207-ReportCenter-Menu
updated_at: 2022-04-06T06:08:24Z
---

# ReportCenter Menu

# ReportCenter Menu

Logi Info developers often have a requirement to provide a menu of the reports in their Logi application. The **ReportCenter**  family of elements provides an easy and flexible way to implement such a menu.

The following topics discuss the ReportCenter Menu elements:

* [Including Reports in the Menu](https://devnet.logianalytics.com/hc/en-us/articles/4406817819671-Including-Reports-in-the-Menu#Reports)
* [Creating the Menu](https://devnet.logianalytics.com/hc/en-us/articles/4406817818647-Creating-a-ReportCenter-Menu#Creating)
* [Scheduling Report Distribution](https://devnet.logianalytics.com/hc/en-us/articles/4406822494103-Scheduling-Report-Distribution#Distribution)

## About the ReportCenter Elements

The **ReportCenter**  elements provide a simple way to create a menu of report links that can be included in any report definition. They also provide a way to display and manage bookmarks (see [Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4406822405143-Bookmarks)), without needing to build these elements separately. And, finally, they provide a quick and easy way to create and manage email-based report distribution schedules without the need to build separate elements or use process tasks.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563099031/rptcenter_01_264x335.png)

An example of a typical menu is shown above. Menu items can be presented as:

1. Individual **Report** links
2. Report links grouped beneath a **menu****folder**
3. **Saved Bookmark** links - developers can enable option link icons to allow users to manage bookmarks and/or schedule them for delivery via email, at runtime.

Reports can be run in the current, or in a different, browser window and individual menu items can be dynamically shown or hidden in the menu, based on tokens and security rights.

As an element, the **ReportCenter Menu** sits within a report definition that you create, giving you the flexibility to position it and style it to match the surrounding page appearance, as desired.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The ReportCenter Menu *cannot* provide a menu of reports and bookmarks available in *multiple* Logi applications; its scope is limited to the Logi application in which the ReportCenter Menu element resides.

The menu background and border colors, border style, fonts, and other appearance-related qualities can be specified using container elements, themes, and/or style classes.

A [ReportCenter Menu Sample Application](https://devnet.logianalytics.com/hc/en-us/articles/360050239173-ReportCenter-Menu-Sample-Application) is available on DevNet and can be reviewed for more implementation examples. The following sections illustrate how the ReportCenter elements are used.

### Other Menu Variants

Logi Info also includes other menu elements you may wish to investigate; they may be more useful depending on the nature of your application. Pop-up menus display a panel with menu options and the Menu Tree menu, introduced in v12.1, can be used to create horizontal and vertical hierarchical menus. For more information see [Popup Menus](https://devnet.logianalytics.com/hc/en-us/articles/4406822654487-Popup-Menus) and [Menu Tree Menus](https://devnet.logianalytics.com/hc/en-us/articles/4406822648983-Menu-Tree-Menus).
