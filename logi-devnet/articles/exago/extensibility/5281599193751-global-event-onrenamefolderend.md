---
title: "Global Event: OnRenameFolderEnd"
id: 5281599193751
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281599193751-Global-Event-OnRenameFolderEnd
updated_at: 2022-05-03T22:08:12Z
---

# Global Event: OnRenameFolderEnd

# Global Event: OnRenameFolderEnd

The **OnRenameFolderEnd** Event occurs after user has renamed a folder.

## Signature

For custom code the args array is structured as follows:

`args[]` is contains two strings, the first represents the fully qualified old folder name, the second is the new folder name.

For .NET Assemblies the method signature is as follows:

string **EventHandlerName**(SessionInfo sessionInfo, string currentFolderName, string newFolderName)

## Expected Return

Anything can be returned to the OnRenameFolderEnd Event. Any return value will be ignored.
