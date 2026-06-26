---
title: "Linked Reports (Drilldowns)"
id: 5281533707031
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281533707031-Linked-Reports-Drilldowns
updated_at: 2022-05-03T22:09:23Z
---

# Linked Reports (Drilldowns)

# Linked Reports (Drilldowns)

**Linked Reports**are reports linked from cells or charts as a means of exploring data points by “drilling down” into their background data. Use the Advanced Report Designer to add them.

The terms **Linked Reports** and **Drilldowns** are used interchangeably throughout the application and this topic, but they refer to the same concept.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Drilldowns work in the **Report Viewer** and **Dashboard Viewer**, but the linked data is not included in exported reports or Dashboards.

![AhY7cOv9cS.png](https://devnet.logianalytics.com/hc/article_attachments/5432403582999/ahy7cov9cs.png)

Drilling down from a column chart by clicking one of the chart elements

![OKONYZJsf7.png](https://devnet.logianalytics.com/hc/article_attachments/5432429426455/okonyzjsf7.png)

Drilling down from report data by clicking on the data in the cell

**Drilldowns** require a *child report*, which can be an **Dashboard**, **Advanced**, **CrossTab** or **Express Report** that contains the background data for the *parent report*. Drilldowns can be created on a Dynamic Cell or a chart by linking to the *child report* from the *parent report.* Clicking each cell value or chart series will filter the *child report* by its respective value before opening it. Depending on system configuration, the *child report* will open at the mouse cursor location, in the center of the screen or in a new report tab.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Currently, the prompt window will not appear when drilling down into a *child report* that contains prompting parameters. However, this can be partially bypassed by adding the prompting parameter in a hidden cell on the *parent report* so that the user will be prompted at runtime for the parameter value.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Adding a drilldown to a cell may override or interfere with any linked **Action Event** on the cell. Adding a linked report to a chart may override some aspects of the chart’s basic interactivity.

Since drilldowns are themselves reports they can have visualizations, be exported, and even have their own drilldowns.

## Linking Types

### Default Linking

By default, the **Data Field** in the *parent report’s* linking cell filters the closest joined **Data Field** on the *child report*. The topic on Joins has more information on data field joining. If there is no direct join path, then fields may be linked manually in the **Fields** tab of the **Linked Report Wizard**.

For example, a parent report links an *Employees* data field to a child report with an *Orders* category. The two categories are joined on `Orders.EmployeeId >> Employees.Id`. For each *Employees* row, its `Employee.Id` value filters the linked report down to the Order rows with matching `Orders.EmployeeId` values. Therefore, clicking on an Employee name in the *parent report* will drilldown to a list of orders that the employee made.

![screen.link_child.png](https://devnet.logianalytics.com/hc/article_attachments/5432403672727/screen.link_child.png)  
![screen.link_parent_with_child.png](https://devnet.logianalytics.com/hc/article_attachments/5432438638487/screen.link_parent_with_child.png)  

Orders linked report filtered by Employee Id

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Linking filters do not cascade down to *grand-children*, or child reports of the linked report.

### Manually Defining Link Fields

To link on different fields or categories than the default link, use the **Fields** tab of the **Linked Report Wizard**. The *From* fields from the parent report filter the *To* fields on the child report. The Fields tab is suitable for the following situations:

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> The **From** fields from the *parent report* filter the **To** fields on the *child report*.

* The default join is not the desired link to use  
  **Example**: Linking on related fields other than the Id field, such as “Region”  
  `Employees.Region >> Orders.ShipRegion`
* No join exists between the From and To categories  
  **Example**: Categories have related fields but are not joined, such as Orders and Suppliers  
  `Orders.ShipCity >> Suppliers.City`
* The From and To categories are the same  
  **Example**: Fields are related to other fields in the category, such as Employee X supervises Employees Y and Z  
  `Employees.Id >> Employees.ReportsTo`

### Conditionally Link with Formula

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This feature is disabled in system configuration by default. Contact the system administrator for more information.

Use the **Formula** tab of the **Linked Report Wizard** to conditionally enable drilldowns on specific values. By default, once a drilldown is setup, all records on the report can drilldown to the child. By adding a Formula, only values meeting the condition will permit drilling.

The formula must return *True* or *False*. The formula is evaluated for each row in the *parent report*, and if the condition is not met, drilling down to the *child report* is not enabled.

For example, the following formula could be used to create a drilldown to a report showing a suppliers list if and only if there are items on order or the quantity in stock is less than the product’s reorder level. Those products that do not meet that criteria cannot be drilled down.

```
Or({Products.UnitsOnOrder} > 1, {Products.UnitsInStock} <= {Products.ReorderLevel})
```

![FoxitReader_PHwd6gTCqp.png](https://devnet.logianalytics.com/hc/article_attachments/5432429501847/foxitreader_phwd6gtcqp.png)

Therefore, only *Queso Cabrales*, *Gorgonzola Telino*, and *Marscarpine Fabioli* meet the criteria. Clicking on the other products will have no effect.

## Dashboards as Child Reports

Beginning in *v2019.2+*, Dashboards can be drilled down to as *child reports*. Dashboard Drilldowns open in the standard Dashboard Viewer in a new tab. There are a few special considerations when drilling down to a Dashboard:

When drilling down to a Dashboard, filters on the *parent report* will affect the Dashboard tiles differently.

**Linking filters** are filters created during the linking process. **Interactive filters** are filters created on a Dashboard, or from Report Viewer Options in the Report Designer.

**Report Filters** are filters created in the *parent report* using either the Report Wizard or the Filters menu of the Report Designer.

| Tile Type | Linking Filter Behavior | Report Filter Behavior |
| --- | --- | --- |
| Existing TreeAdvancedReport.pngAdvanced, TreeExpressReport.pngExpress or TreeAdvancedReport.pngCrossTab Report | if the **Filter Field** is already on the report in the tile, or if it can be directly joined to the other Data Objects on the report, the filter is applied to the tile. | if the **Filter Field** is already on the report in the tile, the filter is applied to the tile. If not, the filter is not applied. |
| Existing TreeExpressView.pngExpressView | if the **Filter Field** is already on the report in the tile, or if it can be directly or indirectly joined to the other Data Objects on the report, the filter is applied to the tile. |
| Visualization | if the **Filter Field** is already in the visualization in the tile, or if it can be directly or indirectly joined to the other Data Objects in the visualization, the filter is applied to the tile. |

In the Dashboard Viewer’s Filters Pane, all filters that are a result of the linking process except for non-prompting filters from the *parent report* are visible.  
These filters are:

1. Filters from the Fields tab of the Linked Report Wizard
2. Filters that are a result of the formula in the Formula Tab of the Linked Report Wizard
3. If the *parent report* is on a Dashboard, interactive filters from *parent* and *parent-of-parent (aka grandparent)* reports
4. Prompting filters from *parent report*

## Adding Linked Reports

1. Create a new **Dashboard**, **Advanced**, **CrossTab** or **Express****Report** that contains the drilldown data. This will become the linked *child report*.Linked reports typically open in a small window, so the child report should be simple and concise. Avoid large fonts, a lot of static content, or making it too large in size. The *child report*‘s **General Option** for **No Data Qualify Display Mode** should be set to *Show Report* in order to show an empty drilldown instead of an error message.
2. In the *parent report*, select the cell to link then click the **Link Reports ![LinkedReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432125018135/linkedreport.png)**icon in the toolbar. This will open the **Linked Report Wizard**.
   ![twgyamGLV3.png](https://devnet.logianalytics.com/hc/article_attachments/5432403761303/twgyamglv3.png)

   The **Linked Report Wizard** in *v2021.1+*.

   ![CdgI0WyrGT.png](https://devnet.logianalytics.com/hc/article_attachments/5432403808791/cdgi0wyrgt.png)

   The **Linked Report Wizard** in *pre-v2021.1*.
3. Select or search for the desired *child report.* This will use **default linking** to drilldown to the *child report*.  

   ### To manually define link fields:

   ![Z0ZjuS1uSh.png](https://devnet.logianalytics.com/hc/article_attachments/5432325506711/z0zjus1ush.png)

   The **Fields** tab of the **Linked Report Wizard**

   1. Select the **From Category** and **To Category** from their respective dropdowns.
   2. Click the ![+](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Add** button for each set of linked fields to add. Use multiple linked fields to show only the drilldown rows that satisfy all of the link conditions.
   3. For each set of linked fields, select the **From Field** and **To Field**.

   ### To conditionally link with formula:

   ![firefox_oNSGU0vs56.png](https://devnet.logianalytics.com/hc/article_attachments/5432445858583/firefox_onsgu0vs56.png)

   The **Formula** tab of the **Linked Report Wizard**

   1. Add a data field by dragging and dropping it into the **Formula** pane or double-clicking it. Or enter it manually using the following format: `{DataCategory.DataField}`  
      **Caution:** Linked report conditional formulas support only one data field. If multiple data fields are used, all but the first will be ignored.
   2. Add a Parameter by entering it manually using the following format: `@ParameterName@`.
   3. Add a function by dragging and dropping it into the **Formula** box or double-clicking it, or enter it manually.
4. Click **Okay** to close the **Linked Report Wizard**.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Because the *child* is a separate report from the *parent*, if the *child report* is moved to another folder, or the linked field is removed from the report, the link will be broken.

## Modifying Linked Reports

1. Click the **Link**![LinkedReportNotice.png](https://devnet.logianalytics.com/hc/article_attachments/5432325545879/linkedreportnotice.png) icon in the corner of the linking cell, or click the cell and then click the **Link Reports ![LinkedReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432125018135/linkedreport.png)** icon in the toolbar.
2. Interact with the **Linked Report Wizard** just as if the link is being added (continue at step 2).

## Deleting Linked Reports

In *v2021.1+*:

![twgyamGLV3.png](https://devnet.logianalytics.com/hc/article_attachments/5432403761303/twgyamglv3.png)

1. Click the **Link**![LinkedReportNotice.png](https://devnet.logianalytics.com/hc/article_attachments/5432325545879/linkedreportnotice.png) icon in the corner of the linking cell, or click the cell and then click the **Link Reports ![LinkedReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432125018135/linkedreport.png)** icon in the toolbar.
2. Click the name of the of the report at the bottom of the dialog. A **Remove Link**![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon will also appear.
3. Click **Okay**.

In *pre-v2021.1*:

![firefox_Rjs8Tjj8GB.png](https://devnet.logianalytics.com/hc/article_attachments/5432429670935/firefox_rjs8tjj8gb.png)

1. Click the **Link**![LinkedReportNotice.png](https://devnet.logianalytics.com/hc/article_attachments/5432325545879/linkedreportnotice.png) icon in the corner of the linking cell, or click the cell and then click the **Link Reports ![LinkedReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432125018135/linkedreport.png)** icon in the toolbar.
2. Click the **Remove Link ![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png)** icon.
3. Click **Okay**.

Or, right-click the cell with the linked report in it, then click **Remove Linked Value**.
