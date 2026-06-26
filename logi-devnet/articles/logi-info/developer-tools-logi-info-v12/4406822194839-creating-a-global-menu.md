---
title: "Creating a Global Menu"
id: 4406822194839
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822194839-Creating-a-Global-Menu
updated_at: 2022-04-06T06:04:34Z
---

# Creating a Global Menu

# Creating a Global Menu

InfoGo can be configured to present a "global menu", which is a menu of links to selected dashboards, reports, and analyses, and is available to all users. To create and manage a global menu, a user must have the InfoGoReportManager security Right.

If you're upgrading from a pervious version and preserved your \_Settings file, to make this work you'll need to add a Startup Process element (Process Def File = *InfoGo.goManageReports*, Task = *RedirectToDefault*) to it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584084759/cfginfogo125_17c.png)

A user with that security Right will see a "Global Menu" folder in their folder list and can drag resources into, just like any other shared folder, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575825943/cfginfogo125_17d.png)

If the user selects the Global Menu folder, he'll see its contents and can manage them as usual.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Remember that items in this folder are *not* copies of, or links to, items in the My Items folder. To remove them from the global menu *without deleting them*, drag them back to the My Items (or another) folder.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563447831/cfginfogo125_17e.png)

Once items have been dragged into the Global Menu folder and the browser has been refreshed, a "hamburger" icon will be available at the top of the side-bar menu. When *any* user clicks it, a menu of links to the items in the Global Menu folder will slide out from the left, as shown above. Click again to close it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Other users do not need the security Right to use the menu, but the Global Menu folder must be *shared* with them. Resources in the menu are automatically available to other users without the need to explicitly share them, but they cannot be modified beyond simple resizing of charts.

As a user drags items into the Global Menu folder, menu items are added to the "shared menu" Shared Element by a plug-in. Customizing the menu for additional folders and/or levels would require rewriting that plug-in and is probably not a realistic goal at this time.
