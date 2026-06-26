---
title: "Define a Hierarchical Source"
id: 34932885575053
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932885575053-Define-a-Hierarchical-Source
updated_at: 2026-05-26T22:09:44Z
---

# Define a Hierarchical Source

# Define a Hierarchical Source

**Note:** 
Hierarchical fields are enabled by default at the server level. Work with [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) to disable.

Create or edit a source to include a facts table and at least one lookup table to create your hierarchical source.

## Define a New Hierarchical Source

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).
2. Select **Sources** on the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167939586573)) or the [top-level navigation menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933063528717-Home-Page) The [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page appears.
3. On the [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page, select the **Create Source** button. The [Source Creation](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891763981-Source-Creation-Tab) work area opens.
4. Name your source, then add the first data entity, including appropriate connection, schema, and entity options or Custom SQL.

   **Note:** 

   The first data entity can be, but does not have to be, the facts table.
5. Add the second data entity, your hierarchy lookup table, including appropriate connection, schema, and entity options or Custom SQL.
6. Select **Add** in the Join Definition work area to connect the hierarchy lookup table to the facts table.
7. If only one hierarchy is used, we recommend you use a left join from a hierarchy lookup table to a facts table. To configure multiple hierarchical tables on a single source, contact [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support).

   * Select a left join to preserve the contents and structure of the hierarchical tree, regardless of the contents of the facts table.
   * If you select an inner join, the hierarchy is limited to data in the facts table. This may break your hierarchy structure, separating nested items from parents, making the nest items top-level items.

     **Note:** You can visualize your joins by selecting the view icon in the Joins work area. See [Visualize Joins](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932990526221-Create-a-Fusion-Source#Visualiz).
8. Select **Apply** to create the join, then **Save Source** to save your source.

Next, define a hierarchy field for your source. See[Define a Hierarchy Field for Your Source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932871949581-Define-a-Hierarchy-Field-for-Your-Source).
