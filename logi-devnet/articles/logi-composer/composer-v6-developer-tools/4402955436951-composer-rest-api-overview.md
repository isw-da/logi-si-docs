---
title: "Composer REST\u00a0API Overview"
id: 4402955436951
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955436951-Composer-REST-API-Overview
updated_at: 2021-08-07T17:29:19Z
---

# Composer REST API Overview

# Composer REST API Overview

The Composer REST API provides methods for retrieving, updating, and deleting Composer metadata pertaining to accounts, connections, and users.

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

![](https://devnet.logianalytics.com/hc/article_attachments/4404952805911/criticalicon.gif) Some API endpoints are marked as “experimental” in the Swagger documentation we provide. These endpoints are in the early stages of design and are subject to change. In addition, Logi Analytics makes no commitment to their stability and may remove them without notice. These experimental endpoints are not recommended for use in production.

This topic describes the following REST API topics:

* [*Authentication*](#Authentication)
* [*Version Compatibility*](#Versioning)
* [*HATEOAS Architecture*](#HATEOAS)
* [*API Entry Point*](#EntryPoint)
* [*The /api/ Path*](#servicepath)
* [*Optimistic Locking on PATCH Calls*](#Optimist)
* [*Reference Documentation*](#Referenc)

## Authentication

The API currently uses basic access authentication. Most actions require admin-level access to the particular account manipulated using the API.

## Version Compatibility

Each version of the API maintains backward compatibility with previous versions. The HTTP Accepts/Content-type header is used to specify the version for the resources that are produced and used by the API. When sending data to or receiving data from the API, you must use the appropriate HTTP header.

When working with the API, you should explicitly set the version of the API that you want to use. For example, in cURL requests, you would include the `--header` parameter as shown below.

```
   # For submitting data     
   curl --header "Content-type: application/vnd.composer.v2+json" ...
     
   # Consuming data     
   curl --header "Accept: application/vnd.composer.v2+json,application/vnd.composer+json" ...
```

To ensure you always use the latest version of Composer, use the generic media type: `application/vnd.composer+json`.

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) There is a risk associated with using this generic media time to ensure you always use the latest version. Because this approach does not tie calls to specific API versions, if the latest version changes, your integration may break. It is safer to tie your API calls to specific versions.

The current API media type version will be sent as a header, `X-Composer-Media-Type`, in the response to every API request.

The rule for specifying media types is simple. Always include the generic media type `application/vnd.composer+json`and, if you specify a particular version, always put it first. For example:

* Correct: `application/vnd.composer.v2+json,application/vnd.composer+json`
* Incorrect: `application/vnd.composer+json, application/vnd.composer.v2+json`

## HATEOAS Architecture

The Composer API implements the HATEOAS architectural pattern. Most resources returned by the API have a `links` element. The links elements is an array of objects, each with two properties:

* `rel`: short description of how this link relates to the parent object
* `href`: the actual link value

Every resource will at least have a `rel: "self"` link, which is the canonical reference to that object. You can use the other links to explore the relations of a given object, for example, the users in an account or the sources tied to a connection.

## API Entry Point

The initial entry point to the API is `http://<host>:<port>/<context>/api`. For example:

```
http://localhost:8080/composer/api
```

This URL points to the root API resources that you can use to browse through the API.

## The /api/ Path

Some functions of the Composer client application call APIs using a `/api/` path. Except where noted in Composer's developer documentation, endpoints that use the
`/api/` path are for Composer's internal use only.

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) Applications built with Composer's internal-use APIs, are subject to a high risk of unexpected breakage.

APIs on the `/api/` path that are safe to use include, for example, the `/api/sources/key` endpoint.

## Optimistic Locking on PATCH Calls

API data source PATCH calls use optimistic locking to ensure the PATCH is applied to the most recent records. A `version` parameter is used in these calls to track the version counter number. If this counter is not incremented in the payload of the call or if it is in error, the PATCH call will fail with an error similar to this:

```
"details": "Source Epsilon Impala API Update Test has been updated since last read. Refresh required",  
"error": "INTERNAL_ERROR"
```

The exact and correct version counter number must be used or the API call will fail. For example, if you just submitted a PATCH call using version 8 and your next PATCH call uses version 10, you will receive an error response.

Consequently, prior to any PATCH call, be sure you do one of the following things:

* Perform a GET call immediately prior to the PATCH call to retrieve the latest version counter number. This is the recommended approach.
* If no changes have been made using the UI, and you can safely remember the version counter number of the previous call after every successful PATCH call, simply increment the version counter number in your newest PATCH call.

## Reference Documentation

Composer maintains Swagger-based reference materials for the REST APIs. In this testing environment, you can experiment with the APIs features.

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

![](https://devnet.logianalytics.com/hc/article_attachments/4404952805911/criticalicon.gif) Some API endpoints are marked as “experimental” in the Swagger documentation we provide. These endpoints are in the early stages of design and are subject to change. In addition, Logi Analytics makes no commitment to their stability and may remove them without notice. These experimental endpoints are not recommended for use in production.
