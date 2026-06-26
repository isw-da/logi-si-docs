---
title: "Application Settings"
id: 5281615366423
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings
updated_at: 2023-04-03T17:52:19Z
---

# Application Settings

# Application Settings

Some options need to be loaded by the web server at runtime. XML files located at the root of:

* Exago Web Application install path
  + `appSettings.config`
  + `web.config`
* Web Service API install path
  + `appSettings.config`
* and Scheduler Service install paths
  + `eWebReportsScheduler.exe.config`

allow for these additional options to be configured.

To apply a setting, add an XML key in the `<appSettings />` node with “key” and “value” parameter pairs, in the following form:

```
<add key="key" value="value" />
```

The following topic is a collection of all the possible app settings, and descriptions for their use. In general, you should not use any of these settings unless you have been specifically directed by an Exago Inc. staff member. Keys and values are **case sensitive**.

## Web Application

### `web.config`

#### sessionState

#### cookieless v2018.1+

Enable or disable **[Cookieless Sessions](https://devnet.logianalytics.com/hc/en-us/articles/5281619580311-Cross-Origin-Embedding-of-Exago-BI#Cookiele)**. Possible values:

* *True*
* *False*

#### mode

* *InProc* (default) *—* in-process session storage
* *Custom* — session storage is being handled by a custom state server (for example Redis, Elasticache). See [Setting up a State Server](https://devnet.logianalytics.com/hc/en-us/articles/5281581463959-Setting-up-a-State-Server) for more information.

#### timeout

Editing this attribute is not supported.

Example:

```
<sessionState mode="InProc" cookieless="false" timeout="20" />
```

### `appSettings.config`

#### AccessControlAllowCredentials v2019.2.29+v2020.1.13+v2021.1.1+

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5851201783703/noteicon.jpg "Note")
>
> As of *v2019.2.29*, *v2020.1.13* and *v2021.1.1*, this option in conjunction with **CorsAllowedOrigins** (below) should be the only way of setting these headers for new installations. Exago no longer recommends manually adding them via the web server’s configuration except when directed by our Support Group.
>
> For more information, refer to the [Cross-Origin Embedding of Exago BI](https://devnet.logianalytics.com/hc/en-us/articles/5281619580311-Cross-Origin-Embedding-of-Exago-BI) topic.

When the Web Application is accessed at a different origin than the embedding host application, use **AccessControlAllowCredentials** to control the existence and value of the `Access-Control-Allow-Credential` header in HTTP responses from the Exago web server.

The only case-sensitive allowed value is *true*. To disable the `Access-Control-Allow-Credential` header, omit this setting from the file.

This setting only applies to the version numbers listed above and subsequent versions. For previous versions, refer to the [Cross-Origin Embedding of Exago BI](https://devnet.logianalytics.com/hc/en-us/articles/5281619580311-Cross-Origin-Embedding-of-Exago-BI) topic for details setting the web server’s configuration files instead.

Example:

```
<add key="AccessControlAllowCredentials" value="true" />
```

#### CorsAllowedOrigins v2019.2.29+v2020.1.13+v2021.1.1+

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5851145968663/criticalicon.gif "Important")
>
> As of *v2019.2.29*, *v2020.1.13* and *v2021.1.1*, this option in conjunction with **AccessControlAllowCredentials** (above) should be the only way of setting these headers for new installations. Exago no longer recommends manually adding them via the web server’s configuration except when directed by our Support Group.
>
> For more information, refer to the [Cross-Origin Embedding of Exago BI](https://devnet.logianalytics.com/hc/en-us/articles/5281619580311-Cross-Origin-Embedding-of-Exago-BI) topic.

When the Web Application is accessed at a different origin than the embedding host application, use **CorsAllowedOrigins** to control the existence and value of the `Access-Control-Allow-Origin` header in HTTP responses from the Exago web server.

Set the *value* attribute to a comma-separated list of origins of pages embedding Exago. The wild card (\*) character may be used in the list entries.

Exago will set `Access-Control-Allow-Origin` to the origin(s) in the *value* attribute.

Examples:

```
<add key="CorsAllowedOrigins" value="https://domain1.com" />
<add key="CorsAllowedOrigins" value="https://domain1.com,https://domain2.com" />
<add key="CorsAllowedOrigins" value="https://s1.domain1.com,https://s2.domain1.com" />
<add key="CorsAllowedOrigins" value="https://*.domain1.com" />
```

This setting only applies to the version numbers listed above and subsequent versions. For previous versions, refer to the Cross-Origin Embedding of Exago topic for details setting the web server’s configuration files instead.

### EncryptionIV v2020.1.35+v2020.1.23+v2021.2.6+

**EncryptionKey**

```
<add key="EncryptionIV" value="YWJjZGVmMTIzNDU2Nzg5MA=="/>
```

### EncryptionKey v2020.1.35+v2020.1.23+v2021.2.6+

**EncryptionIV**

```
<add key="EncryptionKey" value="MTIzNDU2Nzg5MGFiY2RlZg=="/>
```

### maxPuppeteerPages v2020.1.0+

If [useWkHtmlToImage v2019.1.5+](#useWkHtm) is *False*, Exago will use the Puppeteer rendering library. Puppeteer allots a certain number of “browser pages” for rendering charts in exports. This setting tells Exago the maximum number of pre-allocated browser pages to make available on the server for rendering. A larger number will consume more system resources.

Possible values:

* **Default value:***4*
* Any valid integer value greater than *0*, although no more than *100* is recommended.

Example:

```
<add key="maxPuppeteerPages" value="20" />
```

### maxRasterizationsBeforeReset v2021.1.7+

If [useWkHtmlToImage v2019.1.5+](#useWkHtm) is *False*, Exago will use the Puppeteer rendering library. Puppeteer uses “browser pages” for rendering charts in exports. This value sets the number of charts that each page may render before it is released and a new page is generated. Disposing of Puppeteer browser pages frees up memory on the server.

Possible values:

* **Default value:***1000*
* Any valid integer value greater than *0*.  
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5851201783703/noteicon.jpg "Note")
  >
  > Setting this value too high could cause out-of-memory errors. Setting it too low could impact performance as the process must be started and stopped frequently.

Example:

```
<add key="maxRasterizationsBeforeReset" value="2000" /><add key="maxRasterizationsBeforeReset" value="100" />
```

### maxWaitForPuppeteerResource v2020.1.0+

If [useWkHtmlToImage v2019.1.5+](#useWkHtm) is *False*, Exago will use the Puppeteer rendering library. Puppeteer allots a certain number of “browser pages” for rendering charts in exports. If a page is not available to render a chart, Exago will wait this number of seconds for one to become available.

If no Puppeteer browser page becomes available, an “Unable to acquire a browser page. Ran out of time waiting for a resource to become available.” error message will be displayed

Possible values:

* **Default value:***60*
* Any valid integer value greater than *0*, and the value should generally be quite a bit less than the **Admin Console** > **General** > **Other Settings** > **Max Report Execution Time (minutes)** value. Note though, that **maxWaitForPuppeteerResource** is in *seconds* and **Max Report Execution Time** is in *minutes*.

Example:

```
<add key="maxWaitForPuppeteerResource" value="120" />
```

### SameSiteCookiesMode v2019.1.14+

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5851145968663/criticalicon.gif "Important")
>
> When Exago is accessed from a different origin than the host application and cookies are used to maintain session state, Exago must be accessed via HTTPS. If you cannot use HTTPS to embed Exago in this scenario, cookieless sessions must be turned on.

Possible values:

* *Default* (default) — If the user-agent (browser) supports it, `SameSite=None; Secure` will be added to the **Set-Cookie** HTTP header. If the user-agent does not support `SameSite=None; Secure`, the `SameSite` directive is removed entirely from the header.
* *Off* — Exago will not affect the `SameSite` directive when setting session cookies.

#### sessionStorage

Determine which method to use to store session information for the user’s configuration.

Possible values:

* *Diff* (default) — Store the “diff” between the user’s config and the base config.
* *InMemory* — Store the entire effective config in session.

#### inputSanitizationMethod

Determine how aggressively to sanitize user-input data, such as report name, description, etc., against script attacks.

Possible values:

* *Safe* (default) — Sanitizes against a blacklist of html tags and attributes. Less likely to alter user input.
* *Aggressive* — Sanitizes against a white list of html tags. Potentially more harmful to user input. As of *v2016.3.7+* the white list located at `{webAppInstallDir}ConfigOthertagwhitelist.json`

#### ExagoConfigPath

Specifies the location of the WebReports.xml config file when storing the config in a Cloud (Azure/Amazon) location. See **[Installing Exago on Azure](https://devnet.logianalytics.com/hc/en-us/articles/5281601143191-Installing-Exago-on-Azure)** for details.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5851201783703/noteicon.jpg "Note")
>
> When both the REST Web Service API and cloud config storage are being used, the `ExagoConfigPath` entry must be placed in both the REST Web Service API’s and Web Application’s copy of **appSettings.config**.

#### ShowErrorDetail

Set to false to disable the ability to append `?ShowErrorDetail=true` to an Exago URL to see the full text of error messages. See **[See Full Error Details](https://devnet.logianalytics.com/hc/en-us/articles/5281647422487-See-Full-Error-Details)** for details.

Possible values:

* *False* — Show the generic error text. Overrides the URL flag.

### enableantiforgery v2016.2.12+

Enable protection for Cross-Site Request Forgery (CSRF) attacks.

Possible values:

* *True* — Enable anti-forgery protection.

### MinCompactionInterval v2016.2.12+

At specified intervals during .NET Garbage Collection, Exago will attempt to compact the large object heap in order to reduce memory consumption by eliminating fragmentation. This will only happen in a .NET 4.5.1**+** environment.

Possible values:

* *Any positive integer including 0* — The minimum number of minutes between compaction cycles. *3* is the default.
* *-1* — Disable compaction.

### SecurityProtocol v2016.3.4+

Specify which security protocols the Web Application should use. Multiple values are separated by commas (,).

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5851145968663/criticalicon.gif "Important")
>
> The **Web Application**, **Scheduler Service**, **Web Service API** and any cloud storage mechanisms must share at least one security protocol in common otherwise they will not be able to communicate with each other.

Possible values (one or more):

* *Ssl3* — SSL 3.0
* *Tls* — TLS 1.0
* *Tls11* — TLS 1.1
* *Tls12* — TLS 1.2
* *Tls13* — TLS 1.3 (*.NET v4.6+*)

Example:

```
<add key="SecurityProtocol" value="Tls11,Tls12" />
```

### Monitoring v2017.1+

Encompasses several keys determining which monitoring data is collected by the application. See **[Configuring Monitoring](https://devnet.logianalytics.com/hc/en-us/articles/5281636945431-Monitoring-Setup#Configur)** for details.

### useSecurityToken v2018.1+

Enable two-factor authentication for **[Cookieless Sessions](https://devnet.logianalytics.com/hc/en-us/articles/5281619580311-Cross-Origin-Embedding-of-Exago-BI#Cookiele)** (the web server must enforce a secured connection).

Possible values:

* *True* — Enable security token.

### LoadAssemblyInExternalDomain v2018.2+

Load Assembly Data Sources in an external domain, as opposed to the application domain. If enabling this feature, it should also be set in the Scheduler’s `eWebReportsScheduler.xml` and `eWebReportsScheduler.exe.config` files.

Possible values:

* *True* — Enable
* *False* (default) — Disable

### useWkHtmlToImage v2019.1.5+

Revert to using the older WkHtmlToImage library for exporting visualizations. Only set to true if you are experiencing an incompatibility with Puppeteer.

In *v2020.1* this flag has been changed to default to *False*, as Puppeteer is the default visualization rendering library in that version.

Possible values:

* *True* — Use the WkHtmlToImage library for visualization rendering
* *False* — Use Puppeteer library for visualization rendering

### cacheConfig v2018.1+

Set to *True* to cache the configuration data in the session. This can increase performance when using extremely large config files. Default value is *False*.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5851145968663/criticalicon.gif "Important")
>
> Any in-session operations which modify the configuration will cause erroneous behavior. Such operations include: OnConfigLoadEnd server event, advanced joins, vertical table transformations.

## Scheduler Services

### `eWebReportsScheduler.exe.config`

#### maxPuppeteerPages v2020.1.0+

If [useWkHtmlToImage v2019.1.5+](#useWkHtm2) is *False*, Exago will use the Puppeteer rendering library. Puppeteer allots a certain number of “browser pages” for rendering charts in exports. This setting tells Exago the maximum number of pre-allocated browser pages to make available on the server for rendering. A larger number will consume more system resources.

Possible values:

* **Default value:***4*
* Any valid integer value greater than *0*, although no more than *100* is recommended.

Example:

```
<add key="maxPuppeteerPages" value="20" />
```

#### maxRasterizationsBeforeReset v2021.1.7+

If [useWkHtmlToImage v2019.1.5+](#useWkHtm2) is *False*, Exago will use the Puppeteer rendering library. Puppeteer uses “browser pages” for rendering charts in exports. This value sets the number of charts that each page may render before it is released and a new page is generated. Disposing of Puppeteer browser pages frees up memory on the server.

Possible values:

* **Default value:***1000*
* Any valid integer value greater than *0*.  
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5851201783703/noteicon.jpg "Note")
  >
  > Setting this value too high could cause out-of-memory errors. Setting it too low could impact performance as the process must be started and stopped frequently.

Examples:

```
<add key="maxRasterizationsBeforeReset" value="2000" />
<add key="maxRasterizationsBeforeReset" value="100" />
```

#### maxWaitForPuppeteerResource v2020.1.0+

If [useWkHtmlToImage v2019.1.5+](#useWkHtm2) is *False*, Exago will use the Puppeteer rendering library. Puppeteer allots a certain number of “browser pages” for rendering charts in exports. If a page is not available to render a chart, Exago will wait this number of seconds for one to become available.

If no Puppeteer browser page becomes available, an “Unable to acquire a browser page. Ran out of time waiting for a resource to become available.” error message will be displayed

Possible values:

* **Default value:***60*
* Any valid integer value greater than *0*, and the value should generally be quite a bit less than the `<max_job_execution_minutes>` and `<default_job_timeout>` settings in the [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration). Note though, that **maxWaitForPuppeteerResource** is in *seconds* and `<max_job_execution_minutes>` is in *minutes*.

Example:

```
<add key="maxWaitForPuppeteerResource" value="120" />
```

#### configFile

Specify the path and file name of the scheduler config file. Typically used in a multi-scheduler configuration where it would be desirable to maintain a global config file for all of them. If not specified, the scheduler will look for the config file in the default location.

#### MinCompactionInterval v2016.2.12+

At specified intervals, during .NET Garbage Collection, Exago will attempt to compact the large object heap in order to reduce memory consumption by eliminating fragmentation. This will only happen in a .NET 4.5.1+ environment.

Possible values:

* *Any positive integer including 0* — The minimum number of minutes between compaction cycles. *3* is the default.
* *-1* — Disable compaction.

#### Monitoring.CollectExecuteReportUsage v2017.1+

Specify whether to collect data about the report executions handled by this scheduler.

Possible values:

* *True* — Enable collecting report execution data.

#### inputSanitizationMethod

Determine how aggressively to sanitize user-input data, such as report name, description, etc., against script attacks.

Possible values:

* *Safe* (default) — Sanitizes against a blacklist of html tags and attributes. Less likely to alter user input.
* *Aggressive* — Sanitizes against a white list of html tags. Potentially more harmful to user input. As of *v2016.3.7+* the white list located at `{schedulerInstallDir}tagwhitelist.json`

#### useWkHtmlToImage v2019.1.5+

Revert to using the older WkHtmlToImage library  for exporting visualizations. Only set to true if you are experiencing an incompatibility with Puppeteer.

In *v2020.1* this flag has been changed to default to *False*, as Puppeteer is the default visualization rendering library in that version.

Possible values:

* *True* — Use the WkHtmlToImage library for visualization rendering
* *False* — Use Puppeteer library for visualization rendering

## REST Web Service API

### `appSettings.config`

#### maxPuppeteerPages v2020.1.0+

If useWkHtmlToImage is *False*, Exago will use the Puppeteer rendering library. Puppeteer allots a certain number of “browser pages” for rendering charts. This setting tells Exago the maximum number of pre-allocated browser pages to make available on the server for rendering.

Possible values:

* **Default value:***4*
* Any valid integer value greater than *0*, although no more than *100* is recommended.

#### maxWaitForPuppeteerResource v2020.1.0+

If useWkHtmlToImage is *False*, Exago will use the Puppeteer rendering library. Puppeteer allots a certain number of “browser pages” for rendering charts. If a page is not available to render a chart, Exago will wait this number of seconds for one to become available.

If no Puppeteer browser page becomes available, an “Unable to acquire a browser page. Ran out of time waiting for a resource to become available.” error message will be displayed

Possible values:

* **Default value:***60*
* Any valid integer value greater than *0*, and the value should generally be quite a bit less than the **Admin Console** > **General** > **Other Settings** > **Max Report Execution Time (minutes)** value. Note though, that **maxWaitForPuppeteerResource** is in *seconds* and **Max Report Execution Time** is in *minutes*.

Example:

```
<add key="maxWaitForPuppeteerResource" value="120" />
```

#### ExagoRest

Add this key to enable use of the **REST Web Service API**.

Possible values:

* *True* — Enable the REST Web Service API.

#### SecurityProtocol v2016.3.4+

Specify which security protocols the Web Service should use. Multiple values are separated by commas (,).

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5851145968663/criticalicon.gif "Important")
>
> The **Web Application**, **Scheduler Service**, **Web Service API** and any cloud storage mechanisms must share at least one security protocol in common otherwise they will not be able to communicate with each other.

Possible values (one or more):

* *Ssl3* — SSL 3.0
* *Tls* — TLS 1.0
* *Tls11* — TLS 1.1
* *Tls12* — TLS 1.2
* *Tls13* — TLS 1.3 (*.NET v4.6+*)

Example:

```
<add key="SecurityProtocol" value="Tls11,Tls12" />
```

#### aspnet:MaxJsonDeserializerMembers

Sets the maximum number of JSON items that can be processed in a single Web Service API call. When not included in the file, the application uses *1000* for this setting.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5851201783703/noteicon.jpg "Tip")
>
> Increasing this value can help eliminate “*The JSON request was too large to be deserialized*” error messages when making large BATCH Web Service API calls.

Possible values:

* **Suggested value:***10000*
* Any integer value between *1* and *2147483647*

#### ExagoConfigPath

Specifies the location of the WebReports.xml config file when storing the config in a Cloud (Azure/Amazon) location. See **[Installing Exago on Azure](https://devnet.logianalytics.com/hc/en-us/articles/5281601143191-Installing-Exago-on-Azure)** for details.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5851145968663/criticalicon.gif "Important")
>
> When both the REST Web Service API and cloud config storage are being used, the `ExagoConfigPath` entry must be placed in both the REST Web Service API’s and Web Application’s copy of **appSettings.config**.
