---
title: "Logi v12 Upgrade FAQs"
id: 4406816927383
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816927383-Logi-v12-Upgrade-FAQs
updated_at: 2022-04-06T06:02:56Z
---

# Logi v12 Upgrade FAQs

# Logi v12 Upgrade FAQs

This page provides answers to frequently-asked questions regarding
upgrading from previous versions to Logi v12.
In general, v12 contains many changes that are not enumerated here. The
best way to become aware of them, prior to upgrading, is to review the
[Release Notes](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF) for the current release and a few previous releases in order
to understand the fixes and enhancements that have been made.

1. [Can v11 and v12 be installed on the same machine at the same
   time?](#SameMachine)
2. [Does installing v12 automatically upgrade my existing
   applications?](#AutoUpgrade)
3. [After the upgrade, will my reports look any different?](#LookDifferent)
4. [Are any previously-available features missing in v12?](#MissingFeatures)
5. [Are there 64-bit versions of your product?](#64bit)
6. [Are there Java versions of your product?](#Java)
7. [Will your v12 product work with Microsoft SQL Server 2012 and
   Windows 8?](#Win7)
8. [Can I use Logi v12 products with .NET 3.x?](#NET35)
9. [Can I use my v11 license files with Logi Info v12?](#v9License)
10. [Can I move my v12 licenseto a different computer?](#MoveV10)
11. [What are the v12 licensing ramifications of using server
    virtualization?](#Virtualization)
12. [Logi v12 requires a license file for *every* Logi app. Is
    a centralized file possible instead?](#Centralized)
13. [Does Security work the same way?](#Security)
14. [Will my Logi Scheduler settings be affected?](#Scheduler)
15. [Is the v11 Logi Scheduler compatible with Logi Info v12?](#SchedulerCompat)

**1. Can v11 and v12 be installed on the same
machine at the same time?**

Yes, however, the *installation location is significant* and related
to your intentions:

If you are just curious about v12 and want to play with it first, without
committing to using it, we recommend that you install the new version in a
**separate location** from any older version. This will maintain
separate versions of Logi Studio and the Logi Server Engine files. You can
open an existing v11 Logi app in Studio v12, upgrade it to v12, and test
it. Then you'll need to open that same app in Studio v11 to downgrade it
back to v11 later, if you want to. This is because the engine files will
be separately located and, as a result, neither version of Studio will see
them all.

If you're committed to making the upgrade, then install v12 in the
**same location** as an older version. The Logi Server Engine files
from all versions will co-exist, allowing you to upgrade and downgrade
your existing Logi applications at will from within Studio. Only one
instance of Studio, however, will then exist (Studio v12).

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Per the Logi Analytics Support Policy, Logi Info v11 has reached End of Life and support for this product will be phased out with the release of Logi Info 14. This End of Life process concludes on 12/31/2021. Please contact [Sales](mailto:salesteam@logianalytics.com) or [Customer Service](mailto:CustomerService@LogiAnalytics.com) for information about upgrades. Thank you.

**2. Does installing v12 automatically upgrade
my existing applications?**  
 No. After v12 is installed, you must upgrade each Logi application to use
the v12 server engine files. This can be done individually by opening an
application in Studio and using the "Change Version" link in the
Workspace Panel's Application tab, or in groups by using the Server
Manager tool in Studio (Tools menu).

**3. After the upgrade, will my reports look
any different?**Perhaps. Many visual enhancements have been made in v12, affecting charts
and super-elements especially. If you're implementation is highly
sensitive to appearance, testing prior to upgrading is recommended.

**4. Are any previously-available v11
features missing in v12?**  
 In general, no. Some attributes may have been moved into different
elements, and some elements may have been replaced by new elements (though
backward compatibility has been maintained).

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Significant changes were made in v12 to the
**Analysis Grid** user interface. If you are using Template Modifier
files to customize the Analysis Grid, you may have to re-engineer them to
use the new Analysis Grid XML identifiers.

**5. Are there 64-bit versions of your product?**  
 Yes. Logi Info versions earlier than v12.2 are available for
**32-bit** and **64-bit** systems. Starting with v12.2 only 64-bit
versions are available.

**6. Are there Java versions of your product?**  
 We don't distinguish between .NET and Java versions of the *product*.
Logi Info is capable of generating web applications for both environments.
When you launch the New Application Wizard in Logi Studio, you'll be
prompted to select which environment you want to use.

**7.** **Will your v12 product work with IE 11, Microsoft SQL
Server 2012 R2, and Windows 10?**  
 Yes. IE 11 is fully supported. For Windows 10, we only support editions
that have an actual desktop and can run Logi Studio.

**8. Can I use Logi Info v12 with .NET 3.x?**  
 No, Logi Info applications for the Windows environment, and Logi Studio,
require the .NET Framework 4.x. If not already in place, with your
consent, appropriate versions of the .NET framework are installed when
Logi products are installed. They are also available for free from the
[Microsoft Download Center](http://www.microsoft.com/en-us/download/developer-tools.aspx?q=developer+tools).

You *must* use Application Pools that use .NET 4.x for your
applications.
If such an application pool doesn't exist, Studio will generate a
warning when you upgrade an existing Logi application. When you create a
new application, Studio will create a new application pool, named
"Logi Info .Net v4.x", and will assign the application to
it.

**9.** **Can I use my v11 license files with Logi Info
v12?**  
 No. Version 12 uses a different license than v11. You will need to get
separate v12 licenses for Logi Info v12 and applications upgraded to v12.
For more information, see [Product Licensing](https://devnet.logianalytics.com/hc/en-us/articles/4406817805207-Product-Licensing).

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Per the Logi Analytics Support Policy, Logi Info v11 has reached End of Life and support for this product will be phased out with the release of Logi Info 14. This End of Life process concludes on 12/31/2021. Please contact [Sales](mailto:salesteam@logianalytics.com) or [Customer Service](mailto:CustomerService@LogiAnalytics.com) for information about upgrades. Thank you.

**10. Can I move my v12 license to a different
computer?**  
 Yes, the Logi 12 licensing scheme allows you to login and visit the
License Manager page on DevNet and reassign your license to a different
machine. You then generate a new license file and install it along with
the product. You *do not* need to contact Customer Service to
accomplish any of this.

**11. What are the v12 licensing
ramifications of using server virtualization?**  
 It is supported but please see the Server Virtualization section of
[Product Licensing](https://devnet.logianalytics.com/hc/en-us/articles/4406817805207-Product-Licensing) for details.

**12. Logi v12 requires a license file in
*every* Logi app folder. Is a centralized file possible instead?**  
 Yes, instead of distributing and maintaining many license files on a
single computer, you place a one copy of the license file in a central
location. In each Logi application, you modify the \_Settings definition,
configuring the **General** element's
**License File Location** attribute to point the folder containing the
license file. The account the web server uses to run your apps must have
access permissions to that license file folder.

**13. Does Security work the same way?**Logi Info v12 uses the same "Logi Security" scheme, which
provides streamlined and flexible security. For more information, see
[Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4406822422295-Logi-Security).

**14. Will my Logi Scheduler settings be
affected?**

Yes. If you used settings *other than the defaults* in the v11
Scheduler's \_Settings.lgx file, you will need to recreate those settings
in a new \_Settings.lgx file for the v12 Scheduler. For more information, see [Using Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/4406818028311-Using-Logi-Scheduler).

**15. Is the v11 Logi Scheduler compatible
with Logi Info v12?**Yes, it is. You can use the Logi Scheduler v11 to run Logi Info v12
process tasks.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Per the Logi Analytics Support Policy, Logi Info v11 has reached End of Life and support for this product will be phased out with the release of Logi Info 14. This End of Life process concludes on 12/31/2021. Please contact [Sales](mailto:salesteam@logianalytics.com) or [Customer Service](mailto:CustomerService@LogiAnalytics.com) for information about upgrades. Thank you.
