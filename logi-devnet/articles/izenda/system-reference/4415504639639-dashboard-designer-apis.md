---
title: "Dashboard Designer APIs"
id: 4415504639639
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504639639-Dashboard-Designer-APIs
updated_at: 2021-12-10T03:08:08Z
---

# Dashboard Designer APIs

# Dashboard Designer APIs

The **Dashboard Designer** page allows users to:

|  |  |
| --- | --- |
| * select a preset layout * add report parts to dashboard * customize dashboard layout * edit dashboard description and background * copy and move dashboard | * switch to presentation mode * configure sharing access * add subscriptions and scheduled delivery * print dashboards * email |

This page documents the APIs related to dashboard designer.

## Summary

| API | Purpose | Usage in Izenda Front-end |
| --- | --- | --- |
| [POST dashboard](#post-dashboard) | Saves a dashboard. | Dashboard Designer > Save (As) > OK |
| [POST dashboard/loadFilterFieldData](#post-dashboard-loadfilterfielddata) | Returns data source field data for Equivalence operators in filter. | Dashboard Designer/Viewer with Equivalence filter |
| [POST dashboard/loadFilterFieldDataAsTree](#id1) | Returns data source field data in a hierarchy for Equivalence operators in filter. | To be updated |
| [POST dashboard/loadPartialFilterFieldData](#post-dashboard-loadpartialfilterfielddata) | Returns paged data source field data for Equivalence operators in filter. | To be updated |
| [POST dashboard/loadPartialFilterFieldDataAsTree](#post-dashboard-loadpartialfilterfielddataastree) | Returns paged data source field data in a hierarchy for Equivalence operators in filter. | To be updated |
| [POST dashboard/loadFilterComparisonFields](#post-dashboard-loadfiltercomparisonfields) | Returns a list of available dashboard filter fields for a common filter field. | To be updated |
| [POST dashboard/detectDashboardChange](#post-dashboard-detectdashboardchange) | Verifies that all dashboard filters are not changed. | To be updated |
| [POST dashboard/loadDashboard](#post-dashboard-loaddashboard) | Returns a dashboard object. | Open an existing dashboard |
| [POST dashboard/loadSubscriptions](#post-dashboard-loadsubscriptions) | Returns a list of dashboard subscriptions. | Dashboard Designer > Schedule |
| [POST dashboard/subscription/validate](#post-dashboard-subscription-validate) | Validates a subscription schedule and delivery template. | Dashboard Designer > Schedule > Add Schedule > OK |
| [POST dashboard/subscriptions](#post-dashboard-subscriptions) | Saves a list of dashboard subscriptions. | Dashboard Designer > Schedule > Add Schedule > OK |
| [POST dashboard/validateDashboardName](#post-dashboard-validatedashboardname) | Validates dashboard name. | Dashboard Designer > Save (As) > Dashboard Name |
| [POST dashboard/validate](#post-dashboard-validate) | Validates dashboard. | Dashboard Designer > Save (As) > OK |
| [POST dashboard/validateGlobalDashboard](#post-dashboard-validateglobaldashboard) | Validates that dashboard contains only global report parts. | Dashboard Designer > Save (As) > Save into Global Categories > OK |
| [POST dashboard/previewDashboardPartData](#post-dashboard-previewdashboardpartdata) | Returns data for a dashboard part, given the dashboard part definition. | Dashboard Designer > create a Dashboard Part |
| [POST dashboard/loadDashboardPartData](#post-dashboard-loaddashboardpartdata) | Returns data for a dashboard part, given the dashboard part id. | Not used |
| [POST dashboard/loadDashboardPartData2](#post-dashboard-loaddashboardpartdata2) | Returns data for a dashboard part, given the dashboard part id, optionally loads default data.  New in version 2.2.0. | Dashboard Viewer |
| [GET dashboard/dashboardPart/{dashboard\_part\_id}](#get-dashboard-dashboardpart-dashboard-part-id) | Returns dashboard part definition. | To be updated |
| [POST dashboard/accesses/validate](#post-dashboard-accesses-validate) | Validates dashboard access. | Dashboard Designer > Save (As) |
| [GET dashboard/allowedSavingCategories](#get-dashboard-allowedsavingcategories) | Deprecated since version 2.0.0: superseded by [POST dashboard/allowedSavingCategories](#post-dashboard-allowedsavingcategories) and [POST dashboard/allowedSavingSubCategories](#post-dashboard-allowedsavingsubcategories)  Returns an array of allowed saving categories for dashboard. | Not used |
| [POST dashboard/allowedSavingCategories](#post-dashboard-allowedsavingcategories) | Returns an array of allowed saving categories for dashboard, with total number of items. | Dashboard Designer > Save (As) > Category |
| [POST dashboard/allowedSavingSubCategories](#post-dashboard-allowedsavingsubcategories) | Returns an array of allowed saving sub-categories for dashboard, with total number of items. | Dashboard Designer > Save (As) > Sub-category |
| [POST dashboard/loadCommonFilters](#post-dashboard-loadcommonfilters) | Returns a list of report filters that are common among all report parts from a dashboard definition. | Dashboard Viewer |
| [GET dashboard/commonFilters/{dashboard\_id}](#get-dashboard-commonfilters-dashboard-id) | Returns the saved common filters from a dashboard\_id. | Dashboard Viewer |
| [POST dashboard/updateRenderingTime](#post-dashboard-updaterenderingtime) | Updates the rendering time of a dashboard. | Dashboard Viewer |
| [POST dashboard/draft](#post-dashboard-draft) | Saves a dashboard as draft. | Dashboard Designer > Print before saving |
| [GET dashboard/draft/{dashboard\_id}](#get-dashboard-draft-dashboard-id) | Returns a dashboard from draft. | To be updated |
| [GET dashboard/embeddedReports/{dashboard\_part\_id}](#get-dashboard-embeddedreports-dashboard-part-id) | Returns reports and report parts embedded inside the specified dashboard part.  New in version 2.2.0. | Dashboard Viewer |
| [GET dashboard/loadRelatedDashboardParts/{dashboard\_id}](#get-dashboard-loadrelateddashboardparts-dashboard-id) | Returns a nested list of dashboard part ids, where each inner list contains dashboard part ids using report parts in a same report.  New in version 2.2.0. | Dashboard Viewer |

## POST dashboard

Saves a dashboard.

**Request**

> Payload: a [DashboardSavingParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415492791703-DashboardSavingParameter) object

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **success**  boolean | Is the save successful |  |
> | **dashboard**  object | A [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object |  |

**Samples**

> ```
> POST/api/dashboardHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"saveAs":false,"dashboard":{"accesses":[],"name":"TestDashboard01","description":null,"categoryName":"Category01","subCategoryName":"Category01","tenantId":null,"imageUrl":null,"stretchImage":false,"id":null,"state":0,"inserted":false,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null,"showFilterDescription":true,"categoryId":null,"subCategoryId":null,"dashboardParts":[{"isDirty":false,"dashboardId":null,"positionX":0,"positionY":0,"width":12,"height":4,"title":"text","isBackSide":false,"isFullScreenMode":false,"state":1,"type":"text","bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}},"id":null,"numberOfRecord":-1,"dashboardPartContent":{"contentTitle":{"text":"A Title","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"desc","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"filters":[]},{"isDirty":false,"dashboardId":null,"positionX":0,"positionY":4,"width":6,"height":4,"isBackSide":false,"isFullScreenMode":false,"state":1,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}},"id":null,"numberOfRecord":-1,"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"filters":[]},{"isDirty":false,"dashboardId":null,"positionX":6,"positionY":4,"width":6,"height":4,"isBackSide":false,"isFullScreenMode":false,"state":1,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}},"id":null,"numberOfRecord":-1,"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"filters":[]}],"commonFilterFields":[],"subscriptions":[]}}
> ```
>
> Sample response:
>
> ```
> {"success":true,"dashboard":{"commonFilterFields":[],"accesses":[],"subscriptions":[],"dashboardParts":[{"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","positionX":0,"positionY":0,"width":12,"height":4,"title":"text","state":0,"type":"text","id":"0cd06216-ee6f-4dee-9a8a-23d12f845e34","numberOfRecord":-1,"dashboardPartContent":{"contentTitle":{"text":"A Title","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"desc","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"filters":[],"reportId":null,"reportPartId":null,"filterDescription":null,"inserted":false,"version":1,"created":"2016-08-11T03:20:08.7766703","createdBy":null,"modified":"2016-08-11T03:20:08.7766703","modifiedBy":null},{"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","positionX":0,"positionY":4,"width":6,"height":4,"title":null,"state":0,"type":null,"id":"6b8a0f81-b0ba-4320-bd84-0cd6f61b2842","numberOfRecord":-1,"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"filters":[],"reportId":null,"reportPartId":null,"filterDescription":null,"inserted":false,"version":1,"created":"2016-08-11T03:20:08.7922799","createdBy":null,"modified":"2016-08-11T03:20:08.7922799","modifiedBy":null},{"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","positionX":6,"positionY":4,"width":6,"height":4,"title":null,"state":0,"type":null,"id":"042035e9-77e7-4102-baa7-e37eb5ed00d5","numberOfRecord":-1,"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"filters":[],"reportId":null,"reportPartId":null,"filterDescription":null,"inserted":false,"version":1,"created":"2016-08-11T03:20:08.7922799","createdBy":null,"modified":"2016-08-11T03:20:08.7922799","modifiedBy":null}],"name":"TestDashboard01","description":null,"categoryId":"709742d0-2300-4f99-8cdd-1e1675d7c2e7","categoryName":"Category01","subCategoryId":"17a6e855-f211-4a5c-b990-3463d453cecc","subCategoryName":"Category01","tenantId":null,"imageUrl":null,"stretchImage":false,"backgroundColor":null,"showFilterDescription":true,"lastViewed":null,"id":"a496ad94-fe92-48d5-a285-e45be738921f","state":0,"inserted":false,"version":1,"created":"2016-08-11T03:20:08.7766703","createdBy":null,"modified":"2016-08-11T03:20:08.7766703","modifiedBy":null}}
> ```

## POST dashboard/loadFilterFieldData

Returns data source field data for Equivalence operators in filter.

**Request**

> | Field | Description | Note |
> | --- | --- | --- |
> | **dashboard**  object | A [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object |  |
> | **commonFilterName**  string | The filter name |  |

**Response**

> An array of string values

**Samples**

> To be updated

## POST dashboard/loadFilterFieldDataAsTree

Returns data source field data in a hierarchy for Equivalence operators in filter.

**Request**

> | Field | Description | Note |
> | --- | --- | --- |
> | **dashboard**  object | A [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object |  |
> | **commonFilterName**  string | The filter name |  |

**Response**

> An array of [ValueTreeNode](https://devnet.logianalytics.com/hc/en-us/articles/4415492903063-ValueTreeNode) objects

**Samples**

> To be updated

## POST dashboard/loadPartialFilterFieldData

Returns paged data source field data for Equivalence operators in filter.

**Request**

> A [DashboardFilterFieldPagedRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492784663-DashboardFilterFieldPagedRequest) object
>
> **Notes:** Key for [SearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415512052759-SearchCriteria) support to search: “Filter”

**Response**

> A [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) object, with **result** field containing an array of string values

**Samples**

> To be updated

## POST dashboard/loadPartialFilterFieldDataAsTree

Returns paged data source field data in a hierarchy for Equivalence operators in filter.

**Request**

> A [DashboardFilterFieldPagedRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492784663-DashboardFilterFieldPagedRequest) object

**Response**

> A [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) object, with **result** field containing an array of [ValueTreeNode](https://devnet.logianalytics.com/hc/en-us/articles/4415492903063-ValueTreeNode) objects

**Samples**

> To be updated

## POST dashboard/loadFilterComparisonFields

Returns a list of available dashboard filter fields for a common filter field.

**Request**

> | Field | Description | Note |
> | --- | --- | --- |
> | **dashboard**  object | A [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object |  |
> | **commonFilterName**  string | The filter name |  |

**Response**

> An array of [ReportFilterField](https://devnet.logianalytics.com/hc/en-us/articles/4415504761879-ReportFilterField) objects

**Samples**

> To be updated

## POST dashboard/detectDashboardChange

Verifies that all dashboard filters are not changed.

**Request**

> Payload: a [DashboardSavingParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415492791703-DashboardSavingParameter) object

**Response**

> * true if all filters are not changed
> * false if changed

**Samples**

> ```
> POST/api/dashboard/detectDashboardChangeHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"saveAs":false,"dashboard":{"accesses":[],"name":"Example Dashboard Name 2","description":null,"categoryName":null,"subCategoryName":null,"tenantId":null,"backgroundColor":"","imageUrl":null,"stretchImage":false,"id":"ce822672-feb2-4954-a95b-33bc118dfd8f","state":3,"inserted":false,"version":1,"created":"2016-09-16T04:34:10.7646747","createdBy":null,"modified":"2016-09-16T04:34:10.7646747","modifiedBy":null,"showFilterDescription":true,"categoryId":null,"subCategoryId":null,"dashboardParts":[{"isDirty":true,"dashboardId":"ce822672-feb2-4954-a95b-33bc118dfd8f","positionX":0,"positionY":0,"width":12,"height":4,"title":"Grid/Grid/Chart","isBackSide":false,"filterDescription":"","isFullScreenMode":false,"numberOfRecord":0,"state":1,"type":"reportPart","bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}},"reportId":"b35b9ff8-dc1f-4da3-971a-ab955dbf1940","reportPartId":"64b06c13-5e38-4eb8-9434-f905f8d32faa","id":null,"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"textTypeContent":""},"filters":[]},{"isDirty":true,"dashboardId":"ce822672-feb2-4954-a95b-33bc118dfd8f","positionX":0,"positionY":4,"width":12,"height":4,"title":"Test/Name/Chart","isBackSide":true,"filterDescription":"Freight = [All]","isFullScreenMode":false,"numberOfRecord":0,"state":1,"type":"reportPart","bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}},"reportId":"4a443b06-0c71-400f-bc99-0a15204c0d9b","reportPartId":"45e8e8bd-e4ee-409e-812a-be68337993e9","id":null,"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"textTypeContent":""},"filters":[{"filterFieldId":"0abc3c48-3e9b-4003-949b-a398a389d9bf","value":"[All]","operatorId":"003c0e13-cc3c-412f-8fee-1cf21aa51e31","isCommon":false,"filterField":{"filterList":[],"isDirty":false,"connectionName":"sqlserver","querySourceCategoryName":"dbo","sourceFieldName":"Freight","sourceFieldVisible":true,"sourceFieldFilterable":true,"sourceDataObjectName":"Orders","dataType":"Money","filterId":"a0d603e7-3fa6-479c-90dd-3b08565df79d","querySourceFieldId":"20f25b2e-2d19-473e-bea6-49f3416d9a0e","querySourceType":"Table","querySourceId":"d579abf2-17de-4f5e-8cac-854ef245164d","relationshipId":null,"alias":"Freight","position":1,"visible":false,"required":false,"cascading":true,"operatorId":"003c0e13-cc3c-412f-8fee-1cf21aa51e31","operatorSetting":null,"value":"[All]","sortType":"Unsorted","fontFamily":"Roboto","fontSize":8,"textColor":null,"backgroundColor":null,"fontBold":false,"fontItalic":false,"fontUnderline":false,"id":"0abc3c48-3e9b-4003-949b-a398a389d9bf","state":0,"modified":null,"dateTimeNow":"","selected":false,"isParameter":false,"dataFormatId":null},"operatorSetting":null,"displayName":"Freight"}]}],"commonFilterFields":[],"subscriptions":[]}}
> ```
>
> Sample response:
>
> ```
> false
> ```

## POST dashboard/loadDashboard

Returns a dashboard object.

**Request**

> Payload: a [DashboardParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415492786327-DashboardParameter) object

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **success**  boolean | Should be true |  |
> | **dashboard**  object | A [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object |  |

**Samples**

> ```
> POST/api/dashboard/loadDashboardHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f"}
> ```
>
> Sample response:
>
> ```
> {"success":true,"dashboard":{"commonFilterFields":[],"accesses":[],"subscriptions":[],"dashboardParts":[{"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","type":null,"title":null,"reportId":null,"reportPartId":null,"filterDescription":null,"numberOfRecord":-1,"positionX":0,"positionY":4,"width":6,"height":4,"filters":[],"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"id":"6b8a0f81-b0ba-4320-bd84-0cd6f61b2842","state":0,"inserted":true,"version":1,"created":"2016-08-11T03:20:08.793","createdBy":null,"modified":"2016-08-11T03:20:08.793","modifiedBy":null},{"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","type":"text","title":"text","reportId":null,"reportPartId":null,"filterDescription":null,"numberOfRecord":-1,"positionX":0,"positionY":0,"width":12,"height":4,"filters":[],"dashboardPartContent":{"contentTitle":{"text":"A Title","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"desc","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"id":"0cd06216-ee6f-4dee-9a8a-23d12f845e34","state":0,"inserted":true,"version":1,"created":"2016-08-11T03:20:08.777","createdBy":null,"modified":"2016-08-11T03:20:08.777","modifiedBy":null},{"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","type":null,"title":null,"reportId":null,"reportPartId":null,"filterDescription":null,"numberOfRecord":-1,"positionX":6,"positionY":4,"width":6,"height":4,"filters":[],"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"id":"042035e9-77e7-4102-baa7-e37eb5ed00d5","state":0,"inserted":true,"version":1,"created":"2016-08-11T03:20:08.793","createdBy":null,"modified":"2016-08-11T03:20:08.793","modifiedBy":null}],"name":"TestDashboard01","description":null,"categoryId":"e443f282-eba4-422d-a7c3-32560a268373","categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":null,"imageUrl":null,"stretchImage":false,"backgroundColor":null,"showFilterDescription":true,"lastViewed":null,"id":"a496ad94-fe92-48d5-a285-e45be738921f","state":0,"inserted":true,"version":2,"created":"2016-08-11T03:20:08.777","createdBy":null,"modified":"2016-08-11T03:44:01.27","modifiedBy":null}}
> ```

## POST dashboard/loadSubscriptions

Returns a list of dashboard subscriptions.

**Request**

> Payload: a [SubscriptionPagedRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492887831-SubscriptionPagedRequest) object
>
> Note
>
> The keys for [SearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415512052759-SearchCriteria) that this API support:   
> - All   
> - Name   
> - Schedule   
> - FilterValueSelection   
> - DeliveryType   
> - DeliveryMethod   
> - Recipients   
> - LastSuccessfulRun   
> - LastSuccessfulRunFrom   
> - LastSuccessfulRunTo   
> - NextScheduledRun   
> - NextScheduledRunFrom   
> - NextScheduledRunTo   
> - Keyword   
> - ReportingType   
> - ReportDashboardName   
> - Type   
> - RecurrenceType   
> - ExportFileType   
> - CreatedBy

**Response**

> A [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) object, with **result** field containing an array of [Subscription](https://devnet.logianalytics.com/hc/en-us/articles/4415512058519-Subscription) objects

**Samples**

> ```
> POST/api/dashboard/loadSubscriptionsHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","isSubscription":true,"tenantId":null,"criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"name","descending":true}]}
> ```
>
> Sample response:
>
> ```
> {"result":[{"name":"Everyday at 2 PM","schedule":"Occurs every day effective 08/11/2016 at 02:00 PM (UTC-06:00) Central Time (US & Canada)","type":"Subscription Report","timeZoneName":"(UTC-06:00) Central Time (US & Canada)","timeZoneValue":"Central Standard Time","startDate":"2016-08-11T00:00:00","startDateUtc":"0001-01-01T00:00:00","startTime":"2016-08-11T14:00:00","recurrenceType":2,"recurrencePattern":1,"recurrencePatternSetting":{"recurrenceWeek":1,"selectedDayValue":"5"},"isEndless":true,"isScheduled":false,"occurrence":0,"endDate":null,"endDateUtc":null,"deliveryType":"Email","deliveryMethod":"Link","exportFileType":null,"exportAttachmentType":null,"emailSubject":"{reportName}","emailBody":null,"reportId":null,"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","filterValueSelection":"","recipients":null,"lastSuccessfulRun":"The schedule has not started.","nextScheduledRun":"08/11/2016 02:00 PM (UTC-06:00) Central Time (US & Canada)","isSubscription":true,"subscriptionFilterFields":[],"subscriptionCommonFilterFields":[],"tempId":null,"id":"df6d04e8-ce7c-45ea-b485-046ecfe20720","state":0,"inserted":true,"version":1,"created":null,"createdBy":"","modified":"2016-08-11T06:48:39.777","modifiedBy":""}],"pageIndex":1,"pageSize":10,"total":1}
> ```

## POST dashboard/subscription/validate

Validates a subscription schedule and delivery template.

**Request**

> | Field | Description | Note |
> | --- | --- | --- |
> | **subscription**  object | A [Subscription](https://devnet.logianalytics.com/hc/en-us/articles/4415512058519-Subscription) object |  |
> | **commonFilterFields**  array of objects | An array of [CommonFilterField](https://devnet.logianalytics.com/hc/en-us/articles/4415504698647-CommonFilterField) objects |  |

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **success**  boolean | Should be true |  |
> | **subscription**  object | The validated [Subscription](https://devnet.logianalytics.com/hc/en-us/articles/4415512058519-Subscription) object |  |

**Samples**

> ```
> POST/api/dashboard/subscription/validateHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"subscription":{"isDirty":false,"name":"Everyday at 2 PM","type":"Subscription Report","timeZoneName":"(UTC-06:00) Central Time (US & Canada)","timeZoneValue":"Central Standard Time","startDate":"08/11/2016","startTime":"8/11/2016 2:00 PM","recurrenceType":"2","recurrencePattern":1,"recurrencePatternSetting":{"recurrenceWeek":1,"selectedDayValue":"5"},"isEndless":true,"endDate":"11/11/2016","deliveryType":"Email","deliveryMethod":"Link","emailSubject":"{reportName}","subscriptionFilterFields":[],"subscriptionCommonFilterFields":[],"reportId":null,"createdBy":"","id":null,"state":1,"isSubscription":true,"isEndAfter":false,"isEndBy":false,"isEdit":false},"commonFilterFields":[]}
> ```
>
> Sample response:
>
> ```
> {"success":true,"subscription":{"name":"Everyday at 2 PM","schedule":"Occurs every day effective 08/11/2016 at 02:00 PM (UTC-06:00) Central Time (US & Canada)","type":"Subscription Report","timeZoneName":"(UTC-06:00) Central Time (US & Canada)","timeZoneValue":"Central Standard Time","startDate":"2016-08-11T00:00:00","startDateUtc":"2016-08-11T19:00:00","startTime":"2016-08-11T14:00:00","recurrenceType":2,"recurrencePattern":1,"recurrencePatternSetting":{"recurrenceWeek":1,"selectedDayValue":"5"},"isEndless":true,"isScheduled":false,"occurrence":0,"endDate":null,"endDateUtc":null,"deliveryType":"Email","deliveryMethod":"Link","exportFileType":null,"exportAttachmentType":null,"emailSubject":"{reportName}","emailBody":null,"reportId":null,"dashboardId":null,"filterValueSelection":"","recipients":null,"lastSuccessfulRun":"The schedule has not started.","nextScheduledRun":"08/11/2016 02:00 PM (UTC-06:00) Central Time (US & Canada)","isSubscription":true,"subscriptionFilterFields":[],"subscriptionCommonFilterFields":[],"tempId":null,"id":null,"state":1,"inserted":false,"version":null,"created":null,"createdBy":"","modified":null,"modifiedBy":null}}
> ```

## POST dashboard/subscriptions

Saves a list of dashboard subscriptions.

**Request**

> Payload: a [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object, with **id** and **subscriptions** fields populated

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field true if the save is successful

**Samples**

> ```
> POST/api/dashboard/subscriptionsHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"id":"d89d407f-afe7-41f7-a4f3-aa8306af5585","subscriptions":[{"tenantId":null,"isDirty":true,"name":"JDoe Daily","schedule":"Occurs every day effective 01/05/2017 at 12:03 PM (UTC-12:00) International Date Line West","filterValueSelection":"","type":"Subscribed Reporting Item","timeZoneName":"(UTC-12:00) International Date Line West","timeZoneValue":"Dateline Standard Time","startDate":"2017-01-05T00:00:00","startTime":"2017-01-05T12:03:12","recurrenceType":2,"recurrencePattern":1,"recurrencePatternSetting":{"recurrenceWeek":1,"selectedDayValue":"5"},"dailyRecurrencePatternSetting":{"isEveryWeekday":false,"recurrenceDay":1},"weeklyRecurrencePatternSetting":{"recurrenceWeek":1,"selectedDayValue":"5"},"monthlyRecurrencePatternSetting":{"useOrdinalDay":false,"day":5,"recurrenceMonth":1,"ordinalDay":1,"ordinalDayValue":5,"ordinalRecurrenceMonth":0},"yearlyRecurrencePatternSetting":{"recurrenceYear":1,"useOrdinalDay":false,"monthValue":1,"day":5,"ordinalDay":1,"ordinalDayValue":5,"ordinalMonthValue":1},"isEndless":true,"occurrence":0,"endDate":null,"deliveryType":"Email","deliveryMethod":"Link","exportFileType":null,"exportAttachmentType":null,"emailSubject":"{dashboardName}","emailBody":"Dear {currentUserName},\n\nPlease see dashboard in the following link.\n\n{dashboardLink}\n\nRegards,","subscriptionFilterFields":[],"subscriptionCommonFilterFields":[],"reportId":null,"dashboardId":"d89d407f-afe7-41f7-a4f3-aa8306af5585","createdBy":"John Doe","id":null,"state":1,"modified":null,"version":null,"isSubscription":true,"recipients":null,"lastSuccessfulRun":"The schedule has not started.","nextScheduledRun":"01/05/2017 12:03 PM (UTC-12:00) International Date Line West","emailTemplates":[{"key":"Attachment","value":"Dear {currentUserName},\n\nPlease see dashboard in the attachment.\n\nRegards,"},{"key":"Embedded HTML","value":"Dear {currentUserName},\n\nPlease see the following dashboard.\n\n{embedDashboardHTML}\n\nRegards,"},{"key":"Link","value":"Dear {currentUserName},\n\nPlease see dashboard in the following link.\n\n{dashboardLink}\n\nRegards,"}],"isEndAfter":false,"isEndBy":false,"isEdit":false,"selectedValue":false,"currentTab":"schedule"}]}
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null,"data":null}
> ```

## POST dashboard/validateDashboardName

Validates dashboard name.

**Request**

> Payload: a [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field true if the name is valid

**Samples**

> ```
> POST/api/dashboard/validateDashboardNameHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"id":null,"name":"Example Dashboard Name","categoryId":null,"categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":null}
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null,"data":null}
> ```

## POST dashboard/validate

Validates dashboard.

**Request**

> Payload: a [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field true if the dashboard is valid

**Samples**

> ```
> POST/api/dashboard/validateHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"accesses":[],"name":"Example Dashboard Name Test","description":null,"categoryName":null,"subCategoryName":null,"tenantId":null,"backgroundColor":"","imageUrl":null,"stretchImage":false,"id":"d89d407f-afe7-41f7-a4f3-aa8306af5585","state":0,"inserted":true,"version":4,"created":"2016-11-30T08:06:45.113","createdBy":"System Admin","createdById":"9d2f1d51-0e3d-44db-bfc7-da94a7581bfe","modified":"2017-01-05T05:06:22.313","modifiedBy":"John Doe","showFilterDescription":true,"ownerId":"9d2f1d51-0e3d-44db-bfc7-da94a7581bfe","lastViewed":"2017-01-05T05:06:35.2","accessPriority":1,"categoryId":null,"subCategoryId":null,"dashboardParts":[],"commonFilterFields":[],"subscriptions":[]}
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null,"data":null}
> ```

## POST dashboard/validateGlobalDashboard

Validates that dashboard contains only global report parts.

**Request**

> Payload: a [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object with:
>
> 1. **isGlobal**: true
> 2. **dashboardParts**: an array of [DashboardPart](https://devnet.logianalytics.com/hc/en-us/articles/4415504704023-DashboardPart) objects with the **reportId** field populated at minimum.

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field true if the dashboard is global

**Samples**

> ```
> POST/api/dashboard/validateGlobalDashboardHTTP/1.1
> ```
>
> To be updated

## POST dashboard/previewDashboardPartData

Returns data for a dashboard part, given the dashboard part definition.

**Request**

> | Field | Description | Note |
> | --- | --- | --- |
> | **dashboardPart**  object | A [DashboardPart](https://devnet.logianalytics.com/hc/en-us/articles/4415504704023-DashboardPart) object |  |
> | **dataRequest**  object | A [FusionDataRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492814103-FusionDataRequest) object |  |

**Response**

> A [FusionResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492815127-FusionResult) object

**Samples**

> ```
> POST/api/dashboard/previewDashboardPartDataHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"dashboardPart":{"reportId":"babe2f8c-a9b9-4a28-98b9-426b8c15497c","reportPartId":"48c238bb-1296-44bc-bd16-c7e09bdad1ac","filters":[{"filterFieldId":"d192bde7-0e51-4daa-8113-d3d79b539337","value":"USA"}],"numberOfRecord":-1},"dataRequest":{"expandedLevel":-1}}
> ```
>
> Sample response:
>
> ```
> {"grandTotalMapping":[],"subTotalMapping":[],"sideTotalMapping":[],"records":[{"freight_914e4fca_2d9e_":48.2900},{"freight_914e4fca_2d9e_":4.5600},{"freight_914e4fca_2d9e_":4.5400},{"freight_914e4fca_2d9e_":98.0300},{"freight_914e4fca_2d9e_":147.2600},{"freight_914e4fca_2d9e_":257.6200},{"freight_914e4fca_2d9e_":0.5600},{"freight_914e4fca_2d9e_":17.5200},{"freight_914e4fca_2d9e_":74.1600},{"freight_914e4fca_2d9e_":150.1500},{"freight_914e4fca_2d9e_":12.6900},{"freight_914e4fca_2d9e_":214.2700},{"freight_914e4fca_2d9e_":191.6700},{"freight_914e4fca_2d9e_":84.2100},{"freight_914e4fca_2d9e_":23.2900},{"freight_914e4fca_2d9e_":142.0800},{"freight_914e4fca_2d9e_":8.6300},{"freight_914e4fca_2d9e_":195.6800},{"freight_914e4fca_2d9e_":20.1200},{"freight_914e4fca_2d9e_":30.9600},{"freight_914e4fca_2d9e_":126.5600},{"freight_914e4fca_2d9e_":30.3400},{"freight_914e4fca_2d9e_":89.1600},{"freight_914e4fca_2d9e_":12.5100},{"freight_914e4fca_2d9e_":0.2000},{"freight_914e4fca_2d9e_":4.3400},{"freight_914e4fca_2d9e_":86.5300},{"freight_914e4fca_2d9e_":73.0200},{"freight_914e4fca_2d9e_":140.2600},{"freight_914e4fca_2d9e_":60.1800},{"freight_914e4fca_2d9e_":708.9500},{"freight_914e4fca_2d9e_":7.4800},{"freight_914e4fca_2d9e_":15.2800},{"freight_914e4fca_2d9e_":59.1300},{"freight_914e4fca_2d9e_":367.6300},{"freight_914e4fca_2d9e_":3.3500},{"freight_914e4fca_2d9e_":24.9100},{"freight_914e4fca_2d9e_":11.9200},{"freight_914e4fca_2d9e_":252.4900},{"freight_914e4fca_2d9e_":13.7500},{"freight_914e4fca_2d9e_":58.9800},{"freight_914e4fca_2d9e_":37.6000},{"freight_914e4fca_2d9e_":25.4100},{"freight_914e4fca_2d9e_":13.7300},{"freight_914e4fca_2d9e_":4.4200},{"freight_914e4fca_2d9e_":5.2400},{"freight_914e4fca_2d9e_":16.3400},{"freight_914e4fca_2d9e_":44.4200},{"freight_914e4fca_2d9e_":45.1300},{"freight_914e4fca_2d9e_":48.7700},{"freight_914e4fca_2d9e_":200.2400},{"freight_914e4fca_2d9e_":544.0800},{"freight_914e4fca_2d9e_":116.5300},{"freight_914e4fca_2d9e_":18.5300},{"freight_914e4fca_2d9e_":94.8000},{"freight_914e4fca_2d9e_":107.4600},{"freight_914e4fca_2d9e_":57.1500},{"freight_914e4fca_2d9e_":352.6900},{"freight_914e4fca_2d9e_":111.2900},{"freight_914e4fca_2d9e_":1.2800},{"freight_914e4fca_2d9e_":26.3100},{"freight_914e4fca_2d9e_":388.9800},{"freight_914e4fca_2d9e_":26.6100},{"freight_914e4fca_2d9e_":76.1300},{"freight_914e4fca_2d9e_":139.3400},{"freight_914e4fca_2d9e_":102.5500},{"freight_914e4fca_2d9e_":65.1000},{"freight_914e4fca_2d9e_":135.6300},{"freight_914e4fca_2d9e_":2.9600},{"freight_914e4fca_2d9e_":52.4100},{"freight_914e4fca_2d9e_":167.0500},{"freight_914e4fca_2d9e_":24.4900},{"freight_914e4fca_2d9e_":51.4400},{"freight_914e4fca_2d9e_":74.5800},{"freight_914e4fca_2d9e_":21.7200},{"freight_914e4fca_2d9e_":45.9700},{"freight_914e4fca_2d9e_":81.8800},{"freight_914e4fca_2d9e_":232.5500},{"freight_914e4fca_2d9e_":73.2100},{"freight_914e4fca_2d9e_":8.1900},{"freight_914e4fca_2d9e_":18.6600},{"freight_914e4fca_2d9e_":20.2500},{"freight_914e4fca_2d9e_":237.3400},{"freight_914e4fca_2d9e_":45.5300},{"freight_914e4fca_2d9e_":14.6200},{"freight_914e4fca_2d9e_":719.7800},{"freight_914e4fca_2d9e_":37.5200},{"freight_914e4fca_2d9e_":36.6800},{"freight_914e4fca_2d9e_":7.0000},{"freight_914e4fca_2d9e_":487.5700},{"freight_914e4fca_2d9e_":174.0500},{"freight_914e4fca_2d9e_":170.9700},{"freight_914e4fca_2d9e_":14.9300},{"freight_914e4fca_2d9e_":1.9300},{"freight_914e4fca_2d9e_":23.1000},{"freight_914e4fca_2d9e_":0.5300},{"freight_914e4fca_2d9e_":90.9700},{"freight_914e4fca_2d9e_":280.6100},{"freight_914e4fca_2d9e_":116.1300},{"freight_914e4fca_2d9e_":162.9500},{"freight_914e4fca_2d9e_":33.6800},{"freight_914e4fca_2d9e_":400.8100},{"freight_914e4fca_2d9e_":144.3800},{"freight_914e4fca_2d9e_":12.9600},{"freight_914e4fca_2d9e_":657.5400},{"freight_914e4fca_2d9e_":211.2200},{"freight_914e4fca_2d9e_":61.1400},{"freight_914e4fca_2d9e_":4.2700},{"freight_914e4fca_2d9e_":55.1200},{"freight_914e4fca_2d9e_":141.1600},{"freight_914e4fca_2d9e_":14.9100},{"freight_914e4fca_2d9e_":25.1900},{"freight_914e4fca_2d9e_":11.6500},{"freight_914e4fca_2d9e_":830.7500},{"freight_914e4fca_2d9e_":227.2200},{"freight_914e4fca_2d9e_":606.1900},{"freight_914e4fca_2d9e_":40.3200},{"freight_914e4fca_2d9e_":18.8400},{"freight_914e4fca_2d9e_":14.0100},{"freight_914e4fca_2d9e_":30.0900},{"freight_914e4fca_2d9e_":44.7200},{"freight_914e4fca_2d9e_":8.5300}],"fieldsMapping":[{"fieldId":"914e4fca-2d9e-4a9f-a224-8d4cc4133996","fieldNameAlias":"Freight","columnName":"freight_914e4fca_2d9e_"}],"paging":{"pageIndex":0,"pageSize":0,"total":0}}
> ```

## POST dashboard/loadDashboardPartData

Returns data for a dashboard part, given the dashboard part id.

**Request**

> Payload: a [FusionDataRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492814103-FusionDataRequest) object

**Response**

> A [FusionResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492815127-FusionResult) object

**Samples**

> ```
> POST/api/dashboard/loadDashboardPartDataHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"dashboardPartId":"8f64491a-3c07-46c7-a224-f5f6a58a1e29","expandedLevel":-1}
> ```
>
> Response is the same as [POST dashboard/previewDashboardPartData](#post-dashboard-previewdashboardpartdata)

## POST dashboard/loadDashboardPartData2

Returns data for a dashboard part, given the dashboard part id, optionally loads default data.

New in version 2.2.0.

**Request**

> Payload: a [FusionDataRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492814103-FusionDataRequest) object with **loadDefaultData** field populated.

**Response**

> A [FusionResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492815127-FusionResult) object

**Samples**

> ```
> POST/api/dashboard/loadDashboardPartData2HTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"dashboardPartId":"32025f38-549b-4702-a723-3415ba06a541","loadDefaultData":true,"filters":[]}
> ```
>
> Response:
>
> ```
> {"grandTotalMapping":[],"subTotalMapping":[],"sideTotalMapping":[],"executionTrace":[],"records":[{"orderid_40544508_b91a_":10248,"shipcity_3d2b5d33_d539_":"Reims","rowNumber":1},{"orderid_40544508_b91a_":10249,"shipcity_3d2b5d33_d539_":"Münster","rowNumber":2},{"orderid_40544508_b91a_":10251,"shipcity_3d2b5d33_d539_":"Lyon","rowNumber":3},{"orderid_40544508_b91a_":10252,"shipcity_3d2b5d33_d539_":"Charleroi","rowNumber":4},{"orderid_40544508_b91a_":10254,"shipcity_3d2b5d33_d539_":"Bern","rowNumber":5},{"orderid_40544508_b91a_":10255,"shipcity_3d2b5d33_d539_":"Genève","rowNumber":6},{"orderid_40544508_b91a_":10258,"shipcity_3d2b5d33_d539_":"Graz","rowNumber":7},{"orderid_40544508_b91a_":10259,"shipcity_3d2b5d33_d539_":"México D.F.","rowNumber":8},{"orderid_40544508_b91a_":10260,"shipcity_3d2b5d33_d539_":"Köln","rowNumber":9},{"orderid_40544508_b91a_":10263,"shipcity_3d2b5d33_d539_":"Graz","rowNumber":10}],"fieldsMapping":[{"fieldId":"40544508-b91a-4e32-b7ee-0092bc73ba65","fieldNameAlias":"OrderID","columnName":"orderid_40544508_b91a_"},{"fieldId":"3d2b5d33-d539-43bf-ac7d-435139d8b176","fieldNameAlias":"ShipCity","columnName":"shipcity_3d2b5d33_d539_"}],"paging":{"pageIndex":1,"pageSize":10,"total":526,"skipItems":0,"isLastPage":false},"pivotHeaderValues":[],"cities":[],"postalCodes":[]}
> ```

## GET dashboard/dashboardPart/{dashboard\_part\_id}

Returns dashboard part definition.

**Request**

> No payload

**Response**

> A [DashboardPart](https://devnet.logianalytics.com/hc/en-us/articles/4415504704023-DashboardPart) object

**Samples**

> ```
> GET/api/dashboard/dashboardPart/75950fe5-fb5b-4f99-a3a1-0ef0f6a26aedHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"dashboardId":"827f1a53-8afc-4f7c-b384-dd3a7cbe7b45","type":"reportPart","title":"002/002/test/Chart","reportId":"46af03c2-a740-46e0-bb15-49f97e66ff49","reportPartId":"7e76a8cb-d584-4f3e-9494-2c937d49dde6","filterDescription":"","numberOfRecord":-1,"positionX":0,"positionY":0,"width":12,"height":4,"filters":[],"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"textTypeContent":""},"id":"75950fe5-fb5b-4f99-a3a1-0ef0f6a26aed","state":0,"deleted":false,"inserted":true,"version":1,"created":"2016-10-06T09:03:30.313","createdBy":null,"modified":"2016-10-06T09:03:30.313","modifiedBy":null}
> ```

## POST dashboard/accesses/validate

Validates dashboard access, for example:

* owner must have full access
* there is no user or role duplication
* “everyone” is used only once

**Request**

> Payload: a [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object

**Response**

> An object with **success** field
>
> * true if the list of accesses is valid
> * false if not

**Samples**

> ```
> POST/api/dashboard/accesses/validateHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"id":null,"ownerId":"9d2f1d51-0e3d-44db-bfc7-da94a7581bfe","accesses":[{"isDirty":true,"accessors":["9fc0f5c2-decf-4d65-9344-c59a1704ea0c"],"accessRight":null,"assignedType":3,"id":null,"permissionId":null,"reportId":null,"selected":false,"state":1,"accessRightId":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d011","reportAccessRightId":null,"dashboardAccessRightId":null,"tempId":"401","assignedTypeName":null,"accessorNames":[],"reportAccessRights":null,"dashboardAccessRights":null},{"isDirty":true,"accessors":["76956905-b578-474a-b17a-0198d3724039"],"accessRight":null,"assignedType":2,"id":null,"permissionId":null,"reportId":null,"selected":false,"state":1,"accessRightId":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d006","reportAccessRightId":null,"dashboardAccessRightId":null,"tempId":"398","assignedTypeName":null,"accessorNames":[],"reportAccessRights":null,"dashboardAccessRights":null},{"isDirty":true,"accessors":[],"accessRight":null,"assignedType":1,"id":null,"permissionId":null,"reportId":null,"selected":false,"state":1,"accessRightId":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d008","reportAccessRightId":null,"dashboardAccessRightId":null,"tempId":"395","assignedTypeName":null,"accessorNames":[],"reportAccessRights":null,"dashboardAccessRights":null}]}
> ```
>
> Successful response:
>
> ```
> {"success":true}
> ```

## GET dashboard/allowedSavingCategories

Deprecated since version 2.0.0: superseded by [POST dashboard/allowedSavingCategories](#post-dashboard-allowedsavingcategories) and [POST dashboard/allowedSavingSubCategories](#post-dashboard-allowedsavingsubcategories)

Returns an array of allowed saving categories for dashboard.

**Request**

> No payload

**Response**

> An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects

**Samples**

> ```
> GET/api/dashboard/allowedSavingCategoriesHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"name":"Uncategorized","type":2,"parentId":null,"tenantId":null,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":null,"dashboards":null,"id":null,"state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}]
> ```

## POST dashboard/allowedSavingCategories

Returns an array of allowed saving categories for dashboard, with total number of items.

**Request**

> Payload: a [ReportDashboardSearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415492849559-ReportDashboardSearchCriteria) object

**Response**

> The following object:
>
> > | Field | Description | Note |
> > | --- | --- | --- |
> > | **data**  array of objects | An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects |  |
> > | **totalItems**  string | The number of all items |  |
> > | **numOfChilds**  integer | The number of children |  |
> > | **numOfCheckedChilds**  integer | The number of selected children |  |
> > | **indeterminate**  boolean | * true if 0 < numOfCheckedChilds < numOfChilds * false if not |  |
> > | **isLastPage**  boolean | Whether this is the last page |  |

**Samples**

> ```
> POST/api/dashboard/allowedSavingCategoriesHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"pageIndex":1,"pageSize":24,"type":2,"criteria":[{"key":"name","value":null}],"parentIds":["09f8c4ab-0fe8-4e03-82d1-7949e3738f87"],"includeUncategory":false,"tenantId":null}
> ```
>
> Sample response:
>
> ```
> {"data":[{"name":"AAA","type":2,"parentId":null,"tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":null,"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":"3340a862-0eda-4a45-9dc5-794d79b77085","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null},{"name":"BBB","type":2,"parentId":null,"tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":"B","type":2,"parentId":"08af67ff-6597-447e-84b5-9761fcba82f3","tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":null,"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":"ae6cca2b-fd25-4b91-83c2-3418685d7bc6","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"checked":false,"reports":[],"dashboards":[],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":"08af67ff-6597-447e-84b5-9761fcba82f3","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null},{"name":"CCC","type":2,"parentId":null,"tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":"C","type":2,"parentId":"39c3dba7-9484-433c-a3e8-00f2e26a7f73","tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":null,"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":"10ae0b7e-6994-4c23-b80c-ac48a3016d03","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"checked":false,"reports":[],"dashboards":[],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":"39c3dba7-9484-433c-a3e8-00f2e26a7f73","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"totalItems":5,"numOfChilds":3,"numOfCheckedChilds":0,"indeterminate":false,"isLastPage":true}
> ```

## POST dashboard/allowedSavingSubCategories

Returns an array of allowed saving sub-categories for dashboard, with total number of items.

> The following object:
>
> > | Field | Description | Note |
> > | --- | --- | --- |
> > | **data**  array of objects | An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects |  |
> > | **totalItems**  string | The number of all items |  |
> > | **numOfChilds**  integer | The number of children |  |
> > | **numOfCheckedChilds**  integer | The number of selected children |  |
> > | **indeterminate**  boolean | * true if 0 < numOfCheckedChilds < numOfChilds * false if not |  |
> > | **isLastPage**  boolean | Whether this is the last page |  |

**Samples**

> ```
> POST/api/dashboard/allowedSavingSubCategoriesHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"pageIndex":1,"pageSize":24,"type":2,"criteria":[{"key":"name","value":null}],"parentIds":["09f8c4ab-0fe8-4e03-82d1-7949e3738f87","39c3dba7-9484-433c-a3e8-00f2e26a7f73"],"tenantId":null}
> ```
>
> Response:
>
> ```
> {"data":[{"name":"C","type":2,"parentId":"39c3dba7-9484-433c-a3e8-00f2e26a7f73","tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":null,"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":"10ae0b7e-6994-4c23-b80c-ac48a3016d03","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"totalItems":1,"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"isLastPage":true}
> ```

## POST dashboard/loadCommonFilters

Returns a list of report filters that are common among all report parts from a dashboard definition.

**Request**

> Payload: a [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object

**Response**

> An array of [CommonFilterField](https://devnet.logianalytics.com/hc/en-us/articles/4415504698647-CommonFilterField) objects

**Samples**

> ```
> POST/api/dashboard/loadCommonFiltersHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"accesses":[],"name":"Example Dashboard Name 2","description":null,"categoryName":null,"subCategoryName":null,"tenantId":null,"backgroundColor":"","imageUrl":null,"stretchImage":false,"id":"ce822672-feb2-4954-a95b-33bc118dfd8f","state":3,"inserted":false,"version":1,"created":"2016-09-16T04:34:10.7646747","createdBy":null,"modified":"2016-09-16T04:34:10.7646747","modifiedBy":null,"showFilterDescription":true,"categoryId":null,"subCategoryId":null,"dashboardParts":[{"isDirty":true,"dashboardId":"ce822672-feb2-4954-a95b-33bc118dfd8f","positionX":0,"positionY":0,"width":12,"height":4,"title":"Grid/Grid/Chart","isBackSide":false,"filterDescription":"","isFullScreenMode":false,"numberOfRecord":0,"state":1,"type":"reportPart","bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}},"reportId":"b35b9ff8-dc1f-4da3-971a-ab955dbf1940","reportPartId":"64b06c13-5e38-4eb8-9434-f905f8d32faa","id":null,"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"textTypeContent":""},"filters":[]},{"isDirty":true,"dashboardId":"ce822672-feb2-4954-a95b-33bc118dfd8f","positionX":0,"positionY":4,"width":12,"height":4,"title":"Test/Name/Chart","isBackSide":true,"isFullScreenMode":false,"numberOfRecord":0,"state":1,"type":"reportPart","bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}},"reportId":"4a443b06-0c71-400f-bc99-0a15204c0d9b","reportPartId":"45e8e8bd-e4ee-409e-812a-be68337993e9","id":null,"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"textTypeContent":""},"filters":[{"filterFieldId":"0abc3c48-3e9b-4003-949b-a398a389d9bf","value":"[All]","operatorId":"003c0e13-cc3c-412f-8fee-1cf21aa51e31","isCommon":false,"filterField":{"filterList":[],"isDirty":false,"connectionName":"sqlserver","querySourceCategoryName":"dbo","sourceFieldName":"Freight","sourceFieldVisible":true,"sourceFieldFilterable":true,"sourceDataObjectName":"Orders","dataType":"Money","filterId":"a0d603e7-3fa6-479c-90dd-3b08565df79d","querySourceFieldId":"20f25b2e-2d19-473e-bea6-49f3416d9a0e","querySourceType":"Table","querySourceId":"d579abf2-17de-4f5e-8cac-854ef245164d","relationshipId":null,"alias":"Freight","position":1,"visible":false,"required":false,"cascading":true,"operatorId":"003c0e13-cc3c-412f-8fee-1cf21aa51e31","operatorSetting":null,"value":"[All]","sortType":"Unsorted","fontFamily":"Roboto","fontSize":8,"textColor":null,"backgroundColor":null,"fontBold":false,"fontItalic":false,"fontUnderline":false,"id":"0abc3c48-3e9b-4003-949b-a398a389d9bf","state":0,"modified":null,"dateTimeNow":"","selected":false,"isParameter":false,"dataFormatId":null},"operatorSetting":null,"displayName":"Freight"}]}],"commonFilterFields":[],"subscriptions":[]}
> ```
>
> Sample response:
>
> ```
> []
> ```

## GET dashboard/commonFilters/{dashboard\_id}

Returns the saved common filters from a dashboard\_id.

**Request**

> No payload

**Response**

> An array of [CommonFilterField](https://devnet.logianalytics.com/hc/en-us/articles/4415504698647-CommonFilterField) objects

**Samples**

> ```
> GET/api/dashboard/commonFilters/70193a58-5752-48b7-bd0b-018a430087ecHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"name":"042a04a3-dfe1-4ef9-bd27-1b657886f02e-ShipCountry","displayName":"ShipCountry","value":"","operatorId":"042a04a3-dfe1-4ef9-bd27-1b657886f02e","operatorSetting":"","dataType":null,"dashboardId":"70193a58-5752-48b7-bd0b-018a430087ec","position":1,"cascading":false,"sortType":null,"filterFields":[{"filterFieldId":"e5698682-3118-41ba-94e4-985955fc2f2f","dashboardPartId":"00000000-0000-0000-0000-000000000000"},{"filterFieldId":"9baaf9a0-5e65-45c2-b8e5-1cdb8ad5a021","dashboardPartId":"00000000-0000-0000-0000-000000000000"}],"id":"32bf178c-eeac-473a-bc0e-3d4c4096bb13","state":0,"deleted":false,"inserted":true,"version":1,"created":"2017-01-10T03:35:23.803","createdBy":"John Doe","modified":"2017-01-10T03:35:23.803","modifiedBy":"John Doe"}]
> ```

## POST dashboard/updateRenderingTime

Updates the rendering time of a dashboard.

**Request**

> Payload: a [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field true if the update is successful

**Samples**

> ```
> POST/api/dashboard/updateRenderingTimeHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"id":"d89d407f-afe7-41f7-a4f3-aa8306af5585","renderingTime":691}
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null,"data":null}
> ```

## POST dashboard/draft

Saves a dashboard as draft.

**Request**

> Payload: a [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object

**Response**

> The dashboard id in draft

**Samples**

> ```
> POST/api/dashboard/draftHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"accesses":[],"name":"Example Dashboard Name","description":null,"categoryName":null,"subCategoryName":null,"tenantId":null,"backgroundColor":"","imageUrl":null,"stretchImage":false,"id":null,"state":3,"inserted":false,"version":null,"created":null,"createdBy":null,"createdById":null,"modified":null,"modifiedBy":null,"showFilterDescription":true,"ownerId":"9fc0f5c2-decf-4d65-9344-c59a1704ea0c","lastViewed":null,"accessPriority":1,"categoryId":null,"subCategoryId":null,"dashboardParts":[],"commonFilterFields":[],"subscriptions":[]}
> ```
>
> Sample response:
>
> ```
> {"id":"17406c2b-8395-45be-adce-87a33bab6107"}
> ```

## GET dashboard/draft/{dashboard\_id}

Returns a dashboard from draft.

**Request**

> No payload

**Response**

> A [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object

**Samples**

> ```
> GET/api/dashboard/draft/17406c2b-8395-45be-adce-87a33bab6107HTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"commonFilterFields":[],"accesses":[],"subscriptions":[],"inaccessible":false,"name":"Example Dashboard Name","description":null,"categoryId":null,"categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":null,"imageUrl":null,"stretchImage":false,"backgroundColor":"","showFilterDescription":true,"lastViewed":null,"owner":null,"ownerId":"9fc0f5c2-decf-4d65-9344-c59a1704ea0c","createdById":null,"modifiedById":null,"checked":false,"numberOfView":0,"renderingTime":0,"sourceId":null,"deletable":false,"editable":false,"movable":false,"copyable":false,"accessPriority":1,"dashboardParts":[],"id":null,"state":3,"deleted":false,"inserted":false,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}
> ```

## GET dashboard/embeddedReports/{dashboard\_part\_id}

Returns reports and report parts embedded inside the specified dashboard part.

New in version 2.2.0.

**Request**

> No payload

**Response**

> The following object
>
> | Field | Description | Note |
> | --- | --- | --- |
> | **reports**  array of objects | An array of embedded [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492852759-ReportDefinition) objects |  |
> | **reportParts**  array of objects | An array of embedded [ReportPartDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415504773527-ReportPartDefinition) objects |  |

**Samples**

> ```
> GET/api/dashboard/embeddedReports/6b87f048-bffc-4a46-adf4-9a683feb43e2HTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"reports":[],"reportParts":[]}
> ```

## GET dashboard/loadRelatedDashboardParts/{dashboard\_id}

Returns a nested list of dashboard part ids, where each inner list contains dashboard part ids using report parts in a same report.

New in version 2.2.0.

**Request**

> No payload

**Response**

> A list of list of strings (GUIDs)

**Samples**

> ```
> GET/api/dashboard/loadRelatedDashboardParts/aac3c448-99af-4ac3-b8e2-bc27582cee0bHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [["4522d9e6-786a-49aa-8403-aaa8d89c8790","2af78b97-a8f8-4c91-b9d4-cb557939203b"]]
> ```
