---
title: "Oracle Packages"
id: 4406817766039
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817766039-Oracle-Packages
updated_at: 2022-04-06T06:08:05Z
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

* [Writing Oracle Packages and Procedures](#StoredProcedures)
* [The Oracle Connection String](#ConnString)
* [Using DataLayer.SQL & Procedure.SQL](#SQLElements)
* [Using DataLayer.SP & Procedure.SP](#SPElements)
