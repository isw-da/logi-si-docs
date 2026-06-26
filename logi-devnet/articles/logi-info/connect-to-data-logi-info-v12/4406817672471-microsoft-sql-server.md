---
title: "Microsoft SQL Server"
id: 4406817672471
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817672471-Microsoft-SQL-Server
updated_at: 2022-04-06T06:07:32Z
---

# Microsoft SQL Server

# Microsoft SQL Server

**Microsoft SQL Server** is a relational database management system developed by Microsoft. It's available in a variety of editions and in local, remote, and cloud-based configurations. It supports a wide variety of transaction processing, business intelligence, and analytics applications in corporate IT environments and is one of the market-leading database technologies.

## Context Switching

Microsoft SQL Server supports "context switching" - changing of the identity against which permissions to execute statements or perform activities are checked. This is analogous to using the "EXECUTE AS *<UserName>*" command in SQL.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575603479/introconn5_25.png)

To switch contexts in a Logi application, use a child **SQL Server Context** element beneath the Connection.SQL Server element, as shown above, and set its **Username** attribute value to a valid SQL Server user name, or to any Logi token containing one. The context is re-evaluated with every data request, gets set just before the SQL query is run, and gets reset right after it runs, providing a way to dynamically set the context.

## Connection Parameters

The **Microsoft SQL Server Parameters** element allows you to supply additional parameters when connecting to a Microsoft SQL Server database.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563165207/introconn5_26.png)

Examples of additional connection parameters include *Async*, *Encrypt*, *Integrated Security*, *Persist Security Info*, *Replication*, and *TrustServerCertificate*.

## SQL Server Connection using Windows Authentication

If you're working within a Windows Domain, you may wish to use the domain login credentials as SQL Server login credentials. This may be a convenience just for developers or may be the method you want to employ for all application users. Here are the steps to achieve this:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583815959/introconn5_26_247x76.png)

1. Add a **Connection.SqlServer** element, withchild **Microsoft SQL Server Parameters** element, as shown above. Leave the Connection element's **User** and **Password** attributes blank.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563165719/introconn5_29.png)
2. Configure the Microsoft SQL Server Parameters element to have one parameter, as shown above. *Use the exact spelling and case shown*.

## Logi Application Services Parameters

The **Logi Application Service Jdbc Params** element allows you to supply additional parameters when connecting to the Logi Application Service.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583816343/introconn5_27.png)

Logi Info generates special JDBC connections when the Logi Application Service has been installed. Use this to element to supply additional parameters for connecting to it. An example of a JDBC parameter is *integratedSecurity*.
