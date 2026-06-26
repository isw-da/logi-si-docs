---
title: "Install the Self-Service Reporting Module"
id: 1500009515322
section: "Upgrade Logi Products and Apps"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515322-Install-the-Self-Service-Reporting-Module
updated_at: 2021-06-17T01:58:24Z
---

# Install the Self-Service Reporting Module

# Install the Self-Service Reporting Module

This document guides you through installing the **Self-Service Reporting Module** on a single computer under the Windows 7 and similar operating systems. It is intended for system administrators and application developers. Topics in this document include:

* About the Self-Service Reporting Module
* [Prepare to Install](#Preparing)
* [Install the Software](#StartInstall)
* [Remove or Repair the Installation](#Removing)
* [Release Pairings](#Pairings)

## About the Self-Service Reporting Module

The Logi Self-Service Reporting Module (SSRM) is an add-on module, sold separately, that enables special elements in Logi Info v11.3+ and adds a pre-built Logi application to your computer. It works with the Analysis Grid super-element, which is *not* available for Logi Report.

The special SSRM elements installed can be used with the Analysis Grid in your applications and make it easy for users to configure data queries at runtime, as described in our document *[Developing with Analysis Grids - v11.3](https://devnet.logianalytics.com/hc/en-us/articles/1500009532281-Develop-with-Analysis-Grids-v11-3-)*.

The included application, **InfoGo**, uses the special SSRM elements and allows users to create and share visualizations, dashboards, and reports at runtime. Developers can examine InfoGo for educational purposes and can also customize its branding and other features, if desired. InfoGo can be deployed to .NET and Java servers.

After the SSRM installer finishes, there are several things you need to do to complete the installation. These are explained in our document *[Configuring InfoGo](https://devnet.logianalytics.com/hc/en-us/articles/1500009529941-Configure-InfoGo)*.

### Important Restrictions

Please note these important restrictions on the use of the SSRM:

* Requires Logi Info v11.3 or later, 64-bit version; there is no 32-bit SSRM version available.
* Cannot be used with Logi Report.
* Works with Chrome, Firefox, and other major browsers, but *does not* work with Internet Explorer 7 or 8.

The **Active Query Builder** and **Metadata** elements and InfoGO application installed with the SSRM use these database servers only:

* HP Vertica (with Logi Info v11.3.049 SP 5+)
* Microsoft SQL Server 2005+
* MySQL
* Oracle
* PostgreSQL

Ensure that your environment meets these restrictions prior to installation!

## Prepare to Install

Logi Info v11.3+ must be installed and licensed *before* the SSRM is installed. The SSRM works with your Logi Info license.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) It's critical that installation and configuration occur while running as the built-in "Administrator" account.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771740055/installssrm_01.png)Even if your personal account has been added to the local Administrators Group, it may not have sufficient privileges, so don't rely on it.

As shown at left, the correct practice when running the Logi installation program or using the Command Line to make configuration adjustments is to start the tool by *right-clicking* its icon and selecting "**Run as administrator**" from the menu to start the program.

This ensures that appropriate permissions are provided for the installed components.

Don't see a "Run as administrator" option?

If the system is in a network domain, your network admin may have created security policies that don't allow you to see this option, in which case you need to consult your IT staff for assistance.

### Upgrade Considerations

SSRM upgrades are usually associated with a Logi Info upgrade and *we highly recommend that you upgrade both of them**together*. Upgrading just one or the other will usually result in undesirable effects. See the [Release Pairings](#Pairings) section for more information.

If you're upgrading to a newer version of the SSRM, be aware of these important considerations related to the included InfoGO application:

* Upgrading the SSRM will *overwrite* any edited InfoGo files, *except* those in the goCustomizations virtual folders under InfoGo![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Definitions![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Reports and InfoGo![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)\_SupportFiles. The file goCustomizations.goWebFooter.lgx will not be overwritten, for example.
* The application's \_Settings.lgx definition will not be overwritten; however, the new version may require new elements and/or attributes not found in older versions. You'll have to add these manually in the source code if they're missing. See *[Configuring InfoGO](https://devnet.logianalytics.com/hc/en-us/articles/1500009529941-Configure-InfoGo)* for details.
* If you've used your own Definition or Template Modifier Files, identifiers used with them may change from one SSRM version to the next and you may need to adjust your modifier files accordingly.

Making backup copies of any InfoGO files you've edited, prior to applying an upgrade, is highly recommended.

## Install the Software

As usual, you can click **Back** at any time before the physical installation begins to
go back to the previous screen.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778607511/installssrm_01a.png)

1. To start the installation, *right-click* the Logi product installation program icon and select "Run as administrator" to launch the installer. Allow it to complete the installation preparation.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778607767/installssrm_02_543x423.png)

2. When the **Welcome Screen** appears, click **Next**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771740311/installssrm_03.png)

3. **License Agreement**: Select the "I accept the terms..." radiobutton after reading the license agreement and click **Next** to continue.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771740567/installssrm_04.png)

4. **Destination Location:** Click **Next** to accept the default installation location and continue. *Optional* - click **Browse** to specify an alternative installation location if you don't like the default location.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771740823/installssrm_05.png)

5. **Ready to Install**: Click **Install**.****

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778608023/installssrm_06.png)

6. The physical installation will begin and you'll see several **progress indicators** for different tasks.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771741207/installssrm_07.png)

7. **Installation is complete**: Click **Finish** to exit the installer.

### What To Do Next

Before users can use the included InfoGO application, there are several steps you still need to take. For example, you need to register and license it and make a number of configurations in Studio. These steps are explained in our document *[Configuring InfoGO](https://devnet.logianalytics.com/hc/en-us/articles/1500009529941-Configure-InfoGo)*.

Before attempting to use the Metadata elements you should read our document *[Using the Metadata Builder Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009516142-Use-the-Metadata-Builder-Wizard)*. Use of the Active Query Builder is described in our document *[Developing with Analysis Grids - v11.3](https://devnet.logianalytics.com/hc/en-us/articles/1500009532281-Develop-with-Analysis-Grids-v11-3-)*.

## Remove or Repair the Installation

You can repair damaged SSRM files or remove the Logi SSRM completely by re-running the installer:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778608279/installssrm_08.png)

Don't forget to right-click it and use "Run as administrator" to start it. You can also use Control Panel![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Programs
to do this.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  Removing the SSRM will remove the special elements *and* the InfoGO application (any InfoGO definition or support files you've modified, however, will be left in place).

## Release Pairings

The table below shows which Logi Info and SSRM versions were released together:

|  |  |  |
| --- | --- | --- |
| **Release Date** | **Logi Info Version** | **SSRM Version** |
| 8 Dec 2014 | 11.4.046 SP 2 | 1.1.47 |
| 17 Oct 2014 | 11.4.046 | 1.1.41 |
| 30 Jun 2014 | 11.3.049 | 1.0.90 |

These version pairings should be used together. For more information, see the **Release Notes** for each Logi Info version.
