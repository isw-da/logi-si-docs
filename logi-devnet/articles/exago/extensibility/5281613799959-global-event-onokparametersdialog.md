---
title: "Global Event: OnOkParametersDialog"
id: 5281613799959
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281613799959-Global-Event-OnOkParametersDialog
updated_at: 2022-05-03T22:08:11Z
---

# Global Event: OnOkParametersDialog

# Global Event: OnOkParametersDialog

The **OnOkParametersDialog** Event occurs when a user clicks on the Ok button of the Parameter Prompt Window. The window will only displays if the report has a non-hidden parameter with a prompt text. This Event could be used to see what values the user is setting for each prompting parameter.

## Signature

For custom code the args array is structured as follows:

args[] is empty.

For .NET Assemblies the method signature is as follows:

```
string EventHandlerName(SessionInfo sessionInfo)
```

## Expected Return

The **OnOkParametersDialog** Event expects a string to be returned. Based on the returned string there are three possible results.

* **Null / White space** — If the string is null or white space then the report execution will continue as expected.
* **LanguageId** — If the string matches the id of any element in the language files then the string of that language element will be displayed as a message to the user. For more information see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support)
* **Other** — If the string does not match the id of any element in the language files then the returned value will be displayed as a message to the user.

## Notes

This Event cannot override the value of Parameters for the report execution.

The Parameters of the report being executed can be accessed through the sessionInfo object by using `sessionInfo.Report`.
