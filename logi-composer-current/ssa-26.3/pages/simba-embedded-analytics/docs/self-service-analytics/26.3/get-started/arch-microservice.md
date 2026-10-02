> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Microservices Architecture

The Self-Service Analytics platform is architected as a set of loosely-coupled Java microservices. Unlike traditional business intelligence software, which is deployed as a monolithic application, a microservices architecture allows for the following benefits:

* Faster deployment of new functionality
* Optimal resource management
* Faster recovery in some failure scenarios
* Greater deployment flexibility

Each microservice runs in its own Java Virtual Machine (JVM) to optimize memory allocation and runtime attributes to meet its function and load. A failure in one microservice does not take down all microservices, and recovery is faster because only the failed microservice needs to restart. Deploying new functionality, such as an updated or custom data store connector, occurs by auto-discovery, and without requiring a server restart.

Separately, Self-Service Analytics centralizes its metadata store in a relational database and includes an internal messaging queue. The communication protocols used by the microservices include WebSockets (for real-time bidirectional communication) and HTTP/S.

For more information about individual microservices, see:

* Self-Service Analytics server microservice for its [Web-Based User Interface](#web-based-user-interface)
* [Configuration Microservice](#configuration-microservice)
* [Query Engine Microservice](#query-engine-microservice)
* [Data Connector Microservices](#data-connector-microservices)
* [Data Writer Microservice](#data-writer-microservice)
* [Service Monitor Microservice](#service-monitor-microservice)
* [Service Discovery Microservice](#service-discovery-microservice)
* [Self Service Report Microservice](#self-service-report-microservice)
* [Screenshot Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/screenshot-install)
* [Distributed Tracing for Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/distributed-tracing-using)

The following links provide general information about all microservices:

* [Self-Service Analytics Microservice Name Reference](#self-service-analytics-microservice-name-reference)
* [Microservice Startup Order](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#microservice-startup-order)
* [Start Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices)
* [Stop Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#stop-microservices)
* [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices)
* [Scaling Self-Service Analytics Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#scaling-self-service-analytics-microservices)
* [Manage Self-Service Analytics Microservices Using the Command Line Utility](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#manage-self-service-analytics-microservices-using-the-command)
* [Self-Service Analytics System Metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#self-service-analytics-system-metrics)

<h2 id="configuration-microservice">
  Configuration Microservice
</h2>

The Self-Service Analytics configuration microservice is packaged with the [Spring Cloud Configuration](https://www.baeldung.com/spring-cloud-configuration) server, which allows Self-Service Analytics to easily integrate with its Spring-based microservices. It provides the mechanism by which property settings can be maintained using the Service Monitor. The property settings are persisted in a supported PostgreSQL data store or in a GitHub repository.

A `config-server-upload.jar` utility is available that can be used to migrate the microservice properties from your standalone Self-Service Analytics servers to the Self-Service Analytics configuration data in the PostgreSQL data store, where the configuration microservice can maintain them. See [Migrate Properties to the Configuration Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/distenv-ov#migrate-properties-to-the-configuration-server).

For complete information, see [Maintain Application Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#maintain-application-properties).

<h2 id="data-connector-microservices">
  Data Connector Microservices
</h2>

Self-Service Analytics offers the widest set of connectors for modern data stores deployed on-premises or in the cloud, such as Hadoop, NoSQL, search engines, and modern data warehouses. In addition to the set of standard, out-of-the-box, data connectors that we provide, you can create custom data connectors.

Self-Service Analytics's standard, out-of-the-box, data connectors are smart, leveraging the unique capabilities of each data platform to take advantage of query expressiveness and to optimize performance. For example, the data connectors leverage:

* Data partitions in Impala and other similar sources
* Faceted search when querying an unstructured data search engine such as Elasticsearch or Solr
* Native APIs for NoSQL databases

The data connectors use native APIs either in whole or in part to interact with the target data store. For some modern data platforms, all user interactions are converted to native API calls. For data stores that can be queried using SQL over a JDBC driver, the data connector uses SQL when available and native API calls when necessary. For example, a data store may support query cancellation, but its JDBC driver may not. Self-Service Analytics data connectors are smart enough to enrich the data interaction experience beyond standard off-the-shelf functionality.

Self-Service Analytics's microservices-based architecture allows your developers to build connectivity to proprietary data platforms or to data for which a native connector is not currently available. Custom connectors can also be smart by making full use of the Self-Service Analytics query engine, including its Data Sharpening and live mode functionality as well as enabling custom security features such as user delegation and Kerberos authentication.

Custom connectors can also be used to extend Self-Service Analytics data connectors with additional business rules. For example, a custom connector can implement the logic necessary to query specific tables based on the end user's group membership.

Each Self-Service Analytics data connector deploys as a standalone Thrift server running in its own Java processing space and registers with Consul and Self-Service Analytics's Service Monitor as a Self-Service Analytics microservice.

For complete information about Self-Service Analytics data connectors, see [Connect Self-Service Analytics to Data Stores](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov).

<h2 id="service-discovery-microservice">
  Service Discovery Microservice
</h2>

The Service Discovery microservice integrates Self-Service Analytics with the Spring Cloud Consul. It provides:

* External configuration capabilities for Self-Service Analytics via a key/value store.
* A service discovery client backed by the Consul service registry.

<h2 id="data-writer-microservice">
  Data Writer Microservice
</h2>

Self-Service Analytics offers a multipurpose Data Writer microservice that writes data to a relational database for an enriched analytic experience. Its current uses are to:

* Persist [user-uploaded flat text or CSV files](#user-uploaded-files) for reuse, performance, and functional improvements such as push-down processing and derived fields
* Simplify [landing or persisting streaming data](#landing-streaming-data) into a high-performance data platform for subsequent analysis
* Store user-generated [keysets](#keysets-user-directed-set-analysis) for “set analysis” to be used in single and multisource data environments.

The Data Writer microservice consists of a microservice that receives requests using a REST API, a message queue, and writable data connectors.

<h3 id="user-uploaded-files">
  User Uploaded Files
</h3>

Users with privileges to create Self-Service Analytics data sources can use the user interface to upload flat files to your environment. The Data Writer microservice passes the text or CSV file to a message queue to manage backflow, and then writes the file contents to a database. Users then work with it as any other data source. Additional APIs are available to manage uploaded files.

<h3 id="landing-streaming-data">
  Landing Streaming Data
</h3>

Any streaming engine, such as Kafka, Spark Streaming, Storm, Apex, Nifi, Kinesis, and others, can be used to process and land data in a persistent data storage environment. Alternatively, the Data Writer microservice can receive live streaming data via the REST API, pass it to an internal messaging queue for backflow management, and then write it to a database. After it is landed, data is accessible as any other data source for seamless live mode and historical analysis.

insightsoftware took this approach because it provides greater functionality than connecting directly to a live stream, and requires far less administrative overhead and maintenance than a complex lambda architecture.

<h3 id="keysets-user-directed-set-analysis">
  Keysets: User-Directed Set Analysis
</h3>

Self-Service Analytics offers an elegant approach to “set analysis” that allows users to explore key relationships within and between data, regardless of where the data is stored. The Data Writer microservice provides the backbone for this functionality by receiving an ordered and filtered set of “keys” from the web application, passing the keyset through the message queue, and storing it in a relational database for reuse by authorized persons. Users work independently to apply keysets to data stored on any platform. The user experience is swift and fluid, and the supporting architecture is so elegant and straightforward that no SQL or coding is ever required.

<h2 id="query-engine-microservice">
  Query Engine Microservice
</h2>

The Self-Service Analytics query engine sits between the web application and the Self-Service Analytics data connectors.

The query engine has three primary roles:

1. It deconstructs and converts your query requests into distributed execution plans.

2. It optimizes the execution plans based on data platform capabilities, in-memory cached results, and the query engine capabilities.

3. It executes data functions that include:

   * Communicating with Self-Service Analytics data connectors to execute push-down queries
   * Retrieving data from in-memory cached results, as appropriate
   * Using in-memory processing to combine, append, or manipulate one or more data sets to produce only the values needed to fulfill your request.

The key capabilities of the query engine include [push-down processing for select data sources](#push-down-processing), [microqueries and Data Sharpening](#microqueries-and-data-sharpening), [adaptive caching](#adaptive-caching), [data playback and live mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#data-playback-and-live-mode), and [multisource analysis](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#multisource-analysis).

<h3 id="push-down-processing">
  Push-Down Processing
</h3>

Self-Service Analytics is built so users can interact directly with data down to the atomic row-level detail. Push-down processing is necessary to support this ad-hoc, interactive user experience on fresh data. As users explore the data and drill down to lower levels of detail, Self-Service Analytics continues to push processing down as new queries. The data store returns only the values that the query engine needs to populate the user’s visuals. The Self-Service Analytics push-down architecture also avoids scaling up the query engine unnecessarily when complex processing can be better executed on high-performance database engines or scalable data platforms.

Self-Service Analytics’s default processing strategy is to push down as much work to the underlying data sources as possible, for as many data sources as possible. Internal to the query engine is a query optimizer that evaluates each end-user request, and determines whether to submit all or part of the request to the target data stores. This includes pushing down filtering criteria, derived fields, custom metrics, and offset, limit, sort, and time bucketing operations.

The ability to push down filters means that the data platform engine doesn’t need to scan large data sets unnecessarily. It also reduces the amount of data transferred over the network from the data source to Self-Service Analytics. Self-Service Analytics can push down all filters that a user requests in the UI.

Push-down of derived fields and custom metrics optimizes performance for the most resource-intensive operations. Self-Service Analytics always pushes down custom metric aggregations: min, max, sum, avg, count, distinct count, last value, and percentiles. Where advantageous, the query engine combines several simpler aggregates to compute more complex metrics.

Self-Service Analytics offers automatic time bucketing, which allows you to group and filter data by time categories such as current or prior week, month and year, rolling time periods, and so on. There is no need to pre-aggregate or model time buckets, freeing up technical personnel to work on other work. All that is needed is a date-time field. The query engine does all the work of interpreting and converting user requests to one or more queries and pushing the whole operation to the data store.

The benefits of the Self-Service Analytics live-connect approach with push-down processing are:

* You always have access to fresh data from the data store
* Computational resources are scaled and managed where they make the most sense
* Network bandwidth is conserved
* It works very well for hybrid-cloud deployments, since there’s no need for massive data movement between systems

Self-Service Analytics’s implementation of push-down processing also allows users to explore down to the atomic, row level detail. In this way, Self-Service Analytics is unique in its ability to make the full breadth and depth of big data environments available for exploration.

<h3 id="microqueries-and-data-sharpening">
  Microqueries and Data Sharpening
</h3>

Microqueries and Data Sharpening™ are patented technologies that work together to let you interact with big data. The query engine invokes microqueries and Data Sharpening based on criteria such as the type of aggregate values requested and anticipated query run time. Microqueries and Data Sharpening are ideal for big data that is partitioned by date and that runs on a cluster with many processing cores. This functionality can be disabled when you set up the Self-Service Analytics data source configurations for your data store.

Microqueries, which are executed first, sample data across database partitions. The query engine submits a full long-running query that runs with the first set of microqueries. A progress indicator estimates the progress of the full long-running query. Both the full query and the microqueries run until the full query runs to completion or the user changes direction, at which point both the long-running query and microqueries are canceled to conserve processing and network resources.

Data Sharpening analyzes the sample data and streams predictive results to the your browser (or other client) over a WebSocket connection. Data Sharpening’s predictive results may fluctuate a bit up or down until the final query is reported. However, the relative values of each group usually remain consistent as the data is sharpened. For example, the tallest bar in a bar chart at 10% completion will almost always remain the tallest bar at 100% completion. This means that you can be confident exploring data even as it streams live to the dashboard.

When you drill down, filter, change metrics or groupings, or perform any other action that changes data values, Self-Service Analytics cancels the full long-running query and microqueries to free up the data source engine for the next sequence of queries. Canceling active queries, however, is not trivial, and many JDBC drivers do not support it. In these cases, Self-Service Analytics’s data connectors issue native API calls to complete the task.

<h3 id="adaptive-caching">
  Adaptive Caching
</h3>

The query engine optionally accelerates performance through adaptive caching. The cache eviction algorithm prefers the most frequently used data, with consideration of cache size and expiration times. Users with the appropriate privileges can configure cache sizes and time-to-live (TTL) schedules, and can forcibly clear caches.

Self-Service Analytics uses its cache to enhance performance in scenarios where large numbers of users are concurrently viewing the same shared visuals.

<Note>
  Cached data is shared between users only if they have the same data access permissions and security context.
</Note>

When caching is enabled, Self-Service Analytics does not requery the data source to obtain the data unless the cache is cleared or unless a refresh schedule is defined in the data source configuration. See [Cache Tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab) and [Trigger Refresh Jobs](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/console#trigger-refresh-jobs).

By default, data caching is enabled for all data sources. The Self-Service Analytics cache stores all the results of aggregated requests from your data source. When a visual is created the request is first sent to the cache. If the required results are found in the cache, they are visualized on your visual.

Each visual that is cached has a key that uniquely identifies its content and how it can be reused. The key is calculated based on the request and user. The request provides the information related to data grouping and content, such as the data attributes and metrics. The user provides contextual information, like per-user security filters, user attributes, etc. This way all the security settings are taken into account when storing and using the cached visual. Information from the cached visual is shared between users only when they have the same data access permissions and security context.

The data cache optimizes data processing and avoids unnecessarily expensive queries. To avoid an expensive query, all or parts of multiple interactive data caches can be used to fulfill different user requests.

The cache uses normalized requests for its cache entry key. This key allows data caches to be safely used by multiple users with different security contexts and visual types. To serve requests that require different data, the query engine applies a number of possible transformations to the cached data. For example, columns can be dropped to enforce field-based security, additional filters can be applied to enforce row-level security, time windows can shift, or the data can be rolled up to higher levels of aggregation. Because there may be several ways to get the same result using different cache entries, the query engine evaluates different transformation approaches for complexity, and selects the simplest approach.

Not all data requests are cached. By default, cache entries are stored in the metadata repository, where they are retained after a service restart.

## Screenshot Microservice

The Screenshot microservice allows you to view snapshots of your saved dashboards. See [Screenshot Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/screenshot-install).

<h2 id="service-monitor-microservice">
  Service Monitor Microservice
</h2>

The Service Monitor microservice provides administrators with real-time views of microservice health, configuration, and logs. The Service Monitor is not installed as part of a default Self-Service Analytics installation, so you must install and configure this before you can use it. Using the Service Monitor, you can:

* Review all Self-Service Analytics microservices and their log files.
* Produce a [diagnostics bundle](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support#download-the-diagnostics-bundle) to send to insightsoftware Support.
* Set the logging level and properties for each microservice.

For complete information, see [Screenshot Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/screenshot-install).

<h2 id="web-based-user-interface">
  Web-Based User Interface
</h2>

Self-Service Analytics provides a single, unified web-based user interface for administrators, dashboard developers, analysts and users who consume the information provided in your visuals, dashboards, and self service reports. The web application is compatible with modern browsers that support the HTML5 standard for web applications and WebSocket communication protocol.

Because it supports the HTML5 standard, the user interface responsively adjusts to a tablet form factor without loss of functionality. The application will function on a smartphone, however due to the smaller form factor, such devices do not lend themselves well to the out-of-the-box exploratory experience for which Self-Service Analytics was developed. Custom mobile apps can be developed using mobile frameworks such as Ionic or React Native.

The web browser (or any client application using the Self-Service Analytics JavaScript APIs) is responsible for establishing a two-way WebSocket communication channel between itself and the Self-Service Analytics query engine. The web browser is responsible for keeping the WebSocket connection alive and automatically reconnecting to the query engine when network problems occur.

Messages transmit over WebSockets using the lightweight JSON (JavaScript object notation) file format. There are several message types used by Self-Service Analytics.

| Message Type | Description |
| - | - |
| Query messages | Define the query request. Requests can be raw data requests or single or multidimensional data requests that include filters, sorts, and limits. |
| Data messages | Contain the results of a query execution. |
| Metadata messages | Contain information about the query status (progress, error, time window). |
| Control messages | Define control events, such as pause or play. |

The Self-Service Analytics web application delivers unique functionality to the end-user, such as:

* Data Sharpening™ to stream predictive results when working with very large data sets
* Smart loading of visuals and dashboards. Smart loading improves the performance for loading visuals on a dashboard.
* A time bar to simplify time-based analysis
* Data DVR to rewind, play, and fast forward data streams
* Live mode to visualize near real-time data streams
* Highly configurable visuals and dashboards that includes filtering and sorting the data in near real-time
* Search box and facets to maximize performance when connecting to search-enabled data platforms such as Apache Solr and Elasticsearch.

The web application pulls all these technologies and features together in a “non-blocking” data exploration experience.

There are two ways to understand the non-blocking UI. One is that data loads independently in each visual, so viewing the entire dashboard is not slowed down by the longest running query. The second is that at the same time that data rolls in, users can filter, sort, drill down, reformat, change visual type (re-visualize), and otherwise manipulate visuals. The ability to interact with visuals while data loads is significant because it is what enables users to engage in speed-of-thought analysis against massive and live data sources. When a user switches direction to explore different data, Self-Service Analytics efficiently cancels previously running queries to conserve computing and network resources.

The value of the Self-Service Analytics non-blocking user experience should not be underestimated. Because many studies suggest that the human attention span for most tasks is less than 10 seconds, it’s important that your users are not stuck staring at a blank screen or a waiting hourglass. True data exploration only happens when users can rapidly and freely decide to explore where the data leads.

<h2 id="self-service-report-microservice">
  Self Service Report Microservice
</h2>

The self service report microservice included in your environment, when [enabled](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables), supports a number of self-service analytics capabilities. To support these features, keep some performance details in mind.

* [Self Service Reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage): Users with appropriate permissions can create, edit, and send self service reports. If enabled, users can schedule and send reports to other users, or add them to a designated SFTP location.

  * Generate, export, and schedule delivery of PDF reports in a variety of page size and orientation formats.
  * Generate, export, and schedule delivery of reports in Excel (XLSX) format. These reports can include and support formatting and [conditional formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt-condt-format-using#configure-conditional-formatting).

* Scheduled Reports: Limit each scheduled report to fewer than 10 users, and plan time gaps between consecutive runs.

* Table visuals: Users with appropriate permissions can export table visuals in [Excel (XLSX) format](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-export-23#export-visual-data-in-excel-xlsx-format). These visuals can include and support formatting and [conditional formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt-condt-format-using#configure-conditional-formatting).

<h3 id="environment-configuration">
  Environment Configuration
</h3>

Before you [enable](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) the self service report microservice in production, work with your infrastructure team to provision appropriate resources. The microservice requires [dedicated memory allocation](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configure-memory-settings) and can scale with additional pods to accommodate concurrent user load and report complexity.

The name of this service, when installing from bootstrap, is `report-service`.

<h3 id="performance-considerations">
  Performance Considerations
</h3>

Report generation and export performance varies significantly based on report complexity and export format. The following guidelines are provided to help you plan your deployment and use.

Performance expectations noted here are based on internal testing we performed across three report service pods. Your results may vary based on [resource allocation](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configure-memory-settings) and concurrent user load.

In general, test your typical use report configurations thoroughly before deploying at scale.

<h4 id="report-type-performance">
  Report Type Performance
</h4>

These guidelines are based on the report service running across three pods, with a memory request of 6 Gi and limit of 9 Gi, on one CPU core. Structure your environment to accommodate your reporting needs.

* Simple grouped reports are the best performers across both PDF and Excel (XLSX) formats.
* Simple reports perform well in PDF format; response times increase substantially with more complex datasets. XLSX is more resilient than PDF for simple reports.
* Keep your header and footer image sized between 200kb and 500kb for optimal rendering performance.
* The maximum generated report file size is 50 MB. Validate with test runs before you put large conditionally-formatted reports into production.
* Structured reports are the most resource-intensive type. Excel (XLSX) exports for structured reports average a few minutes and are not recommended for high-throughput or user-facing scenarios.

#### Conditional Formatting

[Conditional formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt-condt-format-using#configure-conditional-formatting) increases report generation time significantly. A report with conditional formatting can take from twice as long to significantly longer than an equivalent report without it. Conditional formatting in complex reports exported to PDF format place a higher load on your environment, resulting in a percentage of error rates.

<h4 id="file-size-and-media">
  File Size and Media
</h4>

Keep in mind when designing your reports the limitations we built in to optimize performance, and guidelines users should follow for designing and formatting their reports.

* Generated report file size is capped at 50 MB.
* Keep header and footer images in the 200 KB–500 KB range.

#### Landscape Orientation Considerations

* Reports generated in landscape orientation accommodate more columns per page. This requires additional write operations and memory allocation when compared to portrait, and can result in measurable performance impact.
* Due to the increased demands of landscape oriented reports, test landscape configurations in your environment before you deploy them to production.
* Landscape orientation combined with conditional formatting brings the highest load. Explore alternative configurations or expand the resources available to the self service report microservice.

### Scheduling and Distribution

When you enable scheduled reports for your users, keep these operational limits in mind.

* Scheduled reports should be limited to a maximum of 10 recipients per report. Leave adequate time gaps between consecutive scheduled runs.
* Stagger report schedules to avoid concentration of export operations during the same time window.

## Developer Resources

The following topics provide information about the developer resources available in Self-Service Analytics.

* [Upgrade Self-Service Analytics with Custom Applications](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server#upgrade-self-service-analytics-with-custom-applications)
* [Get Started with the Self-Service Analytics Application Framework](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/application-framework/getting-started-with-the-application-framework)
* [REST API Overview](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/rest-api/restapi-overview2)
* [Manage Custom Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-managing)
* [Manage User Interface Themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov)
* [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov)
* [White Label the Self-Service Analytics Interface](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/customizing-ui#white-label-the-self-service-analytics-interface)

<h2 id="self-service-analytics-microservice-name-reference">
  Self-Service Analytics Microservice Name Reference
</h2>

The following table lists the Self-Service Analytics microservices. The order in which microservices should be started is described in [Microservice Startup Order](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#microservice-startup-order).

| Microservice Name | Description |
| - | - |
| `zoomdata` | The primary microservice for the Self-Service Analytics server. |
| `zoomdata-admin-server` | The [Service Monitor](#service-monitor-microservice) microservice. |
| `zoomdata-config-server` | The [configuration](#configuration-microservice) microservice. |
| `zoomdata-consul` | The Service Discovery microservice. |
| `zoomdata-data-writer-mssql` | The [Data Writer](#data-writer-microservice) microservice (using an MSSQL metastore). |
| `zoomdata-report-service` | The [self service reports](#self-service-report-microservice) microservice. Also used to support expanded data export options. |
| `zoomdata-data-writer-postgresql` | The [Data Writer](#data-writer-microservice) microservice. |
| `zoomdata-edc-apache-solr` | The [Apache Solr connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) microservice. |
| `zoomdata-edc-bigquery` | The [BigQuery connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) microservice. |
| `zoomdata-edc-cloudera-search` | The [Cloudera Search connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) microservice. |
| `zoomdata-edc-dremio` | The [Dremio connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) microservice. |
| `zoomdata-edc-drill` | The [Apache Drill connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) microservice. |
| `zoomdata-edc-elasticsearch-7.0` | The [Elasticsearch 7.0 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) microservice. |
| `zoomdata-edc-elasticsearch-8-0` | The [Elasticsearch 8.0 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) microservice. |
| `zoomdata-edc-hdfs` | The [HDFS connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) microservice. |
| `zoomdata-edc-hive` | The [Hive connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) microservice. |
| `zoomdata-edc-impala` | The [Cloudera Impala connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) microservice. |
| `zoomdata-edc-managed` | Dundas BI (Managed) connector microservice . The user interface to interact with this connector must be enabled. See [Server-Level Variables](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables). |
| `zoomdata-edc-memsql` | The [MemSQL connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) microservice. |
| `zoomdata-edc-mongo` | The [MongoDB connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) microservice. |
| `zoomdata-edc-mssql` | The [Microsoft SQL Server connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) microservice. |
| `zoomdata-edc-mysql` | The [MySQL connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) microservice. |
| `zoomdata-edc-oracle` | The [Oracle connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) microservice. |
| `zoomdata-edc-phoenix-4.7` | The [Apache Phoenix 4.7 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) microservice. |
| `zoomdata-edc-phoenix-4.7-queryserver` | The [Apache Phoenix Query Server 4.7 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) microservice. |
| `zoomdata-edc-postgresql` | The [PostgreSQL connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) microservice. |
| `zoomdata-edc-redshift` | The [Amazon Redshift connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) microservice. |
| `zoomdata-edc-rts` | The [Real-Time Sales connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) microservice. |
| `zoomdata-edc-s3` | The [Amazon S3 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) microservice. |
| `zoomdata-edc-saphana` | The [SAP Hana connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) microservice. |
| `zoomdata-edc-saphanacloud` | The [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) connector microservice. |
| `zoomdata-edc-sapiq` | The [SAP IQ connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) microservice. |
| `zoomdata-edc-snowflake` | The [Snowflake connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) microservice. |
| `zoomdata-edc-sparksql` | The [Spark SQL connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) microservice. |
| `zoomdata-edc-teradata` | The [Teradata connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) microservice. |
| `zoomdata-edc-tibcodv` | The [TIBCO DV connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) microservice. |
| `zoomdata-edc-trino` | The [Trino connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) microservice. |
| `zoomdata-edc-vertica` | The [Vertica connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) microservice. |
| `zoomdata-postgres` | The [metadata repository](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#metadata-repository). |
| `zoomdata-query-engine` | The [query engine](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#manage-the-self-service-analytics-query-engine) microservice. |
| `zoomdata-screenshot-service` | The [Screenshot](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/screenshot-install) microservice. |

<h2 id="self-service-analytics-metadata-stores">
  Self-Service Analytics Metadata Stores
</h2>

Self-Service Analytics uses the following metadata stores:

| Store Name | Description |
| - | - |
| zoomdata | Stores Self-Service Analytics metadata. This is the primary metadata store for Self-Service Analytics. |
| zoomdata-config | Stores metadata associated with the Self-Service Analytics [configuration microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#maintain-application-properties). This store name is also configurable. |
| zoomdata-keyset | Stores [keyset](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview) data. |
| zoomdata-upload | Stores flat files that have been uploaded using the [flat file connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file). |

<h2 id="self-service-analytics-administration">
  Self-Service Analytics Administration
</h2>

Self-Service Analytics makes visual analytics easy for end users. Self-Service Analytics administrators are a big part of that. This docs portal will help you install, configure, maintain, and upgrade Self-Service Analytics.

<h3 id="how-do-i-administer-self-service-analytics">
  How Do I Administer Self-Service Analytics?
</h3>

Self-Service Analytics is much like any installed software in that the administrator manages the software's life-cycle. Some tasks need to be done only when you start out or want to upgrade Self-Service Analytics.

* Read the [Self-Service Analytics overview](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/welcome).
* [Install Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov).
* [Configure Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).
* [Upgrade Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server) to a new version.
* [Manage Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs) microservices.

<Warning>
  Self-Service Analytics uses a packaged PostgreSQL database instance to store its metadata. Use the provided instance due to the specific configuration and version combination:
</Warning>

* Self-Service Analytics 26.3 and later: PostgreSQL 16

If you would like to use another PostgreSQL instance, contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for further guidance.

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

You do other tasks only as needed.

* Configure a [high availability](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/distenv-ov#configure-a-high-availability-environment) environment.
* [Manage connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers) and [data source configurations](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview).
* [Create custom metrics and derived fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics).
* Manage [tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage), [groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#manage-user-groups),and [users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage).
* Manage [activity logging](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/activity-logging).
* [Start](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices) and [stop](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#stop-microservices) the Self-Service Analytics microservices.
* [Uninstall Self-Service Analytics.](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/uninstall)

You will need to do some maintenance tasks at regular intervals.

* [Review activity logs.](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/activity-logging#manage-activity-logs)

## Reference Information

The following topics provide reference material useful for managing and using Self-Service Analytics.

* [Self-Service Analytics Microservice Name Reference](#self-service-analytics-microservice-name-reference)
* [Microservice Startup Order](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#microservice-startup-order)
* [Self-Service Analytics Metadata Stores](#self-service-analytics-metadata-stores)
* [Self-Service Analytics Log Files Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging#self-service-analytics-log-files-reference)
* [Default Port Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/port-reference)
* [Application Configuration Object](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/application-framework/getting-started-with-the-application-framework#application-configuration-object)
* [Query Configuration Object](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/application-framework/getting-started-with-the-application-framework#query-configuration-object)
* [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference)
* [Visual Type Configuration Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-config)
* [Self-Service Analytics Visual Metrics and Attributes Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/application-framework/getting-started-with-the-application-framework#self-service-analytics-visual-metrics-and-attributes-reference)
* [Supplied Color Palettes](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/colors#supplied-color-palettes)
* [Operators](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#operators)
* [State Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/country-name-reference#state-name-reference)
* [Country Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/country-name-reference)
* [Preset Time Ranges](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#preset-time-ranges)
* [Errors and Exceptions](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/errors-and-exceptions)
* [Events Created by Client](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/application-framework/getting-started-with-the-application-framework#events-created-by-client)
* [Cautionary Note About Internal APIs](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/rest-api/restapi-overview2#cautionary-note-about-internal-apis)
