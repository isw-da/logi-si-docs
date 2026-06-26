---
title: "Use the Visual Gallery"
id: 43701180261773
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701180261773-Use-the-Visual-Gallery
updated_at: 2026-05-29T14:09:56Z
---

# Use the Visual Gallery

# Use the Visual Gallery

Use the Visual Gallery to manage the visuals defined in a Composer instance and shared with other users.

You must be logged in as a user in a group with the **Administer Visuals** privilege to see the Visual Gallery. Read, write, and delete permissions for a visual gallery visual are controlled by the permissions assigned the data source used by the visual in combination with the user's group [privileges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).

As creator and owner of a visual, you are automatically granted read, write, and delete for the visual in the Visual Gallery. When you remove a user who has created visuals from the system, items created by that user are retained.

**Note:** 
Local visuals exist only on the dashboard on which they were created. Convert to a Visual Gallery visual and add to the Visual Gallery at any time. Visual gallery visuals can be converted to a local visual at any time. See [Convert Visual Gallery Visuals and Local Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214385933-Convert-Visual-Gallery-Visuals-and-Local-Visuals).

## Access the Visual Gallery

To access the visual gallery, log in as an administrator or as a user with the **Administer Visuals** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference). Select **Visual Gallery** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242226053517)) or the [top-level navigation menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner), or select the **Visuals** box on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). The Visuals page appears, and visuals are listed in a table format.

![use this work area to manage your visuals](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242240140941 "visual gallery with visuals listed")

**Note:** 
You can select and open a visual in the visual gallery to make a copy of a visual if needed. See [Copy Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184709901-Copy-Visuals).

## Search Field

Use the search field to filter the visuals shown by visual Type, Name, Description, Data Source, or Author. For example, if you type a **C** in the search box, only visuals that include the letter *C* in the selected field searched (or all fields if All is selected) are shown in the working area. See [Search and Filter Lists](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008213517-Search-and-Filter-Lists).

## Buttons

The buttons on the page allow easy access to saved visuals, as well as other visuals created by other users in your Composer environment. They also allow you to create a new visual and filter the visuals shown.

| Button | Description |
| --- | --- |
| All | Removes any filters for the visual gallery and displays all visuals you can access within your Composer environment. |
|  | Displays only the visuals that you have marked as favorites. |
|  | Displays only visuals that you created and saved. Visuals created and saved by other users are hidden. |
|  | Displays only the visuals that other users shared with you.  See [Grant Permissions for a Visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701199414925-Grant-Permissions-for-a-Visual). |
|  | Select to generate an embeddable visual link.  See [Generate a Visual Gallery HTML Snippet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701086397581-Generate-a-Visual-Gallery-HTML-Snippet). |
| **Export Selected Items** | Select to export multiple selected items.  See [Export Visual Gallery Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184939533-Export-Visual-Gallery-Visuals). |
| **Import Visual** | Select to import one or more visuals.  See [Import Visual Gallery Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214789517-Import-Visual-Gallery-Visuals). |
| **Create Visual** | Select to create a new visual. See [Create and Add Visuals to the Visual Gallery](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701179894541-Create-and-Add-Visuals-to-the-Visual-Gallery). |

## The Visual Gallery List

Each column in the table is described below. Several of these columns can be used to sort the list: select the column header to sort first to last and again to sort last to first. You can search for items by the contents of several columns. See [Search and Filter Lists](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008213517-Search-and-Filter-Lists).

| Column | Description |
| --- | --- |
| Select (not labeled) | Select one or more items to perform bulk actions, such as export, for your resources. |
| Fav | Identifies favorite visuals using a star icon. If the star is colored (), the visual is a favorite. If the star is empty (), the visual is not a favorite. |
| Type | An icon identifying the visual type (style) of the visual in the visual.  See [Composer Visual Metrics and Attributes Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115864205-Composer-Visual-Metrics-and-Attributes-Reference) to see all the possibilities. |
| Name | The name assigned to the visual. The visual name is not necessarily the same as the display name.  See [Visual Names and Display Names](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214877197-Visual-Names-and-Display-Names) for more information about how visual names and display names are set. |
| Description (not labeled) | The description icon is visible if a description associated with a visual. You can search for a visual by the contents of this field. |
| Tags | Content tags applied to the visual. Select the filter icon to open a drop-down list and select tags to filter your list or to [narrow your search results](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008213517-Search-and-Filter-Lists#Filter). If several tags are associated with an item, hover over the ellipsis to see all tags for this resource. |
| Data Source | The name of the data source used by the visual. If a user doesn't have permission to view the data source, this field is blank. |
| Author | The name of the user who defined the visual. |
| Modified Date | The time stamp indicating when the visual was last modified. |
| Permissions | Assign and manage the permissions for a visual. Visible if you are logged in as a user with the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or as a user with the **Manage Source Permissions** privilege. |
| Actions | Delete a visual if you have delete permissions. Before you delete a visual, you must remove it from all the dashboards that use it.  See [Delete and Remove Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701132460301-Delete-and-Remove-Visuals). |
