---
title: "Manage User Interface Themes"
id: 43701163831053
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-User-Interface-Themes
updated_at: 2026-08-31T04:16:24Z
---

# Manage User Interface Themes

# Manage User Interface Themes

Composer includes support for color themes that help you define the colors of your user interface. Match to your corporate colors, or use one of several built in themes.

**Important:** In this release, when you [enable the Enhanced Experience](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables) user interface, users see changes to workflows and the user interface. The classic themes require updates to allow your users to see a consistent color scheme. For more information, see [User Interface Themes: v26.2 and Later](#User2) and [Themes and UI Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077251302669-Themes-and-UI-Updates).

You can define and use your own color themes. To manage themes, a Composer user must be assigned to a group with the **Administer Themes** (ROLE\_ADMINISTER\_THEMES) privilege enabled. See [Group Privilege Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).

**Note:** You can only tailor theme colors. Other tailoring properties (such as fonts or font sizes) should not be changed.

Themes are defined, controlled, and managed using the `customization/themes` API endpoint. Any changes you make to the theme are applied for all users in the tenant account. Users in other tenant accounts are not affected.

You can specify a master theme in the theme JSON using the `masterThemeID` property to define properties you want have inherited by a custom theme. Using a master theme is optional. Only Composer-supplied themes can be used as a master theme. See [Supplied Themes](#Supplied).

## User Interface Themes: v26.2 and Later

Beginning with the release of v26.2, you have access to a refreshed user interface for use in your environment. For information on previous releases, see [User Interface Themes: Earlier Releases](#User).

Your home page, main menu, and overall user interface have been enhanced with a new look, feel, and fresh color theme. We call it the Enhanced Experience. It modernizes and expands the Classic Experience that has defined your embedded analytics experience.

The home page updates bring together changes that make it easier for users to access sources, visuals, libraries, and administrative features.

The main menu has been reimagined, so your users and administrators can quickly access the features, information, tenants, or other tools they need.

For more information, see [Home Page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page) and [The Main Menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Main-Menu).

Which interface will I see when I implement 26.2?

No matter your transition path, when implement v26.2 in your environment, your custom theme is honored. When you are ready to stage and then roll out the layout changes to your users, enable the `enhanced-experience` toggle. See [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables).

* **The Enhanced Experience** If you are transitioning from Symphony 26.1 or earlier, you will see the enhanced experience layout and colors you are already using.
* **The Classic Experience** If this is a fresh installation of v26.2 in your environment, you will see the classic experience layout and [default **composer** color theme](#Supplied "default composer color theme"). Enable the `enhanced-experience` toggle in your staging environment to try it out, then roll it out to your users.
* **The Classic Experience** If you are transitioning from Composer 26.1 or earlier and using any [previous color theme](#Supplied "previous color theme") (**composer**, **modern**, **dark**), you will see the classic experience layout and composer color theme. Enable the `enhanced-experience` toggle in your staging environment to try it out, then roll it out to your users.
* **The Classic Experience** If you are transitioning from Composer 26.1 or earlier and using a custom color theme, you will see the classic experience layout with your colors. Enable the `enhanced-experience` toggle in your staging environment to see what it looks like. You will need to [add information to your existing color theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210155405-Themes-JSON-File#Update "add information to your existing color theme") to expand it to include the new user interface elements before you roll it out to your users. See [User Interface Themes: v26.2 and Later](#User2) and [Themes and UI Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077251302669-Themes-and-UI-Updates).

**Caution:** Update your custom theme and enable the `enhanced-experience` toggle before upgrading past version 26.2. The enhanced homepage and navigation will become the standard experience for all users in the near future. We recommend making these updates now to ensure a smooth transition.

### Supplied Themes

When you install or upgrade to version 26.2 or later, five themes are provided. You can switch to (activate) a different theme when needed using the provided API.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

* Two of these themes fully support color and customization for environments that enable the `enhanced-experience` user interface toggle: `d+a_light` and `__platform__` (for environments [transitioning from Symphony](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968228172557-Transitioning-for-Symphony-and-Composer-Users) that previously used the platform theme).
* Three themes support the classic experience from earlier releases: **composer**, **modern** (light) and **dark**. The **composer** theme is used by default in v26.2 and earlier releases when you install v26.2 or upgrade to v26.2 to ease the transition.

**Caution:** Update your custom theme and enable the `enhanced-experience` toggle before upgrading past version 26.2. The enhanced homepage and navigation will become the standard experience for all users in the near future. We recommend making these updates now to ensure a smooth transition.

### User Interface Interaction With Themes

The `d+a_light` and `__platform__` themes have definitions for the full range of user interface changes introduced when you enable the `enhanced-experience` toggle.

You will need expand and update your classic theme colors to accommodate the new interface objects.

![This chart explains that  classic composer themes do not have info to handle UI elements such as home and left navigation](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48527894439053 "Chart detailing what each theme type covers")

Additional information about themes can be found here:

* [Themes and UI Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077251302669-Themes-and-UI-Updates)
* [Themes API Endpoint](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163688205-Themes-API-Endpoint)
* [List Themes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701166457613-List-Themes)
* [Create a Theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163712141-Create-a-Theme)
* [Review and Download the Theme JSON Code](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210283277-Review-and-Download-the-Theme-JSON-Code)
* [Activate a Theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701176469261-Activate-a-Theme)
* [Update a Theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701166643213-Update-a-Theme)
* [Patch a Theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163854733-Patch-a-Theme)
* [Delete a Theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163742861-Delete-a-Theme)
* [Themes JSON File](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210155405-Themes-JSON-File)

## User Interface Themes: Earlier Releases

### Supplied Themes

When Composer is installed, three themes are provided: **composer**, **modern** (light) and **dark**. The **composer** theme is used by default. You can switch to (activate) a different theme when needed.

See [Activate a Theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701176469261-Activate-a-Theme).

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.
