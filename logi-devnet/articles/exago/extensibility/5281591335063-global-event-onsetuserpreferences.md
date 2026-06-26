---
title: "Global Event: OnSetUserPreferences"
id: 5281591335063
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281591335063-Global-Event-OnSetUserPreferences
updated_at: 2022-05-03T22:08:09Z
---

# Global Event: OnSetUserPreferences

# Global Event: OnSetUserPreferences

The **OnSetUserPreferences** Event is used to store user preferences when setting [startup reports](https://devnet.logianalytics.com/hc/en-us/articles/5281553297559-User-Preferences-and-Context-Sensitive-Help#Startup), saving interactive Report Viewer modifications as [user reports](https://devnet.logianalytics.com/hc/en-us/articles/5281553297559-User-Preferences-and-Context-Sensitive-Help#User) or color chooser user colors. The event will only be called if the **Admin Console** > **General** > **User Settings** > **User Preference Storage Method** is set to *Server Events*.

## Signature

For custom code the args array is structured as follows:

`args[]` contains two objects:

0. a string with the user preference’s id
1. a string with the user preference’s value

For .NET Assemblies the method signature is as follows:

```
void EventHandlerName(SessionInfo sessionInfo, string id, string value)
```

## Expected Return

The event has no return value.

## Additional Resources

* [Admin Support Lab — Customizing Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/5281531648279-Customizing-Color-Picker)
