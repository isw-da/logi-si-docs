---
title: "REST \u2014 Server Events"
id: 5281646580247
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281646580247-REST-Server-Events
updated_at: 2022-05-03T22:07:50Z
---

# REST — Server Events

# REST — Server Events

Server events can be accessed for reference and disabled for the session. Server events cannot currently be created or edited using REST.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All requests require a [Session Id](https://devnet.logianalytics.com/hc/en-us/articles/5281669654679-REST-Sessions#Session) URL parameter and basic request headers. In the following topic, headers are omitted in the interest of brevity.

## Server Event JSON

Server events are represented as JSON objects with the following properties:

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| Id | string | no | The unique Id of this server event |
| Name | string | no | The name of this server event |

#### Example

```
{
  "Id":   "0",
  "Name": "RunAfterReportExecution"
}
```

## List Server Events

List all the server events in the current configuration. Output is an array of objects, each representing an individual server event.

```
GET /rest/ServerEvents
```

| Name | Type | Description |
| --- | --- | --- |
| Id | string | The unique Id of this server event |
| Name | string | The name of this server event |

### Using curl

```
curl http://{webservice}/rest/ServerEvents?sid={sid} -X GET
```

### Example response

```
Status: 200 OK
[
  {
    "Id":   "0",
    "Name": "RunAfterReportExecution"
  },
  {
    "Id":   "1",
    "Name": "AddDisclaimerToOutput"
  }
]
```

## Show Server Event

Show the properties of the server event specified by its Id.

```
GET /rest/ServerEvents/{Id}
```

### Using curl

```
curl http://{webservice}/rest/ServerEvents/{Id}?sid={sid} -X GET
```

### Example response

```
Status: 200 OK
{
  "Id":   "0",
  "Name": "RunAfterReportExecution"
}
```

## Delete Server Event

```
DELETE /rest/ServerEvents/{Id}
```

### Using curl

```
curl http://{webservice}/rest/ServerEvents/{Id}?sid={sid} -X DELETE
```

### Example response

```
Status: 204 No Content
```
