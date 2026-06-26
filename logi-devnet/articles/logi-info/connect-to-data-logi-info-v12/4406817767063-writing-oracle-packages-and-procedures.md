---
title: "Writing Oracle Packages and Procedures"
id: 4406817767063
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817767063-Writing-Oracle-Packages-and-Procedures
updated_at: 2022-04-06T06:08:03Z
---

# Writing Oracle Packages and Procedures

# Writing Oracle Packages and Procedures

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
