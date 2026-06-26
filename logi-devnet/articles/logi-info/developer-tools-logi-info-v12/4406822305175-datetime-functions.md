---
title: "DateTime Functions"
id: 4406822305175
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822305175-DateTime-Functions
updated_at: 2022-04-06T06:05:51Z
---

# DateTime Functions

# DateTime Functions

Supported date\_part values are *Second*, *Minute*, *Hour*, *Day*, *Week*, *Month*, *Quarter*, and *Year*.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The functions listed in the table below are for SQL queries and should not be used with inline scripts.

The following table lists the datetime functions used in Logi Info:

| Function | Description |
| --- | --- |
| DATEADD('date\_part', interval, datetime) | Returns a datetime value by adding the interval to datetime. The type of interval is determined by date\_part. e.g. DATEADD(Month, 4, '1997-04-20T11:30:15') returns '1997-08-20T11:30:15' |
| DATEDIFF('date\_part', date1, date2) | Returns the difference between date1 and date2 in units of date\_part. e.g. DATEDIFF('Month', '1997-04-20T11:30:15', '1997-07-20T11:30:15') returns 3 |
| DATENAME('date\_part', date) | Returns date\_part of the datetime value as a string. e.g. DATENAME('Month', '1997-04-20T11:30:15') returns 'April' |
| DAYOFMONTH(date) | Returns the day of the month (number from 1 to 31). e.g. DAYOFMONTH('1997-04-20T11:30:15') returns 20 |
| DAYOFWEEK(date) | Returns the weekday index of the date (1 = Sunday, 2 = Monday, ..., 7 = Saturday). e.g. DAYOFWEEK('1997-04-20T11:30:15') returns 1 |
| DAYOFYEAR(date) | Returns the day of the year (number from 1 to 366). e.g. DAYOFYEAR('1997-04-20T11:30:15') returns 110 |
| DATEPART('date\_part', date) | Returns date\_part of the datetime value as an integer. e.g. DATEPART('Day', '1997-04-20T11:30:15') returns 20 |
| NOW() | Returns the current date and time. Does not accept arguments. |
| TO\_DATE(datetime) | Returns the date part of datetime value. e.g. TO\_DATE([OrderDate]) returns the date without the time component. |
| TODAY() | Supported temporal values are Second, Minute, Hour, Day, Week, Month, Quarter, and Year. |
