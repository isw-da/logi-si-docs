---
title: "Installing Discovery Module Instances Manually"
id: 4406822366871
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822366871-Installing-Discovery-Module-Instances-Manually
updated_at: 2022-04-06T06:06:38Z
---

# Installing Discovery Module Instances Manually

# Installing Discovery Module Instances Manually

The following topics guide you through manually installing single or multiple instances of the **Discovery Module** on a single computer under the Windows or Linux operating systems:

* [Manual Installations under Windows](https://devnet.logianalytics.com/hc/en-us/articles/4406822367767-Manual-Installations-Under-Windows#Windows)
* [Manual Installations under Linux](https://devnet.logianalytics.com/hc/en-us/articles/4406817525143-Manual-Installations-Under-Linux#Linux)

## About Manual Installations

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Advanced features discussed here work with Logi Info v12.5. Earlier
and later Info versions may not support them; consult the [Release Notes](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF)
for specific details.

The Logi Discovery Module (DM) provides an embedded data discovery experience
that works directly with relational data sources using Logi data services. It does this by making several special elements available in Logi Studio. These include the **Thinkspace** element, which provides
a highly-interactive analysis experience. In its interface, best-fit visualization suggestions are automatically referred to the user by a built-in "recommendation engine" and data is organized using intelligent
technology
that clusters data to make it more easily consumable by users.

A "manual" installation does not use the usual installer program. Instead, you begin with a .zip file and manually accomplish the steps that are normally completed by the installer. Why would you do this? You might manually install a *single* instance of the DM in order to gain a better understanding of how it works, or to customize the installation.

A manual installation is also necessary for situations like a "multi-instance installation". That's a scenario where you may need to have multiple, separate DM installations on the same server. You may want to do this for a variety of reasons, including ensuring that multiple "tenants" are completely isolated from one another. The standard DM installers, however, are not engineered for this scenario. When they run and find an existing installation,
they assume that
you're trying to apply an upgrade and respond accordingly. A manual installation lets you install as many instances as you need.

### Requirements

Generally, we recommend that you use the standard installers for your first installation instance, then follow the instructions provided here for subsequent instances. However, as mentioned earlier, you can manually install a single or first instance, if you prefer.

Information about requirements, licensing, and what get's installed is provided in the standard [Install the Discovery Module - Windows](https://devnet.logianalytics.com/hc/en-us/articles/4406817527319-Install-the-Discovery-Module-Windows)and [Install the Discovery Module - Linux](https://devnet.logianalytics.com/hc/en-us/articles/4406822365975-Install-the-Discovery-Module-Linux) installation topics and is not repeated here.

You have the choice of whether or not to use a *separate* instance of the OpenJDK 12 and [Node.js 8.11.4](https://nodejs.org/dist/v8.11.4/node-v8.11.4-linux-x64.tar.xz) for each DM instance. These should be installed before you begin the instructions provided below. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) If Node.js is installed using the OS package manager, its files may
be distributed across multiple folders, which is unacceptable for Discovery. The correct process is to download Node.js and keep in contained in one folder, setting the $NODE\_HOME variable to that folder, e.g. /home/someUser/node-v8.11.4-linux-x64.

The Home folders and the logiDiscovery.bat (Windows) or logiDiscovery.sh (Linux) should be named differently for each instance.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) You may not install directly to the root folder of a drive, i.e. C:\ and the folder names in the path must *not* contain *spaces*. For example, this path is not valid: C:\Program Files\Discovery. In addition, the *length*
of the path must not exceed 260 characters.
