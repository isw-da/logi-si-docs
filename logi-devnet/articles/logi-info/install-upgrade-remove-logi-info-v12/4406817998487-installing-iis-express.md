---
title: "Installing IIS Express"
id: 4406817998487
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817998487-Installing-IIS-Express
updated_at: 2022-04-06T06:09:32Z
---

# Installing IIS Express

# Installing IIS Express

Please note that, although it's included with the product, IIS Express is
*not* automatically installed when Logi Studio is installed.
Developers who have no need of IIS Express (i.e. those who have IIS
installed already) will never see it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)
If you have regular IIS installed and decide to "turn it off" in
Control Panel in order to see how IIS Express works, when you turn it back
on later you may not have all of your IIS custom Application Pools and
Virtual Directories restored! If that happens, they can be restored as
part of a general System Restore Point restore operation (assuming you
have a recent Restore Point saved). This is not something we recommend, in
general, so if you must do it, do it on a dedicated test machine, not your
development or production machine.

The first time Logi Studio is used to create a new application (by
selecting File
![](https://devnet.logianalytics.com/hc/article_attachments/4417575446295/menuarrow.gif)
New Application... from Studio's main menu), its New Application wizard
will determine whether IIS is installed on the computer where Studio is
installed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575497623/iisexpress_01.png)

If Studio can't detect an IIS installation, the dialog box above will be
displayed. The user can then decide whether to install IIS Express or IIS.
Why would anyone decide to use IIS Express instead of IIS?

* IIS Express, as installed by Studio, is configured and ready to go
  immediately and does not need the additional configuration IIS requires.
* IIS Express can be installed and administered by users who do not have
  Admin privileges on their computer.
* IIS Express can be easily uninstalled when no longer needed.

If you decide to install IIS Express, click **Install IIS Express**, as
shown above, and a separate installer is launched:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583672215/iisexpress_02.png)

As shown above, you'll need to accept the License Agreement and click
**Install**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563024023/iisexpress_03.png)

Once the installation starts, progress will be displayed in the dialog box
shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575497751/iisexpress_04.png)

When the installation is complete, click **Finish** to return to
Studio's New Application wizard.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583672599/iisexpress_05.png)  

Once IIS Express is installed, Studio becomes aware that it's dealing with
IIS Express and not IIS, and it adjusts its prompts, wizards, and
activities to be compatible with IIS Express, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583672727/iisexpress_06.png)  

Once the wizard finishes, the only difference you can see in your report
will be in its \_Settings definition. The **Path** element's
**Application Path** attribute will have a an address value similar to
the one shown above. The high-lighted part is a port number, which will be
different for each Logi app you create.
Your Logi applications will be displayed just as they would if you had
regular IIS installed: you can preview them in Studio and browse them by
using the Studio browse button and link or by entering their URL in an
independent browser window.
