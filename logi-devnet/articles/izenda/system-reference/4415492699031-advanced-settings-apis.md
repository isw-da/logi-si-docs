---
title: "Advanced Settings APIs"
id: 4415492699031
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492699031-Advanced-Settings-APIs
updated_at: 2021-12-10T03:08:06Z
---

# Advanced Settings APIs

# Advanced Settings APIs

The **Advanced Settings** page allows users to manage the list of data source categories and update system settings in related groups.

## Summary

| API | Purpose | Usage in Izenda Front-end |
| --- | --- | --- |
| [POST advancedSetting/category](#id1) | Updates the list of [categories](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-data-source-category). | Settings > Data Setup > Advanced Settings > Category > Save |
| [GET advancedSetting/category/(tenant\_id)](#id2) | Returns an array of [categories](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-data-source-category) (filtered by tenant\_id if provided). | Settings > Data Setup > Advanced Settings > Category |
| [DELETE advancedSetting/category/{category\_id}](#id3) | Deletes the [category](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-data-source-category) specified by category\_id. | Settings > Data Setup > Advanced Settings > Category > click Remove icon |
| [GET advancedSetting/performance/(tenant\_id)](#get-advancedsetting-performance-tenant-id) | Returns the settings in Performance group (filtered by tenant\_id if provided). | - On Front-end load   - Settings > Data Setup > Advanced Settings > Performance |
| [POST advancedSetting/performance](#post-advancedsetting-performance) | Updates the settings in Performance group. | Settings > Data Setup > Advanced Settings > Performance > Save |
| [GET advancedSetting/security/(tenant\_id)](#get-advancedsetting-security-tenant-id) | Returns the settings in Security group (filtered by tenant\_id if provided). | - On Front-end load   - Settings > Data Setup > Advanced Settings > Security |
| [POST advancedSetting/security](#post-advancedsetting-security) | Updates the settings in Security group. | Settings > Data Setup > Advanced Settings > Security > Save |
| [GET advancedSetting/miscSetting/(tenant\_id)](#get-advancedsetting-miscsetting-tenant-id) | Returns the settings in Others group (filtered by tenant\_id if provided). | Settings > Data Setup > Advanced Settings > Others |
| [POST advancedSetting/miscSetting](#post-advancedsetting-miscsetting) | Updates the settings in Others group. | Settings > Data Setup > Advanced Settings > Others > Save |
| [POST advancedSetting/defaultImageUrl](#post-advancedsetting-defaultimageurl) | Updates the default image url setting. | Not used |
| [GET advancedSetting/defaultImageUrl(?tenantId=tenant\_id)](#get-advancedsetting-defaultimageurl-tenantid-tenant-id) | Returns the default image url setting. | Setting Level Tenant is selected |
| [GET api/advancedSetting/defaultTheme(?tenantId=tenant\_id)](#get-api-advancedsetting-defaulttheme-tenantid-tenant-id)  New in version 2.9.0. | Returns the default theme setting. | Setting Level Tenant is selected |
| [POST api/advancedSetting/defaultTheme](#post-api-advancedsetting-defaulttheme)  New in version 2.9.0. | Add or update default theme for system or tenant. | Save default theme setting. |

## POST advancedSetting/category

Updates the list of [categories](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-data-source-category).

**Request**

> An array of [DataSourceCategory](https://devnet.logianalytics.com/hc/en-us/articles/4415492802327-DataSourceCategory) objects

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field true if the update is successful

**Samples**

> ```
> POST/api/advancedSetting/categoryHTTP/1.1
> ```
>
> With an existing empty category list, this request payload will add two categories ABC and XYZ:
>
> ```
> [{"id":null,"name":"ABC","tenantId":null},{"id":null,"name":"XYZ","tenantId":null}]
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":[]}
> ```
>
> User needs to reload the category list to have the server-generated ids by calling [GET advancedSetting/category/(tenant\_id)](#id2). User will get:
>
> ```
> [{"id":"0eac7266-4150-4b45-b6f7-6c40d95b6a37","name":"ABC","tenantId":null},{"id":"45c747c5-a11a-48f4-b966-14819a07450f","name":"XYZ","tenantId":null}]
> ```
>
> Right after that, assuming user have renamed ABC category to ABCDEF, removed XYZ and added QRS, the update request payload will be:
>
> ```
> [{"id":"0eac7266-4150-4b45-b6f7-6c40d95b6a37","name":"ABCDEF","tenantId":null},{"id":null,"name":"QRS","tenantId":null}]
> ```

## GET advancedSetting/category/(tenant\_id)

Returns an array of [categories](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-data-source-category) (filtered by tenant\_id if provided).

**Request**

> No payload

**Response**

> An array of [DataSourceCategory](https://devnet.logianalytics.com/hc/en-us/articles/4415492802327-DataSourceCategory) objects

**Samples**

> ```
> GET/api/advancedSetting/categoryHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"id":"45c747c5-a11a-48f4-b966-14819a07450f","name":"ABC","tenantId":null,"modified":"2016-03-20T04:47:09.1170000+07:00","deleted":false},{"id":"cda0ef9a-7fc0-4f9b-96ed-b1c33ea624b1","name":"DEF","tenantId":null,"modified":"2016-03-20T04:47:09.1330000+07:00","deleted":false},{"id":"868e6176-530f-4e8a-bef4-fb14d50e1882","name":"QRS","tenantId":null,"modified":"2016-03-20T04:47:09.1330000+07:00","deleted":false}]
> ```

## DELETE advancedSetting/category/{category\_id}

Deletes the [category](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-data-source-category) specified by category\_id.

**Request**

> No payload

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field true if the deletion is successful

**Samples**

> ```
> DELETE/api/advancedSetting/category/cda0ef9a-7fc0-4f9b-96ed-b1c33ea624b1HTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null}
> ```

## GET advancedSetting/performance/(tenant\_id)

Returns the settings in Performance group (filtered by tenant\_id if provided).

**Request**

> No payload

**Response**

> A [PerformanceSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504742039-PerformanceSetting) object

**Samples**

> ```
> GET/api/advancedSetting/performanceHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"queryTimeoutValue":3600,"queryTimeoutDefaultValue":3600,"useNoLockValue":true,"useNoLockDefaultValue":true,"dataSourceLimitValue":1000,"dataSourceLimitDefaultValue":1000,"tenantId":null}
> ```

## POST advancedSetting/performance

Updates the settings in Performance group.

**Request**

> A [PerformanceSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504742039-PerformanceSetting) object

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** fied true if the update is successful

**Samples**

> ```
> POST/api/advancedSetting/performanceHTTP/1.1
> ```
>
> Request payload to update Query Timeout to 360:
>
> ```
> {"queryTimeoutValue":360,"useNoLockValue":true,"dataSourceLimitValue":1000,"tenantId":null}
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null}
> ```

## GET advancedSetting/security/(tenant\_id)

Returns the settings in Security group (filtered by tenant\_id if provided).

**Request**

> No payload

**Response**

> A [SecuritySetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504792855-SecuritySetting) object

**Samples**

> ```
> GET/api/advancedSetting/securityHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"tenantFieldValue":"TenantID;UserID","tenantFieldDefaultValue":"","showTenantFieldValue":true,"showTenantFieldDefaultValue":true,"setAdditiveFieldAutoVisibleValue":false,"setAdditiveFieldAutoVisibleDefaultValue":false,"setAdditiveFieldAutoFilterableValue":false,"setAdditiveFieldAutoFilterableDefaultValue":false,"tenantId":null,"tenantFields":[{"name":"TenantID","isSystem":true},{"name":"UserID","isSystem":true}],"allowShowTenant":true,"modified":"2017-02-15T06:31:15"}
> ```

## POST advancedSetting/security

Updates the settings in Security group.

**Request**

> A [SecuritySetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504792855-SecuritySetting) object

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field true if the update is successful

**Samples**

> ```
> POST/api/advancedSetting/securityHTTP/1.1
> ```
>
> Request payload to set Additive Fields Auto Visible:
>
> ```
> {"showTenantFieldValue":true,"setAdditiveFieldAutoVisibleValue":true,"setAdditiveFieldAutoFilterableValue":false,"tenantId":null}
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null}
> ```

## GET advancedSetting/miscSetting/(tenant\_id)

Returns the settings in Others group (filtered by tenant\_id if provided).

**Request**

> A [Entity](https://devnet.logianalytics.com/hc/en-us/articles/4415504722455-Entity) object

**Response**

> An [OtherSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415512013975-OtherSetting) object

**Samples**

> ```
> GET/api/advancedSetting/miscSettingHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"sortColumnNameValue":false,"sortColumnNameDefaultValue":false,"trimTimeInJoinsValue":true,"trimTimeInJoinsDefaultValue":true,"timezoneForDataOffsetValue":0,"timezoneForDataOffsetDefaultValue":0,"timezoneForTimestampOffsetValue":0,"timezoneForTimestampOffsetDefaultValue":0,"convertNullToEmptyStringValue":false,"convertNullToEmptyStringDefaultValue":false,"showSchemaNameValue":false,"showSchemaNameDefaultValue":false,"showIntroductionTextValue":false,"showIntroductionTextDefaultValue":false,"introductionTextValue":"","introductionTextDefaultValue":"","sendToDiskPathValue":"","sendToDiskPathDefaultValue":"","tenantId":null,"modified":"2017-02-15T07:29:25.3300651""hideReportHeaderAndFooterValue":true,"hideReportHeaderAndFooterDefaultValue":false}
> ```

## POST advancedSetting/miscSetting

Updates the settings in Others group.

**Request**

> An [OtherSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415512013975-OtherSetting) object

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field true if the update is successful

**Samples**

> ```
> POST/api/advancedSetting/miscSettingHTTP/1.1
> ```
>
> Request payload to set Timezone Offset to -4:
>
> ```
> {"sortColumnNameValue":false,"trimTimeInJoinsValue":true,"timezoneForDataOffsetValue":"-4","timezoneForTimestampOffsetValue":"0","convertNullToEmptyStringValue":false,"showSchemaNameValue":false,"showIntroductionTextValue":false,"introductionTextValue":"","sendToDiskPathValue":"","sortColumnNameDefaultValue":false,"trimTimeInJoinsDefaultValue":true,"timezoneForDataOffsetDefaultValue":0,"timezoneForTimestampOffsetDefaultValue":0,"convertNullToEmptyStringDefaultValue":false,"showSchemaNameDefaultValue":false,"showIntroductionTextDefaultValue":false,"introductionTextDefaultValue":"","sendToDiskPathDefaultValue":"","tenantId":null,"modified":"2017-02-15T07:29:25.3300651","hideReportHeaderAndFooterValue":true}
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null}
> ```

## POST advancedSetting/defaultImageUrl

Updates the default image url setting.

**Request**

> Payload: an [AdvancedSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504696343-AdvancedSetting) object

**Response**

> The saved [AdvancedSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504696343-AdvancedSetting) object with **name** field value “DefaultImageUrl”

**Samples**

> ```
> POST/api/advancedSetting/defaultImageUrlHTTP/1.1
> ```
>
> Payload:
>
> ```
> {"value":"http://localhost/img/default.png","tenantId":null}
> ```
>
> Response:
>
> ```
> {"id":"c8ecf9fd-196d-44a3-90ec-97f393ebfc0c","name":"DefaultImageUrl","value":"http://localhost/img/default.png","defaultValue":null,"type":null,"tenantId":null,"deleted":false,"modified":"2017-04-12T16:55:11.4884228Z"}
> ```

## GET advancedSetting/defaultImageUrl(?tenantId=tenant\_id)

Returns the default image url setting.

**Request**

> No payload
>
> Optional querystring: ?tenantId=<the id of the tenant>

**Response**

> An [AdvancedSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504696343-AdvancedSetting) object

**Samples**

> ```
> GET/api/advancedSetting/defaultImageUrlHTTP/1.1
> ```
>
> Response:
>
> ```
> {"id":"c8ecf9fd-196d-44a3-90ec-97f393ebfc0c","name":"DefaultImageUrl","value":"http://localhost/img/default.png","defaultValue":null,"type":null,"tenantId":null,"deleted":false,"modified":"2017-04-12T16:55:11.4900000+07:00"}
> ```

## GET api/advancedSetting/defaultTheme(?tenantId=tenant\_id)

New in version 2.9.0.

Returns the default theme setting.

**Request**

> No payload
>
> Optional querystring: ?tenantId=<the id of the tenant>

**Response**

> An [AdvancedSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504696343-AdvancedSetting) object

**Samples**

> ```
> GET/api/advancedSetting/defaultThemeHTTP/1.1
> ```
>
> Response:
>
> ```
> {"id":"04d46221-24e0-4363-b2f6-99370d85ebe6","name":"DefaultTheme","value":"Monte Carlo","defaultValue":null,"type":"Others","tenantId":null,"deleted":false,"modified":"2018-05-22T06:43:56.0000000+07:00"}
> ```
>
> ```
> GET/api/advancedSetting/defaultTheme/c39a4500-b902-4e5b-ae86-901c09b71516HTTP/1.1
> ```
>
> Response:
>
> ```
> {"id":"06a83a57-39c0-44d4-841d-aa56e2d15ba7","name":"DefaultTheme","value":"Morning Sky","defaultValue":null,"type":"Others","tenantId":"c39a4500-b902-4e5b-ae86-901c09b71516","deleted":false,"modified":"2018-05-22T10:20:07.2700000+07:00"}
> ```

## POST api/advancedSetting/defaultTheme

New in version 2.9.0.

Add or update default theme for system or tenant.

**Request**

> Payload: an [AdvancedSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504696343-AdvancedSetting) object

**Response**

> The saved [AdvancedSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504696343-AdvancedSetting) object with **name** field value is “DefaultTheme”

**Samples**

> ```
> POST/api/advancedSetting/defaultThemeHTTP/1.1
> ```
>
> Response:
>
> ```
> {"id":"04d46221-24e0-4363-b2f6-99370d85ebe6","name":"DefaultTheme","value":"Monte Carlo","defaultValue":null,"type":"Others","tenantId":null,"deleted":false,"modified":"2018-05-22T10:38:41.5779097Z"}
> ```
