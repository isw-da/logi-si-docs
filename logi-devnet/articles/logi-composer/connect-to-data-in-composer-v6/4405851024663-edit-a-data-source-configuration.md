---
title: "Edit a Data Source Configuration"
id: 4405851024663
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851024663-Edit-a-Data-Source-Configuration
updated_at: 2021-09-21T01:28:14Z
---

# Edit a Data Source Configuration

# Edit a Data Source Configuration

You can only edit a data source configuration if you are logged in as an administrator, a user with the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference), or a user with **write**[permission](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions) for the data source.

To edit a data source configuration:

1. Make sure you are logged in as a Composer administrator, a user with the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference), or a user with **write**[permission](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions) for the data source.
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or the [top-level navigation menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. In the table on the Sources page, locate and select the data source configuration you want to edit. The data source configuration wizard appears.
4. Select and alter the settings on the tabs in the data source configuration wizard, as appropriate.

   * [*General Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859318039-General-Tab)
   * [*Connection Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405851023767-Connection-Tab)
   * [*Tables/Indices Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859323287-Tables-Indices-Tab)
   * [*Fields Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab)
   * [*Refresh Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859322007-Refresh-Tab)
   * [*Visuals Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab)

   See also [*Define a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405859320727-Define-a-Data-Source-Configuration).

   If you change the data table (schema, index, or collection) used by the data source configuration on the [*Tables/Indices Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859323287-Tables-Indices-Tab), you will be prompted to confirm the change because it will be applied to any visuals currently using this data source configuration. In addition, because the field, visual, and refresh settings are reset to defaults after you change the data table, you are encouraged to review and alter (if necessary) the Fields tab, the Refresh tab, and the Visuals tab for the configuration.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) For flat file data connectors, the Connection tab is replaced with a Data tab and there is no Tables or Indices tab.

   For information on configuring the time bar or search bar defaults, including the refresh rate settings, for your data source, see [*Configure Time Bar Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4405859324311-Configure-Time-Bar-Defaults) and [*Configure Search Box Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4405851028503-Configure-Search-Box-Defaults).
5. When your changes are complete, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743833239/save-white-btn.png), ![](https://devnet.logianalytics.com/hc/article_attachments/4406743834903/save-next-btn.png), or ![](https://devnet.logianalytics.com/hc/article_attachments/4406743835287/finish-btn.png) (depending on the tab) to save the data source configuration and close the wizard.
