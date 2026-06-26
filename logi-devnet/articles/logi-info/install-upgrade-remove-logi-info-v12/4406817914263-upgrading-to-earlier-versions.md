---
title: "Upgrading to Earlier Versions"
id: 4406817914263
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817914263-Upgrading-to-Earlier-Versions
updated_at: 2022-04-06T06:09:02Z
---

# Upgrading to Earlier Versions

# Upgrading to Earlier Versions

This topic introduces considerations you may need to be aware of
if you're upgrading to an earlier SSRM version.

## Upgrading to SSRM v12.0

The tool used in InfoGo to create analyses now has the option to apply
changes made to chart and table options as a "batch". When
turned on, users can make several changes, then click an OK button to
apply them. Normally, changes are applied immediately as each change is
made. The batch approach may make for a smoother user experience,
especially with large data sets. A new constant, goBatchSelection,
controls this behavior. If you upgrade, this constant will not be added to
the \_Settings definition automatically, but you can add it manually in the
source code and set it to True if you want to use this feature. You will
also have to set the attribute that uses this constant:

1. Open the goAnalysisGrid definition.
2. Under the BodydivGoContainerdivMainContent elements, locate the
   "ag" element.
3. Set its Batch Selection attribute to @Constant.goBatchSelection~.
4. Save the definition.

In addition, the deployment strategy you've chosen has ramifications when
you install SSRM updates. When installing an update on top of an existing
version in the standard installation location, the installer program will
not overwrite InfoGo definitions you've modified. So, for example, your
customizations won't ever be overwritten. However, if you also have other
instances of InfoGo, you'll have to copy updated files to them and then
you are responsible for deciding what gets overwritten.

## Upgrading to SSRM V12.1

Logi Info v12.1 allows developers to create a custom theme for use with
InfoGo using a new tool, the Theme Editor. The new version of InfoGo
provides an option for Administrators to modify that custom theme at
runtime. You will need to configure a constant and users will need
appropriate security rights to make this feature available. These are
discussed in the [Configuring InfoGo Constants](https://devnet.logianalytics.com/hc/en-us/articles/4406822192535-Configuring-InfoGo-Constants) and [Customizing InfoGo Files](https://devnet.logianalytics.com/hc/en-us/articles/4406817200279-Customizing-InfoGo-Files) topics.

InfoGo v12.1 now uses the Logi Info
Master Report
(see) feature to provide a header, a footer, and a left sidebar menu.
Nonetheless, your existing **goWebHeader** and
**goWebFooter** definitions *should* work without modification.   
  
 However, if you've customized the goWebHeader definition and you'd like to
use the new sidebar menu after upgrading, you should review and backup
your existing goWebHeader definition, then delete it,
*before* installing the new SSRM version. This will ensure that the
new goWebHeader definition is installed. You'll then need to customize it
as desired, using the old definition as a guide if necessary.  
  
 Alternately, if you've developed your own menu system and
*do not* want to use the sidebar menu, leave your goWebHeader in
place and run the installation. To be thorough, after the installation
remark the Left Frame in the goMaster definition.

## Upgrading to SSRM v12.2

The InfoGo side-bar menu has changed and there have been some styling
changes to the stock Signal theme. A new "Data Manager" tool,
based on the Web Metadata Builder, is available along with the Schedule
Manager and the Theme Editor and a new Security Right ID has been provided
to control access to it.

In the InfoGo application, dashboard panels no longer resize themselves
horizontally to fit the size of the chart they contain. Charts in
dashboard panels are automatically displayed at or near the largest width
feasible, and charts no longer have horizontal resizing handles. This
ensures good cross-browser and cross-device compatibility.
