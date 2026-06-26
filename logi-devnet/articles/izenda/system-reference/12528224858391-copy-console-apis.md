---
title: "Copy Console APIs"
id: 12528224858391
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528224858391-Copy-Console-APIs
updated_at: 2023-02-23T16:06:43Z
---

# Copy Console APIs

# Copy Console APIs

The Izenda Copy Console Tool will allow you to copy templates, reports and dashboards from one Izenda Configuration database to another or within one configuration database.

The following APIs are used internally for the tool.

## List of APIs

| API | Purpose |
| --- | --- |
| [POST copyManagement/console/validate/sourcedata](#post-copymanagement-console-validate-sourcedata) | Returns a distinct list of connections from selected tenant, reports, templates and dashboards. |
| [POST copyManagement/console/validate/dataconsistent](#post-copymanagement-console-validate-dataconsistent) | Validates for consistency between source and destination, for example database server types, database mappings and data models. |
| [POST copyManagement/console/validate/listusingfield](#post-copymanagement-console-validate-listusingfield) | Returns a list of all using fields in source.  New in version 2.6.21. |
| [POST copyManagement/console/validate/source](#post-copymanagement-console-validate-source) | Validates that ids of source tenant, reports, templates and dashboards are correct. |
| [POST copyManagement/console/validate/destination](#post-copymanagement-console-validate-destination) | Validates that destination tenants, database mappings and role mappings are correct. |
| [POST copyManagement/console/loadreport](#post-copymanagement-console-loadreport) | Returns all report/template and related data to be copied to another system. |
| [POST copyManagement/console/copyreport](#post-copymanagement-console-copyreport) | Copies report and related data to a system. |
| [POST copyManagement/console/updatesubreport](#post-copymanagement-console-updatesubreport) | Updates the content of copied reports to match destination state. |
| [POST copyManagement/console/loaddashboard](#post-copymanagement-console-loaddashboard) | Returns all dashboard and related data to be copied to another system. |
| [POST copyManagement/console/copydashboard](#post-copymanagement-console-copydashboard) | Copies dashboard and related data to a system. |
| [POST copyManagement/console/listreport](#post-copymanagement-console-listreport) | Returns a list of report definitions. |

## API Workflow

[![../_images/Copy_Console_API_Workflow.png](https://devnet.logianalytics.com/hc/article_attachments/12528148321303/copy_console_api_workflow_428x635.png)](https://devnet.logianalytics.com/hc/article_attachments/12528164267799/copy_console_api_workflow.png)

## POST copyManagement/console/validate/sourcedata

Returns a distinct list of connections from selected tenant, reports, templates and dashboards.

**Request**

> Payload: an [InputWorkspace](https://devnet.logianalytics.com/hc/en-us/articles/12528281839511-InputWorkspace) object with **sourceTenantId**, **reportIds**, **templateIds** and **dashboardIds** fields populated

**Response**

> An [InputWorkspace](https://devnet.logianalytics.com/hc/en-us/articles/12528281839511-InputWorkspace) object with **dataInSource** field populated

**Samples**

> ```
> POST/api/copyManagement/console/validate/sourcedataHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"sourceTenantId":"78e5699a-6a67-471f-8374-529a80777754","reportIds":["4b6d592e-ad29-408d-a3f2-845776d555db"]}
> ```
>
> Sample response:
>
> ```
> {"sourceTenantId":null,"reportIds":[],"reportIdsLineNumber":[],"templateIds":[],"templateIdsLineNumber":[],"dashboardIds":[],"dashboardIdsLineNumber":null,"destinationTenants":null,"dataInSource":{"dbSetupInfo":{"serverTypeId":"3d4916d1-5a41-4b94-874f-5bedacb89656","serverTypeName":"[MYSQL] MySQL","connectionString":"encrypted","connectionId":"00000000-0000-0000-0000-000000000000"},"sourceConnections":"To be updated"},"sourceLineNumber":0,"destinationLineNumber":0,"sourceTenantLineNumber":0}
> ```

## POST copyManagement/console/validate/dataconsistent

Validates for consistency between source and destination, for example database server types, database mappings and data models.

**Request**

> Payload: an [InputWorkspace](https://devnet.logianalytics.com/hc/en-us/articles/12528281839511-InputWorkspace) object with **dataInSource** field populated

**Response**

> An array of strings containing the errors if available

**Samples**

> To be updated

## POST copyManagement/console/validate/listusingfield

Returns a list of all using fields in source

New in version 2.6.21.

**Request**

> Payload: an [InputWorkspace](https://devnet.logianalytics.com/hc/en-us/articles/12528281839511-InputWorkspace) object with **dataInSource** field populated

**Response**

> An array of strings containing the using fields.

**Samples**

> Request payload:
>
> ```
> {"reportIds":["897d01a6-ed6e-46c2-a7c1-d68e1dab5fb9","34c92a53-fe74-4fb3-b62e-d1ca3204236d"],"dashboardIds":["9d2f1d51-0e3d-44db-bfc7-da94a7581bfe"]}
> ```
>
> Sample response:
>
> ```
> ["[con;#0].[cat;#0].[Employees].[ReportsTo]","[con;#0].[cat;#0].[Employees].[EmployeeID]","[con;#0].[cat;#0].[Employees].[FirstName]","[con;#0].[cat;#0].[Employees].[LastName]"]
> ```

## POST copyManagement/console/validate/source

Validates that ids of source tenant, reports, templates and dashboards are correct.

**Request**

> Payload: an [InputWorkspace](https://devnet.logianalytics.com/hc/en-us/articles/12528281839511-InputWorkspace) object

**Response**

> An array of strings containing the errors if available

**Samples**

> To be updated

## POST copyManagement/console/validate/destination

Validates that destination tenants, database mappings and role mappings are correct.

**Request**

> Payload: an array of [DestinationTenant](https://devnet.logianalytics.com/hc/en-us/articles/12528281570583-DestinationTenant) objects

**Response**

> An array of strings containing the errors if available

**Samples**

> To be updated

## POST copyManagement/console/loadreport

Returns all report/template and related data to be copied to another system.

**Request**

> Payload: a [ReportParameter](https://devnet.logianalytics.com/hc/en-us/articles/12528282666391-ReportParameter) object

**Response**

> A [WorkspaceDetailConsole](https://devnet.logianalytics.com/hc/en-us/articles/12528283547415-WorkspaceDetailConsole) object with **reportDefinition**, **sourceTenantConnections**, **dataSourceConnections**, **sourceRoles** and **sourceUserPermissions** fields populated

**Samples**

> To be updated

## POST copyManagement/console/copyreport

Copies report and related data to a system.

**Request**

> Payload: a [WorkspaceDetailConsole](https://devnet.logianalytics.com/hc/en-us/articles/12528283547415-WorkspaceDetailConsole) object, which has been fully-populated from [POST copyManagement/console/loadreport](#post-copymanagement-console-loadreport)

**Response**

> An array of [CopyStatus](https://devnet.logianalytics.com/hc/en-us/articles/12528281235479-CopyStatus) objects

**Samples**

> Skipped because of too much data

## POST copyManagement/console/updatesubreport

Updates the content of copied reports to match destination state.

**Request**

> Payload: an [UpdateSubReportInput](https://devnet.logianalytics.com/hc/en-us/articles/12528283319831-UpdateSubReportInput) object, with **copyStatus** field populated from the result of [POST copyManagement/console/copyreport](#post-copymanagement-console-copyreport)

**Response**

> An array of [UpdateSubReportStatus](https://devnet.logianalytics.com/hc/en-us/articles/12528298662295-UpdateSubReportStatus) objects

**Samples**

> To be updated

## POST copyManagement/console/loaddashboard

Returns all dashboard and related data to be copied to another system.

**Request**

> Payload: a [LoadDashboard](https://devnet.logianalytics.com/hc/en-us/articles/12528281923607-LoadDashboard) object

**Response**

> A [WorkspaceDetailConsole](https://devnet.logianalytics.com/hc/en-us/articles/12528283547415-WorkspaceDetailConsole) object with **dashBoardDefinition**, **sourceReports**, **reportDefinitions**, **sourceRoles** and **sourceUserPermissions** fields populated

**Samples**

> Skipped because of too much data

## POST copyManagement/console/copydashboard

Copies dashboard and related data to a system.

**Request**

> Payload: a fully-populated [WorkspaceDetailConsole](https://devnet.logianalytics.com/hc/en-us/articles/12528283547415-WorkspaceDetailConsole) object

**Response**

> An array of [CopyStatus](https://devnet.logianalytics.com/hc/en-us/articles/12528281235479-CopyStatus) objects

**Samples**

> Skipped because of too much data

## POST copyManagement/console/listreport

Returns a list of report definitions.

**Request**

> Payload: an array of [ReportKey](https://devnet.logianalytics.com/hc/en-us/articles/12528282642071-ReportKey) objects

**Response**

> An array of [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/12528297929111-ReportDefinition) objects

**Samples**

> To be updated
