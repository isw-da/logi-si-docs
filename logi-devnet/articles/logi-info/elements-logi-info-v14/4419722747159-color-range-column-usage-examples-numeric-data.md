---
title: "Color Range Column Usage Examples: Numeric Data"
id: 4419722747159
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722747159-Color-Range-Column-Usage-Examples-Numeric-Data
updated_at: 2022-07-17T01:57:10Z
---

# Color Range Column Usage Examples: Numeric Data

# Color Range Column Usage Examples: Numeric Data

Here's an example of the Color Range Column element in use with numeric data.
The technique used here adds two new columns to the data layer, evaluates data ranges and correlates them to a background color value and contrasting text color value, and inserts those color values into the new columns. We then use the @Data tokens for those columns to set the color of the Data Table cells.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699595287/colorrangecol_01.png)

In the example shown above, we start with a Data Table element with child DataLayer.SQL element and then add a Color Range Column element. Its attributes are configured as follows:

* **Data Column** - The data to be evaluated will be in the *Freight* column.
* **ID** - The new column added to the datalayer containing background color data will be named *FreightColor*.
* **Contrast Color Column ID** - The new column added to the datalayer containing contrasting text color data will be named *FreightTextColor*.

You can use multiple Color Range Column elements beneath a datalayer. Next, we add and configure four Color Range elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706694167/colorrangecol_02.png)

Color Range elements are evaluated according to their top-to-bottom order in the Element Tree, so the element order matters. Notice how that the Range End Value increases with each successive element. Values up to 20 will have a background color of #D7FFD8, from 21 to 50 the background will be #4EFF54, and so on up to 100. *Values above 100 will have no background color.*

If you do wish to set a background color for all values greater than 100, add a fifth Color Range element (at the "bottom" of the set of Color Range elements) and leave its Range End Value blank.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699595543/colorrangecol_03.png)

In order to display the colors, we configure our Data Table Column element, as shown above. The tokens for the data in the two new columns are used to provide values in the **Background Color** and **Text Color** attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706694423/colorrangecol_04.png)

When we run this example, as shown above, we see the Freight column (which has been included just for reference) and the Freight Colors column. Notice how the contrasting text color changes depending on the background color.
