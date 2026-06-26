---
title: "Install Logi Info/Logi Report"
id: 1500009530921
section: "Install Logi Info/Logi Report"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530921-Install-Logi-Info-Logi-Report
updated_at: 2021-06-17T01:58:24Z
---

# Install Logi Info/Logi Report

# Install Logi Info/Logi Report

**Welcome** to Logi Analytics reporting products. This topic guides you through installing Logi Info or Logi Report, **versions 10 or 11**, on a single computer under the Windows 7 operating system, for use with the IIS web server.

* Installation Scenarios
* [Product Licenses](#Licenses)
* [Prepare to Install](#Preparing)
* [Install the Software](#StartInstall)
* [Configure IIS](#Configuring)
* [Modify or Repair the Installation](#Modifying)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)Installing on **Windows Server** or **XP**? See [Install Logi Info/Logi Report on Windows Server of Windows XP](https://devnet.logianalytics.com/hc/en-us/articles/1500009515302-Install-Logi-Info-Logi-Report-on-Windows-Server-of-Windows-XP) instead.

Installing for use with a **Java** web server? See [Install Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4402771959063-Install-Logi-Studio) instead.

## Installation Scenarios

There are two major parts to the Logi product in the installation file you downloaded:

**Logi Studio**, our development environment, is a Windows application that's typically installed on a Windows development machine and interacts with the local IIS web server for Logi application development and testing.

The **Logi****Server Engine** is a set of files that's part of each Logi application and which provides an extension to the IIS web server at runtime. When you build a Logi application, Studio adds the Engine files to the application. The engine also includes a Windows utility application, **Logi Server Manager**, that allows you to perform basic configuration of Logi applications without using Studio.

A very typical installation scenario is to install Studio and the Server Engine on a development machine, and then install only the Server Engine (including Server Manager) on the production web server. This "development and production" dual installation is allowed by our licensing scheme.

Additional copies of Studio may be licensed and installed on additional development machines.

There are a number of ways to *deploy* your Logi applications to production, including using Studio's built-in **Application Deployment** tool.

Other installation scenarios, involving shared network drives and team development, can be used. This topic covers installation of Studio and the Server Engine on a development machine, and also explains what's needed to install the Server Engine on a single production server.

### 32- or 64-bit?

Logi Info and Logi Report are both available for **32-bit** and **64-bit** systems. There are different Logi product distribution files for 32-bit and 64-bit versions, so be sure you've downloaded the right one for your system.

## Product Licenses

Current Logi Info and Logi Report versions come with a built-in **15-day trial license**. You don't need to do anything but install the product and you can begin using it immediately. A clearly-visible display, shown below, in the Studio main menu counts down the days remaining in the trial period.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771636503/triallicensemsg.png)

Clicking the counter display will take you to a web page that offers information about **purchasing** a Logi Info license.

After the trial period expires, Studio won't be usable and any Logi reports you may have developed will *no longer run* without a regular license.

Logi Analytics licenses are **server-based** rather than individual-user or concurrent-access licenses, so an unlimited number of end-users can access Logi reports through a single web server. Our licensing scheme allows you to deploy our product on one development machine and on one production server. As mentioned earlier, additional separate licenses for Studio, for additional developers, are also available.

Licenses are keyed to you or your organization; they take the physical form of license files, which are assigned to a specific computer. DevNet includes a **License Management page** where you can manage your licences, including reviewing them, assigning and un-assigning them to machines, and generating license files, at any time, without any interaction with our staff. For more detailed information about licenses, see [Product Licensing](https://devnet.logianalytics.com/hc/en-us/articles/1500009531601-Product-Licensing).

You *may not* use our products for redistribution with, or embed them in, other products without an **OEM license**; contact our Sales group for more information if you need OEM licenses.

## Prepare to Install

Logi products work with *all* editions of Windows 7. The following sections discuss features that impact the installation and/or operation of Logi Analytics products.

### Use the Administrator Account

Windows 7 includes a number of security enhancements that impact software installation and it is critical that installation and configuration occur while using the software with the built-in "Administrator" account.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771744791/installinfo11w7_02.png)Even if your personal account has been added to the local Administrators Group, it may not have sufficient privileges, so don't rely on it.

As shown at left, the correct practice when running the Logi installation program or using the Command Line to make configuration adjustments is to start the tool by *right-clicking* its icon and selecting "**Run as administrator**" from the menu to start the program. The ensures that appropriate permissions are provided for the installed components.

Don't see a "Run as administrator" option? If the system is in a network domain, your network admin may have created security policies that don't allow you to see this option, in which case you need to consult your IT staff for assistance.

### .NET Framework

Logi products require the .NET Framework components. When Windows 7 is installed, multiple versions of the framework are typically included. Before doing anything else, ensure that you have .NET installed by using File Explorer to browse to:

C:\Windows\Microsoft.NET\Framework

where you should see several folders, such as v4.0.30319, one for each version of .NET installed.

Prior to v11.0.127, .NET v2.0 or 3.x was required; for v11.0.127 and later, .NET 4.x is required. If not already in place, with your consent, appropriate versions of the .NET framework are installed when Logi products are installed. They are also available for free from the [Microsoft Download Center](http://www.microsoft.com/en-us/download/developer-tools.aspx?q=developer+tools).

### Enable the IIS Web Server

When Windows 7 is installed, the components for the **IIS web server** are installed but are usually not enabled. You must do this manually, *before* you install your Logi product.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778610071/installinfo11w7_03.png)

This is accomplished in Control Panel, under Programs and Features![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Turn Windows features on or off, as shown above. Check the boxes on your machine so they match the image above, then close the dialog boxes.

### The IIS "Default Web Site"

When it's enabled, IIS creates a "Default Web Site" and the New Application wizard in Logi Studio expects to create all new Logi applications as virtual directories of that web site. If you have renamed, replaced, or disabled the "Default Web Site", or have installed another web server that handles HTTP requests on Port 80, the wizard will fail during its application registration phase. Under these circumstances, you can continue to use Logi Studio to develop Logi applications but you
will need to manually register them. This process is described in [Windows IIS Configuration](https://devnet.logianalytics.com/hc/en-us/articles/1500009515222-Windows-IIS-Configuration).

## Install the Software

As usual, you can click **Back** at any time before the physical installation begins to
go back to the previous screen.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778610327/installinfo11w7_04.png)

1. To start the installation, *right-click* the Logi product installation program icon and select "Run as administrator" to launch the installer. Allow it to complete the installation preparation.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771745175/installinfo11w7_05.png)

2. When the **Welcome Screen** appears, click **Next**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771745431/installinfo11w7_06.png)

3. **License Agreement**: Select the "I accept the terms..." radiobutton after reading the license agreement and click **Next** to continue.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778610711/installinfo11w7_07.png)

4. **Destination Folder:** Click **Next** to accept the default installation location and continue. *Optional* - click **Change** to specify an alternative installation location if you don't like the default location. Multiple versions may be installed on the same machine and will co-exist smoothly using the default value here.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778610967/installinfo11w7_08.png)

5. **Setup Type:** Select the **Typical** or **Custom** radiobutton (see Custom information below) and click **Next** to continue.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778611223/installinfo11w7_09.png)

If you selected a "Typical" setup, **skip ahead** to Step 6.

If you selected a "Custom" setup, the dialog box shown above appears. The following components are available during a **Custom** setup:

+ **Studio** - The integrated development environment used by developers to create applications and report definitions. Click to remove Studio from the installation if you're only installing the Logi Server Engine.
+ **Server** - The Logi Server Engine that processes XML data in report definitions and outputs HTML (includes Server Manager).
+ **LogiXML Scheduler Service for .NET**- The Logi Windows Service that manages scheduled events; required if you want to schedule report generation and distribution from a .NET web server (IIS). *Not available in Logi Report.*
+ **LogiXML Scheduler Service for Java**- The Logi Java daemon that manages scheduled events; required if you want to schedule report generation and distribution from a Java-based web server. *Not available in Logi Report.*

Left-click any of the components shown and make a selection from the popup menu to include them in the installation. If desired, click **Space** to review the disk space requirements for the Custom setup you've selected. Click **Next** to proceed without the review.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771745687/installinfo11w7_10.png)

The **Disk Space Requirements** display will give you information about the available storage space and warn you if there is not enough space to complete the installation, You can repeatedly adjust the components in the Custom setup dialog box and see the effect on storage here, if necessary. Click **OK** to return to the previous dialog box.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778611479/installinfo11w7_11.png)

6. **Installation Summary**: Review the installation summary and click **Install**.****

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778611863/installinfo11w7_12.png)

7. The physical installation will begin and you'll see several **progress indicators** for different tasks.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771746071/installinfo11w7_13.png)

9. **Installation is complete**: *If* you have User Account Control (UAC) *turned off*, you may click **Finish** to exit the installer and launch Studio and skip the next two steps.   
     
   If UAC is *not* turned off, uncheck the "Launch Logi Studio" checkbox, then click **Finish** and proceed to the next two steps.  
     
   If you have only installed the Logi Server Engine, there will be no "Launch Logi Studio" checkbox; just click **Finish**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771746327/installinfo11w7_14.png)

10. Use the Computer browser to navigate to C:\Program Files. Right-click the LogiXML IES Dev folder and select Properties. In the Security tab, add **NETWORK SERVICE** to the list of user names and grant it **Full Control**. Repeat the process, granting Full Control to **your own account** (and to any other Logi developers who will work on this
    computer).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778612119/installinfo11w7_15.png)

11. You may now launch your Logi product (Start Menu![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)All Programs![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Logi Info or Report![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Studio)
    and you should see
    a splash screen similar to the one shown above.  
      
    Should you need to, you can launch Server Manager using Start Menu![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)All Programs![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Logi Info or Report![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Server
    Manager or from Studio's Tools menu. More information about using Server Manager is available in [Use Studio 11](https://devnet.logianalytics.com/hc/en-us/articles/1500009516162-Use-Studio-11).

Installation is complete and Studio and/or the Server Engine is ready for use. However, go on to the next section to complete the IIS configuration.

## Configure IIS

First, using the IIS Manager tool provided with the OS, ensure that the ASP.NET extension is allowed to execute:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778612375/installinfo11w7_18.png)

This is done, as shown above, by selecting the Home item at the left, then double-clicking the **ISAPI and CGI Restrictions** item. If the ASP.NET entry (or entries) is marked *Not Allowed*, edit its settings and check the *Allow extension*... checkbox.

Next, you must ensure that either your Default Web Site, or your individual Logi application virtual directories (when you create them), have the correct **.NET Trust Levels** assigned:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778612631/installinfo11w7_17.png)

In order to be able to cache data, interact with handlers, and perform other required operations, the .NET Trust Levels must be set to *Full (Internal)*, as shown above.

Finally, here's a "best practices" tip for configuring IIS for use with Logi applications:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778612887/installinfo11w7_16.png)

We recommend that you create a new **Application Pool** specifically for your Logi applications, as shown above, left. Then you will need to assign your Logi app virtual directories to it by editing their Basic Settings and selecting the new pool, as shown above, right. This allows you to manage and restart the pool independently of any other non-Logi applications that are also using IIS. Logi apps use the default *Integrated* pipeline mode in
application pools, resulting in better performance; Logi apps built using earlier versions must use *Classic* mode.

## Modify or Repair the Installation

Suppose you installed Logi Info but didn't initially install the Scheduler, and now you find you want to schedule reports. Or you suspect a Logi Studio .DLL file is missing or is corrupted and you want to fix it.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778613143/installinfo11w7_19.png)

These kinds of situations can be addressed by either modifying or repairing the installation, which you should do by re-running the installation program file (don't forget to right-click it and use "Run as administrator" to start it).

*Do not* use Control Panel![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Programs
to do this; it
will request an .msi file, which is not retained after the original installation.
