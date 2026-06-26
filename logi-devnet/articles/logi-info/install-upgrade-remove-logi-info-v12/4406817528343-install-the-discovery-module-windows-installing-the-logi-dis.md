---
title: "Install the Discovery Module - Windows - Installing the Logi Discovery Software"
id: 4406817528343
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817528343-Install-the-Discovery-Module-Windows-Installing-the-Logi-Discovery-Software
updated_at: 2022-04-06T06:06:40Z
---

# Install the Discovery Module - Windows - Installing the Logi Discovery Software

# Install the Discovery Module - Windows - Installing the Logi Discovery Software

Follow these steps to install the Logi Discovery Software.

As usual, you can click **Back** at any time before the
physical installation begins to go back to the previous screen.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563238935/installdm31_02.png)

1. To start the installation, *right-click* the Logi product
   installation file icon and select "Run as administrator" to
   launch the installer. When the **Welcome Screen** appears, click
   **Next**.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575664535/installdm31_02a.png)  
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)
   If you see the dialog box shown above, click **No** and the
   installer will close. [Uninstall](#Removing) the existing DM
   version and then re-run the DM v3.1+ installer.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583888663/installdm31_03.png)

2. **License Agreement**: Select the "I accept the agreement"
   radio button after reading the license agreement and click
   **Next** to continue.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575665047/installdm31_04.png)
3. **Java Acknowledgement:** Next, if you have OpenJDK installed, you'll see the screen shown above.
   If you don't, an error message is displayed, along with a link to
   download OpenJDK. If you have it installed but haven't set
   therelated Windows SystemVariables, an error message is
   displayed. You *must* install it before proceeding.  
   If the link in the window does not resolve correctly, you can go here to get OpenJDK12: [JDK12 Download from Archive.](https://jdk.java.net/archive/ "Click this link to get a download of JDK12.")  
    Click
   **Next**.   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583888791/installdm31_04a.png)
4. **Dataview Authoring Credentials**: (Not shown for upgrades) Provide
   the required information for the default Dataview Authoring
   "admin" user, as shown above. Click **Next** to continue.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583889047/installdm31_05.png)

5. **Installation Directory:** Click **Next** to accept the
   default installation location and continue. *Optional* - click the
   Folder icon to specify an alternative installation location if you don't
   like the default location.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)
   You may not install directly to the root folder of a drive, i.e.
   C:\
   and if you specify a custom installation directory, the folder names in
   the path must not contain *spaces*. For example, this path is
   *not valid*:
   C:\Program Files\Discovery.  
    In addition, the *length* of the path must not exceed 260
   characters.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583889431/installdm31_06.png)

6. **Ready to Install**: Click **Next**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575665431/installdm31_07.png)

7. The physical installation will begin and you'll see a progress indicator
   for different tasks.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563240343/installdm31_08.png)

8. **Installation is complete**: Click **Finish** to exit
   the installer.
