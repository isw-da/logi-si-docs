> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction to Simba Self-Service Analytics 26

Designed specifically for software teams, Simba Self-Service Analytics delivers the first out-of-the-box development experience for embedded analytics. Choose Self-Service Analytics for:

* Its [effortless authoring paradigm](#effortless-authoring) empowers developers to easily create, customize and embed data visualizations with complete control over the end user experience.
* The [self-service embed](#embedded-self-service) with a visualization can be tailored and configured to match the skill level of your end users, while enabling them to modify and share their own visualizations.
* Its internal [query engine (z-Engine) and smart data connectors](#query-engine-and-smart-data-connectors) unlock unmatched modern data connectivity and query performance while also working with your existing tech stack.
* Its cloud-ready [microservices architecture](#microservices-architecture) provides you with elastic scale so that your CFO loves you and your DevOps team respects you.

<Warning>
  Self-Service Analytics is released on a quarterly schedule. See [Self-Service Analytics Release Vehicles and Third Party End of Life Policy](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#self-service-analytics-release-vehicles-and-third-party-end-of).
</Warning>

<Danger>
  Older license keys may not be not compatible with this product. If you are upgrading from an older Composer or Symphony release, see [Request and Apply a New License Key](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/license-request).
</Danger>

If you are already familiar with Self-Service Analytics and want to read up on the latest updates, see: [Simba Self-Service Analytics Release Notes 26.3](/simba-embedded-analytics/docs/self-service-analytics/26.3/release-notes/ssa-rn-26-3). For information about hardware and software requirements for Self-Service Analytics, see [System Requirements](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#system-requirements) and [Supported Technologies Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#supported-technologies-reference).

For information about the Postgres metadata repository that Self-Service Analytics uses to store definitions and settings, see [Metadata Repository](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#metadata-repository).

For information about the job skills necessary to use Self-Service Analytics, see [Personas](#personas).

<h2 id="effortless-authoring">
  Effortless Authoring
</h2>

Self-Service Analytics's effortless authoring allows your developers to avoid heavy data modeling using a data authoring workflow that streamlines data connectivity, preparation and enrichment. You can rapidly build embedded analytics content with an easy-to-use visual authoring workflow and create a persistent look and feel by seamlessly embedding analytics into your application with custom themes and extensibility that goes beyond just colors and styling.

You can build visuals once and reuse them to populate multiple dashboards, eliminating the need to recreate them over and over again. Finally, you can enjoy the ultimate end user control that a complete embedded analytics development environment provides to develop and manage content directly in your existing application’s workflow.

See also:

* [Configurable Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#configurable-data-sources)
* [Configurable Data Visualization](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis)
* [Product Customizations](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#product-customizations)
* [Web-Based User Interface](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#web-based-user-interface)

<h2 id="embedded-self-service">
  Embedded Self-Service
</h2>

<h3 id="self-serve-business-intelligence">
  Self-Serve Business Intelligence
</h3>

Using Self-Service Analytics's embedded self-service, your end users will enjoy the freedom to securely collaborate and share content on-demand or with automated scheduled delivery.

While other products take a one-size-fits-all approach, we empower your application teams to embed and customize end user self-service with embedded visualizations. Granular controls allow you to define levels of end user self-service and dashboard interactivity at the feature level. Precise controls over end user data access and governance ensure a secure discovery experience. You can provide end users with the freedom to visually author analytic content and perform ad hoc analysis all within your application.

In addition, [Data DVR](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#data-playback-and-live-mode) enables your end users to explore and interact with embedded content, including play, rewind, pause and fast forward of raw data and charts.

See also:

* [Embeddable Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#embeddable-analytics)
* [Data Playback and Live Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#data-playback-and-live-mode)

## Query Engine and Smart Data Connectors

Respecting the uniqueness of data stores, the internal query engine (also called z-Engine) and smart data connectors allow you to explore SaaS scale data sets with speed and scale including relational, NoSQL, multisource and other non-traditional data stores.

The query engine analyzes and optimizes queries and pushes processing down to the data store to enable the processing of thousands of concurrent user requests. Its data fusion technology empowers multisource analysis that allows end users to easily interact with visualizations from multiple data sources by virtually combining them so they appear to be from a single source.

Our broad set of smart data connectors for modern data stores such as search engines, streaming, and cloud data warehouses let you access all your data without the need to move or prepare the data in advance. Self-Service Analytics uses your existing data infrastructure and security framework, eliminating the need for redundant technology investments and ongoing maintenance efforts by your team.

See also:

* [Query Engine Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#query-engine-microservice)
* [Data Connector Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#data-connector-microservices)
* [Multisource Analysis](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#multisource-analysis)
* [Security](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#security)
* [Data Protection Policy](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode#data-protection-policy)

<h2 id="microservices-architecture">
  Microservices Architecture
</h2>

Self-Service Analytics's microservice architecture is comprised of code that is adaptable and extensible. It runs on a wide variety of modern data platforms and architectures. It allows data store connectivity to run independently from the query engine and it allows you to build, deploy, and automate at cloud speed.

The horizontal scale provided with distributed microservices helps you avoid single points of failure and assures high availability with no proprietary hardware required. This elastic scale lets you optimize computer resources and avoid waste by scaling up and down resources such as CPU process power and RAM when and where you need it.

See also:

* [Microservices Architecture](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice)
* [Distributed Environment Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/distenv-ov)
* [Flexible Deployment](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#flexible-deployment)

<h2 id="personas">
  Personas
</h2>

The successful implementation and use of requires the completion of tasks that require different job skills. Whether these tasks are performed by one person or by more than one person varies by organization. This topic describes the different skills needed.

* Somebody with the authorization and skills to install the software as a standalone product, in a high availability environment, or behind a load balancer. This person must understand your server and database infrastructure. Typically, this is someone in Operations.

* Somebody who manages licensing of the product.

* One or more people to manage product security, including:

  * Your organization's authentication tools (X.509, SAML, Kerberos, or LDAP) and their integration into Self-Service Analytics
  * The tenant accounts, users, and groups required by your organization.

* One or more people to manage configuration of the product. Among other things, configuration can include tasks such as setting up logging, creating and managing custom charts and admin-defined functions, or tailoring the theme and other features of the UI as needed by your organization. Typically, this would be a system developer.

* Somebody who manages the connectors and connector server definitions needed by for your data stores. This person would also create the connection definitions needed to access those data stores. Typically, this is a database administrator.

* Somebody to define data source configurations from the data available in your data stores. This person must understand the data in your data stores and how it will be used. They must also understand who should have access to the data in each data source and whether access should be controlled by column or row. This person may be referred to as a *data author*.

* One or more people who can create meaningful dashboards and visuals that help your organization analyze the data you have collected. These people need to be able to specify who should have access to the dashboard data and the dashboard functions available for end users to interact with after the dashboard is embedded in your application. This person may be referred to as a *content author*.

* One or more people to embed your dashboards into your applications. Typically, this is an application developer.

<h2 id="get-started-with-self-service-analytics-26">
  Get Started With Self-Service Analytics 26
</h2>

The following steps guide you through the process of installing and configuring the Self-Service Analytics platform and provides an overview of developing embeddable content. In addition, read [Personas](#personas) for a descriptions of the different job skills that contribute to the successful implementation and use of your software.

Some of the setup work described below requires use of the Self-Service Analytics API.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<AccordionGroup>
  <Accordion title="1. Product Installation">
    1. Verify you have a server environment available that meets the sizing requirements of Self-Service Analytics. See [Server Size Guidelines](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#server-size-guidelines), [System Requirements](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#system-requirements), [Plan Your Installation](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites) and [Supported Technologies Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#supported-technologies-reference).
    2. Install using the supplied bootstrap script. See [Installation Steps](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#installation-steps). Optionally, install the product and its metadata store manually (see [Install Self-Service Analytics Manually](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#install-self-service-analytics-manually)).
    3. Optionally, configure servers in a distributed environment (either a load balanced environment or a high availability environment). See [Distributed Environment Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/distenv-ov).
    4. License the product, if a new license is required. See [Request and Apply a New License Key](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/license-request).
  </Accordion>

  <Accordion title="2. Product Security and Authorization">
    1. Integrate with your security software (LDAP, SAML, Kerberos, or X.509). See [Supported Authentication Tools](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/authorization-tools).
    2. Set up tenants, users, and groups, with appropriate privileges. See [Authorize Self-Service Analytics Access for Users in Groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov).
    3. Define custom attributes, as needed, for each user. Custom attributes provide a way for administrators to create variables in user definitions. These variables can be interpolated in other fields elsewhere in the product. See [Specify Custom User Attributes](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#specify-custom-user-attributes).
  </Accordion>

  <Accordion title="3. Data Store Connector and Connection Configuration">
    1. Log in as the supplied [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) (System Administrator) or a member of the Supervisors group and set up the connectors needed to support the data stores your organization uses and that you will want to use for data source configurations. See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers).
    2. Log in as an administrator and define the connection strings necessary for the connectors to access your data stores. See [Create and Manage Data Store Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing).
  </Accordion>

  <Accordion title="4. Product Configuration">
    1. Activate logging. (regular -- Fluentd optional) See [Activity Logging](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/activity-logging), [Manage Activity Logs](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/activity-logging#manage-activity-logs), and [Set Up Unified Logging Using Fluentd](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging).
    2. Optionally, create custom charts needed by your organization. [Manage Custom Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-managing).
    3. Optionally, create admin-defined functions needed for your environment. [Admin-Defined Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/admin-fx-ov).
    4. Optionally, configure a different theme for the your environment's UI. See [Manage User Interface Themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).
    5. Optionally, customize the UI for your environment. See [Customize the User Interface](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/customizing-ui).
  </Accordion>

  <Accordion title="5. Data Authoring">
    1. Identify the data you need to use from your data stores to perform the data analytics you want.
    2. Define data source configurations that collect the data you need. Data source configurations use the data store connections previously defined. See [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview).
    3. Optionally, configure row and column security for your data sources. See [Restrict Access to Data Using Row and Column Security](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-security-row) and [Restrict Access to Fields Using Column Security](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-security-row#restrict-access-to-fields-using-column-security).
    4. Optionally, configure permissions for each data source. See [About Source Permissions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions).
  </Accordion>

  <Accordion title="6. Visual, Dashboard, and Report Creation">
    1. Configure visuals, dashboards, and enable reports your users need to analyze your data. See [Visuals Work Areas](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup), [Dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage), and [Self Service Reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage).
    2. Optionally, configure permissions for each dashboard. See [About Dashboard and Self Service Report Permissions](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-auth-permissions#about-dashboard-and-self-service-report-permissions).
    3. Optionally, specify how each visual can be interacted with when embedded. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).
    4. Optionally, share dashboards with other users in your tenant. See [Share a Dashboard or Self Service Report with Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-share-withinacct).
    5. Optionally, export a dashboard or report. See [Export Dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import#export-dashboards) and [Export Your Self Service Report](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage#export-your-self-service-report).
    6. Optionally, schedule a self service report or dashboard report. See [About Scheduled Reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule).
  </Accordion>

  <Accordion title="7. Dashboard Embedding">
    1. Set up Trusted Access and register your application as a client. See [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov).
    2. Embed dashboards or self service reports in your applications. See [Embed Components Into Your Application](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed/dash-embed).
    3. Optionally, enable embedded dashboard access from other sites using cross-origin sharing (CORS). See [Enable Self-Service Analytics Component Access From Other Sites Using Cross-Origin Resource Sharing (CORS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#enable-self-service-analytics-component-access-from-other-sites).
  </Accordion>
</AccordionGroup>

The following additional topics may also be helpful.

* [Access and Use Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access)
* [Log Into the User Interface](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#log-into-the-user-interface)
* [Switch Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#switch-tenants)
* [Home Page](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#home-page)
* [About Dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#about-dialog)
