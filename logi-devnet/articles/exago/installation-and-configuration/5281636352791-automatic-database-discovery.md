---
title: "Automatic Database Discovery"
id: 5281636352791
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281636352791-Automatic-Database-Discovery
updated_at: 2023-04-03T17:52:19Z
---

# Automatic Database Discovery

# Automatic Database Discovery

This topic applies to the **Admin Console** > ![TreeData.png](https://devnet.logianalytics.com/hc/article_attachments/5432184487703/treedata.png)**Data** > ![TreeDataSource.png](https://devnet.logianalytics.com/hc/article_attachments/5432124400791/treedatasource.png)**Sources** settings.

---

To discover and add data objects, joins and metadata to the configuration automatically use:

* [Add All Complete Objects, Joins and Metadata v2021.2+](#Add), or
* [Discover Database Metadata](#Discover)

Automatic Database Discovery is available for all Exago BI supported Data Sources except files (Excel & XML), .NET Assemblies and Microsoft OLAP. Google BigQuery Data Sources do not support primary and foreign key constraints, so the Automatic Database Discovery tools does not add primary key columns or suggest joins.

## Add All Complete Objects, Joins and Metadata v2021.2+

To automatically add all complete data objects, joins and column metadata in a single operation, use the **Add All Complete Objects, Joins and Metadata** feature.

This feature adds new tables, views, stored procedures or database functions that have at least one primary key defined in the data source (called a complete object). Joins are added when there is a foreign key from one complete object to another.

Any data objects or joins that already exist in the configuration will not be updated with information discovered with this method, they are skipped instead. To add missing metadata or join information, use the [Discover Database Metadata](#Discover) method described below.

To do so:

1. Right-click on a Data Source.
2. Click ![AddNew.png](https://devnet.logianalytics.com/hc/article_attachments/5432231941911/addnew.png) **Add All Complete Objects, Joins and Metadata** in the context menu
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432231965079/add-all-objects-menu.png)
3. Click **Okay** on the confirmation dialog, or **Cancel** to abort the process.  
   ![GqNYnO1Lx7.png](https://devnet.logianalytics.com/hc/article_attachments/5432256788759/gqnyno1lx7.png)
4. Wait for the summary tab to open.  
   ![Y4S9hjHFbZ.png](https://devnet.logianalytics.com/hc/article_attachments/5432232012823/y4s9hjhfbz.png)

   The summary tab shows the result of the operation:

   * **Total complete objects added** — number of complete data objects added to the configuration
   * **Total incomplete objects found** — number of incomplete objects found. Incomplete objects are not added to the configuration with this feature. Use [Discover Database Metadata](#Discover) to add them.
   * **Total objects skipped** — number of complete data objects found that already exist, or otherwise not added to the configuration
   * **Total joins added** — number of joins added to the configuration
   * **Total joins skipped** — number of joins found that already exist, or otherwise not added to the configuration
   * **Total metadata added** — number of data object columns that had column metadata added
5. If in step 4 there were any incomplete objects found, either use [Discover Database Metadata](#Discover) or manually add the metadata to make them complete.

## Discover Database Metadata

The **Discover Database Metadata** option is available for granular control over the automatic discovery and import of Data Source schema information.It is also used when incomplete objects exist in a Data Source and are not detected with the [Add All Complete Objects, Joins and Metadata v2021.2+](#Add) feature.

To start using Automatic Database Discovery, select a Data Source from the list and then either:

* click the **Discover Database Metadata**![AdminDiscoveryLarge.png](https://devnet.logianalytics.com/hc/article_attachments/5432184643735/admindiscoverylarge.png) icon at the top of the main menu
* right-click the Data Source then click ![AdminDiscoverySmall.png](https://devnet.logianalytics.com/hc/article_attachments/5432184668439/admindiscoverysmall.png)**Discover Object/Join Metadata** from the context menu

This will open a discovery tab for the Data Source.

![explorer_df40UvksDn.png](https://devnet.logianalytics.com/hc/article_attachments/5432232093975/explorer_df40uvksdn.png)

Automatic Database Discovery tab

In the discovery tab you can:

1. Select the Tables, Views, Functions, and Stored Procedures you would like to add by either:
   * checking individual item checkboxes
   * clicking ![DiscoverySelectAll.png](https://devnet.logianalytics.com/hc/article_attachments/5432257142807/discoveryselectall.png)**Select All Complete Objects** to select only those objects with unique key values already defined
   * clicking ![DiscoverySelectAll.png](https://devnet.logianalytics.com/hc/article_attachments/5432257142807/discoveryselectall.png)**Select All Objects** to select all data objects regardless of whether or not unique key values are defined  

     Table A — Icons

     | Icon | Description |
     | --- | --- |
     | skeleton key | This object has identified unique key values |
     | converging right pointing arrows | This object has associated joins |
     | DiscoveryObjectInfoNeeded.png | This object is incomplete |
2. Add Unique Key fields by right-clicking on an object and selecting **Add/Edit Primary Key Info**.
3. Check **Preview Only** and then ![ApplyBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432257516055/applybtn.png)**Add Objects** to preview the selected objects and joins.
4. Uncheck **Preview Only** and then add the selected Data Objects to the system by clicking ![ApplyBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432257516055/applybtn.png)**Add Objects** or ![ApplyBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432257516055/applybtn.png)**Add Objects and Joins** to add the selected objects and any associated joins.  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > If any selected Objects are missing unique key values they can be completed individually in a new tab which will open entitled **Incomplete Objects**.

## Schema Discovery

Exago BI can retrieve primary and foreign key constraint information from the Data Sources by either:

* [SQL Queries](#SQL)
* [ADO.NET GetSchema() v2021.1.8+](#ADO.NET)

### SQL Queries

### Customizing Data Discovery SQL v2016.3.6+

The SQL statements used for Automatic Database Discovery can be customized if necessary, in order to accommodate non-standard key names.

To customize the discovery SQL:

1. Refer to [Managing the dbconfigs.json File](https://devnet.logianalytics.com/hc/en-us/articles/5281593110167-Managing-the-dbconfigs-json-File) for the location of the file to edit. Follow the instructions in the **Overriding `dbconfigs` Information** section to correctly override the default behavior depending on the version of Exago BI.
2. Locate the property for the data source type and edit the SQL for either or both primary and foreign keys.
3. Save the file, then run Database Discovery to see the changes.

Excerpt from `dbconfigs.json` showing the database discovery SQL statements for Primary and Foreign Key discovery on a MySQL Data Source:

```
"mysql": {
     "PrimaryKeySql": "SELECT CONSTRAINT_NAME AS indexname, TABLE_SCHEMA as schemaname, TABLE_NAME as tablename, COLUMN_NAME as columnname FROM information_schema.key_column_usage WHERE table_schema = schema() AND CONSTRAINT_NAME = 'PRIMARY'",
     "ForeignKeySql": "SELECT TABLE_SCHEMA As schemaname, TABLE_NAME as tablename, COLUMN_NAME as columnname, REFERENCED_TABLE_SCHEMA as referencedschemaname, REFERENCED_TABLE_NAME as referencedtablename, REFERENCED_COLUMN_NAME as referencedcolumnname FROM information_schema.key_column_usage WHERE  table_schema = schema() AND CONSTRAINT_NAME Like 'FK%'"
}
```

### ADO.NET GetSchema() v2021.1.8+

Exago BI uses the standard `GetSchema()` methods to request schema information from a Data Source when:

* The database driver in use to connect to the Data Source is an ADO.NET driver
* The `dbconfigs.json` (or according `dbconfigs.overrides.json`) file contains the **`PrimaryKeysCollection`** and/or the **`ForeignKeysCollection`** properties.

Exago BI provides the definition of the **`PrimaryKeysCollection`** and **`ForeignKeysCollection`** properties on data source-by-data source basis. The values for each property vary with the Data Source type and the driver in use.

An example of implementing ADO.NET GetSchema() primary/foreign key constraint discovery for a MySQL Data Source follows:

```
{
 "mysql": {
  "PrimaryKeysCollection": {
   "CollectionName": "Indexes",
   "ConstraintNameColumn": "INDEX_NAME",
   "SchemaColumn": "INDEX_SCHEMA",
   "TableColumn": "TABLE_NAME",
   "IsPrimaryColumn": "PRIMARY"
  },
  "PrimaryKeyColumnsCollection": {
   "CollectionName": "IndexColumns",
   "ConstraintNameColumn": "INDEX_NAME",
   "SchemaColumn": "INDEX_SCHEMA",
   "TableColumn": "TABLE_NAME",
   "ColumnColumn": "COLUMN_NAME"
  },
  "ForeignKeysCollection": {
   "CollectionName": "Foreign Key Columns",
   "FromSchemaColumn": "TABLE_SCHEMA",
   "FromTableColumn": "TABLE_NAME",
   "FromColumnColumn": "COLUMN_NAME",
   "ToSchemaColumn": "REFERENCED_TABLE_SCHEMA",
   "ToTableColumn": "REFERENCED_TABLE_NAME",
   "ToColumnColumn": "REFERENCED_COLUMN_NAME"
  }
 }
}
```
