---
title: "Supported Date and Time Formats"
id: 4405851010711
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851010711-Supported-Date-and-Time-Formats
updated_at: 2021-09-21T01:28:01Z
---

# Supported Date and Time Formats

# Supported Date and Time Formats

Composer generally supports all valid date and time formats, including the ISO (International Organization for Standardization) 8601 standard. ISO 8601 ([*http://en.wikipedia.org/wiki/ISO\_8601*](https://en.wikipedia.org/wiki/ISO_8601)) provides a method for representing dates and times that help avoid misinterpretation of numeric representations of dates and times, especially across countries using different conventions. Composer supports time based on both the 12- and 24-hour timekeeping systems and can read timezone information. In addition, Composer can also interpret UNIX time stamp and time represented in milliseconds. Composer allows you to change the date and time format of time fields in a data source. See [*Configure Date and Time Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4405859289879-Configure-Date-and-Time-Fields).

Composer recognizes the following standard date and time formats for [flat file](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer), [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4405850929943-Manage-the-Amazon-S3-Connector), [Hadoop Distributed File System (HDFS)](https://devnet.logianalytics.com/hc/en-us/articles/4405859226903-Manage-the-HDFS-Connector), and [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) connectors:

* yyyy-MM-dd HH:mm:ss
* yyyy-MM-dd HH:mm:ss.SSS
* yyyy-MM-dd HH:mm:ss,SSS
* yyyy-MM-dd'T'HH:mm:ss
* yyyy-MM-dd'T'HH:mm:ssZ
* yyyy-MM-dd'T'HH:mm:ss.SSS
* yyyy-MM-dd'T'HH:mm:ss.SSSZ
* MM/dd/yyyy HH:mm:ss
* MM/dd/yy h:mm a
* MM/dd/yy HH:mm:ss
* MM/dd/yy HH:mm
* MM/dd/yy hh:mm a
* MMM dd, yyyy hh:mm a
* MMM dd yyyy HH:mm:ss
* dd/MM/yyyy hh:mm:ss a
* dd/MM/yy hh:mm:ss a
* yyyy-MM-dd
* MM/dd/yy
* MM/dd/yyyy
* yyyy
* unix time stamp
* time as milliseconds

Upon successful connection with a data source, Composer displays the results on the Fields page (as shown in Figure 1). Date and time information will be available via either the Timestamp (\_ts) column (1) or identified in the Type descriptor (2). Note that if the data source does not provide a Timestamp column, then the admin can edit the Type column to specify a Time attribute.
