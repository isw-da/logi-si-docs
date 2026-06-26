---
title: "Global Event: OnReportExecuteInit"
id: 5281591136663
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281591136663-Global-Event-OnReportExecuteInit
updated_at: 2022-05-03T22:08:10Z
---

# Global Event: OnReportExecuteInit

# Global Event: OnReportExecuteInit

Available in *v2019.1.9+*

The **OnReportExecuteInit**event occurs at the beginning of the report execution process similar to **OnReportExecuteStart**, but triggers before the Report Viewer’s rendering information metadata file has been created and sent to the client. This is in contrast to **OnReportExecuteStart** which triggers after the metadata is created.

This Event could be used to make modifications to column labels or column widths based on schema information, for example, prior to the generation of the metadata file being created.

This event will be called for all report execution types, including those via:

* Execution in the web app process (remote execution disabled)
* Remote execution
* Scheduled execution (including those using the **Scheduler Queue**)
* Batch scheduled executions
* GetExecute()

## Signature

For custom code the `args[]` array is structured as follows:  
`args[]` is empty

For .NET Assemblies the method signature is as follows:

```
string OnReportExecuteInit(SessionInfo sessionInfo)
```

## Expected Return

The **OnReportExecuteInit** Event expects a string to be returned. Based on the return string there are three possible results.

* **null**: If the string is null then the report execution will continue as normal.
* **LanguageId**: If the string matches the ID of any element in the language files then the string of that language element will be displayed as a message to the user and the report execution will terminate. For more information refer to [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support)
* **Other**: If the string does not match the ID of any element in the language files then the returned value will be displayed as a message to the user and the report execution will terminate.

## Notes

The report being executed can be accessed through the `sessionInfo` object by using `sessionInfo.Report`
