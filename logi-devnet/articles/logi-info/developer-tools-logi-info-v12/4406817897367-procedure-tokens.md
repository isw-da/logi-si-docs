---
title: "@Procedure Tokens"
id: 4406817897367
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817897367--Procedure-Tokens
updated_at: 2022-04-06T06:08:55Z
---

# @Procedure Tokens

# @Procedure Tokens

These tokens are used within Process definition tasks:

| Token | Resolves To |
| --- | --- |
| @Procedure.*myProcedureID*.*ColumnName*~ | The data returned in the first row for the named column after **Procedure.SQL** executes. The element's **SQL Return Type** attribute must be set to *FirstRow*. |
| @Procedure.*myProcedureID*.ErrorMessage~ | The last error message string for the procedure with the specified ID. Usage: @Procedure.MyProcedureID.ErrorMessage~ |
| @Procedure.*myProcedureID*.ErrorOutput~ | When using the **Procedure.Run Shell Command** element, if the element's Error Output Filename attribute has been left blank, this token contains the shell command's or application's error output. If no error has occurred, this token will have no value. |
| @Procedure.*myProcedureID*.ExitCode~ | When using the **Procedure.Run Shell Command** element, contains the "exit" or "return" code from the shell command or application, often *0* for success. |
| @Procedure.*myProcedureID*.*MethodName*~ | The data returned from an external web service after **Procedure.Web Service** executes. The Web Service Method element used in the procedure must have its **Return Type** attribute set to *String*. |
| @Procedure.*myProcedureID*.rdReturnValue~ | The value of the stored procedure's Return Value, if any, after **Procedure.SP** executes.  For Procedure.File Exists and Procedure.Folder Exists, this token will return "*True*" or "*False*". |
| @Procedure.RowsAffected~ | The number of rows affected by an INSERT, UPDATE, or DELETE statement, after **Procedure.SQL** executes. Procedure.SQL element's **SQL Return Type** attribute must be set to *RowsAffected*. |
| @Procedure.*myProcedureID*.StandardOutput~ | When using the **Procedure.Run Shell Command** element, if the element's Standard Output Filename attribute has been left blank, this token contains the shell command's or application's standard console output. If there is no standard output, this will have no value. |
| @Procedure.*myProcedureID*.*Stored ProcedureOutputParamID~* | The data in an SP output parameter with the specified ID, after **Procedure.SP** executes.  Usage: @Procedure.MyProcedureID.MyOutputParamID~ |
| @Procedure.*myProcedureID*.TimedOut~ | When using the **Procedure.Run Shell Command** element, contains *True* if a timeout occurred; otherwise contains *False*. |

Four additional Procedure tokens specific to the File Upload process are shown in [@File Upload Tokens](https://devnet.logianalytics.com/hc/en-us/articles/4406817893271--File-Upload-Tokens).
