---
title: "Building Your First Report"
id: 5281539047703
section: "Overview"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281539047703-Building-Your-First-Report
updated_at: 2022-05-03T22:09:27Z
---

# Building Your First Report

# Building Your First Report

---

In versions *v2021.1+*:

There are two report types well suited for building your first report: **ExpressView** and **Advanced Reports**.

[**ExpressView**](https://devnet.logianalytics.com/hc/en-us/articles/5281589443095-ExpressView-Introduction-v2021-1-) is a tool to quickly get insight into vertically expanding data records and groups. An ExpressView can optionally include a visualization.

[**Advanced Reports**](https://devnet.logianalytics.com/hc/en-us/articles/5281541735063-Report-Designer-v2021-1-) are the flagship report type of the application. Advanced Reports are made using an spreadsheet-like cell-grid interface. The most powerful reporting tools are available with Advanced Reports, including geographic maps; CrossTabs; repeating groups; complex join, filter, and sort logic; drilldowns to linked child reports, and more.

Review [Report Types](https://devnet.logianalytics.com/hc/en-us/articles/5281561339799-Report-Types) to learn more. The examples below utilize the Northwind sample data set.

## Creating an ExpressView

This section will walk-through creating an ExpressView report listing the unit prices of products organized into categories. A column chart comparing the average price on a per-category basis is also included. The report looks like this:

![CFe03qdgK0.png](https://devnet.logianalytics.com/hc/article_attachments/5432449658775/cfe03qdgk0.png)

1. On the main menu in the top-left corner, click the **Create New Report**![MainLeftPaneNewReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432314432023/mainleftpanenewreport.png) icon.
2. Click **ExpressView**![ThumbnailExpressView.png](https://devnet.logianalytics.com/hc/article_attachments/5432275054231/thumbnailexpressview.png)to start the ExpressView Designer.
3. Add the necessary data fields to the canvas, by dragging them from the ![MainLeftPaneDataFieldsSelected.png](https://devnet.logianalytics.com/hc/article_attachments/5432222814999/mainleftpanedatafieldsselected.png)**Data Fields Pane** on the left side of the screen and dropping them into desired position on the canvas:
   * `Categories.CategoryName`
   * `Products.ProductName`
   * `Products.Discontinued`
   * `Products.UnitPrice`![vpUVM7f0WY.gif](https://devnet.logianalytics.com/hc/article_attachments/5432442713111/vpuvm7f0wy.gif)
4. To organize the report by the product category, set `Categories.CategoryName` as a **Group**. Click-and-drag on the `CategoryName` header and drop it to the *Add Group* drop zone.![1AlIDaBjBh.gif](https://devnet.logianalytics.com/hc/article_attachments/5432476138391/1alidabjbh.gif)
5. To calculate the average unit price for each category, on the **Group Totals** line, click on the *Sum for UnitPrice* dropdown and change to *Avg for UnitPrice.*![BHLfLnCM2t.png](https://devnet.logianalytics.com/hc/article_attachments/5432467928727/bhlflncm2t.png)
6. Add a chart to the report, by clicking the **Chart ![ShowViz.png](https://devnet.logianalytics.com/hc/article_attachments/5432220914071/showviz.png)** icon on the toolbar. Then, in the Properties Pane on the right, choose the **Visualizations** tab, and then **Data**. ![5n3UIrMzZp.png](https://devnet.logianalytics.com/hc/article_attachments/5432433448599/5n3uirmzzp.png)
7. Since columns that are not totaled don’t appear in charts, remove the **Values** for `Products.ProductName` and `Products.Discontinued` by clicking the **X** icon in each element. The chart will appear.![vBfKTRkIaj.png](https://devnet.logianalytics.com/hc/article_attachments/5432442884759/vbfktrkiaj.png)
8. Switch to the **Type** tab, then click the **Column**![ChartTypeColumn.png](https://devnet.logianalytics.com/hc/article_attachments/5432354124567/charttypecolumn.png)icon to change the chart to a column chart.  
   ![6k7NKji2Wa.png](https://devnet.logianalytics.com/hc/article_attachments/5432449860631/6k7nkji2wa.png)

At this point, the ExpressView very closely matches the same report at the beginning of this topic. It should look something like the figure below.

![H7j72BDZjX.png](https://devnet.logianalytics.com/hc/article_attachments/5432327969175/h7j72bdzjx.png)

Continue on to apply formatting such as color schemes, fonts and column names:

9. To style the groups and detail fields, click the **Canvas**![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png)![FormatPaintbrush.png](https://devnet.logianalytics.com/hc/article_attachments/5432248054935/formatpaintbrush.png) icon in the toolbar.
   1. Choose a color **Theme** from the dropdown. The *Office Park* theme is used in the example report. The color theme will immediately change on the canvas.
   2. Choose a **Font** from the dropdown. *Bookman Old Style* is used in the example report.
10. Click the **Canvas**![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png)![FormatPaintbrush.png](https://devnet.logianalytics.com/hc/article_attachments/5432248054935/formatpaintbrush.png) icon again to close the menu.![h3oAYL0cmE.png](https://devnet.logianalytics.com/hc/article_attachments/5432468104727/h3oayl0cme.png)
11. In the Properties Pane on the right, choose the **Visualizations** tab, then **Appearance**, then **Chart Titles**.
12. Enter a **Main Chart Title**, and choose a font.![Nt6LEC2Iin.png](https://devnet.logianalytics.com/hc/article_attachments/5432442956183/nt6lec2iin.png)
13. In the **Labels** section, choose a font to match the others. Optionally, add an **X-Axis Title** and **Y-Axis Title**.![C4IngGwKIp.png](https://devnet.logianalytics.com/hc/article_attachments/5432442969111/c4inggwkip.png)
14. Change to the **Chart Colors** section, then choose a color theme from the dropdown. The example report uses the *Sandstone* theme.![We9iJ9INnz.png](https://devnet.logianalytics.com/hc/article_attachments/5432442994839/we9ij9innz.png)
15. Change to the **Chart Data** section, scroll down to **Number Format**. This section formats how the values in the chart axes appear. Since they are average dollar values, set these controls as follows:
    * Enter *2* for **Decimal Places**
    * Check the **Use Currency Symbol** checkbox ![Thu0WXvTWX.png](https://devnet.logianalytics.com/hc/article_attachments/5432443021847/thu0wxvtwx.png)
16. Each column can be given a custom name, font style and alignment. Click on a column header (for example `CategoryName`) and then in the ![SelectedCellMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432314102935/selectedcellmenu.png)**Selected Section** tab of the Properties Pane, enter a **Display Name**, **Horizontal Align** choice, **Font Style** and **Underline** as desired. Repeat for the `ProductName`, `Discontinued` and `UnitPrice` columns.  
    > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
    >
    > The **Horizontal Align** property will apply to the column header and the data in the column. The **Display Name**, **Font Style** and **Underline** only apply to the column header.

    ![XYcmYUORLi.png](https://devnet.logianalytics.com/hc/article_attachments/5432443064727/xycmyuorli.png)
17. The data in the columns, and the totals can also be styled. Click on the white area of the Unit Price column between the header and the total. In the Selection Section tab of the Properties Pane, choose a **Data Format** (*Number* should already be selected)*.* Repeat this step for the **Group Totals**, which will also apply the settings to the **Report Totals** line.
18. Save the report by clicking the **Save**![Save.png](https://devnet.logianalytics.com/hc/article_attachments/5432229545751/save.png)![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png) icon in the toolbar. Enter a **Name**, an optional **Description** and select a folder to save it to. The *My Reports* folder is a good choice for a first report.
19. Click **![Run](https://devnet.logianalytics.com/hc/article_attachments/5432298567575/run_button.png)** on the toolbar to switch to Live Data mode and see the new ExpressView in all its glory. Congratulations!

## Creating an Advanced Report

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> A quick way of getting an Advanced Report up and running is to start with an ExpressView, then [export that ExpressView as an Advanced Report](https://devnet.logianalytics.com/hc/en-us/articles/5281611975319-ExpressView-Exporting-v2021-1-#Exportin). Editing can then resume in the Advanced Report Designer.

This section will walk-through creating an Advanced Report from scratch with the **Advanced Report Designer**. The sample report lists the amount of revenue generated by each salesperson in a company, including the amount of revenue of each product category in a collapsible section. A multi-series column chart appears at the beginning of the report. The sample report looks like this:

![MkOPuhzJkF.png](https://devnet.logianalytics.com/hc/article_attachments/5432443077911/mkopuhzjkf.png)

1. On the main menu in the top-left corner, click the **Create New Report**![MainLeftPaneNewReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432314432023/mainleftpanenewreport.png) icon.
2. Click **Advanced Report**![ThumbnailAdvancedReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432450064279/thumbnailadvancedreport.png)to start the Advanced Report Designer.
3. The **Add Data Objects** dialog appears. These data objects are needed for this report:
   * `Categories`
   * `Products`
   * `Employees`
   * `Orders`
   * `OrderDetails`

   Not all of these data objects appear on the report, but they provide a join path between the objects that do.![zKcmN034Al.png](https://devnet.logianalytics.com/hc/article_attachments/5432433699735/zkcmn034al.png)

     
   Click **Okay**.
4. The report will group and aggregate (summarize) data by the employee name, and by the product category name. **Sorts** are required to create groups. To create sorts:
   1. Click the **Sorts**![SortsMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432211886103/sortsmenu.png) icon on the toolbar to open the Report Sorts dialog.
   2. From the dropdown on the left, choose `Employees`, then double click the `LastName` field. This will add `Employees.LastName` as a sort.![IdkgjepthR.png](https://devnet.logianalytics.com/hc/article_attachments/5432433734679/idkgjepthr.png)
   3. Repeat step 2 to add `Categories.CategoryName` as a second sort.
   4. Click **Okay** to close the Report Sorts dialog.
5. This report will show two columns: one with the employee’s name and category names, the other withe actual revenue values. The other columns can be removed from the grid
   1. Hold the **Ctrl** key on the keyboard and click the column headers for columns E, D and C.
   2. Click the **Column Menu**![MoreOptions_Black_Small.png](https://devnet.logianalytics.com/hc/article_attachments/5432415957271/moreoptions_black_small.png) icon to open the Column Menu.
   3. Click ![DeleteReportSmall.png](https://devnet.logianalytics.com/hc/article_attachments/5432232340503/deletereportsmall.png)**Delete 3 Columns**.![oSgFnGa66v.gif](https://devnet.logianalytics.com/hc/article_attachments/5432328144535/osgfnga66v.gif)
6. The Page Header section is also not needed for this example report. Click the **Section Menu**![MoreOptions_Black_Small.png](https://devnet.logianalytics.com/hc/article_attachments/5432415957271/moreoptions_black_small.png) icon on the Page Header, then click ![DeleteReportSmall.png](https://devnet.logianalytics.com/hc/article_attachments/5432232340503/deletereportsmall.png)**Delete Section**. The design grid should now look like this:![glahf0GH9D.png](https://devnet.logianalytics.com/hc/article_attachments/5432328175767/glahf0gh9d.png)
7. The chart will reside in the Report Header section. To add it:
   1. Click the ![AddNew.png](https://devnet.logianalytics.com/hc/article_attachments/5432231941911/addnew.png)**Add Section** button
   2. Click ![ReportHeader.png](https://devnet.logianalytics.com/hc/article_attachments/5432463418135/reportheader.png)**Report Header**.
8. Add the Group Header sections for the Employee Name and Category Name:
   1. Click the ![AddNew.png](https://devnet.logianalytics.com/hc/article_attachments/5432231941911/addnew.png)**Add Section** button
   2. Click ![GroupHeader.png](https://devnet.logianalytics.com/hc/article_attachments/5432447395607/groupheader.png)**Group Header**.
   3. In the Group Header dialog, select `Employees.LastName` from the dropdown list.![twQ02ZeHOx.png](https://devnet.logianalytics.com/hc/article_attachments/5432433785239/twq02zehox.png)
   4. Click **Okay** to close the Group Header dialog.
   5. Repeat steps 1–3 for `Categories.CategoryName`.  
      The design grid should now look like this:![Q05PrLQzbZ.png](https://devnet.logianalytics.com/hc/article_attachments/5432476878999/q05prlqzbz.png)
9. Add the data to the cells on the design grid:
   1. Add `Categories.CategoryName` directly from the Data Objects Pane by dragging it to cell A3 on the grid.
   2. Type the word *Revenue* into cell B2.
10. Since the employee’s first and last names are contained in two different fields, a **formula** can be used to **concatenate** or join the fields together. Here is how:
    1. Select cell A2 by clicking it.
    2. Place the cursor into the ![FormulaLarge.png](https://devnet.logianalytics.com/hc/article_attachments/5432236378775/formulalarge.png)**Formula Bar** just below the toolbar.
    3. Type an equals sign =.
    4. Begin typing `Employees`. A tooltip will appear with all of the fields that contain the word `Employees` as guidance. Use the mouse or arrow keys to highlight `Employees.FirstName` then press Enter. The entire data field name will be added to the formula bar. Notice it is enclosed in `{` curly braces `}`. Data fields must always be enclosed in curly braces in formulas.![YUa1KdhtZC.png](https://devnet.logianalytics.com/hc/article_attachments/5432443360791/yua1kdhtzc.png)
    5. Type &. This is called the **concatenation character** and tells the system to join two things together.
    6. Type ” “. This will add a space between the first and last names.
    7. Type another &.
    8. Type `Employees` again, this time highlighting `Employees.LastName`, then press Enter. The complete formula should look like this:

       ```
       ={Employees.FirstName} & " " & {Employees.LastName}
       ```
11. Use another **formula** to calculate the revenue for each category:
    1. Select cell B3 by clicking it.
    2. Place the cursor into the ![fx](https://devnet.logianalytics.com/hc/article_attachments/5432236378775/formulalarge.png)**Formula Bar** just below the toolbar.
    3. Enter the formula exactly as it appears below:

       ```
       =AggSum({OrderDetails.UnitPrice}*{OrderDetails.Quantity})
       ```

       This formula uses an **aggregate function** to calculate sum of the revenues of all sales, by multiplying the quantity of each product sold by its unit price, then adding them all together. The breaking down of revenues into product categories, and for each employee happens automatically since the aggregate function is contained in the group sections created earlier. The design grid should now look something like this:![tzKJNOru11.png](https://devnet.logianalytics.com/hc/article_attachments/5432450278295/tzkjnoru11.png)
12. Now is a good time to save the report. Click the Save ![Save.png](https://devnet.logianalytics.com/hc/article_attachments/5432229545751/save.png)![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png) icon on the toolbar. Enter a **Name**, an optional **Description** and select a folder to save it to. The *My Reports* folder is a good choice for a first report.
13. Apply the color formatting to the cells to match the example report.
    1. Select cell A2, then click the **Background Color**![BackgroundColor.png](https://devnet.logianalytics.com/hc/article_attachments/5432322889879/backgroundcolor.png) icon on the toolbar. Select a medium gray color. Click the **Bold**![StyleBold.png](https://devnet.logianalytics.com/hc/article_attachments/5432248067735/stylebold.png) icon to increase the font’s weight.
    2. Repeat step 1 for cell B2, choosing a medium green color. Click the **Horizontal Alignment**![AlignLeft.png](https://devnet.logianalytics.com/hc/article_attachments/5432264137495/alignleft.png)![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png) icon, then choose **Center**![AlignCenter.png](https://devnet.logianalytics.com/hc/article_attachments/5432248296855/aligncenter.png).
    3. Select cell A3, apply a light blue background color. Select cell B3 and apply a light green background color. Set cell B3 for a center alignment as well.
    4. Select both columns A and B, then place the cursor between the columns and drag to resize both of them.![qvhBwDPHwR.gif](https://devnet.logianalytics.com/hc/article_attachments/5432450298391/qvhbwdphwr.gif)
    5. To make the categories list collapsible, click the header for row number 2 to open the Row Menu. Click **Collapse Rows.**
    6. Delete the Detail section from the report, it won’t be needed.
14. The design grid should now look like this:![pK2LuT2xRM.png](https://devnet.logianalytics.com/hc/article_attachments/5432468694167/pk2lut2xrm.png)  
    Click ![Run](https://devnet.logianalytics.com/hc/article_attachments/5432298567575/run_button.png) on the toolbar to execute the report to see the progress so far. In the Report Viewer, the report should look like this:![M7qzxIYeUF.png](https://devnet.logianalytics.com/hc/article_attachments/5432450348951/m7qzxiyeuf.png)  
    Click on the **Open Rows**![OpenRows.png](https://devnet.logianalytics.com/hc/article_attachments/5432417978391/openrows.png) icons to open or close the collapsed rows to see the revenue figures.
15. Close the Report Viewer tab and return to the Report Designer.
16. Apply borders and advanced numeric formatting to the data. These changes don’t appear on the Design Grid, but they affect how the data is presented in the Report Viewer and when exported to output files such as PDF or Excel.
    1. Select cell A2, then click the **Format Cells**![FormatCells.png](https://devnet.logianalytics.com/hc/article_attachments/5432243560855/formatcells.png)icon. When the Format Cells dialog opens, switch to the Border tab.
    2. Check the **Make Borders Uniform** checkbox. Click the **Color Chooser**![color-picker-icon.png](https://devnet.logianalytics.com/hc/article_attachments/5432272123671/color-picker-icon.png) icon, then choose black.
    3. Click **Okay** to close the dialog.
    4. Select cell B2, then click the **Format Cells**![FormatCells.png](https://devnet.logianalytics.com/hc/article_attachments/5432243560855/formatcells.png)icon. Apply a top, right and bottom border with color black by setting the individual border settings.![LC19CASv9P.png](https://devnet.logianalytics.com/hc/article_attachments/5432433918999/lc19casv9p.png)
    5. Repeat step 4 for:
       * cell A3 — apply a left, bottom and right border
       * cell B3 — apply a bottom and right border
    6. With cell B3 still selected, and the Format Cells dialog still open, switch to the Number tab to apply advanced numeric formatting to the revenue values contained within it:![aYT2zLGuYz.png](https://devnet.logianalytics.com/hc/article_attachments/5432433937303/ayt2zlguyz.png)
       1. Under **Category**, select *Number.*
       2. Ensure **Decimal Places** is set to *2.*
       3. Check the **Use 1000 Separator** and **Use Currency Symbol.**
       4. Click **Okay** to close the dialog.
17. Run the report again to observe the changes that the formatting options have made to the report output. When satisfied, close the Viewer tab and return to the Designer.
18. Hold the **Ctrl** key on the keyboard and click cells A1 and B1 to select both cells. Click the **Merge Cells ![MergeCells.png](https://devnet.logianalytics.com/hc/article_attachments/5432269867671/mergecells.png)** icon on the toolbar to combine the cells together.
19. Place the cursor between the headers for rows 1 and 2, then drag the mouse down to increase row 1’s height.![lhBD0U6kXT.gif](https://devnet.logianalytics.com/hc/article_attachments/5432450469911/lhbd0u6kxt.gif)
20. Select the new single cell on row 1, then add the chart:
    1. Click the **Insert**![Insert.png](https://devnet.logianalytics.com/hc/article_attachments/5432182571543/insert.png)![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png) icon on the toolbar, then select ![Type.png](https://devnet.logianalytics.com/hc/article_attachments/5432380243863/type.png)**Chart** to start the Chart Wizard.
    2. On the Type tab, select the *Stack Column* chart type. Then, click **Next** to advance to the Data tab.![QQ05tQeR41.png](https://devnet.logianalytics.com/hc/article_attachments/5432468882071/qq05tqer41.png)
    3. Click the ![ApplyBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432257516055/applybtn.png)**Data Layout…** button. Since all of the revenues that appear on the chart are in a single column but different rows, click **Row Based Chart** then click **Okay** to return to the Chart Wizard.![OHy4s8uJ44.png](https://devnet.logianalytics.com/hc/article_attachments/5432328321815/ohy4s8uj44.png)
    4. Under **Data for Chart**, make the following choices, then click Next to advance to the **Appearance** tab.
       * **Data Values** — choose the formula `=AggSum({OrderDetails.UnitPrice}*{OrderDetails.Quantity})`. This setting determines the size of the colored segments in each column.
       * **Data Labels** — choose the formula `={Employees.FirstName}`& ” ” & {Employees.LastName}. This setting determines the labels that appear along the X-axis of the chart.
       * **Series Labels** — choose the cell value `Categories.CategoryName`. This setting determines the labeling of each of the Data Values.
    5. Under **Colors**, choose *Blue Grey* as the **Theme**.
    6. Under **Labels**, enter *Employee Sales by Category* for the **Chart Title**.
    7. Click **Finish** to close the Chart Wizard.
21. Save the report with the chart.
22. The report design should now look like this:![PpHeaILRvk.png](https://devnet.logianalytics.com/hc/article_attachments/5432393129367/ppheailrvk.png)Run the report to see the completed report design in the Report Viewer. Congratulations!![Ovp0cEO0n8.png](https://devnet.logianalytics.com/hc/article_attachments/5432443618455/ovp0ceo0n8.png)

### Additional Resources

* [Advanced Reports: Sections (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281572597527-Advanced-Reports-Sections-v2021-1-)
* [Advanced Reports: Design Grid (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281555584663-Advanced-Reports-Design-Grid-v2021-1-)
* [Advanced Reports: Sorts](https://devnet.logianalytics.com/hc/en-us/articles/5281555992343-Advanced-Reports-Sorts)
* [Charts and the Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281542473367-Charts-and-the-Chart-Wizard)

In versions *pre-v2021.1*:

This section will walk users through the **New Report Wizard** and demonstrate how to create a new report from start to finish.

1. In the main menu, click the **Create New Report** ![MainLeftPaneNewReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432314432023/mainleftpanenewreport.png) icon.
2. There are several types of reports, the most common being an **Advanced Report**.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic will focus on building an **Advanced Report.** For information on the other types of reports, see the topic on [Report Types](https://devnet.logianalytics.com/hc/en-us/articles/5281561339799-Report-Types).

The **Report Wizard** will open. The Report Wizard has five tabs: Name, Categories, Sorts, Filters and Layout. The Name and Categories tabs must be completed while the other tabs are optional.

### Name Tab

In the Name tab, enter a report name and click on the folder where the report will be saved.

The report name can be up to 255 characters long. The following special characters may not be used: `? : / * “ < >`

The report’s description appears at the bottom of the Main Menu when it is selected. The description text may also be used to search for a report.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> You cannot create a report inside a folder that is read-only ![](https://devnet.logianalytics.com/hc/article_attachments/5432176031767/treereportlock.png)

![screen.ar_nametab.png](https://devnet.logianalytics.com/hc/article_attachments/5432420639383/screen.ar_nametab.png)

### Categories Tab

In the Categories Tab, select the Data Categories that you would like to have access to on the report. It is important to understand two terms: Data Category and Data Field.

**Data Category** – A Data Category is a data object that has several attributes. For example, *Students* is a category; each student has an ID, a major, an advisor, etc.

**Data Field –** A Data Field is a single attribute within a category. For example, *Students.ID* is the numeric value that identifies a specific student.

![screen.ar_categoriestab.png](https://devnet.logianalytics.com/hc/article_attachments/5432450665751/screen.ar_categoriestab.png)

* To add a Data Category, either drag and drop it to the Category Name column, use the ![](https://devnet.logianalytics.com/hc/article_attachments/5432239633943/add.png)**Add** button, or double-click the category.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> When one Data Category is added, other Data Categories that are not joined to it become unavailable by default.

* To search for a specific Data Category or folder, type its name into the Search box.
* To see what Data Fields are in a Data Category, click on a Data Category and then click the information ![](https://devnet.logianalytics.com/hc/article_attachments/5432321848855/information.png) button.
* Check the *Suppress Duplicates* box to suppress any repeated records from that category.
* To remove a Data Category, click the delete ![](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) button.

For this report, we’ve selected **Categories**and **Products**.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> For each category selected, a user can **Suppress Duplicates** within the data by ticking the check box that appears next to the category name. This will suppress repeated items in the given category for the final report.

### Sorts Tab

In the Sorts tab, specify which Data Fields will be used to determine the order of data on the report.

![screen.ar_sortstab.png](https://devnet.logianalytics.com/hc/article_attachments/5432450718359/screen.ar_sortstab.png)

* To sort by a Data Field either drag and drop it to the **Sort By** Column, use the ![+](https://devnet.logianalytics.com/hc/article_attachments/5432239633943/add.png)**Add**  button, or double-click the field.
* You can sort each Data Field in Ascending (A-Z, 0-9) or Descending (Z-A, 9-0) order.
* Use the **Move Item Up**![^](https://devnet.logianalytics.com/hc/article_attachments/5432225168663/movegridrowup.png) and **Move Item Down**![v](https://devnet.logianalytics.com/hc/article_attachments/5432338912791/movegridrowdown.png) icons to indicate the sort priority.
* To remove a sort, click the Delete ![x](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon.

For this report we have sorted on *Categories.CategoryName*in descending order.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Sorts are not mandatory in order to create a report. Sorts allow for more complex organization of a report but do not bar the report wizard from continuing if left blank.

### Filters Tab

In the Filters tab, create statements that will be used to filter the data when you run a report.

![screen.ar_fitlerstab.png](https://devnet.logianalytics.com/hc/article_attachments/5432450749591/screen.ar_fitlerstab.png)

There is no limit to the number of filters that can be defined. Filters can be numeric (up to eight decimal places) or alphanumeric.

* To filter a Data Field, either drag and drop it to the ‘Filter By’ column, use the button or double-click it.
* Use the **Move Item Up**![^](https://devnet.logianalytics.com/hc/article_attachments/5432225168663/movegridrowup.png) and **Move Item Down**![v](https://devnet.logianalytics.com/hc/article_attachments/5432338912791/movegridrowdown.png) icons to indicate the filter priority.
* To remove a filter, click the **Delete**![x](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon.
* Set the operator (*equal to*, *less than*, *one of*, etc…) by selecting it from the **Operator** dropdown.
* Set the filter value by either entering it manually or selecting a value from the dropdown. If the Data Field is a date, the calendar and function buttons can be used to select a value.
* Choose **AND With Next Filter** to require that the selected filter and the one below it both evaluate to true. Choose **OR With Next Filter** to require that either or both be true.
* Check **Group With Next Filter** to group the filters. Filters can be nested indefinitely by using the following keyboard shortcuts while a filter is selected:
  + **Ctrl + [** adds an open-parenthesis before the selected filter.
  + **Ctrl + ]** adds a close-parenthesis after the selected filter.
  + **Ctrl + Shift + [** removes an open-parenthesis from before the selected filter.
  + **Ctrl + Shift + ]** removes a close-parenthesis from after the selected filter.
* Check **Prompt for Value** to prompt the user for a new filter value at the time the report is executed.

For this report, an **Equal To** filter on *Category Name* has been created in order to limit the data on the final report.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Like Sorts, Filters add complexity to a report but, but their completion is not mandatory.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> If a filter is chosen, the above fields must be completed or the report will not execute.

### Layout Tab

In the Layout tab, select the Data Fields that will appear on the report. For each Data Field chosen, the report will automatically create a column header and place the Data Field in the detail section. Additionally, subtotals, grand totals, and a page header/footer can be created.

![screen.ar_layouttab.png](https://devnet.logianalytics.com/hc/article_attachments/5432443693335/screen.ar_layouttab.png)

### Display Data

* To place a Data Field on the report, either drag and drop it to the **Data Field** column, use the Add ![+](https://devnet.logianalytics.com/hc/article_attachments/5432239633943/add.png) button, or double-click the field.
* Use the **Move Item Up**![^](https://devnet.logianalytics.com/hc/article_attachments/5432225168663/movegridrowup.png) and **Move Item Down**![v](https://devnet.logianalytics.com/hc/article_attachments/5432338912791/movegridrowdown.png) arrows to indicate the order the Data Fields should appear on the report. The Data Field at the top will appear on the report as the left-most column.
* The Summary Function column is used to make subtotals and grand totals.
* To remove a Data Field, click the **Delete**![x](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon.

Using the **Summarize By** box, you can display subtotals, grand totals, or headers for the values of a Data Field.

### Subtotals and Grand Totals

* To display subtotals, check the box of the category you want subtotals for in the **Summarize By** box. Then, for each Data Field you want totaled, select a Summary Function (see below).
* To display grand totals, check the Grand Total box. Then for each Data Field you want totaled, select a Summary Function (see below).

![screen.ar_summarizeby.png](https://devnet.logianalytics.com/hc/article_attachments/5432477675799/screen.ar_summarizeby.png)

### Summary Functions

* **Sum**: Totals the all of the data in the Data Field.
* **Count**: Returns the number of rows in the Data Field.
* **Average**: Takes the mean of the data in the Data Field.
* **Minimum**: Displays the lowest value in the Data Field.
* **Maximum**: Displays the highest value in the Data Field.

### Data Headers

A checkbox will appear in the **Summarize By** box for each Data Category in the **Sorts** tab. To display a header for each value of a Data Field, click on the associated Data Category in the Summarize By box. Click the Data Category name next to the checkbox, and the will appear.

* To include a Header, check the **Include Header at the beginning** checkbox. In order to select the text that will appear as the header value, use the Header dropdown to select a Data Field or use the **Formula Editor**![fx](https://devnet.logianalytics.com/hc/article_attachments/5432247626647/formula.png) icon to create a formula.
* Use the **Summarize by each unique** dropdown to specify if the header should repeat based on a specific field or fields within a Category.
* Check the **Include Total at the end** checkbox to have a subtotal created for this Category.

For this report, the Data Fields `Products.ProductName`, `Products.ProductID`, `Products.UnitPrice`, and `Products.QuantityPerUnit` have been selected.

* To see the report in the Report Designer, click **Finish**.

The Report Designer will display the report like this.

![screen.ar_reportdesigner.png](https://devnet.logianalytics.com/hc/article_attachments/5432420722967/screen.ar_reportdesigner.png)
