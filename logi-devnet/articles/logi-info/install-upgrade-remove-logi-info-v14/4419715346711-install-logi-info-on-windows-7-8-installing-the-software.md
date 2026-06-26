---
title: "Install Logi Info on Windows 7-8 - Installing the Software"
id: 4419715346711
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715346711-Install-Logi-Info-on-Windows-7-8-Installing-the-Software
updated_at: 2022-07-17T01:46:01Z
---

# Install Logi Info on Windows 7-8 - Installing the Software

# Install Logi Info on Windows 7-8 - Installing the Software

This topic describes the installation steps and the dialog boxes you'll see when using the interactive tool built into your Logi product installation file. If you need a "silent" (non-interactive) installation, see [Command Line Install](https://devnet.logianalytics.com/hc/en-us/articles/4419722752535-Command-Line-Install).

1. Double-click the Logi product **installation file** to launch InstallShield. Allow it to complete the installation preparation.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706895127/prepare_install_14.0.png)

2. When the **Welcome Screen** appears, select **Next:**

![](https://devnet.logianalytics.com/hc/article_attachments/4419706895383/welcome_install_shield_14.0.png)

3. **License Agreement**: Select the "I accept the terms..." radio button after reading the license agreement and select **Next** to continue:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699775127/license_agreement_14.0.png)

4. **Destination Folder:** *Optional* - select **Change** to specify an alternative installation
   location if you don't like the default location. Select **Next** to accept the installation location and continue:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706895639/destination_folder_14.0.png)

5. **Setup Type:**  Select the **Typical** or **Custom** radio button (see Custom information below) and click **Next** to continue:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706896023/setup_type_14.0.png)

If you selected a "Typical" setup, **skip ahead** to Step 6. If you selected a "Custom" setup, the dialog box (shown below) appears. The following components are available during a **Custom** setup:

* **Studio** - The integrated development environment used by developers to create applications and report definitions. Select to remove Studio from the installation if you're only installing the Logi Server Engine.
* **Server** - The Logi Server Engine that processes XML data in report definitions and outputs HTML (includes Server Manager).
* **LogiXML Scheduler Service for .NET** - The Logi Windows Service that manages scheduled events; not required if you want to test scheduled report generation and distribution using Java facilities.
* **LogiXML Scheduler Service for Java** - The Logi Java daemon that manages scheduled events; required if you want scheduled report generation and distribution on Linux/UNIX-like systems.

Click any of the components shown above and make a selection from the pop-up menu to include them in the installation. If desired, select **Space** to review the disk space requirements for the Custom setup you've selected. Select **Next** to proceed without the review:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714815511/feature_installation_14.0.png)

The **Disk Space Requirements** display will give you information about the available storage space and warn you if there is not enough space to complete the installation. You can repeatedly adjust the components in the Custom setup and see the effect on storage here, if necessary. Select **OK** to return to the previous dialog box.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699775511/disk_space_14.0.png)

6. **Installation Summary**: Review the installation summary and select **Install**:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714815767/select_install_14.0.png)

The physical installation will begin and you'll see several progress indicators for different tasks:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714816023/installation_progress_14.0.png)

8. **Installation Complete**: Select **Finish** to exit
   the installer (if you have only installed the Logi Server Engine, there will be no "Launch Logi Studio" check box visible).

![](https://devnet.logianalytics.com/hc/article_attachments/4419706896407/select_finish_14.0.png)

9. If you left the "Launch Logi Studio" check box checked, Studio will now launch and you should see a splash screen, like below:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706896663/logi_info_14.0.png)  
  
Installation is complete and you may begin to use Studio and/or the Server Engine immediately.
*If* you have User Account Control (UAC) *turned off*, you may click **Finish** to exit the installer and launch Studio and skip the next two steps. If UAC is *not* turned off, uncheck the "Launch Logi Studio" check box, then click **Finish** and proceed to the next two steps.  
  
If you have only installed the Logi Server Engine, there will be no "Launch Logi Studio" check box; just click **Finish**.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699783831/installinfo12w7_14.png)  

10. Use the Computer browser to navigate to C:\Program Files. Right-click the LogiXML IES Dev folder and select Properties. In the Security tab, add **NETWORK SERVICE** to the list of user names and grant it **Full Control**. Repeat the process, granting Full Control to **your own account** (and to any other Logi developers who will work on this
    computer).

![](https://devnet.logianalytics.com/hc/article_attachments/4419706896663/logi_info_14.0.png)

11. You may now launch your Logi product (Start Menu![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)Logi Info or Report![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)Studio)
    and you should see
    a splash screen similar to the one shown above.  
      
    Should you need to, you can launch Server Manager using Start Menu![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)Logi Info or Report![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)Server
    Manager or from Studio's Tools menu. More information about using Server Manager is available in [Using Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4419707934103-Using-Logi-Studio).

Installation is complete and Studio and/or the Server Engine is ready for use. See [Install Logi Info on Windows 7-8 - Configuring IIS](https://devnet.logianalytics.com/hc/en-us/articles/4419715345431-Install-Logi-Info-on-Windows-7-8-Configuring-IIS) to complete.
