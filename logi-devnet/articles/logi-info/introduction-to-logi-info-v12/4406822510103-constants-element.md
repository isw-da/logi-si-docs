---
title: "Constants Element"
id: 4406822510103
section: "Introduction to Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822510103-Constants-Element
updated_at: 2022-04-06T06:08:34Z
---

# Constants Element

# Constants Element

Constants are global, literal values that will not change and that can be used in all definitions. They're created in \_Settings, using the **Constants** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575548183/settingsdef_03.png)

Constants are created, as shown above, as a parameter list and are accessed using @Constant tokens. For example, the value of the first constant in the list shown above would be available using @Constant.EditMode~. For more information on @Constant tokens, see [Token Types](https://devnet.logianalytics.com/hc/en-us/articles/4406817900439-Token-Types).

The use of constants provides a way to have values referenced throughout your application while only defining them in a single place, which makes maintenance very easy. Constants are often used for values that might change between development and production environments.
