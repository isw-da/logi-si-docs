---
title: "DataLayer.Cached - DataLayer.Cached Special Considerations"
id: 4419707475607
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707475607-DataLayer-Cached-DataLayer-Cached-Special-Considerations
updated_at: 2022-07-17T01:54:04Z
---

# DataLayer.Cached - DataLayer.Cached Special Considerations

# DataLayer.Cached - DataLayer.Cached Special Considerations

The following should be considered when using this datalayer:

## Joins

Developers may choose to retrieve data from multiple sources and use **Join** elements to combine it. How does DataLayer.Cached work in this scenario?

![](https://devnet.logianalytics.com/hc/article_attachments/4419706744471/dlcached_03.png)

As shown in the example above, all of the datalayers and joins can be placed beneath one DataLayer.Cached element and the data resulting from *all* of the joins will be cached.
This is fine if the currency of all of the data sources is similar. However, what if some of the data is updated more frequently than the rest?

![](https://devnet.logianalytics.com/hc/article_attachments/4419714716183/dlcached_04.png)

One approach when data has mixed currency, as shown above, is to use DataLayer.Cached to cache "long-term" data that *does not* change frequently and then join that data with another datalayer that retrieves "short-term" data that *does* change frequently.

If you have a large number of joins, then this approach depends upon your ability to relate the data appropriately (no short- and long-term datalayers interleaved).

What about caching at different levels of the join? Sorry, it's not possible to use a DataLayer.Cached element beneath a Join element.

## Time to Service Requests Can Vary

Typically, systems that cache data "snapshots", such as data marts and mini data warehouses, use independent processes to monitor the cache's expiration time and refresh it. However, no such process exists for DataLayer.Cached; cache expiration is tested with every request and the cache is refreshed when expiration is detected. This may result in some requests (those that cause the cache to be refreshed) taking longer than others, as the child datalayer that actually retrieves the data
will then run.

## Scope Issues

This datalayer can be used in multiple report definitions to access the same cached data (by using the same Cache Key value). It's very important, in such circumstances, that all instances of DataLayer.Cached, and its child elements, which access the same cache be *configured**identically*. They must have the exact same attribute settings and the exact same child datalayer, otherwise the cached data will be different and/or be set to expire differently, depending on which report definition's
request causes it to be refreshed. This is a good reason to consider implementing this datalayer as a Shared Element, see [Shared Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419715558423-Shared-Elements).

## Not for Use with Subdatalayers

At this time, DataLayer.Cached should *not* be used with reports that include **Subdata Layer** elements; an error will result.
