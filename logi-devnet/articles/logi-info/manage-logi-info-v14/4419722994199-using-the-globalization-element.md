---
title: "Using the Globalization Element "
id: 4419722994199
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722994199-Using-the-Globalization-Element
updated_at: 2022-07-17T01:45:34Z
---

# Using the Globalization Element 

# Using the Globalization Element

The \_Settings definition in a Logi application provides application-wide configuration of various settings, such as connections, team development, etc. The **Globalization** element, which provides valuable assistance when developing a multi-cultural application, is also available for use the \_Settings definition. The following table describes its attributes:

| Attribute | Description |
| --- | --- |
| Default Input Date Format | Specifies the default input date format used when an Input Date element does not have its own Format attribute set. |
| Default Input Date Reformat | Sets a default value for all Input Date Reformat attributes. These are available with Input Date elements, which allow the user to enter dates. |
| Default Input Time Format | The default input time format used when an Input Time element does not have its own Format attribute set. |
| Default Input Time Reformat | Sets a default value for all Input Time Reformat attributes. These are available with Input Time elements, which allow the user to enter times. |
| First Day of Fiscal Year | Specifies the first day of the Fiscal Year and is used when calculating dates and quarters for fiscal calendars. The value must be in the format of mm/dd. For example if your fiscal year begins on March 5, enter 03/05. The default value is *01/01*. This value affects the Fiscal Year and Fiscal Quarter formats. See [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722930327-Format-Data). |
| First Day of Week | Changes the order of days in the week in popup calendars used with date inputs and data calendars. Also changes how the first day of the week is determined for the @Date tokens that return first and last days of the week, such as @Date.ThisWeekStart~ and @Date.ThisWeekEnd~. Valid values are: 0 = Sunday (default), 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday This value affects the Fiscal Week format. See [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722930327-Format-Data). |
| Input Reformat Culture | *This attribute is deprecated - do not use it.* A culture value that can be used to reformat input dates and values. You can set this to a different culture so that values from Input elements are returned in that culture. This can be useful when the database expects date and numeric values that are not in the invariant format. In most cases it is best to set up the database or database client account to use an "English" culture. This attribute is not used for dates when Input Date Reformat is used. The culture is specified as a string, such asen-us. To see a list of cultures, open IE, select Tools, Internet Options, Languages, then Add. The default culture is the "invariant" culture, which is basically US-English. |
| Java Font Folder | *Active only for Java applications*. Identifies the folder where TrueType fonts are located for PDF exports. The folder is required for PDF exports with fonts that contain characters that are not in the ISO-8859\_1 character set. In Windows this is usually something like C:\Windows\Fonts. In Linux, this would be something like/usr/local/share/fonts/ttfonts. |
| Metric Prefix String | Specifies user-defined values to be used when the Metric Prefix ("mp") is selected in **Format** attributes. The range of numbers formatted by metric prefixes isfrom 1000^6 to 1000^-6, so one of 12 characters is applied to each power of 10. The default string of characters is:  representing atto, femto, pico, nano, micro, milli, kilo, mega, giga, tera, peta, and exa. You can replace this string with a comma-separated string of your own 12 characters. More information about Metric Prefixes is [available here](http://en.wikipedia.org/wiki/Metric_prefix). |
| User Culture | Normally, the user's culture is obtained from the browser's settings. If a value is supplied here, the User Culture attribute overrides the browser's culture setting with another value. User Culture can be set with a token value, such as @Session or @Request. The culture is specified as a string, such as en-us. A list of available cultures can be viewed in the browser, where Language is specified. |
