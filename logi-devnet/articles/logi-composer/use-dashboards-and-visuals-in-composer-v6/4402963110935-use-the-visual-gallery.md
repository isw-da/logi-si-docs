---
title: "Use the Visual Gallery"
id: 4402963110935
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963110935-Use-the-Visual-Gallery
updated_at: 2021-08-07T17:32:26Z
---

# Use the Visual Gallery

# Use the Visual Gallery

The Visual Gallery can be used to manage the visuals defined in a Composer instance.

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) To see the Visual Gallery, you must be logged in as an administrator or as a user in a group with the **Can Administer Visuals** privilege. Read, write, and delete permissions for a visual are controlled by the permissions assigned the data source used by the visual in combination with the user's group [privileges](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference). The creator of a visual is automatically granted read, write, and delete for the visual in the Visual Gallery. When they are removed from the system, the supervisor is assigned ownership for the visual.

![](https://devnet.logianalytics.com/hc/article_attachments/4404952782231/visual-gallery_576x243.png)

The Visual Gallery page includes the following features:

1. The ![](https://devnet.logianalytics.com/hc/article_attachments/4404952783511/add-visual-btn.png) button allows you to add a new visual to the Visual Gallery if you have the **Can Create Visuals** or **Can Administer Visuals**[group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference). See [*Add Visuals to the Visual Gallery*](https://devnet.logianalytics.com/hc/en-us/articles/4402955727639-Add-Visuals-to-the-Visual-Gallery).
2. The table lists and allows you to maintain your previously defined visuals. You can add edit and delete visuals in this table.
3. A search bar at the top of the page that you can use to search for a visual in the table.

To access the Visual Gallery:

1. Log into Composer as an administrator or as a user with the **Can Administer Visuals**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference).
2. Select **Visual Gallery** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4402963040407-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4404952783767/hamburger.png)) or the [top-level navigation menu](https://devnet.logianalytics.com/hc/en-us/articles/4402963039639-The-Top-Level-Navigation-Banner), or select the **Visuals** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4402963020951-Home-Page). The Visuals page appears.

You can edit and delete visuals listed in the table on the Visuals page. If there are many visuals listed, you may need to search for the visual you need. Use the search bar to search for a visual in the list. See [Search for a Definition in a List](https://devnet.logianalytics.com/hc/en-us/articles/4402955458455-Search-for-a-Definition-in-a-List).

Each column in the table is described below. The Type, Name, Author, and Modified Date columns are sortable.

| Column | Description |
| --- | --- |
| Type | An icon identifying the visual type (style) of the visual in the visual. See [*Composer Visual Metrics and Attributes Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4402955650583-Composer-Visual-Metrics-and-Attributes-Reference) to see all the possibilities. |
| Name | The name assigned the visual. The visual name is not necessarily the same as the visual name. See [*Understand Visual Names and Titles*](https://devnet.logianalytics.com/hc/en-us/articles/4402963111959-Understand-Visual-Names-and-Titles) for more information about how visual names are set. |
| Author | The name of the user who defined the visual. |
| Usage | The number of times the visual is used in dashboards. If this count is not zero, you cannot delete a visual from the Visual Gallery. |
| Modified Date | The time stamp when the visual definition was last modified. |
| Actions | The  button in this column allows you to delete a visual. Before you delete a visual, you must delete it from all the dashboards that use it. If the Usage column for a visual is not zero, the  button is disabled. See [*Delete and Remove Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4402963109143-Delete-and-Remove-Visuals). |
