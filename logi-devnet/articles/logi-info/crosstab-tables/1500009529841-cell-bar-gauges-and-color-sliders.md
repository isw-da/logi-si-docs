---
title: "Cell Bar Gauges and Color Sliders"
id: 1500009529841
section: "Crosstab Tables"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009529841-Cell-Bar-Gauges-and-Color-Sliders
updated_at: 2021-06-17T01:58:05Z
---

# Cell Bar Gauges and Color Sliders

# Cell Bar Gauges and Color Sliders

This topic introduces developers to the **Cell Bar****Gauge** and the **Cell Color Slider** elements. As child elements of the Data Table Column, both provide new methods of depicting data values using color.

* Cell Bar Gauge
* [Cell Color Slider](#ColorSlider)

## Cell Bar Gauge

The Cell Bar Gauge element creates an **in-cell, horizontal bar gauge** which allows easy visual comparison of relative values in a single column. It looks like this:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778722839/cellbar_01.png)

The example above shows part of a table with three data columns using the Cell Bar Gauge element. The first column, Sequence, is configured to display a plain horizontal bar who's length is based on the column's data value. The second column, Unit Price, is configured similarly but adds a background color for greater visual contrast. And the last column is configured to display both the bar and a label with the actual data value.

Here are the report definition elements for the first part of the above example:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771894295/cellbar_02.png)

As shown above, the Cell Bar Gauge element is the child of a **Data Table Column** element, which is in turn the child of the **Data Table** element. The column with the Cell Bar Gauge can also use a Label element to display the actual data value along with the Cell Bar Gauge, or not, as desired.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  Note that you *cannot* use the Cell Bar Gauge element in a SubData Table.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771894551/cellbar_03.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771894807/cellbar_03a.png)

When a Data Table Column is selected, the Cell Bar Gauge child element can be found in the **Charts and Gauges** folder in the Suggestions panel, as shown above.

## Set Cell Bar Attributes

The attributes associated with the Cell Bar Gauge element in our example are shown below:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771894551/cellbar_03.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778723095/cellbar_03b.png)

* (Required) The **Data Column** attribute has been set to the *name* of the *data column* retrieved in your Data Layer element (the actual column name, not the @Data.ColumnName~ token).
* The **Alternate Text** attribute is the text to be displayed if the bar gauge can't be rendered for some reason.
* The **Background Color** attribute sets a color for the background of the bar Here it's been set to *LightBlue*.
* The **Color** attribute sets the color for the part of the bar representing the data. The default color is *Blue*.
* **Height** and **Width** determine the physical size of the bar - note that it can be smaller than the cell itself; allowing you to put both a Cell Bar Gauge and a Label in a column.
* **ID** and **Tooltip** are the usual identifier and "hover text" attributes.

## What About the Data?

You don't need to do anything other than identify the data column. The Cell Bar Gauge element automatically evaluates all of the values for its column and adjusts the graphics segments that make up the bar accordingly, sizing them to provide a meaningful visual range of bar lengths.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778723351/cellbar_04.png)

A example of a data table using Cell Bar Gauges is shown above.

The arrangement in the Units In Stock column was achieved by using both Cell Bar Gauge and Label elements, separated by a Space element, beneath the Data Table Column element. Set the gauge's Background Color attribute (to white, in the example) to get the data values to align on the right side of the column.

If you include and configure a Sort element in your Data Table Column, the Cell Bar Gauge will sort when the column header is clicked, just like any data value.

## Cell Bars Can Be Links

Cell Bar Gauge elements, like Labels, can be **links** to other reports or URLs.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771895319/cellbar_05.png)

As shown above, the Cell Bar Gauge element can be a parent to any of the Action elements.

## Cell Color Slider

The **Cell Color Slider** element is similar to the Cell Bar Gauge element in that it generates a graphic depiction of the data within its data table column.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778723607/cellbar_06.png)

As shown above, the Cell Color Slider element shows a column's numeric values with a colored indicator or background. The color for a particular column varies depending on where its value fits into the overall population of values for that column in the table. Low values are one color, middle values a second, and high values, a third color; everything in between is given shades of those colors. The Cell Color Slider element makes it easy to visualize how values in a column relate to each other.

At runtime, the user can manipulate an optional slider control at the top of the column to adjust the "middle value" color and the color indicator can be a square, a circle or the entire cell background.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) Cell Color Slider elements should *not* be used in reports that will be **exported**, for example, to PDF or Excel formats.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771895575/cellbar_07.png)

The report definition elements for the first part of the earlier example are shown above. The Cell Color Slider element is the child of a Data Table Column element, which is in turn the child of the Data Table element.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  Note that you *cannot* use the Cell Color Slider element in a SubData Table.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771895831/cellbar_08.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771896215/cellbar_08a.png)

When a Data Table Column is selected, the Cell Color Slider child element can be found in the **Charts and Gauges** folder in the Suggestions panel, as shown above.

## Cell Color Slider Attributes

The attributes associated with the Cell Color Slider element in our example are shown below:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771895831/cellbar_08.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771896471/cellbar_08b.png)

* The **Data Column** attribute has been set to the *name* of the *data column* retrieved in your Data Layer element (the actual column name, not the @Data.ColumnName~ token).
* The **Color Indicator** allows you to choose between Square, Circle, or Background indicators. Default: *Background*
* The **Foreground Black and White** attribute, when set to *True*, automatically sets the foreground color of text in each cell depending on the background color. If the background color is dark, the foreground font is set to white; if the background is light, the font becomes black.
* The **High Value Color** attribute sets the "high" end of the color scale; representing the highest data values. Default: *Green*
* The Middle and Low Value Color attributes set the "middle" and "low end" of the color scale; representing the median and low data values. Defaults: *Yellow* and *Red*
* The **Show Slider** attribute determines whether a slider appears below the column header caption; when visible, the slider can be moved by users at runtime to fine tune the Middle value color.
* **Height** and **Width** determine the physical size of the bar - note that it can be smaller than the cell itself; allowing you to put both a Cell Color Slider and a label in a column.
* **ID** and **Slider Tooltip** are the usual identifier and "hover text" attributes.

## What About the Data?

You don't need to do anything other than identify the Data Column. The Cell Color Slider element automatically evaluates all of the values for its column and adjusts the colors accordingly.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771896727/cellbar_09.png)

A example of a data table using Cell Color Slider is shown above.

The arrangement in the Units In Stock column was achieved by using both a Cell Color Slider and a Label element, and setting the Data Table Column element's **Class** attribute to *ThemeAlignCenter*.

If you include and configure a Sort element in your Data Table Column, the Cell Color Slider will sort when the column header is clicked, just like any data value.

## Cell Color Sliders Can Be Links

Cell Color Slider elements, like Labels, can be **links** to other reports or URLs.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771896983/cellbar_10.png)

As shown above, the Cell Color Slider element can be a parent to any of the Action elements.
