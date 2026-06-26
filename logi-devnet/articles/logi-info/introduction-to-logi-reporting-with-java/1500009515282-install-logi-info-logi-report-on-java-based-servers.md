---
title: "Install Logi Info/Logi Report on Java-Based Servers"
id: 1500009515282
section: "Introduction to Logi Reporting with Java"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515282-Install-Logi-Info-Logi-Report-on-Java-Based-Servers
updated_at: 2021-06-17T01:58:24Z
---

# Install Logi Info/Logi Report on Java-Based Servers

# Install Logi Info/Logi Report on Java-Based Servers

**Welcome** to Logi Analytics reporting products. This topic guides you through installing Logi Info or Logi Report, **version 10 or 11**, on a single computer for use with a Java-based web server.

* Installation Scenarios
* [Licenses](#Licenses)
* [Before Beginning the Studio Installation](#BeforeBeginning)
* [Installing Logi Studio](#Software)
* [Installing Logi Scheduler](#Scheduler)
* [Modifying or Repairing a Studio Installation](#Modifying)

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014842061/attnicon.gif) Installing on **Windows 7**? See [Install Logi Info/Logi Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009530921-Install-Logi-Info-Logi-Report) instead.

Installing on **Windows Server or Windows XP**? See [Install Logi Info/Logi Report on Windows Server of Windows XP](https://devnet.logianalytics.com/hc/en-us/articles/1500009515302-Install-Logi-Info-Logi-Report-on-Windows-Server-of-Windows-XP) instead.

**IMPORTANT**: If you wish to upgrade to JDK 8 release build 261 (1.8.0\_261), or any later build of JDK 8, you will need to replace the mscorlib.jar file in the application folder with the new one and restart your server. The mscorlib.jar file can be found on our [Product Download](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads "Select to access Product Dowload page") page. Please contact Support for additional assistance.

## Installation Scenarios

The installation file you received contains everything you need to create both .NET and Java web applications. The distinction between the two is made when you start to build an application. There are two major parts to the product in the installation file: **Studio** (the development tool) and the **Server Engine**.

**Studio** is a Windows application that's installed on a Windows platform and the **Server Engine** is a set of files that's added to each Logi application and is processed by the web server. When you build an application, Studio adds the engine files to the application folder.

A typical installation scenario for developers who wish to create Logi applications for Java is to install Studio on a Windows **development** machine, equipped with the Sun JDK 1.6, 1.7, or 1.8 or JRockit and one of the approved web servers. In this way, development and testing can be done on a single non-production machine.

However, for deployment to production, only the **Server Engine** files (and your application) need to be copied to the production web server, which can be a Linux/UNIX or Windows platform. This is discussed in more detail below.

### 32- or 64-bit?

Logi Info and Logi Report Java applications will run on 32-bit and 64-bit  Linux/UNIX platforms.

### Java Server Configurations

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014853521/attnicon_40x7.gif)  Important configuration information for each Java web server we support can be found in [Java Server Configurations](https://devnet.logianalytics.com/hc/en-us/articles/1500009515622-Java-Server-Configurations).

[![](https://logianalytics.zendesk.com/hc/article_attachments/1500014529602/totop.png)Back to top](#top "Click to go to the top")

## Licenses

Current Logi Info and Logi Report versions come with a built-in **15-day trial license**. You don't need to do anything but install the product and you can begin using it immediately. A clearly-visible display, shown below, in the Studio main menu counts down the days remaining in the trial period.

### Java Server Configurations

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014853541/triallicensemsg.png)

Clicking the counter display will take you to a web page that offers information about **purchasing** a Logi Info license.

After the trial period expires, Studio and any Logi reports you may have developed will *no longer run* without a real license.

Logi Analytics licenses are **server-based** rather than individual-user or concurrent-access licenses, so an unlimited number of end-users can access Logi reports through a single web server.

Our licensing scheme allows you to deploy our product on one development machine and on one production server. Additional separate licenses for Studio, for additional developers, are also available.

Licenses are keyed to you or your organization; they take the physical form of license files, which are assigned to a specific computer. DevNet includes a **License Management page** where you can manage your licences, including reviewing them, assigning and un-assigning them to machines, and generating license files, at any time, without any interaction with our staff. For more detailed information about licenses, see [Product Licensing](https://devnet.logianalytics.com/hc/en-us/articles/1500009531601-Product-Licensing).

You *may not* use our products for redistribution with, or embed them in, other products without an **OEM license**; contact our Sales group for more information if you need an OEM license.

[![](https://logianalytics.zendesk.com/hc/article_attachments/1500014529602/totop.png)Back to top](#top "Click to go to the top")

## Before Beginning the Studio Installation

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014842061/attnicon.gif) **Administrator privileges** on the target computer are **required** to complete the
installation of Logi reporting tools.

Logi products for the Windows environment, and Logi Studio, require the .NET Framework. Prior to v11.0.127, .NET v2.0 or 3.x was required; for v11.0.127 and later, .NET 4.x is required. If not already in place, with your consent, appropriate versions of the .NET framework are installed when Logi products are installed. They are also available for free from the [Microsoft Download Center](http://www.microsoft.com/en-us/download/developer-tools.aspx?q=developer+tools).

[![](https://logianalytics.zendesk.com/hc/article_attachments/1500014529602/totop.png)Back to top](#top "Click to go to the top")

## Installing Logi Studio

As usual, you can click **Back** at any time before the physical installation begins to
go back to the previous screen.

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014538642/installinfo11xp_03.png)

1. Double-click the Logi product **installation file** to launch InstallShield. Allow it to complete the installation preparation.

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014538662/installinfo11xp_04.png)

2. When the **Welcome Screen** appears, click **Next**.

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014853561/installinfo11xp_05.png)

3. **License Agreement**: Select the "I accept the terms..." radiobutton after reading the license agreement and click **Next** to continue.

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014853581/installinfo11xp_06.png)

4. **Destination Folder:** *Optional* - click **Change** to specify an alternative installation
   location if you don't like the default location. Click **Next** to accept the installation location and continue.

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014538682/installinfo11xp_07.png)

5. **Setup Type:**  Select the **Typical** or **Custom** radiobutton (see Custom information below) and click **Next** to continue.

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014538702/installinfo11xp_08a.png)

If you selected a "Typical" setup, **skip ahead** to Step 6.

If you selected a "Custom" setup, the dialog box shown above appears. The following components are available during a **Custom** setup:

+ **Studio** - The integrated development environment used by developers to create applications and report definitions. Click to remove Studio from the installation if you're only installing the Logi Server Engine.
+ **Server** - The Logi Server Engine that processes XML data in report definitions and outputs HTML (includes Server Manager).
+ **LogiXML Scheduler Service for .NET**- The Logi Windows Service that manages scheduled events; not required if you want to test scheduled report generation and distribution using Java facilities. *Not available in Logi Report.*
+ **LogiXML Scheduler Service for Java**- The Logi Java daemon that manages scheduled events; required if you want scheduled report generation and distribution on Linux/UNIX-like systems. *Not available in Logi Report.*

Click any of the components shown and make a selection from the popup menu to include them in the installation. If desired, click **Space** to review the disk space requirements for the Custom setup you've selected. Click **Next** to proceed without the review.

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014853601/installinfo11xp_09.png)

The **Disk Space Requirements** display will give you information about the available storage space and warn you if there is not enough space to complete the installation, You can repeatedly adjust the components in the Custom setup and see the effect on storage here, if necessary. Click **OK** to return to the previous dialog box.

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014538722/installinfo11xp_10.png)

6. **Installation Summary**: Review the installation summary and click **Install**.****

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014538742/installinfo11xp_11.png)

7. The physical installation will begin and you'll see several **progress indicators** for different tasks.

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014853621/installinfo11xp_12.png)

8. **Installation Complete**: click **Finish** to exit
   the installer (if you have only installed the Logi Server Engine, there will be no "Launch Logi Studio" checkbox visible).

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014853641/installinfo11xp_13_500x302.png)

9. If you left the "Launch Logi Studio" checkbox checked, Studio will now launch and you should see a splash screen like the one shown above.  
     
   You can also launch Studio by using Start Menu![](https://logianalytics.zendesk.com/hc/article_attachments/1500014845941/menuarrowrt.png)All Programs![](https://logianalytics.zendesk.com/hc/article_attachments/1500014845941/menuarrowrt.png)Logi Info or Report![](https://logianalytics.zendesk.com/hc/article_attachments/1500014845941/menuarrowrt.png)Studio.   
     
   Should you need to, you can launch Server Manager using Start Menu![](https://logianalytics.zendesk.com/hc/article_attachments/1500014845941/menuarrowrt.png)All Programs![](https://logianalytics.zendesk.com/hc/article_attachments/1500014845941/menuarrowrt.png)Logi Info or Report![](https://logianalytics.zendesk.com/hc/article_attachments/1500014845941/menuarrowrt.png)Server
   Manager or from Studio's Tools menu. More information about using Server Manager is available in [Use Logi 10 Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009516182-Use-Logi-10-Studio).

Installation is complete and you may begin to use Studio and/or the Server Engine immediately.

[![](https://logianalytics.zendesk.com/hc/article_attachments/1500014529602/totop.png)Back to top](#top "Click to go to the top")

## Install Logi Scheduler

Logi Info includes the Logi Scheduler for Java, which runs on **Windows** or **Linux**. In simple terms, the Scheduler is a proprietary application that runs "in the background" on your server as either a Windows service or as a Linux/UNIX daemon.

Services of this type are generally configured to start up when their host computer is started and therefore run automatically with little user intervention. From a performance perspective, they pose little overhead as they consume very few resources and spend most of their time idling.

When the Scheduler "runs" an event from its database, it does so by calling a specified task in a process definition in a Logi Info application. That task can then run reports, send emails, export data, etc. Logi Report does not support process definitions, therefore the Scheduler *is not included* with it.

When you run the Logi Info installation and elect to install the Logi Scheduler for Java, it places all of its files in:

C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service Java

To install the scheduler on a production server, you need to copy the contents of this folder to it, in the directory of your choice.

Due to the nature of the Scheduler and its interactions with Logi reports, you can install the Scheduler on a different server than the web server, if desired.

For Windows

To complete the installation, run the batch file regevenlog.bat
which has been included in the LogiXML Scheduler Service for Java directory. This
batch file copies the file NTEventLogAppender.dll to the Windows
System32 directory and then registers it. Logi Scheduler for Java logs events to
the Windows Event Log. Normally these events do not require monitoring but, if
issues do occur, the logs can be reviewed for diagnostic clues.

The Scheduler is started by running *<yourDirectory>\*bin\Scheduler.bat.

If you wish to start Logi Scheduler for Java automatically in Windows, then
use the Registry editor to add a String value in

HK\_Local\_Machine\Software\Microsoft\Windows\CurrentVersion\Run

named LogiSchedulerJava and set its data value to
the path to Scheduler.bat, for example:

C:\Program
Files\LogiXML IES Dev\LogiXML Scheduler Service Java\bin\Scheduler.bat  
   
 


For Linux/UNIX

The Scheduler is started by running *<yourDirectory>/*bin/Scheduler.sh.

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014842061/attnicon.gif) The use of symbolic links in Linux for this
application should be avoided as they may lead to unstable behavior.

If you wish to start Logi Scheduler for Java automatically in Linux, add a
line to /etc/rc.d/rc.local. The invocation should
be similar to

/opt/rdScheduler/Scheduler.sh
&

Note that the ampersand (&) at the end is significant: it causes the
application to load as a background process.

Logi Scheduler for Java logs events to the Linux Syslog. Normally these
events do not require monitoring but, if issues do occur, the logs can be
reviewed for diagnostic clues. The Linux Syslog utility does not permit remote
access by default, so to enable this functionality, the /etc/init.d/syslog
file needs to be modified. In it, the line invoking syslogd needs to be modified
to include the -r option.

[![](https://logianalytics.zendesk.com/hc/article_attachments/1500014529602/totop.png)Back to top](#top "Click to go to the top")

## Modifying or Repairing an Installation

Suppose you suspect a .DLL file is missing or is corrupted and you want to fix it, or you need to otherwise change your Studio installation.

![](https://logianalytics.zendesk.com/hc/article_attachments/1500014538762/installinfo11xp_15.png)

These kinds of situations can be addressed by either modifying or repairing the installation, which you should do by re-running the installation .exe file. *Do not* use Control Panel ![](https://logianalytics.zendesk.com/hc/article_attachments/1500014844761/menuarrow.gif) Add-Remove Programs
to do this; it
will request an .msi file, which is not retained after the original installation.

[![](https://logianalytics.zendesk.com/hc/article_attachments/1500014529602/totop.png)Back to top](#top "Click to go to the top")
