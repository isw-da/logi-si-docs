---
title: "DataLayer.REST - Multi-Step Security Processing"
id: 4419722837271
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722837271-DataLayer-REST-Multi-Step-Security-Processing
updated_at: 2022-07-17T02:08:14Z
---

# DataLayer.REST - Multi-Step Security Processing

# DataLayer.REST - Multi-Step Security Processing

You may encounter a security scenario where a two-step process is required, such as when a web service expects a "login" API call with credentials (as opposed to supplying credentials in a Connection.REST element) and returns an access ID, which must then be part of any other API calls. You can use this approach to handle this scenario:

1. Use Local Data with DataLayer.REST to authenticate and retrieve the web service's access ID. If the results are returned as JSON data, you'll need to use a Flattener element to make them available in tokens.
2. Use the resulting @Local token for the access ID with other DataLayer.REST elements to retrieve the desired data.

Some web services may require you to login and get an access ID, using a login URL, and then use that access ID in the Request Header of any subsequent queries, which go to to a different URL. In that case, you can use this approach:

1. Add *two* Connection.REST elements in your \_Settings definition, one for the API login and one for API queries, each with their appropriate URL.
2. Add a Request Header child element beneath the "query" connection element.
3. Use Local Data with DataLayer.REST and the "login" connection element to authenticate and retrieve the web service's access ID. If the results are returned as JSON data, you'll need to use a Flattener element to make them available in tokens.
4. Then use Set Session Variables to assign the resulting @Local token for the access ID to a session variable, for example "AccessID".
5. Use the @Session.AccessID~ token to configure the "query" connection element's child Request Header element.
6. All other DataLayer.REST elements that make API calls will use the "query" connection element.
