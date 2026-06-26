---
title: "Source Creation Tab"
id: 43701080568205
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab
updated_at: 2026-05-29T14:10:59Z
---

# Source Creation Tab

# Source Creation Tab

Use the Source Creation tab in the Sources work area to define new sources, edit sources, and define the data entity or entities that make up your source.

**Note:** In this release, the user interface and workflows have changed from previous releases. If you are running an earlier release, see [Source Creation Tab (Earlier Releases)](#v25.3).

## Source Creation Tab

If you are upgrading from an earlier version of Composer, you may temporarily see the earlier interface until you create, edit, or update a source. See [Source Creation Tab (Earlier Releases)](#v25.3) for interface information.

![Use this work area to create or update a source](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242565593229 "Source Creation work area")

**Note:** 
You must be logged in as user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) to see the Source Creation tab, or have **Read** and **Write** permissions on the source.

**Note:** 
When you upload a flat file, Select Schema and Select Entity fields are not present, and the option to create Custom SQL is not available. You can instead Select File, Edit File, and configure API Endpoints.

The general structure of the Source Creation tab includes:

* Edit and update the name of this source in the top left the work area.
* Export, Preview, Copy, or Save the source using the available icons in the top right of the work area.
* Build your source by dragging one or more entities from you connections or files by dragging and dropping them from the Connections or Files tabs in the right panel to the source work area in the left panel.
* Use the Connections and Files tabs to build your source from available entities, uploaded files, or to add an SQL entity as needed.
* If you add muliple entities, you can manage the Joins directly in the work area.

## Source Work Area (Left Panel)

Drag and drop data entities to build your source. After adding a data entity or making changes, select **Save Source** to save your changes, or **Preview Source** to preview your data.

![drag and drop entities to this left panel source  work area to define one or more data entities for your source](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242583151373 "source work area (left pane)")

### Connections Panel

Available connections are listed in the Connections panel. Select the arrows to open and find entities and indices to drag and drop to the source work area. The added entity is represented visually, making it easier for you to make direct changes or create joins when multiple entitles are included in the source.

![drag and drop your entity and schema to the work area](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242565593229 "drag and drop your entity and schema to the work area")

**Note:** Alternatively, select **Add SQL Entity** to use Custom SQL to define your entities and indices in this source.

**Note:** 
When you create a connection from a flat file, Select Schema and Select Entity fields are not present, and the option to create Custom SQL is not available. You can instead select a file to edit it or configure API Endpoints.

After you've added a data entity, you can keep the applied name (the Entity Name, appended by a number), or change it in the Properties panel.

Optionally, add a filter values entity to provide an alternative source of metadata values. Use these entities in a dynamic override on Filter Values tab in Fields to improve the filter experience of heavy data entities.

### Entity Details - From Connection

Each entity you add is given a unique **Entity Name**, appended by a number. Select an entity to edit its properties in the Properties panel, and manage details of how the information is accessed and presented.

**Note:** 
Depending on the your source, different options are available to define it.

![Use this work area to define your entity, schema, connection, available fields, and more along with caching settings, if available.](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242561337101 "Entity Details Properties Panel")

Details you can define can include:

* **Entity Name**: The unique name for this data entity. By default, a name is generated for the entity name, appended by a number.
* **Select Connection**: Select a connection for this data entity. The connection currently selected is shown, but you can change that. You will only see connections you have access to.
* **Select Schema**: If a Schema is available for your connection, you can select a schema to filter a list of entities for this connection. See [Connector Feature Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992759565-Connector-Feature-Support). Visualize your schema by selecting the view option. See [View Relationships of a Schema in a Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038666125-Visualize-Schemas-and-Joins#View).
* **Select Indices**: ElasticSearch connections support Indices: select one or more to include.

  + **Indice Selection**: Select **Manually** to create a merged list of fields from selected indices, or **Automatically** to select a pattern that automatically selects indices.

    ![Supported connections allow you to use automatic or manual index selection here](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242597668621 "Indec Selection work area")
* **Existing Entity** and **Custom SQL**:

  + Select **Existing Entity** to use an available entity from your source.
  + **Custom SQL**: Select to define a custom SQL to retrieve the data you want from your source. **Select Entity** is not available if you select Custom SQL.
* **Select Entity**: Select an available entity.

  + **Available Fields**: All fields available from this source are included by default. Disable (uncheck) specific fields to exclude them from the source. The fields, when disabled, are not included for your users. If you attempt to remove a field currently in use by a visual or other object, Composer will prevent you from saving your changes to the data source.
  + **Entity Preview** table: Select the Preview icon in the Available Fields work area. This opens an **Entity Preview** dialog pop up. This preview includes all of the fields in the entity (no matter your selections) to help you decide what to include or exclude.

    **Note:** The Preview icon next to the Save Source button opens a Source Preview. This preview only includes what fields you have made available after applying your field selections and saving your work.

    In the example shown here, the **credit\_limit** field is deselected in Available Fields. It is visible in the Entity Preview table, but not the Source Preview table.

    ![Entity Preview includes all fields. Source preview only includes fileds selected for inclusion.](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242594350349 "Entity and Source Preview tables")

Select **Apply** to apply your changes, or add another data entity to [create joins for a Fusion source](#Join "create joins for a Fusion source details").

### Custom SQL

When you select this option, a Custom SQL editing pane opens that you can use to write and run your SQL query. After you have run a successful query, the results populates **Available Fields** and the **Preview** table, and you can **Apply** your changes. You can't save invalid SQL.

Table visuals and Details dialogs display fields in the order they are retrieved from the source. When you create a source using custom SQL, your fields are shown in the order you specify.

**Important:** 
Custom SQL queries are a powerful tool for performing complex data queries. However, be careful when creating custom SQL queries because it is easy to define a heavy query or a query that may overwhelm your database. Use this feature carefully.

![enter the custom SQL for your entity](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242610742413 "Entity Details work area")

**Note:** Use the grab bars at the corner of the editing field to expand your viewable area.

Variables (specified as custom user attributes) can be inserted in custom SQL. See [Specify Custom User Attributes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051547533-Specify-Custom-User-Attributes). In addition, you can use a vertical bar (|) in the SQL to separate the custom attribute name from a default value used for user definitions that do not have the custom user attribute defined. For example, the following custom SQL uses the value of the `state` customer user attribute to filter source data for records from whatever state the user's `state` custom user attribute is set to. If a `state` custom user attribute is not defined for a user, a default of Alabama is used.

SELECT \* FROM Orders WHERE state = '${User.state|Alabama}'

### Data Entity Details - From File

Each entity you add is given a unique **Entity Name**, appended by a number. Select an entity to edit its properties in the Properties panel, and manage details of how the information is accessed and presented.

![edit and manage data provided from a file](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242583794573 "Data Entity Details work area")

When you select a File to use for your data source, the details you can define can include:

* **Entity Name** - The unique name for this data entity. By default, a name is generated for the entity name, appended by a number.
* **Select File**: Select an available uploaded file for this data entity. A list of all native fields from this entity populates **Available Fields** and the **Preview** table. Use **Upload New File** to add files to this source. See [Manage File Uploads](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads).
* **[API Endpoints](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads)**: Select for more information about appending data, replacing data, or deleting data from your file upload.
* **Edit File**: Select to edit the **File Details** of your uploaded file.

Select **Apply** to apply your changes, or add another data entity to [create joins for a Fusion source](#Join "create joins for a Fusion source details").

## Join Definition

Create joins between pairs of data entities to create a [Fusion](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072155405-Fuse-Data-Sources) source. You must have at least two data entities in source to create a join. If you have more than one data entity in your source, all entities must be used in a join.

To create a new join, select **Joins** to add a join object to your work area.

![select to add a joins object to your data source](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243224802061 "Joins button")

Select the join object to define how the entities use a join type to connect specific fields. Select **Apply** to finish creating the join.

![use this area to create and edit joins](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243224803981 "Join Definition work area")

When you create a join, settings you can define can include:

* **Entity Left**: Select an available entity from the data entities you defined.
* **Join Type**: Select Left, Inner, or Full Outer.
* **Entity Right**: Select an available entity from the data entities you defined.
* **Enable Dimension Entity**: Select the settings icon to enable dimensions for one or both entities. This improves the performance of queries execution by removing unused data entities from the join.
* **Field Left**: Select at least one field from this entity. You can add multiple fields by selecting the add field button.
* **Field Right**: Select at least one field from this entity. You can add multiple fields by selecting the add field button.

You can also view the relationships of your joins and add more joins in a visualization. See [Create a Fusion Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072201741-Create-a-Fusion-Source).

## Source Creation Tab (Earlier Releases)

![Use this work area to create or update a source](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242583935117 "Source Creation work area")

**Note:** 
You must be logged in as user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) to see the Source Creation tab, or have **Read** and **Write** permissions on the source.

**Note:** 
When you upload a flat file, Select Schema and Select Entity fields are not present, and the option to create Custom SQL is not available. You can instead Select File, Edit File, and configure API Endpoints.

The general structure of this tab includes:

* In the upper portion of the tab, you can edit and update the Name and Description of this source in the **[Source Definition](#Source)** work area.
* In the lower portion of the tab, you can add and manage data entities in the **[Source Definition](#Source)** work area.
* In the bottom portion of the tab, you can manage Joins and Join Settings. The **[Join Definition](#Join)** work area is visible after you've added multiple data entities to create a Fusion source.

## Source Creation Tab

Define basic information about this source.

![update source definition information in this section of the work area](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242562157965 "Source Creation work tab")

## Source Definition

Add and edit the unique **Name** and optional **Description** of your source.

## Data Entity Definition

Add and edit data entities for this source. After adding a data entity or making changes, select **Save Source** to save your changes, or **Preview Source** to preview your data.

![use this work area to define one or more data entities to create your source](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242595076365 "Data Entity Definition work area")

### Entities

Select **Add** to add a new data entity from a connection or an uploaded file.

* Select **From Connection** to add a data entity from an existing source.
* Select **From File** to add a data entity from a file.

After you've entered a data entity, you can add a filter values entity to provide an alternative source of metadata values. Use these entities in a dynamic override on Filter Values tab in Fields to improve the filter experience of heavy data entities.

### Entity Details - From Connection

Define a unique **Data Entity Name**, then define the details for how the information is accessed and presented.

**Note:** 
Depending on the your source, different options are available to define it.

When you select **From Connection**, details you can define can include:

* **Entity Name** - The unique name for this data entity.
* **Select Connection**: Select a connection for this data entity. You will only see connections you have access to.
* **Select Schema**: If a Schema is available for your connection, you can select a schema to filter a list of entities for this connection. See [Connector Feature Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992759565-Connector-Feature-Support). Visualize your schema by selecting the view option. See [View Relationships of a Schema in a Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038666125-Visualize-Schemas-and-Joins#View).
* **Select Indices**: ElasticSearch connections support Indices: select one or more to include.

  + **Indice Selection**: Select **Manually** to create a merged list of fields from selected indices, or **Automatically** to select a pattern that automatically selects indices.

    ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242566927117)
* **Existing Entity** and **Custom SQL**:

  + Select **Existing Entity** to use an available entity from your source.
  + **Custom SQL**: Select to define a custom SQL to retrieve the data you want from your source. **Select Entity** is not available if you select Custom SQL.
* **Select Entity**: Select an available entity. A list of all native fields from this entity populates **Available Fields** and the **Preview** table.

  + **Available Fields**: All fields available from this source are included by default. Disable (uncheck) specific fields to exclude them from the source. The fields, when disabled, are not included in any work areas of the source. If you attempt to remove a field in use by a visual or other object, Composer will prevent you from saving your changes to the source configuration.
  + Data Entity **Preview** table: A preview of the data from the source for all fields, even if deselected in **Available Fields**.
  + Source **Preview** table: A preview of data from the source as defined in **Available Fields**. Select **Preview Source** to preview your selected data.

    In the example shown here, the **date** field is deselected in Available Fields. It is visible in the Data Entity Preview table, but not the Source Preview table.

    ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242595326861)

Select **Apply** to apply your changes, or add another data entity to [create joins for a Fusion source](#Join "create joins for a Fusion source details").

### Custom SQL

When you select this option, a Custom SQL editing pane opens that you can use to write and run your SQL query. After you have run a successful query, the results populates **Available Fields** and the **Preview** table, and you can **Apply** your changes. You can't save invalid SQL.

Table visuals and Details dialogs display fields in the order they are retrieved from the source. When you create a source using custom SQL, your fields are shown in the order you specify.

**Important:** 
Custom SQL queries are a powerful tool for performing complex data queries. However, be careful when creating custom SQL queries because it is easy to define a heavy query or a query that may overwhelm your database. Use this feature carefully.

![enter the custom SQL for your entity](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242611655053 "Data Entity Definition work area")

Variables (specified as custom user attributes) can be inserted in custom SQL. See [Specify Custom User Attributes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051547533-Specify-Custom-User-Attributes). In addition, you can use a vertical bar (|) in the SQL to separate the custom attribute name from a default value used for user definitions that do not have the custom user attribute defined. For example, the following custom SQL uses the value of the `state` customer user attribute to filter source data for records from whatever state the user's `state` custom user attribute is set to. If a `state` custom user attribute is not defined for a user, a default of Alabama is used.

SELECT \* FROM Orders WHERE state = '${User.state|Alabama}'

### Data Entity Details - From File

Define a unique **Data Entity Name**, then define the details for how the information is accessed and presented.

![edit and manage data provided from a file](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242613173005 "Data Entity Details work area")

When you select **From File**, details you can define can include:

* **Data Entity Name** - The unique name for this data entity.
* **Select File**: Select an available uploaded file for this data entity. A list of all native fields from this entity populates **Available Fields** and the **Preview** table. Use **Upload New File** to add files to this source. See [Manage File Uploads](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads).
* **[API Endpoints](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads)**: Select for more information about appending data, replacing data, or deleting data from your file upload.
* **Edit File**: Select to edit the **File Details** of your uploaded file.

Select **Apply** to apply your changes, or add another data entity to [create joins for a Fusion source](#Join "create joins for a Fusion source details").

## Join Definition

Create joins between pairs of data entities to create a [Fusion](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072155405-Fuse-Data-Sources) source. You must have at least two data entities in source to create a join. If you have more than one data entity in your source, all entities must be used in a join.

To create a new join, select **Add**, then define the entities, join type, and fields. Select **Apply** to finish creating the join.

![use this area to create and edit joins](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242599232141 "Join Definition work area")

When you create a join, settings you can define can include:

* **Entity Left**: Select an available entity from the data entities you defined.
* **Join Type**: Select Left, Inner, or Full Outer.
* **Entity Right**: Select an available entity from the data entities you defined.
* **Enable Dimension Entity**: Select the gear icon to enable dimension for one or both entities. This improves the performance of queries execution by removing unused data entities from the join.
* **Field Left**: Select at least one field from this entity. You can add multiple fields by selecting the add field button.
* **Field Right**: Select at least one field from this entity. You can add multiple fields by selecting the add field button.

You can also view the relationships of your joins and add more joins in a visualization. See [Create a Fusion Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072201741-Create-a-Fusion-Source).
