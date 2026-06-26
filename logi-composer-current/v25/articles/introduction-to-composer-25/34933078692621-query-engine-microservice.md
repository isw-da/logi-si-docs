---
title: "Query Engine Microservice"
id: 34933078692621
section: "Introduction to Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933078692621-Query-Engine-Microservice
updated_at: 2026-05-26T22:07:41Z
---

# Query Engine Microservice

# Query Engine Microservice

The Composer query engine sits between the web application and the Composer data connectors.

The query engine has three primary roles:

1. It deconstructs and converts your query requests into distributed execution plans.
2. It optimizes the execution plans based on data platform capabilities, in-memory cached results, and the query engine capabilities.
3. It executes data functions that include:

   * Communicating with Composer data connectors to execute push-down queries
   * Retrieving data from in-memory cached results, as appropriate
   * Using in-memory processing to combine, append, or manipulate one or more data sets to produce only the values needed to fulfill your request.

The key capabilities of the query engine include [push-down processing for select data sources](#Push-Dow), [microqueries and Data Sharpening](#Microque), [adaptive caching](#Adaptive), [data playback and live mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933104108173-Data-Playback-and-Live-Mode), and [multisource analysis](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933104442765-Multisource-Analysis).

## Push-Down Processing

Composer is built so users can interact directly with data down to the atomic row-level detail. Push-down processing is necessary to support this ad-hoc, interactive user experience on fresh data. As users explore the data and drill down to lower levels of detail, Composer continues to push processing down as new queries. The data store returns only the values that the query engine needs to populate the user’s visuals. The Composer push-down architecture also avoids scaling up the query engine unnecessarily when complex processing can be better executed on high-performance database engines or scalable data platforms.

Composer’s default processing strategy is to push down as much work to the underlying data sources as possible, for as many data sources as possible. Internal to the query engine is a query optimizer that evaluates each end-user request, and determines whether to submit all or part of the request to the target data stores. This includes pushing down filtering criteria, derived fields, custom metrics, and offset, limit, sort, and time bucketing operations.

The ability to push down filters means that the data platform engine doesn’t need to scan large data sets unnecessarily. It also reduces the amount of data transferred over the network from the data source to Composer. Composer can push down all filters that a user requests in the UI.

Push-down of derived fields and custom metrics optimizes performance for the most resource-intensive operations. Composer always pushes down custom metric aggregations: min, max, sum, avg, count, distinct count, last value, and percentiles. Where advantageous, the query engine combines several simpler aggregates to compute more complex metrics.

Composer offers automatic time bucketing, which allows you to group and filter data by time categories such as current or prior week, month and year, rolling time periods, and so on. There is no need to pre-aggregate or model time buckets, freeing up technical personnel to work on other work. All that is needed is a date-time field. The query engine does all the work of interpreting and converting user requests to one or more queries and pushing the whole operation to the data store.

The benefits of the Composer live-connect approach with push-down processing are:

* You always have access to fresh data from the data store
* Computational resources are scaled and managed where they make the most sense
* Network bandwidth is conserved
* It works very well for hybrid-cloud deployments, since there’s no need for massive data movement between systems

Composer’s implementation of push-down processing also allows users to explore down to the atomic, row level detail. In this way, Composer is unique in its ability to make the full breadth and depth of big data environments available for exploration.

## Microqueries and Data Sharpening

Microqueries and Data Sharpening™ are patented technologies that work together to let you interact with big data. The query engine invokes microqueries and Data Sharpening based on criteria such as the type of aggregate values requested and anticipated query run time. Microqueries and Data Sharpening are ideal for big data that is partitioned by date and that runs on a cluster with many processing cores. This functionality can be disabled when you set up the Composer data source configurations for your data store.

Microqueries, which are executed first, sample data across database partitions. The query engine submits a full long-running query that runs with the first set of microqueries. A progress indicator estimates the progress of the full long-running query. Both the full query and the microqueries run until the full query runs to completion or the user changes direction, at which point both the long-running query and microqueries are canceled to conserve processing and network resources.

Data Sharpening analyzes the sample data and streams predictive results to the your browser (or other client) over a WebSocket connection. Data Sharpening’s predictive results may fluctuate a bit up or down until the final query is reported. However, the relative values of each group usually remain consistent as the data is sharpened. For example, the tallest bar in a bar chart at 10% completion will almost always remain the tallest bar at 100% completion. This means that you can be confident exploring data even as it streams live to the dashboard.

When you drill down, filter, change metrics or groupings, or perform any other action that changes data values, Composer cancels the full long-running query and microqueries to free up the data source engine for the next sequence of queries. Canceling active queries, however, is not trivial, and many JDBC drivers do not support it. In these cases, Composer’s data connectors issue native API calls to complete the task.

## Adaptive Caching

The query engine optionally accelerates performance through adaptive caching. The cache eviction algorithm prefers the most frequently used data, with consideration of cache size and expiration times. Users with the appropriate privileges can configure cache sizes and time-to-live (TTL) schedules, and can forcibly clear caches.

Composer uses its cache to enhance performance in scenarios where large numbers of users are concurrently viewing the same shared visuals.

**Note:** 
Cached data is shared between users only if they have the same data access permissions and security context.

When caching is enabled, Composer does not requery the data source to obtain the data unless the cache is cleared or unless a refresh schedule is defined in the data source configuration. See [Cache Tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891391629-Cache-Tab) and [Trigger Refresh Jobs](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933145070861-Trigger-Refresh-Jobs).

By default, data caching is enabled for all data sources.
The Composer cache stores all the results of aggregated requests from your data source. When a visual is created the request is first sent to the Composer cache. If the required results are found in the cache, they are visualized on your visual.

Each visual that is cached has a key that uniquely identifies its content and how it can be reused. The key is calculated based on the ​request​ and user.​ The request provides the information related to data grouping and content, such as the data attributes and metrics. The user provides contextual information, like per-user security filters, user attributes, etc. This way all the security settings are taken into account when storing and using the cached visual. Information from the cached visual is shared between users only when they have the same data access permissions and security context.

The data cache optimizes data processing and avoids unnecessarily expensive queries. To avoid an expensive query, all or parts of multiple interactive data caches can be used to fulfill different user requests.

The cache uses normalized requests for its cache entry key. This key allows data caches to be safely used by multiple users with different security contexts and visual types. To serve requests that require different data, the query engine applies a number of possible transformations to the cached data. For example, columns can be dropped to enforce field-based security, additional filters can be applied to enforce row-level security, time windows can shift, or the data can be rolled up to higher levels of aggregation. Because there may be several ways to get the same result using different cache entries, the query engine evaluates different transformation approaches for complexity, and selects the simplest approach.

Not all data requests are cached. By default, cache entries are stored in the metadata repository, where they are retained after a service restart.
