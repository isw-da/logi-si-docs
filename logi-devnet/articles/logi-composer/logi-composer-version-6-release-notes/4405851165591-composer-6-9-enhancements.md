---
title: "Composer 6.9 Enhancements"
id: 4405851165591
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements
updated_at: 2022-04-25T15:19:14Z
---

# Composer 6.9 Enhancements

# Composer 6.9 Enhancements

This topic describes the significant enhancements in Composer 6.9.

* [*License Changes*](#License)
* [*Authorization Changes*](#Auth)
* [*Security Key Updates*](#Security)
* [*Connector Updates*](#Connector)
* [*New Visual Permissions*](#VisPerm)
* [*Dashboard Save Changes*](#DashboardSave)
* [*Dashboard Link Changes*](#DashboardLink)
* [*Dashboard Javascript Embed Update*](#Embed)
* [*New Dashboard Interactivity Setting*](#InteractDash)
* [*Visual Save Changes*](#VisualSave)
* [*New Visual Save As Support*](#VisualSaveAs)
* [*Visual Name Uniqueness*](#VisualNameUnique)
* [*New List Filter Visual Style*](#List)
* [*New Stacked Area Chart Options*](#Stacked)
* [*Table Changes*](#Table)
* [*New Visual Interactivity Settings*](#Interactivity)
* [*Experimental Materialized View Enhancements*](#MatView)
* [*New Experimental Alerting API Functionality*](#Alerts)
* [*Keyset Updates*](#Keyset)

## License Changes

This release implements a new license file structure and the Manage License page in the Supervisor UI has been updated to support the new license structure.

![](https://devnet.logianalytics.com/hc/article_attachments/4409070299415/criticalicon.gif)**IMPORTANT:** Older license keys are not compatible with Composer 6.9. If you are upgrading from any older Composer or Zoomdata release, a new license must be requested.

See [*Request and Apply a New License Key*](https://devnet.logianalytics.com/hc/en-us/articles/4405851108247-Request-and-Apply-a-New-License-Key).

In support of these changes, the following license properties have been removed from the `api/license` endpoint response: `type` and `enforcementLevel`.

## Authorization Changes

Two new privileges have been introduced in support of visual permissions in this release:

* The **Can Create Visuals** privilege allows users to create visuals. Users must have Read authorization for the data source used to create the visual.
* The **Can Manage Visual Permissions** privilege allows users to assign user, group, and account permissions for a visual.

If a user is granted the **Can Administer Visuals** privilege, they are now automatically granted both the **Can Create Visuals** and **Can Manage Visual Permissions** privileges as well. In addition, users with the **Can Administer Visuals** privilege are automatically granted read, write, and delete permissions to all visuals in the account. However, if they do not also have [read permission for the data source](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions) associated with a visual, they cannot see any data on the visual. See [*Group Privilege Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

In past releases, if a user had Read permissions for a data source, they also had Read permission to any visuals created using the data source. However, with the introduction of visual permissions in this release, this is no longer true. With this release, authorization for visuals is now controlled by visual permissions. See [*About Visual Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851253271-About-Visual-Permissions).

With this release, a non-administrative user must have the **Can Create Visuals** or **Can Administer Visuals**[group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) to add a visual.

With this release, a non-administrative user must also have the **Can Create Visuals** (or **Can Administer Visuals**[group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) to import a dashboard. In prior releases, they only needed the **Can Create new Data Sources** and **Can Create Dashboards**[group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

## Security Key Updates

Security keys are deprecated in this release and will be removed from the product in a future release. Use Trusted Access instead for all embedded workflows. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access).

However, while Composer still supports security keys, it's previous method of authorizing the use of visuals using new security keys changed due to the introduction of visual permissions in this release. In past releases, if a user was authorized to Read a data source, they were also authorized to Read any visual from that data source. This is no longer true. The following changes have been made:

* When you generate a new security key for a data source, users of the data source are automatically granted Read permission for all existing visuals using the data source, but not for any new visuals created after the security key was generated. Instead, a new security key must be generated for new visuals.
* When you generate a new security key for a dashboard, users of the dashboard are automatically granted Read permission for all existing visuals on the dashboard for which they have Read permissions. However, if a new visual is created on the dashboard after the security key is generated, dashboard users will not automatically be granted Read permission for the new visual. Instead, a new security key must be generated for newer visuals on the dashboard.

See [*Generate a Security Key*](https://devnet.logianalytics.com/hc/en-us/articles/4405851169431-Generate-a-Security-Key).

## Connector Updates

The following updates were made to Composer connectors in this release:

* The Elasticsearch 6 connector now supports Elasticsearch versions up to 6.8. In past Composer releases, the maximum supported Elasticsearch 6 version was 6.7. See [*Manage the Elasticsearch Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector).
* The Elasticsearch 7 connector now supports Elasticsearch versions up to 7.12. In past Composer releases, the maximum supported Elasticsearch 7 version was 7.6. See [*Manage the Elasticsearch Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector).
* The MySQL connector now supports MySQL versions 5.6 through 8.0. In past Composer releases, the only supported MySQL version was 5.6. See [*Manage the MySQL Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector).

## New Visual Permissions

This release introduces visual permissions. Visual permissions allow you to permit your entire account, groups within your account, or users within your account to read, write, or delete a visual. This allows you to share a visual with other users.

In past releases, if a user had Read permissions for a data source, they also had Read permission to any visuals created using the data source. However, with the introduction of visual permissions in this release, this is no longer true. With this release, authorization for visuals is now controlled by visual permissions.

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) If you upgrade from a previous version to Composer 6.9, previously created visuals are automatically granted account, group, or user permissions for the visual based on their current permissions for the data source used by the visual.

If a user belongs to a group that has the **Can Administer Visuals**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) enabled, the user can read, add, modify, or remove any visual in the Composer account. However, if the user does not belong to a group with this privilege enabled, the user can still be granted permission to read, write, or delete specific visuals in the account using visual permissions. Visual permissions allow users in an account or group to read, write, or delete a visual, regardless of any group privilege settings that ordinarily limit their ability to do so.

If a user belongs to a group that has the **Can Manage Visual Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) enabled, the user can modify the user, group, and account permissions for visuals. See [*About Visual Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851253271-About-Visual-Permissions).

A new **Permissions** option is now available on the More (![](https://devnet.logianalytics.com/hc/article_attachments/4409054856343/three-dots-menu.png)) menu for a visual in a dashboard, if the user has been granted the **Can Manage Visual Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference). Use this option to quickly view the Visual Permissions dialog for the visual and quickly make changes. See [*Use the Visual Menu*](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu).

API updates were made to support the new visual permissions. See [*API Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes#API).

## Dashboard Save Changes

The following changes have been made in this release when dashboards are saved:

* Saving dashboards has changed to support visual permissions. If a visual in a dashboard has changed, you can only save it if you have all of the following access rights and permissions:

  + The **Can Create Dashboards** [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)
  + The **Can Create Visuals** (or **Can Administer Visuals**) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)
  + Write [permission](https://devnet.logianalytics.com/hc/en-us/articles/4405859259159-About-Dashboard-Permissions) for the dashboard
  + Write [permission](https://devnet.logianalytics.com/hc/en-us/articles/4405851253271-About-Visual-Permissions) for the visual.

  If you only have read [permission](https://devnet.logianalytics.com/hc/en-us/articles/4405859259159-About-Dashboard-Permissions) for a dashboard, the ![](https://devnet.logianalytics.com/hc/article_attachments/4409070300183/dash-save.png) button with its **Save** and **Save As** options is not available on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar). If you have authorization to create dashboards (**Can Create Dashboard**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)), but do not have write permissions for the dashboard you are trying to save, only the **Save As** option is available.
* Pre-existing visuals are no longer automatically saved when you save a dashboard (new visuals are automatically saved). You must explicitly elect to save pre-existing visuals on the dashboard Save Options dialog. If you do not save pre-existing visuals with the dashboard and you do not [save the visuals](https://devnet.logianalytics.com/hc/en-us/articles/4405851257879-Save-Visuals-With-Their-Current-Names) individually, your visual changes will be lost when you close the dashboard.
* The **Save** and **Save As** options on the dashboard menu, which were listed on a submenu in prior releases, have been split and a new **Save As** dashboard icon, ![](https://devnet.logianalytics.com/hc/article_attachments/4409054856599/save-as_22x25.png), has been added to the dashboard icon bar. See [*Use the Dashboard Icon Bar*](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar).
* The dashboard Save Options dialog has changed. It may now show two tabs: **Existing Visuals** and **New Visuals**.

  + The **Existing Visuals** tab lists existing visuals with unsaved changes. It appears on the dialog only if there are any existing visuals with unsaved changes on the dashboard. A new checkbox on this tab allows you indicate whether the changed visuals should be saved when you save the dashboard. When you save a changed visual on a dashboard, a message now appears warning you that the change will affect all dashboards that use the visual.
  + The **New Visuals** tab lists new visuals added to the dashboard. It appears on the dialog only if there are any new visuals added to the dashboard. New visuals are always saved when you save the dashboard.

  See [*Save a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405850986647-Save-a-Dashboard).
* The dashboard Save As Options dialog, used to copy a dashboard, has changed. An option to also create copies for all of the dashboard visuals is now provided.

  + If you select this option, copies of all the pre-existing visuals are made along with the copy of the dashboard. You will be able to edit the copies of the visuals.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) New unsaved visuals on the dashboard will not be copied when this option is selected. New visuals must first be saved before they can be copied. Save the dashboard and the new visual first.
  + If you do not select this option, a warning on the dialog indicates that any changes made to the pre-existing visuals will be carried over to the new dashboard and, if you have appropriate permissions, you can save or undo the visual changes on the new dashboard.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) New unsaved visuals on the dashboard will be removed from the copied dashboard. New visuals must first be saved before they can be used on another dashboard. Save the dashboard and the new visual first.

  See [*Copy a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859260183-Copy-a-Dashboard).

## Dashboard Link Changes

Dashboard link information is no longer stored with visual definitions, but with the dashboard definitions. For this reason, the `dashboardLink` field has been removed from the visual payload and is now in the widget payload of the new dashboard API. See [*API Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes#API).

When you upgrade to Composer 6.9, the dashboard link information is automatically upgraded for you.

## Dashboard Javascript Embed Update

A new `composer-dashboard-failed` event has been added to the product and can be used in your Javascript embed code to control what happens when a dashboard fails to load. See [*Embedded Events*](https://devnet.logianalytics.com/hc/en-us/articles/4405851052695-Supported-Composer-v6-Embedded-Events)

## New Dashboard Interactivity Setting

A new dashboard interactivity setting is introduced in this release: **Share Filter Sets**. Use this setting to control whether saved filter sets for this dashboard can be shared with other users. See [*Control How Users Interact With a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard).

## Visual Save Changes

The option to **Save** a visual with its current name has been removed from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). Instead, the ![](https://devnet.logianalytics.com/hc/article_attachments/4409070300183/dash-save.png) icon appears at the top of visuals that need to be saved. This icon allows you to save the visual with its current name. To save it using a new name, use the new **Save As** option.

To save visuals with its current name, you must be logged in as an administrator or as a user with the **Can Create Visuals** or **Can Administer Visuals**[group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

See [*Save Visuals With Their Current Names*](https://devnet.logianalytics.com/hc/en-us/articles/4405851257879-Save-Visuals-With-Their-Current-Names).

## New Visual Save As Support

A new **Save As** option on the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) when a visual is edited in a dashboard, a new ![](https://devnet.logianalytics.com/hc/article_attachments/4409054856599/save-as_22x25.png) icon on the visual when edited in the Visual Gallery, and a new Save As Options dialog have been added. Use these to save a visual with a new visual name. The original visual still exists with its original name in the system.

To save visuals with a new name, you must be logged in as an administrator or as a user with the **Can Create Visuals** or **Can Administer Visuals**[group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

See [*Save Visuals With New Names*](https://devnet.logianalytics.com/hc/en-us/articles/4405859575447-Save-Visuals-With-New-Names) and [*Copy Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405859567895-Copy-Visuals).

## Visual Name Uniqueness

Visual name uniqueness is now enforced with this release. When you upgrade to this version, your visual names are automatically examined and changed to make them unique. The initial visual retains its visual name, but subsequent visuals with the same name append an incremented number in parentheses to the end of the name. For example, if the original name was **Orders**, the name of subsequent visuals with the same name is **Orders (<n>)**, where `<n>` is the number that increments for each visual with the same name.

When you attempt to save a visual in the Visual Gallery with the same name as another visual, an error message appears and the visual is not saved. However, when you save a new visual in a dashboard with the same name as another visual, the visual is saved, but an incremented number in parentheses `(<n>)` is appended at the end.

See [*Understand Visual Names and Titles*](https://devnet.logianalytics.com/hc/en-us/articles/4405851256087-Understand-Visual-Names-and-Titles).

## New List Filter Visual Style

A new visual style called a list filter has been added to the product. A list filter visual can be used to list the values of a data source field in a visual list. You can select one or more of the field values in the list to quickly apply a filter to other visuals in the dashboard that subscribe to a [cross-visual filter](https://devnet.logianalytics.com/hc/en-us/articles/4405859431447-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard) for the field. Regular visual filters can also be applied to a list filter visual itself. Filters applied to the list filter visual are saved when the visual or dashboard are saved. However, any filtering performed using the list filter visual is not saved when the dashboard is saved and any data selections made on the list filter visual are not saved.

The data source field selected for a list filter visual is initially set in a data source's list filter visual defaults, but can be changed using the List Filter Setting sidebar on a specific visual. You can also [modify the visual title and description](https://devnet.logianalytics.com/hc/en-us/articles/4405859521047-Modify-the-Visual-Title-and-Description).

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) A list filter visual cannot be converted to a different style, as other visual styles can using the [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu). Likewise, other visual styles cannot be converted to the list filter visual style.

See [*List Filter Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405859526295-List-Filter-Visuals) for more information.

## New Stacked Area Chart Options

Two new options on [Line Trend: Attribute Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859525143-Line-Trend-Attribute-Value-Charts) visuals now allow you to create stacked area charts. These options are **Display as stacked** and **Stacking Style**. The **Display as stacked** option allows you to control whether the visual data is displayed in a stacked format. When you turn the **Display as stacked** switch on (when you slide it to the right), the Stacking Style options become available.

Two new **Stacking Style** options are also provided: **Stacked** and **100% Stacked**. Use these options to control how the stacked format of the data is charted -- either as actual values or as a percentage of the whole. See [*Configure Settings for a Specific Attribute Value Line Chart*](https://devnet.logianalytics.com/hc/en-us/articles/4405859525143-Line-Trend-Attribute-Value-Charts#Configur3).

## Table Changes

If a table has been grouped, the options to export its raw or visual data are no longer available. You cannot export raw and visual table data after it has been grouped. See [*Export Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405851255191-Export-Visuals).

## New Visual Interactivity Settings

Three new visual interactivity settings are introduced in this release: **Maximize**, **Rename**, and **Show Time Bar Panel**. Use these settings to control how users interact with the visual.

| Use | To control the ability to: |
| --- | --- |
| Maximize | Maximize a visual for optimal viewing. |
| Rename | Rename a visual. |
| Show Time Bar Panel | Show the time bar. |

See [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual).

## Experimental Materialized View Enhancements

You can now create materialized view definitions using the Composer UI. In past releases, they could only be created using the API.

![](https://devnet.logianalytics.com/hc/article_attachments/4409070299415/criticalicon.gif) This is an experimental feature.

Configuring a materialized view allows you to use pre-aggregated data to serve the results of a query and speed up query processing. It is especially effective when executing queries that process large volumes of data and heavily aggregate the data.

For more information, see [*Use Materialized Views (Experimental)*](https://devnet.logianalytics.com/hc/en-us/articles/4405859403287-Use-Materialized-Views-Experimental-).

## New Experimental Alerting API Functionality

This release introduces new API endpoint that you can use to alert your end users when a metric reaches a specified threshold. Composer API endpoints can be used to manage (list, create, update, and delete) alert definitions, each describing an alert condition, the schedule by which it is evaluated, and how notification is handled when the alert condition is met. See [*Manage Alerts*](https://devnet.logianalytics.com/hc/en-us/articles/4405859133079-Manage-Alerts).

![](https://devnet.logianalytics.com/hc/article_attachments/4409070299415/criticalicon.gif) This is an experimental feature.

## Keyset Updates

An error now displays when an attempt to upload keyset values uses a keyset upload file that contains more records than are allowed by the Composer environment configuration.
