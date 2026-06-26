---
title: "Oracle Packages"
id: 4419707766039
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707766039-Oracle-Packages
updated_at: 2022-07-17T02:06:47Z
---

# Oracle Packages

# Oracle Packages

Oracle does not support directly returning **row sets** from stored procedures; however, this functionality is possible using Oracle Packages.

In the past most Oracle Server databases contained only a small amount of code in stored
procedures but, today, this is rapidly changing. **Oracle Packages** serve as a way to group **stored procedures** and **functions** together, typically based upon their common role. Benefits include better performance, code isolation, and the close coupling of data with behavior.

Logi reporting products support calls to Oracle Package procedures using **DataLayer.SQL**, **Procedure.SQL**, **DataLayer.SP**, and **Procedure.SP** elements.

When working with Oracle, you will need to ensure that you have the correct Oracle Provider
(if using OLEDB) or the Oracle Client (if using ODBC) installed on the web server.

The following topics discuss the use of Oracle Packages:

* [Writing Oracle Packages and Procedures](https://devnet.logianalytics.com/hc/en-us/articles/4419707766935-Writing-Oracle-Packages-and-Procedures#StoredProcedures)
* [The Oracle Connection String](https://devnet.logianalytics.com/hc/en-us/articles/4419723102231-The-Oracle-Connection-String#ConnString)
* [Using DataLayer.SQL & Procedure.SQL](https://devnet.logianalytics.com/hc/en-us/articles/4419723103255-Using-DataLayer-SQL-or-Procedure-SQL-Elements#SQLElements)
* [Using DataLayer.SP & Procedure.SP](https://devnet.logianalytics.com/hc/en-us/articles/4419715426071-Using-DataLayer-SP-or-Procedure-SP-Elements#SPElements)

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 Logi Info and SSRM now support Oracle 19c databases.
