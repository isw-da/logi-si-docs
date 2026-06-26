---
title: "Designating a Global Main Page"
id: 4419722765207
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722765207-Designating-a-Global-Main-Page
updated_at: 2022-07-17T02:24:55Z
---

# Designating a Global Main Page

# Designating a Global Main Page

InfoGo can be configured to present a "global main page", which will be the starting page all users will see (rather than the Home page) when they first run the application. To set a global main page, the user must have the InfoGoReportManagersecurity Right.

If you're upgrading from a previous version and preserved your \_Settings file, to make this work you'll need to add a Startup Process element (Process Def File = *InfoGo.goManageReports*, Task = *RedirectToDefault*) to it.

![](https://devnet.logianalytics.com/hc/article_attachments/7522862398615/cfginfogo125_17b.png)

When a user with the appropriate security Right navigates to an InfoGo Dashboard or report and clicks the gear icon, he'll see the **Set as Global Main Page** option shown above. Once the main page is set, the same option becomes **Unset as Global Main Page** to reverse the process, if desired.

![](https://devnet.logianalytics.com/hc/article_attachments/7522848073751/cfginfogo125_17a.png)

Once a main page has been set, the Main Page option will appear at the top of the menu, as shown above. Users may need to refresh the page or close and restart their browser in order to see it.

If the Dashboard or report set as the global main page has been, or is subsequently, shared with others, they too will see it as their starting page (they do not need a specific security Right to see it).
