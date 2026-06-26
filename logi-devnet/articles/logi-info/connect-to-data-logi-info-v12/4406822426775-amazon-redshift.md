---
title: "Amazon Redshift"
id: 4406822426775
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822426775-Amazon-Redshift
updated_at: 2022-04-06T06:07:28Z
---

# Amazon Redshift

# Amazon Redshift

Amazon Redshift is a fast, fully-managed, petabyte-scale data warehouse service in "the cloud". It's optimized for datasets ranging from a few hundred gigabytes to a petabyte, or more. Before using the service, you must sign-up and be licensed by Amazon. For more information, see the [Amazon Redshift website](http://docs.aws.amazon.com/redshift/latest/dg/welcome.html).

The **Connection.Redshift** element allows you to connect your Logi application to the Amazon service. This is an ODBC connection and requires an ODBC connection string that includes the credentials assigned to you by Amazon.

For a .NET application, you'll need to install the Amazon Redshift ODBC Driver (32- or 64-bit, matching your Logi Info installation), and configure it with appropriate settings and a connection string with account credentials. This process is described in detail in [this Amazon Web Services
document](http://docs.aws.amazon.com/redshift/latest/mgmt/install-odbc-driver-windows.html).

For earlier versions of Logi Info .NET and Info Java applications, you must use
the PostgreSQL 8.x JDBC and ODBC drivers to ensure compatibility. The PostrgreSQL
9.x JDBC and ODBC drivers might not work properly with all applications.

Though you can have success using standard DataLayer.SQL, for best performance with very large datasets, we recommend use of [DataLayer.ActiveSQL](https://devnet.logianalytics.com/hc/en-us/articles/4406817277847-DataLayer-ActiveSQL). Amazon Redshift SQL is based on PostgreSQL 8.0.2. syntax but has a number of very important differences that you must be aware of as you design and develop your data warehouse applications. Please refer to the [Amazon SQL Reference](http://docs.aws.amazon.com/redshift/latest/dg/cm_chap_SQLCommandRef.html) for more information.

Because of the nature of the Amazon Redshift service, Studio's wizards, Query Builder, Database Browser, and the "available columns" list in the Attributes panel, may not work, or work completely,in all cases.
