---
title: "Color Range Column Usage Example: Text Data"
id: 4406817178263
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817178263-Color-Range-Column-Usage-Example-Text-Data
updated_at: 2022-04-06T06:04:28Z
---

# Color Range Column Usage Example: Text Data

# Color Range Column Usage Example: Text Data

Here's an example of the Color Range Column element in use with text data.

The technique used here adds two new columns to the data layer, evaluates data strings and correlates them to a background color value and contrasting text color value, and inserts those color values into the new columns. We then use the @Data tokens for those columns to set the color of the data table cells.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563459351/colorrangecol_05.png)

In the example shown above, we start with a Data Table element with child DataLayer.SQL element and then add a Color Range Column element. Its attributes are configured as follows:

* **Data Column** - The data to be evaluated will be in the *ShipCountry* column.
* **ID** - The new column added to the datalayer containing background color data will be named *CountryColor*.
* **Color Range Style** - The data being evaluated consists of specific text strings, so this is set to *TextList*.
* **Contrast Color Column ID** - The new column added to the datalayer containing contrasting text color data will be named *CountryTextColor*.

You can use multiple Color Range Column elements beneath a datalayer. Next, we add and configure three Color Range elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584092439/colorrangecol_06.png)

Color Range elements are evaluated according to their top-to-bottom order in the Element Tree, so the element order matters. Notice the use of the asterisk wildcard (\*) in the bottom Range End Value attribute. *Values that do not match USA, Brazil, or F\* will have no background color.*
If you do wish to set a background color for all *other* text values, add a fourth Color Range element (at the "bottom" of the set of Color Range elements) and set its Range End Value to \*.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563459735/colorrangecol_07.png)

In order to display the colors, we configure our Data Table Column element, as shown above. The tokens for the data in the two new columns are used to provide values in the **Background Color** and **Text Color** attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575833623/colorrangecol_08.png)

When we run this example, as shown above, we see the ShipCountry column (which has been included just for reference) and the Country Color column. Notice how the contrasting text color changes depending on the background color.
