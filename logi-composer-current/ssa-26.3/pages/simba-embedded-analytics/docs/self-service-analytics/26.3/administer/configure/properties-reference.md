> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Properties Reference

<h2 id="zoomdata-properties-properties">
  zoomdata.properties Properties
</h2>

The zoomdata.properties file can be edited in the `/etc/zoomdata` directory. Each property is described in the table below.

Some situations where the `zoomdata.properties` file needs to be updated include:

* [Add an SSL Certificate](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso#add-an-ssl-certificate)
* [Disable the SSL Certificate in Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso#disable-the-ssl-certificate-in-self-service-analytics)
* [Screenshot Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/screenshot-install)
* [Create a Symmetric Key to Encrypt Data Source Passwords](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#create-a-symmetric-key-to-encrypt-data-source-passwords)
* [About Scheduled Reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule)
* [Set Up and Use the Data Gateway Service](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/data-gateway#set-up-and-use-the-data-gateway-service)

For information on editing configuration files, see [Edit a Configuration File](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#edit-a-configuration-file).

### General Properties

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>access.control.allow\.origin</td>
      <td>\*</td>

      <td>
        By default, CORS is set to `---` in the Self-Service Analytics Server. You can set CORS to restrict access:

        <br />

        `access.control.allow.origin=<user-defined>`

        <br />

        For more information, see [Enable Self-Service Analytics Component Access From Other Sites Using Cross-Origin Resource Sharing (CORS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#enable-self-service-analytics-component-access-from-other-sites).
      </td>
    </tr>

    <tr>
      <td>logs.dir</td>
      <td>*\<ZD\_install\_directory>* /logs</td>

      <td>
        Path to Self-Service Analytics logs. The placeholder *\<ZD\_install\_directory>* is replaced with the actual location where Self-Service Analytics is installed.

        <br />

        Verify that this log directory has all the necessary permissions and that the owner of the directory is set to `zoomdata`.

        <br />

        The `/home` directory cannot be used for logging.

        <br />

        Example: `logs.dir=/opt/<ZD_install_directory>/logs)`
      </td>
    </tr>

    <tr>
      <td>data-gateway.client-api.enabled</td>
      <td>False</td>
      <td>Set to true to enable use of the Data Gateway API and Data Gateway Service. See [Set Up and Use the Data Gateway Service](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/data-gateway#set-up-and-use-the-data-gateway-service).</td>
    </tr>

    <tr>
      <td>saml.maxAuthAge</td>
      <td>86400</td>

      <td>
        Sets the timeout for SAML, in seconds. The default is 24 hours.

        <br />

        Example: `saml.maxAuthAge=86400`
      </td>
    </tr>

    <tr>
      <td>server.compression.enabled</td>
      <td>true</td>

      <td>
        Enables gzip compression for http requests.

        <br />

        Example: `server.compression.enabled=true`
      </td>
    </tr>

    <tr>
      <td>server.port</td>
      <td>8080</td>
      <td>The default server port, which is set to use http. Prior releases used `http.port`</td>
    </tr>

    <tr>
      <td>server.servlet.context-path</td>
      <td>/composer</td>
      <td>Example: `server.servlet.context-path=/composer`</td>
    </tr>

    <tr>
      <td>server.session-timeout</td>
      <td>1800 seconds</td>

      <td>
        Sets when your Self-Service Analytics session will timeout (in seconds).

        <br />

        Example: `server.session-timeout=1800`

        <br />

        If you alter this value, also alter the value of the zoomdata.server.ws.idle.timeout property to match it.
      </td>
    </tr>

    <tr>
      <td>source.attribute.values.limit</td>
      <td>1000</td>

      <td>
        Sets the limit for the number of attribute values that can be displayed in the Filter list.

        <br />

        Example: `source.attribute.values.limit=1000`
      </td>
    </tr>

    <tr>
      <td>spring.servlet.multipart.max-file-size</td>
      <td>500Mb</td>
      <td>Example: `spring.servlet.multipart.max-file-size=500Mb`</td>
    </tr>

    <tr>
      <td>spring.servlet.multipart.max-request-size</td>
      <td>500Mb</td>
      <td>Example: `spring.servlet.multipart.max-request-size=500Mb`</td>
    </tr>

    <tr>
      <td>zoomdata.server.ws.idle.timeout</td>
      <td>1800000 ms</td>
      <td>Idle time that allows the WebSocket to be still valid. If you alter this value, also alter the value of the server.session-timeout property to match it.</td>
    </tr>

    <tr>
      <td>http.response.header.content-security-policy</td>
      <td>frame-ancestors \*;</td>

      <td>
        Add appropriate values to override the default values and support your business needs, such as `default-src 'self'` , `script-src 'self'` , and more.

        <br />

        Secure your implementation by including values for these resources using appropriate source URLs.

        <br />

        Example:

        <br />

        `frame-ancestors *; default-src 'self'; script-src 'self' 'nonce-composerScript' https://*.storage.example.com; style-src 'self' 'unsafe-inline' https://*.storage.example.com; img-src 'self'; connect-src 'self'; font-src 'self'; base-uri 'self';`
      </td>
    </tr>
  </tbody>
</table>

### Source Metadata Properties

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>zoomdata.source.refresh.metadata.cache.timeout.minutes</td>
      <td>10080 (one week)</td>
      <td>Sets the default time-to-live for cache values, in minutes.</td>
    </tr>

    <tr>
      <td>zoomdata.source.refresh.values.maxDistinctValues</td>
      <td>100000</td>
      <td>Sets the number of queried distinct values that can be stored in cache.</td>
    </tr>
  </tbody>
</table>

### Encryption Properties

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>security.encryption.algorithm</td>

      <td />

      <td>The encryption algorithm used for file encryption.</td>
    </tr>

    <tr>
      <td>security.encryption.key.algorithm</td>

      <td />

      <td>The algorithm type of the encryption key used for file encryption.</td>
    </tr>
  </tbody>
</table>

### Keystore Properties

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>keystore.location</td>
      <td>classpath:security/zoomkeystore.jks</td>

      <td>
        Self-Service Analytics uses symmetric encryption. You can point to a new keystore to strengthen security.

        <br />

        Example: `keystore.location=classpath:security/zoomkeystore.jks`

        <br />

        See [Create a Symmetric Key to Encrypt Data Source Passwords](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#create-a-symmetric-key-to-encrypt-data-source-passwords) for further guidance.
      </td>
    </tr>

    <tr>
      <td>keystore.password</td>
      <td>zoomkey</td>

      <td>
        Lets you set up a unique password for the keystore.

        <br />

        Example: `keystore.password=zoomkey`
      </td>
    </tr>

    <tr>
      <td>keystore.key.alias</td>
      <td>zoomkey</td>
      <td>Example: `keystore.key.alias=zoomkey`</td>
    </tr>

    <tr>
      <td>keystore.key.password</td>
      <td>zoomkey</td>
      <td>Example:`keystore.key.password=zoomkey`</td>
    </tr>
  </tbody>
</table>

### Server SSL Properties

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>server.ssl.key-store</td>
      <td>\<Self-Service Analytics\_install\_directory>/conf/keystore</td>

      <td>
        Sets the path for the keystore location.

        <br />

        Example: `server.ssl.key-store=HOME/conf/keystore`
      </td>
    </tr>

    <tr>
      <td>server.ssl.key-store-password</td>
      <td>changeit</td>

      <td>
        Stores the keystore password.

        <br />

        Example: `server.ssl.key-store-password=<YourPassword>`
      </td>
    </tr>
  </tbody>
</table>

### SAML Configuration Properties

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>saml.artifactBindingDefault</td>
      <td>true</td>
      <td>Example: `saml.artifactBindingDefault=true`</td>
    </tr>

    <tr>
      <td>saml.useMultiValueList</td>
      <td>true</td>
      <td>Example: `saml.useMultiValueList=true`</td>
    </tr>

    <tr>
      <td>saml.stringDelimiter</td>
      <td>,</td>
      <td>Example: `saml.stringDelimiter=;`</td>
    </tr>
  </tbody>
</table>

### Kerberized PostgreSQL Properties

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>spring.datasource.url</td>
      <td>jdbc:postgresql://\<IP\_address>:\<port>/zoomdata</td>

      <td>
        The URL of the `zoomdata` database in the PostgreSQL metadata store.

        <br />

        Example: `spring.datasource.url=jdbc:postgresql://localhost:5432/zoomdata`
      </td>
    </tr>

    <tr>
      <td>spring.datasource.username</td>
      <td>zoomdata</td>

      <td>
        The user name for the `zoomdata` database in the PostgreSQL metadata store.

        <br />

        Example: `spring.datasource.username=zoomdata`
      </td>
    </tr>

    <tr>
      <td>spring.datasource.password</td>
      <td>---</td>
      <td>The password associated with the user name for the `zoomdata` database in the PostgreSQL metadata store.</td>
    </tr>

    <tr>
      <td>keyset.destination.params.jdbc\_url</td>
      <td>jdbc:postgresql://\<IP\_address>:\<port>/zoomdata-keyset</td>

      <td>
        The URL of the `zoomdata-keyset` database in the PostgreSQL metadata store.

        <br />

        Example: `keyset.destination.params.jdbc_url=jdbc:postgresql://10.2.1.4:5432/zoomdata-keyset`
      </td>
    </tr>

    <tr>
      <td>keyset.destination.params.user\_name</td>
      <td>zoomdata</td>

      <td>
        The user name for the `zoomdata-keyset` database in the PostgreSQL metadata store.

        <br />

        Example: `keyset.destination.params.user_name=zoomdata`
      </td>
    </tr>

    <tr>
      <td>keyset.destination.params.password</td>
      <td>---</td>
      <td>The password associated with the user name for the `zoomdata-keyset` database in the PostgreSQL metadata store.</td>
    </tr>

    <tr>
      <td>upload.destination.params.jdbc\_url</td>
      <td>jdbc:postgresql://\<IP\_address>:\<port>/zoomdata-upload</td>

      <td>
        The URL of the `zoomdata-upload` database in the PostgreSQL metadata store.

        <br />

        Example: `upload.destination.params.jdbc_url=jdbc:postgresql://10.2.1.4:5432/zoomdata-upload`
      </td>
    </tr>

    <tr>
      <td>upload.destination.params.user\_name</td>
      <td>zoomdata</td>

      <td>
        The user name for the `zoomdata-upload` database in the PostgreSQL metadata store.

        <br />

        Example: `upload.destination.params.user_name=zoomdata`
      </td>
    </tr>

    <tr>
      <td>upload.destination.params.password</td>
      <td>---</td>
      <td>The password associated with the user name for the `zoomdata-upload` database in the PostgreSQL metadata store.</td>
    </tr>
  </tbody>
</table>

### Source Sampling Properties

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>source.sampling.rows</td>
      <td>1000</td>
      <td>Example: `source.sampling.rows=1000`</td>
    </tr>

    <tr>
      <td>source.attribute.values.limit</td>
      <td>1000</td>
      <td>Example: `source.attribute.values.limit=1000`</td>
    </tr>
  </tbody>
</table>

### Logging Properties

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>logging.unified.host</td>
      <td>127.0.0.1</td>

      <td>
        Sets the host IP address for [Fluentd server](https://www.fluentd.org/) message logging. For more information, see [Set Up Unified Logging Using Fluentd](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging).

        <br />

        Example: `logging.unified.host=123.4.5.6`
      </td>
    </tr>

    <tr>
      <td>logging.unified.level</td>
      <td>OFF</td>

      <td>
        Sets the log level for messages logged to the [Fluentd server](https://www.fluentd.org/). The following options are available for this property: TRACE, DEBUG, INFO, WARN, ERROR, and OFF. If set to OFF, Fluentd unified logging is disabled. For more information, see [Set Up Unified Logging Using Fluentd](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging).

        <br />

        Example: `logging.unified.level=INFO`
      </td>
    </tr>

    <tr>
      <td>logging.unified.port</td>
      <td>24224</td>

      <td>
        Sets the port for [Fluentd server](https://www.fluentd.org/) message logging. For more information, see [Set Up Unified Logging Using Fluentd](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging).

        <br />

        Example: `logging.unified.port=1234`
      </td>
    </tr>

    <tr>
      <td>logging.unified.tag</td>
      <td>zoomdata-server</td>

      <td>
        Sets the microservice tag name for messages logged to the [Fluentd server](https://www.fluentd.org/). This is important because the tag identifies the microservice to which the log messages apply. Valid values are `query-engine`, `zoomdata-server`, `stream-writer`, `upload-service`, and `edc-<connector-name>` (where `<connector-name>` is one of the names listed in [Connector Properties and Property Files](#connector-properties-and-property-files)).

        <br />

        For more information, see [Set Up Unified Logging Using Fluentd](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging).

        <br />

        Example: `logging.unified.tag = zoomdata-server`
      </td>
    </tr>

    <tr>
      <td>syslog.host</td>
      <td>127.0.0.1</td>

      <td>
        Sets the host IP address for [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) message logging.

        <br />

        Example: `syslog.host=127.0.0.1`
      </td>
    </tr>

    <tr>
      <td>syslog.log.level</td>
      <td>OFF</td>

      <td>
        Sets the syslog log level for messages logged to the [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/). The following options are available for this property: TRACE, DEBUG, INFO, WARN, ERROR, and OFF.

        <br />

        Example: `syslog.log.level=DEBUG`
      </td>
    </tr>

    <tr>
      <td>syslog.port</td>
      <td>1514</td>

      <td>
        Sets the port for [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) message logging.

        <br />

        Example: `syslog.port=1514`
      </td>
    </tr>

    <tr>
      <td>syslog.suffix</td>
      <td>local</td>

      <td>
        Specifies a suffix that is appended at the end of the [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) log entry that Self-Service Analytics generates.

        <br />

        Example: `syslog.suffix=local`
      </td>
    </tr>
  </tbody>
</table>

### Password Policy

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>auth.password.policy.specialCharacters</td>
      <td>!@#\$%^&\*()-\_=+,.:;\<></td>

      <td />
    </tr>

    <tr>
      <td>auth.password.policy.minCharacters</td>
      <td>9</td>

      <td />
    </tr>

    <tr>
      <td>auth.password.policy.maxCharacters</td>
      <td>255</td>

      <td />
    </tr>

    <tr>
      <td>auth.password.policy.minLowercaseCharacters</td>
      <td>1</td>

      <td />
    </tr>

    <tr>
      <td>auth.password.policy.minUppercaseCharacters</td>
      <td>1</td>

      <td />
    </tr>

    <tr>
      <td>auth.password.policy.minNumericCharacters</td>
      <td>1</td>

      <td />
    </tr>

    <tr>
      <td>auth.password.policy.minSpecialCharacters</td>
      <td>1</td>

      <td />
    </tr>

    <tr>
      <td>auth.password.policy.helpMessage</td>
      <td>Password must contain at least 9 characters including 1 lowercase, 1 uppercase, 1 number and 1 special (!@#\$%^&\*()-\_=+,.:;\<>).</td>
      <td>Text is not enclosed in quotation marks.</td>
    </tr>
  </tbody>
</table>

### Data Export Properties

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>zoomdata.export.data.max.cols</td>
      <td>1000 columns</td>

      <td>
        Use this property to define the maximum number of columns that can be exported for two-dimensional visuals (such as a pivot table). Self-Service Analytics enforces this limit for visual data, but does not enforce it for raw data.

        <br />

        The distributed default for this setting is 1000 columns. Valid values can range from 0 through 2147483647 columns.
      </td>
    </tr>

    <tr>
      <td>zoomdata.export.data.max.rows</td>
      <td>100000 rows</td>

      <td>
        Use this property to define the maximum number of rows that can be exported for visuals. Self-Service Analytics enforces this limit for visual data. However, for raw data, Self-Service Analytics produces an error if the number of rows requested for export exceeds this setting.

        <br />

        The distributed default for this setting is 100000 rows. Valid values can range from 0 through 2147483647 rows.
      </td>
    </tr>

    <tr>
      <td>zoomdata.export.visualdata.max.rows</td>
      <td>100000 rows</td>

      <td>
        Use this property to define the maximum number of rows that can be exported for visuals. Self-Service Analytics enforces this limit for visual data. However, for raw data, Self-Service Analytics produces an error if the number of rows requested for export exceeds this setting.

        <br />

        The distributed default for this setting is 100000 rows. Valid values can range from 0 through 2147483647 rows.
      </td>
    </tr>
  </tbody>
</table>

### Screenshot Microservice Client & Dashboard Scheduling Properties

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>dashboard.scheduling.screenshot.png.height</td>
      <td>`1080`</td>
      <td>Identifies the maximum height (in pixels) of the screenshot PNG file that will be sent.</td>
    </tr>

    <tr>
      <td>dashboard.scheduling.screenshot.png.width</td>
      <td>`1920`</td>
      <td>Identifies the maximum width (in pixels) of the screenshot PNG file that will be sent.</td>
    </tr>

    <tr>
      <td>dashboard.scheduling.screenshot.timeout</td>
      <td>`60`</td>

      <td>
        Specifies the timeout (in seconds) to take a screenshot for a dashboard email report.

        <br />

        <Note>
          The time specified by this property must be less than or equal to the time set by the `screenshot.service.http.client.read.timeout.milliseconds` property. If you increase the value of this property, make sure that you increase the value of the `screenshot.service.http.client.read.timeout.milliseconds property` accordingly. Bear in mind that this property is specified in seconds, but the `screenshot.service.http.client.read.timeout.milliseconds` property is specified in milliseconds.
        </Note>
      </td>
    </tr>

    <tr>
      <td>export.proxy.allow</td>
      <td>`.*`</td>
      <td>Specifies a regular expression that allow-lists the outgoing URLs the canvas proxy can request when generating screenshots and PDF exports.</td>
    </tr>

    <tr>
      <td>export.proxy.mime-types.allowed</td>
      <td>`image/jpeg,image/jpg,image/png,image/gif,image/webp,image/svg+xml,image/svg-xml,text/html,application/xhtml,application/xhtml+xml`</td>
      <td>Specifies the MIME types the canvas proxy is permitted to fetch. Separate multiple values with commas.</td>
    </tr>

    <tr>
      <td>export.proxy.client.timeout.millis</td>
      <td>`300000`</td>
      <td>Sets how long (in milliseconds) the canvas proxy waits when fetching a resource from a remote source before the request fails.</td>
    </tr>

    <tr>
      <td>screenshot.service.name</td>
      <td>screenshot-service</td>

      <td />
    </tr>

    <tr>
      <td>screenshot.service.url</td>
      <td>`http://localhost:8083/`</td>
      <td>This is the default screenshot microservice URL, used when service discovery is disabled in your environment.</td>
    </tr>

    <tr>
      <td>screenshot.service.http.client.connect.timeout.milliseconds</td>
      <td>`10000`</td>
      <td>Specifies the number of milliseconds that can elapse before Self-Service Analytics stops trying to connect to the screenshot microservice client.</td>
    </tr>

    <tr>
      <td>screenshot.service.http.client.read.timeout.milliseconds</td>
      <td>`60000`</td>

      <td>
        Specifies the number of milliseconds that can elapse before Self-Service Analytics stops trying to read from the screenshot microservice client.

        <br />

        <Note>
          If you increase the time set by the `dashboard.scheduling.screenshot.timeout` property, make sure that you increase the value of this property as well. The total time set by `screenshot.service.http.client.read.timeout.milliseconds` should always be greater than or equal to the time set by the `dashboard.scheduling.screenshot.timeout` property. Bear in mind that this property is specified in milliseconds, but the `dashboard.scheduling.screenshot.timeout` property is specified in seconds.
        </Note>
      </td>
    </tr>

    <tr>
      <td>screenshot.service.http.client.write.timeout.milliseconds</td>
      <td>`60000`</td>
      <td>Specifies the number of milliseconds that can elapse before Self-Service Analytics stops trying to write to the screenshot microservice client.</td>
    </tr>

    <tr>
      <td>screenshot.service.http.client.max-in-memory-size.bytes</td>
      <td>`512000`</td>
      <td>The maximum amount of buffered bytes used when aggregating the response stream.</td>
    </tr>
  </tbody>
</table>

### Field Settings

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>zoomdata.detect.type.attribute.max.length</td>
      <td>200 characters</td>
      <td>Use this property to set the maximum character length of attribute fields. If this limit is exceeded, the field will be recognized as a Text field.</td>
    </tr>
  </tbody>
</table>

### JSON Dataset Properties

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>json.storage.max-size</td>
      <td>5242880 bytes (5 MB)</td>
      <td>Sets the maximum size of each JSON dataset, in bytes, for each tenant account.</td>
    </tr>

    <tr>
      <td>json.storage.max-datasets-per-account</td>
      <td>100 datasets</td>
      <td>Sets the maximum number of JSON datasets for each tenant account.</td>
    </tr>
  </tbody>
</table>

### Mail SMTP Information

<table>
  <thead>
    <tr>
      <th scope="col">Property</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>sftp.host</td>

      <td>
        sftp.host=localhost

        <br />

        sftp.port=2222

        <br />

        sftp.user=uname

        <br />

        sftp.password=pwd

        <br />

        sftp.strictHostKeyChecking=no

        <br />

        sftp.remote.directory=/tmp
      </td>

      <td>Specifies the properties for SFTP location, credentials, and other settings to deliver scheduled reports and schedule dashboard reports to the defined SFTP location.</td>
    </tr>

    <tr>
      <td>mail.from</td>

      <td />

      <td>Specifies the email address identifying where the email comes from. "[User@example.com](mailto:User@example.com)"</td>
    </tr>

    <tr>
      <td>mail.login</td>

      <td />

      <td>Specifies the email login to use to access the mail server.</td>
    </tr>

    <tr>
      <td>mail.password</td>

      <td />

      <td>Specifies the password associated with the email login identified in the `mail.login` property.</td>
    </tr>
  </tbody>
</table>

Mail SMTP Information specifies the properties for SMTP port, enablement, and authentication:

* `mail.smtp.port: 465`
* `mail.smtp.auth: true`
* `mail.smtp.ssl.enable: true`
* `mail.smtp.ssl.protocols: "TLSv1.2"`
* `mail.login: "mail.login"`
* `mail.password: "mail.password"`
* `mail.from: "mail.from"`

In addition, JavaMail API properties (Self-Service Analytics supports both IMAP and SMTP protocols) should be added to the `zoomdata.properties` file to identify the mail server and other mail properties required to use that server to send the scheduled dashboard (for example, `mail.smtp.auth, mail.smtp.host`, `mail.smtp.port`, `mail.imap.host`, and `mail.imap.port`). Complete descriptions of IMAP and SMTP protocol JavaMail properties can be found at these links:

* IMAP: [https://javaee.github.io/javamail/docs/api/com/sun/mail/imap/package-summary.html](https://javaee.github.io/javamail/docs/api/com/sun/mail/imap/package-summary.html)
* SMTP: [https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html](https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html)

<h2 id="zoomdata-jvm-options">
  zoomdata.jvm Options
</h2>

The `zoomdata.jvm` file contains JVM options (e.g. memory configuration) and Java system properties (e.g. timezone, temp directory, etc.) related to Self-Service Analytics. The table below describes the options you can adjust.

Situations where the `zoomdata.jvm` file needs to be edited include:

* [Configure Memory Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configure-memory-settings)
* [Connect to a Kerberized CDH Cluster](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#connect-to-a-kerberized-cdh-cluster)

For information on editing configuration files, see [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).

<table>
  <thead>
    <tr>
      <th>Option</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>DEBUG\_ENABLED</td>
      <td>0/false</td>

      <td>
        Toggle switch to enable or disable the Java debug capability. To enable, enter '1' or 'true'.

        <br />

        Example: `DEBUG_ENABLED=false`
      </td>
    </tr>

    <tr>
      <td>DEBUG\_PORT</td>
      <td>9393</td>

      <td>
        The default port for the Java debug capability.

        <br />

        Example: `DEBUG_PORT=9393`
      </td>
    </tr>

    <tr>
      <td>JAVA\_OPTS</td>
      <td>-Xss256k -Xms2048m -Xmx8192m</td>
      <td>Java-related options for JVM. Refer to Oracle's article on [Java HotSpot VM Options](https://www.oracle.com/java/technologies/javase/vmoptions-jsp.html) for information.</td>
    </tr>

    <tr>
      <td>KERBEROS\_CONFIG</td>
      <td>/etc/krb5.conf</td>

      <td>
        Default location for the Kerberos configuration details. However, the path to the file may be different in your environment.

        <br />

        Refer to Oracle's article on [File Formats](https://docs.oracle.com/cd/E36784_01/html/E36882/krb5.conf-4.html) for information.
      </td>
    </tr>

    <tr>
      <td>KERBEROS\_PRINCIPAL</td>
      <td>[hdfs@HADOOP.COM](mailto:hdfs@HADOOP.COM)</td>
      <td>Kerberos principal name.</td>
    </tr>

    <tr>
      <td>KERBEROS\_KEYTAB</td>
      <td>/etc/zoomdata/zoomdata.keytab</td>
      <td>Kerberos keytab location.</td>
    </tr>

    <tr>
      <td>PROXY\_HOST</td>
      <td>user-defined</td>
      <td>For cloud-based connectors (including Google Analytics and Salesforce) being used in a proxy configuration, this property specifies the server host to be returned for calls, and identifies the proxy host server that will provide internet access.</td>
    </tr>

    <tr>
      <td>PROXY\_PORT</td>
      <td>user-defined</td>
      <td>For cloud-based connectors (including Google Analytics and Salesforce) being used in a proxy configuration, this property specifies the server port to be returned for calls, and identifies the proxy port server that will provide internet access.</td>
    </tr>
  </tbody>
</table>

<h2 id="query-engine-properties">
  Query Engine Properties
</h2>

Most of the query engine components can be edited in the `query-engine.properties` file. You can manage the query engine using the following properties. For information on editing configuration files, see [Edit a Configuration File](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#edit-a-configuration-file).

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**Service Logging**</td>
    </tr>

    <tr>
      <td>access.log.file.size</td>
      <td>10</td>
      <td>Access log file size (in MB).</td>
    </tr>

    <tr>
      <td>qe.error.log.file.size</td>
      <td>5</td>
      <td>Error log file size (in MB).</td>
    </tr>

    <tr>
      <td>log.file.size</td>
      <td>20</td>
      <td>General log file size (in MB).</td>
    </tr>

    <tr>
      <td>websocket.log.file.size</td>
      <td>10</td>
      <td>Websocket log file size (in MB).</td>
    </tr>

    <tr>
      <td>syslog.host</td>
      <td>127.0.0.1</td>
      <td>Sets the host IP address for [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) message logging.</td>
    </tr>

    <tr>
      <td>syslog.log.level</td>
      <td>OFF</td>
      <td>Sets the syslog log level for messages logged to the [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/). The following options are available for this property: TRACE, DEBUG, INFO, WARN, ERROR. and OFF.</td>
    </tr>

    <tr>
      <td>trace.requests</td>
      <td>false</td>
      <td>Enables detailed tracing of HTTP request.</td>
    </tr>

    <tr>
      <td>tracing.sampler.probability</td>
      <td>1</td>
      <td>The distributed tracing request rate percentage. Valid values are between 0 to 1.0, where 0 disables tracing and 1.0 indicates tracing 100% of requests.</td>
    </tr>

    <tr>
      <td colSpan={3}>**General Microservice Configuration for Jetty Web Server**</td>
    </tr>

    <tr>
      <td>server.jetty.max-threads</td>
      <td>200</td>
      <td>Number of threads to serve the HTTP & WebSocket clients.</td>
    </tr>

    <tr>
      <td>qe.server.ws.idle.timeout</td>
      <td>86400000</td>
      <td>Idle time (in milliseconds) that allows the WebSocket to be still valid.</td>
    </tr>

    <tr>
      <td>qe.server.ws.input.buffer.size</td>
      <td>16384</td>
      <td>Buffer size (in bytes) for the WebSocket message.</td>
    </tr>

    <tr>
      <td>qe.server.ws.max.message.size</td>
      <td>1048576</td>
      <td>Max size (in bytes) of a message that could be sent over the query engine WebSocket.</td>
    </tr>

    <tr>
      <td>server.port</td>
      <td>5580</td>
      <td>REST/WebSocket microservice port.</td>
    </tr>

    <tr>
      <td>server.ssl.enabled</td>
      <td>false</td>
      <td>Defines whether the REST/WS API should use SSL.</td>
    </tr>

    <tr>
      <td>server.ssl.key-store</td>

      <td />

      <td>Path to the file with the keystore.</td>
    </tr>

    <tr>
      <td>**Graceful Shutdown**</td>

      <td />

      <td />
    </tr>

    <tr>
      <td>application.graceful.shutdown.enabled</td>
      <td>true</td>
      <td>Indicates whether or not graceful shutdown processing should occur. Valid values are `true` (perform graceful shutdown processing) or `false` (do not perform graceful shutdown processing).</td>
    </tr>

    <tr>
      <td>application.graceful.shutdown.event-propagation-timeout-sec</td>
      <td>5</td>
      <td>Specifies how long (in seconds) a query engine instance will wait to allow clients to receive the information that it is out of service.</td>
    </tr>

    <tr>
      <td>application.graceful.shutdown.force-kill-timeout-sec</td>
      <td>30</td>

      <td>
        The maximum number of seconds that a query engine instance will wait for the number of its active tasks to reach zero.

        <br />

        When this time has elapsed, all remaining active WebSockets serving in-flight queries are closed and then the query engine instance will stop.
      </td>
    </tr>

    <tr>
      <td>**Topology Configuration**</td>

      <td />

      <td />
    </tr>

    <tr>
      <td>calculations.detect.array.fields</td>
      <td>true</td>

      <td>
        Enables and disables the query engine validation of multivalue fields in a derived field.

        <br />

        By disabling (set the value to `false`) this functionality, any custom metrics that you may have created in earlier versions of Self-Service Analytics that are aggregations of multivalue fields will produce valid values.
      </td>
    </tr>

    <tr>
      <td>qe.max.allowed.time.groups</td>
      <td>10000</td>

      <td>
        The maximum amount of time in which groups can be generated by the **Include Blanks** function.

        <br />

        For information on even time intervals, see [Even Time Intervals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/even-time-interval)

        <br />

        .
      </td>
    </tr>

    <tr>
      <td>qe.max.rows.during.execution</td>
      <td>5000000</td>

      <td>
        The maximum number of rows that can be processed during a single query. The value specified must be at least slightly greater than the value for the `qe.zengine.edc.rows.limit` property.

        <br />

        If you increase the value of `qe.zengine.edc.rows.limit`, consider increasing the value of this property.

        <br />

        When a query exceeds the limit set by this property, a `Resource limit is reached during query execution` message appears.
      </td>
    </tr>

    <tr>
      <td>qe.zengine.edc.rows.limit</td>
      <td>1000000</td>
      <td>The maximum number of records that can be fused from a single data source.</td>
    </tr>

    <tr>
      <td>sharpening.enabled</td>
      <td>true</td>

      <td>
        Enables or disables [Data Sharpening](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-sharpening-ov).

        <br />

        Set this property to `true` to enable Data Sharpening; set it to `false` to disable it.
      </td>
    </tr>

    <tr>
      <td>sharpening.samples.max.count</td>
      <td>100</td>
      <td>The maximum number of Data Sharpening requests that can be generated by the sharpening process.</td>
    </tr>

    <tr>
      <td>sharpening.samples.skip.first</td>
      <td>1</td>
      <td>Defines how many first samples are skipped before visualizing the result of sharpening.</td>
    </tr>

    <tr>
      <td>zoomdata.validation.histogram.max.size</td>
      <td>1000</td>
      <td>Histogram max bucket count.</td>
    </tr>
  </tbody>
</table>

<h2 id="screenshot-service-properties-properties">
  screenshot-service.properties Properties
</h2>

The following table lists properties you might adjust for the Self-Service Analytics [Screenshot microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/screenshot-install).

For information on editing configuration files, see [Edit a Configuration File](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#edit-a-configuration-file).

<table>
  <thead>
    <tr>
      <th>Property Name</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>pool.queue.size</td>
      <td>`10`</td>

      <td>
        Sets the queue size for Screenshot microservice requests.

        <br />

        This property and the pool.thread.size property specify the upper limits for Screenshot microservice processing. When the number of screenshot requests exceeds the limits set by these two properties, you will receive HTTP 429 "Too Many Requests" errors.

        <br />

        You can exceed these limits in a number of ways, including:

        <br />

        * starting up Self-Service Analytics with lots of dashboards and visuals
        * deleting all your screenshots at once
        * rapidly creating a lot of large dashboards

        <br />

        You can increase the values of this property and the pool.thread.size property when you encounter too many failed screenshots. However, do so with caution.
      </td>
    </tr>

    <tr>
      <td>pool.thread.size</td>
      <td>`20`</td>

      <td>
        Sets the thread count for Screenshot microservice requests.

        <br />

        This property and the pool.queue.size property specify the upper limits for Screenshot microservice processing. When the number of screenshot requests exceeds the limits set by these two properties, you will receive HTTP 429 "Too Many Requests" errors.

        <br />

        You can exceed these limits in a number of ways, including:

        <br />

        * starting up Self-Service Analytics with lots of dashboards and visuals
        * deleting all your screenshots at once
        * rapidly creating a lot of large dashboards

        <br />

        If your use of Self-Service Analytics includes [scheduling dashboard reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule), update this setting so it is greater than the number of concurrent reports. You can also increase the values of this property and the pool.queue.size property when you encounter too many failed screenshots. However, do so with caution.
      </td>
    </tr>

    <tr>
      <td>syslog.host</td>
      <td>`127.0.0.1`</td>

      <td>
        Sets the host IP address for [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) message logging.

        <br />

        Example: `syslog.host=127.0.0.1`

        <br />

        Override in the zoomdata.properties file; this affects more than the screenshot microservice if you edit it.
      </td>
    </tr>

    <tr>
      <td>syslog.log.level</td>
      <td>OFF</td>

      <td>
        Sets the syslog log level for messages logged to the [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/). The following options are available for this property: TRACE, DEBUG, INFO, WARN, ERROR and OFF.

        <br />

        Example: `syslog.log.level=DEBUG`

        <br />

        Override in the zoomdata.properties file; this affects more than the screenshot microservice if you edit it.
      </td>
    </tr>

    <tr>
      <td>syslog.port</td>
      <td>1514</td>

      <td>
        Sets the port for [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) message logging.

        <br />

        Example: `syslog.port=1514`

        <br />

        Override in the zoomdata.properties file; this affects more than the screenshot microservice if you edit it.
      </td>
    </tr>

    <tr>
      <td>syslog.suffix</td>
      <td>local</td>

      <td>
        Specifies a suffix that is appended at the end of the [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) log entry that Self-Service Analytics generates.

        <br />

        Example: `syslog.suffix=local`

        <br />

        Override in the zoomdata.properties file; this affects more than the screenshot microservice if you edit it.
      </td>
    </tr>
  </tbody>
</table>

<h2 id="connector-properties-and-property-files">
  Connector Properties and Property Files
</h2>

Self-Service Analytics's architecture enables the deployment of Self-Service Analytics's data connectors as standalone components running in their own process space. Each connector has its own dedicated connector server and a corresponding property files. Some properties are common to all connectors and some properties are unique to a specific connector. The properties for each connector are documented in the property files.

The kinds of configuration properties found in these files include:

* logging properties
* actuator properties (Spring Boot management endpoint configuration)
* data source connection pool properties
* data source-specific properties
* Kerberos configuration properties (for some connectors)
* service discovery properties
* other connector-specific properties.

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

The connector property files have names in the following format: `edc-<connector>.properties`. The following table lists these property files and identifies the associated connector.

| Connector | Property File Name |
| - | - |
| Amazon Redshift | `edc-redshift.properties` |
| Amazon S3 | `edc-s3.properties` |
| Apache Drill | `edc-drill.properties` |
| Apache Phoenix 4.7 | `edc-phoenix-4.7.properties` |
| Apache Phoenix Query Server 4.7 | `edc-phoenix-4.7-queryserver.properties` |
| Apache Solr | `edc-apache-solr.properties` |
| BigQuery | `edc-bigquery.properties` |
| Cloudera Impala | `edc-impala.properties` |
| Cloudera Search | `edc-cloudera-search.properties` |
| Couchbase | `edc-couchbase.properties` |
| Dremio | `edc-dremio.properties` |
| Elasticsearch 7.0 | `edc-elasticsearch-7.0.properties` |
| Elasticsearch 8.0 | `edc-elasticsearch-8.0.properties` |
| HDFS | `edc-hdfs.properties` |
| Hive | `edc-hive.properties` |
| Jira | `edc-jira.properties` |
| MemSQL | `edc-memsql.properties` |
| Microsoft SQL Server | `edc-mssql.properties` |
| MongoDB | `edc-mongo.properties` |
| MySQL | `edc-mysql.properties` |
| OpenSearch | `edc-opensearch.properties` |
| Oracle | `edc-oracle.properties` |
| PostgreSQL | `edc-postgresql.properties` |
| Python | `edc-python.properties` |
| Real-Time Sales | `edc-rts.properties` |
| Salesforce | `edc-salesforce.properties` |
| SAP Hana | `edc-saphana.properties` |
| SAP S/4HANA | `edc-saphanacloud.properties` |
| SAP IQ | `edc-sapiq.properties` |
| Snowflake | `edc-snowflake.properties` |
| Spark SQL | `edc-sparksql.properties` |
| Teradata | `edc-teradata.properties` |
| TIBCO DV | `edc-tibcodv.properties` |
| Trino | `edc-trino.properties` |
| Vertica | `edc-vertica.properties` |

For more information about editing property files, see [Edit a Configuration File](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#edit-a-configuration-file).
