---
title: "DashboardDefinition"
id: 4415492783767
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition
updated_at: 2021-12-10T03:08:30Z
---

# DashboardDefinition

# DashboardDefinition

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **commonFilterFields**  array of objects |  | An array of [CommonFilterField](https://devnet.logianalytics.com/hc/en-us/articles/4415504698647-CommonFilterField) objects |  |
| **accesses**  array of objects |  | An array of [UserPermission](https://devnet.logianalytics.com/hc/en-us/articles/4415492896023-UserPermission) objects |  |
| **subscriptions**  array of objects |  | An array of [Subscription](https://devnet.logianalytics.com/hc/en-us/articles/4415512058519-Subscription) objects |  |
| **inaccessible**  boolean |  | True if dashboard is inaccessible for user |  |

Inherited fields:

## Dashboard

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **name**  string |  | The name of the dashboard |  |
| **description**  string |  | The description of the dashboard |  |
| **categoryId**  string (GUID) | Y | The id of the dashboard category |  |
| **categoryName**  string |  | The name of the dashboard category |  |
| **subCategoryId**  string (GUID) | Y | The id of the dashboard sub-category |  |
| **subCategoryName**  string |  | The name of the dashboard sub-category |  |
| **tenantId**  string (GUID) | Y | The id of the tenant if available |  |
| **imageUrl**  string |  | The url of the image |  |
| **stretchImage**  boolean |  | Is the image stretched |  |
| **backgroundColor**  string |  | The background color |  |
| **showFilterDescription**  boolean |  | Whether to show filter descriptions |  |
| **lastViewed**  datetime | Y | The last viewed date time |  |
| **owner**  string |  | The owner name |  |
| **ownerId**  string (GUID) | Y | The id of the owner |  |
| **createdById**  string (GUID) | Y | Id of user who created this dashboard |  |
| **modifiedById**  string (GUID) | Y | Id of user who last modified this dashboard |  |
| **checked**  boolean |  | Is selected for copy in Copy Management |  |
| **numberOfView**  integer |  | The number of view |  |
| **renderingTime**  real number |  | The rendering time |  |
| **sourceId**  string (GUID) | Y | The id of the source dashboard in case this dashboard has been copied |  |
| **isGlobal**  boolean |  | Whether this is global dashboard |  |
| **deletable**  boolean |  | Is deletable |  |
| **editable**  boolean |  | Is editable |  |
| **movable**  boolean |  | Is movable |  |
| **copyable**  boolean |  | Is copyable |  |
| **accessPriority**  integer |  | The access priority |  |
| **dashboardParts**  array of objects |  | An array of [DashboardPart](https://devnet.logianalytics.com/hc/en-us/articles/4415504704023-DashboardPart) objects |  |
| **indeterminate**  boolean |  | Place-holder, returns false |  |
| **isCheck**  boolean |  | Whether this is selected |  |
| **displayDashboardTileHeader**  boolean  New in version 3.1.0. |  | Whether display dashboard tile or not |  |

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
{"commonFilterFields":[],"accesses":[],"subscriptions":[],"dashboardParts":[{"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","type":null,"title":null,"reportId":null,"reportPartId":null,"filterDescription":null,"numberOfRecord":-1,"positionX":0,"positionY":4,"width":6,"height":4,"filters":[],"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"id":"6b8a0f81-b0ba-4320-bd84-0cd6f61b2842","state":0,"inserted":true,"version":1,"created":"2016-08-11T03:20:08.793","createdBy":null,"modified":"2016-08-11T03:20:08.793","modifiedBy":null},{"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","type":"text","title":"text","reportId":null,"reportPartId":null,"filterDescription":null,"numberOfRecord":-1,"positionX":0,"positionY":0,"width":12,"height":4,"filters":[],"dashboardPartContent":{"contentTitle":{"text":"A Title","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"desc","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"id":"0cd06216-ee6f-4dee-9a8a-23d12f845e34","state":0,"inserted":true,"version":1,"created":"2016-08-11T03:20:08.777","createdBy":null,"modified":"2016-08-11T03:20:08.777","modifiedBy":null},{"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","type":null,"title":null,"reportId":null,"reportPartId":null,"filterDescription":null,"numberOfRecord":-1,"positionX":6,"positionY":4,"width":6,"height":4,"filters":[],"dashboardPartContent":{"contentTitle":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentDescription":{"text":"","settings":{"fontFamily":"","fontSize":14,"fontBold":true,"fontItalic":false,"fontUnderline":false,"fontColor":"","fontHighlightColor":"","alignment":""}},"contentFromPreset":true,"bodyContent":{"text":"","config":{"fontFamily":"Roboto","fontSize":14,"bold":false,"italic":false,"underline":false,"strikethrough":false,"textColor":"","backgroundColor":"","alignleft":false,"aligncenter":false,"alignright":false,"alignjustify":false,"bullet":"","numbered":"","alignTop":false,"alignMiddle":false,"alignBottom":false}}},"id":"042035e9-77e7-4102-baa7-e37eb5ed00d5","state":0,"inserted":true,"version":1,"created":"2016-08-11T03:20:08.793","createdBy":null,"modified":"2016-08-11T03:20:08.793","modifiedBy":null}],"name":"TestDashboard01","description":null,"categoryId":"e443f282-eba4-422d-a7c3-32560a268373","categoryName":null,"subCategoryId":null,"subCategoryName":null,"tenantId":null,"imageUrl":null,"stretchImage":false,"backgroundColor":null,"showFilterDescription":true,"lastViewed":null,"id":"a496ad94-fe92-48d5-a285-e45be738921f","state":0,"inserted":true,"version":2,"created":"2016-08-11T03:20:08.777","createdBy":null,"modified":"2016-08-11T03:44:01.27","modifiedBy":null}
```
