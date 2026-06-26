---
title: "Customizing Appearance"
id: 4406822195863
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822195863-Customizing-Appearance
updated_at: 2022-04-06T06:04:36Z
---

# Customizing Appearance

# Customizing Appearance

You can change the basic look of the application by changing its theme, which is set in the \_Settings definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563446935/cfginfogo125_19.png)

The default theme is *Signal* but, as shown above, you can use other themes. More information about themes can be found in [Themes](https://devnet.logianalytics.com/hc/en-us/articles/4406818168855-Themes).

## Editing Themes

Custom themes can be created using the **Theme Editor**. This is most easily done by the developer, using the Theme Editor wizard in Logi Studio. When a custom theme is used in the InfoGo application, administrative users can be allowed edit it at runtime. For more information about creating a custom theme, see
[Using the Theme Editor](https://devnet.logianalytics.com/hc/en-us/articles/4406818044055-Using-the-Theme-Editor).

To enable an administrative user to edit a custom theme while using the InfoGo application, the goThemeEditorEnabled constant must be set to *True* and the user must have the InfoGoThemeManager security Right. Once this is done, the Theme Editor will appear as an option on the menu:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563447063/cfginfogo125_20.png)

This option launches an embedded instance of the Theme Editor and allows modification of an existing custom theme right inside InfoGo at runtime.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The embedded Theme Editor will *not* edit standard built-in themes, like Signal. It will only edit "custom" themes, which are copies of standard themes.

A custom theme can be created using the Theme Editor wizard in Logi Studio, or it can be created manually:

1. Copy a standard theme folder from: C:\Program Files\Logi Analytics\InfoGo\rdTemplate\rdTheme to  
   C:\Program Files\Logi Analytics\InfoGo\\_Themes and rename the folder with your custom theme name (you may need to create the \_Themes folder).
2. In InfoGo's \_Settings definition, set the **Global Style** element's **Theme** attribute to your custom theme name.
3. The embedded Theme Editor will now be able to edit the custom theme.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Any theme customizations are not user-specific; they will affect the appearance of InfoGo for *all* users.
