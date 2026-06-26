---
title: "Logi Composer Version 6 Summary of Changes"
id: 4405851159959
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851159959-Logi-Composer-Version-6-Summary-of-Changes
updated_at: 2022-04-25T15:19:14Z
---

# Logi Composer Version 6 Summary of Changes

# Logi Composer Version 6 Summary of Changes

This is a summary of the major changes made in version 6 of Composer. It is provided so you can quickly identify new and changed Composer features before upgrading from Composer 5 to Composer 6. If you are upgrading from a Zoomdata version, be sure to read the release summary for Composer 5 as well.

Be sure to back up your metadata store (see [*Back Up the Metadata Store*](https://devnet.logianalytics.com/hc/en-us/articles/4405859506199-Back-Up-the-Metadata-Store)) before you upgrade.

In addition to resolving problems and applying security fixes, Composer 6 introduced changes in the following areas.

* [*License Changes*](#License)
* [*Installation Changes*](#Installa)
* [*Security Changes*](#Security)
* [*API Specification Format Change*](#API)
* [*Authorization Changes*](#Authoriz)
* [*Rebranding Updates*](#Rebrandi)
* [*Embedded Analytics Updates*](#Embed)
* [*Connector Updates*](#Connecto)
* [*Data Source Changes*](#Data)
* [*Data Manipulation Changes*](#Data2)
* [*Visual Changes*](#Visual)
* [*Dashboard Changes*](#Dashboar)
* [*Keyset Updates*](#Keyset)
* [*Experimental Materialized View Changes*](#Experime)
* [*Experimental Alerting Introduced*](#Experime2)
* [*Performance Updates*](#Performa)
* [*Query Engine Changes*](#Query)
* [*Deprecated Features*](https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes#Deprecat)
* [*Removed Features*](https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes#Removed)

## License Changes

This release implements a new license file structure.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif)**IMPORTANT:** Older license keys are not compatible with Composer 6.9. If you are upgrading from any older Composer or Zoomdata release, a new license must be requested. See [*Request and Apply a New License Key*](https://devnet.logianalytics.com/hc/en-us/articles/4405851108247-Request-and-Apply-a-New-License-Key).

## Installation Changes

The following installation changes have been made in this release.

* CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead.
* Red Hat Linux 6 and Scientific Linux are no longer supported.

## Security Changes

The following security-related changes have been made in this release.

* Composer now provides its own security methodology that allows for machine-to-machine authorization of Composer resources when embedded in your application (the “parent” application). This is a form of “delegated” authorization where the parent application can determine, on demand, how and when to authorize any given embedded Composer component to an end-user logged into the parent application. This methodology is called *[*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access)*.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.
* Security keys are deprecated and will be removed from the product in a future release. However, while Composer still supports security keys, it's previous method of authorizing the use of visuals using new security keys changed with the introduction of [visual permissions](#Visual).
* If your installation uses Kerberos, the default behavior for unauthenticated users has changed. From a browser, unauthenticated users are now redirected to the Composer login page.
* For API calls, links in the format `<hostname>:8080/api/version` or `<hostname>:8080/zoomdata/api/version` now return an unauthorized 401 error. To resolve the error, use `<hostname>:8080/composer/api/version`.

## API Specification Format Change

The Composer API specification is now generated in OpenAPI 3.0 format.

A new media type, `application/vnd.composer.v3+json` is introduced in this release. The media type `application/vnd.composer.v2+json` is deprecated and will be removed in a future release. Logi Analytics recommends using the `application/vnd.composer.v3+json` media type for all API calls. The difference between the two media types is primarily in the response of listing endpoints.

With this release, you can no longer use `<hostname>:8080/zoomdata/api/version`. This is no longer supported. Use `<hostname>:8080/composer/api/version` instead.

The following table lists all of the other API updates in this release:

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/user/permissions/visuals/<visualId>` | GET | This new endpoint can be used to retrieve a user's permissions for a visual. |
| `/api` (`/composer/api`) | GET | This API endpoint is now deprecated and will be removed from the product in a future release. |
| `/api/alerts` | GET PUT DELETE PATCH POST | A new, experimental, API is introduced in this release that can be used to alert your end users when a metric reaches a specified threshold. No UI support for this feature is provided at this time. See [*Manage Alerts*](https://devnet.logianalytics.com/hc/en-us/articles/4405859133079-Manage-Alerts). |
| `/api/dashboard/<dashboard-ID>?interactivityProfile={linked | readonly | interactive}` | GET | This new endpoint returns the dashboard payload with one of the following three profile names:   * `linked`: Uses the [dashboard interactivity profile](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard) set for the dashboard. * `readonly`: Overrides the [dashboard interactivity profile](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard), setting all visual interactivity settings to `false`, so users can view the dashboard and its visuals, but not interact with them. * `interactive`: Overrides the [dashboard interactivity profile](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard) and all visual interativity settings to `true`, so users can view and interact with the dashboard and its visuals. This is the opposite of `readonly`. |
| `/api/dashboards/*` | DELETE GET POST PUT | This endpoint in the v1 version of the API (`application/vnd.composer.dashboard.v1+json`) is deprecated and will be removed in a future release. Use the new version of the endpoint in the v2 version of the API (`application/vnd.composer.dashboard.v2+json`) instead. |
| DELETE GET PUT | The new `/api/dashboards` API endpoint no longer relies on visuals. Instead, it uses widgets.   * The `visualizations` container is renamed to `widgets`. * The new `widgets` array contains `widget` objects, which contain only widget-specific information: `id`, `name`, `description`, `layout`, `visualId`, and `dashboardLink`.   In addition, the `bookmarksMap` object returned in the response when using the v3 version of the Composer API (`application/vnd.composer.v3+json`) has been renamed `content`.  The `/api/dashboard` family of API endpoints were updated with a new payload in this release. Contact Customer Support to use `vnd.composer.dashboards.v1+json` for backward compatibility, including the use of the `bookmarksMap` object (instead of the new `content` object). |
| `/api/dashboards/<dashboard-id>/acls/bulk` | PATCH | This new endpoint assigns permissions for a dashboard to a list of security identities (groups, users, accounts). |
| `/api/dashboards/<dashboard-ID>/interactivity` | DELETE | This new endpoint deletes a dashboard's interactivity profile. |
| PUT | This new endpoint saves a dashboard's interactivity profile. |
| GET | This new endpoint returns the dashboard's interactivity profile. If you do not have authorization for a dashboard, errors are returned. |
| /`api/dashboards/interactivity` | GET | This new endpoint lists the existing dashboard interactivity profiles. |
| `/api/export/generate/rawdata` | --- | This endpoint is deprecated and will be removed in a future release. Use `/api/export/csv/raw` instead. |
| `/api/groups` |  | The `configType` field is deprecated and will be removed in a future release. |
|  | The `sources` field is deprecated and will be removed in a future release. |
| `/api/keysets/upload` | POST | This new endpoint creates a keyset from a CSV file. See [*Upload Keyset Data From a CSV File Using the API*](https://devnet.logianalytics.com/hc/en-us/articles/4405851106327-Upload-Keyset-Data-From-a-CSV-File-Using-the-API). |
| `/api/keysets/upload/<keyset-id>` | PUT | This new endpoint updates a keyset from a CSV file. See [*Update Keyset Values From a CSV File Using the API*](https://devnet.logianalytics.com/hc/en-us/articles/4405851105431-Update-Keyset-Values-From-a-CSV-File-Using-the-API). |
| `/api/materialized-views` | GET | A new, optional parameter, `?source={<data-source-id>}`, has been added in this release. Use to obtain materialized view data for a specific data source. |
| `/api/screenshot/*` | GET POST PUT | The screenshot-related endpoints are deprecated and will be removed in a future release. |
| `/api/security/sids` | --- | This new endpoint is introduced to retrieve security ID information. The `sidTypes` parameter can be specified with this new endpoint to limit the type of security ID information retrieved. Valid values for `sidTypes` are `GROUP`, `USER`, `ACCOUNT`, or `ALL` (the default). |
| `/api/sources/<source-id>/acls` | GET | Retrieves a list of access rights for a data source. You can restrict the list to specific users, groups, or accounts using the `sidTypes` parameter. In addition, you can use the `returnSids` parameter to restrict the list so it retrieves only users, groups, or accounts with access to the data sources or to only users, groups, or accounts without access. |
| `/api/sources/<source-id>/acls/bulk` | PATCH | This new endpoint assigns permissions for a data source to a list of security identities (groups, users, accounts). |
| PUT | Grants or revokes permissions to a data source configuration a list of groups, users, or accounts. |
| `/api/sources/<source-id>/cache` | DELETE | Clears both the visual and metadata caches. |
| `/api/sources/<source-id>/cache/metadata` | DELETE | Clears the metadata cache. |
| `/api/sources/<source_id>/cache/visdata` | DELETE | Clears the visual data cache. |
| `/api/sources/<source-ID>/fields/meta` | GET | This new endpoint is an experimental endpoint that returns information about all the fields and metrics in a data source. |
| `/api/sources/<source-id>/key` | GET | This security-related endpoint is deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) and [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access). |
| `/api/sources/<source-id>/security/attributes` | --- | This endpoint now supports the specification of multiple groups for a data source column security filter. |
| `/api/sources/<source-id>/security/attributes/<id>` | --- | This endpoint now supports the specification of multiple groups for a data source column security filter. |
| `/api/sources/<source-id>/security/filters` | --- | This endpoint is enhanced to support account and user security identifiers. In past releases, only group security identifiers were supported. |
| `/api/sources/key` | GET | This security-related endpoint is deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) and [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access). |
| `/api/sources/remove/<id>` | DELETE | This security-related endpoint is deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) and [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access). |
| `/api/trusted-access/clients` | POST | Creates a Trusted Access client. The request must specify the number of seconds for which the access token is valid and the client name. The client name must be unique. When you create the client, the client ID, client secret, secret expiration time, and the token authentication method are automatically generated. |
| GET | Returns all the Trusted Access client information in the metadata. Included with this information is the access token validity time (in seconds), client ID, client name, client secret expiration time (in seconds), and the token authentication method. For a description of these, see [*Trusted Access Client Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859468951-Trusted-Access-Client-Properties). |
| `/api/trusted-access/clients/<id>` | GET | Returns the Trusted Access client information for a specific client. The request must specify the client ID. |
| DELETE | Deletes a specific Trusted Access client. The request must specify the client ID. |
| PATCH | Updates the Trusted Access client information for a specific client. The request must specify the client ID and the number of seconds for which the access token is valid. |
| `/api/trusted-access/token` | POST | Generates a new access token for a user. The request must specify the Composer user name. The user must already exist, and have an active Composer user account (unless you are using LDAP with automatic provisioning for Composer). |
| `/api/user/permissions/sources` | GET | Lists the permission levels for the logged in user for all data source configurations in the system. |
| `/api/user/permissions/sources/<sourceid>` | GET | Retrieves the currently logged in user's source permissions for a data source. |
| `/api/user/permissions/visuals/<visual-id>` | GET | This new endpoint retrieves the permissions for a visual for the currently logged in user. |
| `/api/visdefs/<sourceid>` | --- | This endpoint is deprecated and removed. It is replaced by a new `/api/visuals/source/<sourcid>/summary` endpoint. The response produced by the new endpoint has also changed to include a new `visualId` setting. |
| `/api/visdefs/default/<sourceId>` | -- | This API endpoint has now been removed from the product. It was deprecated in a previous release. |
| `/api/visdefs/default/<sourceId>/<visualId>` | GET | This API endpoint now checks for READ permission to the data source when generating a single visual default. |
| `/api/visualizations/libs/*` | DELETE GET POST PUT | The `/api/visualizations/libs` endpoint is deprecated and will be removed in a future release. Use the custom chart CLI instead. See [*Maintain Custom Charts Using the Custom Chart CLI*](https://devnet.logianalytics.com/hc/en-us/articles/4405859247127-Maintain-Custom-Charts-Using-the-Custom-Chart-CLI). |
| `/api/visuals` | PUT DELETE POST | The following fields in the response payload of all other `/api/visuals` endpoints are deprecated and will be removed in a future release.   * `enabled` * `ownerType` * `lastModified` (use `lastModifiedDate` instead) * `ownerSourceId` (use `source.sourceId` instead) * `name` (use `visualName` instead) * `dashboardLinks` ((this field is now defined and stored in the new dashboard API response payload) |
| GET | The following fields in the response payload are deprecated and will be removed in a future release.   * `enabled` * `ownerType` * `name` (use `visualName` instead) * `dashboardLinks` (this field is now defined and stored in the new dashboard API response payload) |
| The payload from this API now can include permission information for the visual, if the query parameter `includePermissions=true` is included, enabling this capability. |
| `/api/visuals/<visualId>` | GET PUT DELETE | The visual permissions for a user are now verified when this API endpoint is used to retrieve, update, or delete a visual. |
| `/api/visuals/<visualId>/acls` | GET | This new endpoint can be used to list the users and groups for which visual permissions have been defined. |
| `/api/visuals/<visualId>/acls/bulk` | PATCH | This endpoint can now be used to grant or revoke visual permissions. However, the `ownerType=Source` property can no longer be specified because permissions to view or manage a visual are no longer tied to your permissions for its data source. However, read permissions for the visual's data source are required to see data in the visual. |
| `/api/visuals/source/<source-id>/summary` | GET | This API endpoint now checks for READ permission to the data source when reading a summary of all the visual defaults. |
| This endpoint obtains the default visual definitions for a data source configuration. |
| `/oauth/authorize` | GET | This endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See [*Trusted Access API Endpoints*](https://devnet.logianalytics.com/hc/en-us/articles/4405851180439-Trusted-Access-API-Endpoints). |
| `/oauth2/client` | DELETE GET POST PUT | This endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See [*Trusted Access API Endpoints*](https://devnet.logianalytics.com/hc/en-us/articles/4405851180439-Trusted-Access-API-Endpoints). |
| `/oauth2/token` | DELETE GET POST | This endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See [*Trusted Access API Endpoints*](https://devnet.logianalytics.com/hc/en-us/articles/4405851180439-Trusted-Access-API-Endpoints). |
| `description` property | --- | A new property called `description` is added to the visual payload. |
| Group privilege renamed |  | The API privilege **ROLE\_MANAGE\_VISUALS** was renamed to **ROLE\_ADMINISTER\_VISUALS**. Customers who use the API to manage groups must manually make this change wherever **ROLE\_MANAGE\_VISUALS** is currently used. See [*Authorization Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859454231-Composer-6-6-Enhancements#Authoriz). |
| Group Updates | --- | Groups can no longer be transferred to a different account using the API. |
| Source definition endpoints | --- | A new boolean `cacheableMetadata` property indicates whether metadata caching is enabled for a data source. The existing `cacheable` property indicates whether caching, in general, is enabled for the data source. |
| Source definition endpoints | --- | A new `statsCached` property allows you to control metadata (field statistics) caching on a per-field basis. This property can be used to configure the field statistics look-up via materialized views (ignoring internal caches and redirecting the requests from the original source) and to improve the performance of statistics requests when precreated statistics data exists. Please contact your Technical Support representative to get guidance on how to configure this. |
| Visual placement | --- | An error is now produced when you try to place the same visual on a dashboard twice. |

## Authorization Changes

The following changes in group privileges have been made in this release.

* The group privilege **Can Manage Visuals** has been renamed to **Can Administer Visuals**. The corresponding API privilege **ROLE\_MANAGE\_VISUALS** is also renamed to **ROLE\_ADMINISTER\_VISUALS**. Customers who use the API to manage groups must manually make this change wherever **ROLE\_MANAGE\_VISUALS** is currently used; if you use the Composer user interface (UI) to manage groups, the change will happen automatically. In addition, to alter and save an individual visual in a dashboard now, you must either be assigned to a group with the **Can Administer Visuals** (**ROLE\_ADMINISTER\_VISUALS**) privilege or be the creator of the visual.
* Two new privileges, **Can Create Visuals** and **Can Manage Visual Permissions** have been introduced to support [visual permissions](#Visual). When a user is granted the **Can Administer Visuals** privilege, they are now automatically granted both the **Can Create Visuals** and **Can Manage Visual Permissions** privileges as well. A non-administrative user must have the **Can Create Visuals** or **Can Administer Visuals**[group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) to add a visual. Finally, a non-administrative user must also have the **Can Create Visuals** (or **Can Administer Visuals** [group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) to import a dashboard. In prior releases, they only needed the **Can Create new Data Sources** and **Can Create Dashboards**[group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).
* New **Can Manage Source Permissions** and **Can Administer Sources** privileges have been added to support [data source permissions](#Data).
* The **Can Export Dashboards & Data Sources** privilege is renamed to simply **Can Export Dashboards**.

Finally, groups can no longer be transferred to a different account using the API.

See [*Group Privilege Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)

## Rebranding Updates

The following rebranding updates have been made in this release.

* The `Content-Type` header `vnd.zoomdata.v2+json` is no longer supported in version 5.9.1 and later and can no longer be used as the `Content-Type` for API routes. It is removed from the product. Use `vnd.composer.v2+json` as the `Content-Type` for API routes instead.
* The name Zoomdata has been replaced with Composer in error messages for source and dashboard imports as well as in several messages in log files.
* The Service Monitor has been rebranded.
* Error messages in the UI have been rebranded.
* The word "chart" has been changed to "visual," where appropriate, in the translation file used for internationalization.

## Embedded Analytics Updates

The following changes have been made for embedded analytics in this release.

* Significant changes have been made to how dashboards can be embedded in your applications. Primarily, while your existing embedded dashboard HTML snippets will continue to work, this release introduces the ability to embed dashboards using JavaScript code. This is more powerful than the HTML script snippet provided in previous releases because it provides you with more tailoring options for the dashboards in your application.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.

* This release introduces the ability to embed Composer's visual authoring experience in your applications using JavaScript. This allows your end users to add and maintain the visuals embedded in a dashboard.
* Embedded dashboards can now be controlled by dashboard interactivity settings. Several new properties and a new object for the Javascript `createComponent` method used to embed dashboards are added to support dashboard interactivity.

See [*Embed Composer Components Into Your Application*](https://devnet.logianalytics.com/hc/en-us/articles/4405859263895-Embed-Composer-Components-Into-Your-Application).

## Connector Updates

The following data connector updates have been made in this release.

* Multiple Elasticsearch connector changes have been made:

  + The Elasticsearch 6 connector now supports Elasticsearch versions up to 6.8. In past Composer releases, the maximum supported Elasticsearch 6 version was 6.7.
  + The Elasticsearch 7 connector now supports Elasticsearch versions up to 7.12. In past Composer releases, the maximum supported Elasticsearch 7 version was 7.6.
  + Support for Composer Elasticsearch 6 and 7 indices with a disabled `_source` field or with a `_source` field with exclusions has been introduced. In past releases, only Elasticsearch data stores with the `_source` field enabled and with no exclusions were supported.
  + A new `elasticsearch.inner-hits.size property` has been introduced for Elasticsearch 6 and 7 connectors.

  See [*Manage the Elasticsearch Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector).
* The MySQL connector now supports MySQL versions 5.6 through 8.0. In past Composer releases, the only supported MySQL version was 5.6. See [*Manage the MySQL Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector).
* The MongoDB connector now supports MongoDB versions up to 4.4. See [*Manage the MongoDB Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector).
* The maximum version of Spark SQL data stores supported by the Composer Spark SQL connector is now version 3.0. See [*Manage the Spark SQL Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850963991-Manage-the-Spark-SQL-Connector).
* A new Dremio connector is introduced. See [*Manage the Dremio Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405859221911-Manage-the-Dremio-Connector).

## Data Source Changes

### Data Source Permissions

This release introduced data source permissions, the ability to permit your account or specific groups or users in your account to read, write, or delete a data source configuration. As a result of the introduction of data source permissions, the ability to restrict data sources within group definitions is removed.

You can now only assign data source permissions equivalent to your own.

See [*About Data Source Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions).

### Fused Data Sources

Text fields can now be joined in fused data sources. In addition, you can now join data sources by a derived field in a fused data source. See [*Fuse Data Sources*](https://devnet.logianalytics.com/hc/en-us/articles/4405851072279-Fuse-Data-Sources).

### Row Security Filters

* A new "Data Unavailable" message now appears when an error occurs obtaining data from a data source for a row security filter. In addition, if a row security filter returns no results, a new "No search results" message appears.
* The row security restrictions specified for a data source configuration can now reference the same field in the data source. In past releases this was not possible.
* Row security is enhanced to allow you to use filters to restrict data source data for specific users or accounts. In past releases you could only restrict the data for specific groups.

See [*Restrict Access to Data Using Row Security*](https://devnet.logianalytics.com/hc/en-us/articles/4405859333655-Restrict-Access-to-Data-Using-Row-Security).

### Column Security Filters

* This release introduces support for multiple groups in a data source column security filter. In past releases, only a single group could be selected for a column security filter.The row security and column security restrictions specified for a data source configuration can now reference the same field in the data source. In past releases this was not possible.
* The column security restrictions specified for a data source configuration can now reference the same field in the data source. In past releases this was not possible.

See [*Restrict Access to Fields Using Column Security*](https://devnet.logianalytics.com/hc/en-us/articles/4405851034007-Restrict-Access-to-Fields-Using-Column-Security).

### Disabling Data Source Configurations

Data source configurations can no longer be disabled. Once they are enabled, they cannot be disabled by anyone.

### Variable Use in Data Source Configurations

You can now insert variables in the custom SQL of a data source configuration and specify defaults for those variables.

## Data Manipulation Changes

The following updates have been made in how data from your data sources can be manipulated and represented in visuals.

* Quarter granularity for date and time fields has been introduced.
* For fast distinct values, when custom ranges or list values are requested for a field, full data scans are no longer performed. See [*Fast Distinct Values*](https://devnet.logianalytics.com/hc/en-us/articles/4405850912279-Fast-Distinct-Values).
* The [COALESCE function](https://devnet.logianalytics.com/hc/en-us/articles/4405851017239-Conditional-Functions) now supports aggregate metrics with complex calculations using arithmetic functions (for example `COALESCE(max(sales) * 1.3, 0)`), so a default value can be used if null values are returned.
* You can now use the `NOW()` function in a derived field definition to obtain the current date and time. However, `NOW()` functionality is not enabled by default.

## Visual Changes

The following updates have been made to visuals in this release.

### Visual Permissions Introduced

This release introduces visual permissions. Visual permissions allow you to permit your entire account, groups within your account, or users within your account to read, write, or delete a visual. With this release, authorization for visuals is now controlled by visual permissions. API updates have been made to support this new functionality.

The creator of a visual is automatically granted read, write, and delete permissions for a visual in the Visual Gallery, but when they are removed from the system, the supervisor is assigned ownership for the visual.

See [*About Visual Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851253271-About-Visual-Permissions).

### Visual Name Uniqueness Enforced

Visual name uniqueness is now enforced with this release.

### New Version of the Custom Chart CLI

A new version 5 of the custom chart CLI has been introduced.

### New List Filter Visual

A new visual style called a list filter has been added to the product. A list filter visual can be used to list values of a data source field in a visual. You can select one or more of the field values in the list to quickly apply a filter to other visuals in the dashboard that subscribe to a cross-visual filter for the field. See [*List Filter Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405859526295-List-Filter-Visuals).

### New Combo Chart Visual

A new combo chart visual has been added. In addition, a new interactive legend is introduced for combo charts; the legend used by other visuals is not supported. See [*Combo Charts*](https://devnet.logianalytics.com/hc/en-us/articles/4405851217047-Combo-Charts).

### Line Visual Changes

New **Display as stacked** and **Stacking Style** options on [Line Trend: Attribute Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859525143-Line-Trend-Attribute-Value-Charts) visuals allow you to create stacked area charts. See [*Line Trend: Attribute Value Charts*](https://devnet.logianalytics.com/hc/en-us/articles/4405859525143-Line-Trend-Attribute-Value-Charts).

### Table Visual Changes

* UI references to "raw data tables" or "raw data table" have been changed to simply "tables" or "table."
* A context menu has been added to table column headings.
* You can now group tables. If a table has been grouped, the options to export its raw or visual data are no longer available. You cannot export raw and visual table data after it has been grouped.
* You can aggregate metrics in a table.
* You can set even time intervals in a table.
* You can alter the granularity of a time field in a table.
* The default settings available for tables in a data source configuration have changed.
* You can now specify the **Rows per Fetch** for an individual table. In past releases, this could be set at the data source level, but not for an individual table.
* Pagination mode is introduced for viewing raw data tables. You can now use a new pagination bar at the bottom of a raw data table to page through and view the fetched data.

See [*Tables*](https://devnet.logianalytics.com/hc/en-us/articles/4405851243799-Tables).

### Visual Interactivity Changes

* With the introduction of dashboard interactivity, visual interactivity is removed from the visual sidebar menu when you edit a visual in a dashboard. Visual interactivity settings are still available for visuals when you edit the visual in the Visual Gallery.
* A new **Preview Interactivity Settings** switch allows you to test the visual interactivity settings when you edit visual interactivity in the Visual Gallery.
* Three new visual interactivity settings have been introduced: **Maximize**, **Rename**, and **Show Time Bar Panel**.

See [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual).

### Visual Caching

Visuals with some dynamic time ranges can now be cached. In past releases, visuals with dynamic time range filters were never cached.

### Arc Gauge Changes

* You can now specify the minimum and maximum values of the metric that determines the color of the arc gauge on the Rulers sidebar.
* The maximum value for the arc gauge can now be determined by a second metric. A new **Static maximum value** switch is added to the Rulers sidebar for arc gauges that you can use to specify whether or not a second metric is used.
* A new **Show Label Description** switch is added to the Rulers sidebar for arc gauge. Use this switch to display a description for the label on the gauge.
* Percentages can now be used for the arc gauge metric range. A new **Show as percentage** switch is added to the Rulers sidebar for arc gauges that you can use to activate this.
* You can now view the raw values for the arc gauge metric and identify the metric used to determine the maximum value.

See [*Arc Gauges*](https://devnet.logianalytics.com/hc/en-us/articles/4405851211287-Arc-Gauges).

### UI Changes

* The option to **Save** a visual with its current name has been removed from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). Instead, the ![](https://devnet.logianalytics.com/hc/article_attachments/4406743710231/dash-save.png) icon appears at the top of visuals that need to be saved. This icon allows you to save the visual with its current name. To save it using a new name, use the new **Save As** option.
* A new **Save As** option on the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) when a visual is edited in a dashboard, a new ![](https://devnet.logianalytics.com/hc/article_attachments/4406747401879/save-as_22x25.png) icon on the visual when edited in the Visual Gallery, and a new Save As Options dialog have been added. Use these to save a visual with a new visual name. The original visual still exists with its original name in the system.

## Dashboard Changes

### Dashboard Permissions

You now can only assign dashboard permissions equivalent to your own. See [*About Dashboard Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859259159-About-Dashboard-Permissions).

### New Dashboard Cross-Visual Filtering

* New dashboard cross-visual filtering controls have been introduced. You can now specify which cross-visual filter each dashboard visual publishes (which link fields it can apply cross-visual filtering for) and which cross-visual filter each visual subscribes to (which cross-visual filters can be applied to the visual). Cross-visual filters are filters created using same-source and cross-source link fields established in the dashboard.
* Custom charts support cross-visual filtering controls if the chart supports the radial menu and filtering and if the appropriate publish and subscribe controls are enabled.
* Cross-visual link publish and subscribe settings for a dashboard can be specified for embedded dashboards using JavaScript. Two JavaScript methods are provided with the `Zoomdata` object: `publish` and `subscribe`.
* The cross-source links dialog has changed. In addition, cross-source links can now be published and subscribed using the new dashboard link controls.
* Cross-visual filters that are applied from same-source and cross-source links are now listed separately on the Filters sidebar from filters that are applied from the Filters sidebar. In addition, you can now view them from a drop-down dialog when you select the filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743754263/filter-vis.png)) on the visual.

See [*Control How Cross-Visual Filters Interact in a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859431447-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard).

### Dashboard Interactivity Settings

This release introduces new dashboard interactivity settings you can use to control how users can interact with a dashboard after it is embedded. Dashboard interactivity settings allow you to control whether users can change the layout, add visuals to the dashboard, delete the dashboard, save the dashboard, filter the dashboard, rename the dashboard, add the dashboard to favorites, set up or change dashboard links, set up or change cross-source links, refresh the dashboard, export the dashboard to PNG or PDF format, or export the dashboard configuration. They also allow you to override the individual visual interactivity settings for the visuals in the dashboard. See [*Control How Users Interact With a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard).

### Saving Dashboards

Dashboard save processing and dashboard copy processing have been improved and now support visual permissions. The Save Options and the Save As Options dialogs have changed to reflect these improvements.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Pre-existing visuals are no longer automatically saved when you save a dashboard (new visuals are automatically saved). You must explicitly elect to save pre-existing visuals on the dashboard Save Options dialog.

See [*Save a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405850986647-Save-a-Dashboard) and [*Copy a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859260183-Copy-a-Dashboard).

### Dashboard Links

Dashboard link information is no longer stored with visual definitions, but with the dashboard definitions. When you upgrade to Composer 6.9, the dashboard link information is automatically upgraded for you.

### Radial Menu Changes

* Use of the radial menu to apply cross-visual filters for cross-source links to other visuals in a dashboard has now been extended to also apply filters for same-source links, based on the publish and subscribe settings for the dashboard and its visuals.
* Null values can now be removed from a visual using the radial menu **Remove** option.

See [*Use the Radial Menu*](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu).

### UI Changes

* The Save and Save As options that were available from a drop-down menu off of the dashboard icon bar have been separated. With this release, two icons on the dashboard icon bar are now provided: one for Save and one for Save As.
* The icon you select to export a dashboard or a visual has changed and the Export As PDF dialog is redesigned. In addition, when you export a dashboard to a PNG file, the PNG file is created and downloaded without an intermediate step.

## Keyset Updates

The following updates have been made for keysets in this release.

* You can now upload and update the values of a keyset from a CSV file. A new **Upload Keyset Values** button on the Keyset tab of the Filters sidebar allows you to select a CSV file containing keyset values and save the value list with a new keyset name.
* The keyset details panel that appears in the filters sidebar is updated visually.
* An administrator can now remove keysets they did not create.

See [*Use Keysets*](https://devnet.logianalytics.com/hc/en-us/articles/4405859392151-Use-Keysets).

## Experimental Materialized View Changes

You can now create materialized view definitions using the Composer UI. In past releases, they could only be created using the API. This is an experimental feature. See [*Use Materialized Views (Experimental)*](https://devnet.logianalytics.com/hc/en-us/articles/4405859403287-Use-Materialized-Views-Experimental-).

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) This is an experimental feature.

## Experimental Alerting Introduced

This release introduces the ability to alert your end users when a metric reaches a specified threshold. See [*Manage Alerts*](https://devnet.logianalytics.com/hc/en-us/articles/4405859133079-Manage-Alerts).

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) This is an experimental feature.

## Performance Updates

The following performance updates have been made in this release:

* Improved server start times by 15 percent.
* A new metadata cache to cache field statistics and improve overall metadata caching performance is introduced.

## Query Engine Changes

The following query engine changes have been made in this release:

* The INFO-level messages logged by the query engine are enhanced to include more information about the request execution.
* A new property for the query engine has been introduced: `qe.max.rows.during.execution`. Use this property in the query engine properties file (`/etc/zoomdata/query-engine.properties`) to limit the number of rows of data that can be processed for a single query.
