> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Configurable Data Visualization

You can visualize data from your data stores in visuals and dashboards in the Self-Service Analytics user interfaceI. A dashboard is a container for one or more visuals. The visuals in a dashboard do not have to be related, but for easier data analysis, probably should be. See [Multisource Analysis](#multisource-analysis).

Your data can be visualized using a wide variety of visual types: arc gauges, bar charts, box plots, donuts, heat maps, KPI charts, line charts, maps, pie charts, scatter charts, tables, tree maps, and word clouds are all supported. You can create variations of these visual types as well. For example, you can create standard bar charts, stacked bar charts, clustered bar charts, histograms, and multiple metric bar charts. See the [Self-Service Analytics Visual Metrics and Attributes Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/application-framework/getting-started-with-the-application-framework#self-service-analytics-visual-metrics-and-attributes-reference).

You can customize visuals in a variety of ways. When you define a data source configuration, you can specify some default global settings for visuals created using the data source. Read about the [Global Settings Work Areas](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab) of a configured data source.

After a visual is created, you and add it to a dashboard, and customize it in the following ways. Some of these customizations depend on the visual type you select or the data source (and visual types defined for the data source) used for the visual.

<table>
  <thead>
    <tr>
      <th>Customization</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Visual Colors</td>
      <td>You can change the colors used in the visual. See [Change Color Schemes](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/colors) and [Change the Visual Color Metric](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/colors#change-the-visual-color-metric).</td>
    </tr>

    <tr>
      <td>Re-Visualize (formerly *Visual Style*)</td>
      <td>You can re-visualize the data represented in a visual by changing the visual type. See [Re-Visualize (Change a Visual Type)](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/available-visual-types#re-visualize-change-a-visual-type).</td>
    </tr>

    <tr>
      <td>Names and Descriptions</td>
      <td>You can change the title and description of dashboards and visuals. See [Rename a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#rename-a-dashboard), [Descriptions](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save#descriptions), [Modify Visual Names, Display Names, and Descriptions](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save#modify-visual-names-display-names-and-descriptions).</td>
    </tr>

    <tr>
      <td>Data Sorting</td>
      <td>You can sort visual data. See [Sort and Limit Visual Data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/sortlimit-composer).</td>
    </tr>

    <tr>
      <td rowSpan={4}>Data Filtering</td>
      <td>You can filter visual data by specific field values or ranges. See [Filter Data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters).</td>
    </tr>

    <tr>
      <td>You can filter visual and dashboard data by time ranges using the time bar. See [Use the Time Bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar)</td>
    </tr>

    <tr>
      <td>You can filter visual data by unique data values stored in a keyset. See [Use Keysets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview).</td>
    </tr>

    <tr>
      <td>You can filter dashboard data by cross-source linked fields from different data sources. See [Use Cross-Source Links](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/using-cross-source-links).</td>
    </tr>
  </tbody>
</table>

In addition to these dashboard and visual configuration features, you can link dashboards and share dashboards with other users. You can also export visuals and dashboards in a variety of formats: PNG, PDF, CSV (visuals), XLSX (dashboards and visuals as raw data or visual data) and JSON (dashboards and visuals). When you export visuals and dashboards in JSON format, you can import them into other Self-Service Analytics environments running the same version of Self-Service Analytics. See [Dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage) and [Visuals Work Areas](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup).

Finally, you can change the look of the UI altogether using themes. See [Manage User Interface Themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).

<h2 id="configurable-data-sources">
  Configurable Data Sources
</h2>

Data queries in Self-Service Analytics use data sources you configure to identify the data needed and the data store from which it should be obtained. The Self-Service Analytics data source you configure defines the following settings:

| Setting | Description |
| - | - |
| connection definition | The connection string that should be used to connect to your data store. |
| data store table, index, or data to use | The table, index, or other data in your data store that should be collected when the data source is used in a Self-Service Analytics query. |
| data customizations | Any customizations you want made to the data collected from the data store. This can include customizations to the field names, types, partition settings, distinct count activation for the data, filter display customizations, and other configurations such as the time pattern or granularity used for time fields or the aggregation used for numeric fields. |
| derived fields and custom metrics | Any derived fields or custom metrics you want calculated from the data collected from the data store. |
| refresh schedule | The schedule by which the data collected from the data store is refreshed. Derived field and custom metric data is also refreshed on this schedule, after the data store data is updated. |
| time bar settings | The default time bar settings that should be used for visuals and dashboards created using the data source. |

For more information about creating and managing data source configurations, see [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview).

In addition to standard data source configurations, Self-Service Analytics provides methods of analyzing data from multiple sources at the same time, including the ability to fuse data sources. See [Multisource Analysis](#multisource-analysis).

<h2 id="embeddable-analytics">
  Embeddable Analytics
</h2>

Simba Self-Service Analytics was built for extensibility and for integrating business intelligence into other applications. Integrations can be used to pass context between applications and Self-Service Analytics as part of your workflow or data exploration experience.

There are several options for embedding analytics:

* White-label for rebranding Self-Service Analytics to display another organization’s logo, fonts, colors, etc. See [Product Customizations](#product-customizations).
* Data integration using the Self-Service Analytics API to run a query from your application and then display or use the data pulled by the query. The query definition is invoked by an *action* in the Self-Service Analytics UI and is based on the filters applied to a Self-Service Analytics visual and on the data and limit specifications in the application integration definition for the visual data source. The invoked action creates the query definition and sends it to your application. See [Integrate Visual Data Into Your Applications](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/actions-overview).

The behavior of visuals, dashboards, and reports when they are embedded into your applications is controlled by the interactivity settings for the visuals themselves. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

Our REST APIs use common design practices to be easily navigable by any user. The APIs are documented with Swagger, allowing for interactive experiences when conducting experimentation and testing.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<Warning>
  Some API endpoints are marked as `experimental` in the Swagger documentation we provide. These endpoints are in the early stages of design, and are subject to change. We make no commitment to their stability and may remove them without notice. These experimental endpoints are not recommended for use in production.
</Warning>

<h2 id="multisource-analysis">
  Multisource Analysis
</h2>

Most organizations have data stored in disparate systems for a variety reasons. Regardless of how the data is stored, you may need to combine it for clarity or to analyze the relationships between data stored in different systems.

Self-Service Analytics dashboards can contain many visuals, and each visual can depict data from a different data store. In addition, Self-Service Analytics offers more practical approaches to multisource analysis through data fusion, cross-source filtering, and keysets.

* Fusion combines multiple data sources using one or more common keys so that they appear to be from a single source. The two most common reasons for using data fusion are to enrich or provide clarity to the data. One simple example is to use fusion to look up labels or other attributes. Depending on the size of the data being fused, data fusion can be resource-intensive. See [Fuse Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview).
* Cross-source filtering allows business you to quickly apply common filters across visuals that are populated by different data sources. Cross-source filtering simplifies and accelerates exploration when a dashboard contains data that is logically related but physically in different systems. See [Use Cross-Source Links](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/using-cross-source-links).
* Keysets are an innovative way to perform multipass data analysis without requiring IT or developer intervention. You can simply create a keyset from one visual and apply that keyset as a filter on other visuals. Keysets can be applied to any visuals, and are usable across all data sources. See [Use Keysets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview).

<h2 id="data-playback-and-live-mode">
  Data Playback and Live Mode
</h2>

There is one common attribute to all data streams: time. Any data source that has a date-time field can be playable in the Self-Service Analytics time bar (Data DVR). Historical data can be played back visually, just like replaying a movie. Data sources that host frequently updated data can be configured to play data in live mode. In live mode, Self-Service Analytics uses internal markers to automatically push incremental updates to visuals. Live mode updates are configurable for all levels of granularity available in your data source: from as frequently as once a second, to once a minute, hour, or day, to broader time frames, such as 30, 90, 180, or 365 days.

You do not need to force expensive full query refreshes, and since only newly arrived data is pushed to your visuals, network and other resources are conserved. Self-Service Analytics's built-in live mode functionality increases productivity and overall user satisfaction when working with very large and rapidly updated data.

Like Data Sharpening, the time bar streams data to the user over WebSocket connections. Within your WebSocket connection, Self-Service Analytics multiplexes commands from each visual over that connection so each visual's query request results in its own virtual communication channel that receives data streaming in one direction, and sends control commands, such as changing playback speed, pausing, or flipping the time window in the other direction.

For more information, see [Live Mode and Historical Playback](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#live-mode-and-historical-playback).

<h2 id="product-customizations">
  Product Customizations
</h2>

You can customize Self-Service Analytics in the following ways.

<table>
  <thead>
    <tr>
      <th>Customization</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Custom charts</td>

      <td>
        We provide APIs that use web standards such as HTML, CSS, and JavaScript to expand the number and type of visuals available to you. The use of web standards allows developers to leverage popular JavaScript libraries to build custom charts, and then integrate them directly into dashboards.

        <br />

        Custom charts make use of the same query engine that powers standard visuals. Data connectors, microqueries with Data Sharpening, and live mode are all available with custom charts.

        <br />

        Custom charts are built using the Command Line Interface (CLI). The custom chart CLI offers a flexible environment for creating, managing, and deleting custom charts without being connected to the client application. The CLI tool uses `Node.js` and is installed locally via `npm`. After it is installed and configured, the CLI behaves much like any other command line tool.

        <br />

        See [Manage Custom Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-managing).
      </td>
    </tr>

    <tr>
      <td>Custom connectors</td>
      <td>See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers).</td>
    </tr>

    <tr>
      <td>Derived fields</td>

      <td>
        Derived fields extend each row with additional attributes or metric fields that can be used in filters and aggregations. Derived fields can be complex or as simple as concatenating text strings, such as first and last names. A full editor is available to simplify the development of complex row level expressions (RLE). Derived fields can be used in the creation of other derived fields and custom metrics.

        <br />

        See [Maintain Derived Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields).
      </td>
    </tr>

    <tr>
      <td>Custom metrics</td>

      <td>
        Custom metrics are used to perform complex math across rows and at various levels of aggregation such as grand totals and grouped subtotals. For example, you can define custom metrics that calculate percentages of total values. Custom metrics are retained as formulas and can be used in other custom metrics.

        <br />

        See [Maintain Custom Metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics).
      </td>
    </tr>

    <tr>
      <td>Custom interactivity</td>

      <td>
        Interactivity settings can be applied to visuals to control how users interact with a visual and, more specifically, how users can interact with the visuals after they are embedded in other applications.

        <br />

        See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).
      </td>
    </tr>

    <tr>
      <td>Admin-defined functions</td>

      <td>
        This software provides a set of functions that you can use in expressions to build derived fields or custom metrics. However, you can use your own functions (for which there is no equivalent) to extend your data analytics. Examples of this might be functions available within your data store either natively or as user-defined functions.

        <br />

        See [Admin-Defined Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/admin-fx-ov).
      </td>
    </tr>

    <tr>
      <td>UI white labeling and customization</td>

      <td>
        When you install Self-Service Analytics, default UI settings are applied. Manage links to help content, customize copyright info, the default logo, and change or remove the link to terms of use. To match the style of your company, you can also upload a custom *.css* file to modify the default skin.

        <br />

        See [Customize the User Interface](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/customizing-ui) and [White Label the Self-Service Analytics Interface](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/customizing-ui#white-label-the-self-service-analytics-interface).
      </td>
    </tr>

    <tr>
      <td>Themes</td>

      <td>
        When you install or upgrade to version 26.2 or later, five themes are provided. You can switch to (activate) a different theme when needed using the provided API.

        <br />

        * Two of these themes fully support color and customization for environments that enable the `enhanced-experience` user interface toggle: `d+a_light` and `__platform__` (for environments [transitioning from Symphony](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/transition-sym) that previously used the platform theme).
        * Three themes support the classic experience from earlier releases: **composer**, **modern** (light) and **dark**. The **composer** theme is used by default in v26.3 and earlier releases when you install v26.3 or upgrade to v26.3 to ease the transition.

        <br />

        See [Manage User Interface Themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov)
      </td>
    </tr>
  </tbody>
</table>

<h2 id="flexible-deployment">
  Flexible Deployment
</h2>

Self-Service Analytics microservices and related components can be deployed on-premise, in the cloud, or in hybrid environments, provided that the host server meets [operating system and hardware requirements](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites). Additionally, Self-Service Analytics can query supported data sources in the cloud or on-premises, provided network-level connectivity exists between the host and the data store. As a best practice, SSL should be used on connections between Self-Service Analytics and a data store, especially when traversing network enclaves.

As a Java web application, Self-Service Analytics can meet increasing user concurrency requirements through horizontal scaling. Horizontal scale-out is achieved by replicating Self-Service Analytics behind a load balancer with a common metadata store for all nodes. This configuration also provides a higher degree of application availability, as traffic will be routed to healthy nodes in the event of an application or hardware failure on another node.

As the Self-Service Analytics microservices architecture matures, more microservices will be deployed independently for greater availability and optimized load management.

## Distributed Environment Support

You can deploy Self-Service Analytics microservices in a distributed environment. Such an environment ensures that you can minimize the downtime caused by:

* hardware or software failures due to excessive resource use or other events
* software upgrades or updates

You have two options for setting up a distributed Self-Service Analytics environment:

* **Load balancing:** Load balancing helps you scale Self-Service Analytics for hundreds of users. You can use load balancing both on-premises and with cloud deployments. A single set of microservices communicate with each other in a monolithic flow.

  For more information, see [Configure the Self-Service Analytics Server Behind a Load Balancer](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/distenv-ov#configure-the-self-service-analytics-server-behind-a-load).

* **High Availability:** A high availability environment includes multiple Self-Service Analytics nodes, each with its own set of microservices. This ensures that a microservice is available at all times, somewhere in the cluster. Each microservice communicates with others using service discovery.

  Different numbers of different types of microservices can be defined for the Self-Service Analytics nodes, although at least two of each must be installed.

  A high-availability load balancer is required to distribute the network traffic across your user-facing Self-Service Analytics nodes. If only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Self-Service Analytics nodes behind it if the load balancer should fail. Microservice load balancing and failover occur automatically within the Self-Service Analytics nodes themselves.

  For more information, see [Configure a High Availability Environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/distenv-ov#configure-a-high-availability-environment).

If you have the configuration microservice configured and running, you can maintain properties for microservices of a given type in a single location in the Service Monitor. For example, if you have two query engine microservices running in your high availability environment, you can change the properties for both microservices in a single location, ensuring that the query engine microservices operate in the same manner across the product nodes. A `config-server-upload.jar` utility is provided that can be used to migrate the microservice properties from your standalone Self-Service Analytics servers to the Self-Service Analytics configuration data in the high availability PostgreSQL data store, where the configuration microservice can maintain them. For more information see [Migrate Properties to the Configuration Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/distenv-ov#migrate-properties-to-the-configuration-server).

<h2 id="security">
  Security
</h2>

Self-Service Analytics provides robust data security that ensures the "three As" of security -- proper [authentication](#authentication), [authorization](#authorization), and [accounting](#accounting) of the visual analytics environment. Additionally, its architecture provides [inherent data security](#inherent-data-security).

<h3 id="authentication">
  Authentication
</h3>

Administrators can manage access to the application by creating user accounts in Self-Service Analytics, or by synchronizing with an authentication identity provider (idP) to take advantage of centralized user management and authentication.

Self-Service Analytics adheres to standards-based methods for defining and enforcing security. This includes [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov), a default in-house developed security methodology that allows for machine-to-machine authorization of Self-Service Analytics resources when embedded in your application, using delegated authorization.

Other supported standard authentication protocols include Kerberos (SPNEGO), X.509, and SAML2 for single sign on, along with plug-ins for LDAP and SAML2 IdPs to facilitate user and permissions verification. Where available, Self-Service Analytics can authenticate as a microservice using Kerberos or LDAP on connections to data sources.

<h3 id="authorization">
  Authorization
</h3>

Self-Service Analytics's authorization security model allows administrators to configure user access to data sources, attributes, and records. Fine-grained access control is configured at the group level with permissions passed via inheritance to the groups members (users).

For data sources that support delegation, pass user credentials as a connection parameter. When enabled, the database authorization polices are enforced on queries so that they run with that user's privileges.

<h3 id="accounting">
  Accounting
</h3>

Advanced accounting permits logging of all data a user viewed while using Self-Service Analytics. This is performed by logging all WebSocket data transmitted to the user's browser. All user activity can be recorded in they Self-Service Analytics application logs in your instance.

<h3 id="inherent-data-security">
  Inherent Data Security
</h3>

Self-Service Analytics is inherently secure because there is no need to extract or move data out of secured platforms. Direct data connectivity, push-down processing, adaptive caching, Data Sharpening™, and standards-based authentication and authorization (including user delegation) make it possible to securely work with the most current data in your data stores. Restricting the movement of data is a critical requirement for organizations that must regulated and monitor access to sensitive information, and whose data is too big to move.

<h2 id="metadata-repository">
  Metadata Repository
</h2>

Metadata is any data that is used for the configuration and runtime operation of the Self-Service Analytics application, with the exception of customer-managed data stores. The metadata repository is simply the relational database instance containing the Self-Service Analytics schemas. The primary metadata schema includes configurations for:

* dashboards, visuals, and filters
* data store connectivity
* data source configurations and statistics
* enterprise authentication, accounts, users, groups, and permissions.

The metadata repository also contains separate schemas for storing raw data, which supports upload and keyset functionality. Note that the metadata schema definitions and the stored data are internal to the Self-Service Analytics application; they are not intended for direct manipulation.

Self-Service Analytics uses relational database technology for metadata storage, and ships with an open-source PostgreSQL database.

<Warning>
  Self-Service Analytics uses a packaged PostgreSQL database instance to store its metadata. Use the provided instance due to the specific configuration and version combination:
</Warning>

If you would like to use another PostgreSQL instance, contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for further guidance.

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

Internally, industry-standard technologies are used for database connectivity, object-relational mapping, and schema changes that are executed during Self-Service Analytics software upgrades. The database administrator can use well-known tools and procedures for backing up and restoring the entire metadata repository. The administrator is responsible for setting up authenticated access from the Self-Service Analytics server to the database.
