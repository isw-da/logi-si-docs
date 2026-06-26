---
title: "Global Event: OnConfigLoadEnd"
id: 5281598746391
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281598746391-Global-Event-OnConfigLoadEnd
updated_at: 2022-05-03T22:08:15Z
---

# Global Event: OnConfigLoadEnd

# Global Event: OnConfigLoadEnd

The **OnConfigLoadEnd** Event occurs after all API changes are made and the host application container is redirected to Exago. If entering Exago directly this event occurs immediately after [Global Event: OnConfigLoadStart](https://devnet.logianalytics.com/hc/en-us/articles/5281583209367-Global-Event-OnConfigLoadStart). If the API is being used but the host application does not redirect to Exago (such as using the direct Report.GetExecuteData method) the event can manually be called using the public method *Api.SetupData.FireOnConfigLoadEndEvent()*.

Similar to the OnConfigLoadStart event, this event can also be used to change configuration information on-the-fly via the sessionInfo object. However making these changes after the API calls can provide extra convenience. For example if the host application is using the Web Service API it can set a single parameter value using the WebService and then based on that parameter make further configuration changes within this event. This provides better performance, security and a reduction of http requests.

## Signature

For custom code the args array is structured as follows:

`args[]` is empty.

For .Net Assemblies the method signature is as follows:

```
void EventHandlerName(SessionInfo sessionInfo)
```

## Expected Return

The OnConfigLoadEnd Event has a void return value.
