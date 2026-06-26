---
title: "Customizing InfoGo Files"
id: 4419722764311
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722764311-Customizing-InfoGo-Files
updated_at: 2022-07-17T02:08:38Z
---

# Customizing InfoGo Files

# Customizing InfoGo Files

As an optional feature, InfoGo can be customized or "branded" in several ways to make it look like "your" application.

All of the following definitions appear in the goCustomizations folder, in Logi Studio's Application panel:

| Reports | Customization Opportunity |
| --- | --- |
| goBookmarkSharingUserlist | Used to specify an optional list of user names, with other information, that will be available for selection when sharing folders with users and groups. |
| goEmailAddressList | Used provide a list of email addresses, allowing the user to make address selections, in addition to entering them. |
| goExtraGalleryFiles | Used to specify customized Extra Gallery File elements in order to include globally-shared custom gallery items. |
| goWebFooter | Used to customize copyright statement and other footer information. |
| goWebHeader | Used to customize logo, application title, and user icons. Includes icon for sidebar menu. |

| Support Files | Customization Opportunity |
| --- | --- |
| Custom.css | Add your own custom CSS classes here; be sure to include this file using a Style or Global Style element. |
| Custom.html | Include custom HTML for insertion within the HTML <Head> tags. Among other things, this is where you can specify the location of your Favicon file. |
| Custom.js | Include custom JavaScript for use within the application. |
| dmfAnlysisGrid.xml | Definition Modifier code for the goAnalysisGrid definition. A reference to this already exists in the definition. |
| dmfDashboard.xml | Definition Modifier code for the goDashboard definition. A reference to this is already exists in the definition. |
| dmfHome.xml | Definition Modifier code for the goHome definition. A reference to this is already exists in the definition. |
| dfmMaster.xml | Definition Modifier code for the goMaster definition. A reference to this is already exists in the definition. |
| dmfReport.xml | Definition Modifier code for the goReport definition. A reference to this is already exists in the definition. |
| dmfSchedulerManager.xml | Definition Modifier code for the goScheduleManager definition. A reference to this is already exists in the definition. |
| tmfBookmarkOrganizer.xml | Template Modifier code for the goHome definition. A reference to this is already exists in the definition. |
