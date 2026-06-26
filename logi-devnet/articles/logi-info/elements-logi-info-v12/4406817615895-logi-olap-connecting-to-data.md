---
title: "Logi OLAP - Connecting to Data"
id: 4406817615895
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817615895-Logi-OLAP-Connecting-to-Data
updated_at: 2022-04-06T06:07:14Z
---

# Logi OLAP - Connecting to Data

# Logi OLAP - Connecting to Data

These are the basic steps for creating an application using an OLAP Grid and connecting to the data:

1. In Logi Studio, create a new application as usual and register it with IIS.
![](https://devnet.logianalytics.com/hc/article_attachments/4417575622039/getstartolap_02.png)  

2. In the \_Settings definition, add a **Connection.OLAP** element, as shown above, and set its attributes. The **ADOMD Connection String** attribute value can be a bit more complicated than the usual database connection string and there are other data provider requirements as well. For more information, see [Connect to MS SQL Server Analysis Services](https://devnet.logianalytics.com/hc/en-us/articles/4406822201239-Connect-to-MS-SQL-Server-Analysis-Services).
