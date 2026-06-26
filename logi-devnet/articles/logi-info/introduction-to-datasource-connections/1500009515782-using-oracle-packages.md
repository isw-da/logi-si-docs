---
title: "Using Oracle Packages"
id: 1500009515782
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515782-Using-Oracle-Packages
updated_at: 2021-06-17T01:58:33Z
---

# Using Oracle Packages

# Using Oracle Packages

This topic discusses the use of **Oracle Packages**. Oracle does not support directly returning **row sets** from stored procedures; however, this functionality is possible using Oracle Packages.

* About Oracle Packages
* [Writing Oracle Packages and Procedures](#StoredProcedures)
* [The Oracle Connection String](#ConnString)
* [Using DataLayer.SQL & Procedure.SQL](#SQLElements)
* [Using DataLayer.SP & Procedure.SP](#SPElements)

## About Oracle Packages

In the past most Oracle Server databases contained only a small amount of code in stored
procedures but, today, this is rapidly changing. **Oracle Packages** serve as a way to group **stored procedures** and **functions** together, typically based upon their common role. Benefits include better performance, code isolation, and the close coupling of data with behavior.

Logi reporting products support calls to Oracle Package procedures using **DataLayer.SQL**, **Procedure.SQL**, **DataLayer.SP**, and **Procedure.SP** elements.

When working with Oracle, you will need to ensure that you have the correct Oracle Provider
(if using OLEDB) or the Oracle Client (if using ODBC) installed on the web server.

## Writing Oracle Packages and Procedures

Oracle stored procedures can perform **non-query activities** such as INSERTs, UPDATEs, and DELETEs that do not necessarily return data.

However, in order for a stored procedure that *does* return data to work with Logi applications, it must return a valid **result set**, such as the output from a SELECT statement; data **cannot** be returned as individual values in **output parameters**. The package and procedure should be similar to this example, which returns a list of UserIDs from
a table in the database :

PACKAGE LGX\_GET\_DATA  
AS  
TYPE UserCur IS
REF CURSOR;  
PROCEDURE AllUser(o\_EmpCursor OUT UserCur);  
END
LGX\_GET\_DATA;  
  
PACKAGE BODY "LGX\_GET\_DATA"  
AS  
PROCEDURE
AllUser(o\_EmpCursor OUT UserCur)   
AS  
BEGIN   
OPEN o\_EmpCursor FOR
  
SELECT USER\_ID  
FROM USER\_ACCOUNTS   
ORDER BY USER\_ID;  
END AllUser;
  
END LGX\_GET\_DATA;

Your stored procedure can have any number of input parameters but it can have only **one output cursor**. In addition, the output cursor must be **last** in your procedure's **argument list**. For example, this **will work**

procedure X( iParam1 in integer, iParam2 in integer, ..., o\_cur out ioCursor )

but this **will not**:

procedure X( o\_cur out ioCursor, iParam1 in integer, iParam2 in integer, .... )

## The Oracle Connection String

The Connection String for an Oracle database requires a **special parameter** that you must code manually.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778537495/orapkgs_01.png)

Add the following parameter, highlighted above, to your Connection element's **Connection String** attribute:

PLSQLRSet=1

This informs the OLEDB provider that row sets can be returned (in the example above, an OLEDB provider supplied by Oracle has been installed and is used).

Check here to see examples of [Oracle connection strings](http://www.connectionstrings.com/?carrier=oracle) for a variety of configurations and circumstances. All must include the parameter shown above in order to return row sets.

## Using DataLayer.SQL or Procedure.SQL Elements

Although they're generally not used with stored procedures, the **DataLayer.SQL** and **Procedure.SQL** elements provide an easy way to call a stored procedure in an Oracle Package.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778537751/orapkgs_02.png)

As shown above, if you use the DataLayer.SQL or Procedure.SQL elements, their **Source** attribute should contain a command with the following syntax:

{call PackageName.ProcedureName('StringValue',NumericValue,...)}

The data in the returned row set is referenced using @Data tokens as usual.

**Usage Example**: imagine that a stored procedure named *MyProc* has been included an Oracle Package named *MyPackage*. The stored procedure requires two parameters: one a string and the other a number.

To use the stored procedure, the DataLayer element's Source attribute should contain:

{call MyPackage.MyProc('George',100)} 

If you want to call this stored procedure with variable arguments using token, the Source attribute should contain:

{call MyPackage.MyProc('@Request.FirstName~',@Request.Count~)}

## Using DataLayer.SP or Procedure.SP Elements

The Logi Studio elements designed to be used with stored procedures, **DataLayer.SP** and **Procedure.SP** can be used to retrieve data from an Oracle Package procedure. However, they behave slightly differently than they do in other circumstances.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771646487/orapkgs_03.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778538007/orapkgs_03a.png)

The DataLayer.SP or Procedure.SP element's **Command** attribute uses a particular syntax, shown above, to identify the Oracle Package and Procedure. This is *<packageName>.<procedureName>.*

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778538263/orapkgs_04.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771646743/orapkgs_04a.png)

As shown above, set the SP Parameters element's **Null Value** attribute to NULL.

You may use as many **input** parameters in your definition as you wish but **do not** use any **output parameters**. The data in the returned row set is referenced using @Data tokens as usual.
