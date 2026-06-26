---
title: "Edit a Hierarchical Source"
id: 34932885881741
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932885881741-Edit-a-Hierarchical-Source
updated_at: 2026-05-26T22:09:46Z
---

# Edit a Hierarchical Source

# Edit a Hierarchical Source

**Note:** 
Hierarchical fields are enabled by default at the server level. Work with [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) to disable.

You can edit an existing source to pair a facts table and at least one lookup table to use hierarchical data.

**Edit a source**

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).
2. Select **Sources** on the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167929272333)) or the [top-level navigation menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933063528717-Home-Page). The [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page appears.
3. On the [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page, select a source to edit. The [Source Creation](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891763981-Source-Creation-Tab) work area opens.
4. In this example, the existing data entity is the fact table. Select **Add** to add a data entity to use as a hierarchical lookup table.
5. Select **Add** in the Join Definition work area to connect the hierarchy lookup table to the facts table.
6. If only one hierarchy is used, we recommend you use a left join from a hierarchy lookup table to a facts table.

   * Select a left join to preserve the contents and structure of the hierarchical tree, regardless of the contents of the facts table.
   * If you select an inner join, the hierarchy is limited to data in the facts table. This may break your hierarchy structure, separating nested items from parents, making the nest items top-level items.

     **Note:** You can visualize your joins by selecting the view icon in the Joins work area. See [Visualize Joins](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932990526221-Create-a-Fusion-Source#Visualiz).
7. Select **Apply** to create the join, then **Save Source** to save your source.
8. Next, [define a hierarchy field](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932871949581-Define-a-Hierarchy-Field-for-Your-Source) for your source.
