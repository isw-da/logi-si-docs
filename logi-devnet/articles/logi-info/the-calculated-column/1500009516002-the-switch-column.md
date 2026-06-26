---
title: "The Switch Column"
id: 1500009516002
section: "The Calculated Column"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009516002-The-Switch-Column
updated_at: 2021-06-17T01:58:39Z
---

# The Switch Column

# The Switch Column

The **Switch Column** element is used with datalayer elements to make data replacements. It's analogous to using both a CASE structure and a REPLACE function in a SQL query but, unlike a query, it's applied to the data *after* it's been retrieved into the datalayer. This topic discusses use of this element.

* About the Switch Column
* [Apply the Switch Column](#sec1)
* [Use Multiple and Dynamic Switch Columns](#sec2)

*This element is not available in Logi Report.*

## About the Switch Column

The **Switch Column** element, introduced in v10.1.18, is available for use with all datalayer elements and is particularly useful in conjunction with those lacking query capabilities, such as DataLayer.XML and DataLayer.Web Service.

In operation, the element basically searches a specified data column in each datalayer row for a specified value and, if found, *replaces**it* with another value. Optionally, the replacement value can be put into a new column that's added to the datalayer, leaving the original column's data intact.

This is useful for replacing storage-friendly codes, such "1,2,3..." with readable text, such as "Overnight Delivery, Second Day Delivery, Ground Delivery...". or "1, 0" into "True, False". These replacements are temporary (they happen only in the cached datalayer) and don't effect the original data in the datasource, so they're great for increasing legibility in reports.

## Apply the Switch Column

The following example  illustrates how the **Switch Column** is used:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778508951/switchcol_01b.png)

First, look at the example datalayer row above which shows the data as retrieved, with a numeric code for the **ShipVia** field.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778509207/switchcol_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771609623/switchcol_01a.png)

1. As shown above, a **Switch Column** element is added as a child beneath a datalayer element.
2. Its **Data Column** attribute value is set to the column in that datalayer whose value will be evaluated.
3. The **ID** attribute is set to name of a column that will receive the replacement data. If it's the *same* as the Data Column, as shown above, the original data will be replaced. If it's *different*, a new column by that name will be added to the datalayer.
4. The optional **Data Type** attribute helps the comparison routine when the data may be ambiguous.  
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771609879/switchcol_02.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778509463/switchcol_02a.png)
5. Next add one (or more) **Switch If** elements beneath the Switch Column element, as shown above. These specific the **Compare Value** (3) which, when found, will trigger a replacement using the **New Value** ("UPS"). The evaluation is always "if the original value *equals* the comparison value, substitute the new value". Note that you can leave the Compare Value *blank* in order to deliberately replace the original value in all rows.   
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771610263/switchcol_02b.png)  
     
   If we look at the data again, we'll see that the ShipVia field has been changed.  
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771610519/switchcol_03.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778509719/switchcol_03a.png)
6. Finally, if desired, you can add an optional **Switch Else** element as a child of Switch Column which will replace the original value with a **New Value**, shown above, in any row unaffected by the preceding Switch If elements.

In the complete example above, the sequence of events is that the datalayer reads in all the data from the XML data file, then the Switch Column examines the specified data column in each datalayer row and, depending on the original value found there, replaces the original value with the specified new value. Any rows that aren't affected by one of the Switch If elements has their original value changed by the Switch Else element.

## Use Multiple and Dynamic Switch Columns

1. Developers can use two or more **consecutive** Switch Column elements:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778509975/switchcol_04.png)

In this case, the operations will be conducted **sequentially**, based on their arrangement from top to bottom in the element tree. So, after the first Switch Column is applied, rows that may have been changed by it will be evaluated by the second Switch Column.

2. The Switch Column element also has an **Include Condition** attribute:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778509207/switchcol_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771610903/switchcol_05.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be altered or not.
