---
title: "Install Logi Info on Windows Server 2016 - Preparing to Install"
id: 4419722976023
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722976023-Install-Logi-Info-on-Windows-Server-2016-Preparing-to-Install
updated_at: 2022-07-17T01:46:25Z
---

# Install Logi Info on Windows Server 2016 - Preparing to Install

# Install Logi Info on Windows Server 2016 - Preparing to Install

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) **Administrator privileges** on the target computer are *required* to complete the
installation of Logi products.
Logi Info for the Windows environment requires the .NET Framework 4.x. If not already in place, with your consent, appropriate versions of the .NET framework are installed when Logi products are installed. They are also available for free from the [Microsoft Download Center](http://www.microsoft.com/en-us/download/developer-tools.aspx?q=developer+tools).

## Roles and Features

Before Logi product installation, you must ensure that the appropriate IIS roles and features have been enabled.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714817431/installinfo12ws2016_01.png)

Use the Server Management tool to examine Web Server (IIS) role:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706899735/installinfo12ws2016_02.png)  
Check each sub-category to ensure correct configuration.  
  
![](https://devnet.logianalytics.com/hc/article_attachments/4419699780631/installinfo12ws2016_03.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419699780887/installinfo12ws2016_04_720x311.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419714817687/installinfo12ws2016_05.png)

Ensure that the features shown in the images above are installed and enabled correctly.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706899991/installinfo12ws2016_06.png)

Then examine the .NET Framework Features and ensure that the features shown above are installed and enabled.

## The IIS "Default Web Site"

When it's installed, IIS creates a "Default Web Site" and the New Application wizard in Logi Studio expects to create all new Logi applications as virtual directories of that web site. If you have renamed, replaced, or disabled the "Default Web Site", or have installed another web server that handles HTTP requests on Port 80, the wizard will fail during its application registration phase. Under these circumstances, you can continue to use Logi Studio to develop Logi applications but you
will need to manually register them. This process is described in [Windows IIS Configuration](https://devnet.logianalytics.com/hc/en-us/articles/4419707947543-Windows-IIS-Configuration).
