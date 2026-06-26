---
title: "Misc System Settings APIs"
id: 4415511950871
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415511950871-Misc-System-Settings-APIs
updated_at: 2021-12-10T03:08:10Z
---

# Misc System Settings APIs

# Misc System Settings APIs

## Summary

| API | Purpose | Usage in Izenda Front-end |
| --- | --- | --- |
| [GET accessRight/reportDashboard/{type}](#get-accessright-reportdashboard-type) | Returns access right for report/template (type=0) or dashboard (type=1). |  |
| [GET accessRight/authentication/{type}](#get-accessright-authentication-type) | Returns access right for authentication setup for report/template (type=0) or dashboard (type=1). |  |
| [POST accessRight/load](#post-accessright-load) | Searches for access rights. |  |
| [POST accessRight/validate](#post-accessright-validate) | Validates an array of user permissions. |  |
| [POST authorization/checkPermissions](#post-authorization-checkpermissions) | Returns an array of permissions with boolean values depending on permissions of current user. |  |
| [GET authorization/permission/(section)](#get-authorization-permission-section) | Returns an array of permissions for current user. |  |
| [GET accessRight/loadAccessDefaults/{reportingType}](#get-accessright-loadaccessdefaults-reportingtype) | Returns an array of access defaults for report (reportingType=1), dashboard (reportingType=2), or both (reportingType=0). |  |
| [GET systemSetting/status](#get-systemsetting-status) | Returns system time, for system alive check. |  |
| [GET systemSetting/reset](#get-systemsetting-reset) | Resets system settings. |  |
| [GET systemSetting/systemVariables](#get-systemsetting-systemvariables) | Returns an array of system variable names. |  |
| [GET systemSetting/supportedDataSourceTypes](#get-systemsetting-supporteddatasourcetypes) | Returns an array of supported data source types. |  |
| [POST systemSetting/loadEmailVariables](#post-systemsetting-loademailvariables) | Returns an array of supported email variables. |  |
| GET systemSetting/securityQuestions | Returns an array of security questions.  Obsolete |  |
| [POST systemSetting/securityQuestions](#post-systemsetting-securityquestions) | Saves a new security question.  New in version 2.15.1. |  |
| PUT systemSetting/securityQuestions | Updates an existing security question.  Obsolete |  |
| DELETE systemSetting/securityQuestions/{security\_question\_id} | Deletes a security question.  Obsolete |  |
| GET systemSetting/securityQuestions/{user\_name}/(tenant\_display\_id) | Returns security question for a user and tenant display id.  Obsolete from version 2.15.1. Replace by the [POST systemSetting/securityQuestions](#post-systemsetting-securityquestions) |  |
| [GET systemSetting/email/(tenant\_id)](#get-systemsetting-email-tenant-id) | Returns email setting. |  |
| [POST systemSetting/email](#post-systemsetting-email) | Saves email setting. |  |
| [GET systemSetting/email/status/(tenant\_id)](#get-systemsetting-email-status-tenant-id) | Returns email setting status. |  |
| [GET systemSetting/language](#get-systemsetting-language) | Returns all supported languages. |  |
| [GET systemSetting/dateFormat](#get-systemsetting-dateformat) | Returns all supported date formats. |  |
| [GET systemSetting/googleAPIKey/(tenantId)](#get-systemsetting-googleapikey-tenantid)  New in version 3.5.0. | Returns the Google Map API Key for specific tenant. |  |
| [POST systemSetting/googleAPIKey](#post-systemsetting-googleapikey)  New in version 3.5.0. | Save Google Map settings. |  |

## GET accessRight/reportDashboard/{type}

Returns access right for report/template (type=0) or dashboard (type=1).

**Request**

> No payload

**Response**

> An array of [AccessRight](https://devnet.logianalytics.com/hc/en-us/articles/4415504691095-AccessRight) objects

**Samples**

> ```
> GET/api/accessRight/reportDashboard/0HTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"name":"Full Access","type":0,"id":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d010","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"name":"Locked","type":0,"id":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d003","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"name":"No Access","type":0,"id":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d005","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"name":"Quick Edit","type":0,"id":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d001","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"name":"Save As","type":0,"id":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d002","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"name":"View Only","type":0,"id":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d004","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}]
> ```

## GET accessRight/authentication/{type}

Returns access right for authentication setup for report/template (type=0) or dashboard (type=1).

**Request**

> No payload

**Response**

> An array of [AccessRight](https://devnet.logianalytics.com/hc/en-us/articles/4415504691095-AccessRight) objects

**Samples**

> ```
> GET/api/accessRight/authentication/1HTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"name":"Locked","type":1,"id":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d007","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"name":"No Access","type":1,"id":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d009","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"name":"Save As","type":1,"id":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d006","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"name":"View Only","type":1,"id":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d008","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}]
> ```

## POST accessRight/load

Searches for access rights.

**Request**

> Payload: an [AccessPagedRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415504690199-AccessPagedRequest) object

**Response**

> A [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) object with **result** field containing an array of [UserPermission](https://devnet.logianalytics.com/hc/en-us/articles/4415492896023-UserPermission) objects

**Samples**

> ```
> POST/api/accessRight/loadHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"dashboardId":"89dca314-f66f-489d-a14c-117aa3ec875d","criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"shareWith","descending":true}]}
> ```
>
> Sample response:
>
> ```
> {"result":[{"reportId":null,"dashboardId":"89dca314-f66f-489d-a14c-117aa3ec875d","assignedType":2,"accessRightId":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d006","accessRight":"Save As","shareWith":"Role ReportCreator","position":0,"accessors":["d8a30ef0-41b4-4c97-9b7a-9fcbe90db880"],"tempId":null,"reportAccessRightId":null,"reportAccessRights":"","dashboardAccessRightId":null,"dashboardAccessRights":"","id":"879472bc-3c7a-4f9c-a090-ea7882019885","state":0,"deleted":false,"inserted":true,"version":1,"created":"2016-10-18T07:24:56.887","createdBy":null,"modified":"2016-10-18T07:24:56.887","modifiedBy":null},{"reportId":null,"dashboardId":"89dca314-f66f-489d-a14c-117aa3ec875d","assignedType":1,"accessRightId":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d008","accessRight":"View Only","shareWith":"Everyone","position":0,"accessors":[],"tempId":null,"reportAccessRightId":null,"reportAccessRights":"","dashboardAccessRightId":null,"dashboardAccessRights":"","id":"193c7f1b-5fcd-40ee-be09-0d7b96736115","state":0,"deleted":false,"inserted":true,"version":1,"created":"2016-10-18T07:24:41.387","createdBy":null,"modified":"2016-10-18T07:24:41.387","modifiedBy":null}],"pageIndex":1,"pageSize":10,"total":2}
> ```

## POST accessRight/validate

Validates an array of user permissions.

**Request**

> Payload: an array of [UserPermission](https://devnet.logianalytics.com/hc/en-us/articles/4415492896023-UserPermission) objects

**Response**

> * true if valid
> * false if not

**Samples**

> ```
> POST/api/accessRight/validateHTTP/1.1
> ```
>
> Request payload:
>
> ```
> [{"reportId":null,"dashboardId":"89dca314-f66f-489d-a14c-117aa3ec875d","assignedType":2,"accessRightId":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d006","accessRight":"Save As","shareWith":"Role ReportCreator","position":0,"accessors":["d8a30ef0-41b4-4c97-9b7a-9fcbe90db880"],"tempId":null,"reportAccessRightId":null,"reportAccessRights":"","dashboardAccessRightId":null,"dashboardAccessRights":"","id":"879472bc-3c7a-4f9c-a090-ea7882019885","state":0,"deleted":false,"inserted":true,"version":1,"created":"2016-10-18T07:24:56.887","createdBy":null,"modified":"2016-10-18T07:24:56.887","modifiedBy":null},{"reportId":null,"dashboardId":"89dca314-f66f-489d-a14c-117aa3ec875d","assignedType":1,"accessRightId":"13698ebf-3e8e-43e1-9e2b-ad3f17d7d008","accessRight":"View Only","shareWith":"Everyone","position":0,"accessors":[],"tempId":null,"reportAccessRightId":null,"reportAccessRights":"","dashboardAccessRightId":null,"dashboardAccessRights":"","id":"193c7f1b-5fcd-40ee-be09-0d7b96736115","state":0,"deleted":false,"inserted":true,"version":1,"created":"2016-10-18T07:24:41.387","createdBy":null,"modified":"2016-10-18T07:24:41.387","modifiedBy":null}]
> ```
>
> Sample response:
>
> ```
> true
> ```

## POST authorization/checkPermissions

Returns an array of permissions with boolean values depending on permissions of current user.

**Request**

> Payload: an array of permissions (strings)

**Response**

> A dynamic object with permission names as fields, and boolean values to specify if current user has this permission or not.

**Samples**

> ```
> POST/api/authorization/checkPermissionsHTTP/1.1
> ```
>
> Request payload:
>
> ```
> ["reports","dashboards","scheduling"]
> ```
>
> Sample response:
>
> ```
> Tobeupdated
> ```

## GET authorization/permission/(section)

Returns an array of permissions for current user.

**Request**

> No payload
>
> Possible **section** values:
>
> |  |  |  |
> | --- | --- | --- |
> | * systemconfiguration * datasetup * usersetup * rolesetup | * reports * dashboards * access * scheduling | * emailing * exporting * systemwide |

**Response**

> A dynamic object, either the full [Permission](https://devnet.logianalytics.com/hc/en-us/articles/4415492827287-Permission) object or a section of it depending on the section parameter.

**Samples**

> ```
> GET/api/authorization/permissionHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"fullReportAndDashboardAccess":false,"systemConfiguration":{"scheduledInstances":{"value":false,"tenantAccess":0},"tenantAccess":0},"dataSetup":{"dataModel":{"value":false,"tenantAccess":0},"advancedSettings":{"category":false,"others":false,"tenantAccess":0},"tenantAccess":0},"userSetup":{"userRoleAssociation":{"value":false,"tenantAccess":0},"actions":{"create":false,"edit":false,"del":false,"configureSecurityOptions":false,"tenantAccess":0},"tenantAccess":0},"roleSetup":{"actions":{"create":false,"edit":false,"del":false,"tenantAccess":0},"dataModelAccess":{"value":false,"tenantAccess":0},"permissions":{"value":false,"tenantAccess":0},"grantRoleWithFullReportAndDashboardAccess":{"value":false,"tenantAccess":0},"tenantAccess":0},"reports":{"canCreateNewReport":{"value":false,"tenantAccess":0},"dataSources":{"simpleDataSources":false,"advancedDataSources":false,"tenantAccess":0},"reportPartTypes":{"chart":false,"form":false,"gauge":false,"map":false,"tenantAccess":0},"reportCategoriesSubcategories":{"canCreateNewCategory":{"value":false,"tenantAccess":0},"categoryAccessibility":{"categories":[],"tenantAccess":0}},"filterProperties":{"filterLogic":false,"tenantAccess":0},"fieldProperties":{"customURL":false,"embeddedJavaScript":false,"subreport":false,"tenantAccess":0},"actions":{"schedule":false,"email":false,"viewReportHistory":false,"del":false,"registerForAlerts":false,"print":false,"unarchiveReportVersions":false,"overwriteExistingReport":false,"subscribe":false,"exporting":false,"configureAccessRights":false,"tenantAccess":0},"tenantAccess":0},"dashboards":{"canCreateNewDashboard":{"value":false,"tenantAccess":0},"dashboardCategoriesSubcategories":{"canCreateNewCategory":{"value":false,"tenantAccess":0},"categoryAccessibility":{"categories":[],"tenantAccess":0}},"actions":{"schedule":false,"email":false,"del":false,"subscribe":false,"print":false,"overwriteExistingDashboard":false,"configureAccessRights":false,"tenantAccess":0},"tenantAccess":0},"access":{"accessLimits":{"value":[],"tenantAccess":0},"accessDefaults":{"value":[],"tenantAccess":0},"tenantAccess":0},"scheduling":{"schedulingLimits":{"value":[],"tenantAccess":0},"schedulingScope":{"systemUsers":false,"externalUsers":false,"tenantAccess":0},"tenantAccess":0},"emailing":{"deliveryMethod":{"link":false,"embeddedHTML":false,"attachment":false,"tenantAccess":0},"attachmentType":{"word":false,"excel":false,"pdf":false,"csv":false,"xml":false,"json":false,"tenantAccess":0},"tenantAccess":0},"exporting":{"exportingFormat":{"word":false,"excel":false,"pdf":false,"csv":false,"xml":false,"json":false,"queryExecution":false,"tenantAccess":0},"tenantAccess":0},"systemwide":{"canSeeSystemMessages":{"value":false,"tenantAccess":0},"tenantAccess":0}}
> ```

## GET accessRight/loadAccessDefaults/{reportingType}

Returns an array of access defaults for report (reportingType=1), dashboard (reportingType=2), or both (reportingType=0).

**Request**

> No payload

**Response**

> An array of [UserPermission](https://devnet.logianalytics.com/hc/en-us/articles/4415492896023-UserPermission) objects

**Samples**

> ```
> GET/api/accessRight/loadAccessDefaults/0HTTP/1.1
> ```
>
> Sample response:
>
> ```
> Tobeupdated
> ```

## GET systemSetting/status

Returns system time, for system alive check.

**Request**

> No payload

**Response**

> The current date time if system is alive

**Samples**

> ```
> GET/api/systemSetting/statusHTTP/1.1
> ```
>
> Sample response:
>
> ```
> "2016-12-05T03:24:09.5807888Z"
> ```

## GET systemSetting/reset

Resets system settings.

**Request**

> No payload

**Response**

> The string “Done” if successful

**Samples**

> ```
> GET/api/systemSetting/resetHTTP/1.1
> ```
>
> Sample response:
>
> ```
> "Done"
> ```

## GET systemSetting/systemVariables

Returns an array of system variable names.

**Request**

> No payload

**Response**

> An array of strings, which are system variable names

**Samples**

> ```
> GET/api/systemSetting/systemVariablesHTTP/1.1
> ```
>
> Sample response:
>
> ```
> ["@Tenant ID","@User ID","@Role ID"]
> ```

## GET systemSetting/supportedDataSourceTypes

Returns an array of supported data source types.

**Request**

> No payload

**Response**

> A list [Item](https://devnet.logianalytics.com/hc/en-us/articles/4415504733207-Item) objects.

**Samples**

> ```
> GET/api/systemSetting/supportedDataSourceTypesHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"key":"Table","value":"Table","originalValue":null,"dataFormat":null,"intimePeriodType":null,"valueInTimePeriod":0,"function":null},{"key":"View","value":"View","originalValue":null,"dataFormat":null,"intimePeriodType":null,"valueInTimePeriod":0,"function":null}]
> ```

## POST systemSetting/loadEmailVariables

Returns an array of supported email variables.

**Request**

> Payload: a [SystemVariablePagedRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415504798615-SystemVariablePagedRequest) object
>
> Note
>
> The keys for [SearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415512052759-SearchCriteria) that this API support:   
> - All   
> - Name   
> - DataType

**Response**

> A [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) object with **result** field containing an array of [SystemVariable](https://devnet.logianalytics.com/hc/en-us/articles/4415504797719-SystemVariable) objects

**Samples**

> ```
> POST/api/systemSetting/loadEmailVariablesHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"reportingType":0,"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"name","descending":true}],"criteria":[]}
> ```
>
> Sample response:
>
> ```
> {"result":[{"id":"5cd4d4be-96d9-4c30-8680-04bd602bccd7","name":"{reportName}","dataType":"Text","description":"","scope":0},{"id":"b22170b0-48a6-45fa-8254-04be7843b9f9","name":"{currentDateTime}","dataType":"Text","description":"","scope":0},{"id":"18a820bf-9c48-465d-83ef-05511ab491cf","name":"{currentUserName}","dataType":"Text","description":"","scope":0},{"id":"e3dcd547-d9ac-417d-b42e-056358bf508c","name":"{tenantName}","dataType":"Text","description":"","scope":0},{"id":"0645098c-cb7c-4da5-aa98-059eb8fbdc16","name":"{reportLink}","dataType":"Text","description":"","scope":2},{"id":"6e204246-c212-4115-805b-0628d89c8ce2","name":"{embedReportHTML}","dataType":"Lob","description":"","scope":2},{"id":"673ad95a-7cc3-4a7e-b3d0-0643913359de","name":"{recipientName}","dataType":"Text","description":"","scope":1}],"pageIndex":0,"pageSize":1000,"total":7}
> ```

## POST systemSetting/securityQuestions

Returns security question for a user and tenant display id.

**Request**

> > The object with the following properties:
>
> | Field | Description | Notes |
> | --- | --- | --- |
> | **userName**  string | The username of the user requesting security questions |  |
> | **tenantDisplayID**  string | The tenant display id which user belongs to |  |

**Response**

> An array of [SecurityQuestion](https://devnet.logianalytics.com/hc/en-us/articles/4415512054551-SecurityQuestion) objects

**Samples**

> ```
> POST/api/systemSetting/securityQuestionsHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"userName":"employee@deldg.com","tenantDisplayID":"DELDG"}
> ```
>
> Sample response:
>
> ```
> [{"tenantId":null,"question":"What is the first and last name of your first boyfriend or girlfriend?","orderNumber":1,"id":"5784ece5-d2e7-42b1-89bb-859737b7b2a9","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"Which phone number do you remember most from your childhood?","orderNumber":2,"id":"3771bdc2-1add-481a-9649-18a7e494860b","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"What was your favorite place to visit as a child?","orderNumber":3,"id":"1704f7c3-0911-40cc-88c5-3c496613f96a","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"Who is your favorite actor, musician, or artist?","orderNumber":4,"id":"c054397d-e371-4694-ad71-162174f39b2f","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"What is the name of your first pet?","orderNumber":5,"id":"bf8e6807-6dbf-48a7-a5d9-121a46014d41","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"In what city were you born?","orderNumber":6,"id":"036e00b9-09e9-411a-9b9b-74f90f9a1289","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"What high school did you attend?","orderNumber":7,"id":"732fc020-8ac2-40ae-9d22-00d36f034552","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"What is the name of your first school?","orderNumber":8,"id":"89eed492-d117-4c42-a4b2-ab88cfb109df","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"What is your favorite movie?","orderNumber":9,"id":"2042a60d-1894-49e7-a194-77c24917f2c1","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"What is your mother’s maiden name?","orderNumber":10,"id":"470bae4e-0cb4-443d-9d75-ca91fdd81ce8","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"What street did you grow up on?","orderNumber":11,"id":"c57e2ec2-4114-43c4-99fe-80ef9e0b8c11","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"What was the make of your first car?","orderNumber":12,"id":"fd247bfd-3269-4425-a9a9-1239901611b7","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"When is your anniversary?","orderNumber":13,"id":"087a3c5b-ebff-4f96-ba7d-ffede847e09c","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"What is your favorite color?","orderNumber":14,"id":"a8201224-ddd8-4fc1-9573-82e754eb5ce1","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"What is your father’s middle name?","orderNumber":15,"id":"e30524f4-5799-4fcd-ac86-9098571303a6","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"What is the name of your first grade teacher?","orderNumber":16,"id":"c48320ec-763f-48be-a689-8840f26cb5d6","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"tenantId":null,"question":"What was your high school mascot?","orderNumber":17,"id":"20cfa68c-5398-46cf-acf8-b1c2bff297c5","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}]
> ```

## GET systemSetting/email/(tenant\_id)

Returns email setting.

**Request**

> No payload

**Response**

> An [EmailSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415492808215-EmailSetting) object

**Samples**

> ```
> GET/api/systemSetting/emailHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"displayName":null,"emailFromAddress":"contact@izenda.com","useSystemConfiguration":false,"server":"localhost","port":25,"secureConnection":false,"login":"mail","password":"EW+9H/VRg8TH0sWNiPuwpg==","tenantId":null,"id":"1262295f-2b44-4fa2-9446-cda5e029a15c","state":0,"deleted":false,"inserted":true,"version":1,"created":"2017-01-05T04:58:20.6430000+07:00","createdBy":"John Doe","modified":"2017-01-05T04:58:20.6430000+07:00","modifiedBy":"John Doe"}
> ```

## POST systemSetting/email

Saves email setting.

**Request**

> Payload: an [EmailSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415492808215-EmailSetting) object

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **success**  boolean | Should be true |  |
> | **emailSetting**  string | The saved [EmailSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415492808215-EmailSetting) object |  |

**Samples**

> ```
> POST/api/systemSetting/emailHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"isDirty":true,"id":"1262295f-2b44-4fa2-9446-cda5e029a15c","tenantId":null,"server":"localhost","port":25,"secureConnection":false,"login":"mail","password":"EW+9H/VRg8TH0sWNiPuwpg==","displayName":null,"emailFromAddress":"contact@izenda.com","version":1,"created":null,"createdBy":null,"modified":"2017-01-05T04:58:20.6430000+07:00","modifiedBy":"John Doe"}
> ```
>
> Sample response:
>
> ```
> {"success":true,"emailSetting":{"displayName":null,"emailFromAddress":"contact@izenda.com","useSystemConfiguration":false,"server":"localhost","port":25,"secureConnection":false,"login":"mail","password":"EW+9H/VRg8TH0sWNiPuwpg==","tenantId":null,"id":"1262295f-2b44-4fa2-9446-cda5e029a15c","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":"John Doe","modified":"2017-01-06T06:27:51.0508642","modifiedBy":"John Doe"}}
> ```

## GET systemSetting/email/status/(tenant\_id)

Returns email setting status.

**Request**

> No payload

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **success**  boolean | Whether the email settings exist |  |
> | **message**  string | The error message if **success** is false |  |

**Samples**

> ```
> GET/api/systemSetting/email/statusHTTP/1.1
> ```
>
> Sample response:
>
> ```
> true
> ```

## GET systemSetting/language

Returns all supported languages.

**Request**

> No payload

**Response**

> An array of [IzendaLanguage](https://devnet.logianalytics.com/hc/en-us/articles/4415492820503-IzendaLanguage) objects

**Samples**

> ```
> GET/api/systemSetting/languageHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"language":"English - United States","cultureName":"en-US","id":"c6e7d7b5-4e15-44b7-9538-fd1ab38783f0","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"language":"French - Canada","cultureName":"fr-CA","id":"de80459f-cd0a-4443-93c4-a3f87eb0a78f","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null},{"language":"Arabic","cultureName":"ar","id":"15f7bd94-ae10-4fd7-91ed-cae10da3bd9d","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}]
> ```

## GET systemSetting/dateFormat

Returns all supported date formats.

**Request**

> No payload

**Response**

> An array of strings (date formats)

**Samples**

> ```
> GET/api/systemSetting/dateFormatHTTP/1.1
> ```
>
> Sample response:
>
> ```
> ["MM/DD/YYYY","DD/MM/YYYY","YYYY/MM/DD"]
> ```

## GET systemSetting/googleAPIKey/(tenantId)

Returns the Google Map API Key for specific tenant (return System’s key if tenantID is null.

**Request**

> No payload

**Response**

> An [GoogleAPISetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504731799-GoogleAPISetting) object

**Samples**

> ```
> GET/api/systemSetting/googleAPIKeyHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"useSystemConfiguration":false,"googleAPIKey":"The google api key","useGEOCodingService":true,"tenantId":null,"id":"e7798b61-3192-42dc-b0cd-7f7726cbfa69","state":0,"deleted":false,"inserted":true,"version":1,"created":"2019-09-03T07:45:33.0134920+07:00","createdBy":"System Admin","modified":"2019-09-03T07:45:33.0134920+07:00","modifiedBy":"System Admin"}
> ```

## POST systemSetting/googleAPIKey

Save Google Map settings.

**Request**

> An [GoogleAPISetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504731799-GoogleAPISetting) object

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **success**  boolean | Should be true |  |
> | **emailSetting**  string | The saved [GoogleAPISetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504731799-GoogleAPISetting) object |  |

**Samples**

> ```
> POST/api/systemSetting/googleAPIKeyHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"useSystemConfiguration":true,"googleAPIKey":null,"tenantId":"e2b50a50-8f5a-4e55-bbac-72e9e0334be9","id":"00000000-0000-0000-0000-000000000000"}
> ```
>
> Sample response:
>
> ```
> {"success":true,"googleAPIKeySetting":{"useSystemConfiguration":false,"googleAPIKey":"123","tenantId":"e2b50a50-8f5a-4e55-bbac-72e9e0334be9","id":"f060e458-e3f6-462d-a199-838f407b9193","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"System Admin","modified":"2019-08-08T14:31:13.704129","modifiedBy":"System Admin"}}
> ```
