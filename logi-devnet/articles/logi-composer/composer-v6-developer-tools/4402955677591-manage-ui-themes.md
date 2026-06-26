---
title: "Manage UI\u00a0Themes"
id: 4402955677591
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955677591-Manage-UI-Themes
updated_at: 2021-08-07T17:32:08Z
---

# Manage UI Themes

# Manage UI Themes

Logi Composer supports themes for the [UI](https://devnet.logianalytics.com/hc/en-us/articles/4402955636119-Configurable-Data-Visualization). Several themes are supplied when you install Composer. See [*Supplied Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4402955678871-Supplied-Themes).

You can define and use your own themes. To manage themes, your Composer user must be assigned to a group with the **Can Administer Themes** (ROLE\_ADMINISTER\_THEMES) privilege enabled. See [*Group Privilege Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference).

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) At this time, you can only tailor theme colors. Other tailoring properties (such as fonts or font sizes) should not be changed.

Themes are defined, controlled, and managed using the `customization/themes` API endpoint. Any changes you make to the theme are applied for all users in the account. Users in other accounts are not affected.

You can specify a master theme in the theme JSON using the `masterThemeID` property. Master themes are optional, but allow you to identify the Composer-supplied theme from which properties should be inherited by a custom theme, if the properties are not specified in the custom theme JSON. Master themes can only be Composer- supplied themes. See [*Supplied Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4402955678871-Supplied-Themes).

This section covers the following topics:

* [*Themes API Endpoint*](https://devnet.logianalytics.com/hc/en-us/articles/4402955676183-Themes-API-Endpoint)
* [*Supplied Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4402955678871-Supplied-Themes)
* [*List Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4402963059863-List-Themes)
* [*Create a Theme*](https://devnet.logianalytics.com/hc/en-us/articles/4402955676823-Create-a-Theme)
* [*Review and Download the Theme JSON Code*](https://devnet.logianalytics.com/hc/en-us/articles/4402963061015-Review-and-Download-the-Theme-JSON-Code)
* [*Activate a Theme*](https://devnet.logianalytics.com/hc/en-us/articles/4402963057303-Activate-a-Theme)
* [*Update a Theme*](https://devnet.logianalytics.com/hc/en-us/articles/4402955679511-Update-a-Theme)
* [Patch a Theme](https://devnet.logianalytics.com/hc/en-us/articles/4402955678231-Patch-a-Theme)
* [*Delete a Theme*](https://devnet.logianalytics.com/hc/en-us/articles/4402963058327-Delete-a-Theme)
* [Sample Themes JSON File](https://devnet.logianalytics.com/hc/en-us/articles/4402963059095-Sample-Themes-JSON-File)

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.
