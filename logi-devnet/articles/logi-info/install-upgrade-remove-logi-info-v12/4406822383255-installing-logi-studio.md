---
title: "Installing Logi Studio"
id: 4406822383255
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822383255-Installing-Logi-Studio
updated_at: 2022-04-06T06:06:50Z
---

# Installing Logi Studio

# Installing Logi Studio

This topic demonstrates how to install Logi Studio v12 for use with a Java-based web server.

As usual, you can click **Back** at any time before the physical installation begins to
go back to the previous screen.

  
![](https://devnet.logianalytics.com/hc/article_attachments/4417583872151/installinfo12w7_04.png)

1. Double-click the Logi product **installation file** to launch InstallShield. Allow it to complete the installation preparation.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583872407/installinfo12w7_05.png)

2. When the **Welcome Screen** appears, click **Next**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563222423/installinfo12w7_06.png)

3. **License Agreement**: Select the "I accept the terms..." radio button after reading the license agreement and click **Next** to continue.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583873047/installinfo12w7_07.png)  

4. **Destination Folder:** *Optional* - click **Change** to specify an alternative installation
   location if you don't like the default location. Click **Next** to accept the installation location and continue.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563222807/installinfo12w7_08.png)  

5. **Setup Type:**  Select the **Typical** or **Custom** radio button (see Custom information below) and click **Next** to continue.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563223191/installinfo12w7_09.png)

If you selected a "Typical" setup, **skip ahead** to Step 6.
If you selected a "Custom" setup, the dialog box shown above appears. The following components are available during a **Custom** setup:



+ **Studio** - The integrated development environment used by developers to create applications and report definitions. Click to remove Studio from the installation if you're only installing the Logi Server Engine.
+ **Server** - The Logi Server Engine that processes XML data in report definitions and outputs HTML (includes Server Manager).
+ **LogiXML Scheduler Service for .NET**- The Logi Windows Service that manages scheduled events; not required if you want to test scheduled report generation and distribution using Java facilities.
+ **LogiXML Scheduler Service for Java**- The Logi Java daemon that manages scheduled events; required if you want scheduled report generation and distribution on Linux/UNIX-like systems.

Click any of the components shown and make a selection from the popup menu to include them in the installation. If desired, click **Space** to review the disk space requirements for the Custom setup you've selected. Click **Next** to proceed without the review.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575650967/installinfo12w7_10.png)  
 The **Disk Space Requirements** display will give you information about the available storage space and warn you if there is not enough space to complete the installation, You can repeatedly adjust the components in the Custom setup and see the effect on storage here, if necessary. Click **OK** to return to the previous dialog box.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563223447/installinfo12w7_11.png)  

6. **Installation Summary**: Review the installation summary and click **Install**.****

![](https://devnet.logianalytics.com/hc/article_attachments/4417563223575/installinfo12w7_12.png)

7. The physical installation will begin and you'll see several **progress indicators** for different tasks.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563223703/installinfo12w7_13.png)

8. **Installation Complete**: click **Finish** to exit
   the installer (if you have only installed the Logi Server Engine, there will be no "Launch Logi Studio" check box visible).

![](https://devnet.logianalytics.com/hc/article_attachments/4417575651223/installinfo12w7_15.png)

9. If you left the "Launch Logi Studio" check box checked, Studio will now launch and you should see a splash screen like the one shown above.  
     
   You can also launch Studio by using Start Menu![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Logi Info or Report![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Studio.
     
     
   Should you need to, you can launch Server Manager using Start Menu![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Logi Info or Report![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Server
   Manager or from Studio's Tools menu. More information about using Server Manager is available in [Using Logi 12 Studio](https://devnet.logianalytics.com/hc/en-us/articles/4406822594327-Using-Logi-12-Studio).

Installation is complete and you may begin to use Studio and/or the Server Engine immediately.
