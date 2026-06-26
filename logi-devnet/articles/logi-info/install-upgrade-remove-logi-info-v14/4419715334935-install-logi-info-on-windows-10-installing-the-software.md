---
title: "Install Logi Info on Windows 10 - Installing the Software"
id: 4419715334935
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715334935-Install-Logi-Info-on-Windows-10-Installing-the-Software
updated_at: 2022-07-17T02:07:30Z
---

# Install Logi Info on Windows 10 - Installing the Software

# Install Logi Info on Windows 10 - Installing the Software

This topic describes the installation steps and the dialog boxes you'll see when using the interactive tool built into your Logi product installation file. If you need a "silent" (non-interactive) installation, see [Command Line Install](https://devnet.logianalytics.com/hc/en-us/articles/4419722752535-Command-Line-Install).

1. Double-click the Logi product **installation file** to launch InstallShield. Allow it to complete the installation preparation.

![](https://devnet.logianalytics.com/hc/article_attachments/7522809258775/prepare_install_14.0.png)

2. When the **Welcome Screen** appears, select **Next:**

![](https://devnet.logianalytics.com/hc/article_attachments/7522812753943/welcome_install_shield_14.0.png)

3. **License Agreement**: Select the "I accept the terms..." radio button after reading the license agreement and select **Next** to continue:

![](https://devnet.logianalytics.com/hc/article_attachments/7522794019607/license_agreement_14.0.png)

4. **Destination Folder:** *Optional* - select **Change** to specify an alternative installation
   location if you don't like the default location. Select **Next** to accept the installation location and continue:

![](https://devnet.logianalytics.com/hc/article_attachments/7522794029463/destination_folder_14.0.png)

5. **Setup Type:**  Select the **Typical** or **Custom** radio button (see Custom information below) and click **Next** to continue:

![](https://devnet.logianalytics.com/hc/article_attachments/7522809321111/setup_type_14.0.png)

If you selected a "Typical" setup, **skip ahead** to Step 6. If you selected a "Custom" setup, the dialog box (shown below) appears. The following components are available during a **Custom** setup:

* **Studio** - The integrated development environment used by developers to create applications and report definitions. Select to remove Studio from the installation if you're only installing the Logi Server Engine.
* **Server** - The Logi Server Engine that processes XML data in report definitions and outputs HTML (includes Server Manager).
* **LogiXML Scheduler Service for .NET** - The Logi Windows Service that manages scheduled events; not required if you want to test scheduled report generation and distribution using Java facilities.
* **LogiXML Scheduler Service for Java** - The Logi Java daemon that manages scheduled events; required if you want scheduled report generation and distribution on Linux/UNIX-like systems.

Click any of the components shown above and make a selection from the pop-up menu to include them in the installation. If desired, select **Space** to review the disk space requirements for the Custom setup you've selected. Select **Next** to proceed without the review:

![](https://devnet.logianalytics.com/hc/article_attachments/7522823504151/feature_installation_14.0.png)

The **Disk Space Requirements** display will give you information about the available storage space and warn you if there is not enough space to complete the installation. You can repeatedly adjust the components in the Custom setup and see the effect on storage here, if necessary. Select **OK** to return to the previous dialog box.

![](https://devnet.logianalytics.com/hc/article_attachments/7522798318487/disk_space_14.0.png)

6. **Installation Summary**: Review the installation summary and select **Install**:

![](https://devnet.logianalytics.com/hc/article_attachments/7522809364631/select_install_14.0.png)

The physical installation will begin and you'll see several progress indicators for different tasks:

![](https://devnet.logianalytics.com/hc/article_attachments/7522798347415/installation_progress_14.0.png)

8. **Installation Complete**: Select **Finish** to exit
   the installer (if you have only installed the Logi Server Engine, there will be no "Launch Logi Studio" check box visible).

![](https://devnet.logianalytics.com/hc/article_attachments/7522812816663/select_finish_14.0.png)

9. If you left the "Launch Logi Studio" check box checked, Studio will now launch and you should see a splash screen, like below:

![](https://devnet.logianalytics.com/hc/article_attachments/7522812826135/logi_info_14.0.png)

You can also launch Studio by using Start Menu![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Logi Info or Report![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Studio.

Should you need to, you can launch Server Manager using Start Menu![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Logi Info or Report![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Server
Manager or from Studio's Tools menu. More information about using Server Manager is available in [Using Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4419707934103-Using-Logi-Studio).

Installation is complete and you may begin to use Studio and/or the Server Engine immediately.
