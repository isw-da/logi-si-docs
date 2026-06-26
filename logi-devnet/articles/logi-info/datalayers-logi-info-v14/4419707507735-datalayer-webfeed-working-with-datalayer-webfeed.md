---
title: "DataLayer.WebFeed - Working with DataLayer.WebFeed"
id: 4419707507735
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707507735-DataLayer-WebFeed-Working-with-DataLayer-WebFeed
updated_at: 2022-07-17T02:08:12Z
---

# DataLayer.WebFeed - Working with DataLayer.WebFeed

# DataLayer.WebFeed - Working with DataLayer.WebFeed

The datalayer connects directly to the web feed and retrieves the information. Unlike most datalayer elements, this one does not requred a Connection element. Feed information is retrieved and cached as rows and columns, with one row per news item. Data retrieved into the datalayer is cached in XML format.

The data retrieved with a datalayer is available using @Data tokens, in the format @Data.*ColumnName*~. The spelling of the column name is *case-sensitive*. The data is only available within the scope of the parent element of the datalayer, not throughout the entire report definition. The DataLayer.Linked element can be used to make the data reusable in another datalayer outside this scope.

"Column names" may vary depending on the feed, however the column names for news items will all start with "item\_" and for header values with "channel\_".
Examples of possible valid "column names" available through the @Data token are:

| Column | Description |
| --- | --- |
| item\_title | The title of the new item |
| item\_link | A link to the item. If the feed is a news aggregator, this link may have embedded in it the URL of the source for this item |
| item\_guid | A unique identifier used by the feed for this item |
| item\_category | A categorization, specific to the feed, of this item |
| item\_pubDate | A publication timestamp for this item |
| item\_description | Text of the actual item, possibly in HTML format |
| channel\_pubDate | A publication timestamp for this item |
| channel\_lastBuildDate | Timestamp for the last assembly of the feed page |
| channel\_webMaster | Email address of the feed page web master |
| channel\_image\_url | URL for images associated with feed |
| channel\_copyright | HTML copyright message |
| channel\_language | Language designator abbreviation |
| channel\_image\_link | URL for image associated with item |

The [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419700048023-Auto-Columns) element can be used to quickly see which "column names" are being returned by the feed.
You can view the data retrieved into the datalayer by turning on the Debugger Link in the \_Settings definition (General element) and using the resulting icon at the bottom of the report page to view the Debugger Trace Page. A link on the trace page will display the retrieved data.
