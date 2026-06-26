---
title: "Dashboard Designer: Visualization Tiles (v2019.2+)"
id: 5281619429015
section: "Dashboards"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281619429015-Dashboard-Designer-Visualization-Tiles-v2019-2
updated_at: 2022-05-03T22:09:09Z
---

# Dashboard Designer: Visualization Tiles (v2019.2+)

# Dashboard Designer: Visualization Tiles (*v2019.2+*)

A **visualization** is a graphical representation of data that can be designed directly on the Dashboard canvas without first creating a report. The figures below are a small sampling of the visualizations that can be built directly on the Dashboard.

![Tabular visualization](https://devnet.logianalytics.com/hc/article_attachments/5432336915863/explorer_ikynvipm9g.png)

Tabular visualization

![Pie chart visualization](https://devnet.logianalytics.com/hc/article_attachments/5432297231511/pie-chart.png)

Pie chart visualization

![Line chart visualization](https://devnet.logianalytics.com/hc/article_attachments/5432353765399/line-chart.png)

Line chart visualization

![zDdSkiR8JU.png](https://devnet.logianalytics.com/hc/article_attachments/5432353826967/bar-chart.png)

Bar chart visualization

![Pareto chart visualization](https://devnet.logianalytics.com/hc/article_attachments/5432224070807/pareto-chart.png)

Pareto chart visualization

To add a new **Visualization Tile** to a **Dashboard**, review [Dashboard Designer (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281580652951-Dashboard-Designer-v2019-2-). Add tiles with the ![NewTileButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432328391575/newtilebutton.png)**New Tile** menu.

## Creating Visualizations

1. Add a new **visualization tile** to the canvas.
2. Select the **Chart Type** from the **Content** tab of the **Tile Properties Pane** on the right side of the screen. When a new visualization tile is added to the canvas, *Bar* will be selected by default. The documentation section on [Charts and the Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281542473367-Charts-and-the-Chart-Wizard) includes detailed information about the different chart types and how to build them. Dashboards also support an additional *Tabular* visualization type.
3. Next, add data to the visualization by dragging-and-dropping a **Data Object** from the ![MainLeftPaneDataFields.png](https://devnet.logianalytics.com/hc/article_attachments/5432259815831/mainleftpanedatafields.png)**Data Field Pane** on the left side of the screen to the tile. Once at least one Data Object is on the tile, the **Data** section of the **Tile Properties Pane**‘s **Content** tab will also allow Data Object selection. Drag the Data Objects either to the *Values* section on the left side of the tile, or to the *Groups* section on the right side of the tile. *Groups* represent the labels of the chart, whereas the *Values* represent the quantities that will be charted. For example, to create a bar chart that shows total Revenue for each Employee, the Data Object `OrderDetails.Revenue` would be added as a *Value* and `Employee.LastName` would be added as a *Group*.  
     ![CD8OkvKd6u.png](https://devnet.logianalytics.com/hc/article_attachments/5432297380759/cd8okvkd6u.png) or ![FaAvVkKYrS.png](https://devnet.logianalytics.com/hc/article_attachments/5432297401751/faavvkkyrs.png)  
   Some visualization types (*Tabular*, *Bar*, *Column*and *Line**)* allow multiple *Groups* to be added. When a chart has multiple *Groups*, it can categorize the displayed *Values*. Additional groups can be added by dragging the Data Object to the tile, or clicking on the ![Add.png](https://devnet.logianalytics.com/hc/article_attachments/5432239633943/add.png)**Add** button in the Content tab. For example, to see the total Revenue for each Employee by Category, `Category.CategoryName` could be added as a second group.

   The figure below shows a single group bar chart on the left and a multi-group bar chart on the right. Every color change in each bar in the chart on the right represents a different category’s contribution to that employee’s total revenue.

   ![zDdSkiR8JU.png](https://devnet.logianalytics.com/hc/article_attachments/5432353826967/bar-chart.png)

   ![76RxxZgqo5.png](https://devnet.logianalytics.com/hc/article_attachments/5432224143383/76rxxzgqo5.png)

   Multiple *Groups* can be re-ordered which changes how the *values* are categorized. Drag the *Groups* in the Content tab and move them up or down to reorder them. Using the same example above, but changing the order of the *Groups,* the chart changes to show each Employee’s contribution to the Total Revenue for each Category:

   ![Z55lS43ITK.png](https://devnet.logianalytics.com/hc/article_attachments/5432224157207/z55ls43itk.png)

   Some visualization types *(Tabular, Bar, Column, Line, KPI)* allow multiple *Values* to be added to the chart. This adds another quantity to the display. For example, a bar chart showing the number of units in stock and the number of units on order side-by-side can be made by having both `Products.UnitsInStock` and `Products.UnitsOnOrder` as *Values*. Additional *values* can be added by dragging the Data Object to the tile, or clicking on the ![Add.png](https://devnet.logianalytics.com/hc/article_attachments/5432239633943/add.png)**Add** button in the Content tab of the Tile Properties Pane.

   Multiple *Values* can be re-ordered which changes how the *values* are ordered. Drag the *Values* in the Content tab and move them up or down to reorder them.

   ![vcoXN5tVsG.png](https://devnet.logianalytics.com/hc/article_attachments/5432353990679/vcoxn5tvsg.png)
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
   >
   > When adding multiple values to a KPI visualization, choose values which have the same [Number](https://devnet.logianalytics.com/hc/en-us/articles/5281564235671-Cell-Formatting#Number) as only one format can be chosen for the whole visualization tile. For example, include only currency or date values in the same tile.
4. Then, in the **Data** section of the Content tab of the Tile Properties Pane, further customization of the input data can be applied. Click on either the *Group* or *Value* to open the popover.  
   ![table-values.png](https://devnet.logianalytics.com/hc/article_attachments/5432337230359/table-values.png)![table-groups.png](https://devnet.logianalytics.com/hc/article_attachments/5432354056599/table-groups.png)![pie-chart-values.png](https://devnet.logianalytics.com/hc/article_attachments/5432224245271/pie-chart-values.png)  

   From left to right: the Values popover from a tabular visualization, the Groups popover from a tabular visualization and the Values popover from a pie chart

   * [What are formulas?](https://devnet.logianalytics.com/hc/en-us/articles/5281600700183-What-are-formulas-) can be applied to both the *Groups* and the *Values*, including aggregate functions (for *Values* only) by clicking the **Formula Editor ![FormulaLarge.png](https://devnet.logianalytics.com/hc/article_attachments/5432236378775/formulalarge.png)** icon.
   * *Values* can be given a friendly name in the **Display Name** field. This name is displayed prominently in KPI visualizations, chart legends and tabular visualization column labels. *Groups* in *Tabular Visualizations* may also be given a **Display Name**.
   * An **Aggregate** can be chosen from the dropdown (*Sum, Average, Count, Distinct Count, Min, Max or None)*which will aggregate the *Values*. For example, to get the total Revenue for each Employee, choose *Sum*. Functions not included in the list can be added with the Formula Editor.
   * **Tabular Visualizations** have two additional properties that can be changed:
     + *Groups* and *Values* can be sorted in either *ascending* or *descending* order by checking the **Sort** checkbox. When checked, the **Direction** dropdown appear allowing selection of sorting in *Ascending* or *Descending* order.
     + Checking the **Hide Detail** checkbox below the list of **Values** hides the individual rows from the table and shows only the aggregated category summary.
5. Formatting such as color themes, chart titles, X- and Y-axis labels, legends and number formatting can be customized in the [Style](#Style) tab of the Tile Properties Pane.
6. Advanced features such as automatic data reloading, sorting, changing the axes values, and applying Filters can be customized in the [Advanced](#Advanced) tab of the Tile Properties Pane.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Modifying the groups, values, aggregates or changing between tabular and other chart types, or changing the Hide Detail property of a tabular visualization will require a **Refresh** of the tile’s contents.

## Tile Properties Pane

Controls for building and interacting with the **Visualization** tile are contained in the **Tile Properties Pane** on the right side of the Dashboard Designer.

### Content

The **Content** tab for **Visualizations** is further broken down into two areas: **Chart Type** and **Inputs**.

**Chart Type** sets the type of visualization displayed. The documentation on [Charts and the Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281542473367-Charts-and-the-Chart-Wizard) includes detailed information about the different chart types and how to build them. Dashboards also have the *Tabular* type which is unique to the Dashboard Designer. *Tabular Visualizations* display data in a categorized table format.

Choose from the different categories:

* *![ChartTypeTabular.png](https://devnet.logianalytics.com/hc/article_attachments/5432354093591/charttypetabular.png)Tabular*
* *![ChartTypeColumn.png](https://devnet.logianalytics.com/hc/article_attachments/5432354124567/charttypecolumn.png)Bar and Column Type*
  + *![ChartTypeBar.png](https://devnet.logianalytics.com/hc/article_attachments/5432297628311/charttypebar.png)Bar*
  + *![ChartTypeStackBar.png](https://devnet.logianalytics.com/hc/article_attachments/5432224327447/charttypestackbar.png)Stack Bar*
  + *![ChartTypeStackBar100.png](https://devnet.logianalytics.com/hc/article_attachments/5432337384215/charttypestackbar100.png)Stack Bar 100*
  + *![ChartTypePareto.png](https://devnet.logianalytics.com/hc/article_attachments/5432354236567/charttypepareto.png)Pareto*
  + *![ChartTypeColumn.png](https://devnet.logianalytics.com/hc/article_attachments/5432354124567/charttypecolumn.png)Column*
  + *![ChartTypeStackColumn.png](https://devnet.logianalytics.com/hc/article_attachments/5432337446935/charttypestackcolumn.png)Stack Column*
  + *![ChartTypeStackColumn100.png](https://devnet.logianalytics.com/hc/article_attachments/5432224418711/charttypestackcolumn100.png)Stack Column 100*
* *![ChartTypePie.png](https://devnet.logianalytics.com/hc/article_attachments/5432297719447/charttypepie.png)Pie and Other Types*
  + *![ChartTypePie.png](https://devnet.logianalytics.com/hc/article_attachments/5432297719447/charttypepie.png) Pie*
  + *![ChartTypeDonut.png](https://devnet.logianalytics.com/hc/article_attachments/5432328812951/charttypedonut.png)Donut*
  + *![ChartTypePyramid.png](https://devnet.logianalytics.com/hc/article_attachments/5432354379287/charttypepyramid.png)Pyramid*
  + *![ChartTypeFunnel.png](https://devnet.logianalytics.com/hc/article_attachments/5432349203351/charttypefunnel.png)Funnel*
* *![ChartTypeLine.png](https://devnet.logianalytics.com/hc/article_attachments/5432224496535/charttypeline.png)Line*
  + - *![ChartTypeLine.png](https://devnet.logianalytics.com/hc/article_attachments/5432224496535/charttypeline.png)Line*
    - *![ChartTypeSpline.png](https://devnet.logianalytics.com/hc/article_attachments/5432349307671/charttypespline.png)Spline*
    - *![ChartTypeArea.png](https://devnet.logianalytics.com/hc/article_attachments/5432329010967/charttypearea.png)Line Area*
    - *![ChartTypeSplineArea.png](https://devnet.logianalytics.com/hc/article_attachments/5432224529303/charttypesplinearea.png)Spline Area*
  + - *![ChartTypeStackedArea.png](https://devnet.logianalytics.com/hc/article_attachments/5432337830167/charttypestackedarea.png)Stacked Area*
    - *![ChartTypeZoomLine.png](https://devnet.logianalytics.com/hc/article_attachments/5432329107607/charttypezoomline.png)Zoom Line*
  + *![ChartTypeRadar.png](https://devnet.logianalytics.com/hc/article_attachments/5432354801175/charttyperadar.png)Radar*
* *![ChartTypeScatter.png](https://devnet.logianalytics.com/hc/article_attachments/5432329159959/charttypescatter.png)Scatter*
  + *![ChartTypeScatter.png](https://devnet.logianalytics.com/hc/article_attachments/5432329159959/charttypescatter.png)Scatter*
  + *![ChartTypeZoomScatter.png](https://devnet.logianalytics.com/hc/article_attachments/5432329203095/charttypezoomscatter.png)Zoom Scatter*
* *![ChartTypeKPI.png](https://devnet.logianalytics.com/hc/article_attachments/5432338075927/charttypekpi.png)Key Performance Indicator (KPI)*

The **Data** section is where the *Groups* and *Values* for the visualization are configured. To add Groups or *Values*, click the corresponding ![Add.png](https://devnet.logianalytics.com/hc/article_attachments/5432239633943/add.png)

**Add** ![MainLeftPaneDataFields.png](https://devnet.logianalytics.com/hc/article_attachments/5432259815831/mainleftpanedatafields.png)**Data Field Pane**![VQwHvrRfeY.png](https://devnet.logianalytics.com/hc/article_attachments/5432355223575/vqwhvrrfey.png)  

Data section of the **Content** tab for a newly created bar visualization tile

**Groups** represent the categorization of data on the report. **Values** represent the quantities of each of those categories. For example, a column chart showing the total revenue per employee could use *Employees.LastName* as the *Groups* and a formula which calculates the sum of *OrderDetails.Revenue* for the *Values*.

**Formulas** may be entered for either the *Groups* or *Values* by clicking on the corresponding *Group* or *Value* and then on the **Formula Editor**![FormulaLarge.png](https://devnet.logianalytics.com/hc/article_attachments/5432236378775/formulalarge.png) icon. [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/5281623158039-Formula-Editor) contains more information about how to use Formulas.

*Groups* and *Values* may be re-ordered by clicking on the **reordering handle**![SearchOptionsActive.png](https://devnet.logianalytics.com/hc/article_attachments/5432329305367/searchoptionsactive.png) icon and dragging-and-dropping them. Re-ordering *Groups* changes how the *values* are categorized. Reordering *Values* changes the order multiple values appear in the visualization.

![CCrVUlgZXj.gif](https://devnet.logianalytics.com/hc/article_attachments/5432329347607/ccrvulgzxj.gif)  

Re-ordering *Groups* in the **Content** tab

For a **Tabular Report**, checking the **Hide Detail** checkbox will remove the tabular data from the report and show only the aggregate summary. For example, the tile on the left below shows the detail rows, and they are hidden in the tile on the right.

![pJ4FemOJVt.png](https://devnet.logianalytics.com/hc/article_attachments/5432329370775/pj4femojvt.png)

![JelwIXH123.png](https://devnet.logianalytics.com/hc/article_attachments/5432224784151/jelwixh123.png)

### Style

The **Style** tab for **Visualizations** is further broken down into additional areas depending on the type of visualization in the tile. They are: **Color**, **Labels**, **Number Format**, **Tabular Text**, **Fit** and **Tile**.

The **Color** section applies to all visualization types and is where the general appearance of the visualization is set.

![firefox_hvdg33O9Gm.png](https://devnet.logianalytics.com/hc/article_attachments/5432224805271/firefox_hvdg33o9gm.png)  

Color section of the Style tab

* A **theme** can be chosen from the list,
* A **linear range** of colors can be specified (available for all types except *Tabular* visualizations), or
* A **custom** arrangement of colors may be chosen.
* Checking the **3D** checkbox will apply a three-dimensional effect to the visualization.

The **Tabular Text** section applies only to *Tabular* visualizations and is where the font type and color are set.

The **Fit** section applies only to *Tabular* visualizations.

* v2021.1.6+ Setting a **Minimum Column Width** prevents columns of the table from shrinking below a set number of pixels wide. If all of the columns are wider than the space available in the tile, a horizontal scroll bar appears. The default value is *100*.

The **Labels** section applies to all of the chart types except *Tabular.* Labels on the visualization such as a title, axis labels, data points and a legend are configured here. These label choices will vary depending on the type of visualization.

![ZGOb2ADM83.png](https://devnet.logianalytics.com/hc/article_attachments/5432338338455/zgob2adm83.png)  

Labels section

* **Title:** when checked, will add a title to the visualization and allow formatting of the font, size color and position of it
* **Subtitle:** when checked, will add a subtitle under the main title and allow formatting of the font, color and alignment of it
* **X and Y-Axis**: when checked, will add labels to the horizontal (X) and vertical (Y) axes and allow formatting of the font, color and position of them. Only available for *column*, *bar*, *spline*, *line (except Radar)* and *scatter* visualizations. For visualization types other than *bar* and *tabular,* an additional dropdown box will appear to set the orientation of the data labels. This tells the application what to do if there is not enough space in the tile to display the whole label. Choose from:
  + *Auto*: allow the application to select the best orientation for you based on available space in the tile
  + *![g68qOn5XeZ.png](https://devnet.logianalytics.com/hc/article_attachments/5432268236183/g68qon5xez.png)Slant:* rotate the labels 45-degrees along the axis
  + ![sKYCRS3Dta.png](https://devnet.logianalytics.com/hc/article_attachments/5432268283671/skycrs3dta.png)*Wrap:* texts wraps to a new line
  + ![niDP7gwXFf.png](https://devnet.logianalytics.com/hc/article_attachments/5432221287063/nidp7gwxff.png)*Stagger:* values are staggered along two lines so they don’t overlap
  + ![7YBRqc1t7H.png](https://devnet.logianalytics.com/hc/article_attachments/5432221296535/7ybrqc1t7h.png)*Rotate:* rotate the labels 90-degrees along the axis
  + ![Sm9YGoPcF6.png](https://devnet.logianalytics.com/hc/article_attachments/5432289619351/sm9ygopcf6.png)*None:* do not apply any change to labels, they may overlap
* **Points**: when checked, will add data points to the visual elements. Not available for *Tabular* or *KPI* visualizations. Different types will have different choices available:  

  | Choice | Visualization Category | Description |
  | --- | --- | --- |
  | None | All | Does not display data points on the chart. |
  | Series Values | Bar, Line, Pie | Displays the value of the *Values* |
  | Percent of Series Values | Pie | Displays the percentage of the whole represented by this *value*. |
  | Data Labels | Pie | Displays the names of the *Groups* represented each segment of the chart. |
  | Data Labels with Data Values | Pie | Combines the behavior of both *Data Labels* and *Series Values* modes to place both pieces of information in the label. |
* **Legend**: when checked, will add a legend to the visualization located on the tile according to the choice made in the dropdown box, either *Right* or *Bottom*.

The **Number Format** section sets the way that numbers are displayed for *Bar and Column, KPI* and *Line charts.* It works very similar to the other [Number](https://devnet.logianalytics.com/hc/en-us/articles/5281564235671-Cell-Formatting#Number) formatting options throughout the application.

![LiSDC1CJNB.png](https://devnet.logianalytics.com/hc/article_attachments/5432329505047/lisdc1cjnb.png)  

Number Format section

* **Decimal**: when checked, will force a specified number of decimal places to be displayed. The symbol inserted between the whole and fractional part of the number can be specified, as well as the number places after the symbol.
* **1000 Separator**: when checked, will separate thousands places with the specified symbol
* **Currency**: when checked, will display the specified currency symbol in front of the value
* **Percentage**: when checked, will display a percent sign (%) after the value
* **KPI Value Format** applies only to KPI visualizations to set how the value is presented in the tile. Choose from:
  + *English Short Scale  
    ![firefox_pmhx16svE9.png](https://devnet.logianalytics.com/hc/article_attachments/5432329524503/firefox_pmhx16sve9.png)*
  + *Scientific Notation  
    ![firefox_fentOe92oR.png](https://devnet.logianalytics.com/hc/article_attachments/5432329555863/firefox_fentoe92or.png)*
  + *Expanded  
    ![firefox_X3Yeus3xPg.png](https://devnet.logianalytics.com/hc/article_attachments/5432329591703/firefox_x3yeus3xpg.png)*

The **Tile** sectionis where tile appearance can be changed. The settings here override the [**Canvas Format**](https://devnet.logianalytics.com/hc/en-us/articles/5281580652951-Dashboard-Designer-v2019-2-#Backgrou) defaults.

* Check **Background** to set a background color for the tile. Click **Color** to open the color selector and choose a background color. Unchecking the **Background** checkbox makes the tile transparent.
* Check **Tile Header** to set a background color for the tile’s header. Click **Color** to open the color selector and choose a background color. Unchecking the **Tile Header** checkbox makes the header background transparent.  
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > The Tile Header options are only shown if the Tile Header is visible on the canvas.
* Check **Shadow** to show a slight shadow effect around the tile.
* Check **Border** to apply a border to the tile.
  + Check **Customize Border** to set the properties of each of the four tile borders individually. Leave unchecked to have the border properties applied equally to the four sides.
  + Click **Color** to open the color selector and choose a border color.
  + **Width** sets the border width in pixels.
  + **Round** sets the roundness of the corners.

### Advanced

The **Advanced Tab** for **Visualizations** is further broken down into two areas: **Refresh** and **Navigation** (*Tabular* only) or **Data Display** (*Other Chart Types*).

**Refresh** contains one checkbox, to enable automatic refreshing of the data in the [Dashboard Viewer (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281602922903-Dashboard-Viewer-v2019-2-). Check the box and then set the number of seconds in between report refreshes. Uncheck the box to disable automatic report refreshing.

**Navigation** applies only to *Tabular* charts and contains one additional control **Allow searching**that will add a search box at the bottom of the tile.

The **Data Display** section applies to the other chart types and has additional controls for how the chart is formatted:

* Use the **Sort By** dropdown to apply a secondary sort to the chart that will affect the order *Values* are added to the visualization. Choose from *Ascending* or *Descending* order by selecting from the dropdown.
  + *None* adds the *Values* in the order they are returned from the data source.
  + *Data Labels* sorts the data based on the *Groups* in the visualization
  + *Data Values* sorts the data on the *Values* in the visualization

* Check the **Limit Values** checkbox to set a **Min** and **Max** value for the axes labels. If the *Values* in the chart exceed these settings, the settings are ignored.  
  ![U3ayDYafJj.png](https://devnet.logianalytics.com/hc/article_attachments/5432355711639/u3aydyafjj.png)  

  Bar visualization with no **Limit Values** set

  ![ZOxWuvaUpo.png](https://devnet.logianalytics.com/hc/article_attachments/5432224912407/zoxwuvaupo.png)  

  The same bar visualization with **Min** set to 200 and **Max** set to 210,000. Note the change in bar size and the labels along the X-axis.
* Check the **Exclude Values** checkbox to exclude *Values***Less Than** or **Greater Than** these settings from appearing in the chart.
* Click the **Advanced Filters** button to open the **Visualization Advanced Filters Wizard**. Similar to the Report Designer’s Filter Wizard, this wizard allows Filters to be applied to this visualization tile. Advanced Filters created here do not show up in the **Dashboard Designer**‘s **Filters** menu, nor do they appear in the **Dashboard Viewer**‘s **Filters** pane. Advanced Filters created here are applied before the Dashboard Designer or Dashboard Viewer is launched and can be used to limit the amount of data returned from the data source, which can be useful when working with very large amounts of data to improve Dashboard performance.
