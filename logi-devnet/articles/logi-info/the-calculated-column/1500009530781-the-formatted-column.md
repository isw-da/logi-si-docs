---
title: "The Formatted Column"
id: 1500009530781
section: "The Calculated Column"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530781-The-Formatted-Column
updated_at: 2021-06-17T01:58:21Z
---

# The Formatted Column

# The Formatted Column

The **Formatted Column** element is used with datalayer elements to create a **new column** in the datalayer with formatted data in it. This is an alternative to formatting the data in other elements, such as a Label, and provides a significant performance improvement. This topic discusses use of this element.

* About the Formatted Column Element
* [Usage Examples](#Usage)

## About the Formatted Column Element

The Formatted Column is similar to other elements designed to **extend** the **data** available in a datalayer. Like the **Calculated Column** element, the Formatted Column is added as a child element beneath a datalayer and adds a **new column** to the datalayer. This new column contains **formatted data** which is accessible using an @Data token.

Formatting data in the datalayer is particularly useful when working with charts, particularly **Animated Charts**, whose data attributes may not allow application of scripting functions or formats. In addition, **tooltips** can also benefit from being able to use formatted data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778641303/attnicon_87x15.gif)  Note that data in a Formatted Column may not be of the same data *type* as the column from which it is derived. For example, when a numeric column, with a value of 1234, is used to create a Formatted Column that applies the *Currency* format, the result will be string-type data: "$1,234.00". Thus, in this case, the Formatted Column is useful for chart axis labels, but may not work for chart
data, which requires the original numeric value.

The pre-configured format options available in the Formatted Column element are identical to the **Format** attribute value options in elements such as the Label. In addition, custom formatting can be entered manually.

For more information about formatting options and custom formats, see [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009515122-Format-Data).

### Dynamic Formatting

Beginning in v10.0.319, the Formatted Column element has an **Include Condition** attribute:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778641559/formattedcol_09.gif)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if a new column of formatted data will be added to the datalayer or not.

## Usage Examples

1. A common formatting requirement is to apply the **Currency** format to monetary data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778641815/formattedcol_01.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771785879/formattedcol_01a.gif)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771786135/formattedcol_02.gif)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778642071/formattedcol_03.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778642327/formattedcol_03a.gif)

**Formatted Column** element beneath the datalayer, set its attributes as shown, and provide another data table column to display the column added to the datalayer,

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778642583/formattedcol_04.gif)

the output will change as shown above. In this case, the new column added to the datalayer contains the **Freight** column values, formatted as Currency.

**ISO****format** used to store datetime values in many databases isn't very presentable.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778642839/formattedcol_05.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771786391/formattedcol_05a.gif)

**standard** date formats ("Short Date"),

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771786647/formattedcol_06.gif)

and the resulting output is shown above.

**month name abbreviation** of a date value.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778643095/formattedcol_07.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778643351/formattedcol_07a.gif)

The example above shows how a custom format can be used; in this case the custom format value "MMM" will produce a 3-letter month abbreviation,

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778643607/formattedcol_08.gif)

and the resulting output is shown above. Incidentally, a format value of "MM" will produce the **month****number** and "M" will produce the **month name and day** ("July 15"). All of these must be in uppercase.

As mentioned earlier, formatting data in the datalayer is much more efficient that formatting it elsewhere, so using Formatted Column elements can speed up report performance.
