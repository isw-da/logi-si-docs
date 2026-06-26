---
title: "Configure Date and Time Fields"
id: 4405859289879
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859289879-Configure-Date-and-Time-Fields
updated_at: 2021-09-21T01:28:00Z
---

# Configure Date and Time Fields

# Configure Date and Time Fields

Composer defines a field in your data as a date and time field in the following cases:

* The field type is **timestamp**.
* The field type is numeric containing the number of seconds since the UNIX epoch (UNIX Epoch time). This field type also known as the UNIX time stamp in seconds.
* The field type is numeric containing the number of milliseconds since the UNIX epoch (UNIX Epoch time). This field type is also known as the UNIX time stamp in milliseconds.
* The field is numeric and contains a **year** value.
* For [flat file](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer), [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4405850929943-Manage-the-Amazon-S3-Connector), [Hadoop Distributed File System (HDFS)](https://devnet.logianalytics.com/hc/en-us/articles/4405859226903-Manage-the-HDFS-Connector), and [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) connectors, the field is a string that matches one of the patterns in [*Supported Date and Time Formats*](https://devnet.logianalytics.com/hc/en-us/articles/4405851010711-Supported-Date-and-Time-Formats).

If your data contains a time field, Composer attempts to use the default time format (pattern) established in the data source configuration for the field. If Composer fails to detect a numeric field containing seconds, milliseconds, or years as a time field, change the field in the [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) as follows (see [*Change the Default Date and Time Format*](https://devnet.logianalytics.com/hc/en-us/articles/4405851009815-Change-the-Default-Date-and-Time-Format)):

| If the field contains | Change the field in the data source configuration as follows: |
| --- | --- |
| seconds | Set the field type to **Time** and specify a custom time pattern of `sssssssss`. |
| milliseconds | Set the field type to **Time**. (The default time pattern will be used). |
| years | Set the field type to **Time** and specify a custom time pattern of `yyyy`. |

If your data contains time-related fields (attributes) that are not stored in a recognized time format, you can convert the fields to time fields using one of the following methods.

* Change the field format in field specifications of the [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations). This is not the recommended method for reasons described in [*Convert Attributes to Time Fields in Data Source Field Specifications*](https://devnet.logianalytics.com/hc/en-us/articles/4405859290903-Convert-Attributes-to-Time-Fields-in-Data-Source-Field-Specifications).
* Create a Composer [derived field](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) to convert the data in the field to a time format supported by Composer. This is the preferred method. See [*Convert Attributes to Time Fields Using Derived Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4405859291927-Convert-Attributes-to-Time-Fields-Using-Derived-Fields).

You can also manage the time range used when displaying visuals and dashboards. See [*Use the Time Bar*](https://devnet.logianalytics.com/hc/en-us/articles/4405851196695-Use-the-Time-Bar).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Composer works with time data in UTC. Composer recommends that you set the timezone for your data source configurations in UTC to avoid time conversion issues.

See also [*Use the Network Time Protocol to Synchronize Time*](https://devnet.logianalytics.com/hc/en-us/articles/4405859386519-Use-the-Network-Time-Protocol-to-Synchronize-Time).
