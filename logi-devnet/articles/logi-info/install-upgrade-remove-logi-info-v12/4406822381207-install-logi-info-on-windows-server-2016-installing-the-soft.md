---
title: "Install Logi Info on Windows Server 2016 - Installing the Software"
id: 4406822381207
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822381207-Install-Logi-Info-on-Windows-Server-2016-Installing-the-Software
updated_at: 2022-04-06T06:06:49Z
---

# Install Logi Info on Windows Server 2016 - Installing the Software

# Install Logi Info on Windows Server 2016 - Installing the Software

This topic describes the installation steps and the dialog boxes you'll see when using the interactive tool built into your Logi product installation file. If you need a "silent" (non-interactive) installation, see [Command Line Install](https://devnet.logianalytics.com/hc/en-us/articles/4406817183895-Command-Line-Install).
As usual, you can click **Back** at any time before the physical installation begins to
go back to the previous screen.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563225623/installinfo12ws2016_07.png)

1. *Right-click* the Logi product installation program icon and select "Run as administrator" to launch the installer. Allow it to complete the installation preparation.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583875735/installinfo12ws2016_08.png)

2. When the **Welcome Screen** appears, click **Next**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563226007/installinfo12ws2016_09.png)

3. **License Agreement**: Select the "I accept the terms..." radio button after reading the license agreement and click **Next** to continue.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583876247/installinfo12ws2016_10.png)

4. **Destination Folder:** Click **Next** to accept the installation location and continue. *Optional* - click **Change** to specify an alternative installation
   location if you don't like the default location. Multiple versions may be installed on the same machine and will co-exist smoothly using the default values here.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583876375/installinfo12ws2016_11.png)

5. **Setup Type:**  Select the **Typical** or **Custom** radio button (see Custom information below) and click **Next** to continue.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575653527/installinfo12ws2016_12.png)

If you selected a "Typical" setup, **skip ahead** to Step 6.
If you selected a "Custom" setup, the dialog box shown above appears. The following components are available during a **Custom** setup:



+ **Logi Info Studio**  - The integrated development environment used by developers to create applications and report definitions. Click to remove Studio from the installation if you're only installing the Logi Server Engine.
+ **Logi Info Web Server**  - The Logi Server Engine that processes XML data in report definitions and outputs HTML (includes Server Manager).
+ **Logi Info Scheduler Service for .NET**- The Logi Windows Service that manages scheduled events; required if you want to have scheduled report generation and distribution.
+ **Logi Info Scheduler Service for Java**- The Logi Java daemon that manages scheduled events; not applicable when using the .NET version of Logi Info.

  

Click any of the components shown and make a selection from the popup menu to include them in the installation. If desired, click **Space** to review the disk space requirements for the Custom setup you've selected. Click **Next** to proceed without the review.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583876631/installinfo12ws2016_13.png)

The **Disk Space Requirements** display will give you information about the available storage space and warn you if there is not enough space to complete the installation, You can repeatedly adjust the components in the Custom setup and see the effect on storage here, if necessary. Click **OK** to return to the previous dialog box.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575653911/installinfo12ws2016_14.png)

6. **Installation Summary**: Review the installation summary and click **Install**.****

![](https://devnet.logianalytics.com/hc/article_attachments/4417575654167/installinfo12ws2016_15_520x421.png)

7. The physical installation will begin and you'll see several **progress indicators** for different tasks.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575654423/installinfo12ws2016_16.png)

8. **Installation Completed**: click **Finish** to exit
   the installer (if you have only installed the Logi Info Web Server, there will be no "Launch Logi Studio" check box visible).

![](https://devnet.logianalytics.com/hc/article_attachments/4417583876887/installinfo12ws2016_17.png)

9. If you left the "Launch Logi Studio" check box checked, Studio will now launch and you should see a splash screen like the one shown above.  
     
   You can also launch Studio by using Start Menu![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Logi Info or Report![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Studio.
     
     
   Should you need to, you can launch Server Manager using Start Menu![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Logi Info or Report![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Server
   Manager or from Studio's Tools menu. More information about using Server Manager is available in [Using Logi 12 Studio](https://devnet.logianalytics.com/hc/en-us/articles/4406822594327-Using-Logi-12-Studio).

Installation is complete and you may begin to use Studio and/or the Server Engineimmediately.
