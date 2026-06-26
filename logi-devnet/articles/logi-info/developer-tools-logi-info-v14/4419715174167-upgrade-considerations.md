---
title: "Upgrade Considerations"
id: 4419715174167
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715174167-Upgrade-Considerations
updated_at: 2022-07-17T02:08:35Z
---

# Upgrade Considerations

# Upgrade Considerations

The 12.5+ versions of InfoGo presents a re-designed side-bar menu and includes more "administrative user" features. These include the new Data Manager tool (an embedded instance of our Web Metadata Builder) which allows designated users to manage connections and metadata at runtime. There are several new standard security Rights, including InfoGoReportManager which provides control over a "global main page"
and a "global menu". There are also a number of other new security Rights and constants you may need to
grant and set.

If you're upgrading InfoGo to this Logi Info version, and want to take advantage of in-place editing of Dashboard panel content, you'll need to manually add the goDashboardPanelEditing constant. See the [Configuring InfoGo Constants](https://devnet.logianalytics.com/hc/en-us/articles/4419722759447-Configuring-InfoGo-Constants) topic for
more information.

In addition, the deployment strategy you've chosen has ramifications when you install SSRM updates. When installing an update on top of an existing version in the standard installation location, the installer program will *not* overwrite InfoGo definitions you've modified. So, for example, your customizations won't ever be overwritten. However, if you also have other instances of InfoGo, you'll have to copy updated files to them and then *you* are responsible for deciding what gets overwritten.

SSRM 12.7 uses a new method of storing gallery items (visualizations) as Bookmarks and an upgrade to this version requires migrating existing items. For more information about using the included migration utility, see [Upgrade the Self-Service Reporting Module](https://devnet.logianalytics.com/hc/en-us/articles/4419707860247-Upgrade-the-Self-Service-Reporting-Module).
