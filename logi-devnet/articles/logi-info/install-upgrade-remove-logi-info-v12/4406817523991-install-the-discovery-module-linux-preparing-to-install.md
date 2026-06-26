---
title: "Install the Discovery Module - Linux - Preparing to Install"
id: 4406817523991
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817523991-Install-the-Discovery-Module-Linux-Preparing-to-Install
updated_at: 2022-04-06T06:06:38Z
---

# Install the Discovery Module - Linux - Preparing to Install

# Install the Discovery Module - Linux - Preparing to Install

Logi Info must be installed and licensed *before* the DM is installed. *After* the DM is installed, you'll also need to acquire its separate license file.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) It's critical that installation and configuration occur while logged-in as the "root" user.

In this topic, we show instructions and examples of installations on **Centos 6.9** and **Ubuntu 16.04** and for systems with, and without, systemctl. Depending on your
specific OS and distribution version, some of the commands or steps shown may need to be adapted.

Download the Discovery installer from the link provided to you by the
Logi team, which will be similar to:

curl -O https://downloads.logianalytics.com/info/xxxxx-4538-489e-a5b1-18e1ca714458/Discovery3\_02inux\_x64installer.run

Change the permissions on the Discovery installer so that it can be run:

chmod +x Discovery3\_0linux\_x64installer.run
