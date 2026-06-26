---
title: "Install Logi Info on Windows Server 2019 - Preparing to Install"
id: 4406817543703
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817543703-Install-Logi-Info-on-Windows-Server-2019-Preparing-to-Install
updated_at: 2022-04-06T06:06:44Z
---

# Install Logi Info on Windows Server 2019 - Preparing to Install

# Install Logi Info on Windows Server 2019 - Preparing to Install

Administrator privileges on the target computer are *required* to complete the
installation of Logi products.
Logi Info for the Windows environment requires the .NET Framework 4.x. If not already in place, with your consent, appropriate versions of the .NET framework are installed when Logi products are installed. They are also available for free from the [Microsoft Download Center](http://www.microsoft.com/en-us/download/developer-tools.aspx?q=developer+tools).

## Roles and Features

Before Logi product installation, you must ensure that the appropriate IIS roles and features have been enabled.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575651607/installinfo12ws2016_01.png)

1. Use the Server Management tool to examine Web Server (IIS) role:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563229335/server_roles.png)

1. Check each sub-category to ensure correct configuration. Ensure that the features shown below are installed and enabled correctly:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563229463/installinfo12ws2016_03_1025x259.png)

![](https://devnet.logianalytics.com/hc/article_attachments/4417575652247/installinfo12ws2016_04_720x311.png)

![](https://devnet.logianalytics.com/hc/article_attachments/4417583880215/image-2021-05-10-22-16-13-341_423x310.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563230103/installinfo12ws2016_05_390x274.png)

1. Select **Next**.
2. Then examine the .NET Framework Features and ensure that the features shown below are installed and enabled:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575656599/.net_framework.png)

5. Select **Next**.
6. Then, select **Install**.

## The IIS "Default Web Site"

When it's installed, IIS creates a "Default Web Site" and the New Application wizard in Logi Studio expects to create all new Logi applications as virtual directories of that web site. If you have renamed, replaced, or disabled the "Default Web Site", or have installed another web server that handles HTTP requests on Port 80, the wizard will fail during its application registration phase. Under these circumstances, you can continue to use Logi Studio to develop Logi applications but you
will need to manually register them. This process is described in [Windows IIS Configuration](https://devnet.logianalytics.com/hc/en-us/articles/4406822610327-Windows-IIS-Configuration).
