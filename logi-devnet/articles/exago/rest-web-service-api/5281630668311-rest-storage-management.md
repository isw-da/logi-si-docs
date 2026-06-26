---
title: "REST \u2014 Storage Management"
id: 5281630668311
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281630668311-REST-Storage-Management
updated_at: 2022-05-03T22:07:48Z
---

# REST — Storage Management

# REST — Storage Management

Viewing and modifying the Storage Management configuration via the REST Web Service API is available in Exago *v2020.1+*.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All requests require a [Session Id](https://devnet.logianalytics.com/hc/en-us/articles/5281669654679-REST-Sessions#Session) URL parameter and basic request headers. In the following topic, headers are omitted in the interest of brevity.

## Storage Management Configuration JSON

A complete Storage Management configuration is represented as a JSON object with the following properties:

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| IsAdmin | Boolean | yes | If *true*, user can see the entire contents of the Storage Management database. |
| Assembly | string | yes | The fully qualified path to the DLL implementing the [IStorageManagement Interface](https://devnet.logianalytics.com/hc/en-us/articles/5281646850327-Storage-Management-Custom-Implementation#IStorage) |
| ClassName | string | yes | The class name in the **Assembly** implementing the[IStorageManagement Interface](https://devnet.logianalytics.com/hc/en-us/articles/5281646850327-Storage-Management-Custom-Implementation#IStorage) |
| ReportListCacheEnabled | Boolean | yes | *True* if report list caching is enabled |
| ReportXmlCacheEnabled | Boolean | yes | *True* if report definition XML caching is enabled |
| ReportListCacheTimeout | integer | yes | Number of seconds before the report list cache times out |
| ThemeListCacheTimeout | integer | yes | Number of seconds before the theme list cache times out |
| ReportXmlCacheTimeout | integer | yes | Number of seconds before the report XML definition cache times out |
| TablePrefix | string | yes | Prefix for the Storage Management database tables. For more information, review [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management). |
| DefaultInheritFlag | Boolean | yes | Value of the Inherit Flag in the configuration. For more information, review [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management). |
| DefaultPartyTypeId | integer | yes | ID from the Party Type table to create a content access record with. For more information, review [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management). |
| DefaultAccessFlags | integer | yes | Access flags to create a content access record with*.* For more information, review [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management). |
| Identities | string | yes | A collection of name-value pairs for the identity keys. For more information, review [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management). |
| Options | string | yes | A collection of name-values pairs for Storage Management options.  * **DbType** — the type of Storage Management database * **DbProvider** — the database provider used to connect to the Storage Management database * **ConnectionString** — connection string to connect to the Storage Management database * **RptListCacheKey** — a prefix for the report list cache key. In Exago’s implementation of Storage Management, a report list cache key is constructed from the values of the identity keys. Setting this value will apply a prefix to the cache key. Setting a value here should only be necessary if users with the same identity key values should somehow be handled differently. * **ReportListCacheKey** — reserved for future use   In a custom Storage Management implementation, this **Options** collection can also be used to pass additional name-value pairs around the application.  For more information, review [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management). |

### Retrieve the Storage Management Configuration

Returns a complete [Storage Management Configuration JSON](#Storage) object.

```
GET /rest/StorageMgmt
```

### Update the Storage Management Configuration

Send a complete [Storage Management Configuration JSON](#Storage) object. All existing values will be cleared and replaced with the values in the object. Values that are not in the object will be set to their system defaults.

```
PUT /rest/StorageMgmt
```

#### Example

```
{
 "IsAdmin": false,
 "Assembly": "C:\\Exago\\bin\\WebReports.ContentDatabase.dll",
 "ClassName": "WebReports.ContentDatabase.StorageMgmtDatabase",
 "ReportListCacheEnabled": true,
 "ReportXmlCacheEnabled": false,
 "ReportListCacheTimeout": 31,
 "ThemeListCacheTimeout": 63,
 "ReportXmlCacheTimeout": 32,
 "TablePrefix": "dbo.",
 "DefaultInheritFlag": true,
 "DefaultPartyTypeId": 3,
 "DefaultAccessFlags": 65535,
 "EffectiveReportXmlCacheEnabled": false,
 "SaveValuesImplicit": true,
 "Identities": {
  "userId": "Astro Boy",
  "classId": "admin",
  "companyId": "Exago",
  "ownerId": "Astro Boy"
 },
 "Options": {
  "DbType": "SQLite",
  "DbProvider": "SQLite",
  "ConnectionString": "Data Source=C:\\Exago\\mydatabase.sqlite",
  "ReportListCacheKey": "",
  "RptListCacheKey": "mykey"
 }
}
```

### Edit an Individual Storage Management Setting

Include only those properties to be updated. Returns with HTTP 200 to indicate success and a copy of the updated configuration as a [Storage Management Configuration JSON](#Storage) object.

```
PATCH /rest/StorageMgmt
```

#### Example

This example changes the value of three of the Storage Management identity keys.

```
"Identities": {
    "userId": "aboy",
    "classId": "user",
    "companyId": "Exago, Inc."
}
```
