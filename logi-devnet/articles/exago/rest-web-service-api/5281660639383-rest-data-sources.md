---
title: "REST \u2014 Data Sources"
id: 5281660639383
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281660639383-REST-Data-Sources
updated_at: 2022-05-03T22:07:51Z
---

# REST — Data Sources

# REST — Data Sources

A **Data Source** is a resource which contains or accesses the information which is reported on. Often this is a database, but a variety of types are supported. Data Sources are accessed using a connection string, which passes the location of the resource and authentication params. This endpoint allows for session-based read/write access to all data sources for the current config.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All requests require a [Session Id](https://devnet.logianalytics.com/hc/en-us/articles/5281669654679-REST-Sessions#Session) URL parameter and basic request headers. In the following topic, headers are omitted in the interest of brevity.

## Data Source JSON

Data Sources are represented as JSON objects with the following properties:

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| Id | string | no | The unique Id of this data source |
| Name | string | yes | The name of this data source |
| DbType | enum | yes (“MsSql”) | [Data Source Type](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#Data) |
| Connection | string | yes | The connection string of this data source |
| Schema | string | yes | The data source schema name (blank for default) |

#### Example

```
{
  "Id":         "1",
  "Name":       "My Data Server",
  "DbType":     "MsSql",
  "Connection": "Server=DataServer;Database=Northwind;uid=username;pwd=password;",
  "Schema":     "dbo"
}
```

### List Data Sources

List all the data sources in the current configuration. Output is an array of JSON objects, each representing an individual data source.

```
GET /rest/DataSources
```

List all of the data objects only in the user’s session specific configuration. Replace *myconfig.xml* with the file name of the corresponding config file name. Output is an array of JSON objects, each representing an individual data source.

```
GET /rest/DataSources?config=myconfig.xml
```

| Name | Type | Description |
| --- | --- | --- |
| Id | string | The unique Id of this data source |
| Name | string | The name of this data source |

#### Using curl

```
curl http://{webservice}/rest/DataSources?sid={sid} -X GET
```

#### Example response

```
Status: 200 OK
[
  {
    "Id":   "0",
    "Name": "Northwind"
  },
  {
    "Id":   "1",
    "Name": "AdventureWorks"
  }
]
```

### Show Data Source

Show the properties of the data source specified by its Id.

```
GET /rest/DataSources/{Id}
```

#### Using curl

```
curl http://{webservice}/rest/DataSources/{Id}?sid={sid} -X GET
```

#### Example response

```
Status: 200 OK
{
  "Id":         "0",
  "Name":       "Northwind",
  "DbType":     "MsSql",
  "Connection": "Server=DataServer;Database=Northwind;uid=username;pwd=password;",
  "Schema":     "dbo"
}
```

### Create Data Source

```
POST /rest/DataSources
```

#### Using curl

```
curl http://{webservice}/rest/DataSources?sid={sid} -X POST ^
  -d "{'Name':'NW','DbType':'MsSql','Connection':'Server=SRV;Database=NW;uid=ID;pwd=PW;'}"
```

#### Example response

```
Status: 201 Created
Location:/{webservice}/rest/DataSources/2

{
  "Id":         "2",
  "Name":       "NW",
  "DbType":     "MsSql",
  "Connection": "Server=SRV;Database=NW;uid=ID;pwd=PW;",
  "Schema":     ""
}
```

### Edit Data Source

Only supply the properties to be edited.

```
PATCH /rest/DataSources/{Id}
```

#### Using curl

```
curl http://{webservice}/rest/DataSources/{Id}?sid={sid} -X PATCH ^
  -d "{'Connection':'Server=SRV;Database=NW;uid=Admin;pwd=Password;'}"
```

#### Example response

```
Status: 204 No Content
```

### Delete Data Source

```
DELETE /rest/DataSources/{Id}
```

#### Using curl

```
curl http://{webservice}/rest/DataSources/{Id}?sid={sid} -X DELETE
```

#### Example response

```
Status: 204 No Content
```
