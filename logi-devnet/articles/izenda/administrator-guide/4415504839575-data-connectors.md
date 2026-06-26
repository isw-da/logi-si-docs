---
title: "Data Connectors"
id: 4415504839575
section: "Administrator Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504839575-Data-Connectors
updated_at: 2021-12-10T03:10:27Z
---

# Data Connectors

# Data Connectors

The **Data Connectors** page allows users to

* manage the list of connectors
* select individual items from these connectors to be visible in Data Model and Reports

Note:

For the Reporting Databases:   
- The connection string user should have permissions to read schema; to select on all tables, views, store procedures and functions that will be used as data sources; to execute those store procedures and functions.   
- The user should also have permissions to create temp tables.

## Add connector and select visible data sources

In this step user adds a connector and selects data sources to be
visible in reports.

Warning: Please use caution when adding stored procedures to the visible data source list. All stored procedures are executed when added to visible (input parameters are set to NULL) to obtain the resulting fields returned. Some stored procedures are created to do things like delete tables, add data to tables, etc. If these are added to the visible data sources, they will be executed in the database.

1. In browser, log in to Izenda as a user with Data Connectors permission.
2. Click Settings, then Data Setup then Data Connectors in the left menu.

   [![../_images/Connector_Add_Connector.png](https://devnet.logianalytics.com/hc/article_attachments/4415511745559/connector_add_connector_500x580.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504391959/connector_add_connector.png)
3. Select the Setting Level: either System or a specific tenant.
4. Click on Add Connector in the middle panel.

   [![../_images/Connector_Server_Type.png](https://devnet.logianalytics.com/hc/article_attachments/4415492487319/connector_server_type_700x583.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492486679/connector_server_type.png)
5. Select the data server type from the pop-up.
6. The Database Connection pop-up appears for configuring the connector.

   [![../_images/Connector_Builder.png](https://devnet.logianalytics.com/hc/article_attachments/4415504393239/connector_builder_500x376.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504392983/connector_builder.png)

   1. Fill in the **Server Name**, e.g. “yourdbserver.com”.
   2. Fill in the **Database** name, e.g. “Northwind”.
   3. Select the **Authentication** type from the drop-down box.
   4. Fill in the **Login** and **Password** if necessary.
   5. Optional. Fill in the additional connection options specific to the selected data server.

   These steps can be bypassed when user already knows the connection string. In this case, it can be copied and pasted straight into the Connection String box.
   For examples of connection strings, please see the [Connection String Examples](https://www.izenda.com/docs/ui/doc_connection_string.html#connection-string-examples) section below.
   To do this, switch to Connection String mode:

   [![../_images/Connector_Builder_Connection_String.png](https://devnet.logianalytics.com/hc/article_attachments/4415492488087/connector_builder_connection_string_500x382.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492487831/connector_builder_connection_string.png)
7. Click OK button to verify the connection and go to the next step after all required fields are filled in.

   Note: Unless the Connection String has been verified successfully, user will not be able to move next.
8. The connector name will be automatically populated from the database name. User can edit to give it a more suitable name.

   [![../_images/Connector_Name.png](https://devnet.logianalytics.com/hc/article_attachments/4415504396439/connector_name_700x104.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504395543/connector_name.png)
9. Expand the listed user schemas and object types to see the data sources.   
   The data sources can be quickly filtered by typing a partial name in the Search box.
10. Click on the data sources to move them between the two lists.
    User can quickly move all data sources in a group (Table, View, Stored Procedure or Function) by clicking on that group name.

    [![../_images/Connector_Data_Sources.png](https://devnet.logianalytics.com/hc/article_attachments/4415504397591/connector_data_sources_800x459.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504397335/connector_data_sources.png)
11. Click Save button at the top to save the connector and the visible data sources.

## Connector Permissions

Izenda needs permissions to view the database schema and read from selected tables and views.

If using stored procedures as data source, Izenda needs execute permission on these stored procedures as well as create table and delete table permissions.

Note: The create table permission will be used to create temporary tables to store the output of stored procedures, for joining to other data sources. And the delete table permission will be used to clean up these temporary tables afterward.

## Delete connector

1. Click the delete icon (x) on the right of a connector to delete it.
2. Click OK in the confirmation pop-up.

## Make a connector hidden

All data sources from a connector can be hidden quickly by making that connector hidden.

1. Click the visibility icon on the right of that connector.

   [![../_images/Connector_Visible_Invisible.png](https://devnet.logianalytics.com/hc/article_attachments/4415504398103/connector_visible_invisible_450x212.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504397847/connector_visible_invisible.png)
2. Click OK in the confirmation pop-up.

   > All data sources from this connector is hidden from Data Model and Reports. The right pane is disabled and the connector’s visibility icon is changed to a hidden one.
   >
   > [![../_images/Connector_Visible_Confirmation.png](https://devnet.logianalytics.com/hc/article_attachments/4415504398615/connector_visible_confirmation_500x123.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492488599/connector_visible_confirmation.png)

To restore the visibility of the data sources:

1. Click the “hidden visibility” icon on the right of that connector.
2. Click OK in the confirmation pop-up.

   > The visibility of all data sources from this connector is restored back to the time before being hidden. The right pane is enabled and the connector’s visibility icon is changed back to normal.

## Refresh the list of available data sources

When there is a remote change in a connector, it will not be automatically reflected in Izenda. The Reconnect button needs to be manually clicked on to detect that.

1. Click on the connector.
2. Click the Reconnect button.
3. The remote changes in the data sources will be marked as either New data source or Changed data source.

   > The Data Setup, Data Connectors and Data Model menu items will also be marked with Changed data source icon (!).
   >
   > [![../_images/Connector_New_And_Changed_Data_Sources.png](https://devnet.logianalytics.com/hc/article_attachments/4415492489239/connector_new_and_changed_data_sources_800x469.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492488855/connector_new_and_changed_data_sources.png)
4. Go to [Data Model](https://devnet.logianalytics.com/hc/en-us/articles/4415492931607-Data-Model-Tables-Views-and-Stored-Procedures) page to resolve the changes.

## Filter the connector list

The connector list can be quickly filtered by typing a partial connector name in the Search box.

## Cancel the changes

To cancel any changes without saving:

1. Click the Cancel button at the top.
2. Click OK in the confirmation pop-up.

## Connection String Examples

* Oracle:
  :   + Data Source=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.45.37)(PORT=1521))(CONNECT\_DATA=(SERVICE\_NAME=MyOracleSID)));User Id=user;Password=password;
      + Data Source=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.45.37)(PORT=1521))(CONNECT\_DATA=(SID=xe)));User Id=user;Password=password;
* Microsoft SQL Server:
  :   + Server=192.168.45.37,1433;Database=testdatabase;User ID=user;Password=password
      + Server=HOST-PC;Database=testdatabase;User ID=user;Password=password
* MySQL:
  :   + Server=MY-PC;Port=3306;Database=testdatabase;User ID=user;Password=password
* PostgreSQL:
  :   + Server=mydomainname;Port=5432;Database=testdatabase;User ID=user;Password=password
      + Server=mydomainname;Port=5432;Database=testdatabase;User ID=user;Password=password;SslMode=Require;Trust Server Certificate=true;

      Note

      + If using Izenda v3.0.0 or greater and a PostgreSQL connection string with “SslMode=Require”, the “Trust Server Certificate=true;” parameter will also need to be added.
* [Elasticsearch](https://www.izenda.com/docs/intro/elastic.html):
  :   + server=https://xxxxxxxx.us-east-1.aws.found.io;Port=9243;User=user;Password=password;
* [MongoDB](https://www.izenda.com/docs/intro/mongo.html):
  :   + Server=localhost;Port=27017;Database=admin;User=user;Password=password;
      + User=user;Password=password;Server=atlas-host1;Port=27017;Database=testdatabase;AuthDatabase=admin;AuthMechanism=SCRAM-SHA-1;ReplicaSet=cluster0-shard-00-01-u49p2.mongodb.net:27017,cluster0-shard-00-02-u49p2.mongodb.net:27017;UseSSL=true;SlaveOK=true;
