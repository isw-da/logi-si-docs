---
title: "Use the SuperWidget in Your Application"
id: 4406822348055
section: "Use InfoGo/Discovery Module - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822348055-Use-the-SuperWidget-in-Your-Application
updated_at: 2022-04-06T06:06:23Z
---

# Use the SuperWidget in Your Application

# Use the SuperWidget in Your Application

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) SuperWidgets have been deprecated in Logi Info v12.6.
Now you're ready to use your widget in the Logi Info application.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575695383/ls31_getstart_19.png)

Add a **SuperWidget** element in an appropriate place in your Logi
report definition, similar to the example above. Configure the
SuperWidget appropriately and click the browse button at the end of the **Widget Config ID** attribute value to display the SuperWidget Selector dialog box:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583931927/ls31_getstart_20.png)

This dialog box contains an entry for every widget you build with the
SuperWidget Authoring tool. Select the one you just made
and the dialog box will close and the widget's GUID will be
filled-in back in the attribute value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563282327/ls31_getstart_21.png)

Save and browse your report and, as in the example above, your
visualization widget should be included. Notice that the widget is fully-functional,
with live Explorer features, and is not embedded in an iFrame.

You should be aware that the widget is sensitive to the **Logi Theme** being used in your application and may display with different colors or fonts as a result. The *Arizona* theme, downloadable from DevNet, was used in these examples.

To keep this exercise brief, we've done the bare minimum. There are many additional features available when authoring SuperWidgets, including a dashboard widget and the ability to embed a visualization with the complete Thinkspace, and they're fully described in [SuperWidgets](https://devnet.logianalytics.com/hc/en-us/articles/4406817649687-SuperWidgets).
