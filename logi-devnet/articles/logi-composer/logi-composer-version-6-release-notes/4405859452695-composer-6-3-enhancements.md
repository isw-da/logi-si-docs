---
title: "Composer 6.3 Enhancements"
id: 4405859452695
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859452695-Composer-6-3-Enhancements
updated_at: 2022-04-25T15:19:14Z
---

# Composer 6.3 Enhancements

# Composer 6.3 Enhancements

This topic describes the significant enhancements in Composer 6.3.

* [*Installation Changes*](#Installa)
* [*Rebranding Updates*](#Migratio)
* [*Custom Chart CLI Changes*](#Custom)
* [*Elasticsearch Connector Changes*](#Elastics)
* [*Data Source Permissions*](#Data)
* [*Column Security Updates*](#Column)
* [*Authorization Updates*](#Authoriz)
* [*User Interface Changes*](#User)

## Installation Changes

CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead.

In addition, Red Hat Linux 6 and Scientific Linux are no longer supported.

See [*Operating System and Software Requirements*](https://devnet.logianalytics.com/hc/en-us/articles/4405859384727-System-Requirements#Soft).

## Rebranding Updates

The `Content-Type` header `vnd.zoomdata.v2+json` is no longer supported in version 5.9.1 and later and can no longer be used as the `Content-Type` for API routes. It has been removed from the product. Use `vnd.composer.v2+json` as the `Content-Type` for API routes instead.

## Custom Chart CLI Changes

A new version 5 of the custom chart CLI is introduced in this release. It can be used with Composer versions 5.9.1 and later. CLI version 4 can continue to be used with Zoomdata 4 and with Composer versions 5.9 and earlier.

Version 3 of the custom chart CLI is now deprecated because it only supported Zoomdata version 3 and earlier and support for those older Zoomdata versions has been dropped. Use version 4 or version 5 of the custom chart CLI instead.

Custom chart CLI version 5 only supports the use of `vnd.composer.v2+json` as the `Content-Type` for API routes. CLI version 4 only supports the use of `vnd.zoomdata.v2+json`.

In addition, `Node.js` version 10 or later and `npm` version 5.6 or later are now required to install the custom chart CLI.

See [*Maintain Custom Charts Using the Custom Chart CLI*](https://devnet.logianalytics.com/hc/en-us/articles/4405859247127-Maintain-Custom-Charts-Using-the-Custom-Chart-CLI).

## Elasticsearch Connector Changes

This release introduces Composer Elasticsearch 6 and 7 connector support for Elasticsearch indices with a disabled `_source` field or with a `_source` field with exclusions. In past releases, only Elasticsearch data stores with the `_source` field enabled and with no exclusions were supported.

Composer Elasticsearch 6 and 7 connectors now support Elasticsearch data stores with any of the following source document configurations:

* Source documents are disabled.
* Source documents are enabled, but with some source exclusions.
* Source documents are enabled, with no exclusions.

The data sources created from connections to Elasticsearch data stores with any of these configurations function almost identically, with some small differences. For more information, see [*Elasticsearch Source Document Storage Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405850951959-Elasticsearch-Source-Document-Storage-Configurations).

In addition, a new `elasticsearch.inner-hits.size property` has been introduced for Elasticsearch 6 and 7 connectors. Use this property to specify the maximum number of hits to return per `inner_hits` query (used for raw data requests involving nested fields). The default value is 100. For more information, see [*Inner Hits Configuration Property*](https://devnet.logianalytics.com/hc/en-us/articles/4405850948375-Inner-Hits-Configuration-Property).

## Data Source Permissions

The following data source changes were made in this release:

* This release introduces source permissions, the ability to permit your account or specific groups or users in your account to read, write, or delete a data source configuration. To manage source permissions, one of the following conditions must be met:

  + The user must be an administrator, belonging to the [**Administrators** group](https://devnet.logianalytics.com/hc/en-us/articles/4405859110935-About-Supplied-Group-Definitions)
  + The user must belong to a group with the **Can Administer Sources** (ROLE\_ADMINISTER\_SOURCES) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) enabled.
  + The user must belong to a group with the **Can Manage Source Permissions** (ROLE\_PERMISSION\_SOURCES) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) enabled. If your user definition has only this privilege (and *not* the **Can Administer Sources** privilege), you will only be able to manage permissions for the data source configurations you can read.

  A new ![](https://devnet.logianalytics.com/hc/article_attachments/4406747386135/permissions_16x16.png) option in a new **Permissions** column on the UI Sources page allows you to specify data source configuration permissions for a data source. When selected, a new Source Permissions dialog appears. You can use the dialog to grant and revoke read, write, and delete permissions for specific data source configuration to your entire account or to groups or users in your account. If you are the creator of a data source configuration, you automatically receive read, write, and delete privileges for that data source.

  API updates were made to support data source permissions. See [*API Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes#API).

  For complete information, including considerations for data source permissions with connection definitions, fused data sources, and row and column security, see [*About Data Source Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions).

  As a result of the introduction of data source permissions in this release, the ability to restrict data sources within group definitions has been removed. See [*Manage Group Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850856599-Manage-Group-Definitions). Use data source permissions instead.
* If a user definition does not have access to any data source configurations (through [data source permissions](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions) or group [account privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)), the Sources page can now be viewed, but a message appears that reads "No sources are available."

## Column Security Updates

This release introduces support for multiple groups in a data source column security filter. In past releases, only a single group could be selected for a column security filter. Now you can select multiple groups. API updates were also made to support multiple groups in data source column security. See [*API Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes#API).

See [*Restrict Access to Fields Using Column Security*](https://devnet.logianalytics.com/hc/en-us/articles/4405851034007-Restrict-Access-to-Fields-Using-Column-Security).

## Authorization Updates

The following authorization updates were made in this release.

* A new **Can Manage Source Permissions** privilege has been added. This privilege allows a user to assign permissions to a data source configuration. It also allows a user to manage data source row and column security filters.
* A new **Can Administer Sources** privilege has been added. This privilege allows a user to create, import, export, modify and delete data source configurations. When a user is assigned this privilege, they are automatically assigned the **Can Create new Data Source** and **Can Manage Source Permissions** privileges. They are also automatically assigned the **Can Read Calculations** and **Can Edit Calculations** privileges.
* The **Can Export Dashboards & Data Sources** privilege has been renamed to simply **Can Export Dashboards** in this release. The ability to export a data source definition is now solely based on the user's read permissions for the data source.
* The API privileges ROLE\_DELETE\_ALL\_SOURCES, ROLE\_MANAGE\_ALL\_SOURCES, ROLE\_VIEW\_ALL\_SOURCES, and ROLE\_MANAGE\_SOME\_SOURCES have been removed from the product. When you upgrade, groups with these roles will be automatically upgraded with new source authorization settings as follows:

  + Groups with the ROLE\_VIEW\_ALL\_SOURCES privilege are automatically granted read permissions for all data sources.
  + Groups with the ROLE\_MANAGE\_ALL\_SOURCES privilege are automatically granted read and write permissions for all data sources.
  + Groups with the ROLE\_DELETE\_ALL\_SOURCES privilege are automatically granted read and delete permissions for all data sources.

See [*Group Privilege Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

## User Interface Changes

The following changes were made to the user interface in this release:

* A new Permissions column has been added to the Sources page. Select the icon in this column to add or manage the permissions for a data source configuration. See [*About Data Source Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions).
* The Column Security dialog has been changed to support multiple group column security filters. A new Add Groups button is provided that activates a new Add Groups dialog.
