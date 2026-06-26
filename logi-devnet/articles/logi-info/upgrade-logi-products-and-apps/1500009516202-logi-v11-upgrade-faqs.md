---
title: "Logi v11 Upgrade FAQs"
id: 1500009516202
section: "Upgrade Logi Products and Apps"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009516202-Logi-v11-Upgrade-FAQs
updated_at: 2021-06-17T01:58:43Z
---

# Logi v11 Upgrade FAQs

# Logi v11 Upgrade FAQs

This page provides answers to frequently-asked
questions regarding upgrading from previous versions to Logi v11.

**IMPORTANT:** Per the Logi Analytics Support Policy, Logi Info v11 has reached End of Life and support for this product will be phased out with the release of Logi Info 14. This End of Life process concludes on 12/31/2021. Please contact [Sales](mailto:salesteam@logianalytics.com) or [Customer Service](mailto:CustomerService@LogiAnalytics.com) for information about upgrades. Thank you.

In general, v11 contains many changes that are not enumerated here. The best way to become aware of them, prior to upgrading, is to review the [Logi Info v11 Release Notes](https://devnet.logianalytics.com/hc/en-us/articles/1500009515702-Logi-Info-v11-Release-Notes)for the current release and a few previous releases in order to understand the fixes and enhancements that have been made.

1. [Can v10 and v11 be installed on the same machine at the same time?](#SameMachine)
2. [Does installing v11 automatically upgrade my existing applications?](#AutoUpgrade)
3. [After the upgrade, will my reports look any different?](#LookDifferent)
4. [Are any previously-available features missing in v11?](#MissingFeatures)
5. [Are there 64-bit versions of your products?](#64bit)
6. [Are there still Java versions of your products?](#Java)
7. [Will your v11 products work with Microsoft SQL Server 2012 and Windows 8?](#Win7)
8. [Can I use Logi v11 products with .NET 3.x or 4.x?](#NET35)
9. [Can I use my v10 license files with v11 products?](#v9License)
10. [Can I move my v11 product to a different computer?](#MoveV10)
11. [What are the v11 licensing ramifications of using server virtualization?](#Virtualization)
12. [Logi v11 requires a license file for *every* Logi app. Is a centralized file possible instead?](#Centralized)
13. [Does Security work the same way?](#Security)
14. [Will my tasks scheduled with the Logi Scheduler be affected?](#Scheduler)
15. [Is the v10 Logi Scheduler compatible with Logi Info v11?](#SchedulerCompat)

**1. Can v10 and v11 be installed on the same machine at the same time?**  
Yes, however, the *installation location is significant* and related to your intentions:

If you are just curious about v11 and want to play with it first, without committing to using it, we recommend that you install the new version in a **separate location** from any older version. This will maintain separate versions of Logi Studio and the Logi Server Engine files. You can open an existing v10 Logi app in Studio v11, upgrade it to v11, and test it. Then you'll need to open that same app in Studio v10 to downgrade it back to v10 later, if you want to. This is because the engine files
will be separately
located and, as a result, neither version of Studio will see them all.

If you're committed to making the upgrade, then install v11 in the **same location** as an older version. The Logi Server Engine files from all versions will co-exist, allowing you to upgrade and downgrade your existing Logi applications at will from within Studio. Only one instance of Studio, however, will then exist (Studio v11).

**2. Does installing v11 automatically upgrade my existing applications?**  
No. After v11 is installed, you must upgrade each Logi application to use the v11 server engine files. This can be done individually by opening an application in Studio and using the "Change Version" link in the Workspace Panel's Application tab, or in groups by using the Server Manager tool in Studio (Tools menu).

**3. After the upgrade, will my reports look any different?**Perhaps. Many visual enhancements have been made in v11, affecting charts and super-elements especially. If you're implementation is highly sensitive to appearance, testing prior to upgrading is recommended. Two new Themes have been included in v11 and you may wish to experiment with them, as well. In addition, any **Wait Page** elements you've used will be changed to **Wait Panel** elements: instead of showing a blank page containing the animated wait icon, the new Wait Panel element places
a semi-transparent, modal panel, with the wait icon, over the entire current page until processing is completed.

**4. Are any previously-available v10 features missing in v11?**  
In general, no. Some attributes may have been moved into different elements, and some elements may have been replaced by new elements (though backward compatibility has been maintained).

**5. Are there 64-bit versions of your products?**  
Yes. Logi Info and Logi Report are available as separate 32- and 64-bit products.

**6. Are there still Java versions of your products?**  
We no longer distinguish between .NET and Java versions of the *products*. Both Logi Info and Logi Report are now capable of generating web applications for both environments. When you launch the New Application Wizard, you'll be prompted to select which environment you want to use.

**7.** **Will your v11 products work with IE 10, Microsoft SQL Server 2012 R2, and Windows 8?**  
 Yes. IE 10 is fully supported as of v11.0.519. For Windows 8, only the editions that have an actual desktop and can run Logi Studio are supported.

**8. Can I use Logi v11 products with .NET 3.x or 4.0?**  
Logi products for the Windows environment, and Logi Studio, require the .NET Framework. Prior to v11.0.127, .NET v2.0 or 3.x was required; for v11.0.127 and later, .NET 4.0+ is required. If not already in place, with your consent, appropriate versions of the .NET framework are installed when Logi products are installed. They are also available for free from the [Microsoft Download Center](http://www.microsoft.com/en-us/download/developer-tools.aspx?q=developer+tools).

Starting
with v11.0.518, when using IIS 7+,
you *must* use Application Pools that use .NET 4.0. If such an application pool doesn't exist, Studio will generate a warning when you upgrade an existing Logi application. When you create a new application, Studio will create a new application pool, named "Logi Info .Net v4.0", and will assign the application to it.

**9.** **Can I use my v10 license files with v11 products?**  
No. Version 11 uses different licenses than v10. You will need to get separate v11 licenses for Logi v11 products. For more information, see [Product Licensing](https://devnet.logianalytics.com/hc/en-us/articles/1500009531601-Product-Licensing).

**10. Can I move my v11 product to a different computer?**  
Yes, the Logi 11 licensing scheme allows you to visit the License Management page on DevNet and reassign your license to a different machine. You then generate a new license file and install it along with the product. You *do not* need to contact Customer Service to accomplish any of this.

**11. What are the v11 licensing ramifications of using server virtualization?**  
It is supported but please see the Server Virtualization section of [Product Licensing](https://devnet.logianalytics.com/hc/en-us/articles/1500009531601-Product-Licensing) for details.

**12. Logi v11 requires a license file in *every* Logi app folder. Is a centralized file possible instead?**  
Yes, instead of distributing and maintaining many license files on a single computer, you place a one copy of the license file in a central location. In each Logi application, you modify the \_Settings definition, configuring the **General** element's **License File Location** attribute to point the folder containing the license file. The account the web server uses to run your apps must have access permissions to that license file folder.

**13. Does Security work the same way?**Logi v11 products use the same "Logi Security 10" scheme introduced in v10 products, which provides more streamlined and flexible security, using some new security elements. However, the "Logi Security 9" scheme is *no longer available* in Logi v11 products. Developers using Logi Security 9 and upgrading to v11 products will have to adopt Logi Security 10. For more information, see [Introduction to Logi Security 10](https://devnet.logianalytics.com/hc/en-us/articles/1500009515502-Introduction-to-Logi-Security-10).

**14. Will my tasks scheduled with the Logi Scheduler be affected?**  
Yes. If you used settings other than the defaults in the Scheduler's \_Settings.lgx file, you will need to recreate those settings in a new \_Settings.lgx file for the v11 Scheduler. This is discussed in [Use Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/1500009532181-Use-Logi-Scheduler). In addition, the database files used to store your scheduled task data will
automatically
be updated to a new v11 format the first time the Scheduler runs, so you may want to make a backup copy of them prior to the upgrade if there's any chance you'll need to roll back.

**15. Is the v10 Logi Scheduler compatible with Logi Info v11?**No, it is not. You must install and use the v11 Logi Scheduler with a Logi Info v11 application.

keywords: 64bit 32bit
