---
title: "DataLayer.Twitter"
id: 1500009530381
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530381-DataLayer-Twitter
updated_at: 2021-06-17T01:58:14Z
---

# DataLayer.Twitter

# DataLayer.Twitter

The **DataLayer.Twitter** element searches the Twitter web site for "tweets" and messages based on the search criteria specified. There are multiple search criteria available for this search and the datalayer returns a dataset with the results.

* Attributes
* [Work with DataLayer.Twitter](#WorkingWith)

This element is only available in Logi Info; it is *not available* in Logi Report, nor is it available yet in our Java products.

## Attributes

The DataLayer.Twitter element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required through v10.1.46) A unique element ID. |
| Search Type | (Required) The type of tweet or message search to be performed on the Twitter site. Options include:   * User Statuses * Friend Statuses * User's Inbox * User's Sent Items * Keyword Search |
| Connection ID | The ID of a Connection.Twitter datasource connection defined in the \_Settings definition. If this value is left blank, the datalayer will use the **first** connection found in the \_Settings definition. For clarity, developers are advised to enter an ID here in all cases. |
| Keyword | This attribute is only used when the Search Type attribute is set to "Keyword Search". The datalayer will then limit the tweets it retrieves to those including this keyword. |
| Maximum Rows | The maximum number of results rows to retrieve. Default: no limit. |

## Work with DataLayer.Twitter

This datalayer works with a **Connection.Twitter** datasource connection element, which must be added to the \_Settings definition and properly configured.

The datalayer retrieves and **caches** the results returned from Twitter. You can add **child elements** beneath the datalayer to affect the results, including:

* **Filtering**: Sort, group, or restrict the result data
* **Joining**: Apply SQL JOINs to the data in the datalayer
* **Extending**: Add virtual columns to the datalayer that contain aggregated, calculated, or totaled result values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report defintions

The use of many of these elements is described in separate DevNet documents.

Data retrieved into the datalayer is cached in **XML** format, in memory (v8 and earlier), or in memory and/or on the web server's file system (v9+). The latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/1500009515722-The-Logi-Server-Engine) and may be of interest to developers working with extremely large datasets or large numbers of concurrent users.

The data retrieved with a datalayer is available using @Data **tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is **case-sensitive**. The data is only available within the **scope** of the **parent** element of the datalayer, not throughout the entire report definition. The **DataLayer.Linked** element can be used to make the data reusable in another datalayer outside this scope.

DateTime-type data retrieved into the datalayer is automatically reformatted to ISO 8601 format ("2009-06-23T09:32:11-04:00").

The [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/1500009529561-Auto-Columns) element can be used to quickly display in your report all the data in a datalayer; this is particularly useful during development.

The valid "column names" retrieved and available through the @Data token vary depending on the type of search conducted. These are identified in the [Twitter API documentation](https://dev.twitter.com/docs/api) and may change with different API releases. The datalayer retrieves *all* of the columns made available by the API for each search type.

The data retrieved into the datalayer can be viewed by turning on the **Debugging Link** in your \_Settings definition (General element) and using the resulting link at the bottom of your report page to view the **Debugger Trace** page. A link on the Trace page will display the retrieved data.
