---
title: "Use the Visual Menu"
id: 4405851254295
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu
updated_at: 2021-09-21T01:30:30Z
---

# Use the Visual Menu

# Use the Visual Menu

Composer's visual canvas provides a comprehensive suite of tools to help you tailor visuals quickly so they provide the information you need in the best way for you to analyze your data. These tools are available from the visual drop-down menu or from the [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu). This topic discusses the drop-down menu.

The visual drop-down menu lists options that help you modify and use your visuals more effectively. It is accessed by selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4406743718551/three-dots-menu_19x11.png) in the upper right corner of a visual .

The menu options are described in the following table. Some options are only available for specific visual styles. Some options are available when you are working with a visual in a dashboard and are not available when you are working with a visual in the Visual Gallery. Controls for some of these options are available on the interactivity sidebar. See [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual).

The list of options available on an embedded [visual's drop-down menu](#) depends on:

* The mode setting for the dashboard. If the embed mode is [`readonly` or](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects) [**Read Only**](https://devnet.logianalytics.com/hc/en-us/articles/4405859339543-Generate-an-Embeddable-Dashboard-HTML-Snippet), no menu is available at all.
* The [visual interactivity settings](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual) specified in the visual definition.
* The [dashboard interactivity settings](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard) specified for the dashboard, if those settings include override interactivity settings for all visuals in the dashboard.

When options are shown for a visual in an embedded dashboard, they may be shown in the [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) or within the [visual drop-down menu](#) itself, depending on the setting of the [`editor.placement`](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects) property.

* If [`editor.placement`](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects) is set to `dockRight`, the options appear in sidebars using the [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) and the resulting sidebar editing panels.

  If [`editor.placement`](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects) is set to `modals`, the options appear in the [visual drop-down menu](#) itself and the resulting floating dialogs.

| Option | Description |
| --- | --- |
| Actions | Invoke an action if an action template has been enabled for the visual's data source. See [*Invoke an Action*](https://devnet.logianalytics.com/hc/en-us/articles/4405850869911-Invoke-an-Action). |
| Copy Visual | Copy a visual. See [*Copy Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405859567895-Copy-Visuals). |
| Create Keyset | Create a keyset from the visual data. See [*Create a Keyset*](https://devnet.logianalytics.com/hc/en-us/articles/4405851103255-Create-a-Keyset). |
| Edit Visual | Opens the sidebar menu for a visual. See [*Use the Visual Sidebar Menu*](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu). |
| Export | Export a visual or visual data. See [*Export Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405851255191-Export-Visuals). |
| Maximize | Maximize a visual on the dashboard for optimal viewing. |
| Minimize | Minimize a visual so you can see other visuals on the dashboard. |
| Permissions | Quickly allows you to update the user, group, and account permissions for the visual. The Visual Permissions dialog appears. See [*About Visual Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851253271-About-Visual-Permissions). You can only see this option if your user account has been granted the **Can Manage Visual Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference). |
| Remove Visual | Remove a visual from the dashboard. This will not delete the visual from Composer. For more information, see [*Delete and Remove Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405859569047-Delete-and-Remove-Visuals). |
| Save As | Save the visual with a new name. See [*Save Visuals With New Names*](https://devnet.logianalytics.com/hc/en-us/articles/4405859575447-Save-Visuals-With-New-Names). |
