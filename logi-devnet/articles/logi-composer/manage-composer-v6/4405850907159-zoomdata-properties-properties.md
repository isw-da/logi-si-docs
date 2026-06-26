---
title: "zoomdata.properties Properties"
id: 4405850907159
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850907159-zoomdata-properties-Properties
updated_at: 2022-05-26T20:43:09Z
---

# zoomdata.properties Properties

# zoomdata.properties Properties

The zoomdata.properties file can be edited in the `/etc/zoomdata` directory. Each property is described in the table below.

Some situations where the `zoomdata.properties` file needs to be updated include:

* [*Add an SSL Certificate*](https://devnet.logianalytics.com/hc/en-us/articles/4405851178647-Add-an-SSL-Certificate)
* [*Disable the SSL Certificate in Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405851179543-Disable-the-SSL-Certificate-in-Composer)
* [*Set Up the Screenshot Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405851095575-Set-Up-the-Screenshot-Microservice)
* [*Create a Symmetric Key to Encrypt Data Source Passwords*](https://devnet.logianalytics.com/hc/en-us/articles/4405850928023-Create-a-Symmetric-Key-to-Encrypt-Data-Source-Passwords)
* [*About Scheduled Dashboard Reports*](https://devnet.logianalytics.com/hc/en-us/articles/4405850989335-About-Scheduled-Dashboard-Reports)

For information on editing configuration files, see [*Edit a Composer Configuration File*](https://devnet.logianalytics.com/hc/en-us/articles/4405850887703-Edit-a-Composer-Configuration-File).

| Property | Default Value | Description |
| --- | --- | --- |
| access.control.allow.origin | \* | By default, CORS is set to --- in the Composer Server. You can set CORS to restrict access: `access.control.allow.origin=<user-defined>`  For more information, see [*Enable Composer Component Access From Other Sites Using Cross-Origin Resource Sharing (CORS)*](https://devnet.logianalytics.com/hc/en-us/articles/4405850901783-Enable-Composer-Component-Access-From-Other-Sites-Using-Cross-Origin-Resource-Sharing-CORS-). |
| logs.dir | *<ZD\_install\_directory>* /logs | Path to Composer logs. The placeholder *<ZD\_install\_directory>* is replaced with the actual location where Composer is installed.  Verify that this log directory has all the necessary permissions and that the owner of the directory is set to `zoomdata`.  The `/home` directory cannot be used for logging.  Example: `logs.dir=/opt/<composer>/logs)` |
| management.endpoints.web.base-path | /actuator | Path to the Composer actuator. |
| saml.maxAuthAge | 86400 | Sets the timeout for SAML, in seconds. The default is 24 hours. Example: `saml.maxAuthAge=86400` |
| server.compression.enabled | true | Enables gzip compression for http requests.  Example: `server.compression.enabled=true` |
| server.port | 8080 | The default server port, which is set to use http. Prior releases used `http.port` |
| server.servlet.context-path | /composer | Example: `server.servlet.context-path=/composer` |
| server.session-timeout | 1800 seconds | Sets when your Composer session will timeout (in seconds). Example: `server.session-timeout=1800`  If you alter this value, also alter the value of the zoomdata.server.ws.idle.timeout property to match it. |
| source.attribute.values.limit | 1000 | Sets the limit for the number of attribute values that can be displayed in the Filter list. Example: `source.attribute.values.limit=1000` |
| spring.servlet.multipart.max-file-size | 500Mb | Example: `spring.servlet.multipart.max-file-size=500Mb` |
| spring.servlet.multipart.max-request-size | 500Mb | Example: `spring.servlet.multipart.max-request-size=500Mb` |
| zoomdata.server.ws.idle.timeout | 1800000 ms | Idle time that allows the WebSocket to be still valid. If you alter this value, also alter the value of the server.session-timeout property to match it. |
| Source Metadata Properties | | |
| zoomdata.source.refresh.metadata.cache.timeout.minutes | 10080 (one week) | Sets the default time-to-live for cache values, in minutes. |
| zoomdata.source.refresh.values.maxDistinctValues | 100000 | Sets the number of queried distinct values that can be stored in cache. |
| Encryption Properties | | |
| security.encryption.algorithm |  | The encryption algorithm used for file encryption. |
| security.encryption.key.algorithm |  | The algorithm type of the encryption key used for file encryption. |
| Keystore Properties | | |
| keystore.location | classpath:security/zoomkeystore.jks | Composer uses symmetric encryption. You can point to a new keystore to strengthen security. Example: `keystore.location=classpath:security/zoomkeystore.jks`  See [*Create a Symmetric Key to Encrypt Data Source Passwords*](https://devnet.logianalytics.com/hc/en-us/articles/4405850928023-Create-a-Symmetric-Key-to-Encrypt-Data-Source-Passwords) for further guidance. |
| keystore.password | zoomkey | Lets you set up a unique password for the keystore. Example: `keystore.password=zoomkey` |
| keystore.key.alias | zoomkey | Example: `keystore.key.alias=zoomkey` |
| keystore.key.password | zoomkey | Example:`keystore.key.password=zoomkey` |
| Server SSL Properties | | |
| server.ssl.key-store | <Composer\_install\_directory>/conf/keystore | Sets the path for the keystore location. Example: `server.ssl.key-store=HOME/conf/keystore` |
| server.ssl.key-store-password | changeit | Stores the keystore password. Example: `server.ssl.key-store-password=<YourPassword>` |
| SAML Configuration Properties | | |
| saml.artifactBindingDefault | true | Example: `saml.artifactBindingDefault=true` |
| saml.useMultiValueList | true | Example: `saml.useMultiValueList=true` |
| saml.stringDelimiter | , | Example: `saml.stringDelimiter=;` |
| Kerberized PostgreSQL Properties | | |
| spring.datasource.connection-properties:jaasApplicationName | com.sun.security.jgss.initiate | Property that identifies the library to use for secure connection between PostgreSQL and the Composer Server. Example: `spring.datasource.connection-properties:jaasApplicationName=com.sun.security.jgss.initiate` |
| spring.datasource.url | jdbc:postgresql://<IP\_address>:<port>/zoomdata | The URL of the `zoomdata` database in the PostgreSQL metadata store. Example: `spring.datasource.url=jdbc:postgresql://localhost:5432/zoomdata` |
| spring.datasource.username | zoomdata | The user name for the `zoomdata` database in the PostgreSQL metadata store. Example: `spring.datasource.username=zoomdata` |
| spring.datasource.password | --- | The password associated with the user name for the `zoomdata` database in the PostgreSQL metadata store. |
| keyset.destination.params.jdbc\_url | jdbc:postgresql://<IP\_address>:<port>/zoomdata-keyset | The URL of the `zoomdata-keyset` database in the PostgreSQL metadata store. Example: `keyset.destination.params.jdbc_url=jdbc:postgresql://10.2.1.4:5432/zoomdata-keyset` |
| keyset.destination.params.user\_name | zoomdata | The user name for the `zoomdata-keyset` database in the PostgreSQL metadata store. Example: `keyset.destination.params.user_name=zoomdata` |
| keyset.destination.params.password | --- | The password associated with the user name for the `zoomdata-keyset` database in the PostgreSQL metadata store. |
| upload.destination.params.jdbc\_url | jdbc:postgresql://<IP\_address>:<port>/zoomdata-upload | The URL of the `zoomdata-upload` database in the PostgreSQL metadata store. Example: `upload.destination.params.jdbc_url=jdbc:postgresql://10.2.1.4:5432/zoomdata-upload` |
| upload.destination.params.user\_name | zoomdata | The user name for the `zoomdata-upload` database in the PostgreSQL metadata store. Example: `upload.destination.params.user_name=zoomdata` |
| upload.destination.params.password | --- | The password associated with the user name for the `zoomdata-upload` database in the PostgreSQL metadata store. |
| Source Sampling Properties | | |
| source.attribute.values.limit | 1000 | Example: `source.attribute.values.limit=1000` |
| Logging Properties | | |
| logging.level.com.zoomdata | INFO | Sets the log level for log messages in the Composer microservice log file. The following options are available for this property: TRACE, DEBUG, INFO, WARN, and ERROR. Example: `logging.level.com.zoomdata=DEBUG` |
| logging.unified.host | 127.0.0.1 | Sets the host IP address for [Fluentd server](https://www.fluentd.org/) message logging. For more information, see [*Set Up Unified Logging Using Fluentd*](https://devnet.logianalytics.com/hc/en-us/articles/4405859397655-Set-Up-Unified-Logging-Using-Fluentd).  Example: `logging.unified.host=123.4.5.6` |
| logging.unified.level | OFF | Sets the log level for messages logged to the [Fluentd server](https://www.fluentd.org/). The following options are available for this property: TRACE, DEBUG, INFO, WARN, ERROR, and OFF. If set to OFF, Fluentd unified logging is disabled. For more information, see [*Set Up Unified Logging Using Fluentd*](https://devnet.logianalytics.com/hc/en-us/articles/4405859397655-Set-Up-Unified-Logging-Using-Fluentd).  Example: `logging.unified.level=INFO` |
| logging.unified.port | 24224 | Sets the port for [Fluentd server](https://www.fluentd.org/) message logging. For more information, see [*Set Up Unified Logging Using Fluentd*](https://devnet.logianalytics.com/hc/en-us/articles/4405859397655-Set-Up-Unified-Logging-Using-Fluentd).  Example: `logging.unified.port=1234` |
| logging.unified.tag | zoomdata-server | Sets the microservice tag name for messages logged to the [Fluentd server](https://www.fluentd.org/). This is important because the tag identifies the microservice to which the log messages apply. Valid values are `query-engine`, `zoomdata-server`, `stream-writer`, `upload-service`, and `edc-<connector-name>` (where `<connector-name>` is one of the names listed in [*Connector Properties and Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files)). For more information, see [*Set Up Unified Logging Using Fluentd*](https://devnet.logianalytics.com/hc/en-us/articles/4405859397655-Set-Up-Unified-Logging-Using-Fluentd).  Example: `logging.unified.tag = zoomdata-server` |
| syslog.host | 127.0.0.1 | Sets the host IP address for [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) message logging. Example:  `syslog.host=127.0.0.1` |
| syslog.log.level | OFF | Sets the syslog log level for messages logged to the [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/). The following options are available for this property: TRACE, DEBUG, INFO, WARN, ERROR, and OFF. Example: `syslog.log.level=DEBUG` |
| syslog.port | 1514 | Sets the port for [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) message logging. Example:  `syslog.port=1514` |
| syslog.suffix | local | Specifies a suffix that is appended at the end of the [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) log entry that Composer generates. Example:  `syslog.suffix=local` |
| Password Policy | | |
| auth.password.policy.specialCharacters | !@#$%^&\*()-\_=+,.:;<> |  |
| auth.password.policy.minCharacters | 9 |  |
| auth.password.policy.maxCharacters | 255 |  |
| auth.password.policy.minLowercaseCharacters | 1 |  |
| auth.password.policy.minUppercaseCharacters | 1 |  |
| auth.password.policy.minNumericCharacters | 1 |  |
| auth.password.policy.minSpecialCharacters | 1 |  |
| auth.password.policy.helpMessage | Password must contain at least 9 characters including 1 lowercase, 1 uppercase, 1 number and 1 special (!@#$%^&\*()-\_=+,.:;<>). | Text is not enclosed in quotation marks. |
| Data Export Properties | | |
| zoomdata.export.data.max.cols | 1000 columns | Use this property to define the maximum number of columns that can be exported for two-dimensional visuals (such as a pivot table). Composer enforces this limit for visual data, but does not enforce it for raw data.  The distributed default for this setting is 1000 columns. Valid values can range from 0 through 2147483647 columns. |
| zoomdata.export.data.max.rows | 100000 rows | Use this property to define the maximum number of rows that can be exported for visuals. Composer enforces this limit for visual data. However, for raw data, Composer produces an error if the number of rows requested for export exceeds this setting.  The distributed default for this setting is 100000 rows. Valid values can range from 0 through 2147483647 rows. |
| Screenshot Microservice Client & Dashboard Scheduling Properties | | |
| screenshot.service.name | screenshot-service |  |
| screenshot.service.url | `http://localhost:8083/` |  |
| screenshot.service.http.client.connect.timeout.milliseconds | 10000 milliseconds | Specifies the number of milliseconds that can elapse before Composer stops trying to connect to the screenshot microservice client. |
| screenshot.service.http.client.read.timeout.milliseconds | 60000 milliseconds | Specifies the number of milliseconds that can elapse before Composer stops trying to read from the screenshot microservice client.  Note: If you increase the time set by the `dashboard.scheduling.screenshot.timeout` property, make sure that you increase the value of this property as well. The total time set by `screenshot.service.http.client.read.timeout.milliseconds` should always be greater than or equal to the time set by the `dashboard.scheduling.screenshot.timeout` property. Bear in mind that this property is specified in milliseconds, but the `dashboard.scheduling.screenshot.timeout` property is specified in seconds. |
| screenshot.service.http.client.write.timeout.milliseconds | 60000 milliseconds | Specifies the number of milliseconds that can elapse before Composer stops trying to write to the screenshot microservice client. |
| dashboard.scheduling.screenshot.png.height | 720 pixels | Identifies the height (in pixels) of the screenshot PNG file that will be sent. |
| dashboard.scheduling.screenshot.png.width | 1280 pixels | Identifies the width (in pixels) of the screenshot PNG file that will be sent. |
| dashboard.scheduling.screenshot.timeout | 60 seconds | Specifies the timeout (in seconds) to take a screenshot for a dashboard email report.  Note: The time specified by this property must be less than or equal to the time set by the `screenshot.service.http.client.read.timeout.milliseconds` property. If you increase the value of this property, make sure that you increase the value of the `screenshot.service.http.client.read.timeout.milliseconds property` accordingly. Bear in mind that this property is specified in seconds, but the `screenshot.service.http.client.read.timeout.milliseconds` property is specified in milliseconds. |
| mail.from |  | Specifies the email address identifying where the email comes from. |
| mail.login |  | Specifies the email login to use to access the mail server. |
| mail.password |  | Specifies the password associated with the email login identified in the `mail.login` property. |
| In addition, JavaMail API properties (Composer supports both IMAP and SMTP protocols) should be added to the `zoomdata.properties` file to identify the mail server and other mail properties required to use that server to send the scheduled dashboard (for example, `mail.smtp.auth, mail.smtp.host`, `mail.smtp.port`, `mail.imap.host`, and `mail.imap.port`). Complete descriptions of IMAP and SMTP protocol JavaMail properties can be found at these links:   * IMAP: <https://javaee.github.io/javamail/docs/api/com/sun/mail/imap/package-summary.html> * SMTP: <https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html> | | |
| Field Settings | | |
| zoomdata.detect.type.attribute.max.length | 200 characters | Use this property to set the maximum character length of attribute fields. If this limit is exceeded, the field will be recognized as a Text field. |
