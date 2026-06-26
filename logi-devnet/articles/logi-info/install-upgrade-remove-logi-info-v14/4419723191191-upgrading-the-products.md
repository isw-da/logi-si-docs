---
title: "Upgrading the Products"
id: 4419723191191
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723191191-Upgrading-the-Products
updated_at: 2022-07-17T02:06:07Z
---

# Upgrading the Products

# Upgrading the Products

Upgrading to a new version involves two steps: installing the new release of Logi Info, and upgrading the version of any existing Logi applications. You can do the former without doing the latter; applications are not automatically upgraded. Original and upgraded applications can co-exist, so upgrading can be phased in as desired.

## Getting an Upgrade

How do you get an upgrade? Customers who have **purchased a maintenance plan**  for Logi Info, or are using it under an OEM agreement, may be able to download new product releases directly from our DevNet web site. See Support![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png) Product Download.

If the download links are not available to you, contact [Logi Customer Service](mailto:CustomerService@logiAnalytics.com) via email or telephone (703-752-9700) for alternate instructions for downloading upgrades. Customer Service can also answer questions you may have about purchasing or renewing a maintenance plan.

To upgrade your Logi product, run the downloaded installation program and install the new version into the same location as the previous version, or to a different location if you wish to have both versions installed. No un-installation of the original version is required, and existing definitions or data *will not* be overwritten. The upgrade installation will take 2-3 minutes to complete.

## Evaluations

If you wish to install an upgrade for **evaluation** purposes, we recommend that you install it into a *different folder* than any previous version, such as C:\Program Files\LogiXML IES Dev Test. This will preserve the previous version of Studio. If you install an update into the same folder as a previous version, Studio will be updated and you will not be able to roll it back without uninstalling and re-installing the previous version
entirely.

## Backup Scheduler Data

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) If you have previously installed and used the **Logi Scheduler** service and are not using the optional storage configuration to store your scheduled tasks on a networked database server, we recommend that you make a safety copy of your existing schedule data, before upgrading:
(Windows .NET) C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service\Schedules.vdb3  
(Windows Java) C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service Java\Schedules\\*.\*  
(Linux/UNIX) <installFolder>/Schedules/\*.\*
and then proceed with the upgrade installation. Your existing data file *should* be upgraded in place without any difficulty.
