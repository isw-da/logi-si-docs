---
title: "Global Event: OnConfigLoadStart"
id: 5281583209367
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281583209367-Global-Event-OnConfigLoadStart
updated_at: 2022-05-03T22:08:14Z
---

# Global Event: OnConfigLoadStart

# Global Event: OnConfigLoadStart

The **OnConfigLoadStart** event occurs after the configuration file is loaded. This may happen in the API when the API object is initialized or in Exago when entering the application directly. This event can be used to change any configuration information on-the-fly via the SessionInfo object, such as decrypting database connection strings.

## Signature

For custom code the args array is structured as follows:

`args[]` is empty.

For .NET Assemblies the method signature is as follows:

```
void EventHandlerName(SessionInfo sessionInfo)
```

## Expected Return

The OnConfigLoadStart Event has a void return value.
