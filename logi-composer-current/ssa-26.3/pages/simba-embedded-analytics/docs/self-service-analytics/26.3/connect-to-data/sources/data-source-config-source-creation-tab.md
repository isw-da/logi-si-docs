> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Source Creation Work Areas

Use the Source Creation tab in the Sources work area to define new sources, edit sources, and define the data entity or entities that make up your source.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [Source Creation Tab (Earlier Releases)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab#v25.3).
</Note>

### Source Creation Tab

If you are upgrading from an earlier version, you may temporarily see the earlier interface until you create, edit, or update a source. See [Source Creation Tab (Earlier Releases)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab#v25.3) for interface information.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/cmp-more-details-25-4.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=972831b503d51a42373cf98e6066b354" alt="Use this work area to create or update a source" width="1288" height="810" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/cmp-more-details-25-4.png" />

<Note>
  You must be logged in as user with the **Administer Sources** or **Create New Data Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) to see the Source Creation tab, or have **Read** and **Write** permissions on the source.
</Note>

<Note>
  When you upload a flat file, Select Schema and Select Entity fields are not present, and the option to create Custom SQL is not available. You can instead Select File, Edit File, and configure API Endpoints.
</Note>

The general structure of the Source Creation tab includes:

* Edit and update the name of this source in the top left the work area.
* [Export](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/import-export-data-source), Preview, [Copy](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#copy-a-source), or Save the source using the available icons in the top right of the work area.
* Build your source by dragging one or more entities from you connections or files by dragging and dropping them from the Connections or Files tabs in the right panel to the source work area in the left panel.
* Use the Connections and Files tabs to build your source from available entities, uploaded files, or to add an SQL entity as needed.
* If you add multiple entities, you can manage the Joins directly in the work area.

<h3 id="source-work-area-left-panel">
  Source Work Area (Left Panel)
</h3>

Drag and drop data entities to build your source. After adding a data entity or making changes, select **Save Source** to save your changes, or **Preview Source** to preview your data.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/cmp-src-data-ent-25-4.jpg?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=5260e9a175791451886e5b41204bb82e" alt="drag and drop entities to this left panel source work area to define one or more data entities for your source" width="1292" height="801" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/cmp-src-data-ent-25-4.jpg" />

<h4 id="connections-panel">
  Connections Panel
</h4>

Available connections are listed in the Connections panel. Select the arrows to open and find entities and indices to drag and drop to the source work area. The added entity is represented visually, making it easier for you to make direct changes or create joins when multiple entitles are included in the source.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/cmp-more-details-25-4.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=972831b503d51a42373cf98e6066b354" alt="drag and drop your entity and schema to the work area" width="1288" height="810" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/cmp-more-details-25-4.png" />

<Note>
  Alternatively, select **Add SQL Entity** to use Custom SQL to define your entities and indices in this source.
</Note>

<Note>
  When you create a connection from a flat file, Select Schema and Select Entity fields are not present, and the option to create Custom SQL is not available. You can instead select a file to edit it or configure API Endpoints.
</Note>

After you have added a data entity, you can keep the applied name (the Entity Name, appended by a number), or change it in the Properties panel.

Optionally, add a filter values entity to provide an alternative source of metadata values. Use these entities in a dynamic override on Filter Values tab in Fields to improve the filter experience of heavy data entities.

<h4 id="entity-details-from-connection">
  Entity Details - From Connection
</h4>

Each entity you add is given a unique **Entity Name**, appended by a number. Select an entity to edit its properties in the Properties panel, and manage details of how the information is accessed and presented.

<Note>
  Depending on the your source, different options are available to define it.
</Note>

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/prop-panel-25-4.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=083fe07ad6717f9d8960c5a84c03c850" alt="Use this work area to define your entity, schema, connection, available fields, and more along with caching settings, if available." width="405" height="615" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/prop-panel-25-4.png" />

Details you can define can include:

* **Entity Name**: The unique name for this data entity. By default, a name is generated for the entity name, appended by a number.

* **Select Connection**: Select a connection for this data entity. The connection currently selected is shown, but you can change that. You will only see connections you have access to.

* **Select Schema**: If a Schema is available for your connection, you can select a schema to filter a list of entities for this connection. See [Connector Feature Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support). Visualize your schema by selecting the view option. See [View Relationships of a Schema in a Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/nested-data-structures#view-relationships-of-a-schema-in-a-source).

* **Select Indices**: ElasticSearch connections support Indices: select one or more to include.

  * **Index Selection**: Select **Manually** to create a merged list of fields from selected indices, or **Automatically** to select a pattern that automatically selects indices.

    <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/select-indices-25-4.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=088f551df5b99d9182d277cdb17a7bd4" alt="Supported connections allow you to use automatic or manual index selection here" width="366" height="489" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/select-indices-25-4.png" />

* **Existing Entity** and **Custom SQL**:

  * Select **Existing Entity** to use an available entity from your source.
  * **Custom SQL**: Select to define a custom SQL to retrieve the data you want from your source. **Select Entity** is not available if you select Custom SQL.

* **Select Entity**: Select an available entity.

  * **Available Fields**: All fields available from this source are included by default. Disable (uncheck) specific fields to exclude them from the source. The fields, when disabled, are not included for your users. If you attempt to remove a field currently in use by a visual or other object, Self-Service Analytics will prevent you from saving your changes to the data source.

  * **Entity Preview** table: Select the Preview icon in the Available Fields work area. This opens an **Entity Preview** dialog pop up. This preview includes all of the fields in the entity (no matter your selections) to help you decide what to include or exclude.

    <Note>
      The Preview icon next to the Save Source button opens a Source Preview. This preview only includes what fields you have made available after applying your field selections and saving your work.
    </Note>

    In the example shown here, the **credit\_limit** field is deselected in Available Fields. It is visible in the Entity Preview table, but not the Source Preview table.

    <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/previews-25-4.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=8b81bf161f46261ea8b3c44f4a180def" alt="Entity Preview includes all fields. Source preview only includes fileds selected for inclusion." width="1597" height="480" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/previews-25-4.png" />

Select **Apply** to apply your changes, or add another data entity to [create joins for a Fusion source](#join-definition).

<h4 id="custom-sql">
  Custom SQL
</h4>

When you select this option, a Custom SQL editing pane opens that you can use to write and run your SQL query. If you prefer a larger work area, select the **Open editor** option to open a larger editing canvas.

After you have run a successful query, the results populates **Available Fields** and the **Preview** table, and you can **Apply** your changes. You can not save invalid SQL.

Table visuals and Details dialogs display fields in the order they are retrieved from the source. When you create a source using custom SQL, your fields are shown in the order you specify.

<Warning>
  Custom SQL queries are a powerful tool for performing complex data queries. However, be careful when creating custom SQL queries because it is easy to define a heavy query or a query that may overwhelm your database. Use this feature carefully.
</Warning>

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/edit-sql-1-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=dc4baa010ba5f785b6b7d92014ffd96b" alt="enter the custom SQL for your entity" width="404" height="636" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/edit-sql-1-26-2.png" />

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/edit-sql-2-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=50b68faf4d03c7044035797186038900" alt="an expanded work area you can use to enter the custom SQL for your entity" width="597" height="502" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/edit-sql-2-26-2.png" />

<Note>
  Use the grab bars at the corner of the editing field to extend your viewable area.
</Note>

Variables (specified as custom user attributes) can be inserted in custom SQL. See [Specify Custom User Attributes](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#specify-custom-user-attributes). In addition, you can use a vertical bar (|) in the SQL to separate the custom attribute name from a default value used for user definitions that do not have the custom user attribute defined. For example, the following custom SQL uses the value of the `state` customer user attribute to filter source data for records from whatever state the user's `state` custom user attribute is set to. If a `state` custom user attribute is not defined for a user, a default of Alabama is used.

```
SELECT * FROM Orders WHERE state = '${User.state|Alabama}'
```

<h4 id="data-entity-details-from-file">
  Data Entity Details - From File
</h4>

Each entity you add is given a unique **Entity Name**, appended by a number. Select an entity to edit its properties in the Properties panel, and manage details of how the information is accessed and presented.

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/file-ent-det-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=b8a70b6b5bb69885f254ff271aff90ff" alt="edit and manage data provided from a file" width="408" height="737" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/file-ent-det-26-2.png" />

When you select a File to use for your data source, the details you can define can include:

* **Entity Name** - The unique name for this data entity. By default, a name is generated for the entity name, appended by a number.
* **Select File**: Select an available uploaded file for this data entity. A list of all native fields from this entity populates **Available Fields** and the **Preview** table. Use **Upload New File** to add files to this source. See [Manage File Uploads](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file).
* **[API Endpoints](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)**: Select for more information about appending data, replacing data, or deleting data from your file upload.
* **Edit File**: Select to edit the **File Details** of your uploaded file.

Select **Apply** to apply your changes, or add another data entity to [create joins for a Fusion source](#join-definition).

<h3 id="join-definition">
  Join Definition
</h3>

Create joins between pairs of data entities to create a [Fusion](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview) source. You must have at least two data entities in source to create a join. If you have more than one data entity in your source, all entities must be used in a join.

To create a new join, select **Add Join** to add a join node to your work area.

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/add-jn-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=761144515cca85695532f3adcbe5ca69" alt="select to add a joins object to your data source when one or more entities are present" width="499" height="337" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/add-jn-26-2.png" />

Select the join node to define how the entities use a join type to connect specific fields. Select **Apply** to finish creating the join.

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/jn-settings-26-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=d7ae5602ed84a210d0123cb62828a7b3" alt="use this area to create and edit joins" width="1430" height="387" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/jn-settings-26-2.png" />

When you create a join, settings you can define can include:

* **Entity Left**: Select an available entity from the data entities you defined.
* **Join Type**: Select Left, Inner, or Full Outer.
* **Entity Right**: Select an available entity from the data entities you defined.
* **Enable Dimension Entity**: Select the settings icon to enable dimensions for one or both entities. This improves the performance of queries execution by removing unused data entities from the join.
* **Field Left**: Select at least one field from this entity. You can add multiple fields by selecting the add field button.
* **Field Right**: Select at least one field from this entity. You can add multiple fields by selecting the add field button.

You can also view the relationships of your joins and add more joins in a visualization. See [Create a Fusion Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#create-a-fusion-source).
