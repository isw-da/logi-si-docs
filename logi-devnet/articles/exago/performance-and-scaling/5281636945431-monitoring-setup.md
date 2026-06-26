---
title: "Monitoring: Setup"
id: 5281636945431
section: "Performance and Scaling"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281636945431-Monitoring-Setup
updated_at: 2022-05-03T22:07:55Z
---

# Monitoring: Setup

# Monitoring: Setup

**Monitoring** that allows report management, execution, and performance statistics for the web application and schedulers to be tracked in *v2017.1+*. Monitoring data is stored in local SQLite database files and can be reported on using Exago.

Many actions in the application can be monitored:

* Report Management
  + Edit
  + Execute (begin & end)
  + Save
  + Delete
  + Rename
  + Duplicate
* Report Designer usage
  + Gauge Wizard
  + Google Map Wizard
  + GeoChart Wizard
  + Map Wizard
* Scheduling
  + Scheduled report
  + Schedule Manager

Monitoring for these components can be toggled on or off.

Additionally, you can track CPU and memory load for each scheduler application so you can fine-tune the load balancing setup.

When the Exago Web Application is installed, the monitoring system is automatically installed, but it is disabled by default. It must be configured and enabled manually. To set up monitoring, you need to configure the monitoring application, set the options for which data to collect, and then set the monitoring service to run automatically.

## Configuring Monitoring

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

The monitoring system is located in a folder `MonitoringService`, in the same folder as where the Web application is installed. The web application stores its monitoring data in a `Monitoring` subfolder of the installation. So you should have the following folders:

* <WebApp>
  + Monitoring
* MonitoringService

Windows: Ensure that the IIS user has Full Control permissions for the `ExagoWebMonitoring` and `MonitoringService` folders. See **[Configuring IIS for Exago BI](https://devnet.logianalytics.com/hc/en-us/articles/5281623851287-Configuring-IIS-for-Exago-BI)** for instructions.

To configure monitoring:

1. In `MonitoringService`, open the file `Monitoring.exe.config` in a text or xml editor. For each of the following keys in the `<appSettings>` element, set the values as follows:
   * `exagoAppPath, value="path"` where `path` is the file path to the web app  
     **Format:** `"C:filepath"` (Windows), `"/file/path/"` (Linux)  
     A trailing slash () or (/) is required
   * `userConfig, value="config"` where `config`is the application config file  
     **Format:** `"file name.xml"`Use extension `.xml` for either the encrypted or unencrypted version
   * `webAppUri, value="uri"` where `uri` is the url virtual path to the web app  
     **Format:** `"http://local/path/"`A trailing backslash (/) is required
   * Optional: `ExtractionIntervalMinutes, value="i"` where `i` is the number of minutes between updates to the core database. The default is 3.
   * Optional: `StatisticsIntervalMinutes, value="j"` where `j` is the number of minutes between when each scheduler is polled for performance statistics. The default is 1.

   ### Example

   ```
   <appSettings>
   	<add key="ExtractionIntervalMinutes" value="3" />
   	<add key="StatisticsIntervalMinutes" value="1" />
   	<add key="exagoAppPath" value="C:ExagoWeb" />
   	<add key="userConfig" value="WebReports.xml" />
   	<add key="webAppUri" value="http://localhost/monitoring/" />
   </appSettings>
   ```
2. In `<WebApp>`, open the file `appSettings.config` in a text or xml editor. In the `<appSettings>` element, set the `Monitoring.DbPath` key to the folder where the web application’s monitoring data file is. The default location is `<WebApp>Monitoring`.  

   ### Example

   ```
   <appSettings>
   	<add key="Monitoring.DbPath" value="C:ExagoExagoWebMonitoring" />
   	...
   </appSettings>
   ```
3. In the same file, set the options for which types of usage data you want to collect. To turn on monitoring for a specific action, set the value for the key to “true”. Available options are as follows:
   * Monitoring.CollectDeleteReportUsage
   * Monitoring.CollectRenameReportUsage
   * Monitoring.CollectDuplicateReportUsage
   * Monitoring.CollectExecuteReportUsage
   * Monitoring.CollectSaveReportUsage
   * Monitoring.CollectSaveReportXmlUsage
   * Monitoring.CollectDesignReportUsage
   * Monitoring.CollectGaugeControlUsage
   * Monitoring.CollectGoogleMapControlUsage
   * Monitoring.CollectMapControlUsage
   * Monitoring.CollectChartControlUsage
   * Monitoring.CollectScheduleReportControlUsage
   * Monitoring.CollectScheduleReportManagerControlUsage

   ### Example

   ```
   <appSettings>...
   	<add key="Monitoring.CollectDeleteReportUsage" value="true" />
   	<add key="Monitoring.CollectRenameReportUsage" value="false" />
   	<add key="Monitoring.CollectDuplicateReportUsage" value="true" />
   	<add key="Monitoring.CollectExecuteReportUsage" value="true" />
   	...
   </appSettings>
   ```
4. Restart the web server for the changes to be applied.

### Configuring Scheduler Monitoring

If you want to track scheduled report execution, do the following for each **Scheduler Service** installation:

Open the `eWebReportsScheduler.exe.config` file in a text or XML editor. Add the following key to the `<appSettings>` element:

```
<add key="Monitoring.CollectExecuteReportUsage" value="true" />
```

## Enabling the Monitoring Service

The monitoring system uses a Windows or Linux service that updates the core database with data from the **Web Application** and **Scheduler Services** at specified intervals. This way you have the data from every component in a single location.

The service is installed automatically, but it is not enabled by default. To enable the service:

### Windows

1. As an administrator, open the Windows Services manager:
   1. Click **Start**>**Run**.
   2. Type `services.msc`.
   3. Press Enter.
2. Locate the service `Exago Monitoring Service vX.X.X.X`, where `vX.X.X.X` is the Exago BI version. Right-click the service and select **Properties**.
3. In the Properties window:
   1. From the Startup Type list, select **Automatic**.
   2. Click **Start** to start the service.
   3. Click **OK**.

## Accessing the Monitoring Data With Exago

To use monitoring data in reports, you need to add the Monitoring Service’s core database file `MonitoringService/Monitoring.sqlite` as an Exago Data Source.

## Recommended Resources

* [Using SQLite Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5281627628951-Using-SQLite-Data-Sources)
* [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5281617045911-Data-Sources)
