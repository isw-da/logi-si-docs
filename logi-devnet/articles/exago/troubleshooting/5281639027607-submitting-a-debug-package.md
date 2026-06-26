---
title: "Submitting a Debug Package"
id: 5281639027607
section: "Troubleshooting"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281639027607-Submitting-a-Debug-Package
updated_at: 2022-05-03T22:08:46Z
---

# Submitting a Debug Package

# Submitting a Debug Package

If the **Admin Console** > **General** > **Other Settings** > **Debug Password** is set, a client will have the ability to submit **Debug Packages** automatically to Exago, Inc. via the internet.

A copy of the report definition, the Exago configuration file, and the data set used to generate the report will be transmitted to Exago’s Support Team.

## Automatically Creating a Debug Package

To send a Debug Package to Exago Support automatically through the Web Application user interface:

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> The automatic debug packager only works with single **Advanced Reports**, ![TreeAdvancedReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432192105239/treeadvancedreport.png)**CrossTab Reports**, ![TreeExpressReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432173711639/treeexpressreport.png)**Express Reports**and ![TreeExpressView.png](https://devnet.logianalytics.com/hc/article_attachments/5432206928151/treeexpressview.png)**ExpressViews**. Contact Exago’s Support Team directly when troubleshooting **Advanced Reports** with linked reports (a.k.a. drilldowns), ![TreeChainedReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432180048407/treechainedreport.png)**Chained Reports** or ![TreeDashboardReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432192292631/treedashboardreport.png)**Dashboards**.

1. From the **Report Tree**, select the report under test.
2. Press **Ctrl + Shift + X**.
3. In the Debug Package dialog:  
   ![firefox_FjglTqTkwj.png](https://devnet.logianalytics.com/hc/article_attachments/5432192342807/firefox_fjgltqtkwj.png)

   Debug Package dialog

   1. Enter the **Debug Password** (set in the **Admin Console** > **General** > **Other Settings**).
   2. Enter either the ticket ID number or the entire URL to the ticket in the **Exago Support Ticket URL or Ticket ID** field.
   3. Enter a **Contact Email Address**.
4. Click **Okay** to begin the report execution process. If the report has any prompting filters or parameters, enter values for them when prompted.

A success/failure message will display when the process finishes. Click **Dismiss**. A confirmation email will be sent to the email in the **Contact Email Address** field.

![Debug package successfully sent to Exago, Inc.](https://devnet.logianalytics.com/hc/article_attachments/5432122110231/rdtn0dmyev.png)

## Manually Creating a Debug Package

If a debug package cannot be sent [automatically](#Automati), a package may be created manually instead. The files can be zipped and directly attached to a ticket request.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Before manually creating a debug Package verify that **Admin Console** > **General** > **Scheduler Settings** > **Enable Remote Report Execution** is set to *False*

To manually create a Debug Package:

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

1. Create the `<WebApp>/Debug` folder if it doesn’t already exist in the file system.
2. Make sure `<WebApp>/Debug` has the same read/write permissions as the Report and Temp Folders.
3. Set **Admin Console** > **General** > **Other Settings** > **Enable Debugging** to *True*.
4. Execute the report under test.
5. Zip the contents of the `<WebApp>/Debug` together and attach them to the next response to your request.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Each time a report is executed, the `Debug` directory will be cleared. Be sure to save any needed files before creating a new package.
