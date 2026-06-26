---
title: "Global Event: OnOkFiltersDialog"
id: 5281583469847
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281583469847-Global-Event-OnOkFiltersDialog
updated_at: 2022-05-03T22:08:12Z
---

# Global Event: OnOkFiltersDialog

# Global Event: OnOkFiltersDialog

The **OnOkFiltersDialog** Event occurs when a user clicks on the Ok button in the Filter Execution Window. This window only displays if prompt for value was checked for a filter. This Event could be used to see what filters are being used on the report and/or assure that a filter exists.

## Signature

For custom code the args array is structured as follows:

args[] is empty.

For .NET Assemblies the method signature is as follows:

```
string EventHandlerName(SessionInfo sessionInfo)
```

## Expected Return

The OnOkFiltersDialog Event expects a string to be returned. Based on the returned string there are three possible results.

* **Null / White space** — If the string is null or white space then the report execution will continue as expected.
* **LanguageId** — If the string matches the id of any element in the language files then the string of that language element will be displayed as a message to the user and the report execution will terminate. For more information see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support).
* **Other** — If the string does not match the id of any element in the language files then the returned value will be displayed as a message to the user and the report execution will terminate.

## Notes

The filters of the report being executed can be accessed through the sessionInfo object by using `sessionInfo.Report.ExecFilters`.
