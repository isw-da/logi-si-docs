---
title: "DataLayer:Web.Feed"
id: 1500009514782
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514782-DataLayer-Web-Feed
updated_at: 2021-06-17T01:58:14Z
---

# DataLayer:Web.Feed

# DataLayer:Web.Feed

The **DataLayer.WebFeed** element provides developers with data from an **RSS** or **Atom** web feed, such as those on news sites, blogs, and other frequently-updated web information sources, in a convenient form.

* Attributes
* [Work with DataLayer.WebFeed](#WorkingWith)
* [Use Studio's DataLayer Wizard](#Wizard)

## Attributes

The DataLayer.WebFeed element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required through v10.1.46) A unique element ID. |
| Web Feed URL | The address (URL) of a RSS or Atom web feed, e.g.  http://news.google.com/news?output=rss |
| Include Headers | When *True*, feed-level elements (management information) is included with the usual news item information. Default: *False* |

## Work with DataLayer.WebFeed

The datalayer connects directly to the web feed and retrieves the information. Unlike most datalayer elements, this one requires **no connection element**. Feed information is retrieved and cached as rows and columns, with one row per news item. Data retrieved into the datalayer is cached in **XML** format.

The data retrieved with a datalayer is available using @Data **tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is **case-sensitive**. The data is only available within the **scope** of the **parent** element of the datalayer, not throughout the entire report definition. The DataLayer.Linked element can be used to make the data reusable in another datalayer outside this scope.

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

Logi Info developers can make use of the **AutoColumns** element to quickly see which "column names" are being returned by the feed.

Others can view the data retrieved into the datalayer by turning on the **Debugging Link** in the \_Settings definition (General element) and using the resulting link at the bottom of the report page to view the **Application Trace** page. A link on the Trace page will display the retrieved data.

## Use Studio's DataLayer Wizard

Beginning in v10.0.299, Studio includes a wizard that can assist you in configuring DataLayer.Web Feed.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771850391/dlwebfeed_01.png)

As shown above, the wizard can be started by selecting and then right-clicking the parent element under which you want to add the datalayer, and using the context menus to select "Add a Web Feed DataLayer". The wizard will open; use it as follows:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771850647/dlwebfeed_02.png)

1. Enter the URL for the web feed. Click **Next** to continue.  
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778687895/dlwebfeed_03.png)
2. Click **Finish** to close the wizard.  
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771850903/dlwebfeed_04.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778688151/dlwebfeed_04a.png)
3. The wizard has inserted the datalayer and configured its attributes, as shown above.

[![](https://logianalytics.zendesk.com/hc/article_attachments/4402778391063/totop.gif)](#)  [Back to the top](#)
