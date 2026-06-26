---
title: "Report Designer Details APIs"
id: 4415492732439
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492732439-Report-Designer-Details-APIs
updated_at: 2021-12-10T03:08:11Z
---

# Report Designer Details APIs

# Report Designer Details APIs

The **Report Designer** page allows users to:

* create a report
* select report data sources
* create report filters
* design report layout
* set up report schedule

This topic documents the APIs related to report details.

## Summary

| API | Purpose | Usage in Izenda Front-end |
| --- | --- | --- |
| [GET report/category/{type}/(tenant\_id)](#get-report-category-type-tenant-id) | Returns an array of allowed saving categories for Report (type=0), Template (type=1) or Dashboard (type=2). | - Report Designer > Save (As) > Category   - Report List > Expand a report > Copy/Move > Category |
| [POST report/allowedSavingCategories](#post-report-allowedsavingcategories) | Returns an array of allowed saving categories for Report, with total number of items. | Not used |
| [POST report/allowedSavingSubCategories](#post-report-allowedsavingsubcategories) | Returns an array of allowed saving sub-categories for Report, with total number of items. | Not used |
| [GET report/subcategory/{parent\_category\_id}](#get-report-subcategory-parent-category-id) | Returns an array of allowed saving sub-categories under the Report category specified by parent\_category\_id. | - Report Designer > Save (As) > Category > Sub-category   - Report List > Expand a report > Copy/Move > Category > Sub-category |
| [GET report/allCategories/{type}/(tenant\_id)](#id1) | Returns the list of categories by type (Reports/Templates/Dashboards) in parent-child hierarchy. | Not used |
| [POST report/allCategories](#post-report-allcategories) | Returns the list of categories in parent-child hierarchy, with total number of items. | Report List |
| [POST report/category](#post-report-category) | Renames a report category. | Report List > Rename icon > Update change |
| [DELETE report/category/{report\_category\_id}](#delete-report-category-report-category-id) | Removes the report category specified by report\_category\_id. | Not used |
| [POST report/validateCategoryName](#post-report-validatecategoryname) | Validates a report category name. | To be updated |
| [GET report/reportByProperty/{report\_id}/{property}](#get-report-reportbyproperty-report-id-property) | Returns a report section. | Dashboard Designer |
| [POST report](#id2) | Saves a report. | Report Designer > Save (As) |
| [POST report/draft](#id3) | Saves a report as draft. | - Report Designer, when switching between Data Source, Fields, Format.. sections - to store unsaved changes   - Update Result   - Save |
| [POST report/cancel](#post-report-cancel) | Deletes temporary data of a report. | Report Designer > Cancel |
| [POST report/loadForEdit](#post-report-loadforedit) | Returns an object with report key and report’s data. | - Report List > Expand a report > Edit > Design   - Report Viewer > Edit > Design |
| [GET report/(tenant\_id)](#get-report-tenant-id) | Returns all report categories together with the reports inside. | Not used |
| [POST report/validateReportName](#post-report-validatereportname) | Validates that a report name is unique and not empty. | - Report Designer > Save (As) > OK   - Report Designer > Rename icon > Update change   - Report List > Expand a report > Rename icon > Update change   - Report Viewer > Rename icon > Update change |
| [POST report/validate](#post-report-validate) | Validates that a report name is unique and its filter and relationships are valid. | Report Designer > Update Result |
| [POST report/search](#post-report-search) | Deprecated since version 2.0.0: superseded by [POST report/search2](#post-report-search2)  Searches for reports. | Not used |
| [POST report/search2](#post-report-search2) | Searches for reports, with total number of items. | Not used, replaced by [POST report/list2(?includeHashCode=true)](https://devnet.logianalytics.com/hc/en-us/articles/4415492756887-Report-List-APIs#post-report-list2) |
| [POST report/advancedSearch](#post-report-advancedsearch) | Searches for reports with advanced options. | Not used, replaced by [POST report/list2(?includeHashCode=true)](https://devnet.logianalytics.com/hc/en-us/articles/4415492756887-Report-List-APIs#post-report-list2) |
| [GET report/reportMode](#id4) | Returns the report mode. | Report Designer |
| [POST report/reportMode/{value}](#id5) | Sets the report mode to Simple or Advanced.  Deleted in version 2.6.0 | Not used |
| [POST report/detectReportChange](#post-report-detectreportchange) | Verifies that all report details are up to date, without physical changes, and valid. | Report Designer, when switching between Data Source, Fields, Format.. sections |
| [POST report/function/{function\_mode}/{data\_type}/(tenant\_id)](#id6) | Returns a list of report functions filtered by mode (field, sub-total, grand-total), data type, tenant\_id, and optionally filtered by connections of the selected query source ids in payload.  Changed in version 1.25: Changed from GET to POST | Report Designer, when adding a data source field to a report part |
| [GET report/allReports/(tenant\_id)](#get-report-allreports-tenant-id) | Returns a list of all reports filtered by tenant\_id if provided. | To be updated |
| [POST report/detectSchemaChange](#post-report-detectschemachange) | Verifies that all report filter fields are without changes. | - Report Designer, when switching between Data Source, Fields, Format.. sections   - Report Designer > Update Result |
| [POST report/updateResults](#post-report-updateresults) | Updates the report data model. | - Create a report, in Data Source tab, choose a dynamic Store Procedure   - Input parameter values   - Click **Update Result** button |
| [POST report/loadAccesses](#post-report-loadaccesses) | Returns a list of all accesses. | Report Designer > Access |
| [POST report/loadSchedules](#post-report-loadschedules) | Returns a list of all scheduled deliveries. | Report Designer > Schedules |
| [`GET report/reportPart/{report\\_part\\_id}/(report\\_id)`\_](#id10) | Returns the report part definition specified by report\_part\_id from draft (using report\_id) or from database (without report\_id). | Dashboard Designer |
| [POST report/validateExistingField](#id7) | Validates that some fields exist in a report. | - In Report Designer page > Field properties > Custom URL   - Leave a custome URL to another report > click OK button   - Click on any hyperlink |
| [GET report/reportId/(tenant\_id)?reportName=value&categoryName=value](#get-report-reportid-tenant-id-reportname-value-categoryname-value) | Returns report id from report name and category name. | To be updated |
| [POST report/validateExistingReport](#id8) | Validates that a report exists in a category. | - In Report Designer page > Field properties > Custom URL   - Leave a custome URL to another report > click OK button   - Click on any hyperlink |
| [GET report/reportsByTenant/(tenant\_id)](#get-report-reportsbytenant-tenant-id) | Returns list of reports by tenant, with each report containing a list of report parts. | To be updated |
| [POST report/updateRenderingTime](#post-report-updaterenderingtime) | Updates the rendering time of a report. | - Report Viewer   - Report List > Expand a report > Edit > Quick Edit |
| [GET report/isReportValid/(report\_id)](#get-report-isreportvalid-report-id) | Returns true if there is a report definition for the specified report\_id. | - Report Designer for an existing report   - Report Viewer   - Report List > Expand a report > Edit > Quick Edit   - Dashboard Viewer |
| [POST report/areReportsValid](#post-report-arereportsvalid) | Validates if reports are valid. | Not used |
| [POST report/printDraft](#post-report-printdraft) | Saves report as draft and print. | Report Designer > Export - to allow printing unsaved changes |
| [GET report/printDraft/{report\_id}](#get-report-printdraft-report-id) | Gets report as draft for printing. | To be updated |
| [GET report/accessPriority/(report\_dashboard\_id)](#get-report-accesspriority-report-dashboard-id) | Returns access priority for report/dashboard. | Open a report in Design mode OR open a dashboard |
| [GET report/reportPart/crossfiltering/{report\_part\_id}](#get-report-reportpart-crossfiltering-report-part-id) | Returns a list of ids of cross-filtering report parts in the same report as the specified report part, including itself.  New in version 2.0.6. | Not used |
| [GET report/validateEmbeddedReport/(tenant\_id)?reportId=value&reportName=value&reportPartName=value](#get-report-validateembeddedreport-tenant-id-reportid-value-reportname-value-reportpartname-value) | Validates that logged in user can access one and only one report part from the specified reportName and reportPartName.  New in version 2.2.2. | - Create a Form report part   - Drag and drop a field to the container   - In Report Part Properties tab, choose Embedded Report Settings, choose a report and report part |
| [POST report/findBySourceIds](#post-report-findbysourceids) | Returns a list of report definitions based on the provided report source Ids  New in version 2.4.4. | To be updated |
| [POST report/findReportPartsBySourceIds](#post-report-findreportpartsbysourceids) | Returns a list of report parts based on the provided report part source Ids  New in version 2.4.4. | To be updated |

## GET report/category/{type}/(tenant\_id)

Returns an array of allowed saving categories by type (Reports/Templates/Dashboards), filtered by tenant\_id if given.

> type
> :   * 0 = Reports
>     * 1 = Templates
>     * 2 = Dashboards

**Request**

> No payload

**Response**

> An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects

**Samples**

> ```
> GET/api/report/category/1HTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"name":"Category 1","type":"Templates","parentId":null,"tenantId":null,"status":2,"id":"17c176e1-500b-4378-8c59-1f69e84e425b","state":0,"modified":null"},{"name":"Sub Category 1","type":"Templates","parentId":"17c176e1-500b-4378-8c59-1f69e84e425b","tenantId":null,"status":2,"id":"14b3f8c7-c4e8-4730-a57e-3b28ad75b097","state":0,"modified":null"},{"name":"Sub Category 2","type":"Templates","parentId":"17c176e1-500b-4378-8c59-1f69e84e425b","tenantId":null,"status":2,"id":"72d44e10-a707-455e-99dc-054088b6b2f3","state":0,"modified":null"}]
> ```

## POST report/allowedSavingCategories

Returns an array of allowed saving categories for report, with total number of items.

**Request**

> Payload: a [ReportDashboardSearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415492849559-ReportDashboardSearchCriteria) object

**Response**

> The following object:
>
> > | Field | Description | Note |
> > | --- | --- | --- |
> > | **data**  array of objects | An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects |  |
> > | **isLastPage**  boolean | Whether this is the last page |  |

**Samples**

> ```
> POST/api/report/allowedSavingCategoriesHTTP/1.1
> ```
>
> Sample Request Payload:
>
> ```
> {"tenantId":null,"isUncategorized":false,"criterias":[],"ParentIds":["5ca51cd0-1f63-44ca-9711-ba6c988a520a"]}
> ```
>
> Sample Response:
>
> ```
> {"data":[{"name":"Category01","type":0,"parentId":null,"tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[],"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"f93c0770-9629-41ee-9ac2-48e4c89fc2d0","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"System5 Admin5","modified":null,"modifiedBy":null},{"name":"Category02","type":0,"parentId":null,"tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[],"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"5ca51cd0-1f63-44ca-9711-ba6c988a520a","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"System5 Admin5","modified":null,"modifiedBy":null}],"isLastPage":true}
> ```

## POST report/allowedSavingSubCategories

Returns an array of allowed saving sub-categories for report, with total number of items.

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
> POST/api/report/allowedSavingSubCategoriesHTTP/1.1
> ```
>
> Sample Request Payload:
>
> ```
> {"tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","isUncategorized":false,"criterias":[],"ParentIds":["5ca51cd0-1f63-44ca-9711-ba6c988a520a"]}
> ```
>
> Sample Response:
>
> ```
> {"data":[{"name":"SubCategory02","type":0,"parentId":"5ca51cd0-1f63-44ca-9711-ba6c988a520a","tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[],"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"0e771076-c385-4c1f-a10d-a89c2b473405","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"System5 Admin5","modified":null,"modifiedBy":null},{"name":"SubCategory02","type":0,"parentId":"5ca51cd0-1f63-44ca-9711-ba6c988a520a","tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[],"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"f432f63a-92f4-4b9d-8d1f-1433c5f323f8","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"System5 Admin5","modified":null,"modifiedBy":null}],"isLastPage":true}
> ```

## GET report/subcategory/{parent\_category\_id}

Returns an array of allowed saving sub-categories under the Report category specified by parent\_category\_id.

**Request**

> No payload

**Response**

> An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects

**Samples**

> ```
> GET/api/report/subcategory/17c176e1-500b-4378-8c59-1f69e84e425bHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"name":"Sub Category 1","type":null,"parentId":"17c176e1-500b-4378-8c59-1f69e84e425b","tenantId":null,"status":2,"id":"72d44e10-a707-455e-99dc-054088b6b2f3","state":0,"modified":null},{"name":"Sub Category 2","type":null,"parentId":"17c176e1-500b-4378-8c59-1f69e84e425b","tenantId":null,"status":2,"id":"14b3f8c7-c4e8-4730-a57e-3b28ad75b097","state":0,"modified":null}]
> ```

## GET report/allCategories/{type}/(tenant\_id)

Returns the list of categories by type (Reports/Templates/Dashboards) in parent-child hierarchy.

> type
> :   * 0 = Reports
>     * 1 = Templates
>     * 2 = Dashboards

**Request**

> No payload

**Response**

> An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects

**Samples**

> ```
> GET/api/report/allCategories/0HTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"name":"Category 1","type":0,"parentId":null,"tenantId":null,"subReportCategories":null,"canDelete":false,"status":2,"id":"f2d79ff5-3aa8-4ae6-b0d0-e47687a77380","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"name":"Category 2","type":0,"parentId":null,"tenantId":null,"subReportCategories":[{"name":"Sub-category 1","type":0,"parentId":"f514e26f-501c-4369-8ea9-de4eba208bdf","tenantId":null,"subReportCategories":null,"canDelete":false,"status":2,"id":"81517214-273b-42e9-91b5-8ef766cc5761","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}],"canDelete":false,"status":2,"id":"f514e26f-501c-4369-8ea9-de4eba208bdf","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}]
> ```

## POST report/allCategories

Returns the list of categories in parent-child hierarchy, with total number of items.

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
> POST/api/report/allCategoriesHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"data":[{"name":"Local Categories","type":0,"parentId":null,"tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":"CN","type":0,"parentId":null,"tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[],"dashboards":[],"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"dc04087a-a761-43fb-b82d-13d2ffe8d9e3","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"checked":false,"reports":[],"dashboards":[],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"09f8c4ab-0fe8-4e03-82d1-7949e3738f87","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"totalItems":2,"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"isLastPage":true}
> ```

## POST report/category

Renames a report category.

**Request**

> A [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) object

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **success**  boolean | Is the rename successful |  |
> | **messages**  array of strings | The error messages |  |

**Samples**

> ```
> POST/api/report/categoryHTTP/1.1
> ```
>
> Request Payload:
>
> ```
> {"id":"f2d79ff5-3aa8-4ae6-b0d0-e47687a77380","type":1,"name":"Category 1 renamed","parentId":null,"tenantId":null,"status":2,"state":0,"modified":null,"canDelete":false,"subCategories":[],"subReportCategories":null,"reports":[]}
> ```
>
> Successful response:
>
> ```
> {"success":true,"messages":null}
> ```

## DELETE report/category/{report\_category\_id}

Removes the report category specified by report\_category\_id.

**Request**

> No payload

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with the **success** field populated:
>
> | Field | Description | Note |
> | --- | --- | --- |
> | **success**  boolean | Is the rename successful |  |

**Samples**

> ```
> DELETE/api/report/category/f285a869-25fb-428e-8cef-856241ba4249HTTP/1.1
> ```
>
> Sample response in case of error:
>
> ```
> {"success":false,"messages":[{"key":"","messages":["This category (or its sub-category) containing report(s)."]}]"data":null}
> ```

## POST report/validateCategoryName

Validates a report category name.

**Request**

> Payload: a [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) object

**Response**

> * true if the category name is valid and not duplicated
> * false if not

**Samples**

> ```
> POST/api/report/validateCategoryNameHTTP/1.1
> ```
>
> With payload:
>
> ```
> {"name":"InternetSales","type":0,"parentId":"5d034fc7-0cc8-46b7-beb3-35b22c57827c","id":"45f17b8a-3708-4f36-80ef-9178b7124841"}
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null,"data":null}
> ```

## GET report/reportByProperty/{report\_id}/{property}

Returns a report section.

**Request**

> property
> :   * 0 = All
>     * 1 = DataSource
>     * 2 = Relationship
>     * 3 = Filter
>     * 4 = ReportPart
>     * 5 = CalculatedField
>     * 6 = DynamicQuerySourceField
>     * 7 = Scheduling
>     * 8 = Access
>     * 9 = Report

**Response**

> A [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492852759-ReportDefinition) object

**Samples**

> ```
> GET/api/report/reportByProperty/e09f9d45-b721-4012-b8e7-c31c58d52af3/3HTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"inaccessible":false,"category":{"name":"Sales","type":0,"parentId":null,"tenantId":null,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":null,"dashboards":null,"id":"93de93b9-d5d1-48f1-800d-1db1ffc02614","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null},"subCategory":null,"reportRelationship":[],"reportPart":[],"reportFilter":{"filterFields":[],"logic":"","visible":true,"reportId":"e09f9d45-b721-4012-b8e7-c31c58d52af3","id":"93f2af72-1309-46fe-a779-ff426574619f","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null},"calculatedFields":[],"accesses":[],"schedules":[],"dynamicQuerySourceFields":[],"name":"FactInternetSales Date","reportDataSource":[],"type":0,"previewRecord":10,"advancedMode":true,"allowNulls":false,"isDistinct":false,"categoryId":"93de93b9-d5d1-48f1-800d-1db1ffc02614","categoryName":"Sales","subCategoryId":null,"subCategoryName":null,"tenantId":null,"tenantName":null,"description":"","title":"","lastViewed":"2017-01-05T07:25:53.557","owner":"John Doe","ownerId":"9fc0f5c2-decf-4d65-9344-c59a1704ea0c","excludedRelationships":"","numberOfView":7,"renderingTime":1359.8571428571429,"createdById":"9fc0f5c2-decf-4d65-9344-c59a1704ea0c","modifiedById":"9fc0f5c2-decf-4d65-9344-c59a1704ea0c","snapToGrid":false,"usingFields":"78c99b13-af5d-47b9-9d2a-9fae8bc2b51c,80d98874-67fd-49f7-8755-497c0393736b","hasDeletedObjects":false,"header":{"removed":"for brevity"},"footer":{"removed":"for brevity"},"titleDescription":{"removed":"for brevity"},"sourceId":null,"checked":false,"copyDashboard":false,"exportFormatSetting":{"removed":"for brevity"},"deletable":true,"editable":true,"movable":true,"copyable":true,"accessPriority":1,"active":true,"id":"e09f9d45-b721-4012-b8e7-c31c58d52af3","state":0,"deleted":false,"inserted":true,"version":6,"created":"2016-11-21T07:22:01","createdBy":"John Doe","modified":"2016-11-21T08:42:07.763","modifiedBy":"John Doe"}
> ```

## POST report

Saves a report.

**Request**

> Payload: a [ReportSavingParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415512047639-ReportSavingParameter) object

**Response**

> A [ReportSavingResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492872727-ReportSavingResult) object

**Samples**

> ```
> POST/api/reportHTTP/1.1
> ```
>
> Sample payload:
>
> ```
> {"reportKey":{"key":"b95d2611-10c5-4808-aa68-9db2ccc719ff","modified":null},"section":2,"saveAs":false,"ignoreCheckChange":false,"report":{"name":"Report01","type":"Templates","previewRecord":10,"advancedMode":false,"allowNulls":false,"isDistinct":false,"category":{"id":null,"name":"","type":"Templates"},"subCategory":{"id":null,"name":"","type":"Templates"},"reportDataSource":[{"aliasId":"1a67e4e1-7b76-4aac-b905-027bb4302845_Categories","querySourceId":"1a67e4e1-7b76-4aac-b905-027bb4302845","querySourceName":"Categories","selected":true,"categoryId":"00000000-0000-0000-0000-000000000000","primaryFields":[{"name":"CategoryID","alias":"","dataType":"int","izendaDataType":"Numeric","allowDistinct":false,"visible":true,"filterable":true,"deleted":false,"querySourceId":"00000000-0000-0000-0000-000000000000","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":0,"position":0,"extendedProperties":"{\"PrimaryKey\":true}","physicalChange":0,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"fullName":null,"calculatedTree":null,"reportId":null,"originalName":"CategoryID","isParameter":false,"isCalculated":false,"querySource":null,"id":"9fd3b009-4809-47ad-845b-96a9dc4cf71e","state":0,"modified":"0001-01-01T00:00:00.0000000-08:00","dateTimeNow":"2016-06-10T07:29:35.9754058Z"}]}],"reportRelationship":[{"id":"1a67e4e1-7b76-4aac-b905-027bb4302845","category":null,"databaseName":"Northwind","schemaName":"dbo","dataObject":"Categories","dataObjectType":"Table","relationshipKeyJoins":[],"relationshipPosition":0,"level":1}],"reportFilter":{"status":0,"logic":"","visible":false,"filterFields":[],"id":"19578f3d-ce47-4e94-a46b-2f7216e059b7","reportId":"b95d2611-10c5-4808-aa68-9db2ccc719ff"},"reportPart":[{"isDirty":true,"reportPartContent":{"isDirty":false,"type":3,"columns":{"elements":[{"isDirty":false,"name":"CategoryName","properties":{"isDirty":false,"dataFormattings":{"function":"","functionInfo":{},"format":"Format","font":{"family":"Georgia","size":8,"bold":true,"italic":false,"underline":false,"color":"","backgroundColor":""},"alignment":"alignLeft","sort":"","color":{"textColor":{},"cellColor":{}},"alternativeText":{},"customURL":{"url":"","option":"Open link in New Window"},"embeddedJavascript":{"script":""},"subTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""},"grandTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""}},"headerFormating":{"width":{"value":0,"unit":"pixels"},"height":0,"font":{"family":null,"size":null,"bold":null,"italic":null,"underline":null,"color":null,"backgroundColor":null},"alignment":null,"wordWrap":null,"columnGroup":""},"drillDown":{"subReport":{"selectedReport":null,"style":null,"reportPartUsed":null,"reportFilter":true,"mappingFields":[]}}},"position":1,"field":{"fieldId":"0c140c5a-fa48-46f8-91ae-656a394c48ce","fieldName":"CategoryName","fieldNameAlias":"CategoryName","dataFieldType":"Text","querySourceId":"1a67e4e1-7b76-4aac-b905-027bb4302845","querySourceType":"Table","sourceAlias":"Categories","relationshipId":null,"visible":true,"calculatedTree":null},"isDeleted":false,"isSelected":false}]},"rows":{"elements":[]},"values":{"elements":[]},"separators":{"elements":[]},"groups":{"elements":[]},"properties":{"isDirty":false,"generalInfo":{"gridStyle":"Vertical","separatorStyle":"Comma"},"table":{"border":{"top":{},"right":{},"bottom":{},"midVer":{},"left":{},"midHor":{}},"backgroundColor":"#efefef"},"columns":{"width":{"value":60,"unit":"Pixels"},"alterBackgroundColor":false},"rows":{"height":15,"alterBackgroundColor":false},"headers":{"font":{"family":"Georgia","size":12,"bold":true,"italic":false,"underline":false,"backgroundColor":"#dbf2ff"},"alignment":"left","wordWrap":true,"removeHeaderForExport":false},"grouping":{"useSeparator":false},"view":{"dataRefreshInterval":{"enable":false,"updateInterval":0,"isAll":true,"latestRecord":0}}},"settings":{},"title":{"text":"title","properties":{},"settings":{"font":{"family":"","size":0,"bold":true,"italic":false,"underline":false,"color":"","highlightColor":""},"alignment":{"alignment":""}},"elements":[]},"description":{"text":"desc","properties":{},"settings":{"font":{"family":"","size":0,"bold":true,"italic":false,"underline":false,"color":"","highlightColor":""},"alignment":{"alignment":""}},"elements":[]}},"positionX":0,"positionY":0,"width":12,"height":4,"state":1,"modified":null,"isBackSide":true,"title":"Grid"}]}}
> ```
>
> Successful response:
>
> ```
> {"reportKey":{"key":"b95d2611-10c5-4808-aa68-9db2ccc719ff","tenantId":null},"report":{"fields":"omitted",},"success":true,"messages":null,"data":null}
> ```

Note

In the Izenda UI, for a Form report part payload, the column elements properties in the **reportPart > reportPartContent > columns > elements > properties** has higher precedence than the properties in **htmlcontent** (field-prop). Thus, system will display the field(s) in Izenda UI follow the column elements properties.

For example: In the image below, the visible property of ShipCountry field is different between the column elements properties and the htmlcontent. Thus, in the Izenda UI, this field will keep the value `"fieldItemVisible":false` and not be displayed in report part.

[![../_images/POST_report_properties_not_match.png](https://devnet.logianalytics.com/hc/article_attachments/4415511715735/post_report_properties_not_match.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511715735/post_report_properties_not_match.png)

## POST report/draft

Saves a report as draft.

**Request**

> Payload: a [ReportSavingParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415512047639-ReportSavingParameter) object

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object

**Samples**

> ```
> POST/api/report/draftHTTP/1.1
> ```
>
> Sample payload:
>
> ```
> {"reportKey":{"key":null,"modified":null},"saveAs":false,"report":{"name":"TestReport","type":"Reports","previewRecord":100,"advancedMode":true,"allowNulls":false,"distinct":false,"category":null,"subCategory":null,"reportDataSource":[{"querySourceId":"aff154e4-af1f-4b57-8e80-72400ca6deac","querySourceName":"CustOrdersDetail","selected":true,"categoryId":"00000000-0000-0000-0000-000000000000","primaryFields":[]}],"reportRelationship":[],"reportFilter":null}}
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null}
> ```

## POST report/cancel

Deletes temporary data of a report.

**Request**

> Payload: a [ReportParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415504768919-ReportParameter) object

**Response**
:   A [ReportSavingResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492872727-ReportSavingResult) object

**Samples**

> ```
> POST/api/report/cancelHTTP/1.1
> ```
>
> Request Payload:
>
> ```
> {"reportKey":{"key":"4fd37956-4b97-4efb-9d71-c750b0c36474"}}
> ```
>
> Successful response:
>
> ```
> {"reportKey":{"key":null,"tenantId":null},"report":null}
> ```

## POST report/loadForEdit

Returns an object with report key and report’s details.

**Request**

> Payload: a [ReportParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415504768919-ReportParameter) object

**Response**

> A [ReportSavingParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415512047639-ReportSavingParameter) object, with the **report** field fully populated

**Samples**

> ```
> POST/api/report/loadForEditHTTP/1.1
> ```
>
> Payload:
>
> ```
> {"reportKey":{"key":"9d34d5d2-447f-465e-8223-d7f66378b5f9"}}
> ```
>
> Sample response:
>
> ```
> {"saveAs":false,"report":{"category":{"name":"","type":1,"parentId":null,"tenantId":null,"subReportCategories":null,"id":"00000000-0000-0000-0000-000000000000","state":0,"modified":null},"subCategory":{"name":"","type":1,"parentId":null,"tenantId":null,"subReportCategories":null,"id":"00000000-0000-0000-0000-000000000000","state":0,"modified":null},"reportDataSource":[{"reportId":"00000000-0000-0000-0000-000000000000","querySourceId":"e1bc2021-3874-4e5a-b51e-d799cef5e29a","id":"bc4cabe6-6f64-473d-b5c8-d3faf314e1fb","state":0,"modified":null}],"reportRelationship":[],"reportPart":[],"reportFilter":{"filterFields":[],"logic":"","visible":false,"reportId":"00000000-0000-0000-0000-000000000000","id":"e610c0a9-c074-47ec-a633-1195a589549c","state":0,"modified":null},"calculatedFields":[],"name":"","type":1,"previewRecord":10,"advancedMode":true,"allowNulls":false,"isDistinct":false,"categoryId":null,"categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":null,"description":null,"createdBy":null,"createdDate":"0001-01-01T00:00:00","modifiedBy":null,"version":null,"numberOfViews":0,"averageRenderingTime":0.0,"id":"00000000-0000-0000-0000-000000000000","state":1,"modified":null},"section":0,"tenantId":null,"ignoreCheckChange":false,"reportKey":{"key":"9d34d5d2-447f-465e-8223-d7f66378b5f9","tenantId":null}}
> ```

## GET report/(tenant\_id)

Returns all report categories together with the reports inside.

**Request**

> No payload

**Response**

> An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects

**Samples**

> ```
> GET/api/report/b5b3a5cc-9e55-424c-ae85-ba92ec3b934eHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"name":"ACME","type":1,"parentId":null,"tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":null,"type":1,"parentId":"2b3f5a54-a719-41a9-a475-91e0353a4771","tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[{"name":"Example","reportDataSource":[],"type":0,"previewRecord":0,"advancedMode":false,"allowNulls":false,"isDistinct":false,"categoryId":"2b3f5a54-a719-41a9-a475-91e0353a4771","categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":"00000000-0000-0000-0000-000000000000","tenantName":null,"description":null,"title":null,"lastViewed":null,"owner":null,"ownerId":null,"excludedRelationships":null,"numberOfView":0,"renderingTime":0,"createdById":"9d2f1d51-0e3d-44db-bfc7-da94a7581bfe","modifiedById":null,"snapToGrid":false,"usingFields":null,"hasDeletedObjects":false,"header":null,"footer":null,"titleDescription":null,"sourceId":null,"checked":false,"copyDashboard":false,"exportFormatSetting":null,"deletable":false,"editable":false,"movable":false,"copyable":false,"accessPriority":0,"active":false,"fullPath":null,"computeNameSettings":null,"isGlobal":false,"isCheck":false,"id":"f4d5aa24-7ed3-49f4-8c4b-e274ced11191","state":0,"deleted":false,"inserted":true,"version":0,"created":null,"createdBy":"ACME Cooperation","modified":null,"modifiedBy":null}],"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":null,"state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"ACME Cooperation","modified":null,"modifiedBy":null}],"checked":false,"reports":[],"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"2b3f5a54-a719-41a9-a475-91e0353a4771","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"ACME Cooperation","modified":null,"modifiedBy":null}]
> ```

## POST report/validateReportName

Validates that a report name is unique and not empty.

**Request**

> Payload: a [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492852759-ReportDefinition) object, with **name**, **type**, **category** and **subCategory** fields populated.

**Response**

> A [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object, with **success** field means whether the report name is unique (in the specified category and sub-category)

**Samples**

> ```
> POST/api/report/validateReportNameHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"id":null,"name":"AnExistingName","type":1,"category":{"id":"b45d865c-bea2-41be-9986-8a912981bfed","name":"Category A","type":1,"tenantId":null},"subCategory":{"id":null,"name":"","type":1,"tenantId":null}}
> ```
>
> Response when that report name already exists in Category A:
>
> ```
> {"success":false,"messages":[{"key":"Name","detail":null,"messages":["This template name already exists in the \"Category A\" category."]}],"data":null}
> ```

## POST report/validate

Validates that a report name is unique and its filter and relationships are valid.

**Request**

> Payload: a [ReportSavingParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415512047639-ReportSavingParameter) object

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object, with **success** field means whether the validation is successful

**Samples**

> ```
> POST/api/report/validateHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"reportKey":{"key":"940529fd-f1fb-4d98-8def-c8dcfa7eba84","tenantId":null},"report":{"id":"940529fd-f1fb-4d98-8def-c8dcfa7eba84","type":"Templates","category":{"id":"0adae39c-1db0-466d-820b-9f3f59c8e199"},"subCategory":{"id":null}}}
> ```
>
> Sample response:
>
> ```
> {"success":true,"message":null,"errors":[]}
> ```

## POST report/search

Deprecated since version 2.0.0: superseded by [POST report/search2](#post-report-search2)

Searches for reports.

**Request**

> Payload: a [ReportDashboardSearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415492849559-ReportDashboardSearchCriteria) object

**Response**

> An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects

**Samples**

> ```
> POSTapi/report/searchHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"criterias":[{"key":"Category","value":"ACME"}],"isUncategorized":false,"sortCriteria":{"key":"ReportName","descending":false},"tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","type":"0","skipItems":0,"pageSize":100,"parentIds":[],"includeGlobalCategory":true,"isGlobal":null}
> ```
>
> Sample response:
>
> ```
> [{"name":"ACME","type":0,"parentId":null,"tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":"Example","type":0,"parentId":"5ca51cd0-1f63-44ca-9711-ba6c988a520a","tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[{"name":"ExampleReport","reportDataSource":[],"type":0,"previewRecord":0,"advancedMode":false,"allowNulls":false,"isDistinct":false,"categoryId":"5ca51cd0-1f63-44ca-9711-ba6c988a520a","categoryName":null,"subCategoryId":"41a3dff9-d1da-48e5-b4fb-50775324bd3d","subCategoryName":null,"tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","tenantName":null,"description":"","title":null,"lastViewed":"2017-09-28T07:50:02.533","owner":"John Doe","ownerId":"9d2f1d51-0e3d-44db-bfc7-da94a7581bfe","excludedRelationships":null,"numberOfView":3,"renderingTime":646.66667,"createdById":"9d2f1d51-0e3d-44db-bfc7-da94a7581bfe","modifiedById":null,"snapToGrid":false,"usingFields":null,"hasDeletedObjects":false,"header":null,"footer":null,"titleDescription":null,"sourceId":null,"checked":false,"copyDashboard":false,"exportFormatSetting":null,"deletable":true,"editable":true,"movable":true,"copyable":true,"accessPriority":1,"active":true,"fullPath":null,"computeNameSettings":null,"isGlobal":false,"isCheck":false,"id":"5447a5c1-a0c8-4bf6-bd68-f09234ba5e84","state":0,"deleted":false,"inserted":true,"version":2,"created":"2017-09-27T10:20:46.277","createdBy":"John Doe","modified":"2017-09-28T07:49:39.25","modifiedBy":"John Doe"}],"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"41a3dff9-d1da-48e5-b4fb-50775324bd3d","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"checked":false,"reports":[],"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"5ca51cd0-1f63-44ca-9711-ba6c988a520a","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}]
> ```

## POST report/search2

Searches for reports, with total number of items.

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
> POST/api/report/search2HTTP/1.1
> ```
>
> Payload:
>
> ```
> {"criterias":[{"key":"Category","value":"ACME"}],"isUncategorized":false,"sortCriteria":{"key":"ReportName","descending":false},"tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","type":"0","skipItems":0,"pageSize":100,"parentIds":[],"includeGlobalCategory":true,"isGlobal":null}
> ```
>
> Response
>
> ```
> {"data":[{"name":"Local Categories","type":0,"parentId":null,"tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":"ACME","type":0,"parentId":null,"tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":"Example","type":0,"parentId":"5ca51cd0-1f63-44ca-9711-ba6c988a520a","tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[{"name":"ExampleReport","reportDataSource":[],"type":0,"previewRecord":0,"advancedMode":false,"allowNulls":false,"isDistinct":false,"categoryId":"5ca51cd0-1f63-44ca-9711-ba6c988a520a","categoryName":null,"subCategoryId":"41a3dff9-d1da-48e5-b4fb-50775324bd3d","subCategoryName":null,"tenantId":"b5b3a5cc-9e55-424c-ae85-ba92ec3b934e","tenantName":null,"description":"","title":null,"lastViewed":"2017-09-28T07:50:02.533","owner":"John Doe","ownerId":"9d2f1d51-0e3d-44db-bfc7-da94a7581bfe","excludedRelationships":null,"numberOfView":3,"renderingTime":646.66667,"createdById":"9d2f1d51-0e3d-44db-bfc7-da94a7581bfe","modifiedById":null,"snapToGrid":false,"usingFields":null,"hasDeletedObjects":false,"header":null,"footer":null,"titleDescription":null,"sourceId":null,"checked":false,"copyDashboard":false,"exportFormatSetting":null,"deletable":true,"editable":true,"movable":true,"copyable":true,"accessPriority":1,"active":true,"fullPath":null,"computeNameSettings":null,"isGlobal":false,"isCheck":false,"id":"5447a5c1-a0c8-4bf6-bd68-f09234ba5e84","state":0,"deleted":false,"inserted":true,"version":2,"created":"2017-09-27T10:20:46.277","createdBy":"John Doe","modified":"2017-09-28T07:49:39.25","modifiedBy":"John Doe"}],"dashboards":[],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"41a3dff9-d1da-48e5-b4fb-50775324bd3d","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null},],"checked":false,"reports":[],"dashboards":[],"numOfChilds":5,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"5ca51cd0-1f63-44ca-9711-ba6c988a520a","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"checked":false,"reports":[],"dashboards":[],"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"09f8c4ab-0fe8-4e03-82d1-7949e3738f87","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"totalItems":45,"numOfChilds":1,"numOfCheckedChilds":0,"indeterminate":false,"isLastPage":true}
> ```

## POST report/advancedSearch

Searches for reports with advanced options.

**Request**

> Payload: a [ReportPagedRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492860439-ReportPagedRequest) object
>
> Note
>
> The keys for [SearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415512052759-SearchCriteria) that this API support:   
> - All   
> - ReportName   
> - ReportDescription   
> - DashboardName   
> - DashboardDescription   
> - CreatedBy   
> - CreatedDate   
> - LastEditedBy   
> - LastEditedDate   
> - Version   
> - NumberOfView   
> - RenderingTime   
> - ReportOwner   
> - LastViewed   
> - Category   
> - SubCategory   
> - CategoryId   
> - CreatedDateFrom   
> - CreatedDateTo   
> - LastEditedDateFrom   
> - LastEditedDateTo

**Response**

> A [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) object, with **result** field containing an array of [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492852759-ReportDefinition) objects

**Samples**

> ```
> POST/api/report/advancedSearchHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"subcategoryid":null,"categoryId":null,"tenantId":null,"pageSize":10,"pageIndex":1,"sortOrders":[{"key":"reportname","descending":true}],"criteria":[{"key":"reportName","value":"test","operation":1}]}
> ```
>
> Sample response:
>
> ```
> {"result":[],"pageIndex":1,"pageSize":10,"total":0}
> ```

## GET report/reportMode

Returns the report mode.

**Request**

> No payload

**Response**

> The value of the report mode
>
> * 0 = Simple
> * 1 = Advanced

**Samples**

> ```
> GET/api/report/reportModeHTTP/1.1
> ```
>
> Sample response:
>
> ```
> 1
> ```

## POST report/reportMode/{value}

Sets the report mode to Simple or Advanced.

**Request**

> * call report/reportMode/0 to set Simple mode
> * call report/reportMode/1 to set Advanced mode

**Response**

> * true if succeeded
> * false if there was an error

**Samples**

> ```
> POST/api/report/reportMode/0HTTP/1.1
> ```
>
> Successful response:
>
> ```
> true
> ```

## POST report/detectReportChange

Verifies that all report details are up to date, without physical changes, and valid.

**Request**

> Payload: a [ReportSavingParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415512047639-ReportSavingParameter) object, with **section** field specifies where to detect changes
>
> > * 0 = All
> > * 1 = DataSource
> > * 2 = Fields
> > * 3 = CalculatedField

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object, with **success** field means whether the report is up to date, without physical changes, and valid

**Samples**

> ```
> POST/api/report/detectReportChangeHTTP/1.1
> ```
>
> Request Payload to check if a new report with only one data source has physical changes:
>
> ```
> {"reportKey":{"key":null,"modified":null},"section":1,"report":{"reportDataSource":[{"querySourceId":"1a67e4e1-7b76-4aac-b905-027bb4302845"}]}}
> ```
>
> Successful response:
>
> ```
> {"success":true,"messages":null}
> ```
>
> Request Payload for an existing report with two data sources, filter and report part:
>
> ```
> {"reportKey":{"key":"37e99389-fa8a-4f9f-9d03-f6362240c931","modified":null},"section":2,"report":{"reportDataSource":[{"aliasId":"84340ae7-275e-4bd5-bd77-89916341f20e_Order Details","querySourceId":"84340ae7-275e-4bd5-bd77-89916341f20e","querySourceName":"Order Details","selected":true,"categoryId":"00000000-0000-0000-0000-000000000000","primaryFields":[{"name":"OrderID","alias":"","dataType":"int","izendaDataType":"Numeric","allowDistinct":false,"visible":true,"filterable":true,"deleted":false,"querySourceId":"00000000-0000-0000-0000-000000000000","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":0,"position":0,"extendedProperties":"{\"PrimaryKey\":true}","physicalChange":0,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"fullName":null,"calculatedTree":null,"reportId":null,"originalName":"OrderID","isParameter":false,"isCalculated":false,"querySource":null,"id":"9a4c52a4-f931-40d0-88b9-7f914d49581b","state":0,"modified":"0001-01-01T00:00:00.0000000-08:00","dateTimeNow":"2016-06-13T07:22:35.8918127Z"},{"name":"ProductID","alias":"","dataType":"int","izendaDataType":"Numeric","allowDistinct":false,"visible":true,"filterable":true,"deleted":false,"querySourceId":"00000000-0000-0000-0000-000000000000","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":0,"position":0,"extendedProperties":"{\"PrimaryKey\":true}","physicalChange":0,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"fullName":null,"calculatedTree":null,"reportId":null,"originalName":"ProductID","isParameter":false,"isCalculated":false,"querySource":null,"id":"1d379f29-02ae-4f51-ac3a-a627694c3539","state":0,"modified":"0001-01-01T00:00:00.0000000-08:00","dateTimeNow":"2016-06-13T07:22:35.8918127Z"}]},{"aliasId":"8fda0166-5f38-4ca1-ae20-9b6cab288f9d_Orders","querySourceId":"8fda0166-5f38-4ca1-ae20-9b6cab288f9d","querySourceName":"Orders","selected":true,"categoryId":"00000000-0000-0000-0000-000000000000","primaryFields":[{"name":"orderid_alias","alias":"","dataType":"int","izendaDataType":"Numeric","allowDistinct":false,"visible":true,"filterable":true,"deleted":false,"querySourceId":"00000000-0000-0000-0000-000000000000","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":0,"position":0,"extendedProperties":"{\"PrimaryKey\":true}","physicalChange":0,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"fullName":null,"calculatedTree":null,"reportId":null,"originalName":"OrderID","isParameter":false,"isCalculated":false,"querySource":null,"id":"93157476-d4e6-49bb-8900-2fda43e46f87","state":0,"modified":"0001-01-01T00:00:00.0000000-08:00","dateTimeNow":"2016-06-13T07:22:35.8918127Z"}]}],"reportRelationship":[{"tempId":"6da998ae-5451-4a45-ab86-69894e1b3a13","joinConnectionId":"a0028b41-f820-4640-927c-68f6ef730b0f","foreignConnectionId":"a0028b41-f820-4640-927c-68f6ef730b0f","joinQuerySourceId":"84340ae7-275e-4bd5-bd77-89916341f20e","joinQuerySourceName":"Order Details","joinDataSourceCategoryName":"","joinDataSourceCategoryId":"00000000-0000-0000-0000-000000000000","foreignDataSourceCategoryName":"","foreignDataSourceCategoryId":"00000000-0000-0000-0000-000000000000","foreignQuerySourceId":"8fda0166-5f38-4ca1-ae20-9b6cab288f9d","foreignQuerySourceName":"Orders","joinFieldId":"9a4c52a4-f931-40d0-88b9-7f914d49581b","joinFieldName":"OrderID","foreignFieldId":"93157476-d4e6-49bb-8900-2fda43e46f87","foreignFieldName":"orderid_alias","alias":"","systemRelationship":true,"joinType":"Inner","parentRelationshipId":"5147885d-0bac-4252-8d33-f9fd96bd3b8e","position":null,"relationshipKeyJoins":[],"reportId":"00000000-0000-0000-0000-000000000000","selectedForeignAlias":"8fda0166-5f38-4ca1-ae20-9b6cab288f9d_Orders","id":"6da998ae-5451-4a45-ab86-69894e1b3a13","state":1,"validationKey":"5147885d-0bac-4252-8d33-f9fd96bd3b8e","relationshipPosition":0,"invalidAlias":null,"hidden":false,"level":1}],"reportFilter":{"status":0,"logic":null,"visible":false,"filterFields":[{"connectionName":"Northwind","querySourceCategoryName":"dbo","sourceFieldName":"ShipCountry","sourceFieldVisible":true,"sourceFieldFilterable":true,"sourceDataObjectName":"Orders","dataType":"Text","filterId":"00000000-0000-0000-0000-000000000000","querySourceFieldId":"d0f88020-8d3f-4f80-a1ac-0c187f87dfd3","querySourceType":"Table","querySourceId":"8fda0166-5f38-4ca1-ae20-9b6cab288f9d","relationshipId":null,"alias":"ShipCountry","position":1,"visible":false,"required":false,"cascading":true,"operatorId":"737307d1-1e5f-407f-889f-1b3c9a66dd6f","operatorSetting":null,"value":"'US'","sortType":"Unsorted","fontFamily":null,"fontSize":0,"textColor":null,"backgroundColor":null,"fontBold":false,"fontItalic":false,"fontUnderline":false,"id":"00000000-0000-0000-0000-000000000000","status":0,"modified":null,"dateTimeNow":"2016-06-13T07:23:25.9138114Z","isParameter":false,"sourceDataObjectFullName":"Northwind.dbo.Orders","selected":false}],"id":"00000000-0000-0000-0000-000000000000","reportId":"37e99389-fa8a-4f9f-9d03-f6362240c931"},"reportPart":[{"isDirty":true,"reportPartContent":{"isDirty":false,"type":3,"columns":{"elements":[{"isDirty":false,"name":"ShipCity","properties":{"isDirty":false,"dataFormattings":{"function":"","functionInfo":{},"format":"Format","font":{"family":"Georgia","size":8,"bold":true,"italic":false,"underline":false,"color":"","backgroundColor":""},"alignment":"alignLeft","sort":"","color":{"textColor":{},"cellColor":{}},"alternativeText":{},"customURL":{"url":"","option":"Open link in New Window"},"embeddedJavascript":{"script":""},"subTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""},"grandTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""}},"headerFormating":{"width":{"value":0,"unit":"pixels"},"height":0,"font":{"family":null,"size":null,"bold":null,"italic":null,"underline":null,"color":null,"backgroundColor":null},"alignment":null,"wordWrap":null,"columnGroup":""},"drillDown":{"subReport":{"selectedReport":null,"style":null,"reportPartUsed":null,"reportFilter":true,"mappingFields":[]}},"otherProps":{}},"position":1,"field":{"fieldId":"f5b9bac6-aa76-402c-8ade-6b8f619e9ced","fieldName":"ShipCity","fieldNameAlias":"ShipCity","dataFieldType":"Text","querySourceId":"8fda0166-5f38-4ca1-ae20-9b6cab288f9d","querySourceType":"Table","sourceAlias":"Orders","relationshipId":null,"visible":true,"calculatedTree":null},"isDeleted":false,"isSelected":false},{"isDirty":false,"name":"ProductID","properties":{"isDirty":false,"dataFormattings":{"function":"","functionInfo":{},"format":"Format","font":{"family":"Georgia","size":8,"bold":true,"italic":false,"underline":false,"color":"","backgroundColor":""},"alignment":"alignLeft","sort":"","color":{"textColor":{},"cellColor":{}},"alternativeText":{},"customURL":{"url":"","option":"Open link in New Window"},"embeddedJavascript":{"script":""},"subTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""},"grandTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""}},"headerFormating":{"width":{"value":0,"unit":"pixels"},"height":0,"font":{"family":null,"size":null,"bold":null,"italic":null,"underline":null,"color":null,"backgroundColor":null},"alignment":null,"wordWrap":null,"columnGroup":""},"drillDown":{"subReport":{"selectedReport":null,"style":null,"reportPartUsed":null,"reportFilter":true,"mappingFields":[]}},"otherProps":{}},"position":2,"field":{"fieldId":"1d379f29-02ae-4f51-ac3a-a627694c3539","fieldName":"ProductID","fieldNameAlias":"ProductID","dataFieldType":"Numeric","querySourceId":"84340ae7-275e-4bd5-bd77-89916341f20e","querySourceType":"Table","sourceAlias":"Order Details","relationshipId":null,"visible":true,"calculatedTree":null},"isDeleted":false,"isSelected":false},{"isDirty":false,"name":"Quantity","properties":{"isDirty":false,"dataFormattings":{"function":"","functionInfo":{},"format":"Format","font":{"family":"Georgia","size":8,"bold":true,"italic":false,"underline":false,"color":"","backgroundColor":""},"alignment":"alignLeft","sort":"","color":{"textColor":{},"cellColor":{}},"alternativeText":{},"customURL":{"url":"","option":"Open link in New Window"},"embeddedJavascript":{"script":""},"subTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""},"grandTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""}},"headerFormating":{"width":{"value":0,"unit":"pixels"},"height":0,"font":{"family":null,"size":null,"bold":null,"italic":null,"underline":null,"color":null,"backgroundColor":null},"alignment":null,"wordWrap":null,"columnGroup":""},"drillDown":{"subReport":{"selectedReport":null,"style":null,"reportPartUsed":null,"reportFilter":true,"mappingFields":[]}},"otherProps":{}},"position":3,"field":{"fieldId":"1eaa3d97-da56-45ca-b61a-8bf3bb253fea","fieldName":"Quantity","fieldNameAlias":"Quantity","dataFieldType":"Numeric","querySourceId":"84340ae7-275e-4bd5-bd77-89916341f20e","querySourceType":"Table","sourceAlias":"Order Details","relationshipId":null,"visible":true,"calculatedTree":null},"isDeleted":false,"isSelected":false}]},"rows":{"elements":[]},"values":{"elements":[]},"separators":{"elements":[]},"properties":{"isDirty":false,"generalInfo":{"gridStyle":"Vertical","separatorStyle":"Comma"},"table":{"border":{"top":{},"right":{},"bottom":{},"midVer":{},"left":{},"midHor":{}},"backgroundColor":"#efefef"},"columns":{"width":{"value":100,"unit":"Pixels"},"alterBackgroundColor":false},"rows":{"height":40,"alterBackgroundColor":false},"headers":{"font":{"family":"Georgia","size":12,"bold":true,"italic":false,"underline":false,"backgroundColor":"#dbf2ff"},"alignment":"left","wordWrap":true,"removeHeaderForExport":false},"grouping":{"useSeparator":false},"view":{"dataRefreshInterval":{"enable":false,"updateInterval":0,"isAll":true,"latestRecord":0}}},"settings":{},"title":{"text":"Title","properties":{},"settings":{"font":{"family":"","size":0,"bold":true,"italic":false,"underline":false,"color":"","highlightColor":""},"alignment":{"alignment":""}},"elements":[]},"description":{"text":"Description line","properties":{},"settings":{"font":{"family":"","size":0,"bold":true,"italic":false,"underline":false,"color":"","highlightColor":""},"alignment":{"alignment":""}},"elements":[]}},"positionX":0,"positionY":0,"width":12,"height":4,"state":1,"modified":null,"isBackSide":true,"expandedLevel":0,"points":[{"key":"All","filter":[{"key":"","value":""}],"expandedLevel":0,"isViewSeparator":false}],"title":"Grid"}]}}
> ```

## POST report/function/{function\_mode}/{data\_type}/(tenant\_id)

Returns a list of report functions filtered by mode (field, sub-total, grand-total), data type, tenant\_id, and optionally filtered by connections of the selected query source ids in payload.

Changed in version 1.25: Changed from GET to POST

**Request**

> Available values for `function_mode`:
>
> > * 0 = Field
> > * 1 = Sub-total
> > * 2 = Grand total
>
> Optional payload: the following object:
>
> | Field | Description | Note |
> | --- | --- | --- |
> | **querySourceIds**  array of strings (GUIDs) | An array of ids of query sources |  |

**Response**

> An array of [ReportFunction](https://devnet.logianalytics.com/hc/en-us/articles/4415504765847-ReportFunction) objects

**Samples**

> ```
> POST/api/report/function/0/TextHTTP/1.1
> ```
>
> Case 1: no Payload
>
> Sample response:
>
> ```
> [{"id":"8a74f4e0-b845-4b9e-adfa-bb678a116878","name":"Count","expression":null,"dataType":"Text","formatDataType":"Numeric","syntax":null,"expressionSyntax":null,"isOperator":false,"userDefined":false,"extendedProperties":{}},{"id":"e3e16575-9739-4ff3-950a-7d149f96b4f0","name":"Count Distinct","expression":null,"dataType":"Text","formatDataType":"Numeric","syntax":null,"expressionSyntax":null,"isOperator":false,"userDefined":false,"extendedProperties":{}},{"id":"7f942ac7-08d8-41fa-9e89-bad96f07f102","name":"Group","expression":null,"dataType":"Text","formatDataType":"Text","syntax":null,"expressionSyntax":null,"isOperator":false,"userDefined":false,"extendedProperties":{}},{"id":"10a6655f-6954-462d-a57e-5df3c17089d5","name":"Maximum","expression":null,"dataType":"Text","formatDataType":"Text","syntax":null,"expressionSyntax":null,"isOperator":false,"userDefined":false,"extendedProperties":{}},{"id":"36d8f605-1242-4c43-9b46-aced94b62709","name":"Minimum","expression":null,"dataType":"Text","formatDataType":"Text","syntax":null,"expressionSyntax":null,"isOperator":false,"userDefined":false,"extendedProperties":{}}]
> ```
>
> ```
> POST/api/report/function/0/TextHTTP/1.1
> ```
>
> Case 2: with Request Payload:
>
> ```
> {"querySourceIds":["35af86ee-6e8b-4e9b-829d-ea0b38ec575b"]}
> ```
>
> Sample response:
>
> ```
> [{"id":"8a74f4e0-b845-4b9e-adfa-bb678a116878","name":"Count","expression":null,"dataType":"Text","formatDataType":"Numeric","syntax":null,"expressionSyntax":null,"isOperator":false,"userDefined":false,"extendedProperties":{}},{"id":"e3e16575-9739-4ff3-950a-7d149f96b4f0","name":"Count Distinct","expression":null,"dataType":"Text","formatDataType":"Numeric","syntax":null,"expressionSyntax":null,"isOperator":false,"userDefined":false,"extendedProperties":{}},{"id":"7f942ac7-08d8-41fa-9e89-bad96f07f102","name":"Group","expression":null,"dataType":"Text","formatDataType":"Text","syntax":null,"expressionSyntax":null,"isOperator":false,"userDefined":false,"extendedProperties":{}},{"id":"10a6655f-6954-462d-a57e-5df3c17089d5","name":"Maximum","expression":null,"dataType":"Text","formatDataType":"Text","syntax":null,"expressionSyntax":null,"isOperator":false,"userDefined":false,"extendedProperties":{}},{"id":"36d8f605-1242-4c43-9b46-aced94b62709","name":"Minimum","expression":null,"dataType":"Text","formatDataType":"Text","syntax":null,"expressionSyntax":null,"isOperator":false,"userDefined":false,"extendedProperties":{}}]
> ```

## GET report/allReports/(tenant\_id)

Returns a list of all reports filtered by tenant\_id if provided.

**Request**

> No payload

**Response**

> An array of [Category](https://devnet.logianalytics.com/hc/en-us/articles/4415492768663-Category) objects

**Samples**

> ```
> POST/api/report/allReportsHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"name":"CN","type":0,"parentId":null,"tenantId":null,"isGlobal":false,"createdById":null,"canDelete":false,"editable":false,"savable":false,"subCategories":[{"name":null,"type":0,"parentId":"dc04087a-a761-43fb-b82d-5dd56fe8d6f3","tenantId":null,"isGlobal":false,"createdById":null,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[{"name":"091117_api","reportDataSource":[],"type":0,"previewRecord":0,"advancedMode":false,"allowNulls":false,"isDistinct":false,"categoryId":"dc04087a-a761-43fb-b82d-5dd56fe8d6f3","categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":"00000000-0000-0000-0000-000000000000","tenantName":null,"description":"","title":null,"lastViewed":"2017-09-11T04:43:31.5100000+07:00","owner":"John Doe","ownerId":"376545c8-6bfa-4025-9d25-374f3a61be78","headerContent":null,"footerContent":null,"excludedRelationships":null,"numberOfView":1,"renderingTime":163,"createdById":"376545c8-6bfa-4025-9d25-374f3a61be78","modifiedById":null,"snapToGrid":false,"usingFields":null,"usingFieldIds":null,"usingFieldNames":"[\"[con;#0].[cat;#0].[Order Details].[OrderID]\",\"[con;#0].[cat;#0].[Order Details].[UnitPrice]\"]","hasDeletedObjects":false,"excludedRelationshipIds":[],"header":null,"footer":null,"titleDescriptionContent":null,"titleDescription":null,"exportFormatSettingData":null,"sourceId":null,"params":"[{\"Categories\":[{\"QuerySourceNames\":[\"Order Details\"],\"Id\":\"d555363d-5eb8-476d-8987-702f89750edd\",\"Name\":\"dbo\"}],\"Id\":\"068df001-a54b-466f-89ff-4bcc645f5b47\",\"Name\":\"AZ-Northwind-a8tju4mdx0\"}]","relationships":null,"checked":false,"copyDashboard":false,"exportFormatSetting":null,"deletable":true,"editable":true,"movable":true,"copyable":true,"accessPriority":1,"active":true,"fullPath":null,"computeNameSettings":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"isGlobal":false,"isCheck":false,"id":"b3279ee1-9188-484f-9255-31417b92f68e","state":0,"deleted":false,"inserted":true,"version":1,"created":"2017-09-11T03:38:05.6530000+07:00","createdBy":"John Doe","modified":null,"modifiedBy":null}],"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"status":0,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"00000000-0000-0000-0000-000000000000","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}],"checked":false,"reports":[],"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"status":2,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":"dc04087a-a761-43fb-b82d-5dd56fe8d6f3","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},]
> ```

## POST report/detectSchemaChange

Verifies that all report filter fields are without changes.

**Request**

> Payload: a [ReportSavingParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415512047639-ReportSavingParameter) object

**Response**

> | Field | Required | Description | Note |
> | --- | --- | --- | --- |
> | **hasChanged**  boolean | R | * true if there is any change * false if there is no change |  |
> | **filterFields**  array of objects | R | An array of [ReportFilterField](https://devnet.logianalytics.com/hc/en-us/articles/4415504761879-ReportFilterField) objects |  |

**Samples**

> ```
> POST/api/report/detectSchemaChangeHTTP/1.1
> ```
>
> Sample payload:
>
> ```
> {"reportKey":{"key":"d797d877-6ae1-443a-b5f4-e9fbaeb884a8","modified":null},"section":2,"saveAs":false,"ignoreCheckChange":true,"report":{"name":"don't know 2","type":0,"previewRecord":10,"advancedMode":true,"allowNulls":false,"isDistinct":false,"category":{"id":"97bbeef3-0a80-4a0e-9640-962af1f3f1dc","name":"","type":0},"subCategory":{"id":null,"name":"","type":0},"reportDataSource":[{"aliasId":"d4ed8e8e-3cc1-4815-a5c9-30602847345b_order_details","querySourceId":"d4ed8e8e-3cc1-4815-a5c9-30602847345b","querySourceName":"order_details","selected":true,"categoryId":"3c88fe79-4284-4abe-8b25-5cff7b132474","primaryFields":[{"name":"OrderID","alias":"","dataType":"smallint","izendaDataType":"Numeric","allowDistinct":false,"visible":true,"filterable":true,"deleted":false,"querySourceId":"00000000-0000-0000-0000-000000000000","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":0,"position":0,"extendedProperties":"{\"PrimaryKey\":true}","physicalChange":0,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"fullName":null,"calculatedTree":null,"reportId":null,"originalName":"OrderID","isParameter":false,"isCalculated":false,"hasAggregatedFunction":false,"querySource":null,"fullPath":null,"id":"b5b95958-24f9-40a1-b95b-5e22c2d658d0","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":"0001-01-01T00:00:00.0000000-08:00","modifiedBy":null},{"name":"ProductID","alias":"","dataType":"smallint","izendaDataType":"Numeric","allowDistinct":false,"visible":true,"filterable":true,"deleted":false,"querySourceId":"00000000-0000-0000-0000-000000000000","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":0,"position":0,"extendedProperties":"{\"PrimaryKey\":true}","physicalChange":0,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"fullName":null,"calculatedTree":null,"reportId":null,"originalName":"ProductID","isParameter":false,"isCalculated":false,"hasAggregatedFunction":false,"querySource":null,"fullPath":null,"id":"9c9f3f50-e223-41f4-adfe-0ff407e3bd4c","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":"0001-01-01T00:00:00.0000000-08:00","modifiedBy":null}]},{"aliasId":"b5f20d85-1a96-493a-8b1e-15dc9b1f26bc_orders","querySourceId":"b5f20d85-1a96-493a-8b1e-15dc9b1f26bc","querySourceName":"orders","selected":true,"categoryId":"3c88fe79-4284-4abe-8b25-5cff7b132474","primaryFields":[{"name":"OrderID","alias":"","dataType":"smallint","izendaDataType":"Numeric","allowDistinct":false,"visible":true,"filterable":true,"deleted":false,"querySourceId":"00000000-0000-0000-0000-000000000000","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":0,"position":0,"extendedProperties":"{\"PrimaryKey\":true}","physicalChange":0,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"fullName":null,"calculatedTree":null,"reportId":null,"originalName":"OrderID","isParameter":false,"isCalculated":false,"hasAggregatedFunction":false,"querySource":null,"fullPath":null,"id":"0f19cd74-e4e3-4ada-acea-03f9c98a8e3b","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":"0001-01-01T00:00:00.0000000-08:00","modifiedBy":null}]}],"reportRelationship":[{"tempId":"73880663-9fe1-4e70-a02b-ea4471978a73","joinConnectionId":"b513ddd4-ef23-4dbb-901d-2be802896616","foreignConnectionId":"b513ddd4-ef23-4dbb-901d-2be802896616","joinQuerySourceId":"d4ed8e8e-3cc1-4815-a5c9-30602847345b","joinQuerySourceName":"order_details","joinDataSourceCategoryName":"postgres","joinDataSourceCategoryId":"3c88fe79-4284-4abe-8b25-5cff7b132474","foreignDataSourceCategoryName":"postgres","foreignDataSourceCategoryId":"3c88fe79-4284-4abe-8b25-5cff7b132474","foreignQuerySourceId":"b5f20d85-1a96-493a-8b1e-15dc9b1f26bc","foreignQuerySourceName":"orders","joinFieldId":"b5b95958-24f9-40a1-b95b-5e22c2d658d0","joinFieldName":"OrderID","foreignFieldId":"0f19cd74-e4e3-4ada-acea-03f9c98a8e3b","foreignFieldName":"OrderID","alias":"","aliasTempId":"alias_709","systemRelationship":false,"joinType":"Inner","parentRelationshipId":"aa176ab4-15cb-451f-8f6a-a46272cf0e15","position":null,"relationshipKeyJoins":[],"reportId":"d797d877-6ae1-443a-b5f4-e9fbaeb884a8","selectedForeignAlias":"b5f20d85-1a96-493a-8b1e-15dc9b1f26bc_orders","id":"73880663-9fe1-4e70-a02b-ea4471978a73","state":0,"validationKey":"73880663-9fe1-4e70-a02b-ea4471978a73","relationshipPosition":0,"needAlias":false,"previousAlias":"","invalidAlias":null,"hidden":false,"level":1}],"reportFilter":{"logic":"","visible":true,"filterFields":[{"connectionName":"postgres","querySourceCategoryName":"public","sourceFieldName":"Freight","sourceFieldVisible":true,"sourceFieldFilterable":true,"sourceDataObjectName":"orders","dataType":"Numeric","filterId":"8c572300-61ad-47ef-8496-94686f7f1301","querySourceFieldId":"46875d94-d79e-4b39-a863-aaede78e176b","querySourceType":"Table","querySourceId":"b5f20d85-1a96-493a-8b1e-15dc9b1f26bc","relationshipId":null,"alias":"Freight","position":1,"visible":false,"required":false,"cascading":true,"operatorId":null,"operatorSetting":null,"value":null,"sortType":"Unsorted","fontFamily":"Roboto","fontSize":8,"textColor":null,"backgroundColor":null,"fontBold":false,"fontItalic":false,"fontUnderline":false,"id":"6f31e0cb-1cdf-416a-a5c5-8a89236903e3","state":0,"modified":null,"dateTimeNow":"","isParameter":false,"sourceDataObjectFullName":"postgres.public.orders","selected":false,"dataFormatId":null}],"id":"8c572300-61ad-47ef-8496-94686f7f1301","reportId":"d797d877-6ae1-443a-b5f4-e9fbaeb884a8"},"reportPart":[{"isDirty":false,"reportPartContent":{"isDirty":false,"type":3,"columns":{"text":null,"properties":{"addSideTotal":false,"useExpanders":false},"settings":{},"elements":[{"reportPartContent":null,"isDirty":false,"name":"Group (ShipCountry)","properties":{"isDirty":true,"fieldItemVisible":true,"dataFormattings":{"function":"7f942ac7-08d8-41fa-9e89-bad96f07f102","functionInfo":{"id":"7f942ac7-08d8-41fa-9e89-bad96f07f102","name":"Group","expression":null,"dataType":"Text","formatDataType":"Text","syntax":null,"expressionSyntax":null,"isOperator":false,"extendedProperties":{}},"format":{},"font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"","backgroundColor":""},"alignment":"alignLeft","sort":"","color":{"textColor":{"rangePercent":null,"rangeValue":null,"value":null},"cellColor":{"rangePercent":null,"rangeValue":null,"value":null}},"alternativeText":{"rangePercent":null,"rangeValue":null,"value":null},"customURL":{"url":"","option":"Open link in New Window"},"embeddedJavascript":{"script":""},"subTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""},"grandTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""}},"headerFormating":{"font":{"family":null,"size":null,"bold":null,"italic":null,"underline":null,"color":null,"backgroundColor":null},"alignment":null,"wordWrap":null,"columnGroup":""},"drillDown":{"subReport":{"selectedReport":null,"style":null,"reportPartUsed":null,"reportFilter":true,"mappingFields":[]}},"otherProps":{}},"position":1,"field":{"fieldId":"8e65a222-66f1-470b-9f53-7f6481110d5e","fieldName":"ShipCountry","fieldNameAlias":"Group (ShipCountry)","dataFieldType":"Text","querySourceId":"b5f20d85-1a96-493a-8b1e-15dc9b1f26bc","querySourceType":"Table","sourceAlias":"orders","relationshipId":"00000000-0000-0000-0000-000000000000","visible":true,"calculatedTree":null,"isCalculated":false},"isDeleted":false,"isSelected":false}],"name":"columns"},"rows":{"text":null,"properties":{"useExpanders":false},"settings":{},"elements":[{"reportPartContent":null,"isDirty":false,"name":"ShipCity","properties":{"isDirty":true,"fieldItemVisible":true,"dataFormattings":{"function":"","functionInfo":{},"format":{},"font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"","backgroundColor":""},"alignment":"alignLeft","sort":"","color":{"textColor":{"rangePercent":null,"rangeValue":null,"value":null},"cellColor":{"rangePercent":null,"rangeValue":null,"value":null}},"alternativeText":{"rangePercent":null,"rangeValue":null,"value":null},"customURL":{"url":"","option":"Open link in New Window"},"embeddedJavascript":{"script":""},"subTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""},"grandTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""}},"headerFormating":{"font":{"family":null,"size":null,"bold":null,"italic":null,"underline":null,"color":null,"backgroundColor":null},"alignment":null,"wordWrap":null,"columnGroup":""},"drillDown":{"subReport":{"selectedReport":null,"style":null,"reportPartUsed":null,"reportFilter":true,"mappingFields":[]}},"otherProps":{}},"position":1,"field":{"fieldId":"63cb0d69-1451-4c51-b825-6946975e58c5","fieldName":"ShipCity","fieldNameAlias":"ShipCity","dataFieldType":"Text","querySourceId":"b5f20d85-1a96-493a-8b1e-15dc9b1f26bc","querySourceType":"Table","sourceAlias":"orders","relationshipId":"00000000-0000-0000-0000-000000000000","visible":true,"calculatedTree":null,"isCalculated":false},"isDeleted":false,"isSelected":false},{"reportPartContent":null,"isDirty":false,"name":"ShipName","properties":{"isDirty":true,"fieldItemVisible":true,"dataFormattings":{"function":"","functionInfo":{},"format":{},"font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"","backgroundColor":""},"alignment":"alignLeft","sort":"","color":{"textColor":{"rangePercent":null,"rangeValue":null,"value":null},"cellColor":{"rangePercent":null,"rangeValue":null,"value":null}},"alternativeText":{"rangePercent":null,"rangeValue":null,"value":null},"customURL":{"url":"","option":"Open link in New Window"},"embeddedJavascript":{"script":""},"subTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""},"grandTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""}},"headerFormating":{"font":{"family":null,"size":null,"bold":null,"italic":null,"underline":null,"color":null,"backgroundColor":null},"alignment":null,"wordWrap":null,"columnGroup":""},"drillDown":{"subReport":{"selectedReport":null,"style":null,"reportPartUsed":null,"reportFilter":true,"mappingFields":[]}},"otherProps":{}},"position":2,"field":{"fieldId":"a28f4649-bf0a-4d2f-ac4b-3ed9e2a4c2a5","fieldName":"ShipName","fieldNameAlias":"ShipName","dataFieldType":"Text","querySourceId":"b5f20d85-1a96-493a-8b1e-15dc9b1f26bc","querySourceType":"Table","sourceAlias":"orders","relationshipId":"00000000-0000-0000-0000-000000000000","visible":true,"calculatedTree":null,"isCalculated":false},"isDeleted":false,"isSelected":false}],"name":"rows"},"values":{"text":null,"properties":{},"settings":{},"elements":[{"reportPartContent":null,"isDirty":false,"name":"Sum (OrderID)","properties":{"isDirty":true,"fieldItemVisible":true,"dataFormattings":{"function":"902a9168-fc01-4a35-92fb-ea67942d099d","functionInfo":{"id":"902a9168-fc01-4a35-92fb-ea67942d099d","name":"Sum","expression":null,"dataType":"Numeric","formatDataType":"Numeric","syntax":null,"expressionSyntax":null,"isOperator":false,"extendedProperties":{}},"format":{},"font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"","backgroundColor":""},"alignment":"alignLeft","sort":"","color":{"textColor":{"rangePercent":null,"rangeValue":null,"value":null},"cellColor":{"rangePercent":null,"rangeValue":null,"value":null}},"alternativeText":{"rangePercent":null,"rangeValue":null,"value":null},"customURL":{"url":"","option":"Open link in New Window"},"embeddedJavascript":{"script":""},"subTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""},"grandTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""}},"headerFormating":{"font":{"family":null,"size":null,"bold":null,"italic":null,"underline":null,"color":null,"backgroundColor":null},"alignment":null,"wordWrap":null,"columnGroup":""},"drillDown":{"subReport":{"selectedReport":null,"style":null,"reportPartUsed":null,"reportFilter":true,"mappingFields":[]}},"otherProps":{}},"position":1,"field":{"fieldId":"0f19cd74-e4e3-4ada-acea-03f9c98a8e3b","fieldName":"OrderID","fieldNameAlias":"Sum (OrderID)","dataFieldType":"Numeric","querySourceId":"b5f20d85-1a96-493a-8b1e-15dc9b1f26bc","querySourceType":"Table","sourceAlias":"orders","relationshipId":"00000000-0000-0000-0000-000000000000","visible":true,"calculatedTree":null,"isCalculated":false},"isDeleted":false,"isSelected":false}],"name":"values"},"separators":{"text":null,"properties":{},"settings":{},"elements":[],"name":"separators"},"properties":{"isDirty":true,"generalInfo":{"gridStyle":"Pivot","separatorStyle":"Comma"},"table":{"backgroundColor":"#efefef","border":{"top":{},"right":{},"bottom":{},"midVer":{},"left":{},"midHor":{}}},"columns":{"width":{"value":null,"unit":"Pixels"},"alterBackgroundColor":false},"rows":{"height":40,"alterBackgroundColor":false},"headers":{"font":{"family":"Roboto","size":14,"bold":true,"italic":false,"underline":false,"backgroundColor":"#dbf2ff"},"alignment":"left","wordWrap":false,"removeHeaderForExport":false},"grouping":{"useSeparator":true},"view":{"dataRefreshInterval":{"enable":false,"updateInterval":0,"isAll":true,"latestRecord":0},"usePagination":false},"printing":{"usePageBreakAfterSeparator":false}},"settings":{},"dataSource":{},"title":{"text":"","properties":{},"settings":{"font":{"family":"","size":14,"bold":true,"italic":false,"underline":false,"color":"","highlightColor":""},"alignment":{"alignment":""}},"elements":[]},"description":{"text":"","properties":{},"settings":{"font":{"family":"","size":14,"bold":false,"italic":false,"underline":false,"color":"","highlightColor":""},"alignment":{"alignment":""}},"elements":[]}},"reportId":"d797d877-6ae1-443a-b5f4-e9fbaeb884a8","positionX":0,"positionY":0,"width":12,"height":4,"state":3,"modified":null,"numberOfRecord":0,"points":[{"key":"All","filter":[{"key":"","value":""}],"expandedLevel":0,"isViewSeparator":false}],"configField":{},"expandedLevel":0,"title":"Grid","id":"9e632295-41c6-41ba-a235-29c525d6ef59"}],"header":{"visible":false,"items":[{"isDirty":false,"type":"image","label":"Image","id":"formatDetails_17","positionX":0,"positionY":0,"width":6,"height":6,"name":"Logo Image","value":"","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","imageUrl":"http://","dashStyle":"solid","thickness":1},{"isDirty":false,"type":"text","label":"Text","id":"formatDetails_18","positionX":20,"positionY":0,"width":12,"height":2,"name":"Report Name","value":"{reportName}","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":1},{"isDirty":false,"type":"thinHorizontalRule","label":"Horizontal Rule","id":"formatDetails_19","positionX":20,"positionY":4,"width":12,"height":1,"name":"Upper Separator Line","value":"{horizontalRule}","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":2},{"isDirty":false,"type":"text","label":"Text","id":"formatDetails_20","positionX":20,"positionY":5,"width":6,"height":2,"name":"Report Generated","value":"Report Generated:","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":1},{"isDirty":false,"type":"text","label":"Text","id":"formatDetails_21","positionX":20,"positionY":7,"width":6,"height":2,"name":"User","value":"User:","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":1},{"isDirty":false,"type":"text","label":"Text","id":"formatDetails_22","positionX":20,"positionY":9,"width":6,"height":2,"name":"Tenant","value":"Tenant:","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":1},{"isDirty":false,"type":"dateTime","label":"Date Time","id":"formatDetails_23","positionX":26,"positionY":5,"width":6,"height":2,"name":"Current Date Time","value":"{currentDateTime}","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":1},{"isDirty":false,"type":"text","label":"Text","id":"formatDetails_24","positionX":26,"positionY":7,"width":6,"height":2,"name":"Current User Name","value":"{currentUserName}","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":1},{"isDirty":false,"type":"text","label":"Text","id":"formatDetails_25","positionX":26,"positionY":9,"width":6,"height":2,"name":"Tenant Name","value":"{tenantName}","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":1},{"isDirty":false,"type":"horizontalRule","label":"Horizontal Rule","id":"formatDetails_26","positionX":0,"positionY":11,"width":32,"height":1,"name":"Lower Separator Line","value":"{horizontalRule}","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":4}]},"footer":{"visible":false,"items":[{"isDirty":false,"type":"horizontalRule","label":"Horizontal Rule","id":"formatDetails_27","positionX":0,"positionY":0,"width":32,"height":1,"name":"Separator Line","value":"{horizontalRule}","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":4},{"isDirty":false,"type":"text","label":"Text","id":"formatDetails_28","positionX":0,"positionY":1,"width":10,"height":2,"name":"Footer Text","value":"Footer Text","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":1},{"isDirty":false,"type":"text","label":"Text","id":"formatDetails_29","positionX":20,"positionY":1,"width":4,"height":2,"name":"Page","value":"Page","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":1},{"isDirty":false,"type":"pageNumber","label":"Page Number","id":"formatDetails_30","positionX":24,"positionY":1,"width":8,"height":2,"name":"Page Number","value":"{pageNumber}","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":1}]},"titleDescription":{"visible":false,"items":[{"isDirty":false,"type":"title","label":"Title","id":"formatDetails_31","name":"Title","value":"","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":1},{"isDirty":false,"type":"description","label":"Description","id":"formatDetails_32","name":"Description","value":"","font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"#000","backgroundColor":"#fff"},"color":"#000","dashStyle":"solid","thickness":1}]},"version":0,"schedules":[]},"expandedLevel":0}
> ```
>
> Sample response:
>
> ```
> {"hasChanged":false,"filterFields":[]}
> ```

## POST report/updateResults

Updates the report data model.

**Request**

> Payload: a [ReportSavingParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415512047639-ReportSavingParameter) object

**Response**

> A [ReportSavingResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492872727-ReportSavingResult) object

**Samples**

> ```
> POST/api/report/updateResultsHTTP/1.1
> ```
>
> Sample payload:
>
> ```
> {"reportKey":{"key":null,"modified":null,"tenantId":null},"section":0,"saveAs":false,"ignoreCheckChange":true,"report":{"name":"Example Report Name","type":1,"previewRecord":10,"advancedMode":true,"allowNulls":false,"isDistinct":false,"categoryId":null,"category":{"id":null,"name":"","type":1,"tenantId":null},"subCategory":{"id":null,"name":"","type":1,"tenantId":null},"subCategoryId":null,"reportDataSource":[{"aliasId":"322c3528-a582-4e0c-a5b7-eb7c39e8186a_CustOrdersOrders","querySourceId":"322c3528-a582-4e0c-a5b7-eb7c39e8186a","querySourceName":"CustOrdersOrders","selected":true,"categoryId":"058a12ec-a785-4c50-8f9a-c7d59edcf1be","primaryFields":[]}],"reportRelationship":[],"reportFilter":{"logic":"","visible":false,"filterFields":[{"connectionName":"ACMETest","querySourceCategoryName":"dbo","sourceFieldName":"@CustomerID","sourceFieldVisible":true,"sourceFieldFilterable":true,"sourceDataObjectName":"CustOrdersOrders","dataType":"Text","filterId":"00000000-0000-0000-0000-000000000000","querySourceFieldId":"b55d895f-458a-428c-a62f-0f9858208dc8","querySourceType":"Stored Procedure","querySourceId":"322c3528-a582-4e0c-a5b7-eb7c39e8186a","relationshipId":null,"alias":"@CustomerID","position":1,"visible":true,"required":false,"cascading":false,"operatorId":"737307d1-1e5f-407f-889f-1b3c9a66dd6f","operatorName":null,"operatorSetting":null,"value":"[NULL]","sortType":"ASC","fontFamily":"Roboto","fontSize":14,"textColor":"#000","backgroundColor":"#fff","fontBold":false,"fontItalic":false,"fontUnderline":false,"id":null,"state":1,"modified":null,"dateTimeNow":"","isParameter":true,"sourceDataObjectFullName":"ACMETest.dbo.CustOrdersOrders","selected":false,"dataFormatId":null,"reportPartTitle":null,"reportFieldAlias":null,"uniqueId":"107","isInheritableFilter":false}],"id":null,"reportId":null},"reportPart":[],"header":null,"footer":null,"titleDescription":null,"version":0,"schedules":[],"ownerId":"","accesses":[],"exportFormatSetting":null,"createdById":null,"dynamicQuerySourceFields":[],"snapToGrid":false,"excludedRelationships":null,"isGlobal":false},"expandedLevel":0}
> ```
>
> Sample Response:
>
> ```
> {"reportKey":{"key":"cb680f67-e363-4adc-8035-8e61d698fd66","tenantId":null},"report":{"inaccessible":false,"category":{"name":"","type":1,"parentId":null,"tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[],"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":null,"state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null},"subCategory":{"name":"","type":1,"parentId":null,"tenantId":null,"isGlobal":false,"canDelete":false,"editable":false,"savable":false,"subCategories":[],"checked":false,"reports":[],"dashboards":null,"numOfChilds":0,"numOfCheckedChilds":0,"indeterminate":false,"fullPath":null,"computeNameSettings":null,"isCheck":false,"id":null,"state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null},"reportRelationship":[],"reportPart":[],"reportFilter":{"filterFields":[{"connectionName":"ACMETest","querySourceCategoryName":"dbo","sourceFieldName":"@CustomerID","sourceFieldVisible":true,"sourceFieldFilterable":true,"sourceDataObjectName":"CustOrdersOrders","sourceDataObjectFullName":"ACMETest.dbo.CustOrdersOrders","dataType":"Text","isParameter":true,"isCalculated":false,"calculatedTree":null,"compareFieldCalculatedTree":null,"compareValueCalculatedTree":null,"compareField":null,"selected":false,"dataFormat":null,"reportId":null,"useMappedFieldAlias":false,"uniqueId":"107","comparisionValue":null,"inTimePeriodType":null,"valueInTimePeriod":null,"hasModifiedCalculatedTree":false,"isHiddenFilter":false,"isInheritableFilter":false,"operatorName":null,"type":0,"isRunningField":false,"isDrillDown":false,"filterId":"a78b7d13-acfb-406f-b3bb-63a35c2db5c6","reportFieldAlias":null,"reportPartTitle":null,"querySourceFieldId":"b55d895f-458a-428c-a62f-0f9858208dc8","querySourceType":"Stored Procedure","querySourceId":"322c3528-a582-4e0c-a5b7-eb7c39e8186a","relationshipId":null,"alias":"@CustomerID","position":1,"visible":true,"required":false,"cascading":false,"operatorId":"737307d1-1e5f-407f-889f-1b3c9a66dd6f","operatorSetting":null,"value":"[NULL]","dataFormatId":null,"sortType":"ASC","fontFamily":"Roboto","fontSize":14,"textColor":"#000","backgroundColor":"#fff","fontBold":false,"fontItalic":false,"fontUnderline":false,"querySourceUniqueName":null,"querySourceFieldName":null,"comparisonFieldUniqueName":null,"isNegative":false,"id":"a6dd4b7d-1d61-4bd0-b073-e6d3e85d3c1e","state":1,"deleted":false,"inserted":false,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"baseFilterLogic":null,"logic":"","visible":false,"reportId":"cb680f67-e363-4adc-8035-8e61d698fd66","id":"a78b7d13-acfb-406f-b3bb-63a35c2db5c6","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null},"calculatedFields":[],"accesses":[],"schedules":[],"reportParams":null,"dynamicQuerySourceFields":[{"name":"OrderID","alias":"","dataType":"int","izendaDataType":"Numeric","allowDistinct":true,"visible":true,"filterable":true,"querySourceId":"322c3528-a582-4e0c-a5b7-eb7c39e8186a","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":1,"position":0,"extendedProperties":null,"physicalChange":0,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"isRunningField":false,"fullName":null,"calculatedTree":null,"reportId":"cb680f67-e363-4adc-8035-8e61d698fd66","originalName":null,"originalId":"00000000-0000-0000-0000-000000000000","isParameter":false,"isCalculated":false,"hasAggregatedFunction":false,"querySource":null,"querySourceName":null,"categoryName":null,"inaccessible":false,"originalAlias":null,"fullPath":null,"isCheck":false,"id":"45fff2c2-ccb8-4935-937b-e25f7c2ba2d4","state":1,"deleted":false,"inserted":false,"version":null,"created":null,"createdBy":"John Doe","modified":"0001-01-01T00:00:00","modifiedBy":null},{"name":"OrderDate","alias":"","dataType":"datetime","izendaDataType":"Datetime","allowDistinct":true,"visible":true,"filterable":true,"querySourceId":"322c3528-a582-4e0c-a5b7-eb7c39e8186a","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":1,"position":1,"extendedProperties":null,"physicalChange":0,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"isRunningField":false,"fullName":null,"calculatedTree":null,"reportId":"cb680f67-e363-4adc-8035-8e61d698fd66","originalName":null,"originalId":"00000000-0000-0000-0000-000000000000","isParameter":false,"isCalculated":false,"hasAggregatedFunction":false,"querySource":null,"querySourceName":null,"categoryName":null,"inaccessible":false,"originalAlias":null,"fullPath":null,"isCheck":false,"id":"458d97da-f01b-4dd7-ab0a-1adce478eac9","state":1,"deleted":false,"inserted":false,"version":null,"created":null,"createdBy":"John Doe","modified":"0001-01-01T00:00:00","modifiedBy":null},{"name":"RequiredDate","alias":"","dataType":"datetime","izendaDataType":"Datetime","allowDistinct":true,"visible":true,"filterable":true,"querySourceId":"322c3528-a582-4e0c-a5b7-eb7c39e8186a","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":1,"position":2,"extendedProperties":null,"physicalChange":0,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"isRunningField":false,"fullName":null,"calculatedTree":null,"reportId":"cb680f67-e363-4adc-8035-8e61d698fd66","originalName":null,"originalId":"00000000-0000-0000-0000-000000000000","isParameter":false,"isCalculated":false,"hasAggregatedFunction":false,"querySource":null,"querySourceName":null,"categoryName":null,"inaccessible":false,"originalAlias":null,"fullPath":null,"isCheck":false,"id":"42b46c10-0d11-45e3-a137-3f5a2b4bbcd7","state":1,"deleted":false,"inserted":false,"version":null,"created":null,"createdBy":"John Doe","modified":"0001-01-01T00:00:00","modifiedBy":null},{"name":"ShippedDate","alias":"","dataType":"datetime","izendaDataType":"Datetime","allowDistinct":true,"visible":true,"filterable":true,"querySourceId":"322c3528-a582-4e0c-a5b7-eb7c39e8186a","parentId":null,"expressionFields":[],"filteredValue":"","type":0,"groupPosition":1,"position":3,"extendedProperties":null,"physicalChange":0,"approval":0,"existed":false,"matchedTenant":false,"functionName":null,"expression":null,"isRunningField":false,"fullName":null,"calculatedTree":null,"reportId":"cb680f67-e363-4adc-8035-8e61d698fd66","originalName":null,"originalId":"00000000-0000-0000-0000-000000000000","isParameter":false,"isCalculated":false,"hasAggregatedFunction":false,"querySource":null,"querySourceName":null,"categoryName":null,"inaccessible":false,"originalAlias":null,"fullPath":null,"isCheck":false,"id":"9bc77976-9d15-43d6-a738-e74753ceb91b","state":1,"deleted":false,"inserted":false,"version":null,"created":null,"createdBy":"John Doe","modified":"0001-01-01T00:00:00","modifiedBy":null}],"name":"Example Report Name","reportDataSource":[{"reportId":"cb680f67-e363-4adc-8035-8e61d698fd66","querySourceId":"322c3528-a582-4e0c-a5b7-eb7c39e8186a","querySourceUniqueName":null,"querySourceCategoryId":null,"connectionId":null,"selected":true,"id":"1c2df382-de1d-48a2-9e54-0c5815963244","state":1,"deleted":false,"inserted":false,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"type":1,"previewRecord":10,"advancedMode":true,"allowNulls":false,"isDistinct":false,"categoryId":null,"categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":null,"tenantName":null,"description":null,"title":null,"lastViewed":null,"owner":"John Doe","ownerId":"9d2f1d51-0e3d-44db-bfc7-da94a7581bfe","excludedRelationships":null,"numberOfView":0,"renderingTime":0,"createdById":"9d2f1d51-0e3d-44db-bfc7-da94a7581bfe","modifiedById":"9d2f1d51-0e3d-44db-bfc7-da94a7581bfe","snapToGrid":false,"usingFields":null,"hasDeletedObjects":false,"header":null,"footer":null,"titleDescription":null,"sourceId":null,"checked":false,"copyDashboard":false,"exportFormatSetting":null,"deletable":false,"editable":false,"movable":false,"copyable":false,"accessPriority":0,"active":false,"fullPath":null,"computeNameSettings":null,"isGlobal":false,"isCheck":false,"id":"cb680f67-e363-4adc-8035-8e61d698fd66","state":1,"deleted":false,"inserted":false,"version":0,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":"John Doe"},"success":true,"messages":null,"data":null}
> ```

## POST report/loadAccesses

Returns a list of all accesses.

**Request**

> Payload: an [AccessPagedRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415504690199-AccessPagedRequest) object

**Response**

> A [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) object, with **result** field containing an array of [UserPermission](https://devnet.logianalytics.com/hc/en-us/articles/4415492896023-UserPermission) objects

**Samples**

> ```
> POST/api/report/loadAccessesHTTP/1.1
> ```
>
> Request Payload:
>
> > ```
> > {"reportId":"840ba6a8-dfe3-4d92-8341-63e56b95a038","accesses":[],"criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"shareWith","descending":true}]}
> > ```
>
> Successful response:
>
> ```
> {"result":[],"pageIndex":1,"pageSize":10,"total":0}
> ```

## POST report/loadSchedules

Returns a list of all scheduled deliveries.

**Request**

> Payload: an [SubscriptionPagedRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492887831-SubscriptionPagedRequest) object
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
> POST/api/report/loadSchedulesHTTP/1.1
> ```
>
> Request Payload:
>
> ```
> {"reportId":"17bbaf02-0b59-4224-93b3-41bb14da516f","subscriptions":[],"criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"name","descending":true}]}
> ```
>
> Successful response:
>
> ```
> {"result":[],"pageIndex":1,"pageSize":10,"total":0}
> ```

## GET report/reportPart/{report\_part\_id}/(report\_id)?page=value

Returns the report part definition specified by report\_part\_id from draft (using report\_id) or from database (without report\_id).

**Parameters**

> | Field | Description |
> | --- | --- |
> | **report\_part\_id**  string(GUID) | Id of the report part |
> | **report\_id**  string(GUID) | Id of the report |
> | **page** *Optional*  string(GUID) | Id of the web page. |

**Request**

> No payload

**Response**

> A [ReportPartDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415504773527-ReportPartDefinition) object.

**Samples**

> ```
> GET/api/report/reportPart/7391FEC3-53A1-411D-B92E-02C007FB4DD6HTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"reportPartContent":{"showDataInOneGroupNextTogether":false,"columns":{"text":null,"properties":{},"settings":{},"elements":[{"name":"ShipCountry","properties":{"isDirty":false,"fieldItemVisible":true,"dataFormattings":{"function":"","functionInfo":{},"format":{},"font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"","backgroundColor":""},"alignment":"alignLeft","sort":"","color":{"textColor":{"rangePercent":null,"rangeValue":null,"value":null},"cellColor":{"rangePercent":null,"rangeValue":null,"value":null}},"alternativeText":{"rangePercent":null,"rangeValue":null,"value":null},"customURL":{"url":"","option":"Open link in New Window"},"embeddedJavascript":{"script":""},"subTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""},"grandTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""}},"headerFormating":{"font":{"family":null,"size":null,"bold":null,"italic":null,"underline":null,"color":null,"backgroundColor":null},"alignment":null,"wordWrap":null,"columnGroup":""},"drillDown":{"subReport":{"selectedReport":null,"style":null,"reportPartUsed":null,"reportFilter":true,"mappingFields":[]}},"otherProps":{}},"settings":{},"chartType":null,"showTotal":false,"position":1,"field":{"fieldId":"d300a6bd-f218-46c8-a262-3b9fa5ee0382","originalName":null,"fieldName":"ShipCountry","fieldNameAlias":"ShipCountry","dataFieldType":"Text","querySourceId":"d609ecdc-2afc-43ce-a0a4-0583ed667c8f","querySourceType":"Table","sourceAlias":"Orders","relationshipId":"00000000-0000-0000-0000-000000000000","visible":true,"filterable":false,"reportId":null,"fieldFunctionExpression":"","expression":null,"grandTotalExpression":"","subTotalExpression":"","sort":"Unsorted","function":null,"calculatedTree":null,"grandTotalTree":null,"isCalculated":false}}]},"rows":{"text":null,"properties":{},"settings":{},"elements":[]},"values":{"text":null,"properties":{},"settings":{},"elements":[]},"separators":{"text":null,"properties":{},"settings":{},"elements":[{"name":"Group (Freight)","properties":{"isDirty":false,"fieldItemVisible":true,"dataFormattings":{"function":"7f942ac7-08d8-41fa-9e89-bad96f07f102","functionInfo":{"id":"7f942ac7-08d8-41fa-9e89-bad96f07f102","name":"Group","expression":null,"dataType":"Money","formatDataType":"Money","syntax":null,"expressionSyntax":null,"isOperator":false,"extendedProperties":{}},"format":{},"font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"","backgroundColor":""},"alignment":"alignLeft","sort":"","color":{"textColor":{"rangePercent":null,"rangeValue":null,"value":null},"cellColor":{"rangePercent":null,"rangeValue":null,"value":null}},"alternativeText":{"rangePercent":null,"rangeValue":null,"value":null},"customURL":{"url":"","option":"Open link in New Window"},"embeddedJavascript":{"script":""},"subTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""},"grandTotal":{"label":"","function":"","expression":"","dataType":"","previewResult":""}},"headerFormating":{"font":{"family":null,"size":null,"bold":null,"italic":null,"underline":null,"color":null,"backgroundColor":null},"alignment":null,"wordWrap":null,"columnGroup":""},"drillDown":{"subReport":{"selectedReport":null,"style":null,"reportPartUsed":null,"reportFilter":true,"mappingFields":[]}},"otherProps":{}},"settings":{},"chartType":null,"showTotal":false,"position":1,"field":{"fieldId":"fa47d01d-e055-43ad-b1ec-891b1685b9fe","originalName":null,"fieldName":"Freight","fieldNameAlias":"Group (Freight)","dataFieldType":"Money","querySourceId":"d609ecdc-2afc-43ce-a0a4-0583ed667c8f","querySourceType":"Table","sourceAlias":"Orders","relationshipId":"00000000-0000-0000-0000-000000000000","visible":true,"filterable":false,"reportId":null,"fieldFunctionExpression":"","expression":null,"grandTotalExpression":"","subTotalExpression":"","sort":"Unsorted","function":"Group","calculatedTree":null,"grandTotalTree":null,"isCalculated":false}}]},"type":3,"properties":{"isDirty":false,"generalInfo":{"gridStyle":"Vertical","separatorStyle":"Comma"},"table":{"border":{"top":{},"right":{},"bottom":{},"midVer":{},"left":{},"midHor":{}},"backgroundColor":"#efefef"},"columns":{"width":{"value":null,"unit":"Pixels"},"alterBackgroundColor":false},"rows":{"height":40,"alterBackgroundColor":false},"headers":{"font":{"family":"Roboto","size":14,"bold":true,"italic":false,"underline":false,"backgroundColor":"#dbf2ff"},"alignment":"left","wordWrap":false,"removeHeaderForExport":false},"grouping":{"useSeparator":true},"view":{"dataRefreshInterval":{"enable":false,"updateInterval":0,"isAll":true,"latestRecord":0},"usePagination":false},"printing":{"usePageBreakAfterSeparator":false}},"settings":{},"title":{"text":"","properties":{},"settings":{"font":{"family":"","size":14,"bold":true,"italic":false,"underline":false,"color":"","highlightColor":""},"alignment":{"alignment":""}},"elements":[]},"description":{"text":"","properties":{},"settings":{"font":{"family":"","size":14,"bold":false,"italic":false,"underline":false,"color":"","highlightColor":""},"alignment":{"alignment":""}},"elements":[]},"expandedLevel":-1},"title":"Grid","positionX":0,"positionY":0,"width":12,"height":4,"reportId":"055899a3-8886-4099-b360-fabf4656f5ce","numberOfRecord":0,"id":"7391fec3-53a1-411d-b92e-02c007fb4dd6","state":0,"inserted":true,"version":1,"created":"2016-08-29T09:17:05.13","createdBy":null,"modified":"2016-08-29T09:17:05.13","modifiedBy":null}
> ```

## POST report/validateExistingField

Validates that some fields exist in a report.

**Request**

> Payload: a [ReportValidation](https://devnet.logianalytics.com/hc/en-us/articles/4415512049303-ReportValidation) object.

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with the **data** field populated:
>
> * true: the fields exist

**Samples**

> ```
> POST/api/report/validateExistingFieldHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"reportName":"Test","categoryName":"JD","subCategoryName":null,"tenantId":null,"columnFullReference":["ProductID","UnitPrice"]}
> ```
>
> Successful response:
>
> ```
> {"success":true,"messages":null,"data":true}
> ```

## GET report/reportId/(tenant\_id)?reportName=value&categoryName=value

Returns report id from report name and category name.

**Request**

> No payload

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **data** field populated with the id of the report if found.

**Samples**

> ```
> GET/api/report/reportId?reportName=Test%20Report&categoryName=Category%201HTTP/1.1
> ```
>
> No payload
>
> Sample response:
>
> ```
> {"success":true,"data":"4e2d54c8-20e7-437f-a5ce-43e963c763a2"}
> ```

## POST report/validateExistingReport

Validates that a report exists in a category.

**Request**

> Payload: a [ReportValidation](https://devnet.logianalytics.com/hc/en-us/articles/4415512049303-ReportValidation) object.

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **data** field populated
>
> * true if the report exists
> * false if not

**Samples**

> ```
> POST/api/report/validateExistingReportHTTP/1.1
> ```
>
> Request Payload:
>
> ```
> {"tenantId":"de0c01f3-63ab-4f85-90ff-fe2f1d4fa00b","reportName":"TestReport","categoryName":"Category 1"}
> ```
>
> Successful response:
>
> ```
> {"success":true,"messages":null,"data":true}
> ```

## GET report/reportsByTenant/(tenant\_id)

Returns list of reports by tenant, with each report containing a list of report parts.

**Request**

> No payload

**Response**

> An array of [ReportPartDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415504773527-ReportPartDefinition) objects.

**Samples**

> ```
> GET/api/report/reportsByTenantHTTP/1.1
> ```
>
> Request:
>
> > No payload
>
> Sample response:
>
> ```
> [{"id":"b3279ee1-9188-484f-9255-31417b92f68e","name":"Test1","reportParts":[{"id":"1927af27-c7fb-42ef-9a8a-5bdbe810135f","title":"Grid","type":"Grid","width":0,"height":0}]},{"id":"c8bf2254-6377-47ae-aa7f-570ec19206de","name":"Test2","reportParts":[{"id":"6d832822-5e28-43f4-b6d8-30d635ac3f5b","title":"Grid","type":"Grid","width":4,"height":7}]}]
> ```

## POST report/updateRenderingTime

Updates the rendering time of a report.

**Request**

> Payload: a [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492852759-ReportDefinition) object.

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with the **success** field populated.

**Samples**

> ```
> POST/api/report/updateRenderingTimeHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"id":"9197f210-766a-45d3-a1f9-5c4f4a4aa8ba","renderingTime":451}
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null,"data":null}
> ```

## GET report/isReportValid/(report\_id)

Returns true if there is a report definition for the specified report\_id.

**Request**

> No payload

**Response**

> * true if there is a report definition for the specified report\_id
> * false if report\_id is null or there is no report definition

**Samples**

> ```
> GET/api/report/isReportValid/3501e30d-6ded-4f26-9922-011633ace5abHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":[],"data":null}
> ```

## POST report/areReportsValid

Validates if reports are valid.

**Request**

> Payload: an array of report ids (GUIDs).

**Response**

> An array of [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) objects, with **success** field true if that report is valid.

**Samples**

> ```
> POST/api/report/updateRenderingTimeHTTP/1.1
> ```
>
> Request payload:
>
> ```
> ["c8bf2254-6377-47ae-aa7f-570ec19206de","1927af27-6377-2539-aa7f-570ec19206de]
> ```
>
> Sample response:
>
> ```
> [{"success":true,"messages":[],"data":null},{"success":true,"messages":[],"data":null}]
> ```

## POST report/printDraft

Saves report as draft for printing.

**Request**

> Payload: a [ReportSavingParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415512047639-ReportSavingParameter) object.

**Response**

> The id of the report in draft.

**Samples**

> ```
> POST/api/report/printDraftHTTP/1.1
> ```
>
> Response:
>
> ```
> {"id":"5a35257c-4c64-401c-b15f-f9f5681ccdc8"}
> ```

## GET report/printDraft/{report\_id}

Gets report as draft for printing.

**Request**

> No payload

**Response**

> A [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492852759-ReportDefinition) object.

**Samples**

> ```
> GET/api/report/printDraft/5a35257c-4c64-401c-b15f-f9f5681ccdc8HTTP/1.1
> ```

## GET report/accessPriority/(report\_dashboard\_id)

Returns access priority for report/dashboard.

**Request**

> No payload

**Response**

> The access priority

**Samples**

> ```
> GET/api/report/accessPriority/e09f9d45-b721-4012-b8e7-c31c58d52af3HTTP/1.1
> ```
>
> Response:
>
> ```
> 1
> ```

## GET report/reportPart/crossfiltering/{report\_part\_id}

Returns a list of ids of cross-filtering report parts in the same report as the specified report part, including itself.

New in version 2.0.6.

**Request**

> No payload

**Response**

> An array of strings (GUIDs)

**Samples**

> ```
> GET/api/report/reportPart/crossfiltering/04192bb1-7138-4e45-8fd4-506793a29704HTTP/1.1
> ```
>
> Response:
>
> ```
> ["04192bb1-7138-4e45-8fd4-506793a29704","edaf3f13-7ff8-4d0f-a99b-56396080155a"]
> ```

## GET report/validateEmbeddedReport/(tenant\_id)?reportId=value&reportName=value&reportPartName=value

Validates that logged in user can access one and only one report part from the specified reportName and reportPartName.

New in version 2.2.2.

**Request**

> | Parameter | Required | Description |
> | --- | --- | --- |
> | **reportId**  string (GUID) | O | The id of the embedded report.   If not available, all reports containing the specified reportPartName will be checked. |
> | **reportName**  string | R | The name of the embedded report. |
> | **reportPartName**  string | R | The name of the embedded report part. |

**Response**

> | Field | Description |
> | --- | --- |
> | **reportId**  string (GUID) | The id of the unique report |
> | **reportPartId**  string (GUID) | The id of the unique report part |

**Samples**

> ```
> GET/api/report/validateEmbeddedReport/b5b3a5cc-9e55-424c-ae85-ba92ec3b934e?reportId=b8822cba-53f1-4f83-b6a2-1f45557fe62e&reportName=092917-chart&reportPartName=ChartHTTP/1.1
> ```
>
> Response:
>
> ```
> {"reportId":"b8822cba-53f1-4f83-b6a2-1f45557fe62e","reportPartId":"faa882ed-5c20-4faa-861c-03adb8a23edd"}
> ```

## POST report/findBySourceIds

Returns a list of report definitions based on the provided report source Ids

**Request**

> Payload: a list of report source Ids

**Response**

> A list of [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492852759-ReportDefinition) objects.

**Samples**

> ```
> POST/api/report/findBySourceIdsHTTP/1.1
> ```
>
> Request Payload:
>
> ```
> ['89B6301D-2068-4720-B89B-3F716DF2076F','E67CE38D-61E5-4F97-BA2C-F9AA4855959D']
> ```

## POST report/findReportPartsBySourceIds

Returns a list of report parts based on the provided report part source Ids

**Request**

> Payload: a list of report part source Ids

**Response**

> A list of [ReportPartDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415504773527-ReportPartDefinition) objects.

**Samples**

> ```
> POST/api/report/findReportPartsBySourceIdsHTTP/1.1
> ```
>
> Request Payload:
>
> ```
> ['89B6301D-2068-4720-B89B-3F716DF2076F','E67CE38D-61E5-4F97-BA2C-F9AA4855959D']
> ```
