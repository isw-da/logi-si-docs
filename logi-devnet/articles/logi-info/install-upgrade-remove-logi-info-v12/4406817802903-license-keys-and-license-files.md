---
title: "License Keys and License Files"
id: 4406817802903
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817802903-License-Keys-and-License-Files
updated_at: 2022-04-06T06:08:18Z
---

# License Keys and License Files

# License Keys and License Files

When you purchase a Logi product, here's what happens in the licensing process:

1. We create a **license key** for each product you buy, specific to you or your organization, in our licensing database.
2. You log into DevNet and visit the **License Management** page to create a **license file**. You do this by *assigning* one of your license keys to a specific computer, by Computer Name. DevNet then generates a license file.
3. You *download* this file and use it to license Logi Studio and each Logi Info application you develop, or other Logi products.
4. Repeat Steps 2 and 3 for any additional license files required.

A typical license file name is lgx120201.lic and licenses are product-specific. License files arethe same for both .NET and Java deployments.

When you download your license file, save it to:

| Product/Platform | License File Location |
| --- | --- |
| Logi Info on Windows | C:\Program Files\LogiXML IES DEV\LogiStudio and in the application folder of any existing Logi application that you've created with a trial license, or any application that's being upgraded to v12. |
| Logi Info on Linux/UNIX | See the discussion in [License Management](https://devnet.logianalytics.com/hc/en-us/articles/4406817803927-License-Management). |
| Discovery 3.x | Installation folder, default is C:\LogiAnalytics\Discovery |
| DataHub 3.0 | Installation folder, default is C:\LogiAnalytics\Discovery |

## Moving a License to Another Machine

If you need to move an application to another machine, or to re-install your Logi product on a different machine, you can "un-assign" the license you've been using from one machine, assign it to another one, and generate a new license file.
**OEM** licenses operate in a similar fashion, but can be assigned to multiple machines.

## Logi Info Centralized License File

If you have a large number of Logi Info apps on the same development machine or web server, you may care to use a single, centralized license file rather than managing multiple license file copies.

In Logi Info v12, the **General** element in the \_Settings definition includes a **License File Location** attribute where the location of a centralized license file can be specified. This value is a fully-qualified web server file system path to the folder where the file is stored. For example, C:\myProjects\License.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) You must ensure that all web applications that will use this license run under an account that has **file access permissions** to access files
in the folder you specify as the centralized license file location.
With this centralized license file approach, if you use the exact same file path to your license file on both your development machine and your production server, you can deploy Logi applications by copying them, without having to replace the license file or adjust your \_Settings attributes each time.

## Logi Info OEM License File

Customers with Logi Info OEM licenses can embed the entire license key *inside* their Logi application. In the **\_**Settings definition, the **General** element has an **OEM Distribution License** attribute which allows Logi applications to run on a
server that does not otherwise have a license key installed. This is especially
useful for XCOPY-type deployments: the Logi installation program does not have
to be run on the web server.
To use this attribute, double-click the attribute name to open its Zoom window and then copy the entire XML contents of your OEM license file into it. This attribute *only**works* with OEM licenses; other types of licenses copied into here will be ignored.

## Discovery 3.0+ andDataHub 3.0+ Licenses

The very first time one of these products runs, the contents of any license file found (usually the trial license) are automatically copied into the Platform Database (PDB) and used directly from there. After that, any license file in that folder will be *ignored*. When the trial license expires or if you need to use a different license, you'll need to perform the steps detailed in [Other Products: Missing or Expired License](https://devnet.logianalytics.com/hc/en-us/articles/4406822484631-Other-Products-Missing-or-Expired-License) to "replace" the
license in the PDB with another license.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) If you deploy your PDB to another computer, for example by copying it from a development system to a production system, you will need to replace the development system license in the PDB with the production system license using this technique.
