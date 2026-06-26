---
title: "DataLayer.Cached - Attributes"
id: 4419722808471
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722808471-DataLayer-Cached-Attributes
updated_at: 2022-07-17T01:54:05Z
---

# DataLayer.Cached - Attributes

# DataLayer.Cached - Attributes

The **DataLayer.Cached** element has the following attributes:

| Attribute | Description |
| --- | --- |
| Cache Key | (Required) An arbitrary string value assigned by the developer. This is a unique identifier for the cached data, used to identify the cache when it's created and used with any subsequent requests for access to the cached data. It has application-wide scope, so the cache can be shared among all user sessions. The value can contain tokens in order to dynamically identify the cache to be used based on request variables or other values.  Caches can be made user-specific by using the token @Session.ID~ in this attribute. Developers can also identify a cache with multiple identifiers or tokens, in a comma-separated list. |
| ID | An optional element ID. Recommended for easier identification when debugging. |
| Expiration Now | If set to *True*, causes the data cache to be immediately deleted and recreated. Primarily useful for development purposes. Default value: *False* |
| Expiration Time | The **time of day** at which the data cache expires, causing it to be deleted and recreated by the next user request. Uses the 24-hour clock in the format of *hh:mm* or *h:mm*. For example: 5:00 is 5:00 a.m. and 14:24 is 2:24 p.m. Each expiration-related attribute operates independently of other expiration-related attributes. |
| Expiration Time Span | Sets the **lifetime**, in hours and minutes, of the data cache. Once this amount of time has passed since the creation of the cache, it will be deleted and recreated by the next user request. For example: a value of 1:34 represents one hour and 34 minutes, which will cause a cache created at 2:00 p.m. to expire at 3:34 p.m. Values without a colon are treated as minutes. Each expiration-related attribute operates independently of other expiration-related attributes. |
