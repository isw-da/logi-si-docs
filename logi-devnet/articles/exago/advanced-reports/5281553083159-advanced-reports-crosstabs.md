---
title: "Advanced Reports: CrossTabs"
id: 5281553083159
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281553083159-Advanced-Reports-CrossTabs
updated_at: 2022-05-03T22:09:28Z
---

# Advanced Reports: CrossTabs

# Advanced Reports: CrossTabs

Use a **CrossTab**, or cross tabulation, for grouping and summarizing data fields that expands vertically and horizontally depending on the number of data groupings. CrossTabs are also known as *two-way tables*, *contingency tables*, or *pivot tables*.

![firefox_8Co2bLE0bx.png](https://devnet.logianalytics.com/hc/article_attachments/5432420764055/firefox_8co2ble0bx.png)

A CrossTab report built with the CrossTab Report Wizard

## Create a CrossTab

CrossTab Reports can be added to an existing report from the [Report Viewer](https://devnet.logianalytics.com/hc/en-us/articles/5281541805591-Report-Viewer), or they may be created as a new report from the main menu.

### From the Report Designer Toolbar

To add a CrossTab to a report/ in the Report Designer:

1. Select a **Group Footer** (including Footers in a Repeating Group) or **Report Footer** cell.
2. Open the **CrossTab Data Designer** dialog:
   * *(v2021.1+)* Click the **Insert**![Insert.png](https://devnet.logianalytics.com/hc/article_attachments/5432182571543/insert.png)![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png) icon on the toolbar, then click ![Crosstab.png](https://devnet.logianalytics.com/hc/article_attachments/5432370207383/crosstab.png)**CrossTab**. The dialog resembles the Layout tab described below.
   * *(pre-v2021.1)* Click the **CrossTab** ![CrossTabWizard.png](https://devnet.logianalytics.com/hc/article_attachments/5432270123415/crosstabwizard.png) icon in the toolbar.

### From the Main Menu CrossTab Report Wizard

CrossTabs are created from the Main Menu just as any other report is. Creating a CrossTab from the Main Menu will launch the **CrossTab Report Wizard**.

The CrossTab Report Wizard is an interactive tool which will walk through the process of creating a new Advanced Report with a CrossTab embedded within it. All of the settings in the wizard can be modified in the **Report Designer** after the report is created.

The CrossTab Report Wizard has four tabs: **Name**, **Categories**, **Filters**, and **Layout**. All tabs except Layout are required to create the new report.

#### Name

![Name section](https://devnet.logianalytics.com/hc/article_attachments/5432434402327/screen.ct_namesection.png)

In the **Name** tab, enter a name for the report and select a **Folder** to save it to.

The report name can be up to 255 characters long, but cannot contain the following special characters

```
? : /  * " < >
```

Enter an optional description for the report in the **Enter a description for the report** text box.

#### Categories

![Categories section](https://devnet.logianalytics.com/hc/article_attachments/5432451076247/screen.ct_categoriessection.png)

In the **Categories** tab, select the **Data Objects** to include in the CrossTab. It is important to understand the difference between **Data Categories** and **Data Fields**. Data objects are arranged into folders. Those objects are further expanded into **fields**. A field is a parcel of data from a data object, such as the name of a Product or an Employee ID number.

* To add a Data Object, either drag and drop it to the **Data Object Name** Column, click the ![](https://devnet.logianalytics.com/hc/article_attachments/5432434443799/icon.add_.png)**Add** button, or double-click the field name
* To search for a specific Data Object or folder, type its name into the **Search** field.
* To see what fields are in a Data Object, click the **View Data Object Fields**![i](https://devnet.logianalytics.com/hc/article_attachments/5432321848855/information.png) icon.
* Check the **Hide Repeated Values** checkbox to stop duplicate information from appearing on the report.
* Each data object must be referenced by a unique **Alias**. The alias can also be used to provide a different name for the data object. This column will only appear if enabled by the system administrator. See [Advanced Reports: Data Objects (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281533535767-Advanced-Reports-Data-Objects-v2021-1-)
* To remove a Data Object, click the **Delete**![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon at the end of the row.

#### Filters

In the **Filters** tab, create statements to filter the data at runtime.

![Filter section](https://devnet.logianalytics.com/hc/article_attachments/5432469903895/screen.ct_filtersection.png)

A date filter applied to output data from the years 2015 to 2016

There is no limit to the number of filters that can be defined. Filters can be numeric (up to eight decimals) or alphanumeric.

* To filter a Data Field, either drag and drop it to the **Filter By** column, click  the ![](https://devnet.logianalytics.com/hc/article_attachments/5432434443799/icon.add_.png)**Add** button, or double-click on its name.
* To filter using a custom or built-in formula, click the ![](https://devnet.logianalytics.com/hc/article_attachments/5432434443799/icon.add_.png)**Add Formula** button.
* Use the **Move Item Up**![^](https://devnet.logianalytics.com/hc/article_attachments/5432225168663/movegridrowup.png) and  **Move item Down**![v](https://devnet.logianalytics.com/hc/article_attachments/5432338912791/movegridrowdown.png) icons to move the rows to set the filter priority. The top filter has the highest priority.
* To remove a filter, click the **Delete**![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon at the end of the row.

Detailed information about creating and editing filters is found in [Filters](https://devnet.logianalytics.com/hc/en-us/articles/5281549708439-Filters).

#### Layout

In the **Layout** tab, design the CrossTab by moving Data Fields into the **Row Header**, **Column Header**, and **Tabulation Data** panels.

![Layout Section](https://devnet.logianalytics.com/hc/article_attachments/5432434485015/screen.ct_layoutsection.png)

##### Row Headers

**Row Headers** expand a CrossTab vertically. A CrossTab has a row for each unique value of a Row Header. For example, if you were using sales data, you may have the Row Headers `Category.CategoryName` and `Products.ProductName` to provide rows for each product grouped by category.

* To add a Row Header, either drag and drop it to the **Row Header Source** panel or use the **Add Row Header**![+ --](https://devnet.logianalytics.com/hc/article_attachments/5432478193175/addcrosstabrow.png) icon
* Click the **Formula Editor**![fx](https://devnet.logianalytics.com/hc/article_attachments/5432247626647/formula.png) icon to insert a formula into the **Row Header**.
* Click the **Edit Header**![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432185311127/edit.png) icon to open the **Header Options** menu.  
  ![Header Options dialog](https://devnet.logianalytics.com/hc/article_attachments/5432478222487/screen.ct_rowheader_options.png)
  + Set a label for the Row Header. This label will appear at the top of the CrossTab.
  + Select a sorting method and direction:
    - *None*: Does not sort the Row Headers.
    - *Header Value (Text)*: Sorts the Row Header by its values as though they are text.
    - *Header Value (Number)*: Sorts the Row Header by its values as though they were numbers.
    - *Tabular Totals*: Sorts the Row Header by the totals of the Tabulation Data.
  + Select where to display subtotals by using the **Placement** dropdown:
    - *None*: Does not display subtotals.
    - *Top*: Displays subtotals above the Tabulation Data for each Row Header value.
    - *Bottom*: Displays subtotals below the Tabulation Data for each Row Header value.
  + Set a label for the subtotals.
* Use the **Move Item Up**![^](https://devnet.logianalytics.com/hc/article_attachments/5432225168663/movegridrowup.png) and **Move Item Down**![v](https://devnet.logianalytics.com/hc/article_attachments/5432338912791/movegridrowdown.png) icons to rearrange the order of the **Row Headers**.
* To remove a Row Header, click the **Delete**![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon.

##### Column Headers

**Column Headers** expand a CrossTab horizontally. A CrossTab has a column for each unique value of a Column Header. For example, if you were using sales data you may have the Column Headers `Year({Order.OrderDate})` and `MonthName({Orders.OrderDate})` to provide columns for each month grouped by year.

![Column Header example](https://devnet.logianalytics.com/hc/article_attachments/5432434557847/screen.ct_columnheader_example.png)

CrossTab Design Wizard with two column headers

* To add a **Column Header**, either drag and drop a data field to the **Column Header Source** pane or click the **Add Column Header**![+ |||](https://devnet.logianalytics.com/hc/article_attachments/5432470299031/addcrosstabcolumn.png) icon.
* Click the **Formula Editor**![fx](https://devnet.logianalytics.com/hc/article_attachments/5432247626647/formula.png) icon to insert a formula into the Column Header.
* Click the **Edit Header**![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432185311127/edit.png) icon to open the **Header Options** menu.  
  ![screen.ct_columnheader_options.png](https://devnet.logianalytics.com/hc/article_attachments/5432420888855/screen.ct_columnheader_options.png)

  Column Header Options dialog

  + Set a label for the **Column Header** to appear at the top of the **CrossTab**.
  + Select a sorting method and direction:
    - *None*: Does not sort the Column Headers.
    - *Header Value (Text)*: Sorts the **Column Header** by its values as though they were text.
    - *Header Value (Number)*: Sorts the **Column Header** by its values as though they are numbers.
    - *Tabular Totals*: Sorts the **Column Header** by the totals of the **Tabulation Data**.
  + Select where to display subtotals by using the **Placement** dropdown:
    - *None*: Does not display subtotals.
    - *Left*: Displays subtotals to the left of the Tabulation Data for each Column Header value.
    - *Right*: Displays subtotals to the right of the Tabulation Data for each Column Header value.
  + Set a label for the subtotals.
* Use the **Move Item Up**![^](https://devnet.logianalytics.com/hc/article_attachments/5432225168663/movegridrowup.png) icon and **Move Item Down**![v](https://devnet.logianalytics.com/hc/article_attachments/5432338912791/movegridrowdown.png) icon to rearrange the order of the Column Headers.
* To remove a **Column Header**, click the **Delete**![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon at the end of the row.

##### Tabulation Data

**Tabulation Data** provides information when data exists for both the **Column Header** and **Row Header** values. For example, if you have a Row Header on products and a Column Header on the month, then Tabulation Data of `Orders.OrderID` may use the `Count` function to display how many orders contained each product each month.

![CrossTab wizard with tabulation data sources](https://devnet.logianalytics.com/hc/article_attachments/5432420906775/c9bjbldmhd.png)

CrossTab Report Design Wizard with row header, column header and tabulation data sources

* To add a Tabulation Data field, either drag and drop it to the **Tabulation Data** pane or click the **Add Tabulation Data**![](https://devnet.logianalytics.com/hc/article_attachments/5432470509591/addcrosstabtabulation.png) icon.
* Click the Formula Editor ![fx](https://devnet.logianalytics.com/hc/article_attachments/5432247626647/formula.png) icon to insert a formula into the **Tabulation Data**.
* Click the Edit Tabulation Data ![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432185311127/edit.png) icon to open the **Tabulation Options** menu.  
  ![screen.ct_edittab_order_count.png](https://devnet.logianalytics.com/hc/article_attachments/5432420945687/screen.ct_edittab_order_count.png)
  + Set a label for the **Tabulation Data** to appear at the beginning of each row.
  + Use the Method dropdown to select the summary function to be applied to the **Tabulation Data**:
    - *Sum*: Totals the Tabulation Data.
    - *Count*: Counts the Tabulation Data.
    - *Average*: Takes the mean of the Tabulation Data.
    - *Minimum*: Displays the lowest value in the Tabulation Data.
    - *Maximum*: Displays the highest value in the Tabulation Data.
  + Use the Value dropdown to select how the **Tabulation Data** should be displayed:
    - *None*: Displays the value of the Tabulation Data without applying any formula.
    - *Aggregate*: Display the result of the selected method.
    - *Percent of Row*: Display the result of the selected method as a percentage of the row total.
    - *Percent of Column*: Display the result of the selected method as a percentage of the column total.
* Use the **Move Item Up**![^](https://devnet.logianalytics.com/hc/article_attachments/5432225168663/movegridrowup.png)and **Move Item Down**![v](https://devnet.logianalytics.com/hc/article_attachments/5432338912791/movegridrowdown.png) icons to rearrange the order of the Tabulation Data.
* To remove a Tabulation Data source, click the **Delete** icon ![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png).

#### CrossTab Themes

The **Theme** dropdown can be used to quickly style the CrossTab using a predefined theme.

![nLQFBwKYpg.png](https://devnet.logianalytics.com/hc/article_attachments/5432444188439/nlqfbwkypg.png)![yp4Hwd4qAf.png](https://devnet.logianalytics.com/hc/article_attachments/5432470549783/yp4hwd4qaf.png)![1uBkgNj5Tp.png](https://devnet.logianalytics.com/hc/article_attachments/5432470566167/1ubkgnj5tp.png)![w10wwyBZZI.png](https://devnet.logianalytics.com/hc/article_attachments/5432420988439/w10wwybzzi.png)

The same CrossTab as seen in the Report Designer and Report Viewer, with the *Tokyo Night* and *Office Park* themes applied.

Further styling can be done in the **Report Designer**.

#### CrossTab Options

Settings that affect the entire **CrossTab** are controlled in the **CrossTab Options Menu.** Open the **CrossTab Options Menu** by clicking the ![icon.generaloptions.png](https://devnet.logianalytics.com/hc/article_attachments/5432470598039/icon.generaloptions.png)

**Options**![CrossTab Options menu](https://devnet.logianalytics.com/hc/article_attachments/5432478593175/screen.ct_generaloptions.png)

CrossTab Options Menu

##### General

* Use the **Row Headers Placement** dropdown to determine how the Row Headers are displayed:
  + *Columns*: Display the Row Headers in columns from left to right in the order they appear in the Row Header Source panel.
  + *Hierarchical*: Display Row Headers in a hierarchical structure using indentation to display their order.
* Check **Repeat CrossTab Header every new page** to repeat Row Header labels and Column Headers on each new page.

##### Grand Total Row

To get a total for each column, select *Top* or *Bottom* from the **Placement** dropdown in the **Grand Total Row** section and provide a label in the **Label** text box.

##### Grand Total Column

To get a total for each row, select *Top* or *Bottom* from the **Placement** dropdown in the **Grand Total Column** section and provide a label in the **Label** text box.

#### Preview

![1N631UQvhR.png](https://devnet.logianalytics.com/hc/article_attachments/5432478627863/1n631uqvhr.png)

A preview layout of the steps applied above

At the bottom of the **Layout** section, a preview will display how the **CrossTab** will appear based on the fields that have been added.

Finally, clicking the **Finish** button will create the report and open the **CrossTab Report Designer**.

## Work with CrossTabs in the Report Designer

Upon entering the **Report Designer**, the new CrossTab appears in the Report Footer section:

![v1A3tmgjZk.png](https://devnet.logianalytics.com/hc/article_attachments/5432470688279/v1a3tmgjzk.png)

CrossTab Report in Report Designer *v2021.1+*

![firefox_fEyboc0tpR.png](https://devnet.logianalytics.com/hc/article_attachments/5432421096599/firefox_feyboc0tpr.png)

CrossTab Report in Report Designer *v2019.1*

To edit the **CrossTab** after its creation open the **CrossTab Data Designer** dialog by either:

* right-clicking on the CrossTab then clicking **Edit CrossTab** or
* double-click anywhere on the CrossTab

The CrossTab Data Designer dialog resembles the Layout tab of the CrossTab Report Wizard.

Visualizations and formulas may not be added to the **CrossTab**. The following error message appears if trying to add one of these to the report:

![screen.ct_notapplicablewarning.png](https://devnet.logianalytics.com/hc/article_attachments/5432470756375/screen.ct_notapplicablewarning.png)

## CrossTab Formatting

**CrossTabs** often contain a large amount of information and may appear cluttered if they are not well formatted. To help avoid overwhelming appearing reports:

* Set predefined widths of rows containing long strings of characters or integers.
* Use a theme or apply color to cells via cell formatting to help differentiate between certain sections.
* Add borders with cell formatting to detail and header sections.
* Abbreviating longer strings using the built-in String functions. For example, `Left(MonthName({Orders.OrderDate}), 3)` will output the first three letters of each month.
* In the Report Viewer Options, uncheck **Simulate PDF**.
* Use filters to limit the size of the data set.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Conditional formatting expressions are not evaluated for empty CrossTab cells.
