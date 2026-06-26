---
title: "REST \u2014 Parameters"
id: 5281661027479
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281661027479-REST-Parameters
updated_at: 2022-05-03T22:07:49Z
---

# REST — Parameters

# REST — Parameters

Parameters are used throughout the application to store values. The **[User Identification](https://devnet.logianalytics.com/hc/en-us/articles/5281619919255-User-Identification)** parameters are used for identifying the current user. Non-hidden parameters can be accessed in reports.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All requests require a [Session Id](https://devnet.logianalytics.com/hc/en-us/articles/5281669654679-REST-Sessions#Session) URL parameter and basic request headers. In the following topic, headers are omitted in the interest of brevity.

## Parameter JSON

Parameters are represented as JSON objects with the following properties. In *v2022.1.0+*., parameters can have multiple values. When the **IsMultiValue** property is *True*, use the **Values** array for getting and setting the values. When **IsMultiValue** is *False*, use the Value property for getting and setting the value.

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| Id | string | required-create | The unique Id of this parameter |
| DataType | enum | yes (“String”) | [Parameter Type](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#Paramete) |
| Value | string | yes | The value of this parameter, if **IsMultiValue** is *False*. If **IsMultiValue** is *True*, a comma-separated list of the values from the Values array.  If **IsMultiValue** is *True*, and any strings in the array contain commas, all values are encapsulated in single quotes (for example `'a,bc', 'cde', 'efg`). Any strings containing single quotes are escaped (for example `'it\'s', 'hot', 'out'`) |
| PromptText | string | yes | If set, text to prompt the user for a value |
| IsHidden | Boolean | yes (true) | Whether the parameter is accessible in reports |
| IsMultiValue | Boolean | yes (false) | Whether this parameter holds a single value (false) or multiple values (true). If false, the parameter value is held in the **Value** property. If true, the values are held in the **Values** property. |
| Values | Array of strings | yes | If **IsMultiValue** is *True*, an array of values for this parameter.  When **IsMultiValue** is *False*, the string at index 0 is the same as the Value property |

### Example

```
{
  "Id":         "MyParameter",
  "DataType":   "String",
  "Value":      "",
  "PromptText": "Input a value",
  "IsHidden":   true
}
```

## List All Parameters

List all the parameters in the current configuration. Output is an array of objects, each representing an individual parameter.

```
GET /rest/Parameters
```

| Name | Type | Description |
| --- | --- | --- |
| Id | string | The unique Id of this parameter |

### Using curl

```
curl http://{webservice}/rest/Parameters?sid={sid} -X GET
```

### Example response

Status: 200 OK

```
  {
    "Id": "MyParameter"
  },
  {
    "Id": "HelloWorld"
  }
```

## Show an Existing Parameter

Show the properties of the parameter specified by its Id.

```
GET /rest/Parameters/{Id}
```

### Using curl

```
curl http://{webservice}/rest/Parameters/{Id}?sid={sid} -X GET
```

### Example response

```
Status: 200 OK

{
  "Id":         "MyParameter",
  "DataType":   "String",
  "Value":      "",
  "PromptText": "Input a value",
  "IsHidden":   true
}
```

## Create a New Parameter

Parameters are designed to be set in the API. If they do not already exist in config, create them programmatically.

```
POST /rest/Parameters
```

### Using curl

```
curl http://{webservice}/rest/Parameters?sid={sid} -X POST ^
	-d "{'Id':'Hello','DataType':'String','Value':'World','IsHidden':false}"
```

### Example response

```
Status: 201 Created
Location: /{webservice}/rest/Parameters/Hello

{
  "Id":         "Hello",
  "DataType":   "String",
  "Value":      "World",
  "PromptText": "",
  "IsHidden":   false
}
```

## Edit an Existing Parameter

Only supply the properties to be edited.

```
PATCH /rest/Parameters/{Id}
```

### Using curl

```
curl http://{webservice}/rest/Parameters/{Id}?sid={sid} -X PATCH ^
	-d "{'IsHidden':true}"
```

### Example response

```
Status: 204 No Content
```

## Delete Parameter

```
DELETE /rest/Parameters/{Id}
```

### Using curl

```
curl http://{webservice}/rest/Parameters/{Id}?sid={sid} -X DELETE
```

### Example response

```
Status: 204 No Content
```
