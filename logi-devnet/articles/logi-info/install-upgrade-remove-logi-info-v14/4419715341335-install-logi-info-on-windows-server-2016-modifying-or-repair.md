---
title: "Install Logi Info on Windows Server 2016 - Modifying or Repairing an Installation"
id: 4419715341335
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715341335-Install-Logi-Info-on-Windows-Server-2016-Modifying-or-Repairing-an-Installation
updated_at: 2022-07-17T01:46:26Z
---

# Install Logi Info on Windows Server 2016 - Modifying or Repairing an Installation

# Install Logi Info on Windows Server 2016 - Modifying or Repairing an Installation

Suppose you installed Logi Info but didn't initially install the Scheduler, and now you find you want to schedule reports. Or you suspect a .DLL file is missing or is corrupted and you want to fix it.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699780375/installinfo12ws2016_18.png)

These kinds of situations can be addressed by either modifying or repairing the installation, which you should do by re-running the installation .exe file, using "Run As Administrator". *Do not* use Control Panel ![](https://devnet.logianalytics.com/hc/article_attachments/4419706652439/menuarrow.gif) Add-Remove Programs
to do this; it
will request an .msi file, which is not retained after the original installation.
