---
title: "Data Calendar Attributes"
id: 4406817602967
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817602967-Data-Calendar-Attributes
updated_at: 2022-04-06T06:07:08Z
---

# Data Calendar Attributes

# Data Calendar Attributes

The Data Calendar element has the following attributes:

| Attribute | Description |
| --- | --- |
| Data Column | (Required) Specifies the name of a column in the datalayer that contains *date-type* information. The dates in this column will each correspond to a single day in the calendar. This data should be in YYYY-MM-DD format. (As long as the data source thinks the data is date-type date, it will be retrieved into the datalayer in this format. Otherwise, a Calculated Column element should be used to reformat the data into the required format.) |
| ID | (Required) Specifies a unique element ID. |
| Border | Specifies the thickness of the border, in pixels, around the calendar and between each day on the calendar. Default (and minimum) value: *1* |
| Calendar Caption Format | By default, a caption will appear centered above the calendar consisting of a date range (weekly calendar) or the month and year (monthly calendar). This attribute specifies a format for that caption, using system formats such as *Short Date* (weekly) or these combinations (monthly): *None* - the caption is suppressed *yy* - two-digit year *yyyy* - four-digit year *MM* - month number  *MMM* -three-letter month abbreviation (Jan, Feb, Mar, etc.) *MMMM* - full month name *Note: Only date-related formats should be selected here; use of other formats results in the format option itself appearing in the calendar caption.* Default: *Short Date* (weekly calendar); *yyyy MMMM* (monthly calendar) |
| Cell Spacing | Specifies the space, in pixels, between cells (boxes) in the calendar.  Default: *0* |
| Class | Specifies the CSS class(es) to be used by the element. Generally not used if a Theme is being used. |
| Data Calendar Date | Specifies a date value that sets the current date for the calendar. The calendar will display the week or month, based on the Time Period attribute, containing the current date. |
| Day Caption Format | Controls the appearance of the day number in each box of the calendar. Set to "None" to suppress the numbering. Default: *%d*  which provides the day number. |
| Layout | Determines whether the columns of days within the calendar size their widths automatically based on the widest data they contain or are set to a fixed width (based on required width of first row). Default: *Auto* |
| Security Right ID | When using Logi Security, specifies one or more Security Right IDs, separated by commas. Users with these Security Right IDs will be able to view the Analysis Grid, users without them will not. |
| Time Period | Specifies whether the calendar rendered will display a week or a month of days. Default: *Month* |
| Weekday Caption Format | This attribute is used to format the Monday, Tuesday, Wednesday, etc. headings that appear at the top of the calendar above each columns of days. These formats are available: *ddd* - three-letter day abbreviation (Mon, Tues, Weds, etc.) *dddd* - full day name *None* - the caption is suppressed Default - *dddd* |
| Weekday Filter | Specifies which days of the week will appear in the calendar; useful for suppressing display of weekend days. Enter values 0-6, separated by commas. Typically, a value of 1,2,3,4,5 will produce a calendar without Sunday (0) or Saturday (6) in it. The relationship of numbers 0-6 to days of the week can be set differently when using the Globalization element in your \_settings definition by configuring its FirstDayOfWeek attribute. Default: *0,1,2,3,4,5,6* - showing all days of the week |
| Width Width Scale | Specifies the width of the Analysis Grid, in units set in the Width Scale attribute (either *px* for pixels or *%* for percent). |
