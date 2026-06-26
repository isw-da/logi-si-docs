---
title: "Create a Fusion Source"
id: 34932990526221
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932990526221-Create-a-Fusion-Source
updated_at: 2026-05-26T22:09:28Z
---

# Create a Fusion Source

# Create a Fusion Source

Fusing data in a source in Composer  is very similar to adding other data sources. Add multiple entities to a new or existing source, then use the [Join Definition](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891763981-Source-Creation-Tab#Join) work area to identify and specify the data from those entities you want to join.

For an overview of Composer’s data fusion capability, see [Fuse Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932963181197-Fuse-Data-Sources).

**Important:** 
You must log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or write permission for the source for which you want to create a join.

## Before You Start

Before you attempt to create a fusion source, verify you can access the connections. If not, create them. See [Manage Data Store Connections](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932706697357-Manage-Data-Store-Connections).

**Note:** In this release, the user interface and workflows have changed from previous releases. If you are running an earlier release, see [Configure a Fusion Source (Earlier Releases)](#v25.3).

## Configure a Fusion Source

To create a Fusion source, add multiple data entities to a new or existing source, then use the [Join Definition](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891763981-Source-Creation-Tab#Join) work area to specify the fields and joins included in your fused source.

### Add Joins to a New or Existing Source

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or write permission for the source for which you want to create a join.
2. [Create](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932863719309-Define-a-Source) or [edit](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932890384781-Edit-a-Data-Source) an existing source, adding multiple entities from a [connection](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891763981-Source-Creation-Tab#Connecti) or [file](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891763981-Source-Creation-Tab#Data2). You will only see the connections you have read permission for. See [About Source Permissions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions).

   **Note:** 
   If your source contains multiple data entities, you must use all entities in a join to save the source.
3. To create a new join, select **Joins** to add a join object to your work area.

   ![select to add a joins object to your data source](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167176535309 "Joins button")
4. Select the join object. A **Join Settings** work area opens. Use this to define how the entities use a join type to connect specific fields.

   ![use this area to create and edit joins](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167176711309 "Join Definition work area")
5. Define your entities, join type, and fields.

   **Note:** 
   Ensure you have matching fields across the data sources you are joining.

   * **Entity Left**: Select an available entity from the data entities you defined.
   * **Join Type**: Select Left, Inner, or Full Outer.
   * **Entity Right**: Select an available entity from the data entities you defined.
   * **Enable Dimension Entity**: Select the settings icon to enable dimension for one or both entities. This improves the performance of queries execution by removing unused data entities from the join.
   * **Field Left**: Select at least one field from this entity. You can add multiple fields by selecting the add field icon, or remove fields by selecting the remove icon.
   * **Field Right**: Select at least one field from this entity. You can add multiple fields by selecting the add field icon, or remove fields by selecting the remove icon.
6. Select **Apply** to finish creating the join. Remove joins by selecting the remove icon.

   You can also view the relationships of your joins and add more joins in a visualization. See [Visualize Joins](#Visualiz).
7. After creating your joins, select **Preview Source** to preview your data, or select **Save Source** to save your updated source.
8. As needed, update the default settings on the [Fields tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields), [Cache tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891391629-Cache-Tab), or [Global Settings tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932890843277-Global-Settings-Tab).

### Fields Tab for Fusion Sources

Use the [Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields) tab to manage your fused source data: rename field Labels, add [derived fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932837821709-Create-and-Modify-Derived-Fields), or select the custom metrics tab [add a custom metric](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932813034765-Create-and-Modify-Custom-Metrics). If your fused data sources include duplicate field names, Composer appends a number to the duplicate field name.

### Cache Tab for Fusion Sources

Use the [Cache](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891391629-Cache-Tab) tab to enable or disable caching of aggregated results of queries for this source. See [How Composer Caches Data](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932848587917-How-Composer-Caches-Data).

### Global Settings Tab for Fusion Sources

Use the [Global Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932890843277-Global-Settings-Tab) tab to configure settings for new visuals for this fused source. Not all visual styles are available for Fusion data sources. See [Data Fusion Limitations](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932973239821-Data-Fusion-Limitations).

### Visualize Joins

You can use the provided work area to create joins, or view and create joins in a move visual way.

Zoom in or out in this work area, or use the mini map to navigate among the various tables that make up your joins.

**View or edit a joins for a fused data source**

1. Create or edit a fusion source that uses a join.
2. Select the Preview button in the Joins work area to open a visualization of existing joins.
3. Optionally, draw more joins in this work area, then **Save** your changes. New joins are added to the list of those in Join Settings.

   **Note:** To remove a user-applied join, double-click to select the join, then select the backspace key. The relationship is removed.

**Important:** If you add joins that create one-to-many relationships here, Logi Composer may return an error that prevents use of the data in a visual. For best results, when you create a one-to-many relationship with a specific left entity, any additional joins must refer to that table as the right entity. See [Recommended Joins](#Recs).

**Note:** For Postgres connections, both tables and data relationship information are read from the connection. Other supported connections include table information but do not read relationship information. See [Connector Support for Schema Visualization](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692136845-Visualize-Schemas-and-Joins#support). No information is provided for unsupported connections.

![use this work area to view and edit joins in this source](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167208122509 "Join Visualization work area")

### Recommended Joins

Logi Composer provides some visual guidance for recommended joins. You can add these suggested joins, or create your own.

**Note:** Recommended Joins may present one-to-many or many-to-one relationships that when implemented return an error. You can still implement the recommended joins: when you create a one-to-many relationship with a specific left entity, any additional joins must refer to that table as the right entity.

For example:

![use this work area to navigate among the entities of a specifc join, and to draw relationships between tables](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167194197261 "the visual joins work area")

**Table A** has relationships with **Table B**, **Table C**, and **Table D**.

* After defining a relationship with **Table A** as the left entity, include **Table A** as the right entity in additional joins.
* If you are using the visual interface, position only one of the other tables (**Table B**, **Table C**, or **Table D**) on the left side of **Table A**. Remaining tables should be placed to the right of **Table A**.

## Configure a Fusion Source (Earlier Releases)

To create a Fusion source, add multiple data entities to a new or existing source, then use the [Join Definition](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891763981-Source-Creation-Tab#Join) work area to specify the fields and joins included in your fused source.

### Add Joins to a New or Existing Source

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or write permission for the source for which you want to create a join.
2. Select **Sources** on the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167913171725)). The [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page appears.
3. [Create](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932863719309-Define-a-Source) or [edit](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932890384781-Edit-a-Data-Source) an existing source, adding multiple entities [From Connection](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932863719309-Define-a-Source) or [From File](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads). You will only see the connections you have read permission for. See [About Source Permissions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions).

   **Note:** 
   If your source contains multiple data entities, you must use all entities in a join to save the source.
4. Select **Add** in the **Join Definition** work area. A Join work area opens.

   ![use this work area to create, edit, and visualize your data joins](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167177200141 "Jon Definition work area")
5. Define your entities, join type, and fields.

   **Note:** 
   Ensure you have matching fields across the data sources you are joining.

   * **Entity Left**: Select an available entity from the data entities you defined.
   * **Join Type**: Select Left, Inner, or Full Outer.
   * **Entity Right**: Select an available entity from the data entities you defined.
   * **Enable Dimension Entity**: Select the settings icon to enable dimension for one or both entities. This improves the performance of queries execution by removing unused data entities from the join.

     ![use this work area to remove unused data entities to improve query execution performance](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167208585741 "Enable Dimension Entity work area")
   * **Field Left**: Select at least one field from this entity. You can add multiple fields by selecting the add field ![add icon](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167868390541 "add icon") icon, or remove fields by selecting the remove ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167913175309) icon.
   * **Field Right**: Select at least one field from this entity. You can add multiple fields by selecting the add field ![add icon](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167868390541 "add icon") icon, or remove fields by selecting the remove ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167913175309) icon.

     ![use this work area to create, edit, and visualize your data joins](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167208751117 "Join Settings work area")
6. Select **Apply** to finish creating the join. Composer names the join and adds it to the Joins list. Remove joins by selecting the remove ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167913175309) icon.

   You can also view the relationships of your joins and add more joins in a visualization. See [Visualize Joins](#Visualiz).
7. After creating your joins, select **Preview Source** to preview your data, or select **Save Source** to save your updated source.
8. As needed, update the default settings on the [Fields tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields), [Cache tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891391629-Cache-Tab), or [Global Settings tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932890843277-Global-Settings-Tab).

### Fields Tab for Fusion Sources

Use the [Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields) tab to manage your fused source data: rename field Labels, add [derived fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932837821709-Create-and-Modify-Derived-Fields), or select the custom metrics tab [add a custom metric](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932813034765-Create-and-Modify-Custom-Metrics). If your fused data sources include duplicate field names, Composer appends a number to the duplicate field name.

### Cache Tab for Fusion Sources

Use the [Cache](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891391629-Cache-Tab) tab to enable or disable caching of aggregated results of queries for this source. See [How Composer Caches Data](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932848587917-How-Composer-Caches-Data).

### Global Settings Tab for Fusion Sources

Use the [Global Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932890843277-Global-Settings-Tab) tab to configure settings for new visuals for this fused source. Not all visual styles are available for Fusion data sources. See [Data Fusion Limitations](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932973239821-Data-Fusion-Limitations).

### Visualize Joins

You can use the provided work area to create joins, or view and create joins in a move visual way.

Zoom in or out in this work area, or use the mini map to navigate among the various tables that make up your joins.

**View or edit a joins for a fused data source**

1. Create or edit a fusion source that uses a join.
2. Select the view icon in the Joins work area to open a visualization of existing joins.
3. Optionally, draw more joins in this work area, then **Save** your changes. New joins are added to the list of those in Join Settings.

   **Note:** To remove a user-applied join, double-click to select the join, then select the backspace key. The relationship is removed.

**Important:** If you add joins that create one-to-many relationships here, Logi Composer may return an error that prevents use of the data in a visual. For best results, when you create a one-to-many relationship with a specific left entity, any additional joins must refer to that table as the right entity. See [Recommended Joins](#Recs).

**Note:** For Postgres connections, both tables and data relationship information are read from the connection. Other supported connections include table information but do not read relationship information. See [Connector Support for Schema Visualization](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692136845-Visualize-Schemas-and-Joins#support). No information is provided for unsupported connections.

![use this work area to view and edit joins in this source](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167177678733 "Join Visualization work area")

### Recommended Joins

Logi Composer provides some visual guidance for recommended joins. You can add these suggested joins, or create your own.

**Note:** Recommended Joins may present one-to-many or many-to-one relationships that when implemented return an error. You can still implement the recommended joins: when you create a one-to-many relationship with a specific left entity, any additional joins must refer to that table as the right entity.

For example:

![use this work area to navigate among the entities of a specifc join, and to draw relationships between tables](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167194197261 "the visual joins work area")

**Table A** has relationships with **Table B**, **Table C**, and **Table D**.

* After defining a relationship with **Table A** as the left entity, include **Table A** as the right entity in additional joins.
* If you are using the visual interface, position only one of the other tables (**Table B**, **Table C**, or **Table D**) on the left side of **Table A**. Remaining tables should be placed to the right of **Table A**.
