---
title: "Using DataLayer.SQL or Procedure.SQL Elements"
id: 4419723103255
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723103255-Using-DataLayer-SQL-or-Procedure-SQL-Elements
updated_at: 2022-07-17T01:40:46Z
---

# Using DataLayer.SQL or Procedure.SQL Elements

# Using DataLayer.SQL or Procedure.SQL Elements

Although they're generally not used with stored procedures, the **DataLayer.SQL** and **Procedure.SQL** elements provide an easy way to call a stored procedure in an Oracle Package.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714869015/orapkgs_02.png)

As shown above, if you use the DataLayer.SQL or Procedure.SQL elements, their **Source** attribute should contain a command with the following syntax:

{call PackageName.ProcedureName('StringValue',NumericValue,...)}  

The data in the returned row set is referenced using @Data tokens as usual.
**Usage Example**: imagine that a stored procedure named *MyProc* has been included an Oracle Package named *MyPackage*. The stored procedure requires two parameters: one a string and the other a number.

To use the stored procedure, the DataLayer element's Source attribute should contain:

{call MyPackage.MyProc('George',100)}

If you want to call this stored procedure with variable arguments using token, the Source attribute should contain:

{call MyPackage.MyProc('@Request.FirstName~',@Request.Count~)}
