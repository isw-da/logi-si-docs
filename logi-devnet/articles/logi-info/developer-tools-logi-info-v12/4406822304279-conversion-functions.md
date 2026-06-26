---
title: "Conversion Functions"
id: 4406822304279
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822304279-Conversion-Functions
updated_at: 2022-04-06T06:05:50Z
---

# Conversion Functions

# Conversion Functions

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The functions listed in the table below are for SQL queries and should not be used with inline scripts.

The following table lists the conversion functions used in Logi Info:

| Attribute | Description |
| --- | --- |
| BOOLEAN\_TO\_STR(boolean) | Converts a boolean value to a string. Each data sources stores boolean values using different types. Some use integers, others use bit, and a few actually have a boolean type. Because of these type issues, the function code for each system expects sightly different values. In order to test this function or any of the boolean functions, please use a boolean field. e.g. BOOLEAN\_TO\_STR([Invoiced]) returns 'true' if Invoiced is *true*. |
| DATE\_TO\_UNIXTIME(datetime\_value) | Converts a date time value into a unix timestamp. e.g. DATE\_TO\_UNIXTIME([OrderDate]) returns an integer like 1231451515 |
| INT\_TO\_DATETIME(integer) | Converts a numeric integer value to date time value. e.g. INT\_TO\_DATETIME(1231451515) returns 2009-01-08 21:51:55 |
| STR\_TO\_DATETIME(string) | Converts a string representation of a date value to date time value. String must be ISO8601 format. e.g. STR\_TO\_DATETIME('2015-04-30T22:45:33') |
| STR\_TO\_LONG(string) | Converts string value to long value (64bit integer). e.g. STR\_TO\_LONG('723874928') returns 723874928 |
| STR\_TO\_DECIMAL(string) | Converts string value to decimal value. e.g. STR\_TO\_DECIMAL('10.53') returns 10.53 |
| STR\_TO\_BOOLEAN(string) | Converts string value to boolean value. e.g. STR\_TO\_BOOLEAN('true') depending on internal boolean type of system it could be a 1 or true |
| TO\_STRING(any) | Converts value to string value. e.g. TO\_STRING(20) will be converted to '20' |
