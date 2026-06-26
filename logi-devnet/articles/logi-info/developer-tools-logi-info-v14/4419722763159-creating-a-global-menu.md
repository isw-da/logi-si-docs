---
title: "Creating a Global Menu"
id: 4419722763159
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722763159-Creating-a-Global-Menu
updated_at: 2022-07-17T02:24:56Z
---

# Creating a Global Menu

# Creating a Global Menu

InfoGo can be configured to present a "global menu", which is a menu of links to selected Dashboards, reports, and analyses, and is available to all users. To create and manage a global menu, a user must have the InfoGoReportManagersecurity Right.

If you're upgrading from a previous version and preserved your \_Settings file, to make this work you'll need to add a Startup Process element (Process Def File = *InfoGo.goManageReports*, Task = *RedirectToDefault*) to it.

![](https://devnet.logianalytics.com/hc/article_attachments/7522832217751/cfginfogo125_17c.png)

A user with that security Right will see a "Global Menu" folder in their folder list and can drag resources into, just like any other shared folder, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522854141207/cfginfogo125_17d.png)

If the user selects the Global Menu folder, he'll see its contents and can manage them as usual.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Remember that items in this folder are *not* copies of, or links to, items in the My Items folder. To remove them from the global menu *without deleting them*, drag them back to the My Items (or another) folder.

![](https://devnet.logianalytics.com/hc/article_attachments/7522832230679/cfginfogo125_17e.png)

Once items have been dragged into the Global Menu folder and the browser has been refreshed, a "hamburger" icon will be available at the top of the side-bar menu. When *any* user clicks it, a menu of links to the items in the Global Menu folder will slide out from the left, as shown above. Click again to close it.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Other users do not need the security Right to use the menu, but the Global Menu folder must be *shared* with them. Resources in the menu are automatically available to other users without the need to explicitly share them, but they cannot be modified beyond simple resizing of charts.

As a user drags items into the Global Menu folder, menu items are added to the "shared menu" Shared Element by a plug-in. Customizing the menu for additional folders and/or levels would require rewriting that plug-in and is probably not a realistic goal at this time.
