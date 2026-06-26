---
title: "DataLayer.SQL - Writing Data to the Database"
id: 4406817329815
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817329815-DataLayer-SQL-Writing-Data-to-the-Database
updated_at: 2022-04-06T06:05:25Z
---

# DataLayer.SQL - Writing Data to the Database

# DataLayer.SQL - Writing Data to the Database

Logi Info applications are fully capable of writing data to a SQL database (the so-called "Writeback" capability) and can execute any valid SQL statement that does so, including INSERT, UPDATE, and DELETE.

This can be done in combination with a SELECT operation, as shown in the data retrieval example above. More commonly, it's done independently in a Process Task using a **Procedure.SQL** element or by calling a stored procedure using a **Procedure.SP** element. Both of these techniques are discussed in detail in [Process Tasks](https://devnet.logianalytics.com/hc/en-us/articles/4406817796375-Process-Tasks).
