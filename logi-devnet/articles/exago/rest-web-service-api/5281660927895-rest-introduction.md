---
title: "REST \u2014 Introduction"
id: 5281660927895
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281660927895-REST-Introduction
updated_at: 2022-05-03T22:07:50Z
---

# REST — Introduction

# REST — Introduction

The Exago REST Web Service API provides programmatic access to create session configurations based on user credentials. The REST API is an alternative to the .NET API for applications not built in .NET environments. REST web services provide access to API functions for any client capable of passing HTTP requests over a network.

## Installing REST

Install the REST Web Service API following the steps in [REST — Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281669323671-REST-Getting-Started).

## The API

This is the documentation for the Exago REST API. This information will always reflect the latest available Exago version. Changes are made periodically to the API. For details, please refer to [REST Updates](https://devnet.logianalytics.com/hc/en-us/articles/5281630703255-REST-Updates).

The API is a JSON API. For more information, see [Using JSON](https://devnet.logianalytics.com/hc/en-us/articles/5281669842199-Using-JSON).

Endpoints are documented with the HTTP request type and a URI sub-path:

```
POST /rest/Sessions
```

Prepend the URL path to the web service to get the full endpoint URL:

```
http://{myapp}/{exago web service}/rest/Sessions
```

Curly braces, {}, are values that you must supply:

```
GET /rest/Roles/{Id}
```

Usually the value to supply is found in JSON given by a request to the base endpoint. For example, to retrieve a particular Role by its “Id”, first run GET /rest/roles to see the roles available to you:

```
[
  {
    "Id": "Admin"
  },
  {
    "Id": "User"
  }
]
```

Then to see detailed data on a Role, run GET /rest/roles/{Id} where {Id} is the value of its “Id” property (case sensitive):

```
GET /rest/Roles/Admin
```

Some methods may accept optional URL parameters. Append any url parameters to the end of the endpoint URL using the following format:

```
/rest/{endpoint}?{param1}={value1}&{param2}={value2}&{param3}={value3}
```

For all endpoints except /rest/sessions, you must append the session Id as a url parameter to the end of the URL:

```
VERB /rest/{endpoint}?sid={sid}
```

Some examples in this documentation use **cURL** (“curl”), which is a command-line tool for transferring data using various protocols. Curl is compatible with Windows or Linux, and can be downloaded from [**https://curl.haxx.se/**](https://curl.haxx.se/). If curl is installed, copy-and-paste the examples into a command line, replacing any item in {braces} with local variables, in order to test them out.

Long examples may be broken into multiple lines in order to improve readability. The caret symbol (^) tells the command line to ignore the following line break. On Linux, replace the caret with a backslash ().

```
curl http://{webservice}/rest/Settings?sid={sid} ^
	-H "Accept: application/json" ^
	-H "Content-Type: application/json" ^
	-H "Authorization: Basic Og==" ^
	-X PATCH ^
	-d "{'ShowExpressReports':false}"
```

For testing, we recommend a graphical application such as **Advanced Rest Client** or **Postman**.

## Authentication

The REST API requires authorization to be accessed. To make an authorized request, the authorization header must be supplied. There are two different authorization methods depending on requirements. Both rely on the **Admin Console** > **General** > **Other Settings** > **User ID** and **Admin Console** > **General** > **Other Settings** > **REST Key**.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Prior to *v2017.3*, the **Admin Console** > **General** > **Other Settings** > **Password** setting was utilized as the REST Key.

### Basic Authorization

When using basic authorization, the authorization header is constructed as follows:

1. The User ID and REST Key are combined into a string `User ID:REST Key`.
2. The resulting string literal is encoded using Base64.
3. “Basic” and a space are placed before the encoded string.

For example, if the User ID is “Brian” and the REST Key is “open sesame” then the authorization header would be constructed as follows:

1. Combine User ID and REST Key into a string

   ```
   Brian:open sesame
   ```
2. Encode the string using Base 64

   ```
   QWxhZGRpbjpvcGVuIHN1c2FtZQ==
   ```
3. Append “Basic ” to the front

   ```
   Basic QWxhZGRpbjpvcGVuIHN1c2FtZQ==
   ```

The auth key is sent in clear text with each request. If this is a concern, the REST API should be deployed in an SSL environment or the more secure [ExagoKey Authorization](#ExagoKey) should be used.

A configuration with a blank User ID and REST Key can be accessed using the following authorization header:

```
Authorization: Basic Og==
```

### ExagoKey Authorization

ExagoKey authorization uses the HMAC-SHA256 algorithm for authorization. When using ExagoKey authorization, the authorization header is constructed as follows:

1. The string to sign is UTF-8 encoded, then signed with the UTF-8 encoded REST key using the HMAC-SHA256 algorithm.
2. The resulting signature is then encoded using Base64.
3. The User ID and a colon is put before the encoded signature.
4. “ExagoKey” and a space are placed before the encoded string literal.

For example, if the User ID is “Brian” and the REST Key is “open sesame” then depending on the request the authorization header might be something like:

```
Authorization: ExagoKey Brian:6HZE5tCWjsjbJY+VXQg3UzXlK/jeoGhbm25YDXiHWdE=
```

Using ExagoKey does not send the password with each request, making it more secure than Basic Authorization. To ensure greater security the REST API should be deployed in an SSL environment.

### ExagoKey String

The ExagoKey string that is to be signed is constructed using the following information from the request, in the following order, with “n” after each item (including the last one).

1. The HTTP Method, must be in uppercase.
2. The absolute request path, up to but not including the query string if one should exist. For example, if the request is to `http://myserver.com/exago/rest/Sessions?config=myconfig` the absolute request path would be `/exago/rest/Sessions`.
3. The contents of the `Content-Length` header.
4. The contents of the `Content-Type` header, or a string of zero length if no header exists.
5. The contents of the `Content-MD5` header, or a string of zero length if no header exists.
6. The session ID, or a string of zero length if no session ID exists.
7. The contents of the `X-Exago-Date` header, or the contents of the Date header if the `X-Exago-Date` header does not exist, or a string of zero length if neither header exists.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If a date is supplied, the REST API will reject any request that is older than 15 minutes from the supplied date. The date supplied is in GMT (UTC).

## Request Format

The REST API uses JSON. It will not accept data in any other format. In the case of an error, it may return plain text, but this is not session data. You must set the following headers on all requests:

* `Content-Type: application/json`
* `Accept: application/json`
* `Authorization: {type} {authstring}`

Most of the examples in this documentation omit the headers in order to improve readability; however they are required for all requests.

## Response Format

Successful requests return HTTP status codes in the 200 range. When you create a resource with POST, the API returns the resource in the response body:

```
Status: 201 Created
Location: /{webservice}/rest/Entities/Employees
{
  "Id":            "Employees",
  "Name":          "Employees",
  "Schema":        "dbo",
  "CategoryName":  "",
  "DataName":      "Employees",
  "DataSourceId":  "0",
  "DataType":      "Table",
  ...
}
```

You may get a plain text response in the case of errors or bad requests. The content will not contain any session data.

Responses have one of the following status codes:

**200**

The request was completed successfully. The document in the body, if any, is a representation of some resource. This code is usually returned for a successful GET request.

**201**

The request was completed successfully. A new resource has been created at the URL specified in the Location header of the response. The document in the body, if any, is a representation of the resource created. This code is usually returned for a successful POST request.

**204**

The request was completed successfully. There is no content in the body. This code is usually returned for successful PATCH, PUT, and DELETE requests.

**400**

The request was bad on the client side. The document in the body, if any, is error data describing the problem. This is usually the result of using an invalid method type.

**401**

The request wasn’t authorized to access the resource. The document in the body, if any, is error data describing the problem.

**404**

The requested resource was not found. The document in the body, if any, is error data describing the problem. Often this is the result of a malformed URL request string.

**409**

The request caused a conflict between two resources. The document in the body, if any, is error data describing the problem.

**500**

There was a problem on the server side. The document in the body, if any, is error data describing the problem. Often this is the result of a malformed JSON request package.

## Request Data

The API returns and accepts JSON values, which can be strings, numbers, objects, arrays, **true**, **false**, or **null**. See [Using JSON](https://devnet.logianalytics.com/hc/en-us/articles/5281669842199-Using-JSON)

Each endpoint uses a unique JSON object for input and output of variables. The JSON is documented with each resource in a table:

| Name | Type | Writable | Description |
| --- | --- | --- | --- |

Each row represents a property. The **Name** field is the name of the property. The **Type** field indicates what type of data it accepts.

The **Writable** field indicates whether this property can be written:

* no – this property is read-only
* yes – this property can be written
* yes (“value”) – this property can be written; its default value is in parentheses
* required – this property must be written; it cannot be null
* required-create – this property must be written for all POST calls; it is read-only for all other calls

The **Description** field is any relevant information about the property.

### Id Values

Most resources are identified by an “Id” property, which is an integer or string. The Id must be unique among the set of resources. If you are permitted write-access to the Id, avoid conflicting names.

### Constant or Enum Values

Some properties can only accept one of a set of string or integer values (or sometimes null).

Properties which accept enumerated values are indicated as having an “enum” type. The description field in its JSON representation links to the list of possible values, which can usually be represented by their string or equivalent integer value. For example:

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| DataType | enum | yes | [Parameter Type](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#Paramete) |

Properties which accept constant string values are indicated as having an “const” type. The description field in its JSON representation links to the list of possible values. For example:

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| JoinType | const | yes | [Join Type](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#Join) |

## This Documentation

This documentation is broken down by section according to the use cases for different API elements. Each section represents a single endpoint or set of related endpoints and use cases. To find out how to do something using the REST API, first browse to the relevant section for the element you want to use. Then check the table of contents for what actions you want to take; Or read from top to bottom to gain a fuller understanding of the resource.

Check out [REST — Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281669323671-REST-Getting-Started) to get started, or [List of REST Endpoints](https://devnet.logianalytics.com/hc/en-us/articles/5281669098391-List-of-REST-Endpoints) for the available endpoints and their usages.

### Additional Resources

* Admin Support Lab — [REST Web Service API Setup & Security](https://devnet.logianalytics.com/hc/en-us/articles/5281554127767-REST-Web-Service-API-Setup-Security) (video)
* Admin Support Lab — [Batch REST API](https://devnet.logianalytics.com/hc/en-us/articles/5281531616407-Batch-REST-API) (video)
* Admin Support Lab — [.NET and REST APIs](https://devnet.logianalytics.com/hc/en-us/articles/5281562235671--NET-and-REST-APIs) (video)
* Admin Training Series — [Installing REST [Windows]](https://devnet.logianalytics.com/hc/en-us/articles/5281563077271-Installing-REST-Windows-) (video)
* Admin Training Series — [Configuring the REST Web Service [Windows]](https://devnet.logianalytics.com/hc/en-us/articles/5281540715927-Configuring-the-REST-Web-Service-Windows-) (video)
* Admin Training Series — [Installing REST [Linux]](https://devnet.logianalytics.com/hc/en-us/articles/5281540942103-Installing-REST-Linux-) (video)
* Admin Training Series — [Configuring the REST Web Service [Linux]](https://devnet.logianalytics.com/hc/en-us/articles/5281562765719-Configuring-the-REST-Web-Service-Linux-) (video)
