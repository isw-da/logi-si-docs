---
title: "WorkspaceDetailConsole"
id: 4415492905111
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492905111-WorkspaceDetailConsole
updated_at: 2021-12-10T03:10:04Z
---

# WorkspaceDetailConsole

# WorkspaceDetailConsole

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **reportDefinition**  object |  | A [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492852759-ReportDefinition) object |  |
| **destinationTenants**  array of objects |  | An array of [DestinationTenant](https://devnet.logianalytics.com/hc/en-us/articles/4415504719255-DestinationTenant) objects |  |
| **mappingType**  integer |  | Specifies the database mapping type.   * 1 = Schema Mapping * 2 = Database Mapping |  |
| **dataSourceConnections**  object |  | A [DataSourceConnections](https://devnet.logianalytics.com/hc/en-us/articles/4415492803223-DataSourceConnections) object |  |
| **sourceTenantConnections**  array of objects |  | An array of [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) objects |  |
| **sourceRoles**  array of objects |  | An array of [Role](https://devnet.logianalytics.com/hc/en-us/articles/4415492878231-Role) objects |  |
| **categoryType**  integer |  | * 0 = Report * 1 = Template * 2 = Dashboard |  |
| **sourceUserPermissions**  dynamic object |  | A dynamic object with field names equal to id of reports and dashboards, and field values populated by an array of [UserPermission](https://devnet.logianalytics.com/hc/en-us/articles/4415492896023-UserPermission) objects |  |
| **dashBoardDefinition**  object |  | A [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object |  |
| **sourceReports**  array of objects |  | An array of [Report](https://devnet.logianalytics.com/hc/en-us/articles/4415512028439-Report) objects |  |
| **reportDefinitions**  array of objects |  | An array of [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492852759-ReportDefinition) objects |  |

Inherited fields:

# WorkspaceDetail

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **workspaceTenants**  array of objects |  | An array of [WorkspaceTenantDetail](https://devnet.logianalytics.com/hc/en-us/articles/4415492908311-WorkspaceTenantDetail) objects. |  |
| **workspaceMappings**  array of objects |  | An array of [WorkspaceMappingDetail](https://devnet.logianalytics.com/hc/en-us/articles/4415492906391-WorkspaceMappingDetail) objects. |  |
| **copyOption**  object |  | A dynamic object |  |
| **copyAdvancedSettingOption**  object |  | A dynamic object |  |
| **copyTenantPermissionOption**  object |  | A dynamic object |  |
| **copyRolePermissionOption**  object |  | A dynamic object |  |
| **copyReportOption**  object |  | A dynamic object |  |
| **copyDashboardOption**  object |  | A dynamic object |  |
| **copyTemplateOption**  object |  | A dynamic object |  |
| **sourceConnections**  array of objects |  | An array of [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) objects. |  |
| **sourceReports**  array of objects |  | An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects. |  |
| **sourceTemplates**  array of objects |  | An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects. |  |
| **sourceDashboards**  array of objects |  | An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects. |  |
| **copiedRoles**  array of strings (GUIDs) |  | The list of ids of copied roles |  |
| **copiedRolePermissions**  array of strings (GUIDs) |  | The list of ids of copied roles |  |
| **allHashcodes**  dynamic object |  | Each field contains the hashcode for each copied section, e.g. advancedSettings, tenantPermission, etc. |  |
| **schedule**  object |  | A [WorkspaceSchedule](https://devnet.logianalytics.com/hc/en-us/articles/4415492907415-WorkspaceSchedule) object | New in version 3.9.3. |

Inherited fields:

## Workspace

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **name**  string |  | The name of the workspace |  |
| **description**  string |  | The description of the workspace |  |
| **tenantId**  string (GUID) | Y | The id of the tenant if available |  |
| **tenantName**  string |  | The name of the tenant |  |
| **ownerId**  string (GUID) | Y | The id of the owner |  |
| **copyOnlySettings**  boolean |  | Does user select to copy only settings | New in version 3.9.3. |
| **copyDataConnector**  boolean |  | Does user select to copy data connectors | New in version 3.9.3. |
| **copySystemConfiguration**  boolean |  | Does user select to copy system configuration | New in version 3.9.3. |
| **copyGoogleMapConfiguration**  boolean |  | Does user select to copy Google maps configuration | New in version 3.9.3. |
| **copyReportConfiguration**  boolean |  | Does user select to copy report configuration | New in version 3.9.3. |
| **copyEmailConfiguration**  boolean |  | Does user select to copy email configuration | New in version 3.9.3. |
| **copyRoles**  boolean |  | Does user select to copy roles |  |
| **copyRolePermission**  boolean |  | Does user select to copy role permissions |  |
| **copyAdvancedSettings**  boolean |  | Does user select to copy advanced settings |  |
| **copyDataModel**  boolean |  | Does user select to copy data model |  |
| **copyReport**  boolean |  | Does user select to copy reports |  |
| **copyDashboard**  boolean |  | Does user select to copy dashboards |  |
| **copyTenantPermissions**  boolean |  | Does user select to copy tenant permissions |  |
| **sourceId**  string (GUID) | Y | The id of the source |  |
| **selectAllTenants**  boolean |  | Does user select all tenants as destination |  |
| **sourceHashCode**  string |  | Hashcode for source |  |
| **copyPositionID**  boolean |  | Whether system admin select to copy positionID or not | New in version 2.16.0. |

Inherited fields:

### Entity

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id of this object   Example: `572bd576-8c92-4901-ab2a-b16e38144813` | Allow null incase insert a new entity |
| **state**  integer |  | The entity state of this object   * 0 = None * 1 = Insert * 2 = Delete * 3 = Update |  |
| **deleted**  boolean |  | Is this object deleted |  |
| **inserted**  boolean |  | Is this object inserted |  |
| **version**  string | Y | The version |  |
| **created**  datetime in ISO 8601 format | Y | The created datetime |  |
| **createdBy**  string |  | The creator |  |
| **modified**  datetime in ISO 8601 format | Y | The modification datetime |  |
| **modifiedBy**  string |  | The user who last modified this object |  |

**Sample**:

```
{"workspaceTenants":[{"destinationConnections":[],"sourceConnections":[],"tenantName":"Tenant 1","tenantUniqueName":"T1","workspaceId":"49d886bc-45be-4acf-8ebe-4de775546f8c","tenantId":"9ef4b0af-2485-4050-91b9-cf149d999afd","status":0,"id":null,"state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}],"workspaceMappings":[{"workspaceMappingTenants":[],"workspaceId":"49d886bc-45be-4acf-8ebe-4de775546f8c","fromDatabaseName":"[MSSQL] Northwind","type":2,"fromObject":"","toDatabaseName":"","toObject":"","isGlobal":false,"id":"b0cd65d5-762a-48be-afc8-5bc9678aebd0","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}],"copyOption":null,"sourceConnections":[{"id":"e3dfb160-0814-4d13-b801-29b5b0d97664","name":"1234 1351","serverTypeId":"572bd576-8c92-4901-ab2a-b16e38144813","serverTypeName":"MSSQL","connectionString":"secret","visible":true,"deleted":false,"relateToConnectionId":null,"tenantId":null,"dbSource":{"querySources":[{"id":"e7a70258-d781-45ac-a346-7e304f6c2291","name":"dbo","parentCategoryId":null,"connectionId":"e3dfb160-0814-4d13-b801-29b5b0d97664","querySources":[{"id":"8817a241-a858-423c-b64e-3bbf99e45318","name":"Categories","type":"Table","parentQuerySourceId":null,"categoryId":"e7a70258-d781-45ac-a346-7e304f6c2291","selected":false,"connectionId":"00000000-0000-0000-0000-000000000000","connectionName":null,"childs":null,"dataSourceCategoryId":null,"dataSourceCategoryName":null,"alias":null,"querySourceFields":[{"name":"CategoryID","alias":"","dataType":"int","izendaDataType":"Numeric","allowDistinct":true,"visible":true,"filterable":true,"deleted":false,"querySourceId":"8817a241-a858-423c-b64e-3bbf99e45318","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":0,"position":1,"extendedProperties":"{\"PrimaryKey\":true}","physicalChange":0,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"fullName":null,"calculatedTree":null,"reportId":null,"originalName":null,"isParameter":false,"isCalculated":false,"hasAggregatedFunction":false,"querySource":null,"fullPath":null,"id":"549a4a2b-216d-48f7-8e00-eec2277351ac","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":"2016-08-22T04:32:32.173","modifiedBy":null}],"querySourceCategoryName":null,"querySourceCategory":null,"modified":"2016-08-22T04:32:31.85","extendedProperties":null,"physicalChange":0,"approval":0,"existed":false,"checked":true,"fullPath":null}],"childs":null,"connection":null,"physicalChange":0,"existed":false,"checked":true,"fullPath":null}]},"relationships":null,"physicalChange":0,"checked":true,"databaseName":"Northwind","fullPath":null}],"name":"235","description":"dgsd","tenantId":null,"ownerId":"9f58703e-0dff-4690-9dc6-c595a6fd84e1","deleted":false,"copyRoles":false,"copyRolePermission":false,"copyAdvancedSettings":false,"copyDataModel":false,"sourceId":"00000000-0000-0000-0000-000000000000","selectAllTenants":false,"id":"49d886bc-45be-4acf-8ebe-4de775546f8c","state":0,"inserted":true,"version":null,"created":"2016-08-22T04:36:09.063","createdBy":null,"modified":"2016-08-22T04:36:09.063","modifiedBy":null}
```
