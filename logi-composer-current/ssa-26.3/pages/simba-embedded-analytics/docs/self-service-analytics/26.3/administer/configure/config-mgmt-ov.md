> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Self-Service Analytics

The Self-Service Analytics server uses multiple configuration files to ensure successful deployment of Self-Service Analytics in your operating environment. Each component has configuration files including a `<component_name>.properties` file and a `<component_name>.jvm` file.

Use the configuration files to make changes to the Self-Service Analytics server and how it functions. The configuration files need to be created after the Self-Service Analytics server has been installed to override Self-Service Analytics's default configuration. To modify the settings in these files, edit them in the `/etc/zoomdata` directory.

Every `<component_name>.jvm` file should include an `Xmx` JVM option to control the maximum heap memory limit for the application. See [Configure Memory Settings](#configure-memory-settings).

<h2 id="edit-a-configuration-file">
  Edit a Configuration File
</h2>

You can edit the properties for your Self-Service Analytics configuration in the configuration files. For a complete list of configuration files, see [Configuration Property Files](#configuration-property-files).

<Note>
  insightsoftware discourages changing properties in the `/opt/zoomdata/conf` directory (Linux) or `<install-path>/conf` (Windows). Copy the files you want to change to the `/etc/zoomdata` directory (Linux) or `<install-path>/conf-modify` (Windows) and change them there. This will ensure that your changes are not overwritten when Self-Service Analytics is next upgraded.
</Note>

Quickly determine what changes you have made to a properties file using `diff` in Linux. For example:

```bash theme={null}
diff /opt/zoomdata/conf/edc-<connector-name>.properties /etc/zoomdata/<edc-<connector-name>.properties
```

or

```bash theme={null}
diff /opt/zoomdata/conf/zoomdata.properties /etc/zoomdata/zoomdata.properties
```

For Windows environments, use your preferred diff utility to compare the differences between your original and updated property files.

Edit a Self-Service Analytics configuration file in Linux:

1. From your terminal, SSH to your Self-Service Analytics server.

2. Stop the appropriate Self-Service Analytics microservice (Self-Service Analytics, Screenshot, or the specific connector server).

   For the appropriate Linux command, see [Stop Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#stop-microservices).

3. Use the following command to access and open the configuration file:

   ```bash theme={null}
   vi /etc/zoomdata/<config-file-name>
   ```

   For example:

   ```bash theme={null}
   vi /etc/zoomdata/zoomdata.properties
   ```

   Names of valid configuration files are listed in [Configuration Property Files](#configuration-property-files).

   If the configuration file does not exist, this command creates it.

   <Note>
     If you are not logged in as a root user, then you need to enter `sudo vi /etc/zoomdata/zoomdata.properties` to create the desired file.
   </Note>

   Make sure the file is readable by the `zoomdata` microservice account.

4. Add the new variable or property into the file on a new line or edit an existing one, as needed. See:

   * [Properties Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference)
   * [zoomdata.jvm Options](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#zoomdata-jvm-options)
   * [Query Engine Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#query-engine-properties)
   * [screenshot-service.properties Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#screenshot-service-properties-properties)
   * [Connector Properties and Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files)

5. Save and exit the configuration file.

6. Restart Self-Service Analytics microservices.

   For the appropriate Linux command line, see [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

**Edit a Self-Service Analytics** **configuration file in Windows:**

1. Open the configuration file using a text editor that can edit Windows property files.

   Names of valid configuration files are listed in [Configuration Property Files](#configuration-property-files).

2. Stop the appropriate microservice or specific connector server.

   For the appropriate Windows commands, see [Windows Bootstrap Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-windows#windows-bootstrap-reference).

3. Add the new variable or property into the file on a new line or edit an existing one, as needed. See:

   * [Properties Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference)
   * [zoomdata.jvm Options](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#zoomdata-jvm-options)
   * [Query Engine Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#query-engine-properties)
   * [screenshot-service.properties Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#screenshot-service-properties-properties)
   * [Connector Properties and Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files)

4. Save and exit the configuration file.

5. Restart microservices.

Wait a few minutes for the microservice to restart completely, then open a new browser window to log back in. Confirm that your changes have taken effect.

<h2 id="configuration-property-files">
  Configuration Property Files
</h2>

Self-Service Analytics uses the configuration files in the following table to ensure successful deployment in your operating environment. You can edit many of the properties and options in these files. You can edit them in `/etc/zoomdata` as described in [Edit a Configuration File](#edit-a-configuration-file).

<Note>
  insightsoftware discourages changing properties in the `/opt/zoomdata/conf` directory (Linux) or `<install-path>/conf` (Windows). Copy the files you want to change to the `/etc/zoomdata` directory (Linux) or `<install-path>/conf-modify` (Windows) and change them there. This will ensure that your changes are not overwritten when Self-Service Analytics is next upgraded.
</Note>

Quickly determine what changes you have made to a properties file using `diff` in Linux. For example:

```bash theme={null}
diff /opt/zoomdata/conf/edc-<connector-name>.properties /etc/zoomdata/<edc-<connector-name>.properties
```

or

```bash theme={null}
diff /opt/zoomdata/conf/zoomdata.properties /etc/zoomdata/zoomdata.properties
```

For Windows environments, use your preferred diff utility to compare the differences between your original and updated property files.

| File | Defines.... |
| - | - |
| `admin-server.jvm` | JVM options related to the Service Monitor. |
| `admin-server.properties` | Configuration properties related to the Service Monitor. |
| `config-server.jvm` | JVM options related to the configuration microservice. |
| `config-server.properties` | Configuration properties related to the configuration microservice. |
| `consul.json` | Settings related to the Service Discovery microservice. For a description of these settings, see [https://www.consul.io/docs/agent/options](https://www.consul.io/docs/agent/options). |
| `data-writer-postgresql.jvm` | JVM options related to the Data Writer microservice's Postgres relational database. |
| `data-writer-postgresql.properties` | Configuration properties related to the Data Writer microservice's Postgres relational database. |
| `edc-<connector>.jvm` | JVM options related to the specific connector microservice. For example, `edc-impala.jvm` contains JVM options for the Self-Service Analytics Cloudera Impala connector microservice. See [Connector Properties and Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files) . |
| `edc-<connector>.properties` | Configuration properties related to the specific connector microservice. For example, `edc-impala.properties` contains configuration properties for the Cloudera Impala connector microservice. See [Connector Properties and Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files). |
| `query-engine.jvm` | JVM options related to the Self-Service Analytics query engine. See [Manage the Self-Service Analytics Query Engine](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#manage-the-self-service-analytics-query-engine). |
| `query-engine.properties` | Configuration properties related to the query engine. See [Query Engine Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#query-engine-properties). |
| `screenshot-service.jvm` | JVM options related to Self-Service Analytics Screenshot microservice processing. |
| `screenshot-service.properties` | Configuration properties related to Screenshot microservice processing. See [screenshot-service.properties Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#screenshot-service-properties-properties). |
| `zoomdata.jvm` | JVM options (e.g. memory configuration) and Java system properties (e.g. timezone, temp directory, etc.) related to Self-Service Analytics. See [zoomdata.jvm Options](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#zoomdata-jvm-options). |
| `zoomdata.properties` | Configuration properties related to Self-Service Analytics. See [Properties Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference). |

<h2 id="server-level-variables">
  Server-Level Variables
</h2>

Server-level variables can be viewed by Self-Service Analytics administrators or members of the Supervisors group in the Server-Level Variables work area.

<Warning>
  Server-level variables are set during installation and must not be changed without understanding how the change affects or compromises your environment. If you must change a variable here, contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support). Do not add or delete server-level variables.
</Warning>

Select the **Advanced** menu option to access the Server-Level Variables work area.

Server-level variables are defined as key-value pairs. You can enable or disable the listed variables below if needed. Select **Save** to save and apply any changes you make in this work area.

<Danger>
  Changing toggles or editing content other than as instructed in this work area or as directed by Technical Support may prevent your users from using various components of Self-Service Analytics.
</Danger>

<table>
  <thead>
    <tr>
      <th scope="col">Key (Server-Level Variable)</th>
      <th scope="col">Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>allow-dashboard-and-report-sharing-within-tenant</td>
      <td>false (default)</td>

      <td>
        Enable or disable dashboard and self service report sharing options for sharing content with users, established groups, and everyone within your tenants or environment.

        <br />

        See [Share a Dashboard or Self Service Report with Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-share-withinacct).
      </td>
    </tr>

    <tr>
      <td>allow-sending-reports-to-external-emails</td>
      <td>true (default)</td>

      <td>
        Enabled by default, allows users with appropriate privileges to send reports to external email addresses ([user@example.com](mailto:user@example.com)).

        <br />

        Disable to prevent users from sending reports to users external to your data analytics environment. Any user included in a report send in your environment will get the report sent to the email address associated with their user account.
      </td>
    </tr>

    <tr>
      <td>alternative-calendars</td>
      <td>false (default)</td>

      <td>
        Enable or disable fiscal calendars.

        <br />

        When set to `true`, users with appropriate credentials can use the API to define fiscal calendars. Once defined, calendars are available to users.

        <br />

        When set to `false`, users cannot define or use fiscal calendars.

        <br />

        See [Fiscal Calendars](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#fiscal-calendars).
      </td>
    </tr>

    <tr>
      <td>enable-dundas-connector</td>
      <td>false (default)</td>
      <td>Disabled by default, enable to allow users with appropriate privileges [to register the connector server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#register-a-new-connector-server), define a connector, and create or [update sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#connect-to-a-dundas-bi-data-store) to access data hosted in a Dundas BI environment for use in this analytics environment.</td>
    </tr>

    <tr>
      <td>enhanced-experience</td>
      <td>The default setting is determined by your installation or transition path. See [Transitioning for Symphony and Composer Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/transition-sym).</td>

      <td>
        Enable or disable the enhanced user experience layout and theme (`d+a_light`) for your environment.

        <br />

        For environments transitioning from Symphony, this is `true` (enabled) by default.

        <br />

        For fresh installations of Composer v26.2 or later releases, this is `false` (disabled) by default.

        <br />

        For fresh installations of Self-Service Analytics 26.3 or later releases, this is `false` (disabled) by default.

        <br />

        For environments transitioning from earlier releases of Composer, this is `false` (disabled) by default.

        <br />

        See [User Interface Themes: v26.3 and Later](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#user-interface-themes-v26-3-and-later) and [Themes and UI Updates](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#themes-and-ui-updates).

        <br />

        <Danger>
          Update your custom theme and enable the `enhanced-experience` toggle before upgrading past version 26.2. The enhanced homepage and navigation will become the standard experience for all users in the near future. We recommend making these updates now to ensure a smooth transition.
        </Danger>
      </td>
    </tr>

    <tr>
      <td>folder-organization-enabled</td>
      <td>false (default)</td>

      <td>
        Enable or disable folders for use with dashboards and reports. Use folders to organize and manage dashboards and reports in your environment.

        <br />

        When set to `true`, users with appropriate roles assigned to their user account can use the API to define folders, manage folders, and delete folders.

        <br />

        When set to `false`, users cannot define or use folders.

        <br />

        <Warning>
          This feature is considered to be released in beta for your testing purposes. Workflows and features may change before a production-ready version is released.
        </Warning>
      </td>
    </tr>

    <tr>
      <td>hierarchies</td>
      <td>true (default)</td>

      <td>
        Enable or disable hierarchical fields in your environment.

        <br />

        When set to `true`, users with appropriate credentials can define hierarchical fields. These are availability to users with appropriate credentials.

        <br />

        When set to `false`, users cannot define or use hierarchical fields.

        <br />

        See [Hierarchical Fields and Structures](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/hierarchical-fields-ov).
      </td>
    </tr>

    <tr>
      <td>scheduled-report-file-drop</td>
      <td>false (default)</td>

      <td>
        Enable or disable users' ability to deliver a scheduled dashboard report or self service report to an SFTP location.

        <br />

        When set to `true`, users can select an SFTP file location you have defined to accept the scheduled report.

        <br />

        When set to `false`, users do not see an SFTP option for scheduled reports.

        <br />

        Define the settings for your environment at the instance level in `zoomdata.properties`or by passing along tenant or user attributes to `zoomdata.properties`. See [Scheduled Report Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule#scheduled-report-properties).
      </td>
    </tr>

    <tr>
      <td>self-service-reports</td>
      <td>false (default)</td>

      <td>
        Enable or disable self service reports in your environment.

        <br />

        When set to `true`, users with appropriate permissions can create self service reports in the Reports Library.

        <br />

        When set to `false`, users do not see self service report options or a Reports Library.

        <br />

        For more information about configuring your environment and planning for self service reporting, see [Self Service Report Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-report-microservice).
      </td>
    </tr>

    <tr>
      <td>timebar-snap-to-interval</td>
      <td>false (default)</td>

      <td>
        Enable or disable to control the granularity to which the time bar slider snaps.

        <br />

        When set to `true`, moving the time bar slider adjusts to the closest interval of the defined granularity available in the data set.

        <br />

        When set to `false`, moving the time bar slider adjusts to the nearest smallest granularity available in the data set.
      </td>
    </tr>

    <tr>
      <td>materialized-view</td>
      <td>false (default)</td>
      <td>This enabled the materialized views feature, which has been deprecated. Do not enable.</td>
    </tr>
  </tbody>
</table>

<h2 id="configure-memory-settings">
  Configure Memory Settings
</h2>

Unified service memory configuration recommendations can help you avoid out of memory issues, unpredictable service stability, and memory allocation. We strongly recommend you use the new default for Java: Xms=Xmx. These updated default memory allocations are designed configure your services more effectively for a production load after installation or upgrade.

<Note>
  Self-Service Analytics requires slightly higher memory expectations than previous releases. Upgrading will not overwrite your memory configuration if you have already overwritten the default configuration settings.
</Note>

If you’re upgrading your environment:

* Review your data source connector usage; stop unused connectors.
* Review your memory settings based on the chart below.

| | Composer versions through 23.1 Xms/Xmx | Composer v23.2 and later, Self-Service Analytics Xms/Xmx |
| - | - | - |
| Admin Server | 512M/1024M | Deprecated |
| Config Server | 512M/1024M | Deprecated |
| Data Writer | 128M/256M | 512M/512M |
| EDC | 128M/512M | 512M/512M |
| EDC hdfs/s3 | 512M/3584M | 1500M/1500M |
| Query Engine | 1G/6G | 4G/4G |
| Screenshot Service | 128M/1G | 750M/750M |
| Self Service Reports (when enabled) | N/A | 6Gi/9Gi |
| Zoomdata Web | 1G/2G | 4G/4G |

**Change memory allocation settings for microservices**

1. From your terminal, SSH to your Self-Service Analytics server.

2. To modify the memory settings for Self-Service Analytics microservices, you need to edit or create the corresponding `.jvm` files in `/etc/zoomdata/`. Perform the following steps:

   ```bash theme={null}
   vi/etc/zoomdata/<component_name>.jvm
   ```

   For complete information on editing configuration files, see [Edit a Configuration File](#edit-a-configuration-file).

3. Add or update the following line(s) in the corresponding `.jvm` files.

   <Warning>
     Do not allocate more than 85% of your total system memory to all microservices.
   </Warning>

   The following example configures the Self-Service Analytics server to use 20 GB of RAM in the `zoomdata.jvm` configuration file. You can adjust the number to fit your system's needs. Replace the **20** with the necessary memory allocation for your operating environment.

   ```
   -Xms20g
   -Xmx20g
   ```

4. Save and exit the `.jvm` file.

5. Restart the microservice for which you have modified the settings:

   For CentOS and Ubuntu:

   ```bash theme={null}
   sudo systemctl restart <service-name>
   ```

Wait a few minutes for the microservice to restart completely, then open a new browser window to log back into Self-Service Analytics.

<h2 id="encrypt-configuration-properties">
  Encrypt Configuration Properties
</h2>

You can encrypt sensitive property values in Self-Service Analytics's property files, if needed. This can be accomplished using the Spring Cloud CLI.

* [Prerequisites](#prerequisites)
* [Encrypting a Property](#encrypting-a-property)
* [Sample Script to Encrypt a Property](#sample-script-to-encrypt-a-property)

See also [Encryption](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode).

You can also pass sensitive property values using Linux environment variables, rather than hard coding the values in Self-Service Analytics property files. See [Pass Sensitive Data Using Linux Environment Variables](#pass-sensitive-data-using-linux-environment-variables).

<h3 id="prerequisites">
  Prerequisites
</h3>

Before you can encrypt property values, your Self-Service Analytics environment must meet the following requirements.

* Install or upgrade to Spring Cloud CLI version 2.0.0. This specific version is required. Review the installation and upgrade guidance here: [https://docs.spring.io/spring-boot/docs/2.0.0.RELEASE/reference/html/getting-started-installing-spring-boot.html#getting-started-installing-the-cli](https://docs.spring.io/spring-boot/docs/2.0.0.RELEASE/reference/html/getting-started-installing-spring-boot.html#getting-started-installing-the-cli).

  * Manual installation link: [https://github.com/spring-projects/spring-boot/releases/tag/v2.0.0.RELEASE](https://github.com/spring-projects/spring-boot/releases/tag/v2.0.0.RELEASE)
  * The command referenced for setup is `sdk install springboot 2.0.0`.
  * To install, use the command `spring install org.springframework.cloud:spring-cloud-cli:2.0.0.RELEASE`.

<h3 id="encrypting-a-property">
  Encrypting a Property
</h3>

**Encrypt an individual configuration property**

1. Ensure your environment meets the prerequisites listed in [Prerequisites](#prerequisites).

2. Use the following Spring Cloud CLI 2.0.0 command to encrypt a property value with a specified encryption key:

   ```
   spring encrypt <property-value> --key <encryption-key>
   ```

   <Warning>
     Version 2.0.0 of the Spring Cloud CLI must be installed. Other versions are not supported.
   </Warning>

   For example, the following command encrypts the value of the PASSWORD variable using the encryption key specified by the ENCRYPT\_KEY variable.

   ```
   spring encrypt $PASSWORD --key $ENCRYPT_KEY
   ```

   The output of this command is the encrypted property. For example:

   ```
   711448026e2c6a977b2be1b22f13642cc938366397fbd3451a3d2a50e27c348f
   ```

3. Add the following to the properties file in which the encrypted property value will be stored:

   * The encrypted property you obtained in Step 2, prepended with `{cipher}`. The `{cipher}` prefix allows Spring Cloud to recognize encrypted properties. For example:

     ```properties theme={null}
     encrypted.property={cipher}711448026e2c6a977b2be1b22f13642cc938366397fbd3451a3d2a50e27c348f
     ```

   * A new property (once per property file) that identifies the encryption key used. For example:

     ```properties theme={null}
     ENCRYPT.KEY=<encryption-key>
     ```

4. Save the properties file and restart its associated Self-Service Analytics microservice. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

Alternatively, you could modify and use the sample script, provided next, to encrypt a property value in a properties file.

<h3 id="sample-script-to-encrypt-a-property">
  Sample Script to Encrypt a Property
</h3>

You can modify and use the following sample script to encrypt a property value in a properties file.

```bash theme={null}
#!/bin/bash

#define the property file location, property key, and encryption key
FILE=/etc/zoomdata/zoomdata.properties
PROPERTY_KEY=spring.datasource.password
ENCRYPT_KEY=zoomdata

#read the property value
PROPERTY_VALUE=$(< "$FILE" grep -w "$PROPERTY_KEY"|cut -d '=' -f2)

#encrypt the value
#NOTE: this step will fail with 'Unable to initialize due to invalid secret key'
#if the JCE prerequisite is not met
ENCRYPTED_VALUE="{cipher}"$(spring encrypt $PROPERTY_VALUE --key $ENCRYPT_KEY)

#update the file
sed -i "s/$PROPERTY_KEY=$PROPERTY_VALUE/$PROPERTY_KEY=$ENCRYPTED_VALUE/g" $FILE

#add the encryption key if not already present in the file
grep -q -F "encrypt.key=$ENCRYPT_KEY" $FILE || echo "encrypt.key=$ENCRYPT_KEY" >> $FILE
```

<h2 id="pass-sensitive-data-using-linux-environment-variables">
  Pass Sensitive Data Using Linux Environment Variables
</h2>

You can pass sensitive property values (such as database passwords or user names) to Self-Service Analytics using Linux environment variables, rather than hard coding the values in Self-Service Analytics property files. Using the Spring Boot Java application’s ability to consume application properties as environment variables, you can pass sensitive data to Self-Service Analytics without showing the data as plain text in the Self-Service Analytics property files.

<Note>
  The information provided here requires a strong knowledge of Linux internals.
</Note>

You can do this using either of two methods:

* [Method 1: Use systemdOverride Files (Less Secure)](#method-1-use-systemd-override-files-less-secure)
* [Method 2: Use Parameters Passed to Microservices (More Secure)](#method-2-use-parameters-passed-to-microservices-more-secure)

You can also encrypt sensitive property values. See [Encrypt Configuration Properties](#encrypt-configuration-properties) to ensure your environment meets the requirements to perform this task.

<h3 id="method-1-use-systemd-override-files-less-secure">
  Method 1: Use `systemd`Override Files (Less Secure)
</h3>

You can use `systemd` with default unit files override. This is less secure than [Method 2: Use Parameters Passed to Microservices (More Secure)](#method-2-use-parameters-passed-to-microservices-more-secure) because the passwords are still exposed in the `env-pass.conf` files.

Complete the following steps:

1. Stop the affected microservices. See [Stop Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#stop-microservices).

   ```bash theme={null}
   sudo systemctl stop <service>
   ```

2. Add a `systemd` override file, called `env-pass.conf`, for each affected microservice. For example, the `systemd` override file for the `zoomdata` microservice would be `/etc/systemd/system/zoomdata.service.d/env-pass.conf` and the override file for the `zoomdata-query-engine` microservice would be `/etc/systemd/system/zoomdata-query-engine.service.d/env-pass.conf`. A complete list of microservice names is provided in [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference).

3. Edit the `env-pass.conf` file for each microservice and add lines specifying environment variable values for every microservice configuration property containing sensitive information. For example, the following environment variables specify the data store password, the upload destination password, and the keyset destination password in the `env-pass.conf` file for the `zoomdata` microservice:

   ```properties theme={null}
   [Service]
   Environment="SPRING_DATASOURCE_PASSWORD=<data store password>"
   Environment="UPLOAD_DESTINATION_PARAMS_PASSWORD=<upload destination password>"
   Environment="KEYSET_DESTINATION_PARAMS_PASSWORD=<keyset destination password>"
   ```

   In the `env-pass.conf` file for the `zoomdata-query-engine` microservice, you might add the following environment variable to specify the query engine database password:

   ```
   [Service]
   Environment="SPRING_QE_DATASOURCE_PASSWORD=<query engine database password>"
   ```

   The environment variable names are the same as the property names in the corresponding microservice property files, but in all capital letters and substituting underscores for the periods in the property names. Review the [property files](#configuration-property-files) for valid property names. For example, the environment variable name for the `spring.datasource.password` property is `SPRING_DATASOURCE_PASSWORD`.

4. Apply the changes to `systemd`:

   ```bash theme={null}
   sudo systemctl daemon-reload
   ```

5. Start the affected microservices. See [Start Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices).

<h3 id="method-2-use-parameters-passed-to-microservices-more-secure">
  Method 2: Use Parameters Passed to Microservices (More Secure)
</h3>

The most secure method is to pass sensitive parameters to Self-Service Analytics microservices as environment variables when you start the microservices. After the microservice is started, the settings for the sensitive parameters are no longer visible.

<Warning>
  If you use this method, Linux service management will be unable to automatically start or restart the affected Self-Service Analytics microservices when your system or server restarts. To resolve this, develop a wrapper script for `systemd` that will automatically export the required environment variables and restart the microservices.
</Warning>

Complete the following steps:

1. Stop the affected Self-Service Analytics microservice. See [Stop Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#stop-microservices).

   ```bash theme={null}
   sudo systemctl stop <service>
   ```

2. Disable the affected microservice. See [Disable Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#disable-microservices).

   ```bash theme={null}
   sudo systemctl disable <service>
   ```

3. Start the affected microservice, passing the sensitive parameters in environment variables as command line arguments. Make sure you use appropriate escape quotes if your password includes quotes.

   The environment variable names are the same as the property names in the corresponding microservice property files, but in all capital letters and substituting underscores for the periods in the property names. Review the [property files](#configuration-property-files) for valid property names. For example, the environment variable name for the `spring.datasource.password` property is `SPRING_DATASOURCE_PASSWORD`.

   In the following start command, the `zoomdata` microservice is started and the data store password, the upload destination password, and the keyset destination password are all passed as command line arguments:

   ```bash theme={null}
   sudo -u zoomdata /opt/zoomdata/bin/zoomdata start -v
    -E 'SPRING_DATASOURCE_PASSWORD=<data store password>'
    -E 'UPLOAD_DESTINATION_PARAMS_PASSWORD=<upload destination password>'
    -E 'KEYSET_DESTINATION_PARAMS_PASSWORD=<keyset destination password>'
   ```

   The following start command starts the `zoomdata-query-engine` microservice and passes the query engine database password as a command line argument.

   ```
   /opt/zoomdata/bin/zoomdata-query-engine start -v -E 'SPRING_QE_DATASOURCE_PASSWORD=<password>'
   ```

   See [Start Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices).

<h2 id="enable-self-service-analytics-component-access-from-other-sites">
  Enable Self-Service Analytics Component Access From Other Sites Using Cross-Origin Resource Sharing (CORS)
</h2>

Cross-origin resource sharing (CORS) is a standard introduced in HTML 5 that allows web applications to use HTTP headers to specify which origins are permitted to request resources on the server. Cross-origin resource sharing provides a web application access to selected resources running at a different location.

Web browsers consult the Access-Control-Allow-Origin header on how to relax the same origin policy for a given page. By default, this setting was disabled starting version 1.5.0SR1 due to security vulnerability concerns. However, CORS can be enabled for certain or all domains by editing the `zoomdata.properties` file (located in `/etc/zoomdata`). For more information about CORS, see [https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

**Modify CORS request permissions**

1. From your terminal, open a command line session.

2. Connect to your Self-Service Analytics server via command prompt.

3. Use the following command to access and open the `zoomdata.properties` file:

   ```bash theme={null}
   vi /etc/zoomdata/zoomdata.properties
   ```

4. Add the following variables to the file on new lines:

   ```properties theme={null}
   http.response.header.content-security-policy.frame-ancestors=<source1> <source2>
   access.control.allow.origin=<origin1>,<origin2>
   ```

   Replace `<source>` with the actual sources that may embed resources. The default is an asterisk (`*`), or all sources. For more information about the Content-Security-Policy (CSP) frame-ancestors directive, see [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors).

   Replace `<origin1>` and `<origin2>` with your specific URI including `http` or `https` as appropriate. Use `*` as a wildcard instead of a specific origin, thereby allowing any origin to access the resource, keeping in mind that this is a potential security vulnerability and may not work with all browsers. Refer to your Tomcat documentation to verify the appropriate syntax to use.

5. Save the document using standard `vi` commands.

6. Restart Self-Service Analytics microservices after making this change and also make sure to clear your browser cache. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

<h2 id="the-cross-origin-request-blocked-error">
  The Cross-Origin Request Blocked Error
</h2>

Cross-origin resource sharing (CORS) is a new standard introduced in HTML 5 that allows web applications to use HTTP headers to specify which origins are permitted to request resources on the server. Modern web browsers will consult the Access-Control-Allow-Origin header on how to relax the same origin policy for a given page.

By default, this setting was disabled starting version 1.5.0SR1 due to security vulnerability concerns. However, CORS can be enabled for certain or all domains through the zoomdata.conf ( `/etc/zoomdata` ) file. Please add the following parameter:

```properties theme={null}
access.control.allow.origin=*
```

The `*` will open CORS for all domains. If you want to specify specific domains, replace the `*` with the appropriate domain name. Refer to your Tomcat documentation to verify the appropriate syntax to use.

Please restart Self-Service Analytics server after making this change and also make sure to clear your browser cache.
