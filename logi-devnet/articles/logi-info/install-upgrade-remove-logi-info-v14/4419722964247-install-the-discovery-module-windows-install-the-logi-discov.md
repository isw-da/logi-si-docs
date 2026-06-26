---
title: "Install the Discovery Module - Windows - Install the Logi Discovery Software"
id: 4419722964247
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722964247-Install-the-Discovery-Module-Windows-Install-the-Logi-Discovery-Software
updated_at: 2022-07-17T01:47:03Z
---

# Install the Discovery Module - Windows - Install the Logi Discovery Software

# Install the Discovery Module - Windows - Install the Logi Discovery Software

Follow these steps to install the Logi Discovery Software.

As usual, you can click **Back** at any time before the
physical installation begins to go back to the previous screen.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706892055/installdm31_02.png)

1. To start the installation, *right-click* the Logi product
   installation file icon and select "Run as administrator" to
   launch the installer. When the **Welcome Screen** appears, click
   **Next**.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419699768727/installdm31_02a.png)  
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png)
   If you see the dialog box shown above, click **No** and the
   installer will close. [Uninstall](#Removing) the existing DM
   version and then re-run the DM v3.1+ installer.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699769111/installdm31_03.png)

2. **License Agreement**: Select the "I accept the agreement"
   radio button after reading the license agreement and click
   **Next** to continue.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419699769367/installdm31_04.png)
3. **Java Acknowledgement:** Next, if you have OpenJDK installed, you'll see the screen shown above.
   If you don't, an error message is displayed, along with a link to
   download OpenJDK. If you have it installed but haven't set
   the related Windows SystemVariables, an error message is
   displayed. You *must* install it before proceeding. If the link in the window does not resolve correctly, you can go here to get OpenJDK12: [JDK12 Download from Archive.](https://jdk.java.net/archive/ "Click this link to get a download of JDK12.") Click
   **Next**.   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419714813719/installdm31_04a.png)
4. **Dataview Authoring Credentials**: (Not shown for upgrades) Provide
   the required information for the default Dataview Authoring
   "admin" user, as shown above. Click **Next** to continue.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706893975/installdm31_05.png)

5. **Installation Directory:** Click **Next** to accept the
   default installation location and continue. *Optional* - click the
   Folder icon to specify an alternative installation location if you don't
   like the default location.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png)
   You may not install directly to the root folder of a drive, i.e.
   C:\
   and if you specify a custom installation directory, the folder names in
   the path must not contain *spaces*. For example, this path is
   *not valid*:
   C:\Program Files\Discovery.  
    In addition, the *length* of the path must not exceed 260
   characters.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706894231/installdm31_06.png)

6. **Ready to Install**: Click **Next**.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714814231/installdm31_07.png)

7. The physical installation will begin and you'll see a progress indicator
   for different tasks.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699770135/installdm31_08.png)

8. **Installation is complete**: Click **Finish** to exit
   the installer.
