---
title: "Dashboard List APIs"
id: 4415511946519
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415511946519-Dashboard-List-APIs
updated_at: 2021-12-10T03:08:08Z
---

# Dashboard List APIs

# Dashboard List APIs

The **Dashboard List and Viewer** page allows users to:

|  |  |
| --- | --- |
| * browse and search for dashboards * copy and move dashboards between categories * switch to presentation mode * configure sharing access * set up subscriptions and scheduled delivery | * rename and delete dashboards and dashboard categories * print dashboard * email dashboard * design dashboard * configure child report parts:   + view, quick edit and design report parts in new window   + print and export report parts   + re-select report parts |

This page documents the APIs related to dashboard list.

## Summary

| API | Purpose | Usage in Izenda Front-end |
| --- | --- | --- |
| [GET dashboard/categories/(tenant\_id)](#get-dashboard-categories-tenant-id) | Returns an array of dashboard categories, filtered by tenant\_id if available. | Not used |
| [POST dashboard/categories](#post-dashboard-categories) | Returns a paged array of dashboard categories. | Dashboard List |
| [POST dashboard/category](#post-dashboard-category) | Renames a dashboard category. | Dashboard List > Rename icon > Update change |
| [DELETE dashboard/category/{dashboard\_category\_id}](#delete-dashboard-category-dashboard-category-id) | Removes a dashboard category. | Not used |
| [POST dashboard/validateCategoryName](#post-dashboard-validatecategoryname) | Validates dashboard category name. | Dashboard List > Rename icon > Update change |
| [GET dashboard/emailTemplates/{isSubscription}](#get-dashboard-emailtemplates-issubscription) | Returns a list of dashboard email templates.  Note  Obsolete, use [GET dashboard/emailTemplates/{templateType}](#get-dashboard-emailtemplates-templatetype) instead | Not use |
| [GET dashboard/emailTemplates/{templateType}](#get-dashboard-emailtemplates-templatetype) | Returns a list of dashboard email templates.  New in version 2.6.14. | Dashboard List > Expand a dashboard > Subscribe |
| [POST dashboard/rename](#post-dashboard-rename) | Renames a dashboard. | Dashboard List > Expand a dashboard > Rename icon > Update change |
| [POST dashboard/move](#post-dashboard-move) | Moves a dashboard to another category / sub-category. | Dashboard List > Expand a dashboard > Move > OK |
| [POST dashboard/copy](#post-dashboard-copy) | Copies a dashboard. | Dashboard List > Expand a dashboard > Copy > OK |
| [DELETE dashboard/{dashboard\_id}](#delete-dashboard-dashboard-id) | Deletes a dashboard. | Dashboard List > Expand a dashboard > Delete > OK |
| [POST dashboard/loadFilterDescription](#post-dashboard-loadfilterdescription) | Returns a list of report filters data including a filter description. | To be updated |
| [POST dashboard/list](#post-dashboard-list) | Deprecated since version 2.0.0: superseded by [POST dashboard/list2(?includeHashCode=true)](#post-dashboard-list2-includehashcode-true)  Returns dashboards for the dashboard list screen. | Not used |
| [POST dashboard/list2(?includeHashCode=true)](#post-dashboard-list2-includehashcode-true) | Returns dashboards for the dashboard list screen, with total number of item. | Dashboard List |
| [POST dashboard/search](#post-dashboard-search) | Deprecated since version 2.0.0: superseded by [POST dashboard/search2](#post-dashboard-search2)  Searches dashboards. | Not used |
| [POST dashboard/search2](#post-dashboard-search2) | Searches dashboards, with total number of item. | Dashboard List > Search |
| [POST dashboard/loadAccesses](#post-dashboard-loadaccesses) | Returns a list of user permissions for dashboard. | Dashboard List > Expand a dashboard > Access |
| [POST dashboard/findByName](#post-dashboard-findbyname) | Returns the first dashboard definition matching specified name and other criteria.   Needs SystemAdmin permission.  New in version 2.0.3. | To be updated |

## GET dashboard/categories/(tenant\_id)

Returns an array of dashboard categories, filtered by tenant\_id if available.

**Request**

> No payload

**Response**

> A [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) object

**Samples**

> ```
> GET/api/dashboard/categoriesHTTP/1.1
> ```
>
> Response:
>
> ```
> [{"name":"CN","type":2,"parentId":null,"tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","isGlobal":false,"createdById":"88ca2835-81e0-443b-b29e-e694a66b8e7a","canDelete":false,"editable":true,"savable":false,"subCategories":[],"checked":false,"reports":[],"dashboards":[],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"status":2,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"930831d2-a4fd-48fc-bd64-9ba244d05ebf","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"acme","modified":null,"modifiedBy":null},{"name":"Uncategorized","type":2,"parentId":null,"tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","isGlobal":false,"createdById":"88ca2835-81e0-443b-b29e-e694a66b8e7a","canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[],"dashboards":[],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"status":1,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"00000000-0000-0000-0000-000000000000","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"acme","modified":null,"modifiedBy":null}]
> ```

## POST dashboard/categories

Returns a paged array of dashboard categories.

**Request**

> Payload: a [ReportDashboardSearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415492849559-ReportDashboardSearchCriteria) object

**Response**

> The following object:
>
> | Field | Description | Note |
> | --- | --- | --- |
> | **data**  array of objects | An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects |  |
> | **totalItems**  string | The number of all items |  |
> | **numOfChilds**  integer | The number of children |  |
> | **numOfCheckedChilds**  integer | The number of selected children |  |
> | **indeterminate**  boolean | * true if 0 < numOfCheckedChilds < numOfChilds * false if not |  |
> | **isLastPage**  boolean | Whether this is the last page |  |

**Samples**

> ```
> POST/api/dashboard/categoriesHTTP/1.1
> ```
>
> Request Payload:
>
> ```
> {"tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","skipItems":0,"pageSize":1,"parentIds":[],"includeGlobalCategory":true}
> ```
>
> Sample Response:
>
> ```
> {"data":[{"name":"Local Categories","type":0,"parentId":null,"tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":"Uncategorized","type":2,"parentId":null,"tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[],"dashboards":[],"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":null,"state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":" acme","modified":null,"modifiedBy":null}],"checked":false,"reports":[],"dashboards":[],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"09f8c4ab-0fe8-4e03-82d1-7949e3738f87","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"acme","modified":null,"modifiedBy":null}],"totalItems":2,"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"isLastPage":true}
> ```

## POST dashboard/category

Renames a dashboard category.

**Request**

> Payload: a [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) object

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object, with **success** field true if the rename is successful

**Samples**

> ```
> POST/api/dashboard/categoryHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"id":"709742d0-2300-4f99-8cdd-1e1675d7c2e7","type":2,"name":"Category02","parentId":null,"tenantId":null,"status":2,"state":0,"modified":null,"canDelete":false,"subCategories":[],"dashboards":[],"reports":[]}
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null,"data":null}
> ```

## DELETE dashboard/category/{dashboard\_category\_id}

Removes a dashboard category.

**Request**

> No payload

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object, with **success** field true if the removal is successful

**Samples**

> ```
> DELETE/api/dashboard/category/709742d0-2300-4f99-8cdd-1e1675d7c2e7HTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null,"data":null}
> ```

## POST dashboard/validateCategoryName

Validates dashboard category name.

**Request**

> Payload: a [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) object

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object, with **success** field true if the category name is valid

**Samples**

> ```
> POST/api/dashboard/validateCategoryNameHTTP/1.1
> ```
>
> Request Payload:
>
> ```
> {"id":"930831d2-a4fd-48fc-bd64-9ba244d05ebf","type":2,"name":"ACME","parentId":null,"state":0,"modified":null,"canDelete":false,"subCategories":[],"dashboards":[],"reports":[],"checked":false,"indeterminate":false,"numOfCheckedChilds":0,"numOfChilds":0,"isGlobal":false,"isEditing":true,"editable":true,"tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e"}
> ```
>
> Sample Response:
>
> ```
> {"success":true,"messages":null,"data":null}
> ```

## GET dashboard/emailTemplates/{isSubscription}

Returns a list of dashboard email templates.

**Request**

> No payload
>
> isSubscription
>
> > * 1 = for Subcriptions
> > * 0 = not

**Response**

> An array of following objects
>
> | Field | Description | Note |
> | --- | --- | --- |
> | **key**  string | The type of the template |  |
> | **value**  string | The content of the template |  |

**Samples**

> ```
> GET/api/dashboard/emailTemplates/0HTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"key":"Attachment","value":"Dear {currentUserName},\n <br/>\n <br/> \n Please see report in the attachment.\n <br/>\n <br/>\n Regards,"},{"key":"Embedded HTML","value":"Dear {currentUserName},\n <br/>\n <br/> \n Please see the following report.\n <br/>\n <br/> \n{embedReportHTML}\n <br/>\n <br/>\n Regards,"},{"key":"Link","value":"Dear {currentUserName},\n <br/>\n <br/> \n Please see report in the following link.\n <br/>\n <br/> \n{reportLink}\n <br/>\n <br/> \n Regards,"}]
> ```

## GET dashboard/emailTemplates/{templateType}

Returns a list of dashboard email templates.

**Request**

> No payload
>
> templateType
>
> > * 0 = Schedule
> > * 1 = Subscription
> > * 2 = Email

**Response**

> An array of following objects
>
> | Field | Description | Note |
> | --- | --- | --- |
> | **key**  string | The type of the template |  |
> | **value**  string | The content of the template |  |

**Samples**

> ```
> GET/api/dashboard/emailTemplates/1HTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"key":"Attachment","value":"Dear {currentUserName},    \u003cbr/\u003e\u003cbr/\u003e        Please see dashboard in the attachment.    \u003cbr/\u003e\u003cbr/\u003e    Regards,"},{"key":"Embedded HTML","value":"Dear {currentUserName},    \u003cbr/\u003e\u003cbr/\u003e        Please see the following dashboard.    \u003cbr/\u003e\u003cbr/\u003e{embedDashboardHTML}\u003cbr/\u003e\u003cbr/\u003e    Regards,"},{"key":"Link","value":"Dear {currentUserName},    \u003cbr/\u003e\u003cbr/\u003e        Please see dashboard in the following link.    \u003cbr/\u003e\u003cbr/\u003e{dashboardLink}\u003cbr/\u003e\u003cbr/\u003e        Regards,"}]
> ```

## POST dashboard/rename

Renames a dashboard.

**Request**

> Payload: a [DashboardRenameParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415492789015-DashboardRenameParameter) object

**Response**

> * true if the rename was successful
> * false if not

**Samples**

> ```
> POST/api/dashboard/renameHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"tenantId":null,"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","name":"TestDashboard02"}
> ```
>
> Response:
>
> ```
> true
> ```

## POST dashboard/move

Moves a dashboard to another category / sub-category.

**Request**

> Payload: a [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object

**Response**

> * true if the move was successful
> * false if not

**Samples**

> ```
> POST/api/dashboard/moveHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"id":"a496ad94-fe92-48d5-a285-e45be738921f","name":"TestDashboard01","categoryId":null,"categoryName":"Category03","subCategoryId":null,"subCategoryName":""}
> ```
>
> Response:
>
> ```
> true
> ```

## POST dashboard/copy

Copies a dashboard.

**Request**

> Payload: a [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object

**Response**

> A [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object

**Samples**

> ```
> POST/api/dashboard/copyHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"id":"57ce3bb7-3d13-415f-88b6-51dc476008ae","name":"TestDashboard02","categoryId":null,"categoryName":"Category02","subCategoryId":null,"subCategoryName":""}
> ```
>
> Sample response:
>
> ```
> {"commonFilterFields":[],"accesses":[],"subscriptions":[],"dashboardParts":[{"dashboardId":"1b4317fd-490a-4c34-bc61-dcbd7a5ff9dc","type":null,"title":null,"reportId":null,"reportPartId":null,"filterDescription":null,"numberOfRecord":-1,"positionX":0,"positionY":4,"width":6,"height":4,"filters":[],"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"id":"fba896ff-14ed-4576-911d-96ba78b2214a","state":0,"inserted":false,"version":1,"created":"2016-08-11T03:20:08.793","createdBy":null,"modified":"2016-08-11T03:20:08.793","modifiedBy":null},{"dashboardId":"1b4317fd-490a-4c34-bc61-dcbd7a5ff9dc","type":null,"title":null,"reportId":null,"reportPartId":null,"filterDescription":null,"numberOfRecord":-1,"positionX":6,"positionY":4,"width":6,"height":4,"filters":[],"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"id":"ca9dec28-3a4a-48f0-bfe3-cb420eeca25f","state":0,"inserted":false,"version":1,"created":"2016-08-11T03:20:08.793","createdBy":null,"modified":"2016-08-11T03:20:08.793","modifiedBy":null},{"dashboardId":"1b4317fd-490a-4c34-bc61-dcbd7a5ff9dc","type":"text","title":"text","reportId":null,"reportPartId":null,"filterDescription":null,"numberOfRecord":-1,"positionX":0,"positionY":0,"width":12,"height":4,"filters":[],"dashboardPartContent":{"contentTitle":{"text":"A Title","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"desc","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"id":"01ff4872-812a-495f-a8ea-52923162b350","state":0,"inserted":false,"version":1,"created":"2016-08-11T03:20:08.777","createdBy":null,"modified":"2016-08-11T03:20:08.777","modifiedBy":null}],"name":"TestDashboard02","description":null,"categoryId":"4c74e214-9891-460a-9571-8f6bd65bc72b","categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":null,"imageUrl":null,"stretchImage":false,"backgroundColor":null,"showFilterDescription":true,"lastViewed":null,"id":"1b4317fd-490a-4c34-bc61-dcbd7a5ff9dc","state":0,"inserted":true,"version":1,"created":"2016-08-11T03:20:08.777","createdBy":null,"modified":"2016-08-11T03:20:08.777","modifiedBy":null}
> ```

## DELETE dashboard/{dashboard\_id}

Deletes a dashboard.

**Request**

> No payload

**Response**

> * true if the deletion was successful
> * false if not

**Samples**

> ```
> DELETE/api/dashboard/1b4317fd-490a-4c34-bc61-dcbd7a5ff9dcHTTP/1.1
> ```
>
> Sample response:
>
> ```
> true
> ```

## POST dashboard/loadFilterDescription

Returns a list of report filters data including a filter description.

**Request**

> The following object
>
> | Field | Description | Note |
> | --- | --- | --- |
> | **reportIds**  array of strings (GUIDs) | An array of ids of reports |  |
> | **dashboardPart**  object | A [DashboardPart](https://devnet.logianalytics.com/hc/en-us/articles/4415504704023-DashboardPart) object |  |

**Response**

> A [DashboardPart](https://devnet.logianalytics.com/hc/en-us/articles/4415504704023-DashboardPart) object, with the **filters** field populated

**Samples**

> ```
> POST/api/dashboard/loadFilterDescriptionHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"reportIds":[],"dashboardPart":{"reportId":"babe2f8c-a9b9-4a28-98b9-426b8c15497c","reportPartId":"48c238bb-1296-44bc-bd16-c7e09bdad1ac","filters":[{"filterFieldId":"d192bde7-0e51-4daa-8113-d3d79b539337","value":"USA","operatorId":"737307d1-1e5f-407f-889f-1b3c9a66dd6f","displayName":"ShipCountry"}]}}
> ```
>
> Sample response:
>
> ```
> {"dashboardId":null,"type":null,"title":null,"reportId":"babe2f8c-a9b9-4a28-98b9-426b8c15497c","reportPartId":"48c238bb-1296-44bc-bd16-c7e09bdad1ac","filterDescription":"ShipCountry = USA","numberOfRecord":0,"positionX":0,"positionY":0,"width":0,"height":0,"filters":[{"filterFieldId":"d192bde7-0e51-4daa-8113-d3d79b539337","value":"USA","operatorId":"737307d1-1e5f-407f-889f-1b3c9a66dd6f","displayName":"ShipCountry","dashboardPartId":"00000000-0000-0000-0000-000000000000","filterField":null,"isCommon":false,"id":null,"state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}],"dashboardPartContent":null,"id":null,"state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}
> ```

## POST dashboard/list

Deprecated since version 2.0.0: superseded by [POST dashboard/list2(?includeHashCode=true)](#post-dashboard-list2-includehashcode-true)

Returns dashboards for the dashboard list screen.

**Request**

> Payload: a [ReportDashboardSearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415492849559-ReportDashboardSearchCriteria) object

**Response**

> An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects

**Samples**

> ```
> POST/api/dashboard/listHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"tenantId":null,"isUncategorized":false,"criterias":[{"key":"CategoryId"}]}
> ```
>
> Sample response:
>
> ```
> [{"dashboards":[],"subCategories":[{"dashboards":[{"name":"Sample Dashboard","description":null,"categoryId":"aba44e94-ffbb-4435-83fa-5ca659589fc7","categoryName":"Category01","subCategoryId":null,"subCategoryName":null,"tenantId":"00000000-0000-0000-0000-000000000000","imageUrl":null,"stretchImage":false,"backgroundColor":null,"showFilterDescription":false,"lastViewed":null,"id":"f464b993-f632-4e4b-9462-1e2bfc1cace1","state":0,"inserted":true,"version":2,"created":null,"createdBy":null,"modified":"2016-08-23T03:21:22.9100000-07:00","modifiedBy":null}],"subCategories":null,"name":null,"type":0,"parentId":null,"tenantId":null,"canDelete":false,"status":0,"id":"00000000-0000-0000-0000-000000000000","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}],"name":"Category01","type":0,"parentId":null,"tenantId":null,"canDelete":false,"status":2,"id":"aba44e94-ffbb-4435-83fa-5ca659589fc7","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"dashboards":[],"subCategories":[{"dashboards":[{"name":"Dashboard123","description":null,"categoryId":null,"categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":"00000000-0000-0000-0000-000000000000","imageUrl":null,"stretchImage":false,"backgroundColor":null,"showFilterDescription":false,"lastViewed":null,"id":"70e9555c-34c4-44e4-b4d0-8a60f0e73a6c","state":0,"inserted":true,"version":4,"created":null,"createdBy":null,"modified":"2016-08-23T03:19:59.8930000-07:00","modifiedBy":null},{"name":"Dashboard4","description":null,"categoryId":null,"categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":"00000000-0000-0000-0000-000000000000","imageUrl":null,"stretchImage":false,"backgroundColor":null,"showFilterDescription":false,"lastViewed":null,"id":"79b09ae9-de5d-4e52-b441-66f494511de1","state":0,"inserted":true,"version":2,"created":null,"createdBy":null,"modified":"2016-08-23T03:20:10.5630000-07:00","modifiedBy":null}],"subCategories":null,"name":null,"type":0,"parentId":null,"tenantId":null,"canDelete":false,"status":0,"id":"00000000-0000-0000-0000-000000000000","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}],"name":null,"type":0,"parentId":null,"tenantId":null,"canDelete":false,"status":0,"id":"00000000-0000-0000-0000-000000000000","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}]
> ```

## POST dashboard/list2(?includeHashCode=true)

Returns dashboards for the dashboard list screen, with total number of items.

**Request**

> Payload: a [ReportDashboardSearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415492849559-ReportDashboardSearchCriteria) object
>
> Optional query string: includeHashCode=true

**Response**

> * Without includeHashCode: an array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects
> * With includeHashCode=true: the following object:
>
>   | Field | Description | Note |
>   | --- | --- | --- |
>   | **data**  array of objects | An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects |  |
>   | **hashcode**  string | The hashcode |  |
>   | **totalItems**  string | The number of all reports |  |
>   | **numOfChilds**  integer | The number of children |  |
>   | **numOfCheckedChilds**  integer | The number of selected children |  |
>   | **indeterminate**  boolean | + true if 0 < numOfCheckedChilds < numOfChilds + false if not |  |
>   | **isLastPage**  boolean | Whether this is the last page |  |

**Samples**

> ```
> POST/api/dashboard/list2?includeHashCode=trueHTTP/1.1
> ```
>
> Sample payload:
>
> ```
> {"tenantId":"b930adf8-5bfd-4214-97e3-f709f10721fb","isUncategorized":false,"skipItems":0,"pageSize":100,"parentIds":[],"includeGlobalCategory":true,"criterias":[{"key":"CategoryId"}]}
> ```
>
> Sample response:
>
> ```
> {"data":[{"name":"Global Categories","type":0,"parentId":null,"tenantId":null,"isGlobal":true,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":null,"type":0,"parentId":null,"tenantId":null,"isGlobal":true,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":null,"type":0,"parentId":"00000000-0000-0000-0000-000000000000","tenantId":null,"isGlobal":true,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[],"dashboards":[{"commonFilterFields":[],"accesses":[],"subscriptions":[],"inaccessible":false,"name":"Example Dashboard Name","description":null,"categoryId":null,"categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":null,"imageUrl":null,"stretchImage":false,"backgroundColor":null,"showFilterDescription":false,"lastViewed":null,"owner":"John Doe","ownerId":"d928e941-19ef-4382-ba60-7238cb555631","createdById":"d928e941-19ef-4382-ba60-7238cb555631","modifiedById":null,"checked":false,"numberOfView":0,"renderingTime":0,"sourceId":"00000000-0000-0000-0000-000000000000","isGlobal":true,"deletable":false,"editable":false,"movable":false,"copyable":false,"accessPriority":1,"dashboardParts":[{"dashboardId":"abe7a54a-e3cc-4f66-8032-0f341319bf20","positionX":0,"positionY":0,"width":0,"height":0,"title":null,"numberOfRecord":null,"state":0,"type":null,"reportId":"f9348e0e-7572-426d-bf83-0d6a043aaeb8","reportPartId":"5080ff07-ae7c-4bdd-9742-2e56896b6dd3","id":"a8ccf78f-10ab-4244-87d7-0032a501dda7","dashboardPartContent":null,"reportName":"Sample Orders Report","filterDescription":null,"filters":[],"reportDataSource":[{"reportId":null,"querySourceId":"f4ae63fc-4c10-4672-9cd2-4a9d40434a4c","querySourceUniqueName":"[con;#0].[cat;#0].[Orders]","querySourceCategoryId":"0e8d2b0b-010d-46e5-8dc4-ff048d6f5e07","connectionId":"ca12331b-f917-47ae-8397-3758bc393bdb","selected":false,"id":null,"state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"User1 ACME","modified":null,"modifiedBy":null}],"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"User1 ACME","modified":null,"modifiedBy":null},{"dashboardId":"abe7a54a-e3cc-4f66-8032-0f341319bf20","positionX":0,"positionY":0,"width":0,"height":0,"title":null,"numberOfRecord":null,"state":0,"type":null,"reportId":"daefaa42-75b2-4b07-8ef8-019134109054","reportPartId":"1760e4c9-b7b6-467f-b820-6b3b8585079c","id":"08561802-97bf-4a4f-a8b1-2c2e7e920a7e","dashboardPartContent":null,"reportName":"Example Report Name","filterDescription":null,"filters":[],"reportDataSource":[{"reportId":null,"querySourceId":"f4ae63fc-4c10-4672-9cd2-4a9d40434a4c","querySourceUniqueName":"[con;#0].[cat;#0].[Orders]","querySourceCategoryId":"0e8d2b0b-010d-46e5-8dc4-ff048d6f5e07","connectionId":"ca12331b-f917-47ae-8397-3758bc393bdb","selected":false,"id":null,"state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"User1 ACME","modified":null,"modifiedBy":null}],"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"User1 ACME","modified":null,"modifiedBy":null}],"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":"abe7a54a-e3cc-4f66-8032-0f341319bf20","state":0,"deleted":false,"inserted":true,"version":1,"created":"2017-04-27T07:21:54.97","createdBy":"John Doe","modified":"2017-04-27T07:21:54.97","modifiedBy":"John Doe"}],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":null,"state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"User1 ACME","modified":null,"modifiedBy":null}],"checked":false,"reports":[],"dashboards":[],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":null,"state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"User1 ACME","modified":null,"modifiedBy":null}],"checked":false,"reports":[],"dashboards":[],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":"2a83e3ce-f91b-4f14-910d-76cadf42d0fe","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"User1 ACME","modified":null,"modifiedBy":null}],"hashcode":"c7a675c7041bf74773d55ba8840","totalItems":3,"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"isLastPage":true}
> ```

## POST dashboard/search

Deprecated since version 2.0.0: superseded by [POST dashboard/search2](#post-dashboard-search2)

Searches dashboards.

**Request**

> Payload: a [ReportDashboardSearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415492849559-ReportDashboardSearchCriteria) object

**Response**

> An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects

**Samples**

> ```
> POST/api/dashboard/searchHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"criterias":[{"key":"All","value":"1"}],"isUncategorized":false,"sortCriteria":{"key":"DashboardName","descending":false},"tenantId":null}
> ```
>
> Sample response:
>
> ```
> [{"dashboards":[],"name":"ABC","type":0,"parentId":null,"tenantId":null,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"dashboards":[{"name":"Dashboard 1","description":null,"categoryId":"f0fd52d8-eef9-4ba7-b89d-6267be5e6b66","categoryName":"ABC","subCategoryId":"309dbfab-193d-48b7-9a76-c209c507d9d5","subCategoryName":"abc","tenantId":null,"imageUrl":null,"stretchImage":false,"backgroundColor":null,"showFilterDescription":false,"lastViewed":"2016-11-17T04:08:56.9000000+14:00","owner":"Pa system admin","ownerId":"0fa44ace-abd7-4a8d-928e-c84ec2999dfe","createdById":"0fa44ace-abd7-4a8d-928e-c84ec2999dfe","modifiedById":null,"numberOfView":1,"renderingTime":13010,"deletable":true,"editable":true,"movable":true,"copyable":true,"accessPriority":1,"id":"a087f614-d55e-4c53-89f5-04e4fddd173a","state":0,"deleted":false,"inserted":true,"version":1,"created":"2016-11-12T10:35:32.3500000+14:00","createdBy":"Pa system admin","modified":"2016-11-12T10:35:32.3500000+14:00","modifiedBy":"Pa system admin"}],"name":"abc","type":0,"parentId":null,"tenantId":null,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"status":2,"id":"309dbfab-193d-48b7-9a76-c209c507d9d5","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}],"status":2,"id":"f0fd52d8-eef9-4ba7-b89d-6267be5e6b66","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}]
> ```

## POST dashboard/search2

Searches dashboards, with total number of items.

**Request**

> Payload: a [ReportDashboardSearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415492849559-ReportDashboardSearchCriteria) object

**Response**

> The following object:
>
> > | Field | Description | Note |
> > | --- | --- | --- |
> > | **data**  array of objects | An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects |  |
> > | **totalItems**  string | The number of all reports |  |
> > | **numOfChilds**  integer | The number of children |  |
> > | **numOfCheckedChilds**  integer | The number of selected children |  |
> > | **indeterminate**  boolean | * true if 0 < numOfCheckedChilds < numOfChilds * false if not |  |
> > | **isLastPage**  boolean | Whether this is the last page |  |

**Samples**

> ```
> POST/api/dashboard/search2HTTP/1.1
> ```
>
> Sample payload:
>
> ```
> {"criterias":[{"key":"All","value":"ex"}],"isUncategorized":false,"sortCriteria":{"key":"DashboardName","descending":false},"tenantId":"b930adf8-5bfd-4214-97e3-f709f10721fb","skipItems":0,"pageSize":66,"parentIds":[],"includeGlobalCategory":true}
> ```
>
> Sample response:
>
> ```
> {"data":[{"name":"Global Categories","type":0,"parentId":null,"tenantId":null,"isGlobal":true,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":null,"type":0,"parentId":null,"tenantId":null,"isGlobal":true,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":null,"type":0,"parentId":"00000000-0000-0000-0000-000000000000","tenantId":null,"isGlobal":true,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[],"dashboards":[{"name":"Example Dashboard Name","description":null,"categoryId":null,"categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":null,"imageUrl":null,"stretchImage":false,"backgroundColor":null,"showFilterDescription":false,"lastViewed":"2017-04-27T07:23:08.033","owner":"John Doe","ownerId":"d928e941-19ef-4382-ba60-7238cb555631","createdById":"d928e941-19ef-4382-ba60-7238cb555631","modifiedById":null,"checked":false,"numberOfView":1,"renderingTime":2319,"sourceId":"00000000-0000-0000-0000-000000000000","isGlobal":true,"deletable":false,"editable":false,"movable":false,"copyable":false,"accessPriority":1,"dashboardParts":[],"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":"abe7a54a-e3cc-4f66-8032-0f341319bf20","state":0,"deleted":false,"inserted":true,"version":1,"created":"2017-04-27T07:21:54.97","createdBy":"John Doe","modified":"2017-04-27T07:21:54.97","modifiedBy":"John Doe"}],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":null,"state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"User1 ACME","modified":null,"modifiedBy":null}],"checked":false,"reports":[],"dashboards":[],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":null,"state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"User1 ACME","modified":null,"modifiedBy":null}],"checked":false,"reports":[],"dashboards":[],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":"2a83e3ce-f91b-4f14-910d-76cadf42d0fe","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"User1 ACME","modified":null,"modifiedBy":null}],"totalItems":3,"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"isLastPage":true}
> ```

## POST dashboard/loadAccesses

Returns a list of user permissions for dashboard.

**Request**

> Payload: an [AccessPagedRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415504690199-AccessPagedRequest) object

**Response**

> A [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) object, with **result** field containing an array of [UserPermission](https://devnet.logianalytics.com/hc/en-us/articles/4415492896023-UserPermission) objects

**Samples**

> ```
> POST/api/dashboard/loadAccessesHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"dashboardId":"a3243533-166d-4377-90eb-add25edf6563","criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"shareWith","descending":true}]}
> ```
>
> Sample response:
>
> ```
> {"result":[],"pageIndex":1,"pageSize":10,"total":0}
> ```

## POST dashboard/findByName

Returns the first dashboard definition matching specified name and other criteria.   
Needs SystemAdmin permission.

New in version 2.0.3.

**Request**

> Payload: a [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object with **name**, **tenantId** and **isGlobal** fields populated, and optional **categoryName** and **subCategoryName** values.

**Response**

> * A full [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object if found
> * null if not found

**Samples**

> ```
> POST/api/dashboard/findByNameHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"name":"Empty Dashboard","tenantId":null,"isGlobal":false,"categoryName":"Dashboard Category 1"}
> ```
>
> Sample response:
>
> ```
> {"commonFilterFields":[],"accesses":[],"subscriptions":[],"inaccessible":false,"name":"Empty Dashboard","description":null,"categoryId":"1b066da5-7afe-4110-ac69-be9a2a61b6a1","categoryName":"Dashboard Category 1","subCategoryId":null,"subCategoryName":null,"tenantId":null,"imageUrl":null,"stretchImage":false,"backgroundColor":"","showFilterDescription":false,"lastViewed":null,"owner":"john doe","ownerId":"dc18316c-bd87-4af2-9d98-e196a5c1fa6c","createdById":"dc18316c-bd87-4af2-9d98-e196a5c1fa6c","modifiedById":"dc18316c-bd87-4af2-9d98-e196a5c1fa6c","checked":false,"numberOfView":0,"renderingTime":0,"sourceId":null,"isGlobal":false,"deletable":false,"editable":false,"movable":false,"copyable":false,"accessPriority":0,"dashboardParts":[],"indeterminate":false,"fullPath":null,"computeNameSettings":null,"id":"baa03250-9a06-46e1-8cce-bfae8c12c4fe","state":0,"deleted":false,"inserted":true,"version":1,"created":"2017-06-09T04:38:33.233","createdBy":"john doe","modified":"2017-06-09T04:38:33.233","modifiedBy":"john doe"}
> ```
