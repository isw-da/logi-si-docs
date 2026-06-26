---
title: "Dashboard Designer: Parameters (v2019.2+)"
id: 5281588292887
section: "Dashboards"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281588292887-Dashboard-Designer-Parameters-v2019-2
updated_at: 2022-05-03T22:09:10Z
---

# Dashboard Designer: Parameters (v2019.2+)

# Dashboard Designer: Parameters (*v2019.2+*)

When a report containing one or more parameters is added to a Dashboard existing report tile, those parameters are imported to the **![parameters](https://devnet.logianalytics.com/hc/article_attachments/5432356157463/parametersmenu.png)****Parameters** menu. Click on the toolbar **Parameters****![parameters](https://devnet.logianalytics.com/hc/article_attachments/5432356157463/parametersmenu.png)**![AccordionItemClosedArrow.png](https://devnet.logianalytics.com/hc/article_attachments/5432330506263/accordionitemclosedarrow.png) icon to open the Parameters popover menu.

Each imported parameter is shown as an item in the menu. For example, the **![parameters](https://devnet.logianalytics.com/hc/article_attachments/5432356157463/parametersmenu.png)****Parameters** menu below contains two parameters, one named **MyParameter** with a value *Teleportation*, and one named **EmployeeID** with the value *Johnson.*

![firefox_ER1HO01lbn.png](https://devnet.logianalytics.com/hc/article_attachments/5432339222807/firefox_er1ho01lbn.png)

Parameters menu with two parameters imported from reports on the canvas

If more than one report references the same parameter, it is grouped together into a **Consolidated Parameter**. This consolidation happens automatically. Clicking on any of the parameter items in the menu will open the **Parameter Item Detail** menu.

![eRyOdRL9mN.png](https://devnet.logianalytics.com/hc/article_attachments/5432299085463/eryodrl9mn.png)

Parameter Item Detail for a single report

![bnTskA7PWX.png](https://devnet.logianalytics.com/hc/article_attachments/5432225396503/bntska7pwx.png)

Parameter Item Detail for a consolidated parameter

The **Parameter** can be given a title by clicking on and entering it into the text field at the top of the menu. This title is used in the **Parameters Pane** of the **Dashboard Viewer** to more clearly identify it.

![firefox_4RTHyf5b0n.png](https://devnet.logianalytics.com/hc/article_attachments/5432339305239/firefox_4rthyf5b0n.png)

Providing a title for a Parameter in the Dashboard Designer

![firefox_wvaru9SWhP.png](https://devnet.logianalytics.com/hc/article_attachments/5432225421335/firefox_wvaru9swhp.png)

How the title in the Dashboard Viewer Parameters Pane appears

The name of the report or reports that imported this parameter are displayed under the title.

The parameter’s **Name** and **Value** are displayed, and the **Value** can be changed.

The corresponding tile names in the **Affected Tiles** section show which tiles are affected by the parameter. If two or more reports on the canvas have a parameter with the same name, those parameters are consolidated into a **consolidated parameter.** Click the **Group All**  button to consolidate all of the reports with the common parameter

In the example below, the *EmployeeID* parameter appears on two reports, *param-test1* and *param-test2*. In the **Parameter Item Detail** on the left, a **Group All** button allows consolidating all of the reports with the *EmployeeID* parameter. The resulting consolidated parameter is on the right.

**Consolidated Parameters** allow the Value to be changed for all of the reports simultaneously.

To break the consolidation, click the corresponding **ungroup** button.

![MbR9qbWCNs.png](https://devnet.logianalytics.com/hc/article_attachments/5432339380375/mbr9qbwcns.png)

becomes

![EN6fawFy40.png](https://devnet.logianalytics.com/hc/article_attachments/5432357027991/en6fawfy40.png)

The **On Execute** options work as follows:

* **Prompt for value** when checked will prompt the user to specify a value when the Dashboard is run. Otherwise the value in the menu is used when the Dashboard is run.
* **Show on****Output** when checked will show the parameter in the **Dashboard Viewer**‘s **Parameters Pane**. If unchecked, the filter will be hidden from the **Parameters P****ane** but will still affect the reports.
* **Set Default Value** when checked, will apply the **Value** specified in the Dashboard Designer to the parameter when the Dashboard is run. If unchecked, the parameter will use it’s own default value, if any, when the parameter is run.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Changing the value of a parameter will require a **Refresh** of any tiles affected by that parameter.

## Adding/Deleting Parameters

To **add** a parameter to a Dashboard, it must be included in one of the Dashboard’s component reports.

To **remove** a parameter from a Dashboard, remove it from the reports on the Dashboard.
