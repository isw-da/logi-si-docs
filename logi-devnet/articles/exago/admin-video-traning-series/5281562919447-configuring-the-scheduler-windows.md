---
title: "Configuring the Scheduler [Windows]"
id: 5281562919447
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281562919447-Configuring-the-Scheduler-Windows
updated_at: 2022-05-03T22:08:31Z
---

# Configuring the Scheduler [Windows]

# Configuring the Scheduler [Windows]

This video explains how to configure Exago BI’s Scheduler Service on a Windows server.

[<< Installing the Scheduler [Windows]](https://devnet.logianalytics.com/hc/en-us/articles/5281563159831-Installing-the-Scheduler-Windows-) Previous Video

Next Video [Adding a SQL Data Source >>](https://devnet.logianalytics.com/hc/en-us/articles/5281562715799-Adding-a-SQL-Data-Source)

## Transcript

Welcome back to the Exago Technical Training Series! In this video we’ll demonstrate how to configure the Scheduler Service on Windows. Configuration is done in two steps: first we’ll configure the Scheduler Service itself, then move on to the Web Application’s Admin Console to finish the setup.

In the file explorer, navigate to the Scheduler Service’s installation directory. By default, this will be C:\Program Files\Exago\ExagoScheduler. Open the Scheduler Service’s configuration file, eWebReportsScheduler.xml in a text editor. There are many available settings in the file. For this video, we’ll focus on configuring the Scheduler Service to email completed reports and how the Web Application should communicate with the Scheduler Service.

These settings tell the service how to send an email. Provide the host name or IP address of an SMTP server and set smtp\_enabe\_ssl to true if that server requires secure connections. Provide a valid SMTP user ID and password. The smtp\_from and smtp\_from\_name configure the email address and friendly contact name that emails from the Scheduler Service will appear to be from.

These settings tell the service how to communicate with the Web Application. The channel\_type node determines the protocol through which the two communicate, either HTTP or TCP. The port node sets the corresponding port number. All Scheduler Services residing on the same server must have a unique port number. Record these settings as they’ll be needed when completing the configuration in the Admin Console.

The rest of the settings here can be left as the default values, though we would like to point out that setting logging to on can capture any helpful information in troubleshooting. Save the file. Verify that the Scheduler Service is running. Navigating to Services on Windows machines should show the Exago Scheduler as a new service. Stop the service if it is running, and then press Start.

Now we need to go into the Admin Console for the final configuration steps. To open the Admin Console, we’ll open a web browser and build our URL using the server IP slash web app virtual path slash Admin.aspx. In our environment, that looks like this. The Admin Console is used to build Exago’s base configuration file. We will dive into more detail in later videos. Use this pane on the left to navigate through the Admin Console’s many settings. To access the Scheduler Settings, expand the General node, then double-click on Scheduler Settings. First, change Enable Report Scheduling to True. Think of this as the “master switch” for all scheduled report functions. We will also set Show Schedule Reports Manager and email Scheduled Reports to True. The Schedule Reports Manager is an interface in the Web Application that shows the status of scheduled reports. email Scheduled Reports tells Exago to use the stored SMTP settings to send scheduled reports via email. Next, set the Schedule Remoting Host int eh format channel type colon backslash backslash server colon port, in our case tcp colon backslash backslash localhost colon 2001 to point to the Scheduler Service. If there are multiple Scheduler Services, separate their origins on this line with a semicolon. Click the Test Connection icon to test if the connection is successful. Click Apply to save the configuration changes.

Congratulations! At this point, the Exago Scheduler Service has been installed and configured!

We’ll navigate to the Exago full user interface and show the available scheduling options as a result of our configuration. To open the full UI, we’ll open a new browser tab and build our URL using the server IP slash web app virtual path slash exagohome.aspx. From the Report Tree on reports permissioned for scheduling, we will now have options to schedule and email. In the Schedule Manager, we can see existing jobs both complete and pending.
