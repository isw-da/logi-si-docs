---
title: "Install the Discovery Module - Linux - Installing the DM Software from a GUI"
id: 4419722961303
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722961303-Install-the-Discovery-Module-Linux-Installing-the-DM-Software-from-a-GUI
updated_at: 2022-07-17T02:24:13Z
---

# Install the Discovery Module - Linux - Installing the DM Software from a GUI

# Install the Discovery Module - Linux - Installing the DM Software from a GUI

If you prefer to run the installation in a GUI, you can either use "sudo" to run it in a terminal session, or run it directly in the GUI if logged in as "root". These examples are from Centos 6.9. As usual, you can click **Back** at any time before the physical installation begins to
go back to the previous screen.

![](https://devnet.logianalytics.com/hc/article_attachments/7522840369175/installdm31linux_09.png)

1. Run the installer in the GUI. When the **Welcome Screen** appears, click **Forward**.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522794362007/installdm31linux_09a.png)  
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) If you see the dialog box shown above, click **No** and the installer will close. Uninstall the existing DM v2.x version and then re-run the DM 3.2 installer.   
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522813067287/installdm31linux_10.png)
2. **License Agreement**: Select the "I accept the agreement" radio button after reading the license agreement and click **Forward** to continue.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522794371223/installdm31linux_11.png)
3. **Java Acknowledgement:** Next, if you have OpenJDK installed, you'll see the screen shown above. If you don't, an error message is displayed, along with a link to download OpenJDK. If you have it installed but haven't set the related system variables, an error message is displayed. You *must* install it before proceeding. Click **Forward** to continue.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522798709783/installdm31linux_11a.png)
4. **Dataview Authoring Credentials**: (Not shown for upgrades) Provide the required information for the default Dataview Authoring "admin" user, as shown above. Click **Next** to continue.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522809696535/installdm31linux_12.png)
5. **Installation Directory:** Click **Forward** to accept the default installation location and continue. *Optional* - click the Folder icon to specify an alternative installation location if you don't like the default location.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) If you specify a custom installation directory, the folder names in the path must not contain *spaces*. For example, this path is not valid: /opt/Logi Discovery. In addition, the *length* of the path must not exceed the OS PATH\_MAX length (4,096 by default, usually).  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522840407959/installdm31linux_13.png)
6. **Ready to Install**: Click **Forward**.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522809719959/installdm31linux_14.png)
7. The physical installation will begin and you'll see a progress indicator for different tasks.  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522798740375/installdm31linux_15.png)
8. **Installation is complete**: Click **Finish** to exit the installer.

Once installation is complete, skip down to one of the following sections about Configuring Services.
