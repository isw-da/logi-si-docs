---
title: "Manage UI\u00a0Themes"
id: 4405859480983
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859480983-Manage-UI-Themes
updated_at: 2021-09-21T01:29:44Z
---

# Manage UI Themes

# Manage UI Themes

Logi Composer supports themes for the [UI](https://devnet.logianalytics.com/hc/en-us/articles/4405851128343-Configurable-Data-Visualization). Several themes are supplied when you install Composer. See [*Supplied Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859482263-Supplied-Themes).

You can define and use your own themes. To manage themes, your Composer user must be assigned to a group with the **Can Administer Themes** (ROLE\_ADMINISTER\_THEMES) privilege enabled. See [*Group Privilege Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) At this time, you can only tailor theme colors. Other tailoring properties (such as fonts or font sizes) should not be changed.

Themes are defined, controlled, and managed using the `customization/themes` API endpoint. Any changes you make to the theme are applied for all users in the account. Users in other accounts are not affected.

You can specify a master theme in the theme JSON using the `masterThemeID` property. Master themes are optional, but allow you to identify the Composer-supplied theme from which properties should be inherited by a custom theme, if the properties are not specified in the custom theme JSON. Master themes can only be Composer- supplied themes. See [*Supplied Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859482263-Supplied-Themes).

This section covers the following topics:

* [*Themes API Endpoint*](https://devnet.logianalytics.com/hc/en-us/articles/4405851184407-Themes-API-Endpoint)
* [*Supplied Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859482263-Supplied-Themes)
* [*List Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859479831-List-Themes)
* [*Create a Theme*](https://devnet.logianalytics.com/hc/en-us/articles/4405851185303-Create-a-Theme)
* [*Review and Download the Theme JSON Code*](https://devnet.logianalytics.com/hc/en-us/articles/4405851188375-Review-and-Download-the-Theme-JSON-Code)
* [*Activate a Theme*](https://devnet.logianalytics.com/hc/en-us/articles/4405859476887-Activate-a-Theme)
* [*Update a Theme*](https://devnet.logianalytics.com/hc/en-us/articles/4405851189399-Update-a-Theme)
* [Patch a Theme](https://devnet.logianalytics.com/hc/en-us/articles/4405851187351-Patch-a-Theme)
* [*Delete a Theme*](https://devnet.logianalytics.com/hc/en-us/articles/4405859478551-Delete-a-Theme)
* [Sample Themes JSON File](https://devnet.logianalytics.com/hc/en-us/articles/4405851186327-Sample-Themes-JSON-File)

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.
