---
title: "Monitoring: System Overview"
id: 5281617942679
section: "Performance and Scaling"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281617942679-Monitoring-System-Overview
updated_at: 2022-05-03T22:08:51Z
---

# Monitoring: System Overview

# Monitoring: System Overview

The Monitoring system is structured in the following manner:

![MonitoringSystem.png](https://devnet.logianalytics.com/hc/article_attachments/5432183723799/monitoringsystem.png)

Structure of the monitoring system

### Web Application Database

The Web Application database stores data for report and user interface events. The type of data tracked depends on the configuration. At the Extract interval, the monitoring service moves this data from the local db to the collected db.

### Scheduler Application Databases

Each Scheduler Service has a local database which stores report execution data, if enabled in the configuration. At the Extract interval, the monitoring service moves this data from the local dbs to the collected db.

Scheduler performance data is “persistent,” that is, always available, and is therefore not stored in the local scheduler databases. At the Statistics interval, the monitoring service polls the schedulers for their performance statistics, and logs this data in the collected db.

### File Paths for Config Files & Databases

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

* `<WebApp>Monitoring\Monitoring.sqlite` – WebApp db
* `<WebApp>appSettings.config` – Select which web app data to track
* `MonitoringService\Monitoring.sqlite` – Main collected db
* `MonitoringService\Monitoring.exe.config` – Set Extraction & Statistics intervals
* `<Sched>Monitoring.sqlite` – Scheduler local db
* `<Sched>eWebReportsScheduler.exe.config` – Select which scheduled report data to track
