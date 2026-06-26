---
title: "Global Event: OnGetUserPreferences"
id: 5281598997271
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281598997271-Global-Event-OnGetUserPreferences
updated_at: 2022-05-03T22:08:13Z
---

# Global Event: OnGetUserPreferences

# Global Event: OnGetUserPreferences

The **OnGetUserPreferences** Event is used to retrieve user preferences when entering the application and when editing/executing reports.

## Signature

For custom code the args array is structured as follows:

`args[]` contains one object, a string with the user preference’s id.

For .NET Assemblies the method signature is as follows:

```
string EventHandlerName(SessionInfo sessionInfo, string id)
```

## Expected Return

Expects a string return value, which represents the user preference’s value.

## Notes

The event will only be called if the ‘User Preference Storage Method’ is set to Server Events in the [User Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281636299927-User-Settings)
