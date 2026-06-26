---
title: "Global Event: OnAfterLoadReportsList"
id: 5281590543127
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281590543127-Global-Event-OnAfterLoadReportsList
updated_at: 2022-05-03T22:08:16Z
---

# Global Event: OnAfterLoadReportsList

# Global Event: OnAfterLoadReportsList

Occurs after reports created in Exago have been loaded into the Report Tree, but before the Report Tree is drawn into the user interface.

## Signature

For custom code the arguments array is structured as follows:

`args[]` contains one object:

0. a `WebReports.UI.Controls.TreeNodeCollection`, a list of `WebReports.UI.Controls.TreeNode` objects to populate the Report Tree

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The **TreeNodeCollection** and **TreeNode** classes are defined in the `WebReports.dll` library, which is not automatically referenced in the Admin Console. To use this Server Event, add `WebReports.dll` as a reference, and include the `WebReports.UI.Controls` namespace.

For .NET Assemblies the method signature is as follows:

```
void EventHandlerName(SessionInfo sessionInfo, TreeNodeCollection nodes)
```

## Expected Return

The event does not return a value.
