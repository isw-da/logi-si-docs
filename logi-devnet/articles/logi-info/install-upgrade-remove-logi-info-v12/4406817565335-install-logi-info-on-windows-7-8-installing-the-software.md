---
title: "Install Logi Info on Windows 7-8 - Installing the Software"
id: 4406817565335
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817565335-Install-Logi-Info-on-Windows-7-8-Installing-the-Software
updated_at: 2022-04-06T06:06:53Z
---

# Install Logi Info on Windows 7-8 - Installing the Software

# Install Logi Info on Windows 7-8 - Installing the Software

This topic describes the installation steps and the dialog boxes you'll see when using the interactive tool built into your Logi product installation file. If you need a "silent" (non-interactive) installation, see [Command Line Install](https://devnet.logianalytics.com/hc/en-us/articles/4406817183895-Command-Line-Install).

As usual, you can click **Back** at any time before the physical installation begins to
go back to the previous screen.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583872151/installinfo12w7_04.png)

1. To start the installation, *right-click* the Logi product installation program icon and select "Run as administrator" to launch the installer. Allow it to complete the installation preparation.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583872407/installinfo12w7_05.png)

2. When the **Welcome Screen** appears, click **Next**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563222423/installinfo12w7_06.png)

3. **License Agreement**: Select the "I accept the terms..." radio button after reading the license agreement and click **Next** to continue.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583873047/installinfo12w7_07.png)

4. **Destination Folder:** Click **Next** to accept the default installation location and continue. *Optional* - click **Change** to specify an alternative installation location if you don't like the default location. Multiple versions may be installed on the same machine and will co-exist smoothly using the default value here.



![](https://devnet.logianalytics.com/hc/article_attachments/4417563222807/installinfo12w7_08.png)

5. **Setup Type:** Select the **Typical** or **Custom** radio button (see Custom information below) and click **Next** to continue.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563223191/installinfo12w7_09.png)
If you selected a "Typical" setup, **skip ahead** to Step 6.
If you selected a "Custom" setup, the dialog box shown above appears. The following components are available during a **Custom** setup:

+ **Logi Info Studio** - The integrated development environment used by developers to create applications and report definitions. Click to remove Studio from the installation if you're only installing the Logi Server Engine.
+ **Logi Info Web Server** - The Logi Server Engine that processes XML data in report definitions and outputs HTML (includes Server Manager).
+ **Logi Info Scheduler Service for .NET**- The Logi Windows Service that manages scheduled events; required if you want to schedule report generation and distribution from a .NET web server (IIS).
+ **Logi Info Scheduler Service for Java**- The Logi Java daemon that manages scheduled events; required if you want to schedule report generation and distribution from a Java-based web server.

  
Left-click any of the components shown and make a selection from the popup menu to include them in the installation. If desired, click **Space** to review the disk space requirements for the Custom setup you've selected. Click **Next** to proceed without the review.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575650967/installinfo12w7_10.png)  
 The **Disk Space Requirements** display will give you information about the available storage space and warn you if there is not enough space to complete the installation, You can repeatedly adjust the components in the Custom setup dialog box and see the effect on storage here, if necessary. Click **OK** to return to the previous dialog box.   
![](https://devnet.logianalytics.com/hc/article_attachments/4417563223447/installinfo12w7_11.png)

6. **Installation Summary**: Review the installation summary and click **Install**.****

![](https://devnet.logianalytics.com/hc/article_attachments/4417563223575/installinfo12w7_12.png)

7. The physical installation will begin and you'll see several **progress indicators** for different tasks.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563223703/installinfo12w7_13.png)

8. **Installation is complete**: *If* you have User Account Control (UAC) *turned off*, you may click **Finish** to exit the installer and launch Studio and skip the next two steps.   
     
   If UAC is *not* turned off, uncheck the "Launch Logi Studio" check box, then click **Finish** and proceed to the next two steps.  
     
   If you have only installed the Logi Server Engine, there will be no "Launch Logi Studio" check box; just click **Finish**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563223831/installinfo12w7_14.png)  

9. Use the Computer browser to navigate to C:\Program Files. Right-click the LogiXML IES Dev folder and select Properties. In the Security tab, add **NETWORK SERVICE** to the list of user names and grant it **Full Control**. Repeat the process, granting Full Control to **your own account** (and to any other Logi developers who will work on this
   computer).

![](https://devnet.logianalytics.com/hc/article_attachments/4417575651223/installinfo12w7_15.png)

11. You may now launch your Logi product (Start Menu![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Logi Info or Report![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Studio)
    and you should see
    a splash screen similar to the one shown above.  
      
    Should you need to, you can launch Server Manager using Start Menu![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Logi Info or Report![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Server
    Manager or from Studio's Tools menu. More information about using Server Manager is available in [Using Logi 12 Studio](https://devnet.logianalytics.com/hc/en-us/articles/4406822594327-Using-Logi-12-Studio).

Installation is complete and Studio and/or the Server Engine is ready for use. See [Install Logi Info on Windows 7-8 - Configuring IIS](https://devnet.logianalytics.com/hc/en-us/articles/4406822385943-Install-Logi-Info-on-Windows-7-8-Configuring-IIS) to complete.
