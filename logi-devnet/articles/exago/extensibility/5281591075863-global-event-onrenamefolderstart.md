---
title: "Global Event: OnRenameFolderStart"
id: 5281591075863
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281591075863-Global-Event-OnRenameFolderStart
updated_at: 2022-05-03T22:08:11Z
---

# Global Event: OnRenameFolderStart

# Global Event: OnRenameFolderStart

The **OnRenameFolderStart** event occurs when a user attempts to rename a folder. This event happens before the folder is renamed permitting you to stop the renaming if desired.

## Signature

For custom code the args array is structured as follows:

`args[]` contains two strings:

1. the fully qualified current folder name
2. the new folder name.

For .NET Assemblies the method signature is as follows:

```
string EventHandlerName(SessionInfo sessionInfo, string currentFolderName,  string newFolderName)
```

## Expected Return

The OnRenameFolderStart Event expects a string to be returned. Based on the returned string there are three possible results.

* **Null / White space** — If the string is null or white space then the report execution will continue as expected.
* **LanguageId** — If the string matches the id of any element in the language files then the string of that language element will be displayed as a message to the user. For more information see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support).
* **Other** — If the string does not match the id of any element in the language files then the returned value will be displayed as a message to the user.
