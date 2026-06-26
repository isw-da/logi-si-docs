---
title: "DataLayer.JSON - Multi-Step Processing"
id: 4406817302423
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817302423-DataLayer-JSON-Multi-Step-Processing
updated_at: 2022-04-06T06:05:17Z
---

# DataLayer.JSON - Multi-Step Processing

# DataLayer.JSON - Multi-Step Processing

You may encounter a security scenario where a two-step process is required, such as when a web service expects a "login" API call with credentials (as opposed to supplying credentials in a Connection.JSON element) and returns an access ID, which must then be part of any other API calls. You can use this approach to handle this scenario:

1. Use Local Data with DataLayer.JSON to authenticate and retrieve the web service's access ID. You may need to use a Flattener element to make the returned data available in tokens.
2. Use the resulting @Local token for the access ID with other DataLayer.JSON elements to retrieve the desired data.

Some web services may require you to login and get an access ID, using a login URL, and then use that access ID in the Request Header of any subsequent queries, which go to a different URL. In that case, you can use this approach:

1. Add *two* Connection.REST elements in your \_Settings definition, one for the API login and one for API queries, each with their appropriate URL.
2. Add a Request Header child element beneath the "query" connection element.
3. Use Local Data with DataLayer.JSON and the "login" connection element to authenticate and retrieve the web service's access ID. You may need to use a Flattener element to make the returned data available in tokens.
4. Then use Set Session Variables to assign the resulting @Local token for the access ID to a session variable, for example "AccessID".
5. Use the @Session.AccessID~ token to configure the "query" connection element's child Request Header element.
6. All other DataLayer.JSON elements that make API calls will use the "query" connection element.
