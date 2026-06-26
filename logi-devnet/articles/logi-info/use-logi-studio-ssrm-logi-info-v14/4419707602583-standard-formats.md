---
title: "Standard Formats"
id: 4419707602583
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707602583-Standard-Formats
updated_at: 2022-07-17T02:24:22Z
---

# Standard Formats

# Standard Formats

The following standard formats are available, from a pull-down list, in Studio for elements' Format attribute value:

| Type | Description |
| --- | --- |
| < | Converts all characters to lower-case. |
| > | Converts all characters to upper-case. |
| Expanded Spaces | Preserves space characters that are normally collapsed by the web browser. *This formatting will not be applied if used with content that includes more than one @Data token.* |
| Preserve Line Feeds | Preserves line breaks (CTRL-ENTER). *This formatting will not be applied if used with content that includes more than one @Data token.* |
| HTML | Preserves HTML tags, embedding them rather than encoding them. Text appearance and alignment is affected by the tags; they are not seen in the text. |
| General Date | Display a date and/or time. For real numbers, display a date and time, for example, 4/3/93 05:34 PM. If there is no fractional part, display only a date, for example, 4/3/93. If there is no integer part, display time only, for example, 05:34 PM. Date display is determined by the web server's settings. |
| Long Date | Display a date according to the web server's Long Date format. |
| Medium Date | Display a date using the Medium Date format appropriate for the language version of the host application on the web server. |
| Short Date | Display a date using web servers's Short Date format. |
| Long Time | Display time using the web server's Long Time format; includes hours, minutes, seconds. |
| Medium Time | Display time in 12-hour format using hours and minutes and the AM/PM designator. |
| Short Time | Display time using the 24-hour format, for example, 17:45. |
| yyyy/MM/dd | A custom date/time format defined by the developer using the components described in [Custom Date and Time Format](https://devnet.logianalytics.com/hc/en-us/articles/4419707600535-Custom-Date-and-Time-Format). |
| hh:mm | Display time as hours and minutes, with leading zeroes. Example: 01:08 |
| yyyy/MM/dd hh:mm:ss | Display date and time, with leading zeroes. Example: 2007/01/01 01:08:02 |
| General Number | Display number with no thousands separator. |
| Currency | Display number with currency symbol, thousands separators (if appropriate), and two digits to the right of the decimal separator. The symbols and characters used are based on the end-user's browser culture settings or computer system settings. For example, United States = "en-us" = $1,000.00, United Kingdom = "en-gb" = 1.000,00. |
| Fixed | Display at least one digit to the left and two digits to the right of the decimal separator. |
| Standard | Display number with thousands separator, at least one digit to the left and two digits to the right of the decimal separator. |
| Percent | Display number multiplied by 100 with a percent sign (**%**) appended to the right; always display two digits to the right of the decimal separator. |
| Scientific | Use standard scientific notation. |
| Timespan | Displays decimal numbers as a time span, formatted as d:hh:mm:ss. |
| mp | Formats numbers by applying the appropriate "metric prefixes" (giga-, mega-, kilo-, etc.). Example: "1,234,567" formatted with "$#.00mp" produces "$1.23M". More information about metric prefixes can be found [here](http://en.wikipedia.org/wiki/Metric_prefix). Customization of the mp format can be accomplished using the Globalization element's Metric Prefix String attribute. For more information, see [Using the Globalization Element](https://devnet.logianalytics.com/hc/en-us/articles/4419722994199-Using-the-Globalization-Element-). |
| mps3 | Identical to the mp format, but allows rounding to three significant digits. Example: A value of 123456, with format mps3, returns 123K. |
| ###,###,##0.00 | Display number with thousands separator for every three digits to left, at least one digit to the left and two digits to the right of the decimal separator. |
| Yes/No | Display **No** if number is 0; otherwise, display **Yes**. |
| True/False | Display **False** if number is 0; otherwise, display **True**. |
| On/Off | Display **Off** if number is 0; otherwise, display **On**. |

The **HTML** format, when used with a Label caption, allows you to embed HTML code in the report. This be used to accomplish things as simple as making part of a line bold-faced using <B> tags, or as complicated as including scripts within <SCRIPT> tags for various purposes. When using the HTML format, ensure that you do not include a <BODY> tag that might confuse the Logi Server Engine when it generates its HTML output.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png)

* The standard numeric formats, such as Currency, may cause *rounding*, and this may affect aggregations and summaries of the data.
* Use the standard date/time and numeric formats to improve performance with large reports.
