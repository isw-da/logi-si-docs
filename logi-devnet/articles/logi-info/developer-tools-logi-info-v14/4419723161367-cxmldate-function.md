---
title: "CXMLDate Function"
id: 4419723161367
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723161367-CXMLDate-Function
updated_at: 2022-10-06T17:22:09Z
---

# CXMLDate Function

# CXMLDate Function

DateTime-type data returned into a datalayer from a databases is often in [ISO 8601](http://www.iso.org/iso/home/standards/iso8601.htm) format, which looks like this:

2007-05-31T13:30:00 (representing yyyy-mm-ddThh:mm:ss)

If you wish to use script functions to **compare,** **manipulate,** or **format** the date data, you need to convert it into a compatible format. Logi's intrinsic **CXMLDate** function has been provided for this purpose. The following example uses an intrinsic function to add one day to a date value,

=DateAdd("d", 1, CXMLDate("@Data.EnrollmentDate~"))

and the CXMLDate function has been used to convert the data retrieved from the database. Here's another example that finds the difference, in days, between dates in two separate date-type columns,

=DateDiff("d", CXMLDate("@Data.OrderDate~"), CXMLDate("@Data.ShippedDate~"))  

and, once again, the CXMLDate function is used to convert the date values for use with the intrinsicDateDiff() function.
