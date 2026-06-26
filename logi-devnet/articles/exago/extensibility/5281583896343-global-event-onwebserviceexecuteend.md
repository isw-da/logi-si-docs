---
title: "Global Event: OnWebServiceExecuteEnd"
id: 5281583896343
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281583896343-Global-Event-OnWebServiceExecuteEnd
updated_at: 2022-05-03T22:08:08Z
---

# Global Event: OnWebServiceExecuteEnd

# Global Event: OnWebServiceExecuteEnd

The **OnWebServiceExecuteEnd** Event occurs when data is returned from a Web Service Data Source. This Event could be used to decompress or decrypt data being returned from a Web Service Data Source.

## Signature

For custom code the args array is structured as follows:

`args[]` contains a single string of the data coming from the Web Service in position zero.

For .NET Assemblies the method signature is as follows:

```
string EventHandlerName(SessionInfo sessionInfo, string webServiceXml)
```

## Expected Return

The OnWebServiceExecuteEnd Event expects a string to be returned.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This Event only occurs when the **callType** Parameter has the value *1*.
