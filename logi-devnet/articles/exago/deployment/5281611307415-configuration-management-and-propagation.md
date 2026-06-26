---
title: "Configuration Management and Propagation"
id: 5281611307415
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281611307415-Configuration-Management-and-Propagation
updated_at: 2022-05-03T22:08:20Z
---

# Configuration Management and Propagation

# Configuration Management and Propagation

Exago recommends installing at least three entirely separate environments: development, testing, and production. Designing an implementation strategy to move an Exago configuration from system to system is an inevitable and important process. As a highly-configurable environment, Exago consists of many components. This topic will describe these components, where they are located, why they need to be part of the implementation strategy, and how they should be propagated from system to system.

For the sake of being all-encompassing, this topic will assume that all components of Exago have been installed and are part of the deployment strategy. If you choose not to use one or more of these components, the respective sections may be skipped.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Many of the files listed below are impacted by the installer when updating to a new version of Exago. See [Updating Recommendations](https://devnet.logianalytics.com/hc/en-us/articles/5281618359959-Updating-Recommendations) and [Updating to the Latest Version (Potentially Breaking Changes)](https://devnet.logianalytics.com/hc/en-us/articles/5281637050775-Updating-to-the-Latest-Version-Potentially-Breaking-Changes-).

## Exago Components

An Exago installation could include the following components:

* [Web Application](#Web)
* [Web Service API](#Web2)
* [Scheduler Service](#Schedule)
* [Monitoring Service](#Monitori)
* [Extensibility DLLs](#Extensib) (Folder Management, Storage Management, Server Events, Action Events, Custom Functions, Scheduler Queue)

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

## Web Application

The primary configuration for any Exago system is done via the **Admin Console**. There are countless configurations made with the Admin Console that are saved to two separate files. One of these files is a clear-text, standards-based XML file named `WebReports.xml` by default. It is appropriate for source control repositories given its consistent and clear-text nature. The other file, `WebReports.xml.enc` (derived from the name of the associated XML file), is an encrypted version of that XML file.

The encrypted version of the XML file should be considered to be the deployable version of the configuration. As such, it would be passed to *Configuration Management* as part of the deployment process. It is not necessary to deploy both the clear-text and the encrypted versions of the configuration created with the Admin Console. All configuration files created by the **Admin Console** are saved in the Config directory of the Exago Web Application.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> When the configuration settings have been finalized, it is recommended that the **Admin Console** be disabled and the plain-text config file be moved to a secure location outside of the Config directory. For more information refer to the [Security Checklist](https://devnet.logianalytics.com/hc/en-us/articles/5281588834455-Security-Checklist).

Due to the fact that the configuration should progress from development to testing environments, and eventually to production via controlled processes, the Admin Console should only exist in development. While the Admin Console is installed as part of Exago’s base installation, it should be removed from any system outside of development.

In addition to the primary Exago configuration created using the Admin Console, there are numerous additional configuration files that may be relevant. All of these are optional, created or edited manually via a text editor on an as-needed basis, and override existing features or provide additional functionality. These files are saved as clear-text and are appropriate for source control repositories.

### Language Files

All language files are saved as clear-text, standards-based XML files in the `<WebApp>\Config\Languages` directory.

### Data Source Customization

Data Source customizations are saved as clear-text, standards-based JSON in the `<WebApp>\Config\Other` directory.

### Application Themes

Application Themes include CSS, fonts, and images typically replicated saved in the `<WebApp>\ApplicationThemes` directory.

### Element-Level Themes

Element-level theme files are saved as clear-text, proprietary-format files, and are created in a variety of ways. These files are used for the styling of Charts, CrossTab Reports, Express Reports, and GeoCharts, and are saved in the `<WebApp>\Themes` directory for *pre-v2020.1* versions, and in the Storage Management database for *v2020.1+*.

### Folder Management and Monitoring Configuration

A separate config file used for providing configurations for Folder Management or Monitoring, located in `<WebApp>`.

### Web Application Server Configuration

A separate config file used for providing configuration details to the Web Application server and/or Exago itself, this file is frequently modified. Common Exago configurations are used to set cookieless sessions, activate state servers, set connection strings, and add custom headers. This file is located in `<WebApp>`.

### Database Drivers and Fonts

Database drivers may also be added to the system, assuming that the system doesn’t ship with the appropriate divers already. These drivers would be saved as DLLs in the `<WebApp>\Drivers` directory.

Similarly, custom fonts may be included in the system. These would be saved in the `<WebApp>\Fonts` directory.

Due to the fact that these files are compiled components and are likely provided by third parties, drivers and fonts are likely not source code repository friendly, and would also need to be propagated from development through to production.

## REST Web Service API

The **REST Web Service API** is an optional component. If applicable the Web Service API requires some configurable components similar to those listed as components of the Web Application. The following pertain to the Web Service API exactly as they pertain to the Web Application:

* Data Source customizations
* Drivers

In addition to the above, there are two clear-text configuration files that can be customized, based on the needs of the Web Service API itself:

### XML File

The Web Service API XML file, defaulted as `WebReportsApi.xml`, is a clear-text, standards-based XML file, and is used to configure the connection between the Web Service API and the Web Application installation. It is located in the `<WebSvc>\Config` directory.

### appSettings.config

The configuration file is a clear-text, standards-based XML file, and is used to activate the Web Service API. It is located in `<WebSvc>`.

## Scheduler Service

The **Scheduler Service** is an optional component that executes reports an requires configurable components similar to those listed as components of the Web Application. The following pertain to the Scheduler Service exactly as they pertain the Web Application:

* Language files
* Data Source customizations
* Drivers
* Fonts

In addition to the above, there are two clear-text configuration files that can be customized based on the needs of the Scheduler itself:

### XML File

The Scheduler configuration file, defaulted to `<Sched>\eWebReportsScheduler.xml`, is a standards-based XML file that includes configurations such as SMTP server connectivity configurations, communication channel and port information for connection to Exago itself, and many other configuration specific to the Scheduler Service.

### eWebReportsScheduler.exe.config

The Scheduler XML configuration file, defaulted to `<Sched>\bin\eWebReportsScheduler.exe.config`, is a standards-based XML file and is analogous to the Web Application’s `web.config` file and may include configurations described previously.

## Monitoring Service

Other than the monitoring configuration mentioned in the Web Application section, additional configurations can be made in the `Monitoring.exe.config` file. This file is formatted similar to the web application web.config file and saved in `<WebApp>\MonitoringService`.

Additionally, the current Monitoring implementation produces an SQLite database that is saved in `<WebApp>\Monitoring`. While this database is not configurable, if Monitoring is configured, its maintenance should be taken under consideration by Configuration Management.

## Extensibility DLLs

While these are entirely optional components, Exago is frequently and extensively customized via custom code compiled to DLLs. While these DLLs are configured via the aforementioned **Admin Console**, they need only be accessible via file system, meaning that they do not need to be deployed as part of Exago’s configuration. However, typical implementations of custom DLLs require components of Exago DLLs to be referenced, and, as such, require the maintenance of these custom implementations to be taken into consideration by Configuration Management.
