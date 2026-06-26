---
title: "Globalization and Localization"
id: 4406817603991
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817603991-Globalization-and-Localization
updated_at: 2022-04-06T06:07:09Z
---

# Globalization and Localization

# Globalization and Localization

The format and presentation of calendars and dates varies widely depending on
country and/or language. Some aspects of the date-related input elements are
controlled by the "preferred language" settings of the **browser** being used
and others may be affected by the default date and time format settings of the
**operating system**.

At the application level, date-related aspects of your Logi application can
also be changed by adding and configuring a **Globalization** element in the
application's \_Settings definition. More information about it use can be found in [Internationalization and Localization](https://devnet.logianalytics.com/hc/en-us/articles/4406822394391-Internationalization-and-Localization-).

For example, setting the Globalization element's **First Day of Week**attribute will change the display of the calendars. If the attribute value is set to *1*, then *Monday* will be the
first day in the calendar (the default is *Sunday*).

In addition, the browser's preferred **language setting** will affect the
display of the month and day-of-week names:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583849111/datacal_06.png)

In the examples shown above, a Globalization element has been used to change
the first day of the week to Monday. Notice that the day-of-week **abbreviations** in the calendar also change based on the browser's
preferred language setting.

In addition, the actual value returned after the user clicks on a date
also reflects the language preference in any text it
contains - "Jan" vs. "janv", for example.
