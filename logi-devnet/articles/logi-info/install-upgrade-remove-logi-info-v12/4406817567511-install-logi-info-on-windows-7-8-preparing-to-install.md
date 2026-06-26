---
title: "Install Logi Info on Windows 7-8 - Preparing to Install"
id: 4406817567511
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817567511-Install-Logi-Info-on-Windows-7-8-Preparing-to-Install
updated_at: 2022-04-06T06:06:55Z
---

# Install Logi Info on Windows 7-8 - Preparing to Install

# Install Logi Info on Windows 7-8 - Preparing to Install

Logi products work with *all* editions of Windows 7. The following sections discuss features that impact the installation and/or operation of Logi Analytics products.

## Use the Administrator Account

Windows includes a number of security enhancements that impact software installation and it is critical that installation and configuration occur while using the software with the built-in "Administrator" account.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583871767/installinfo12w7_02.png)

Even if your personal account has been added to the local Administrators Group, it may not have sufficient privileges, so don't rely on it.

As shown above, the correct practice when running the Logi installation program or using the Command Line to make configuration adjustments is to start the tool by *right-clicking* its icon and selecting "**Run as administrator**" from the menu to start the program. The ensures that appropriate permissions are provided for the installed components.

Don't see a "Run as administrator" option? If the system is in a network domain, your network admin may have created security policies that don't allow you to see this option, in which case you need to consult your IT staff for assistance.

## .NET Framework

Logi products require the .NET Framework components. When Windows is installed, multiple versions of the framework are typically included. Before doing anything else, ensure that you have .NET installed by using File Explorer to browse to:

C:\Windows\Microsoft.NET\Framework

where you should see several folders, such as v4.0.30319, one for each version of .NET installed.
The .NET Framework 4.x is required. If not already in place, with your consent, appropriate versions of the .NET framework are installed when Logi products are installed. They are also available for free from the [Microsoft Download Center](https://www.microsoft.com/en-us/download/developer-tools.aspx?q=developer+tools).

## Enable the IIS Web Server

When Windows is installed, the components for the **IIS web server** are installed but are usually not enabled. You must do this manually, *before* you install your Logi product.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583871895/installinfo12w7_03.png)

This is accomplished in Control Panel, under Programs and Features![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Turn Windows features on or off, as shown above in Windows 7. Check the boxes on your machine so they match the image above, then close the dialog boxes.

## The IIS "Default Web Site"

When it's enabled, IIS creates a "Default Web Site" and the New Application wizard in Logi Studio expects to create all new Logi applications as virtual directories of that web site. If you have renamed, replaced, or disabled the "Default Web Site", or have installed another web server that handles HTTP requests on Port 80, the wizard will fail during its application registration phase. Under these circumstances, you can continue to use Logi Studio to develop Logi applications but you
will need to manually register them. This process is described in [Windows IIS Configuration](https://devnet.logianalytics.com/hc/en-us/articles/4406822610327-Windows-IIS-Configuration).
