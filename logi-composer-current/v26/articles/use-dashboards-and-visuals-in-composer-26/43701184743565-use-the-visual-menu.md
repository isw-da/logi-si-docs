---
title: "Use the Visual Menu"
id: 43701184743565
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu
updated_at: 2026-05-29T14:09:58Z
---

# Use the Visual Menu

# Use the Visual Menu

Composer's visual canvas provides a comprehensive suite of tools to help you tailor visuals quickly so they provide the information you need in the best way for you to analyze your data. These tools are available from the visual drop-down menu or from the [visual sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu). This topic discusses the drop-down menu.

The visual drop-down menu lists options that help you modify and use your visuals more effectively. Access by selecting the Visual Menu, labeled as the Show more menu (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243133059085)) icon in the upper right corner of a visual.

The menu options are described in the following table. Some options are only available for specific visual styles. Some options are available when you are working with a visual in a dashboard and are not available when you are working with a visual in the Visual Gallery. Controls for some of these options are available on the interactivity sidebar. See [Control How Users Interact With a Visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701185104653-Control-How-Users-Interact-With-a-Visual).

The list of options available on an embedded [visual's drop-down menu](#) depends on:

* The mode setting for the dashboard. If the embed mode is [`readonly` or](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070345997-Embedded-Dashboard-Properties-and-Objects) [**Read Only**](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081719053-Generate-an-Embeddable-Dashboard-HTML-Snippet), no menu is available at all.
* The [visual interactivity settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701185104653-Control-How-Users-Interact-With-a-Visual) specified in the visual definition.
* The [dashboard interactivity settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076696717-Control-How-Users-Interact-With-a-Dashboard) specified for the dashboard, if those settings include override interactivity settings for all visuals in the dashboard.

When options are shown for a visual in an embedded dashboard, they may be shown in the [visual sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) or within the [visual drop-down menu](#) itself, depending on the setting of the [`editor.placement`](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070345997-Embedded-Dashboard-Properties-and-Objects) property.

* If [`editor.placement`](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070345997-Embedded-Dashboard-Properties-and-Objects) is set to `dockRight`, the options appear in sidebars using the [visual sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) and the resulting sidebar editing panels.

  If [`editor.placement`](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070345997-Embedded-Dashboard-Properties-and-Objects) is set to `modals`, the options appear in the [visual drop-down menu](#) itself and the resulting floating dialogs.

| Option | Description |
| --- | --- |
| Add to Visual Gallery | Add a local visual to the Visual Gallery.  See [Convert Visual Gallery Visuals and Local Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214385933-Convert-Visual-Gallery-Visuals-and-Local-Visuals). |
| Actions | Invoke an action if an action template has been enabled for the visual's data source.  See [Invoke an Action](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700988347533-Invoke-an-Action). |
| Convert to Local | Make a copy of a visual gallery visual as a local visual on the dashboard.  See [Convert Visual Gallery Visuals and Local Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214385933-Convert-Visual-Gallery-Visuals-and-Local-Visuals). |
| Copy Visual | Copy a visual.  See [Copy Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184709901-Copy-Visuals). |
| Create Keyset | Create a keyset from the visual data.  See [Create a Keyset](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135635213-Create-a-Keyset). |
| Create Alert | Create an alert from the visual data for this dashboard.  See [Create an Alert Definition](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036492941-Create-an-Alert-Definition). |
| Describe Visual | Generate a description of the visual, for most visual types.   * Select **Copy Visual Summary** to copy it to your device's clipboard; paste it where you need. * Select **Create Snippet and Insert** to generate the visual's summary in a new [rich text snippet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701209714957-Add-Rich-Text-Snippets-to-a-Dashboard#DescVisual), ready to edit. * Select **Insert into [Existing Snippet Name]** to insert it into an existing rich text snippet.  **Note:** If more than one rich text snippet widget exists, you can select the appropriate snippet from a list. |
| Export | Export a visual or visual data.  See [Export Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214516365-Export-Visuals). |
| Maximize | Maximize a visual on the dashboard for optimal viewing. |
| Minimize | Minimize a visual so you can see other visuals on the dashboard. |
| Permissions | Quickly allows you to update the user, group, and account permissions for the visual. The Visual Permissions dialog appears. See [About Visual Permissions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184646285-About-Visual-Permissions).  You can only see this option if your user account has been granted the **Manage Visual Permissions** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference). |
| Remove Widget | Remove a visual from the dashboard. This will delete local visuals, but will not delete visual gallery visuals from Composer.  For more information, see [Delete and Remove Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701132460301-Delete-and-Remove-Visuals). |
| Save As | Save the visual with a new name.  See [Save Visuals With New Names](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214932109-Save-Visuals-With-New-Names). |
| Settings | Opens the sidebar menu for a visual.  See [Use the Visual Sidebar Menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu). Formerly Edit. |
| Undo | Undo a change you made to the visual.  See [Undo a Visual Action](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184401549-Undo-a-Visual-Action). |
