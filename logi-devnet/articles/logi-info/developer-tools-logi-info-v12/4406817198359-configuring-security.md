---
title: "Configuring Security"
id: 4406817198359
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817198359-Configuring-Security
updated_at: 2022-04-06T06:04:34Z
---

# Configuring Security

# Configuring Security

As an optional feature, Logi Security can be used with InfoGo to authenticate users and to control access to application features and data. For information about Logi Security in general, see [Logi Security Scenarios](https://devnet.logianalytics.com/hc/en-us/articles/4406817836055-Logi-Security-Scenarios-).

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) If you do not enable Logi Security then *all* of the features usually controlled by security, including the Data Manager, *will be available to all users*. You can, however, "hide" a feature by hiding its side-bar menu item (by remarking its elements in the InfoGo.goShared
definition, under the sharedGoBox shared element) and by renaming the related definition file (to prevent direct browsing).

![](https://devnet.logianalytics.com/hc/article_attachments/4417563447959/cfginfogo125_12.png)

As shown above, to use Logi Security, add a **Security** element to the \_Settings definition, along with whatever child elements are needed for your security scenario and configure them accordingly.

Access to features and data is controlled using the **Security Right ID**, which is an attribute of many elements. For example, the visibility of the Analysis Grid element in a report can be controlled by setting its Security Right ID attribute. You can use this approach to control the availability of many of the elements used in InfoGo. In general, you can assign arbitrary string values for security Rights but these standard Rights have specific purposes:

| Security Right | Purpose |
| --- | --- |
| InfoGoDataManager | Enables the Data Manager page, allowing the creation and management of connections and metadata from inside InfoGo, and displays an option in the menu. You'll also need to add the default rdMetadataAdmin right, or your own custom right, as discussed in [Using the Web Metadata Builder](https://devnet.logianalytics.com/hc/en-us/articles/4406822571159-Using-the-Web-Metadata-Builder). |
| InfoGoReportManager | Enables the ability to select a Global Main Page and to create and share a Global Menu. Also allows editing of shared items. |
| InfoGoScheduleManager | Enables the Schedule Manager page, allowing the creation and management of scheduled reports from inside InfoGo, and displays an option in the menu. |
| InfoGoThemeManager | Enables the Theme Editor page, allowing the management of a customized theme from inside InfoGo, and displays an option in the menu. |

InfoGo includes a standard logon page, which you can reference in the Security element's Logon Page and Logon Fail Page attributes. You can customize this page which, if the default installation location was used, is

C:\Program Files\Logi Analytics\InfoGo\rdLogon.aspx

You cannot edit .aspx pages in Logi Studio, so you'll need to use some other editing tool, like Notepad.

If you plan to implement sharing of bookmarks, see the security discussion in [Setting Up Sharing](https://devnet.logianalytics.com/hc/en-us/articles/4406817205143-Setting-Up-Sharing).

There are two special opportunities to implement **data security** in the InfoGo application. Assuming you have Logi Security enabled:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563449367/cfginfogo125_13.png)

1. When using the Web Metadata Builder, you can assign Security Right ID values to tables and to columns, as shown above. These tables and columns will only appear in InfoGo's Analysis page's Data tab if the logged-in user has the appropriate security Rights.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563449495/cfginfogo125_14.png)
2. The Metadata element has its own Security Right ID attribute. In the \_Settings definition fragment shown, there are three Metadata elements in use. Normally, all three would appear in the Analysis page's Data tab, in the Source selector. However, if the metaMarket element is configured with a Security Right ID, as shown above, then the logged-in user will only see it in the Source selector if he or she has the appropriate security Rights.
