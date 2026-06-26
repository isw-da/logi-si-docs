---
title: "DataLayer.XML - Using DataLayer.XML with REST Web Services"
id: 4419707509911
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707509911-DataLayer-XML-Using-DataLayer-XML-with-REST-Web-Services
updated_at: 2022-07-17T02:24:37Z
---

# DataLayer.XML - Using DataLayer.XML with REST Web Services

# DataLayer.XML - Using DataLayer.XML with REST Web Services

DataLayer.XML is able to retrieve data from REST-style web services and the simplest approach is to configure its **XML File/URL** attribute with a complete URL. If the web service requires nothing else, the data will be retrieved using the default HTTP GET method.

![](https://devnet.logianalytics.com/hc/article_attachments/7522845573399/dlxmlfile_08.png)

For more flexibility, you can instead use a **Connection.REST** element to define the firstpart of the URL:

![](https://devnet.logianalytics.com/hc/article_attachments/7522830038807/dlxmlfile_09.png)

Using a value in the datalayer's **Connection ID** attribute causes its XML File/URL value to be appended to the Connection element's **URL Host** attribute value, as shown above. This can be useful if your application uses multiple datalayers to connect to the same web service.
If you prefer, you can leave the XML File/URL value blank and add a **Link Parameters** element beneath the datalayer. Its name/value pairs will then be appended to the Connection ID's URL Host value, preceded by a "?".

## Multi-Step Processing

You may encounter a security scenario where a two-step process is required, such as when a web service expects a "login" API call with credentials (as opposed to supplying credentials in a Connection.REST element) and returns an access ID, which must then be part of any other API calls. You can use this approach to handle this scenario:

1. Use Local Data with DataLayer.XML to authenticate and retrieve the web service's access ID. If the results are returned as JSON data, you'll need to use a Flattener element to make them available in tokens.
2. Use the resulting @Local token for the access ID with other DataLayer.XML elements to retrieve the desired data.

Some web services may require you to login and get an access ID, using a login URL, and then use that access ID in the Request Header of any subsequent queries, which go to to a different URL. In that case, you can use this approach:

1. Add *two* Connection.REST elements in your \_Settings definition, one for the API login and one for API queries, each with their appropriate URL.
2. Add a Request Header child element beneath the "query" connection element.
3. Use Local Data with DataLayer.XML and the "login" connection element to authenticate and retrieve the web service's access ID. If the results are returned as JSON data, you'll need to use a Flattener element to make them available in tokens.
4. Then use Set Session Variables to assign the resulting @Local token for the access ID to a session variable, for example "AccessID".
5. Use the @Session.AccessID~ token to configure the "query" connection element's child Request Header element.
6. All other DataLayer.XML elements that make API calls will use the "query" connection element.

## Using Different HTTP Methods and Request Body Data

If the web service requires you to use a different HTTP method, such as *POST* instead of *GET*, you can select it from the option list in the datalayer's **Http Method** attribute. Some web services may want you to use a custom method that's not in the option list, like *PATCH*, and in that case you can just type it right into the attribute value.

![](https://devnet.logianalytics.com/hc/article_attachments/7522842848535/dlxmlfile_10.png)

The **Http Body** element, shown above, has two attributes:

* **Content Type,** which sets the content type in the request header and defaults to *application/xml* for this datalayer.
* **Http Body Content**, which is the request body data, entered as an XML or JSON document or as a URL-encoded set of name/value pairs.

If you want to encode name/value pairs in the request body data to avoid possible issues with invalid characters, set the Http Body element's Content Type attribute to *application/x-www-form-urlencoded* and use the **Http Body Params** element to define the pairs. Tokens may be used in Http Body Param values.
