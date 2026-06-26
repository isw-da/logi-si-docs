---
title: "ExpressView: Introduction (pre-v2021.1)"
id: 5281612161815
section: "ExpressView"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281612161815-ExpressView-Introduction-pre-v2021-1
updated_at: 2022-05-03T22:09:04Z
---

# ExpressView: Introduction (pre-v2021.1)

# ExpressView: Introduction (*pre-v2021.1*)

The **ExpressView Designer** is a data discovery tool that simplifies grouping, sorting, filtering, and aggregating data with a drag-and-drop interface. A chart can be added with a single click, and ExpressViews can be styled and saved as PDF, RTF, CSV, or Excel files.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> This topic applies to the ExpressView Designer in *pre-v2021.1*. For *v2021.1+*, refer to [ExpressView: Introduction (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281589443095-ExpressView-Introduction-v2021-1-)

![d8CbKAIRPd.png](https://devnet.logianalytics.com/hc/article_attachments/5432222264983/d8cbkairpd.png)

The ExpressView Designer

## Making an ExpressView

ExpressView allows you to quickly see data and make reports without concern for the minutiae of old-fashioned report building.

To make an ExpressView:

1. Click the **Create** **New Report ![MainLeftPaneNewReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432314432023/mainleftpanenewreport.png)**icon and select ![ThumbnailExpressView.png](https://devnet.logianalytics.com/hc/article_attachments/5432275054231/thumbnailexpressview.png)**ExpressView**.

   The ExpressView Designer is divided into the Data pane on the left, and the Design pane in the middle. The Data pane comprises all of the accessible data categories, containing groups of related data fields. Click the **Choose Data** icon to expand or collapse the Data pane.
2. Expand a category by clicking the arrow ![ArrowCollapse.png](https://devnet.logianalytics.com/hc/article_attachments/5432314486807/arrowcollapse.png) icon. This shows the fields in that category.
3. Drag a field onto the Design pane to add it to the ExpressView. This expands the field into a data column. It will only show placeholder data initially.  
   ![Dragging field to Design pane](https://devnet.logianalytics.com/hc/article_attachments/5432275113239/screen.expressview_drag_field.png)

   Dragging a field onto the Design pane
4. Continue to add fields as desired. Fields can be added or removed at any time.

   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > As fields are added, unrelated fields become unavailable. To learn about how fields relate to each other, see [Advanced Reports: Joins](https://devnet.logianalytics.com/hc/en-us/articles/5281549160087-Advanced-Reports-Joins).
5. When satisfied with the data selection, click **![Run](https://devnet.logianalytics.com/hc/article_attachments/5432248428183/run.png)**to populate the ExpressView with data. Page through your data using the navigation icons ![PageHome.png](https://devnet.logianalytics.com/hc/article_attachments/5432291191831/pagehome.png) ![PageUp.png](https://devnet.logianalytics.com/hc/article_attachments/5432251989783/pageup.png) ![PageDown.png](https://devnet.logianalytics.com/hc/article_attachments/5432307056279/pagedown.png) ![PageEnd.png](https://devnet.logianalytics.com/hc/article_attachments/5432222191895/pageend.png) in the toolbar.  
   > ![(!)](https://devnet.logianalytics.com/hc/article_attachments/5432314556567/alerttoolbar.png)
   >
   > **Truncated results displayed**  
   > This icon and message indicates that the report has only returned a partial data set. There are fewer detail rows than the full set, and aggregate formulas and visualizations apply only to the data that was returned to the report.
   >
   > To retrieve more data, click the icon and select either:
   >
   > * **Generate +number** to get the next number of data rows and add them to the existing report.
   > * **Generate All** to get the full data set.
6. Click the **Save ![Save.png](https://devnet.logianalytics.com/hc/article_attachments/5432229545751/save.png)**icon to save the ExpressView. In the Settings window, enter a Name and select a folder where it should be stored. Then click **Save Report Info**.

These steps illustrate how quick it is to make a tabular report from scratch using ExpressView. But **ExpressView** can be more than just basic reports. You can make groups, charts, calculations, and customize the look of the report. And it is all designed to be easy to use. The topics in this section will describe how to use these powerful features.

To switch off the data view and revert back to design view, click ![Stop](https://devnet.logianalytics.com/hc/article_attachments/5432248462359/stop.png) in the toolbar.

### About the Radial Menu

Throughout this topic you will see references to a menu called the **Radial Menu**. The Radial Menu is a menu of options for each data column and group, which is accessed by clicking the colored **Radial ![custom.RadialButtonBlue.png](https://devnet.logianalytics.com/hc/article_attachments/5432294787351/custom.radialbuttonblue.png)**icon on the top left of the column or group.

![using-radial-menu.png](https://devnet.logianalytics.com/hc/article_attachments/5432294815767/using-radial-menu.png)

Using the radial menu

Each radial menu has four options, arranged in a circle around the center. When you are prompted to select a radial menu option, you will be asked to “use ![custom.RadialButtonBlue.png](https://devnet.logianalytics.com/hc/article_attachments/5432294787351/custom.radialbuttonblue.png) radial>***direction***“. *Direction* is one of the four cardinal directions corresponding with one of the four options: ***left***, ***right***, ***up***, ***down***.

For example, “use ![custom.RadialButtonBlue.png](https://devnet.logianalytics.com/hc/article_attachments/5432294787351/custom.radialbuttonblue.png) radial>**left**” means to open the radial menu and select the left option. To do this, you have two options:

* Click the radial icon, move the cursor left, then click again.
* Click-and-hold the radial icon, drag the cursor left, then release.

To close the radial menu without selecting an option, click in the center.

## Interactive Editing

With the introduction of interactive editing to ExpressView in *v2018.2*, customize the report by right-clicking on the desired section while in design or live mode.

![rightclickhtmlEV.png](https://devnet.logianalytics.com/hc/article_attachments/5432291862935/rightclickhtmlev.png)

Right-click options include all of the capabilities of the radial menu, conditional filters, and formatting options such as text alignment, font type, and font color.

## Conditional Selector Dropdown

![idEV3V57no.png](https://devnet.logianalytics.com/hc/article_attachments/5432275239063/idev3v57no.png)

The Conditional Selector dropdown allows you to conditionally select certain values in the column you’ve right-clicked: *Apply to all*, *Apply to equal values*, *Apply to unequal values*, *Apply to greater values*, *Apply to greater than or equal values*, *Apply to lesser values* or *Apply to less than or equal values*. This choice will then select the applicable values in the column so changes to the formatting options will only affect them.

If the system administrator has enabled editing ExpessView with Live Data, changing the dropdown will enable the **Create Filter ![funnel](https://devnet.logianalytics.com/hc/article_attachments/5432314899095/editfilter.png)** icon. Clicking the icon creates a filter in the Filter Pane based on the value that was right-clicked and the condition in the dropdown. For example in the figure above, right-clicking on *08-12-1964* and selecting *Apply to unequal values* creates a new filter on the *BirthDate* field with an *Is Not Equal To* operator and the value *08-12-1964.*

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> aving the ExpressView will save any filters created with the **Create Filter ![funnel](https://devnet.logianalytics.com/hc/article_attachments/5432314899095/editfilter.png)** icon but conditional formatting is cleared once Live Data is turned off. To persist conditional formatting, consider saving the ExpressView as an Advanced Report and applying conditional cell formatting instead.
