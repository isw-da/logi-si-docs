---
title: "Edit a Hierarchical Source"
id: 43701096930061
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701096930061-Edit-a-Hierarchical-Source
updated_at: 2026-05-29T14:11:05Z
---

# Edit a Hierarchical Source

# Edit a Hierarchical Source

**Note:** 
Hierarchical fields are enabled by default at the server level. Work with [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) to disable.

You can edit an existing source to pair a facts table and at least one lookup table to use hierarchical data.

**Edit a source**

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. Select **Sources** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243276387981)) or the [top-level navigation menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). The [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page appears.
3. On the [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page, select a source to edit. The [Source Creation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab) work area opens.
4. In this example, the existing data entity is the fact table. Select **Add** to add a data entity to use as a hierarchical lookup table.
5. Select **Add** in the Join Definition work area to connect the hierarchy lookup table to the facts table.
6. If only one hierarchy is used, we recommend you use a left join from a hierarchy lookup table to a facts table.

   * Select a left join to preserve the contents and structure of the hierarchical tree, regardless of the contents of the facts table.
   * If you select an inner join, the hierarchy is limited to data in the facts table. This may break your hierarchy structure, separating nested items from parents, making the nest items top-level items.

     **Note:** You can visualize your joins by selecting the view icon in the Joins work area. See [Visualize Joins](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072201741-Create-a-Fusion-Source#Visualiz).
7. Select **Apply** to create the join, then **Save Source** to save your source.
8. Next, [define a hierarchy field](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701079796493-Define-a-Hierarchy-Field-for-Your-Source) for your source.
