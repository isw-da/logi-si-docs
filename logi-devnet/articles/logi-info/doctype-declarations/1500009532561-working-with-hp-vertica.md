---
title: "Working With HP Vertica"
id: 1500009532561
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009532561-Working-With-HP-Vertica
updated_at: 2021-06-17T01:58:47Z
---

# Working With HP Vertica

# Working With HP Vertica

The column-oriented **HP Vertica** database is designed to manage large,
fast-growing volumes of data. This document discusses the special elements in Logi Info and Logi Report for use with this database.

This document is specific to **v11.2.040+** of our products. Topics include:

* About HP Vertica
* [Connecting to HP Vertica](#Connecting)
* [Retrieving Data from HP Vertica](#Retrieving)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771450519/plusicon.gif)General information about HP Vertica can be found at the [official website.](http://www.vertica.com/)

## About HP Vertica

The column-oriented HP Vertica RDBMS is designed to manage large,
fast-growing volumes of data and provide very fast query performance
when used for data warehouses and other query-intensive applications. It
claims to drastically improve query performance over traditional
relational database systems, to provide high-availability, and offer petabyte-scalability on commodity enterprise servers. A free,
feature-limited copy
for local use is available for download and subscriptions are available to their hosted service.

## Connecting to HP Vertica

In order to use HP Vertica, you need to use a specific Connection element, **Connection.Vertica**, to connect your Logi application to a Vertica database.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771450775/workvertica_02.png)

As shown above, the **Connection.Vertica** element is added to the **\_Settings** definition, beneath the Connections element. Its attributes are then set appropriately for the Vertica datasource.

### Special Drivers Required

For a **.NET** Logi application, you will need to *download* the Vertica **ADO.NET driver** and place it in the <yourLogiApp>\bin folder. The driver is available from the [My Vertica community web site](https://my.vertica.com/), which requires you to register and login. Version 6.1.3.0 or later is required.

For a **Java** Logi application, you will also to *download* the Vertica **JDBC driver** and place it in the <yourLogiApp>/WEB-INF/lib folder. The driver is available from the [My Vertica community web site](https://my.vertica.com/), which requires you to register and login. Version 6.1.3.0 or later is required.

In either case, if you want to be able to use Logi Studio's **Database Browser** and **SQL Query Builder** tools while working with Vertica, you must download the Vertica ADO.NET driver mentioned above and place it in the bin folder of your Logi Info installation, typically C:\Program Files\LogiXML IES Dev\Logi Studio\bin.

## Retrieving Data from HP Vertica

You can use DataLayer.SQL to retrieve data from Vertica but, for best performance with very large datasets, we recommend the use of [DataLayer.ActiveSQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009514502-DataLayer-ActiveSQL).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771451031/workvertica_03.png)

Vertica uses **HP Vertica SQL** which is based on standard SQL syntax but has a number of very important differences that you should be aware of as you create your queries. Please refer to the [HP Vertica SQL Reference Manual](https://www.scribd.com/document/217776653/HP-Vertica-6-1-x-SQLRefManual) for more information. After the data is retrieved, you may condition, filter, and shape it just as you would any other datalayer data.
