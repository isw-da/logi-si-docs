---
title: "Advanced Reports: Using the Toolbar (pre-v2021.1)"
id: 5281556067735
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281556067735-Advanced-Reports-Using-the-Toolbar-pre-v2021-1
updated_at: 2022-05-03T22:09:22Z
---

# Advanced Reports: Using the Toolbar (pre-v2021.1)

# Advanced Reports: Using the Toolbar (*pre-v2021.1*)

The toolbar contains the buttons and menus used to modify the report. Modifications can include aesthetic formatting, inserting formulas and images, linking reports, and much more.

The system administrator has the ability to hide or show specific menu options and toolbar items. Some items may not be available to you.

![firefox_t5ON8UbnFX.png](https://devnet.logianalytics.com/hc/article_attachments/5432366322711/firefox_t5on8ubnfx.png)

Advanced Report Designer toolbar in *v2019.2+*

For application versions *pre-v2019.2*:

![Advanced Report Designer toolbar](https://devnet.logianalytics.com/hc/article_attachments/5432383377943/screen.toolbar.png)

Advanced Report Designer toolbar
*pre-v2019.2*

The toolbar begins with the **Settings** dropdown menu sometimes referred to as the cog wheel menu. This menu controls changes, such as renaming and filtering, that affect the entire report. All other buttons on the toolbar require that a cell (or cells) in the design grid be selected.

![Settings menu](https://devnet.logianalytics.com/hc/article_attachments/5432411005975/screen.optionsmenu.png)

Settings menu

* **![Rename.png](https://devnet.logianalytics.com/hc/article_attachments/5432366374167/rename.png) Rename**: Allows you to change the name and folder where the report will be saved. Enter a new name for the report, or choose a different folder. The name must be unique.
* **![Description.png](https://devnet.logianalytics.com/hc/article_attachments/5432399286423/description.png)Description**: Allows you to enter or change the description of the report or formula description (if enabled).
* **![Categories.png](https://devnet.logianalytics.com/hc/article_attachments/5432366414359/categories.png)Categories**: Allows you to change the **Categories** which are included on the report. See [Advanced Reports: Categories (pre-2021.1)](https://devnet.logianalytics.com/hc/en-us/articles/5281563625623-Advanced-Reports-Categories-pre-2021-1-) for more information.
* **![SortsMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432211886103/sortsmenu.png) Sorts**: Allows you to change the **Sorts** on the report. See [Advanced Reports: Sorts](https://devnet.logianalytics.com/hc/en-us/articles/5281555992343-Advanced-Reports-Sorts)
* **![Filter.png](https://devnet.logianalytics.com/hc/article_attachments/5432312749591/filter.png) Filters**: Allows you to change the **Filters** on the report. See [Filters](https://devnet.logianalytics.com/hc/en-us/articles/5281549708439-Filters).
* **![Template.png](https://devnet.logianalytics.com/hc/article_attachments/5432193608599/template.png) Template**: Allows you to setup document templates and forms. See [Advanced Reports: Templates](https://devnet.logianalytics.com/hc/en-us/articles/5281564145303-Advanced-Reports-Templates).
* **Options**: Allows you to change behavior of the report. The topic on [Options](https://devnet.logianalytics.com/hc/en-us/articles/5281541782039-Advanced-Reports-Report-Options) has detailed information about each option.
  + **![Options.png](https://devnet.logianalytics.com/hc/article_attachments/5432414860055/options.png) General**: Allows you to change things such as report export types, filter execution windows and page formatting. See [General Options](https://devnet.logianalytics.com/hc/en-us/articles/5281541782039-Advanced-Reports-Report-Options#General)
  + **![ConnectionStringVisible.png](https://devnet.logianalytics.com/hc/article_attachments/5432239418775/connectionstringvisible.png) Report Viewer**: Allows you to change things such showing the report grid, the toolbar and interactive filters and sorts in the report viewer. See [Report Viewer Options](https://devnet.logianalytics.com/hc/en-us/articles/5281541782039-Advanced-Reports-Report-Options#Report)
  + ![ExecutionCacheOptions.png](https://devnet.logianalytics.com/hc/article_attachments/5432213420695/executioncacheoptions.png)**Execution Caching**: Allows you to setup Execution Caching options for this report. This is an advanced feature, contact the system administrator for assistance with it.
  + **![CustomOptions.png](https://devnet.logianalytics.com/hc/article_attachments/5432399442327/customoptions.png) Custom**: Allows you to set any **Custom Options** on the report. This is an advanced feature, contact the system administrator for assistance with it.
* **Advanced**: Allows you to change advanced properties of the report.
  + **![Join.png](https://devnet.logianalytics.com/hc/article_attachments/5432414918423/join.png) Joins**: Allows you to define how categories on a report are related to one another. See [Joins](https://devnet.logianalytics.com/hc/en-us/articles/5281548966167-Advanced-Options#Joins)
  + **![TreeParameter.png](https://devnet.logianalytics.com/hc/article_attachments/5432185278615/treeparameter.png) Parameters**: Allows you to define reusable system variables, called Parameters, on the report. See [Report-Level Parameters v2019.1.3+](https://devnet.logianalytics.com/hc/en-us/articles/5281548966167-Advanced-Options#Report-L)
  + **![ExecutionCacheOptions.png](https://devnet.logianalytics.com/hc/article_attachments/5432213420695/executioncacheoptions.png) Show Generated SQL**: Allows you to view the generated SQL query which retrieves the data used on the report. See [Show Generated SQL v2019.1–v2021.1](https://devnet.logianalytics.com/hc/en-us/articles/5281548966167-Advanced-Options#Show2)

## Saving Reports

The report can be saved by clicking the **Save**![](https://devnet.logianalytics.com/hc/article_attachments/5432229545751/save.png) icon. Depending on system configuration, the report may also be saved when it is executed.

## Undo/Redo

Any action on a report can be undone by clicking on the **Undo**![Undo.png](https://devnet.logianalytics.com/hc/article_attachments/5432254416023/undo.png) icon or pressing **Ctrl** + **Z** on the keyboard.

Undone actions can be redone by clicking **Redo**![Redo.png](https://devnet.logianalytics.com/hc/article_attachments/5432212532503/redo.png) icon or pressing **Ctrl** + **Y** on the keyboard.

## Font & Alignment Options

The text of each cell can be formatted using dropdown menus and buttons in the toolbar. A cell or multiple cells must be selected for these tools to be used.

![Font options](https://devnet.logianalytics.com/hc/article_attachments/5432414971927/font.png)

For application versions *pre-v2019.2*:

![Font options](https://devnet.logianalytics.com/hc/article_attachments/5432322869015/screen.fontoptions.png)

### Font

* To change the font, use the dropdown menu. The font names appear in the style that they represent.
* Text size can be controlled using the up and down arrows on font size spinner.
* The **Bold**![B](https://devnet.logianalytics.com/hc/article_attachments/5432248067735/stylebold.png), **Italics**![I](https://devnet.logianalytics.com/hc/article_attachments/5432269691415/styleitalic.png) and **Underline**![U](https://devnet.logianalytics.com/hc/article_attachments/5432248102167/styleunderline.png) icons make the selected font bold, italicized, and underlined, respectively. Clicking the icon will turn it slightly gray to indicate the function is turned on.

### Color

* To change the text color, click the **Foreground Color**![A](https://devnet.logianalytics.com/hc/article_attachments/5432322874391/foregroundcolor.png) icon to show the foreground color selector. Select a color or enter an RGB value. Hexadecimal HTML color codes may be added in the **Hex** text box, or decimal values may be entered into each of the **R**, **G** and **B** textboxes ranging from 0–255. Click the **Reset**![struck droplet](https://devnet.logianalytics.com/hc/article_attachments/5432399705623/firefox_iwg1qcfbat.png) button to revert to the default color. A preview of the active foreground color appears below the **Foreground Color** icon.
* To change the cell background color, click the **Background Color**![paint can](https://devnet.logianalytics.com/hc/article_attachments/5432322889879/backgroundcolor.png) icon to show the background color selector. Select a color or enter an RGB value. Hexadecimal HTML color codes may be added in the **Hex** text box, or decimal values may be entered into each of the **R**, **G** and **B** textboxes ranging from 0–255. Click the **Reset**![struck droplet](https://devnet.logianalytics.com/hc/article_attachments/5432399705623/firefox_iwg1qcfbat.png) button to revert to the default color. A preview of the active background color appears below the **Background Color** icon.

For application versions *pre-v2019.2*:

* To change the text color, click the **Foreground Color** ![ForegroundColor.png](https://devnet.logianalytics.com/hc/article_attachments/5432322874391/foregroundcolor.png) icon to show the foreground color selector. Select a color or enter a hexadecimal RGB value. Click the **Clear**![ClearBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432181372823/clearbtn.png) icon to revert to the default color. A preview of the active foreground color appears below the **Foreground Color** icon.
* To change the cell background color, click the **Background Color** ![BackgroundColor.png](https://devnet.logianalytics.com/hc/article_attachments/5432322889879/backgroundcolor.png) icon to show the background color selector. Select a color or enter a hexadecimal RGB value. Click the **Clear** ![ClearBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432181372823/clearbtn.png) icon to revert to the default color. A preview of the active background color appears below the **Background Color** icon.

![colorpickert.png](https://devnet.logianalytics.com/hc/article_attachments/5432383741463/colorpickert.png)

Color picker

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The colors on the bottom row of the new color picker can be set via extensibility by a system administrator on a system-wide basis or they may be available for user preference.

For application versions *pre-v2019.2*:

![screen.fontcolorpicker.png](https://devnet.logianalytics.com/hc/article_attachments/5432399770903/screen.fontcolorpicker.png)

Color picker

### Alignment

* Text can be aligned to the left, center, right or justified in the cell using the respective horizontal alignment icons. First, click the **Horizontal Alignment Selector**![left align](https://devnet.logianalytics.com/hc/article_attachments/5432264137495/alignleft.png)![v](https://devnet.logianalytics.com/hc/article_attachments/5432330506263/accordionitemclosedarrow.png)  icon, and then choose from **Left**![left align](https://devnet.logianalytics.com/hc/article_attachments/5432264137495/alignleft.png), **Right**![right align](https://devnet.logianalytics.com/hc/article_attachments/5432248342935/alignright.png), **Center**![align center](https://devnet.logianalytics.com/hc/article_attachments/5432248296855/aligncenter.png) or **Justified**![align justified](https://devnet.logianalytics.com/hc/article_attachments/5432219770519/alignjustify.png) alignment. The horizontal alignment selector icon will change to show the currently selected alignment mode.
* Text can be aligned to the top, center, or bottom in the cell using the respective vertical alignment icons. First, click the **Vertical Alignment Selector**![middle align](https://devnet.logianalytics.com/hc/article_attachments/5432219677463/alignmiddle.png)![v](https://devnet.logianalytics.com/hc/article_attachments/5432330506263/accordionitemclosedarrow.png) icon, and then choose from **Top**![align top](https://devnet.logianalytics.com/hc/article_attachments/5432243806487/aligntop.png), **Middle**![align middle](https://devnet.logianalytics.com/hc/article_attachments/5432219677463/alignmiddle.png) or **Bottom**![align bottom](https://devnet.logianalytics.com/hc/article_attachments/5432219698711/alignbottom.png) alignment. The vertical alignment selector icon will change to show the currently selected alignment mode.
* Clicking on the **Wrap Text**![wrap text](https://devnet.logianalytics.com/hc/article_attachments/5432244099607/wraptext.png) icon will cause text longer than the width of a cell to wrap to new lines instead of being cut off by the cell’s boundary.

For application versions *pre-v2019.2*:

* Text can be aligned to the left, center, right or justified in the cell using the respective horizontal alignment icons.  
  ![Horizontal alignment icons](https://devnet.logianalytics.com/hc/article_attachments/5432415098903/screen.fontcentering.png)
* Text can be aligned to the top, center, or bottom in the cell using the respective vertical alignment icons.  
  ![Vertical alignment icons](https://devnet.logianalytics.com/hc/article_attachments/5432415128599/screen.alignment.png)
* The **Wrap Text**![](https://devnet.logianalytics.com/hc/article_attachments/5432244099607/wraptext.png) icon will cause text longer than the width of a cell to wrap to new lines instead of being cut off by the cell’s boundary.

## Formatting Cells

Cells can be formatted in the **Cell Format Window**. To open the window, first click on a cell and then click the **Format Cell** ![FormatCells.png](https://devnet.logianalytics.com/hc/article_attachments/5432243560855/formatcells.png)

**Number****Border****Conditional**

Comprehensive cell formatting information including how to use each of the three tabs can be found in our [Cell Formatting](https://devnet.logianalytics.com/hc/en-us/articles/5281564235671-Cell-Formatting) topic.

Cell formatting can be copied using the **Format Paintbrush** tool. Select the cell you want to copy, click the **Format Paintbrush**![paintbrush](https://devnet.logianalytics.com/hc/article_attachments/5432248054935/formatpaintbrush.png)

## Merge/Split Cells

Multiple cells can be merged together by first selecting the cells and then clicking the **Merge Cells**![MergeCells.png](https://devnet.logianalytics.com/hc/article_attachments/5432269867671/mergecells.png) icon. This is helpful when adding a chart to a report or when creating a heading, for example.

Conversely, merged cells may be split back up by selecting the cell to be split and the clicking the **Split Cells ![SplitCells.png](https://devnet.logianalytics.com/hc/article_attachments/5432264122519/splitcells.png)** icon. Only cells which have been merged can be split.

## AutoSum

To quickly get a total on a **Data Field**, place the field in a Report or Group Footer and click the **AutoSum** ![Sum.png](https://devnet.logianalytics.com/hc/article_attachments/5432230783511/sum.png) icon. Alternatively, a sum can be created with the *aggSum* or *Sum*functions. See Formulas for more information.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Do not use **AutoSum** on a cell with an aggregate formula such as *aggSum*.

## Images

An image file can be added to a cell using the **Insert Image** ![InsertPicture.png](https://devnet.logianalytics.com/hc/article_attachments/5432244444695/insertpicture.png) icon.

## Functions

Complex calculations can be done using **Formulas**. A formula can be added to a cell by keying it in manually or using the **Formula Editor**. To open the **Formula Editor** click the **Formula Editor** ![FormulaLarge.png](https://devnet.logianalytics.com/hc/article_attachments/5432236378775/formulalarge.png) icon.

Detailed information about formulas and how to use them can be found in the Formulas Section of the product documentation.

## Chart Wizard

A chart visualization may be added to the report by first clicking on a cell and then clicking on the **Chart Wizard** ![Chart.png](https://devnet.logianalytics.com/hc/article_attachments/5432233083031/chart.png)icon to launch the chart wizard. Full details about chart types and how to use the chart wizard can be found in the topic on [Charts and the Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281542473367-Charts-and-the-Chart-Wizard).

## Gauge Wizard

A gauge visualization may be added to the report by clicking on a cell and then clicking on the **Gauge Wizard** ![Gauge.png](https://devnet.logianalytics.com/hc/article_attachments/5432233271959/gauge.png) icon to launch the gauge wizard. Full details about gauges and how to use the gauge wizard can be found in the topic on [Gauges](https://devnet.logianalytics.com/hc/en-us/articles/5281556730135-Gauges).

## Suppress Duplicates

You can suppress duplicate values of a Data Object from being displayed. Select the cell and click the **Suppress Duplicates**![SuppressDuplicates.png](https://devnet.logianalytics.com/hc/article_attachments/5432219799575/suppressduplicates.png) icon.

For example, the two reports below are identical, except the second image has suppressed duplicates for the customer column.

![](https://devnet.logianalytics.com/hc/article_attachments/5432411623447/user75.png)

Duplicates are not suppressed

![](https://devnet.logianalytics.com/hc/article_attachments/5432322990487/user76.png)

Duplicates are suppressed

## CrossTab Wizard

A [Advanced Reports: CrossTabs](https://devnet.logianalytics.com/hc/en-us/articles/5281553083159-Advanced-Reports-CrossTabs) can be added to the report by clicking on the **CrossTab Wizard ![CrossTabWizard.png](https://devnet.logianalytics.com/hc/article_attachments/5432270123415/crosstabwizard.png)** icon.

## Linked Reports (aka Drilldowns)

A “subreport” can be linked to data on the current report by creating a link or *drilldown* to another report. Click on a cell and then click the **Link Reports ![LinkedReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432125018135/linkedreport.png)** icon to link a report to that cell. Review the [Linked Reports (Drilldowns)](https://devnet.logianalytics.com/hc/en-us/articles/5281533707031-Linked-Reports-Drilldowns-) topic for full details on how to create a report link (drilldown).

## Linked Action Event

**Action Events** are custom programs which can be activated by certain actions on a report. This is an advanced feature. Consult with the system administrator about which action events are available in the system. To add an **Action Event** to a cell, first click the cell and then click the **Linked Action Event** ![LinkedAction.png](https://devnet.logianalytics.com/hc/article_attachments/5432185689239/linkedaction.png) icon.

## GeoChart Wizard

**GeoCharts** are a way to visualize geographic report data. To insert a GeoChart into a cell, first select the cell and the click on the **GeoChart Wizard ![Map.png](https://devnet.logianalytics.com/hc/article_attachments/5432233146519/map.png)**icon.

**GeoCharts** are a legacy feature, and have been replaced with the **Google Maps** feature. More information about the **GeoCharts** feature can be found in the [GeoCharts](https://devnet.logianalytics.com/hc/en-us/articles/5281573529495-GeoCharts) topic.

## Google Maps Wizard

**Google Maps** are a way to insert interactive maps in a report to visualize geographic report data. To insert a Google Maps visualization into a cell, first select the cell and then click on the **Google Maps Wizard**![Google Maps](https://devnet.logianalytics.com/hc/article_attachments/5432124975895/googlemaps.png) icon.

More information about using this feature can be found in the [Google Maps](https://devnet.logianalytics.com/hc/en-us/articles/5281573605655-Google-Maps) topic.

## Run Report

![gqyKFERY6Y.png](https://devnet.logianalytics.com/hc/article_attachments/5432415178647/gqykfery6y.png)

Run Report button

Selecting the**Run** button executes the report and displays the result in the **Report Viewer**. Depending on system configuration, selecting Run may also save the report first.

## Execution Caching

If **Execution Caching** is enabled for a report, the **Cache Status** icons will appear in the toolbar next to the **Run Report** and **Export** buttons. A report can only be run when the cache is valid.

* ![CacheInvalid.png](https://devnet.logianalytics.com/hc/article_attachments/5432124221719/cacheinvalid.png)**Cache Invalid**: the cache is invalid or out of date. Select this icon to update the cache.
* ![CacheValid.png](https://devnet.logianalytics.com/hc/article_attachments/5432415189399/cachevalid.png)**Cache Valid**: the cache is valid.

## Export

![k7PRN1fok0.png](https://devnet.logianalytics.com/hc/article_attachments/5432399950103/k7prn1fok0.png)

Export PDF button

![firefox_wYPbd9nxnF.png](https://devnet.logianalytics.com/hc/article_attachments/5432415234199/firefox_wypbd9nxnf.png)

Export file types button

To export the report as a downloadable file, select the **Export PDF** button. You can also select the **More**![AccordionItemClosedArrow.png](https://devnet.logianalytics.com/hc/article_attachments/5432330506263/accordionitemclosedarrow.png) icon to choose from the additional exportable file types.

The system administrator can make only certain file types available, so the menu may look differently depending on how the installation is configured.

## Formula Bar

![yBfXbiQRcQ.png](https://devnet.logianalytics.com/hc/article_attachments/5432366976919/ybfxbiqrcq.png)

A formula may be added to cells by directly entering them into this formula bar. Click the **Formula Editor** ![FormulaLarge.png](https://devnet.logianalytics.com/hc/article_attachments/5432236378775/formulalarge.png) icon in the bar to open the Formula Editor for assistance building the formula.

Just as when entering formulas directly into cell content, formulas should be prefixed with an equals sign.

### Examples

```
={Orders.OrderDate}
```

```
=AggCount({Products.ProductName})
```

```
=[A5]
```

### Additional Resources

For more information about formulas, review these topics:

* [What are formulas?](https://devnet.logianalytics.com/hc/en-us/articles/5281600700183-What-are-formulas-)
* [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/5281623158039-Formula-Editor)
