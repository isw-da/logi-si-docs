---
title: "DataLayer.SQL - Writing Data to the Database"
id: 4419722845975
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722845975-DataLayer-SQL-Writing-Data-to-the-Database
updated_at: 2023-06-13T15:23:03Z
---

# DataLayer.SQL - Writing Data to the Database

# DataLayer.SQL - Writing Data to the Database

Logi Info applications are fully capable of writing data to a SQL database (the so-called "Writeback" capability) and can execute any valid SQL statement that does so, including INSERT, UPDATE, and DELETE.

This can be done in combination with a SELECT operation, as shown in the data retrieval example above. More commonly, it's done independently in a Process Task using a **Procedure.SQL** element or by calling a stored procedure using a **Procedure.SP** element. Both of these techniques are discussed in detail in [Process Tasks](https://devnet.logianalytics.com/hc/en-us/articles/4419715442583-Process-Tasks).
