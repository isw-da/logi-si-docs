> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Self-Service Analytics Service Monitor

Self-Service Analytics includes a Service Monitor microservice, which can be used to:

* Review all Self-Service Analytics microservices and their log files.
* Produce a [diagnostics bundle](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support#download-the-diagnostics-bundle) to send to insightsoftware Support.
* Set the logging level and properties for each microservice.

<Note>
  Contact insightsoftware Support for assistance with the installation and use of the Service Monitor.
</Note>

Self-Service Analytics's Service Monitor provides administrators with real-time views of microservice health, configuration, and logs. The Service Monitor is not installed as part of a default Self-Service Analytics installation, so you must install and configure this before you can use it.

#### Prerequisites

* Self-Service Analytics and its microservices must be version 3.5 or later.
* All microservices must have service discovery enabled.
* The Self-Service Analytics Service Monitor must be manually installed, configured and started.

The following topics provide complete information about the Self-Service Analytics Service Monitor:

* [Install and Configure the Self-Service Analytics Service Monitor](#install-and-configure-the-self-service-analytics-service-monitor)
* [Access the Self-Service Analytics Service Monitor](#access-the-self-service-analytics-service-monitor)
* [Service Monitor Views](#service-monitor-views)
* [Download the Diagnostics Bundle](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support#download-the-diagnostics-bundle)
* [Maintain Application Properties](#maintain-application-properties)

<h2 id="access-the-self-service-analytics-service-monitor">
  Access the Self-Service Analytics Service Monitor
</h2>

After [installing the Service Monitor](#install-and-configure-the-self-service-analytics-service-monitor) and [restarting its microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices), you can navigate to its UI in a web browser using default port 8050. For example, if running locally, the Self-Service Analytics instance would be **[http://localhost:8080](http://localhost:8080)**, so the Service Monitor URL would be **[http://localhost:8050](http://localhost:8050)**. If your Self-Service Analytics instance is IP address URL 10.2.3.24, the Service Monitor URL would be **[http://10.2.3.24:8050](http://10.2.3.24:8050)**.

The user ID and password you should use to log into the Service Monitor are defined in properties you set up during the Service Monitor installation. See [Install and Configure the Self-Service Analytics Service Monitor](#install-and-configure-the-self-service-analytics-service-monitor).

<h2 id="service-monitor-views">
  Service Monitor Views
</h2>

The Self-Service Analytics Service Monitor UI includes the following views, each accessible via a menu option in the main menu on the Service Monitor UI page:

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-menu.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=791fafa02d983b117c034816a96c6bca" alt="" width="1897" height="69" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-menu.png" />

Each view is described below.

* [Wallboard View](#wallboard-view)
* [Applications View](#applications-view)
* [Journal View](#journal-view)
* [Downloads View](#downloads-view)
* [Properties View](#properties-view)

<h3 id="wallboard-view">
  Wallboard View
</h3>

The Wallboard view provides shows all the Self-Service Analytics microservice types used in your installation. You can access it by selecting the **Wallboard** menu option.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-wallboard.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=67ae99b0077040356e17b8fc9cc3a4ad" alt="" width="1895" height="896" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-wallboard.png" />

The Wallboard view shows how many instances of a Self-Service Analytics microservice are running and the length of time they have been running.

Select a microservice type to obtain detailed information about it. The detailed information available varies based on the microservice type, but may include metrics, health, environment, configuration properties, scheduled tasks, logging threads, audit log, and web mappings and HTTP traces for the microservice type.

<h3 id="applications-view">
  Applications View
</h3>

Select **Applications** to access the Applications view.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-appl.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=10810a4f89cae3f5f40a4d145ee5a711" alt="" width="1915" height="878" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-appl.png" />

The Applications view shows all the Self-Service Analytics microservice types used in your installation. It also identifies the instance URLs, and indicates how many instances there are of each and how long they have been running. If more than one instance of a microservice is running, you can expand the microservice type to see the specific instance URLs.

If you select the URL for a Self-Service Analytics microservice instance, you will launch the Self-Service Analytics UI for that instance. If you select the URL for a Service Monitor instance, you will launch the Service Monitor for that instance. If you select the URL for an instance of any other microservice, a page of metrics and other information appears for that instance of the microservice.

<h3 id="journal-view">
  Journal View
</h3>

Select **Journal** to access the Journal view.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-journal.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=c8a42f13e74b54eb3b72d10623774e75" alt="" width="1919" height="892" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-journal.png" />

The Journal view allows you to review the journal entries for each Self-Service Analytics microservice type.

<h3 id="downloads-view">
  Downloads View
</h3>

Select **Downloads** to access the Downloads view.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-downloads.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=4ca72d7e4e7850f52a0bae9b7fe50d12" alt="" width="1899" height="430" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-downloads.png" />

The Downloads view can be used to collect a diagnostics bundle for you to send to Self-Service Analytics Support when necessary. See [Download the Diagnostics Bundle](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support#download-the-diagnostics-bundle) for more information.

<h3 id="properties-view">
  Properties View
</h3>

Select **Properties** to access the Properties view.

This view allows you to review and maintain the properties for each of the other Self-Service Analytics microservices. It requires that the Self-Service Analytics configuration microservice be installed and started first. See [Maintain Application Properties](#maintain-application-properties).

<h2 id="install-and-configure-the-self-service-analytics-service-monitor">
  Install and Configure the Self-Service Analytics Service Monitor
</h2>

The Self-Service Analytics Service Monitor microservice is not installed as part of a default Self-Service Analytics installation. The microservice name is `zoomdata-admin-server`.

<Note>
  If you are installing Self-Service Analytics in a Windows environment, you can install the Service Monitor as part of running the initial bootstrap script. See [Install Self-Service Analytics - Windows](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-windows) and [Windows Bootstrap Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-windows#windows-bootstrap-reference).
</Note>

**Install, configure, and start the Service Monitor**

1. Open your SSH client.

2. Use the following command to install the Self-Service Analytics Service Monitor in a CentOS environment:

   ```bash theme={null}
   sudo yum install zoomdata-admin-server -y
   ```

   Use the following command to install the Self-Service Analytics Service Monitor in an Ubuntu environment:

   ```bash theme={null}
   sudo apt-get install zoomdata-admin-server
   ```

3. After the Service Monitor is installed, you must specify a user name and password in its properties file. The properties file is called `admin-server.properties` and can be found in the `/etc/zoomdata/` directory (Linux) or the `<install-path>/conf-modify/` directory (Windows). If the properties file is not there, create it. The properties that must be defined are:

   * `monitor.user.name=<username>`
   * `monitor.user.password=<password>`

   Edit the properties file with a text editor and substitute a Service Monitor user name for `<username>` and its associated password for `<password>`. The user name and password can be any user name and password you want.

   When you have finished, save the file.

4. Add the following properties to the `zoomdata.properties` file, located in the `/etc/zoomdata` directory (Linux) or the `<install-path>/conf-modify/` (Windows). These properties ensure that the Service Monitor has access to the Self-Service Analytics server actuator endpoints.

   * `actuator.user.name=<composer-admin-username>`
   * `actuator.user.password=<composer-pswd>`
   * `actuator.logging.external-file=<log-file-path>`

   Edit the properties file and substitute the valid user name and password of a Self-Service Analytics administrator for `<composer-admin-username>` and `<composer-pswd>`. If the default Self-Service Analytics log file path is not used for your installation, substitute your custom log file path for `<log-file-path>`. The default log file path is `/opt/zoomdata/logs/zoomdata.log` for Linux and `<install-path>/logs/zoomdata.log` for Windows.

   <Note>
     Setting these properties exposes valid Self-Service Analytics credentials as plain text in both the properties file and as tags in the Self-Service Analytics Consul. Anyone in your network with the ability to communicate directly with the Consul API or view the Consul UI will be able to see these values.
   </Note>

   When finished, save the file.

5. Start the microservice. For example, use the following command to start the Self-Service Analytics Service Monitor using `systemd` in a CentOS or Ubuntu environment:

   ```bash theme={null}
   sudo systemctl start zoomdata-admin-server
   ```

   See also [Start Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices).

<h2 id="maintain-application-properties">
  Maintain Application Properties
</h2>

After the Self-Service Analytics configuration microservice has been [configured](#configure-and-start-the-configuration-microservice) and started, you can use the [Properties tab](#properties-view) in the Service Monitor to maintain the configuration properties of Self-Service Analytics's other microservices. For information about specific Self-Service Analytics properties and property files, see [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).

**Maintain configuration properties using the Service Monitor**

1. Using a web browser, navigate to the Service Monitor for the Self-Service Analytics instance. Its default port is 8050. For example, if running locally, the Self-Service Analytics instance would be **[http://localhost:8080](http://localhost:8080)**, so the Service Monitor URL would be **[http://localhost:8050](http://localhost:8050)**. If your Self-Service Analytics instance is at IP address 10.2.3.24, the Service Monitor URL would be **[http://10.2.3.24:8050](http://10.2.3.24:8050)**.

   A login screen will appear.

2. Log into the Service Monitor using the Service Monitor user name and password you defined when the Service Monitor was installed. See [Install and Configure the Self-Service Analytics Service Monitor](#install-and-configure-the-self-service-analytics-service-monitor).

3. Select **Properties** on the main menu bar.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-menu.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=791fafa02d983b117c034816a96c6bca" alt="" width="768" height="28" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-menu.png" />

   The Properties page appears.

4. Select a Self-Service Analytics microservice in the **Service** drop-down list. The properties for the microservice are listed. The screenshot above lists all the properties in the `zoomdata.properties` file used by the `zoomdata` microservice.

   See [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference) for a list of Self-Service Analytics's microservices. If a microservice is not listed in the **Service** drop-down list, that Self-Service Analytics microservice is not yet set up to use the configuration server or the microservice is down.

5. Locate the microservice property in the list that you want to change.

   * The list of properties can be sorted alphabetically by key or value. Select the **Key** or **Value** list heading to sort the properties in ascending or descending order.
   * You can locate a property in the list by typing all or part of its name in the **Search** box at the top of the page.

6. Change the value of the property in the **Value** box associated with the microservice property you located.

   <Note>
     Be careful changing properties. Some properties should not be changed, except with the help of Self-Service Analytics [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support). The results of property changes could be unpredictable, if they are not made correctly.
   </Note>

   See [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files) for a list of the property files and links to descriptions of the properties for which changes are approved.

7. Select **Save Properties** to save your property changes.

8. Select **Apply Updates** to apply the property changes to your running Self-Service Analytics instance. Self-Service Analytics dynamically stops and restarts the appropriate Self-Service Analytics microservices.

<h2 id="use-the-configuration-microservice-to-maintain-application">
  Use the Configuration Microservice to Maintain Application Properties
</h2>

You can use the Service Monitor to review and maintain the properties for each of the other Self-Service Analytics microservices. It provides a centralized location where Self-Service Analytics configuration properties can be maintained. However, it requires that the Self-Service Analytics configuration microservice be configured and started first.

The Self-Service Analytics configuration microservice is packaged with the [Spring Cloud Configuration](https://www.baeldung.com/spring-cloud-configuration) server, which allows Self-Service Analytics to easily integrate with its Spring-based microservices and provides the mechanism by which Self-Service Analytics property settings can be persisted in a supported PostgreSQL metastore or in a GitHub repository. The following diagram depicts this relationship.

<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagrams/spring-cloud-config-server-relationship.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=25d54ed2b8f9b6f9973c5f86ce32dddc" alt="" width="2194" height="1112" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagrams/spring-cloud-config-server-relationship.png" />

After the Self-Service Analytics configuration microservice is installed and started, the properties can be maintained on the Service Monitor's Properties tab.

If you have the configuration microservice configured and running in a high availability environment, you can maintain properties for microservices of a given type in a single location in the Service Monitor. For example, if you have two query engine microservices running in your high availability environment, you can change the properties for both microservices in a single location, ensuring that the query engine microservices operate in the same manner across the product nodes. A `config-server-upload.jar` utility is provided that can be used to migrate the microservice properties from your standalone Self-Service Analytics servers to the Self-Service Analytics configuration data in the high availability PostgreSQL data store, where the configuration microservice can maintain them. For more information see [Migrate Properties to the Configuration Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/distenv-ov#migrate-properties-to-the-configuration-server).

See the following topics:

* [Set Up the Configuration Microservice Metadata Store or Repository](#set-up-the-configuration-microservice-metadata-store-or)
* [Configure and Start the Configuration Microservice](#configure-and-start-the-configuration-microservice)
* [Maintain Application Properties](#maintain-application-properties)

<h2 id="configure-and-start-the-configuration-microservice">
  Configure and Start the Configuration Microservice
</h2>

**Install, configure, and start the** Self-Service Analytics **configuration microservice**

1. Verify that you have set up a PostgreSQL metastore or a GitHub repository to store the property metadata. See [Set Up the Configuration Microservice Metadata Store or Repository](#set-up-the-configuration-microservice-metadata-store-or).

2. Open the SSH client associated with your instance.

3. Configure all installed and enabled microservices to use the configuration microservice. Run the following script:

   ```
   for i in $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}'|sed -e 's/\.service/.properties/g' -e 's/zoomdata\-//g');
   do
   echo "config-server.enabled=true">>/etc/zoomdata/$i;
   done
   ```

4. Each microservice supports two configuration properties related to the configuration microservice:

   * `config-server.enabled`: Enables or disables integration with the configuration microservice. Valid values are `true` (enable integration) and `false` (disable integration). The default is `true`.
   * `config-client.retry.max-attempts`: Sets the maximum number of attempts that should be made to connect to the configuration microservice. The default is 20. The Self-Service Analytics microservice will fail if the number of attempts to connect to the configuration microservice exceeds this value. This property is useful in situations where the configuration microservice starts with a delay. If your microservice fails while waiting for the configuration microservice and you want to give it more time, increase this value.

   Update these properties, as appropriate, for each microservice.

5. Install, enable and start the configuration microservice. Enter the following commands:

   ```bash theme={null}
   sudo yum install zoomdata-config-server \
   && systemctl enable zoomdata-config-server \
   && systemctl start zoomdata-config-server
   ```

   <Note>
     After starting the configuration microservice with a valid database configuration, the microservice should connect to the database and create a properties table.
   </Note>

6. Restart all the other microservices. Enter the following command:

   ```bash theme={null}
   sudo systemctl restart $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}')
   ```

   See also [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

<h2 id="set-up-the-configuration-microservice-metadata-store-or">
  Set Up the Configuration Microservice Metadata Store or Repository
</h2>

Before you can install and start Self-Service Analytics's configuration microservice, you must set up a PostgreSQL metastore or a GitHub repository to store Self-Service Analytics property metadata. A separate PostgreSQL database or a separate GitHub repository must be configured.

### PostgreSQL Database Setup Notes

**If you elect to persist property metadata to a PostgreSQL metastore:**

1. Configure a separate database and make it accessible to the connection user account:

   ```sql theme={null}
   CREATE DATABASE <composer-config> WITH OWNER <db_username>;
   ```

   where `<composer-config>` is the name of the PostgreSQL database and `<db_username>` is the connection user account name.

2. Add the following properties to the Self-Service Analytics `config-server.properties` file, located in the `/etc/zoomdata` directory:

   ```
   # metadata storage settings spring.datasource.url=jdbc:postgresql://localhost:5432/<composer-config> spring.datasource.username=<db_username> spring.datasource.password=<db_password>
   ```

   Substitute the connection user account name and password you set up in Step 1 for `<db_username>` and `<db_password>`. Substitute the name of the PostgreSQL database for `<composer-config>`.

3. Save the properties file. You will restart the configuration microservice when you configure it. See [Configure and Start the Configuration Microservice](#configure-and-start-the-configuration-microservice).

### GitHub Repository Setup Notes

**If you elect to persist property metadata to a GitHub repository:**

1. Add the following properties to the Self-Service Analytics `config-server.properties` file, located in the `/etc/zoomdata` directory:

   ```
   # metadata storage settings spring.cloud.config.server.git.uri=<repo_uri> spring.cloud.config.server.git.skipSslValidation=true spring.cloud.config.server.git.username=<repo_username> spring.cloud.config.server.git.password=<repo_password>
   ```

   Substitute the repository user account name and password for `<repo_username>` and `<repo_password>`. Substitute the URI of the repository for `<repo_uri>` (for example, `https://example.com/my/repo`).

   Additional and advanced configuration information can be found in [Spring.io's documentation](https://cloud.spring.io/spring-cloud-config/multi/multi__spring_cloud_config_server.html#_git_backend).

2. Save the properties file. You will restart the configuration microservice when you configure it. See [Configure and Start the Configuration Microservice](#configure-and-start-the-configuration-microservice).

<h2 id="self-service-analytics-monitoring-solution">
  Self-Service Analytics Monitoring Solution
</h2>

Self-Service Analytics system metrics are published by all microservices. While these measurements provide some visibility of the operating state of the services, the metric data becomes more useful once it can be stored and viewed. In order to provide Self-Service Analytics deployments with observability into the health and performance of the running system, you can use a monitoring solution. This topic describes an example monitoring solution that we make available for download with each release of Self-Service Analytics.

### Monitoring Solution Components

The monitoring solution consists of several components that are built up as layers.

* Generic operating and Self-Service Analytics specific metrics form the fixed foundation layer and are published in various formats.
* Subsequent layers provide storage and visualization capabilities to support further analysis.

<Note>
  Subsequent components added to the metrics foundation can be implemented as provided in the monitoring solution package, or you can substitute them with preferred components that were already deployed.
</Note>

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/composrmicro.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=95615d5e829223be379e7e6855f3b1a3" alt="Microsystem and Metrics solution diagram." width="601" height="460" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/composrmicro.png" />

The example solution is built using the following industry-standard, open-source tools:

1. Prometheus service collects and stores metrics in a time series database.
2. Grafana supports further analysis by providing visualization of stored metrics on pre-built application-specific dashboards.

We provide these components in a tarball containing docker-compose files. We include the configuration files required for monitoring Self-Service Analytics services, along with ready to use dashboards.

### Downloading and Installing the Solution Package

1. Contact your Customer Support representative to download the Solution Package: [Customer Support.](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support)

2. When you get the tarball, extract the tarball to the directory you create.

   ```bash theme={null}
   mkdir composer-monitoring tar -xvf composer-monitoring-X.Y.Z.tar.gz -C composer-monitoring
   ```

3. Open the READ.me file and follow the directions included.
