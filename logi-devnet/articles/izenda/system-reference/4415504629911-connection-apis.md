---
title: "Connection APIs"
id: 4415504629911
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504629911-Connection-APIs
updated_at: 2021-12-10T03:08:06Z
---

# Connection APIs

# Connection APIs

The **Connection String** page allows users to manage the list of connections and select individual items from these connections to be visible in reports.

## Summary

| API | Purpose | Usage in Izenda Front-end |
| --- | --- | --- |
| [GET connection/(tenant\_id)](#get-connection-tenant-id) | Returns an array of connections (filtered by tenant\_id if given). | Settings > Data Setup > Connection String, for a specific tenant |
| [GET connection/basicInfo/(tenant\_id)](#id1) | Returns an array of id and name of connections (filtered by tenant\_id if given). | To be updated |
| [GET connection/detail/{connection\_id}](#get-connection-detail-connection-id) | Returns the details of the connection specified by the {connection\_id} value. | Settings > Data Setup > Connection String > select an existing connection |
| [GET connection/detailInfo/(tenant\_id)/{loadField}](#get-connection-detailinfo-tenant-id-loadfield) | Returns an array of connection details. | To be updated |
| [GET connection/preset/{server\_type\_id}](#get-connection-preset-server-type-id) | Returns a set of all connection presets, filtered by server\_type\_id.  Tip  New in version 3.9.4. | REST Connector: Settings > Data Setup > Connection String > Edit Connection > Load preset |
| GET connection/systemIndicator/(tenantId) | Returns the number of changes in Connection String and Data Model (filtered by tenant\_id if provided).  Warning  Obsolete, use [GET systemSetting/systemIndicator/(tenant\_id)](https://devnet.logianalytics.com/hc/en-us/articles/4415492759191-System-DB-and-License-APIs#get-systemsetting-systemindicator-tenant-id) instead | Not used |
| [GET connection/visible/(tenant\_id)/count](#get-connection-visible-tenant-id-count) | Returns the count of visible connections, filtered by tenant\_id if available. | Settings > Data Setup > Connection String |
| [GET dataAdaptor](#id2) | Returns an array of database server types currently supported for queries.   See also: [GET databaseSetup/supportedDatabaseType](https://devnet.logianalytics.com/hc/en-us/articles/4415492759191-System-DB-and-License-APIs#get-databasesetup-supporteddatabasetype) | Settings > Data Setup > Add Connector > populate Data Server Type tiles |
| [GET systemSetting/databaseSetup](#get-systemsetting-databasesetup) | Returns whether the system database has been set up. | On Front-end load |
| [POST connection](#id3) | Adds a new connection or updates an existing one.   Only visible query sources should be saved. | Settings > Data Setup > Connection String > Save |
| [POST connection/connectionStringData](#post-connection-connectionstringdata) | Returns the connection string data for a specific connection.  Tip  New in version 3.9.4. | Settings > Data Setup > Connection String > Edit Connection |
| [POST connection/databaseName](#post-connection-databasename) | Returns the database name from a connection string. | Settings > Data Setup > Add Connector > Data Server Type > fill all required fields > click OK |
| [POST connection/detailInfo](#post-connection-detailinfo) | Returns an array of connection details with paging. | To be updated |
| [POST connection/detailInfoByQuerySources](#post-connection-detailinfobyquerysources) | Returns an array of connection objects filled with field data.  Tip  New in version 3.11.0. | Settings > Data Setup > Advanced Settings > Security > click Add (Row-Level Security) > select one or more available Data Sources and click Next to go to Step 2 |
| [POST connection/invisible/{connection\_id}](#post-connection-invisible-connection-id) | Hides from Data Model and Reports all query sources in the connection specified by the {connection\_id} value. | Settings > Data Setup > Connection String > click Visibility icon of a visible connection |
| [POST connection/loadDistinctConnections](#id4) | Returns an array of distinct connections (by server type and database name) from a list of tenant ids. | Settings > Data Setup > Copy Management |
| [POST connection/loadRemoteSchema](#id5) | Returns an enumeration of all supported objects (query sources) from a connection string. | Settings > Data Setup > Add Connector > Data Server Type > fill all required fields > click OK |
| [POST connection/reloadRemoteSchema](#post-connection-reloadremoteschema) | Returns an enumeration of all supported objects (query sources) from an existing connection with detected changes. | Settings > Data Setup > Connection String > Reconnect an existing connection |
| [POST connection/validateSchema](#post-connection-validateschema) | Returns true if remote schema has not changed, otherwise returns false. | To be updated |
| [POST connection/verify](#id6) | Validates a connection string.   See also: [POST databaseSetup/testConnection](https://devnet.logianalytics.com/hc/en-us/articles/4415492759191-System-DB-and-License-APIs#post-databasesetup-testconnection) | Settings > Data Setup > Add Connector > Data Server Type > fill all required fields > click OK |
| [POST connection/visible/{connection\_id}](#post-connection-visible-connection-id) | Restores the visibility of all query sources in the connection specified by the {connection\_id} value. | Settings > Data Setup > Connection String > click Visibility icon of a hidden connection |
| [DELETE connection/{connection\_id}](#delete-connection-connection-id) | Deletes the connection specified by the {connection\_id} value. | Settings > Data Setup > Connection String > click Delete icon of a connection |

## GET connection/(tenant\_id)

Returns an array of connections (filtered by tenant\_id if given).

**Request**

> No payload

**Response**

> An array of [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) objects
>
> Note
>
> **dBSource** field is not populated in this API, use [GET connection/detail/{connection\_id}](#get-connection-detail-connection-id) instead.

**Samples**

> ```
> GET/api/connectionHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"id":"89e91284-6546-44d0-8de0-f8f666a590ea","name":"Northwind","serverType":"d968e96f-91dc-414d-9fd8-aef2926c9a18","serverTypeName":"AZSQL","connectionString":"1aBcD+==","visible":true,"deleted":false,"relateToConnectionId":null,"tenantId":null,"dBSource":null,"relationships":null,"physicalChange":0},{"id":"2f7e216b-8637-49e2-8391-cea682e4c32f","name":"oAdventure","serverType":"d968e96f-91dc-414d-9fd8-aef2926c9a18","serverTypeName":"AZSQL","connectionString":"1aBcD+==","visible":true,"deleted":false,"relateToConnectionId":null,"tenantId":null,"dBSource":null,"relationships":null,"physicalChange":0}]
> ```

## GET connection/basicInfo/(tenant\_id)

Returns an array of id and name of connections (filtered by tenant\_id if given).

**Request**

> No payload

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **key**  string (GUID) | The id of the connection |  |
> | **value**  string | The name of the connection |  |

**Samples**

> ```
> GET/api/connection/basicInfoHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"key":"1a65445b-2779-4825-8c0b-2491eaa87a46","value":"AdventureWorks2008R2"},{"key":"dda3633e-659f-4e88-9955-4e20bded686c","value":"Northwind"}]
> ```

## GET connection/detail/{connection\_id}

Returns the details of the connection specified by the {connection\_id} value.

These include the connection fields and the query sources inside.

**Request**

> No payload

**Response**

> A [ConnectionResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492772887-ConnectionResult) object

**Samples**

> ```
> POST/api/connection/detail/2f7e216b-8637-49e2-8391-cea682e4c32fHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"connection":{"id":"2f7e216b-8637-49e2-8391-cea682e4c32f","name":"AdventureWorks","serverType":"d968e96f-91dc-414d-9fd8-aef2926c9a18","serverTypeName":null,"connectionString":"1a2B+=","visible":true,"deleted":false,"relateToConnectionId":null,"tenantId":null,"dbSource":{"querySources":[{"id":"588d7aa8-6ba0-4629-ab68-56b8e1009fc7","name":"dbo","parentCategoryId":null,"connectionId":"2f7e216b-8637-49e2-8391-cea682e4c32f","querySources":[{"id":"38804b44-bf23-41c0-b498-6d4199b8e34d","name":"AWBuildVersion","type":"Table","parentQuerySourceId":null,"categoryId":"588d7aa8-6ba0-4629-ab68-56b8e1009fc7","selected":false,"connectionName":null,"childs":null,"dataSourceCategoryId":null,"dataSourceCategoryName":null,"alias":null,"querySourceFields":[],"querySourceCategory":null,"modified":"2016-03-21T05:27:59.553","extendedProperties":null,"physicalChange":0,"approval":0}],"childs":null,"connection":null,"physicalChange":0}]},"relationships":null,"physicalChange":0},"success":true,"messages":null}
> ```

## GET connection/detailInfo/(tenant\_id)/{loadField}

Returns an array of connection details.

**Request**

> No payload
>
> **loadField**:
>
> * true: return query source field data
> * false: do not return query source field data
>
> **Query String**:
>
> loadStoreProcSchema=boolean&loadInactiveConnections=boolean   
>  &removeEmptyParent=boolean&defaultChecked=boolean

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **hashCode**  string | The hash code of the connections |  |
> | **connections**  string | An array of [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) objects |  |

**Samples**

> ```
> GET/api/connection/detailInfo/f6d1638a-df71-4f33-b2a8-a2510a7dbb40/true&loadStoreProcSchema=falseHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"hashCode":"8d7b2626230999de7f6edb5c7ca","connections":[{"id":"b6cff8c7-fd41-47a3-9a55-7b332344792c","name":"Northwind","serverTypeId":"572bd576-8c92-4901-ab2a-b16e38144813","serverTypeName":"MSSQL","connectionString":"123abc=","visible":true,"deleted":false,"relateToConnectionId":null,"tenantId":"f6d1638a-df71-4f33-b2a8-a2510a7dbb40","dbSource":{"querySources":[{"id":"cc61e681-f6d1-4784-97c7-c387af2d8ff1","name":"dbo","parentCategoryId":null,"connectionId":"b6cff8c7-fd41-47a3-9a55-7b332344792c","querySources":[{"realName":null,"id":"0ad3e706-b775-411d-bcc5-acf615d9f4ce","name":"CustOrderHist","type":"Stored Procedure","parentQuerySourceId":null,"categoryId":"cc61e681-f6d1-4784-97c7-c387af2d8ff1","selected":false,"deleted":false,"connectionId":"00000000-0000-0000-0000-000000000000","connectionName":null,"childs":null,"dataSourceCategoryId":null,"dataSourceCategoryName":null,"alias":null,"querySourceFields":[{"name":"@CustomerID","alias":"","dataType":"nchar","izendaDataType":"Text","allowDistinct":false,"visible":true,"filterable":true,"querySourceId":"0ad3e706-b775-411d-bcc5-acf615d9f4ce","parentId":null,"expressionFields":[],"filteredValue":"","type":1,"groupPosition":0,"position":1,"extendedProperties":null,"physicalChange":-1,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"fullName":null,"calculatedTree":null,"reportId":null,"originalName":null,"originalId":"00000000-0000-0000-0000-000000000000","isParameter":true,"isCalculated":false,"hasAggregatedFunction":false,"querySource":null,"querySourceName":null,"categoryName":null,"inaccessible":false,"fullPath":null,"id":"f8e8651b-64c7-454f-81c2-ca7a5866d4e5","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"4e9fd487-56b6-4ee7-856a-1428ea4d0739","modified":"2016-11-02T10:52:05.723","modifiedBy":null}],"querySourceCategoryName":"dbo","querySourceCategory":null,"modified":"2016-11-02T10:52:05.707","extendedProperties":"{\"Dynamic\":false,\"Static\":false}","physicalChange":-1,"approval":0,"existed":false,"checked":true,"fullPath":null}]}]}}]}
> ```

## GET connection/preset/{server\_type\_id}

Returns a set of all connection presets, filtered by server\_type\_id.

**Request**

> No payload

**Response**

> A set of connection preset objects specific to the specified server type.

**Samples**

> ```
> GET/api/connection/preset/4b751f52-0903-4170-ab15-814a7fa4e42cHTTP/1.1
> ```
>
> Successful response:
>
> ```
> {"data":{"myRest":[{"endpointName":"Northwind","address":"https://rest.service.com","schemePath":"/NorthwindJSON/schema.json","dataPath":"/NorthwindJSON/{0}.json","flattenArrays":true,"flattenObjects":true,"flattenDepth":4,"subColumnSeparator":".","headers":{},"body":null,"requestCacheTtl":600,"requestCacheEnabled":true,"connectionString":null}]},"success":true,"messages":null}
> ```

## GET connection/visible/(tenant\_id)/count

Returns the count of visible connections, filtered by tenant\_id if available.

**Request**

> No payload

**Response**

> The number of connections

**Samples**

> ```
> GET/api/connection/visible/countHTTP/1.1
> ```
>
> Sample response (in case user has System Admin Permission):
>
> ```
> 2
> ```
>
> Reponse in case user does not have System Admin Permission:
>
> ```
> {"message":"You don't have permission to perform this action","detail":"NoPermission"}
> ```

## GET dataAdaptor

Returns an array of database server types currently supported for queries.   
See also: `GETdatabaseSetup/SupportedDatabaseType`

**Request**

> No payload

**Response**

> An array of objects
>
> | Field | Description | Note |
> | --- | --- | --- |
> | **id**  string (GUID) | The id of the connection | Example: `572bd576-8c92-4901-ab2a-b16e38144813` |
> | **shortName**  string | The short name of the database server type |  |
> | **name**  string | The display name of the database server type |  |

**Samples**

> ```
> GET/api/dataAdaptorHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"name":"[AZSQL] AzureSQL","shortName":"AZSQL","id":"d968e96f-91dc-414d-9fd8-aef2926c9a18"},{"name":"[MYSQL] MySQL","shortName":"MYSQL","id":"3d4916d1-5a41-4b94-874f-5bedacb89656"},{"name":"[ORACL] Oracle","shortName":"ORACL","id":"93942448-c715-4f98-85e2-9292ed7ca4bc"},{"name":"[PGSQL] PostgreSQL","shortName":"PGSQL","id":"f2638ed5-70e5-47da-a052-4da0c1888fcf"},{"name":"[MSSQL] SQLServer","shortName":"MSSQL","id":"572bd576-8c92-4901-ab2a-b16e38144813"}]
> ```

## GET systemSetting/databaseSetup

Returns whether the system database has been set up.

**Request**

> No payload

**Response**

> * true if the system database has been set up.
> * false if not.

**Samples**

> ```
> GET/api/systemSetting/databaseSetupHTTP/1.1
> ```
>
> Response when system database has been setup:
>
> ```
> true
> ```

## POST connection

Adds a new connection or updates an existing one.   
Only visible query sources should be saved.

The connection string will be validated before saving.

**Request**

> Payload: a [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) object

**Response**

> A [SaveConnectionStatus](https://devnet.logianalytics.com/hc/en-us/articles/4415492882967-SaveConnectionStatus) object

**Samples**

> ```
> POST/api/connectionHTTP/1.1
> ```
>
> Request payload for a new connection:
>
> ```
> {"id":null,"name":"db01","serverTypeId":"572bd576-8c92-4901-ab2a-b16e38144813","connectionString":"server=izenda01\\DB_INSTANCE;database=db01;User Id=user01;Password=secret;","visible":true,"dBSource":{"querySources":[]}}
> ```
>
> Sample response (in case user has System Admin Permission):
>
> ```
> {"success":true,"connectionId":"f5180bc0-7c07-48db-b672-e66a5adde027","connectionErrors":[]}
> ```
>
> Response in case user does not have System Admin Permission:
>
> ```
> {"message":"You don't have permission to perform this action","detail":"NoPermission"}
> ```

## POST connection/connectionStringData

Returns the connection string data for a specific connection.

**Request**

> | Field | NULL | Description | Note |
> | --- | --- | --- | --- |
> | **connectionId**  string (GUID) |  | The id of the connection |  |
> | **serverTypeId**  string (GUID) |  | The id of the server type |  |
> | **connectionString**  string | Y | The encrypted connection string |  |

**Response**

> A set of connection preset objects specific to the specified server type.

**Samples**

> ```
> POST/api/connection/connectionStringDataHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"connectionId":"3e0e8445-eab1-4570-8528-17f2f93a80ab","serverTypeId":"bfdb387c-f405-4dbc-8677-c3c5bad91193","connectionString":"FPEo/svV4DeikmSZAnqCgDsYKrCR99z2Gn83tcaKxvUJ276UoVtUdfdgyPwLwTIcKoB1AGiqvehnW+jhQBjbF4wV+8VWLAyOZAydPw/QSmdJT06XA=="}
> ```
>
> Sample response:
>
> ```
> {"data":{"":[{"endpointName":"Northwind","address":"https://rest.service.com","schemePath":"/NorthwindJSON/schema.json","dataPath":"/NorthwindJSON/{0}.json","flattenArrays":true,"flattenObjects":true,"flattenDepth":4,"subColumnSeparator":".","headers":{},"body":null,"requestCacheTtl":600,"requestCacheEnabled":true,"connectionString":null}]},"success":true,"messages":null}
> ```

## POST connection/databaseName

Returns the database name from a connection string.

**Request**

> Payload: a [DBSetupInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504716823-DBSetupInfo) object

**Response**

> * The database name if success
> * An empty string in case of error

**Samples**

> ```
> POST/api/connection/databaseNameHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"ServerTypeId":"572bd576-8c92-4901-ab2a-b16e38144813","ConnectionString":"server=host01\instance01;database=db01;User Id=user01;Password=secret;"}
> ```
>
> Successful response:
>
> ```
> "db01"
> ```

## POST connection/detailInfo

Returns an array of connection details with paging.

**Request**

> | Field | NULL | Description | Note |
> | --- | --- | --- | --- |
> | **tenantId**  string (GUID) | Y | The id of the tenant |  |
> | **loadStoreProcSchema**  boolean | Y | Whether to load schema of stored procedures |  |
> | **loadInactiveConnections**  boolean | Y | Whether to load data of inactive connections |  |
> | **removeEmptyParent**  boolean | Y | Whether to remove empty parents |  |
> | **defaultChecked**  boolean | Y | Whether to tick the copy check-box by default, to be used in Copy Management |  |
> | **loadField**  boolean | Y | Whether to load data of query source fields |  |
> | **pagedIndex**  integer | Y | The index of the page |  |
> | **pagedSize**  integer | Y | The size of the page |  |

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **hashCode**  string | The hash code of the connections |  |
> | **connections**  string | An array of [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) objects |  |
> | **maxNumberOfRecords**  integer | The total number of records returned |  |

**Samples**

> ```
> POST/api/connection/detailInfoHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"tenantId":"45c747c5-a11a-48f4-b966-14819a07450f"}
> ```
>
> Sample response:
>
> ```
> {"hashCode":"27ab6cfbfec1bc319cde19a907a","connections":[],"maxNumberOfRecords":0}
> ```

## POST connection/detailInfoByQuerySources

Returns an array of connection objects filled with [QuerySourceField](https://devnet.logianalytics.com/hc/en-us/articles/4415504743703-QuerySourceField) data.

**Request**

> | Field | NULL | Description | Note |
> | --- | --- | --- | --- |
> | **querySourceIds**  array of strings |  | An array of string (GUID) values of [QuerySource](https://devnet.logianalytics.com/hc/en-us/articles/4415512017303-QuerySource) objects. |  |

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **connections**  string | An array of [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) objects filled with [QuerySourceField](https://devnet.logianalytics.com/hc/en-us/articles/4415504743703-QuerySourceField) data. |  |

**Samples**

> ```
> POST/api/connection/detailInfoByQuerySourcesHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"querySourceIds":["8f9a3d47-1d55-4d72-863e-39a365b224e5"]}
> ```
>
> Sample response:
>
> ```
> {"connections":[{"id":"61239e17-2d57-4b0a-b887-37491df9ab07","name":"Northwind","originalName":null,"serverTypeId":"572bd576-8c92-4901-ab2a-b16e38144813","databaseServer":"localhost","databaseUser":null,"serverTypeName":"MSSQL","connectionString":"3GTDfCloEoI/76VPjdIGGbycGQadvS6b0HzDKup7YL5AwTf+k70pBQLIWw88jwSzQXSLUnzCvg883cjkdS5","visible":true,"deleted":false,"relateToConnectionId":null,"tenantId":null,"dbSource":{"querySources":[{"id":"edbd5bdb-a931-4d66-8377-dd55270bf8ea","name":"dbo","parentCategoryId":null,"connectionId":"61239e17-2d57-4b0a-b887-37491df9ab07","querySources":[{"id":"8f9a3d47-1d55-4d72-863e-39a365b224e5","name":"Customers","realName":null,"type":"Table","parentQuerySourceId":null,"categoryId":"edbd5bdb-a931-4d66-8377-dd55270bf8ea","selected":true,"overwritten":false,"deleted":false,"connectionId":"61239e17-2d57-4b0a-b887-37491df9ab07","serverTypeId":"00000000-0000-0000-0000-000000000000","connectionName":null,"childs":null,"dataSourceCategoryId":null,"dataSourceCategoryName":null,"alias":null,"originalAlias":null,"querySourceFields":[{"name":"CustomerID","alias":"","dataType":"nchar","izendaDataType":"Text","allowDistinct":true,"visible":true,"filterable":false,"querySourceId":"8f9a3d47-1d55-4d72-863e-39a365b224e5","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":0,"position":1,"extendedProperties":null,"physicalChange":0,"approval":0,"existed":false,"checked":false,"matchedTenant":false,"functionName":null,"expression":null,"isRunningField":false,"supportDefaultTotal":null,"fullName":null,"calculatedTree":null,"reportId":null,"originalName":null,"originalId":"00000000-0000-0000-0000-000000000000","isParameter":false,"isCalculated":false,"isPredicated":false,"modelName":null,"targetValue":null,"relationColumn":null,"inputFeatures":null,"hasAggregatedFunction":false,"isCompositeField":false,"hasSupportDefaultTotal":true,"querySource":null,"querySourceName":null,"categoryName":null,"inaccessible":false,"originalAlias":null,"allowToSave":false,"filterLookupType":0,"filterLookupStatus":0,"dataBaseType":0,"fullPath":null,"isCheck":false,"id":"0aff7cd0-7da8-4c61-ad65-a8dda605a1d7","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"System Admin","modified":"2020-10-12T07:13:57.193","modifiedBy":null}],"querySourceCategoryName":"dbo","querySourceCategory":null,"modified":"2020-10-12T07:13:57.163","extendedProperties":null,"physicalChange":0,"approval":0,"existed":false,"checked":false,"belongToCopiedReport":false,"customDefinition":null,"isCustomQuerySource":false,"isCheck":false,"disabled":false,"databaseType":0,"fullPath":null,"indeterminate":false,"numOfChilds":0,"numOfCheckedChilds":0,"isLastPage":false}],"childs":null,"connection":null,"physicalChange":0,"existed":false,"deleted":false,"checked":false,"isCheck":false,"numOfChilds":0,"numOfCheckedChilds":0,"totalTableChildNodes":0,"totalTableCheckedNodes":0,"totalStoredProcedureChildNodes":0,"totalStoredProcedureCheckedNodes":0,"totalViewChildNodes":0,"totalViewCheckedNodes":0,"totalFunctionChildNodes":0,"totalFunctionCheckedNodes":0,"fullPath":null,"indeterminate":false,"isLastPage":false}]},"relationships":null,"querySourceCategories":[],"physicalChange":0,"copyDataConnector":false,"checked":false,"isCheck":false,"databaseName":"northwnd","fullPath":null,"indeterminate":false,"numOfChilds":0,"numOfCheckedChilds":0,"isLastPage":false}]}
> ```

## POST connection/invisible/{connection\_id}

Hides from Data Model and Reports all query sources in the connection specified by the {connection\_id} value.

**Request**

> No payload

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field populated

**Samples**

> ```
> POST/api/connection/invisible/866d8a41-3bd8-48d5-bc1e-9e4488c171c3HTTP/1.1
> ```
>
> Successful response (in case user has System Admin Permission):
>
> ```
> {"success":true,"messages":null}
> ```
>
> Response in case user does not have System Admin Permission:
>
> ```
> {"message":"You don't have permission to perform this action","detail":"NoPermission"}
> ```

## POST connection/loadDistinctConnections

Returns an array of distinct connections (by server type and database name) from a list of tenant ids.

**Request**

> | Field | Description | Note |
> | --- | --- | --- |
> | **tenantIds**  array of strings | An array of string (GUID) values. |  |

**Response**

> An array of [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) objects

**Samples**

> ```
> POST/api/connection/loadDistinctConnectionsHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"tenantIds":["e9e54aaf-64d8-4dbd-88c4-642f51ba16ec"]}
> ```
>
> Sample response:
>
> ```
> [{"id":"3cd79317-5d1b-4842-93d7-47abae6e0273","name":"Northwind","serverTypeId":"572bd576-8c92-4901-ab2a-b16e38144813","serverTypeName":"MSSQL","connectionString":"4d8jRon2cmwd8K1blELZB7RtRYUM76oW5ZOYxEcE4eCRy19pnCeeyM4ZFpAxX+dwIsv+p+3JKbZbJCdDyj6XXOlS88wnw9pNBuLfk3SxFJM=","visible":true,"deleted":false,"relateToConnectionId":null,"tenantId":"e9e54aaf-64d8-4dbd-88c4-642f51ba16ec","dbSource":{"querySources":[]},"relationships":null,"physicalChange":0,"checked":false,"databaseName":"Northwind","fullPath":null}]
> ```

## POST connection/loadRemoteSchema

Returns an enumeration of all supported objects (query sources) from a connection string.

**Request**

> Payload: a [SchemaRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492885143-SchemaRequest) object

**Response**

> A [SchemaResult](https://devnet.logianalytics.com/hc/en-us/articles/4415512051735-SchemaResult) object

**Samples**

> ```
> POST/api/connection/loadRemoteSchemaHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"connectionString":"1aBcD+=","serverType":"d968e96f-91dc-414d-9fd8-aef2926c9a18"}
> ```
>
> Successful response:
>
> ```
> {"dBSource":{"querySources":[{"id":"6ca15f34-b4cb-4fd7-8d55-77ee26ba6abe","name":"dbo","parentCategoryId":null,"connectionId":"00000000-0000-0000-0000-000000000000","querySources":[{"id":"bcf124c4-c5df-434a-bc4c-1638161d7949","name":"AWBuildVersion","type":"Table","parentQuerySourceId":null,"categoryId":null,"selected":false,"connectionName":null,"childs":null,"dataSourceCategoryId":null,"dataSourceCategoryName":null,"alias":null,"querySourceFields":[],"querySourceCategory":null,"modified":null,"extendedProperties":null,"physicalChange":0,"approval":0}],"childs":null,"connection":null,"physicalChange":0}]},"differentConnectionAndSchema":false,"success":true,"messages":null}
> ```

## POST connection/reloadRemoteSchema

Returns an enumeration of all supported objects (query sources) from an existing connection with detected changes.

**Request**

> Payload: a [SchemaRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492885143-SchemaRequest) object

**Response**

> A [SchemaResult](https://devnet.logianalytics.com/hc/en-us/articles/4415512051735-SchemaResult) object

**Samples**

> ```
> POST/api/connection/reloadRemoteSchemaHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"connectionId":"d91ee45e-f168-441d-81eb-7878cb2fa2ce","connectionString":"1aBcD+=","serverTypeId":"572bd576-8c92-4901-ab2a-b16e38144813"}
> ```
>
> Successful response:
>
> ```
> {"dBSource":{"querySources":[{"id":"024248ec-0058-49d3-a07c-f987bd300cae","name":"dbo","parentCategoryId":null,"connectionId":"d91ee45e-f168-441d-81eb-7878cb2fa2ce","querySources":[{"id":"bf21830d-bb38-4b17-853b-26df0cb56549","name":"Table01","type":"Table","parentQuerySourceId":null,"categoryId":"024248ec-0058-49d3-a07c-f987bd300cae","selected":true,"connectionId":"00000000-0000-0000-0000-000000000000","connectionName":null,"childs":null,"dataSourceCategoryId":null,"dataSourceCategoryName":null,"alias":null,"querySourceFields":[{"id":"69460143-6fd3-496c-8ddf-32e955801007","name":"TableId","alias":"","dataType":"nvarchar","visible":false,"filterable":false,"deleted":false,"querySourceId":"bf21830d-bb38-4b17-853b-26df0cb56549","parentId":null,"children":null,"modified":"2016-04-04T08:47:32.0000000+07:00","filteredValue":"","type":0,"position":0,"extendedProperties":"","physicalChange":0,"approval":0,"existed":true,"matchedTenant":false}],"querySourceCategory":null,"modified":null,"extendedProperties":null,"physicalChange":0,"approval":0,"existed":true}],"childs":null,"connection":null,"physicalChange":0,"existed":true}]},"differentConnectionAndSchema":false,"success":true,"messages":null}
> ```

## POST connection/validateSchema

Returns true if remote schema has not changed, otherwise returns false.

**Request**

> Payload: a [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) object

**Response**

> A boolean value

**Samples**

> ```
> POST/api/connection/validateSchemaHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"id":"dda3633e-659f-4e88-9955-4e20bded686c","serverType":"572bd576-8c92-4901-ab2a-b16e38144813","connectionString":"1aBcD+="}
> ```
>
> Sample response:
>
> ```
> true
> ```

## POST connection/verify

Validates a connection string.   
See also: [POST databaseSetup/testConnection](https://devnet.logianalytics.com/hc/en-us/articles/4415492759191-System-DB-and-License-APIs#post-databasesetup-testconnection)

**Request**

> Payload: a [DBSetupInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504716823-DBSetupInfo) object

**Response**

> A [ConnectionVerificationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492774167-ConnectionVerificationResult) object

**Samples**

> ```
> POST/api/connection/verifyHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"ServerTypeId":"572bd576-8c92-4901-ab2a-b16e38144813","ConnectionString":"server=host01\instance01;database=db01;User Id=user01;Password=secret;"}
> ```
>
> Successful response:
>
> ```
> {"serverNotValid":false,"databaseNotValid":false,"loginFail":false,"hasValidLicense":false,"success":true,"messages":[]}
> ```

## POST connection/visible/{connection\_id}

Restores the visibility of all query sources in the connection specified by the {connection\_id} value.

**Request**

> No payload

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field populated

**Samples**

> ```
> POST/api/connection/visible/866d8a41-3bd8-48d5-bc1e-9e4488c171c3HTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null}
> ```

## DELETE connection/{connection\_id}

Deletes the connection specified by the {connection\_id} value.

**Request**

> No payload

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field populated

**Samples**

> ```
> DELETE/api/connection/f5180bc0-7c07-48db-b672-e66a5adde027HTTP/1.1
> ```
>
> Successful response (in case user has System Admin Permission):
>
> ```
> {"success":true,"messages":null}
> ```
>
> Response in case user does not have System Asmin Permission):
>
> ```
> {"message":"You don't have permission to perform this action","detail":"NoPermission"}
> ```
