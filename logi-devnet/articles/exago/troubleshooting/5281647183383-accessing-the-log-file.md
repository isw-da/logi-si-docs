---
title: "Accessing the Log File"
id: 5281647183383
section: "Troubleshooting"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281647183383-Accessing-the-Log-File
updated_at: 2022-05-03T22:07:47Z
---

# Accessing the Log File

# Accessing the Log File

Exago keeps a text log of when certain tasks are performed. For example each time a page or report is loaded, each time an error occurs or when various phases of execution happen.

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

To configure logging, see [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings).

## Web Application Log

To access the log file:

1. Ensure that in the **Admin Console** that **General** > **Other Settings** > **Write Log File** is set to *Debug*.
2. Recreate the error you are investigating.
3. Navigate to the folder specified in **General** > **Main Settings** > **Temp Path**. If this is blank go to `<WebApp>\Temp`. If **General** > **Scheduler Settings** > **Enable Remote Report Execution** is set to *True* the report execution is recorded in the [Scheduler Log](#Schedule).
4. Open the file **WebReportsLog.txt**. Scroll to the bottom of the file for the most recent activity.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Occasionally IIS may lock this file and prevent the log from being written. To correct this problem, see [Application and Performance Logging](https://devnet.logianalytics.com/hc/en-us/articles/5281670339479-Application-and-Performance-Logging).

## Scheduler Service & Remote Execution Log

Similar to the Web Application, the **Scheduler Service** maintains a log file. Considering the Scheduler can reside on a different machine than the main application, the log file is written where the Scheduler is installed.

Since **Remote Execution** is handled by Scheduler Services, if Remote Execution is enabled in the environment, all report execution will be logged into the Scheduler Service’s log.

To access the Scheduler Service log file:

1. Set `<logging>` to *on* in the [Scheduler Service’s configuration file](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration).
2. Rerun the scheduled report under investigation.
3. Open the file `<Sched>\eWebReportsScheduler.log`. Scroll to the bottom of the log for the most recent activity.

## REST Web Service API Log

Similar to the Web Application, the **Web Service API** maintains a log file. Considering the Web Service API can reside on a different machine than the Web Application, the log file is written where the Web Service is installed.

To access the Web Service API log file:

1. Set `<writelog>` to *True* in the Web Service API’s configuration file.
2. Rerun the project that makes the API calls under investigation.
3. Open the file `<Temp>\WebReportsApiLog.txt`. Scroll to the bottom of the file for the most recent activity.

## .NET API Log

Some implementations of the .NET API may write to a log file as well. For versions prior to *v2018.1*, the API logs to the same file as the Web Application.In *v2018.1+*, the log file for the built-in logging methods defaults to `<Temp>\WebReportsApiLog.txt`.
