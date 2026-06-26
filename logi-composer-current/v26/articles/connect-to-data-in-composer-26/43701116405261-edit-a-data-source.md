---
title: "Edit a Data Source"
id: 43701116405261
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source
updated_at: 2026-05-29T14:11:02Z
---

# Edit a Data Source

# Edit a Data Source

You can only edit a data source configuration if you are logged in as a user with the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or a user with **read** and **write** [permission](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for the data source.

You can add additional [data entities](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab#Data) to a source to convert into a fusion data source at any time. See [Create a Fusion Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072201741-Create-a-Fusion-Source).

**Edit a data source configuration**

1. Log in as a user with the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or a user with **read** and **write** [permission](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for the data source.
2. Select **Sources** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243275643149)). The [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page appears.
3. On the [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page, locate and select the data source configuration you want to edit. The Source Creation work area opens.
4. Select and alter the settings on the tabs, as appropriate. Some changes can include, but are not limited to:

   * [Source Creation Tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab)

     + Add or change data entities, files, or connections. If fields from the original source are in use in a visual, you can make a change if the same field is present in the new entity, file, or connection.
     + Add or remove fields. Fields can't be removed if in use in a visual, but can be hidden on the Fields tab.
   * [Manage Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields)

     + Hide fields, edit Settings of fields, derived fields, and custom metrics.
     + Upload a translation file.
     + Update field capabilities for your fields in bulk.
     + Add or edit derived fields and custom metrics.
     + Add hierarchy fields.
   * [Cache Tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab)

     + Edit cache settings, including scheduling refresh jobs.
   * [Global Settings Tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085233549-Global-Settings-Tab)

     + Make changes to new and existing visuals.

   See also [Define a Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080450061-Define-a-Source).
5. When your changes are complete, select **Save Source**.

**Important:** Applied filter values that later have **Filtering** disabled to not automatically mask or hide those fields. You must recreate the filter that uses these values.

**Note:** 
When you add a new field to a data source, the scheduled refresh is not enabled for the new fields by default. Quickly enable scheduled refresh for all fields using the bulk update option in the [Schedule Refresh menu on the Cache](#schedulerefresh) tab, or enable each field for scheduled refresh manually on the Cache tab.

If you attempt make changes that remove a field currently in use by a visual, you can't save your changes to the source unless specific conditions are met:

* You remove the visuals using affected fields.

For information on configuring the time bar or search bar defaults, including the refresh rate settings, for your data source, see [Configure Time Bar Defaults](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080606477-Configure-Time-Bar-Defaults) and [Configure Search Box Defaults](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068987277-Configure-Search-Box-Defaults).
