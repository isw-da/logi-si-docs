---
title: "Global Event: OnAfterReportExportSuccess"
id: 5281621560215
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281621560215-Global-Event-OnAfterReportExportSuccess
updated_at: 2022-05-03T22:08:15Z
---

# Global Event: OnAfterReportExportSuccess

# Global Event: OnAfterReportExportSuccess

The *OnAfterReportExportSuccess* event (*v2018.2.14+, v2019.1.1+*) is called after a report execution export file has been generated for a specified report. The server event implementation may load the export file from disk using the supplied file path, *exportFilePath*, modify the file, then save the changes back to disk. If the server event implementation saves changes to the export file, the file must be saved with the same file name that is passed in as the *exportFilePath*.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> If the file is saved to a different path, modifications will not be honored by Exago.

This server event will be called for all report execution export files generated, including those generated via:

* Execution in the web app process (remote execution disabled)
* Remote execution
* Scheduled execution (including those using the **Scheduler Queue**)
* Batch scheduled executions
* GetExecute()

It is compatible with HTML, PDF, RTF, Excel, and CSV export types.

## Signature

For custom code the args array is structured as follows:

args[] contains two arguments: args[0] should contain a string representing the file path of the exported report, and args[1] should contain a [wrExportType](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrExport) object representing the export type of the report.

For .NET Assemblies the method signature is as follows:

```
void EventHandlerName(SessionInfo sessionInfo, string exportFilePath, wrExportType exportType)
```

## Expected Return

The return value of this event is ignored.
