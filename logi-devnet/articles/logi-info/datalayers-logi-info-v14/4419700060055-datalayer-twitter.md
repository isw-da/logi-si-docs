---
title: "DataLayer.Twitter"
id: 4419700060055
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700060055-DataLayer-Twitter
updated_at: 2022-07-17T02:09:43Z
---

# DataLayer.Twitter

# DataLayer.Twitter

The **DataLayer.Twitter** element searches the Twitter web service for "tweets" and messages based on the search criteria specified. There are multiple search criteria available for this search and the datalayer returns a dataset with the results.

* Attributes
* [Working with DataLayer.Twitter](#WorkingWith)

This element is only available in Logi Info .NET applications; it is *not available* in for Java applications.

## Attributes

The DataLayer.Twitter element has the following attributes:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) Specifies the ID of a Connection.Twitter connection element configured in the \_Settings definition. If this value is left blank, the datalayer will use the first connection found in the \_Settings definition. We recommend you enter an ID here in all cases. |
| Search Type | (Required) Specifies the type of search to be performed on the Twitter site. Options include:   * User Statuses * Friend Statuses * User's Inbox * User's Sent Items * Keyword Search |
| ID | Specifies an optional, unique element ID. Recommended for easier identification when debugging. |
| Keyword | This attribute is only used when the Search Type attribute is set to "Keyword Search". The datalayer will then limit the tweets it retrieves to those including this keyword. |
| Maximum Rows | Specifies the maximum number of results rows to retrieve. Default: *unlimited* |

  

## Working with DataLayer.Twitter

This datalayer works with a **Connection.Twitter** datasource connection element, which must be added to the \_Settings definition and properly configured.

The datalayer retrieves and caches the results returned from Twitter. You can add child elements beneath the datalayer to affect the results, including:

* **Filtering**: Sort, group, or restrict the result data
* **Joining**: Apply SQL JOINs to the data in the datalayer
* **Extending**: Add virtual columns to the datalayer that contain aggregated, calculated, or totaled result values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report defintions

Data retrieved into the datalayer is cached in XML format, in memory and/or on the web server's file system. The latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/4419715421975-The-Logi-Server-Engine) and may be of interest to developers working with extremely large datasets or large numbers of concurrent users.

The data retrieved with a datalayer is available using @Data tokens, in the format @Data.*ColumnName*~. The spelling of the column name is case-sensitive. The data is only available within the scope of the parent element of the datalayer, not throughout the entire report definition. The **DataLayer.Linked** element can be used to make the data reusable in another datalayer outside this scope.

DateTime-type data retrieved into the datalayer is automatically reformatted to ISO 8601 format ("2009-06-23T09:32:11-04:00").

The [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419700048023-Auto-Columns) element can be used to quickly display in your report all the data in a datalayer; this is particularly useful during development.

The valid "column names" retrieved and available through the @Data token vary depending on the type of search conducted. These are identified in the [Twitter API documentation](https://developer.twitter.com/en/docs.html) and may change with different API releases. The datalayer retrieves *all* of the columns made available by the API for each search type.

The data retrieved into the datalayer can be viewed by turning on the Debugging Link in your \_Settings definition (General element) and using the resulting link at the bottom of your report page to view the Debugger Trace page. A link on the Trace page will display the retrieved data.
