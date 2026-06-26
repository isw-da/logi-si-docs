---
title: "Globalization Element"
id: 4419723149719
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723149719-Globalization-Element
updated_at: 2022-07-17T01:38:22Z
---

# Globalization Element

# Globalization Element

The **Globalization** element allows you to set application-wide characteristics related to [Internationalization and Localization](https://devnet.logianalytics.com/hc/en-us/articles/4419707658647-Internationalization-and-Localization-), and culture. Its attributes include:

| Attribute | Description |
| --- | --- |
| Default Input Date Format | Specifies a date format that will be used when an **Input Date** element doesn't have its own Format attribute set. For more information, see [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722930327-Format-Data). |
| Default Input Date Reformat | Specifies a date format that will be used when an **Input Date** element doesn't have its own Input Date Reformat attribute set. For more information, see [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722930327-Format-Data).  When this attribute is specified, Input Date element values are reformatted when they're referenced as @Request tokens and the format of @Date tokens are also changed. For more information, see [Token Reference](https://devnet.logianalytics.com/hc/en-us/articles/4419715492631-Token-Reference). |
| Default Input Time Format | Specifies a time format that will be used when an **Input Time** element doesn't have its own Format attribute set. For more information, see [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722930327-Format-Data). |
| Default Input Time Reformat | Specifies a time format that will be used when an **Input Time** element doesn't have its own Input Time Reformat attribute set. For more information, see [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722930327-Format-Data). |
| First Day Of Fiscal Year | Specifies the first day of the fiscal year, which is used when calculating dates and quarters for fiscal calendars. The value must be in the format MM/DD. For example, if the fiscal year begins on March 5, enter *03/05*. The default value is *01/01*. |
| First Day Of Week | Specifies how the first day of the week is determined for @Date tokens that return first and last days of the week, such as @Date.ThisWeekStart~ and @Date.ThisWeekEnd~.  This attribute value is a number representing the days of the week, where: *0* = Sunday, *1* = Monday, *2* = Tuesday, *3* = Wednesday, *4* = Thursday, *5* = Friday, *6* = Saturday |
| Input Reformat Culture | This attribute has been deprecated. |
| Java Font Folder | For Java applications only: Specifies the fully-qualified path and folder name where TrueType fonts are located for PDF exports. The folder is required for PDF exports with fonts that contain characters that are not in the ISO 8859\_1 character set, such as Arabic, Cyrillic, and Korean language characters. Depending on your Java environment, you may even need to point the Logi application to the location of your regular fonts in order to ensure that they'll be used.  A typical value for a Windows installation will be something like C:\Windows\Fonts. For Linux, it could be something like /usr/local/share/fonts/ttfonts. |
| Metric Prefix String | Specifies comma-separated list of custom formatting characters for use with Metric Prefix formatting. Setting Format attributes to "mp" formats numbers with a "metric prefix". For example, to format the value 1,234,567 as $1.23M, the Format attribute value is $#.00mp.  Supported metric prefixes are in the range of 1000^-6 to 1000^6 and the default string of formatting characters is a,f,p,n,,m,k,M,G,T,P,E. You can replace this string with your own comma-separated string of characters to represent this range. |
| User Culture | Specifies a custom value that overrides the "culture" value obtained from the user's browser at runtime. Tokens, such as @Session or @Request, may be used here.  Culture values are specified as a string, such as *en-US*. For a list of cultures, see your browser's options. For example, in Internet Explorer, select ToolsInternet Options LanguagesAdd. |
