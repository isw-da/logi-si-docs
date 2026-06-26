---
title: "Install the Discovery Module - Linux - Installing the DM Software from a Command-Line"
id: 4419715325975
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715325975-Install-the-Discovery-Module-Linux-Installing-the-DM-Software-from-a-Command-Line
updated_at: 2022-07-17T02:24:14Z
---

# Install the Discovery Module - Linux - Installing the DM Software from a Command-Line

# Install the Discovery Module - Linux - Installing the DM Software from a Command-Line

If you do not have a GUI available or prefer to install from a Command Line, use the following instructions:

1. Once the file has been downloaded and you've changed its permissions, run the ".run" file, as root.

sudo ./Discovery3\_2linux\_x64installer.run

2. When prompted, accept the licenses:  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522809742999/installdm31linux_01.png)
3. Next, you'll be prompted to specify an installation directory - we'll use default location (recommended):  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522823959575/installdm31linux_04.png)  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) If you specify a custom installation directory, the folder names in the path must not contain *spaces*. For example, this path is not valid: /opt/Logi Discovery.
4. You'll be prompted to start the physical installation:   
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522809756055/installdm31linux_05.png)  
     
   A progress indicator will be updated as the installation proceeds:  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522840492183/installdm31linux_06.png)  
     
   And installation is complete. Next you need to configure the related services (daemons).
