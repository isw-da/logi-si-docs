---
title: "Wait Panel Element"
id: 4419715468695
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715468695-Wait-Panel-Element
updated_at: 2022-07-17T01:38:11Z
---

# Wait Panel Element

# Wait Panel Element

The **Wait Panel** element is a child of the General element and is automatically added to all new applications. When present in the \_Settings definition, it's global in effect andcauses a Wait Panel to be enabled anywhere one can be used, providing a default for the entire application. The Wait Panel element attribute values become the defaults for the entire application.

If a "local"Wait Panel element exists in a report definition, the attributes of that element will be used when displaying a Wait Panel. However, any empty local element attribute values, such as Caption, Class, or Caption Class, will default to the values set in the global Wait Panel element in \_Settings.

For all Wait Panel elements (except in the scenario in the previous paragraph):

* If there is no specific Caption attribute value specified, the value defaults to "Please Wait...".
* If there is no specific Class value specified, the valuedefaults to "rdThemeWaitPanel".
* If there is no specific Caption Class value specified, the valuedefaults to "rdThemeWaitCaption".
