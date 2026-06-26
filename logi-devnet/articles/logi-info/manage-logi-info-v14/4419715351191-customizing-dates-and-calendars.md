---
title: "Customizing Dates and Calendars "
id: 4419715351191
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715351191-Customizing-Dates-and-Calendars
updated_at: 2022-07-17T01:45:45Z
---

# Customizing Dates and Calendars 

# Customizing Dates and Calendars

A number of individual elements allow the user to enter dates or interact with calendars, and developers may want to change the behavior of related elements based on culture settings. These include the Input Date, Date Picker, Data Calendar, and Time Period Column.
The format and presentation of calendars and dates varies widely depending on
country and/or language.
At the application level, date-related aspects of your Logi application can
be changed by adding and configuring a Globalization element in the
application's \_Settings definition.
For example, setting the Globalization element's **First Day of Week**attribute will change the display of calendars. If the attribute value is set to *1*, then *Monday* will be the
first day in the calendar; the default is *0* which is *Sunday*.
In addition, the browser's preferred language setting will affect the
display of the month and day-of-week names in both a Logi element calendar and
the selected value:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699784983/intlocal_04.png)

In the examples shown above, a Globalization element has been used to change
the first day of the week to Monday. Notice that the **month name** and
day-of-week **abbreviations** in the calendar change based on the browser's
preferred language setting.
In addition, the actual value returned after the user clicks on a date, shown
below the calendars, also reflects the language preference in any text it
contains - "Jan" vs. "janv". The element's Format attribute, of course,
controls the format of the date value returned into the element's input text box
after the mouse click.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) In a "globalized date" scenario, when passing/submitting
dates from your input controls to other definitions for use within tokens, as
filters on queries, or within elements such as Condition Filters, we
*highly* recommend utilizing the ISO-standard date format (yyyy-MM-dd) to
avoid any locale/browser date conflicts that might arise. The element's **Input
Date Reformat** attribute can be used for this purpose.
