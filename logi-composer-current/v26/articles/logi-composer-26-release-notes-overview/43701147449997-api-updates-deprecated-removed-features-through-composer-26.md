---
title: "API Updates, Deprecated, Removed Features Through Composer 26 "
id: 43701147449997
section: "Logi Composer  26 Release Notes Overview"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701147449997-API-Updates-Deprecated-Removed-Features-Through-Composer-26
updated_at: 2026-05-29T14:09:20Z
---

# API Updates, Deprecated, Removed Features Through Composer 26 

# API Updates, Deprecated, Removed Features Through Composer 26

Changes made over time to the Logi Composer API are included here to help you plan upgrades from older releases. Deprecated and removed features are included to allow you to view changes that may affect your environment on upgrade.

**Caution:** Running an older, unsupported operating system in your environment is done so at your own risk. Plan and upgrade to a supported operating system for full support and functionality. For information on operating system and environment support, see [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support).

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

* [API Updates](#API2)

  + [Composer v26](#v2262)
  + [Composer v25](#v252)
  + [Composer v24](#v242)
  + [Composer v23](#v232)
  + [Composer v22](#v222)
  + [Composer v8.4 and Earlier](#v842)
  + [Composer v7.10 and Earlier](#v7102)
  + [Composer v6.9 and Earlier](#v692)
* [Deprecated and Removed Features](#Deprecat)

  + [Composer v26](#v264)
  + [Composer v25](#v254)
  + [Composer v24](#v244)
  + [Composer v23](#v234)
  + [Composer v22](#v224)
  + [Composer v8.4 and Earlier](#v844)
  + [Composer v7.10 and Earlier](#v7104)
  + [Composer v6.9 and Earlier](#v694)

## API Updates

### Composer v26

| Endpoint | Method | Description |
| --- | --- | --- |
| **26.1.2 API Updates** | | |
| None. |  |  |
| **26.1.1 API Updates** | | |
| None. |  |  |
| **26.1 API Updates** | | |
| api/dashboards/ | GET | The GET api/dashboards/ endpoint now returns the creator's full name as **creatorFullName**. |

[Return to top](#top "return to top")

### Composer v25

| Endpoint | Method | Description |
| --- | --- | --- |
| **25.4.4 API Updates** | | |
| None. |  |  |
| **25.4.3 API Updates** | | |
| None. |  |  |
| **25.4.2 API Updates** | | |
| api/sources/odata/s\_{sourceid} | GET | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.4.1 API Updates** | | |
| None. |  |  |
| **25.4 API Updates** | | |
| api/sources/odata/s\_{sourceid} | GET | A new query parameter, **response\_format=compact**, has been added to the existing OData API endpoint: **/api/sources/odata/s\_{sourceid}?response\_format=compact**.  When you include this parameter in your query, the API returns data in a more efficient, compact JSON format. The reduced size of the response payload increases the speed of data transfer. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **25.3.7 API Updates** | | |
| None. |  |  |
| **25.3.6 API Updates** | | |
| None. |  |  |
| **25.3.5 API Updates** | | |
| api/sources/odata/s\_{sourceid} | GET | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.3.4 API Updates** | | |
| None. |  |  |
| **25.3.3 API Updates** | | |
| None. |  |  |
| **25.3.2 API Updates** | | |
| None. |  |  |
| **25.3.1 API Updates** | | |
| None. |  |  |
| **25.3 API Updates** | | |
| api/accounts/{id}  api/accounts  api/accounts/name/{name} | GET, POST, PUT | Use the updated Accounts API to retrieve or define all tenant configuration information, or specific information, such as tenant-level information related to SFTP and SMTP configuration details as needed.  Reserved attributes include:   * sftp.host * sftp.password * sftp.port * sftp.remoteDirectory * sftp.strictHostKeyChecking * sftp.user * email.replyToAddress * email.senderDisplayName |
| api/accounts/{id}  api/accounts | POST, PUT | Users with appropriate permissions to create accounts (tenants) can define a "Reply-To" and "Sender Display Name" for the emails generated to send scheduled dashboard reports. Users with appropriate permissions to update accounts (tenants) can define these attributes for specific accounts (tenants).  Attributes:   * email.replyToAddress * email.senderDisplayName |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **25.2.10 API Updates** | | |
| None. |  |  |
| **25.2.9 API Updates** | | |
| None. |  |  |
| **25.2.8 API Updates** | | |
| api/sources/odata/s\_{sourceid} | GET | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.2.7 API Updates** | | |
| None. |  |  |
| **25.2.6 API Updates** | | |
| None. |  |  |
| **25.2.5 API Updates** | | |
| None. |  |  |
| **25.2.4 API Updates** | | |
| None. |  |  |
| **25.2.3 API Updates** | | |
| None. |  |  |
| **25.2.2 API Updates** | | |
| None. |  |  |
| **25.2.1 API Updates** | | |
| None. |  |  |
| **25.2 API Updates** | | |
| /api/dashboards/{dashboard\_id}/reports/report\_id/  /api/dashboards/{dashboard\_id}/reports | PUT, POST | You can now add a `destinationType` of `EMAIL` or `FILE_DROP` to support SFTP and SMTP dispatch of scheduled dashboard reports. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **25.1.11 API Updates** | | |
| api/sources/odata/s\_{sourceid} | GET | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.1.10 API Updates** | | |
| None. |  |  |
| **25.1.9 API Updates** | | |
| None. |  |  |
| **25.1.8 API Updates** | | |
| None. |  |  |
| **25.1.7 API Updates** | | |
| None. |  |  |
| **25.1.6 API Updates** | | |
| None. |  |  |
| **25.1.5 API Updates** | | |
| None. |  |  |
| **25.1.4 API Updates** | | |
| None. |  |  |
| **25.1.3 API Updates** | | |
| None. |  |  |
| **25.1.2 API Updates** | | |
| None. |  |  |
| **25.1.1 API Updates** | | |
| None. |  |  |
| **25.1 API Updates** | | |
| None. |  |  |

[Return to top](#top "return to top")

### Composer v24

| Endpoint | Method | Description |
| --- | --- | --- |
| **24.4.15 API Updates** | | |
| None. |  |  |
| **24.4.14 API Updates** | | |
| None. |  |  |
| **24.4.13 API Updates** | | |
| None. |  |  |
| **24.4.12 API Updates** | | |
| None. |  |  |
| **24.4.11 API Updates** | | |
| None. |  |  |
| **24.4.10 API Updates** | | |
| None. |  |  |
| **24.4.9 API Updates** | | |
| None. |  |  |
| **24.4.8 API Updates** | | |
| None. |  |  |
| **24.4.7 API Updates** | | |
| None. |  |  |
| **24.4.6 API Updates** | | |
| None. |  |  |
| **24.4.5 API Updates** | | |
| None. |  |  |
| **24.4.4 API Updates** | | |
| None. |  |  |
| **24.4.3 API Updates** | | |
| None. |  |  |
| **24.4.2 API Updates** | | |
| None. |  |  |
| **24.4.1 API Updates** | | |
| None. |  |  |
| **24.4 API Updates** | | |
| /api/sources/{source\_id}/cache?cacheType=ENTITY\_DATA | DELETE | This endpoint has been expanded to allow you to clear the ENTITY\_DATA cache in addition to the DATA and STATISTICS cache. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **24.3.10 API Updates** | | |
| None. |  |  |
| **24.2.9 API Updates** | | |
| None. |  |  |
| **24.3.8 API Updates** | | |
| None. |  |  |
| **24.3.7 API Updates** | | |
| None. |  |  |
| **24.3.6 API Updates** | | |
| None. |  |  |
| **24.3.5 API Updates** | | |
| None. |  |  |
| **24.3.4 API Updates** | | |
| None. |  |  |
| **24.3.3 API Updates** | | |
| None. |  |  |
| **24.3.2 API Updates** | | |
| None. |  |  |
| **24.3.1 API Updates** | | |
| None. |  |  |
| **24.3 API Updates** | | |
| None. |  |  |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **24.2.12 API Updates** | | |
| None. |  |  |
| **24.2.11 API Updates** | | |
| None. |  |  |
| **24.2.10 API Updates** | | |
| None. |  |  |
| **24.2.9 API Updates** | | |
| None. |  |  |
| **24.2.8 API Updates** | | |
| None. |  |  |
| **24.2.7 API Updates** | | |
| None. |  |  |
| **24.2.6 API Updates** | | |
| None. |  |  |
| **24.2.5 API Updates** | | |
| None. |  |  |
| **24.2.4 API Updates** | | |
| None. |  |  |
| **24.2.3 API Updates** | | |
| None. |  |  |
| **24.2.2 API Updates** | | |
| None. |  |  |
| **24.2.1 API Updates** | | |
| None. |  |  |
| **24.2 API Updates** | | |
| /api/group-membership/{id} | PATCH | Manage group membership for users by updating a group: define `usersToAdd` and `usersToRemove` to include a single user or an array of users. |
| /api/inventory/{type}/  and  /api/inventory/{type}/{id} | GET | If you created dashboards and visuals that include your own `originID`, calling this endpoint returns each item and their associated `originID`, if applicable. |
| /api/sources | GET/PUT | Use to return and define information for a source. |
| /api/sources/{sourceId}/clone | POST | Use to create a copy of a source. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **24.1.12 API Updates** | | |
| None. |  |  |
| **24.1.11 API Updates** | | |
| None. |  |  |
| **24.1.10 API Updates** | | |
| None. |  |  |
| **24.1.9 API Updates** | | |
| None. |  |  |
| **24.1.8 API Updates** | | |
| None. |  |  |
| **24.1.7 API Updates** | | |
| None. |  |  |
| **24.1.6 API Updates** | | |
| None. |  |  |
| **24.1.5 API Updates** | | |
| None. |  |  |
| **24.1.4 API Updates** | | |
| None. |  |  |
| **24.1.3 API Updates** | | |
| None. |  |  |
| **24.1.2 API Updates** | | |
| None. |  |  |
| **24.1.1 API Updates** | | |
| /api/groups | POST, PUT | You can now assign an identifier to your groups using `externalId` that is unique across tenants. This does not change or replace the `accountId` assigned by Composer. The `externalId` is not available in the UI. |
| **24.1 API Updates** | | |
| /api/sources/export | GET | These attributes are returned for sources in your environment. Include these attributes to work with import matching strategies.   * `connections[].originId` - Returns the value of the connection ID from the imported connection. * `sources[].originId` - Returns the value of the source ID from the imported source |
| /api/sources/import | POST | When you import objects into your environment, you can define a matching strategy that uses multiple approaches to reviewing objects to determine how to handle them in conjunction with your selected insertion strategy.  Matching strategies are processed in order, proceeding to the next and the next if a strategy fails.  If all strategies fail, the object is imported and tagged with your selected tags to help you find affected objects and manage any issues.  These attributes are used to define the matching strategy and warning tags to use for import. Send as an array; each strategy is considered in order.   * `importSettings.objectClassLevel.connections.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for connections. This array can include:    + `BY_ORIGIN_ID`   + `BY_ID_AND_TYPE_AND_PARAMS`   + `BY_TYPE_AND_PARAMETERS`   + `BY_NAME_AND_TYPE`   + `BY_TYPE_AND_PARAM_KEYS`   + `BY_NAME`  If an order is not specified, the default strategy of `BY_ID_AND_TYPE_AND_PARAMS` or `BY_TYPE_AND_PARAMETERS` is used. * `importSettings.objectClassLevel.sources.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for sources. This array can include:    + `BY_ORIGIN_ID`   + `BY_NAME`  If an order is not specified, the default strategy of `BY_NAME` is used. * `importSettings.warningTags[]` - Send an array of warning tags to apply to objects imported with warnings.   Send `enableDefaultRead` to enable data read permissions for the sources imported for all users in the tenant. |
| /api/dashboards/export/ | GET | These attributes are returned for dashboards in your environment. Include these attributes for importing.   * `connections[].originId` - Returns the value of the associated connection ID. * `sources[].originId` - Returns the value of the associated source ID. * `visuals[].originId` - Returns the value of the associated visual ID. * `dashboards[].originId` - Returns the value of the associated dashboard ID. |
| /api/dashboards/import/ | POST | When you import objects into your environment, you can define a matching strategy that uses multiple approaches to reviewing objects to determine how to handle them in conjunction with your selected insertion strategy.  Matching strategies are processed in order, proceeding to the next and the next if a strategy fails.  If all strategies fail, the object is imported and tagged with your selected tags to help you find affected objects and manage any issues.  These attributes are used to define the matching strategy and warning tags to use for import. Send as an array; each strategy is considered in order.   * `importSettings.objectClassLevel.connections.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for connections. This array can include:    + `BY_ORIGIN_ID`   + `BY_ID_AND_TYPE_AND_PARAMS`   + `BY_TYPE_AND_PARAMETERS`   + `BY_NAME_AND_TYPE`   + `BY_TYPE_AND_PARAM_KEYS`   + `BY_NAME`  If an order is not specified, the default strategy of `BY_ID_AND_TYPE_AND_PARAMS` or `BY_TYPE_AND_PARAMETERS` is used. * `importSettings.objectClassLevel.visuals.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for visuals. This array can include:    + `BY_ORIGIN_ID`   + `BY_NAME`  If an order is not specified, the default strategy of `BY_NAME` is used. * `importSettings.objectClassLevel.sources.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for sources. This array can include:    + `BY_ORIGIN_ID`   + `BY_NAME`  If an order is not specified, the default strategy of `BY_NAME` is used. * `importSettings.objectClassLevel.dashboards.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for dashboards. This array can include:    + `BY_ORIGIN_ID`   + `BY_NAME`  If an order is not specified, the default strategy of `BY_NAME` is used. * `importSettings.warningTags[]` - Send an array of warning tags to apply to objects imported with warnings.   Send `enableDefaultRead` to enable data read permissions for the sources imported for all users in the tenant. |
| /api/visuals/export/ | GET | These attributes are returned for visuals in your environment. Include these attributes for importing.   * `connections[].originId` - Returns the value of the associated connection ID. * `sources[].originId` - Returns the value of the associated source ID. * `visuals[].originId` - Returns the value of the associated visual ID. |
| /api/visuals/import/ | POST | When you import objects into your environment, you can define a matching strategy that uses multiple approaches to reviewing objects to determine how to handle them in conjunction with your selected insertion strategy.  Matching strategies are processed in order, proceeding to the next and the next if a strategy fails.  If all strategies fail, the object is imported and tagged with your selected tags to help you find affected objects and manage any issues.  These attributes are used to define the matching strategy and warning tags to use for import. Send as an array; each strategy is considered in order.   * `importSettings.objectClassLevel.connections.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for connections. This array can include:    + `BY_ORIGIN_ID`   + `BY_ID_AND_TYPE_AND_PARAMS`   + `BY_TYPE_AND_PARAMETERS`   + `BY_NAME_AND_TYPE`   + `BY_TYPE_AND_PARAM_KEYS`   + `BY_NAME`  If an order is not specified, the default strategy of `BY_ID_AND_TYPE_AND_PARAMS` or `BY_TYPE_AND_PARAMETERS` is used. * `importSettings.objectClassLevel.visuals.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for visuals. This array can include:    + `BY_ORIGIN_ID`   + `BY_NAME`  If an order is not specified, the default strategy of `BY_NAME` is used. * `importSettings.objectClassLevel.sources.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for sources. This array can include:    + `BY_ORIGIN_ID`   + `BY_NAME`  If an order is not specified, the default strategy of `BY_NAME` is used. * `importSettings.warningTags[]` - Send an array of warning tags to apply to objects imported with warnings.   Send `enableDefaultRead` to enable data read permissions for the sources imported for all users in the tenant. |
| /api/accounts/name/{name} | GET | This takes the `{name}` of the tenant account as a path parameter and returns tenant account details. Works similarly to `/api/accounts/{id}/`. |

[Return to top](#top "return to top")

### Composer v23

| Endpoint | Method | Description |
| --- | --- | --- |
| **23.4.13 API Updates** | | |
| None. |  |  |
| **23.4.12 API Updates** | | |
| None. |  |  |
| **23.4.11 API Updates** | | |
| None. |  |  |
| **23.4.10 API Updates** | | |
| None. |  |  |
| **23.4.9 API Updates** | | |
| None. |  |  |
| **23.4.8 API Updates** | | |
| None. |  |  |
| **23.4.7 API Updates** | | |
| None. |  |  |
| **23.4.6 API Updates** | | |
| None. |  |  |
| **23.4.5 API Updates** | | |
| None. |  |  |
| **23.4.4 API Updates** | | |
| None. |  |  |
| **23.4.3 API Updates** | | |
| None. |  |  |
| **23.4.2 API Updates** | | |
| None. |  |  |
| **23.4.1 API Updates** | | |
| /api/sources/ | POST | When using the `sources` endpoint, Composer returns the parameter fields of the collection you request, both for `/preview` and `/describe`. |
| **23.4 API Updates** | | |
| /api/recently-accessed-elements | GET | Use to return items recently used, such as dashboards, visuals, and data sources by the logged in user in Composer. Limit the number of items returned by sending `/api/recently-accessed-elements?listSize={number}.` |
| /api/accounts/{id} | PUT | Use `/api/accounts/{id}` to update existing user accounts, or create new ones. |
| /api/sources/{sourceId}/clone | PUT | Use to clone an existing source in your environment with a new `name`. Mandatory fields include `sourceID` and `name`. Optionally add `tags` and `description`. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **23.3.14 API Updates** | | |
| None. |  |  |
| **23.3.13 API Updates** | | |
| None. |  |  |
| **23.3.12 API Updates** | | |
| None. |  |  |
| **23.3.11 API Updates** | | |
| None. |  |  |
| **23.3.10 API Updates** | | |
| None. |  |  |
| **23.3.9 API Updates** | | |
| None. |  |  |
| **23.3.8 API Updates** | | |
| None. |  |  |
| **23.3.7 API Updates** | | |
| None. |  |  |
| **23.3.6 API Updates** | | |
| None. |  |  |
| **23.3.5 API Updates** | | |
| None. |  |  |
| **23.3.4 API Updates** | | |
| None. |  |  |
| **23.3.3 API Updates** | | |
| None. |  |  |
| **23.3.2 API Updates** | | |
| None. |  |  |
| **23.3.1 API Updates** | | |
| None. |  |  |
| **23.3 API Updates** | | |
| /api/connection/{id}  /api/sources/{id}  /api/sources/ {sourceId}/fields/{fieldId}  /api/visuals/{id}  /api/dashboard/{id} | DELETE | When you attempt to delete an object that has dependent object, Composer returns a robust response that includes the item’s `id`, `name`, and `type` to make decoupling of dependent objects easier. |
| /api/connection/types/{id}/accounts | PUT, GET | Use to allow access to specific connection types to users of appropriate permissions in specific Accounts.  If no Accounts are specified for a connection type, all uses with appropriate permissions in all accounts can create new or edit existing connection types. |
| /api/sources | POST | If a request through the API returns a 400 response code, you now see two levels of validation issues, ERROR and WARNING. Optionally, include the query parameter `suppressWarnings` to determine the behavior of the request.   * Send `suppressWarnings=true` to make the request ignore all warning violations and return success if there are no error violations. * Send `suppressWarnings=false` to make the request fail if there is at least one error or warning. * The default value is `false`. |
| /api/sources/${sourceId} | PUT |
| /api/sources/${sourceId}/fields | POST, PUT |
| /api/sources/${sourceId}/fields/${fieldName} | PUT, DELETE |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **23.2.15 API Updates** | | |
| None. |  |  |
| **23.2.14 API Updates** | | |
| None. |  |  |
| **23.2.13 API Updates** | | |
| None. |  |  |
| **23.2.12 API Updates** | | |
| None. |  |  |
| **23.2.11 API Updates** | | |
| None. |  |  |
| **23.2.10 API Updates** | | |
| None. |  |  |
| **23.2.9 API Updates** | | |
| None. |  |  |
| **23.2.8 API Updates** | | |
| None. |  |  |
| **23.2.7 API Updates** | | |
| None. |  |  |
| **23.2.6 API Updates** | | |
| Various |  | We’ve added clarification to our provided Swagger API documentation to specify the security level required to perform each available operation. |
| **23.2.5 API Updates** | | |
| None. |  |  |
| **23.2.4 API Updates** | | |
| None. |  |  |
| **23.2.3 API Updates** | | |
| None. |  |  |
| **23.2.2 API Updates** | | |
| None. |  |  |
| **23.2.1 API Updates** | | |
| None. |  |  |
| **23.2 API Updates** | | |
| /api/sources/export  /api/sources/import | GET, PUT | Use these new endpoints with parameter `ids` to specify one or more source for export and import:   * /api/sources/export?ids=sourceId1,sourceId2,sourceId3  or * /api/sources/export?ids=sourceId1&ids=sourceId2&ids=sourceId3   Source payload includes:   * source object * fields * custom metrics * global settings * cache settings * related connections |
| /api/dashboards/{id}/comments  /api/dashboards/{id}/comments/{id} | GET, POST, PUT, DELETE | Use the comments API to manage comments associated with a dashboard and its widgets:   * GET /api/dashboards/{id}/comments * GET /api/dashboards/{id}/comments/{id} * POST /api/dashboards/{id}/comments/ * PUT /api/dashboards/{id}/comments/{id} * DELETE /api/dashboards/{id}/comments/{id} |
| /api/sources/{source\_id}/unique-key | GET, PUT | Use to define and retrieve a unique key for non-hierarchical fields in data sources. The key can be a field or an array. |
| /api/start-vis | POST | Use to execute `START_VIS` query via REST and get a resulting data set in the response.  **Important:**  This is an experimental API. |
| /api/dashboards/convert-layout/ | POST | Use to convert dashboards to responsive layout. On success, returns an array of dashboard ids converted. See Dashboard Layouts.  **Important:**  This is an experimental API. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **23.1.14 API Updates** | | |
| None. |  |  |
| **23.1.13 API Updates** | | |
| None. |  |  |
| **23.1.12 API Updates** | | |
| None. |  |  |
| **23.1.11 API Updates** | | |
| None. |  |  |
| **23.1.10 API Updates** | | |
| None. |  |  |
| **23.1.9 API Updates** | | |
| None. |  |  |
| **23.1.8 API Updates** | | |
| None. |  |  |
| **23.1.7 API Updates** | | |
| None. |  |  |
| **23.1.6 API Updates** | | |
| None. |  |  |
| **23.1.5 API Updates** | | |
| None. |  |  |
| **23.1.4 API Updates** | | |
| None. |  |  |
| **23.1.3 API Updates** | | |
| None. |  |  |
| **23.1.2 API Updates** | | |
| None. |  |  |
| **23.1.1 API Updates** | | |
| None. |  |  |
| **Composer 23.1 API Updates** | | |
| /api/dashboards/{dashboard\_id}/reports | PATCH | Use to share, revoke, or change user access to a dashboard and its visuals. as a `VIEWER` or `EDITOR`. |
| /api/dashboards/{dashboard\_id}/reports | POST | Use the new field, `{"email": "user@example.com"}`, to schedule dashboard reports for non-Composer users.  Removed the deprecated field `sendOnlyToMe`. |
| /api/dashboards/{dashboard\_id}/reports/{report\_id} | GET |
| /api/dashboards/{dashboard\_id}/reports  /api/dashboards/{dashboard\_id}/reports/{id} | PUT |
| /api/export/rawdataforvisual | POST | Use to generate raw data export CSV and XLSX of your raw data for visuals. Replaces `/api/export/raw`. |
| /api/export/visualdata | POST | Use to generate visual data export CSV and XLSX of your raw data for visuals. Replaces `/api/export/chartdata/{file_name}`. |
| /api/sources/{id}/dictionaries | PUT | Create and update your metadata dictionary for a source. Use MediaType `/multipart/form-data`.  Example:  `Field Label,ua_UK,en_GB`  `city,місто,city`  `county,округ,county`  `zip code,поштовий індекс,postcode` |
| /api/sources/{id}/dictionaries | GET | Returns a list of dictionaries with field labels for a source. |
| /api/sources/{id}/dictionaries/{language} | GET | Returns a dictionary by the specified language for a source. |
| /api/sources/{id}/dictionaries/{language} | PUT | Create and update a dictionary for the specified language for a source. |
| /api/sources/{id}/dictionaries | DELETE | Delete all dictionaries for a specified source. |
| /api/sources/{id}/dictionaries/{language} | DELETE | Delete the dictionary for the specified language for a source. |

[Return to top](#top "return to top")

### Composer v22

| Endpoint | Method | Description |
| --- | --- | --- |
| **22.4.14 API Updates** | | |
| None. |  |  |
| **22.4.13 API Updates** | | |
| None. |  |  |
| **22.4.12 API Updates** | | |
| None. |  |  |
| **22.4.11 API Updates** | | |
| None. |  |  |
| **22.4.10 API Updates** | | |
| None. |  |  |
| **22.4.9 API Updates** | | |
| None. |  |  |
| **22.4.8 API Updates** | | |
| None. |  |  |
| **22.4.7 API Updates** | | |
| None. |  |  |
| **22.4.6 API Updates** | | |
| None. |  |  |
| **22.4.5 API Updates** | | |
| None. |  |  |
| **22.4.4 API Updates** | | |
| None. |  |  |
| **22.4.3 API Updates** | | |
| None. |  |  |
| **22.4.2 API Updates** | | |
| None. |  |  |
| **22.4.1 API Updates** | | |
| None. |  |  |
| **22.4 API Updates** | | |
| /api/sources/{sourceId}/fields/ | POST, PUT | Use `lookup` to set a dynamic field statistics overwrite. Specify `dataEntityId` and `originalFieldName` as a custom source of filter values. |
| /api/sources/{sourceId}/fields/{fieldName} | POST, PUT | Use `lookup` to set a dynamic field statistics overwrite. Specify `dataEntityId` and `originalFieldName` as a custom source of filter values. |
| /api/alerts/{id} | GET | Returns a specific alert definition, identified by its ID. In a multi tenancy environment, respects Recipients rules. |
| /api/inventory/{type}/{id}  /api/inventory  /api/user/permissions/dashboards/{id} | GET | A new field, `accessLevel`, has been added to these endpoints to return users' access to a dashboard. These access levels can be `OWNER`, `EDITOR`, or `VIEWER`. |

[Return to top](#top "return to top")

### Composer v8.4 and Earlier

| Endpoint | Method | Description |
| --- | --- | --- |
| **8.4.1 API Updates** | | |
| None. |  |  |
| **8.4 API Updates** | | |
| None. |  |  |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **8.3 API Updates** | | |
| None. |  |  |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **8.2 API Updates** | | |
| /api/sources/ |  | Actions taken using these endpoints trigger a source `modifiedDate` update:   * `POST /api/sources/{sourceId}` * `POST /api/sources/{sourceId}/fields` * `PUT, DELETE /api/sources/{sourceId}/fields/{fieldName}` * `POST /api/sources/{sourceId}/custom-metrics` * `PUT, DELETE /api/sources/{sourceId}/custom-metrics/{customMetricName}` * `PUT /api/sources/{sourceId}/global-settings` * `PUT /api/sources/{sourceId}/cache-settings` |
| /api/connections/{id} | POST | When you create a connection, use the `?connectionTypeMatching=BY_TYPE_AND_PARAMETERS` URL parameter to omit the matching by `connectionTypeId`; instead, use matching by combining `type` + `subStorageType` + `Connection Parameter Keys`. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **8.1 API Updates** | | |
| /api/sources/ | PUT, GET, DELETE | Use the Composer API to remove a field or change a field type for a field in your source if it is not in use by a global filter.   * PUT `/api/sources/{sourceId}` * PUT `/api/sources/{sourceId}/fields/{fieldName}` * DELETE `/api/sources/{sourceId}/fields/{fieldName}` * GET `/api/sources/{sourceId}/fields/{fieldName}/usage` |
| /api/user/interpolate | POST | Use `/api/user/interpolate` to send custom attribute names and get custom attribute values. |
| /api/favorites/ | POST | Favorite a visual. Specify an `inventoryItemId` and visual in `inventoryItemType`. |
| /api/favorites/{favoriteID} | DELETE | Remove the favorite indication from the specified `{favoriteID}`. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **8.0 API Updates** | | |
| api/inventory?type=VISUAL | GET | Returns information about visuals for which the user has `READ` permission. If the user has no `READ` access to any visuals, an empty list is returned. |

[Return to top](#top "return to top")

### Composer v7.10 and Earlier

| Endpoint | Method | Description |
| --- | --- | --- |
| **7.10.23 API Updates** | | |
| None. |  |  |
| **7.10.22 API Updates** | | |
| None. |  |  |
| **7.10.21 API Updates** | | |
| None. |  |  |
| **7.10.20 API Updates** | | |
| None. |  |  |
| **7.10.19 API Updates** | | |
| None. |  |  |
| **7.10.18 API Updates** | | |
| None. |  |  |
| **7.10.17 API Updates** | | |
| None. |  |  |
| **7.10.16 API Updates** | | |
| None. |  |  |
| **7.10.15 API Updates** | | |
| None. |  |  |
| **7.10.14 API Updates** | | |
| None. |  |  |
| **7.10.13 API Updates** | | |
| None. |  |  |
| **7.10.12 API Updates** | | |
| None. |  |  |
| **7.10.11 API Updates** | | |
| None. |  |  |
| **7.10.10 API Updates** | | |
| None. |  |  |
| **7.10.9 API Updates** | | |
| None. |  |  |
| **7.10.8 API Updates** | | |
| None. |  |  |
| **7.10.7 API Updates** | | |
| None. |  |  |
| **7.10.6 API Updates** | | |
| None. |  |  |
| **7.10.5 API Updates** | | |
| None. |  |  |
| **7.10.4 API Updates** | | |
| None. |  |  |
| **7.10.3 API Updates** | | |
| None. |  |  |
| **7.10.2 API Updates** | | |
| None. |  |  |
| **7.10.1 API Updates** | | |
| None. |  |  |
| **7.10 API Updates** | | |
| /api/visuals | GET | The `tags` experimental request parameter was removed from the `GET /api/visuals` endpoint. |
| /api/sources/ | POST | Use to create a source and control the list of native fields added to the source definition by specifying the list of native fields in the request body. When you create a source using this endpoint, the custom metric Volume is created by default, and Global settings and Cache settings are populated with default values. |
| /api/sources/ | GET | Use to return a list of all sources, paginated. |
| /api/sources/{sourceId} | PUT | Use to update a source. |
| /api/sources/{sourceId} | GET | Use to return a specified source with the list of native fields. |
| /api/sources/{sourceId} | DELETE | Use to delete a specified source. |
| /api/sources/{sourceId}/features | GET | Use to return the features available for the specified source. |
| /api/sources/{sourceID}/global-settings | GET | Use to return global settings for the specified source. Requires `read` or `data_access` permissions for the source. |
| /api/sources/{sourceID}/global-settings | PUT | Use to update global settings for the specified source. Requires `write` permissions for the source. |
| /api/uploads/preview | POST | Use to view a preview of sample file data. |
| /api/uploads/{id}/data/ | DELETE | Use to delete all data stored in a file upload. |
| /api/uploads/{id}/data/ | POST | Use to add data to the file upload. The file structure sent must match the existing validated format and structure. |
| /api/uploads/{id}/data/ | PUT | Use to replace data in the file upload. The file structure sent must match the existing validated format and structure. |
| /api/sources/SOURCE\_ID/meta/visuals | GET | `/api/sources/SOURCE_ID/meta/visuals` has been renamed `/api/sources/{source_id}/visual-types`. The functionality of this endpoint is unchanged. |
| /api/sources/SOURCE\_ID/meta/visuals/{VISUALIZATION\_ID} | GET | `/api/sources/SOURCE_ID/meta/visuals/{VISUALIZATION_ID}` has been renamed `/api/sources/{source_id}/visual-types/{VISUALIZATION_ID_/initial-visual`. The functionality of this endpoint is unchanged. |
| /api/sources/SOURCE\_ID/meta/variables | GET | `/api/sources/SOURCE_ID/meta/variables` has been renamed `/api/sources/{source_id}/visual-types/variables-values`. The functionality of this endpoint is unchanged. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **7.9 API Updates** | | |
| /api/sources/  /api/export/  /api/stream/ |  | Composer now supports permissions to allow source data access. Existing users with READ permission on a source are given DATA ACCESS permission for that source on upgrade to v7.9.  Endpoints that support DATA ACCESS:   * `GET /api/sources/SOURCE_ID/visual-types/VISUAL_TYPE_ID/initial-visual` * `GET /api/sources/SOURCE_ID/visual-types/variables-values` * `GET /api/sources/{sourceId}/features` * `GET /api/sources/SOURCE_ID/fields/FIELD_NAME/statistics/total` * `GET /api/sources/SOURCE_ID/fields/FIELD_NAME/statistics/distinct-values` * `POST /api/export/chartdata/{file_name}` * `POST /api/export/csv/raw` * `POST /api/stream/search` * `GET /api/stream/search/{sourceId}/facet/{attribute}`   Endpoints that support DATA ACCESS or READ permissions:   * `GET /api/sources/SOURCE_ID/visual-types` |
| /api/visualizations/libs |  | Visualization library endpoints used by the CLI and deprecated in Composer v6.9 have been removed. These include:   * `GET /api/visualizations/libs` * `POST /api/visualizations/libs` * `DELETE /api​/visualizations​/libs​/{id}` * `GET /api​/visualizations​/libs​/{id}/*` |
| /user/source-acl/ |  | `/user/source-acl` is now removed from Composer. It was deprecated in a previous release. |
| /user/source-acl/{sourceID} |  | `/user/source-acl/{sourceID}` is now removed from Composer. It was deprecated in a previous release. |
| /api/inventory/ |  | The endpoint `/api/inventory/` has been expanded to return additional information about dashboards and sources.  Send a parameter `type` with your query to return related data.   * DASHBOARD - Returns a list of dashboard inventory items and `associatedItems` for each dashboard. * SOURCE - Returns a list `AssociatedItemResource` information. * If no `type` is sent, all dashboard items are returned. This feature will be removed in a future release. |
| /api/users/ | GET | The API response for GET `/api/users/` using `application/vnd.composer.v3+json` media type has been changed. |
| /api/sources/${sourceId}/fields/${fieldname} | DELETE | Validation updates prevent you from removing a field from a source if the field is used by filters, cross-source links, join configurations, or actions. |
| /api/sources/${sourceId} | PUT | Validation updates prevent you from removing a field from a source if the field is used by filters, cross-source links, join configurations, or actions. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **7.8 API Updates** | | |
| /api/sources/<source-id>/expression-syntax/ | GET | Row label expressions called using `/api/sources/<source-id>/expression-syntax/` now return full text labels for each operator. This includes:   * Subtract * Less than or equal to * Greater than * Multiply * Not equal to * Greater than or equal to * Less than * Add * Divide * Equal to |
| /api/users/ | GET | Call `/api/users/` to return the user `name` and user `id` for all users. Use `application/vnd.composer.v3.lightweight+json` Media Type. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **7.7 API Updates** | | |
| /api/dashboards/{id}/key | GET | This API was deprecated in release v6.9 and has now been removed from the platform along with other previously removed Security Keys endpoints.  Use Trusted Access instead for all embedded workflows. See Trusted Access. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **7.6 API Updates** | | |
| ROLE\_MANAGE\_VISUALIZATION\_TEMPLATES |  | The group privilege `ROLE_MANAGE_VISUALIZATION_TEMPLATES` is now `ROLE_ADMINISTER_VISUAL_TYPES`. |
| /api/actions | GET | Previously, `GET /api/actions` required `(MANAGE_ACTIONS and READ for the source)` privilege/permissions.  Now, with Composer 7.6, `GET /api/actions` requires `((MANAGE_ACTIONS or INVOKE_ACTIONS) and READ for the source)`. |
| /api/visual-types/components/ |  | New `/visual-types/components/` endpoints are now available. |
| /api/visual-types/ |  | `visualizationId` has been renamed in `/visual-types/` to `visualTypeId`. |
| /api/dashboards/{id}/key | GET | This API was deprecated in release v6.9 and cannot be used with the API privilege `ROLE_SHARE_DASHBOARDS`, which has been removed. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **7.5 API Updates** | | |
| /api/trusted-access/pull/tokens | POST | Use to generate a trusted access token for a user, specifying the Composer user name. The user must already exist, and have an active Composer user account (unless you are using LDAP with automatic provisioning for Composer). |
| /api/trusted-access/push/tokens | POST | Use to generate a trusted access token based on user context, optionally group membership, and user attributes, for existing Composer accounts.  If the user exists in Composer, the user is updated.  If the user does not exist in Composer, this creates the user. |
| /api/trusted-access/token |  | Deprecated.  Use `/api/trusted-access/pull/tokens`. This is primarily a name change for the endpoint; payloads and functionality remain unchanged. |
| /api/sources/{id} | PUT/POST | You can no longer manually set the "version": `{integer}` of a source object when using `PUT api/sources/{id}` OR `POST api/sources`. Version is a system controlled variable which cannot be set manually. |
| /api/user/switch/{accountId} |  | Deprecated.  You can no longer authorize this API by a Trusted Access user token for switching Composer accounts. You can still generate a new Trusted Access user token by including the target Composer account information in the request. |
| Removed deprecated security keys-related /api/sources endpoints:  GET /api/sources/{id}/key  GET​ /api​/sources​/key  DELETE ​/api​/sources​/remove​/{id} |  | These APIs were deprecated in release v6.9 and have now been removed from the platform. Use Trusted Access instead for all embedded workflows.See Trusted Access. For more information about embedding Composer components, see Embed Composer Components Using JavaScript and Trusted Access. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **7.4 API Updates** | | |
| /api/sources/{id} | PUT | Use to upload sources using the object's ID while retaining the object ID when migrating from one environment to another.  Use to update sources using the object’s ID while retaining the object ID when migrating from one environment to another.  You must have the `CanCreate{Object}` privilege. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **7.3 API Updates** | | |
| /api/connections/{id} | PUT | Create a connection using a predefined object ID. |
| /api/sources/{id} | PUT | New endpoint.  Use to upload sources using the object's ID while retaining the object ID migrating from one environment to another.  You must have the `CanCreate{Object}` privilege. |
| /api/visuals/{id} | PUT | Use to create a visual using a predefined object ID.  You must have the `CanCreate{Object}` privilege. |
| /api/dashboards/{id} | PUT | Use to create a dashboard using a predefined object ID.  You must have the `CanCreate{Object}` privilege. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **7.2 API Updates** | | |
| None. |  |  |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **7.1 API Updates** | | |
| /api/export/generate/rawdata | POST | This endpoint has been removed. Use `/api/export/csv/raw` instead. |
| /api/dashboards/\* | all | The API v1 (`application/vnd.composer.dashboard.v1+json`) behavior of the `/api/dashboards/*` endpoint has been removed. Use the new version of the endpoint in the v2 version of the API (`application/vnd.composer.dashboard.v2+json`) or `application/vnd.composer.v2` instead. Errors will result if you attempt to use `application/vnd.composer.dashboard.v1+json`.  **Note:** When no `content-type` header is specified, Composer defaults to using `application/vnd.composer.dashboard.v2+json`. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **7.0 API Updates** | | |
| /api/materialized-views | GET | A new, optional parameter, `sourceId={<data-source-id>}`, has been added in this release. Use this parameter to obtain a list of materialized views for a specific data source. |
| /api/dashboards/import | POST | A new query parameter, `strategy`, has been added for this endpoint. Valid values can be `OVERWRITE` or `USE_EXISTING_OR_CREATE`.   * Specify `OVERWRITE` to implement the new overwrite import policy. * Specify `USE_EXISTING_OR_CREATE` to continue to use the existing import policy (importing the dashboard with a slightly altered name). This is the default value and will be used if `strategy` is not specified. |

[Return to top](#top "return to top")

### Composer v6.9 and Earlier

| Endpoint | Method | Description |
| --- | --- | --- |
| **6.9.29 API Updates** | | |
| None. |  |  |
| **6.9.28 API Updates** | | |
| None. |  |  |
| **6.9.27 API Updates** | | |
| None. |  |  |
| **6.9.26 API Updates** | | |
| None. |  |  |
| **6.9.25 API Updates** | | |
| None. |  |  |
| **6.9.24 API Updates** | | |
| None. |  |  |
| **6.9.23 API Updates** | | |
| None. |  |  |
| **6.9.22 API Updates** | | |
| None. |  |  |
| **6.9.21 API Updates** | | |
| None. |  |  |
| **6.9.20 API Updates** | | |
| None. |  |  |
| **6.9.19 API Updates** | | |
| None. |  |  |
| **6.9.18 API Updates** | | |
| None. |  |  |
| **6.9.17 API Updates** | | |
| None. |  |  |
| **6.9.16 API Updates** | | |
| None. |  |  |
| **6.9.15 API Updates** | | |
| None. |  |  |
| **6.9.14 API Updates** | | |
| None. |  |  |
| **6.9.13 API Updates** | | |
| None. |  |  |
| **6.9.12 API Updates** | | |
| /api/sources/{id} | POST/PUT | You can no longer manually set the "version": {integer} of a source object when using PUT api/sources/{id} OR POST api/sources. Version is a system controlled variable which cannot be set manually. |
| **6.9.11 API Updates** | | |
| None. |  |  |
| **6.9.10 API Updates** | | |
| None. |  |  |
| **6.9.9 API Updates** | | |
| /api/connections/{id} | PUT | Create a connection using a predefined object ID. |
| /api/sources/{id} | PUT | New endpoint.  Use to upload sources using the object's ID while retaining the object ID when migrating from one environment to another.  You must have the `CanCreate{Object}` privilege. |
| /api/visuals/{id} | PUT | Use to create a visual using a predefined object ID.  You must have the `CanCreate{Object}` privilege. |
| /api/dashboards/{id} | PUT | Use to create a dashboard using a predefined object ID.  You must have the `CanCreate{Object}` privilege. |
| **6.9.8 API Updates** | | |
| None. | | |
| **6.9.7 API Updates** | | |
| None. | | |
| **6.9.6 API Updates** | | |
| None. | | |
| **6.9.5 API Updates** | | |
| None. |  |  |
| **6.9.4 API Updates** | | |
| None. |  |  |
| **6.9.3 API Updates** | | |
| /api/sources | DELETE  GET  PATCH  POST  PUT | This endpoint is deprecated and will be removed in a future release. |
| /api/upload | DELETE  POST | This endpoint is deprecated and will be removed in a future release. |
| **6.9.2 API Updates** | | |
| /api/dashboards/import | POST | A new query parameter, `strategy`, has been added for this endpoint. Valid values can be `OVERWRITE` or `USE_EXISTING_OR_CREATE`.   * Specify `OVERWRITE` to implement the new overwrite import policy. * Specify `USE_EXISTING_OR_CREATE` to continue to use the existing import policy (importing the dashboard with a slightly altered name). This is the default value and will be used if `strategy` is not specified. |
| **6.9.1 API Updates** | | |
| /api/materialized-views | GET | A new, optional parameter, `sourceId={<data-source-id>}`, has been added in this release. Use this parameter to obtain a list of materialized views for a specific data source. |
| **6.9 API Updates** | | |
| application/vnd.composer.v3+json | --- | A new media type, `application/vnd.composer.v3+json` is introduced in this release. The media type `application/vnd.composer.v2+json` is deprecated and will be removed in a future release. insightsoftware recommends using the `application/vnd.composer.v3+json` media type for all API calls.  The difference between the two media types is primarily in the response of listing endpoints. |
| /api (/composer/api) | GET | This API endpoint is now deprecated and will be removed from the product in a future release. |
| /api/alerts | GET  PUT  DELETE  PATCH  POST | A new experimental API is introduced in this release that can be used to alert your end users when a metric reaches a specified threshold. No UI support for this feature is provided at this time. See Manage Alerts. |
| /api/upload | DELETE  POST | This API endpoint has been deprecated and will be removed in a future release. |
| /api/visuals/<visualId> | GET  PUT  DELETE | The visual permissions for a user are now verified when this API endpoint is used to retrieve, update, or delete a visual. |
| /api/visuals/<visualId>/acls | GET | This new endpoint can be used to list the users and groups for which visual permissions have been defined. |
| /api/visuals/<visualId>/acls/bulk | PATCH | This endpoint can now be used to grant or revoke visual permissions. However, the `ownerType=Source` property can no longer be specified because permissions to view or manage a visual are no longer tied to your permissions for its data source. However, read permissions for the visual's data source are required to see data in the visual. |
| /api/visuals | GET | The following fields in the response payload are deprecated and will be removed in a future release.   * `enabled` * `ownerType` * `name` (use `visualName` instead) * `dashboardLinks` (this field is now defined and stored in the new dashboard API response payload) |
| PUT  DELETE  POST | The following fields in the response payload of all other `/api/visuals` endpoints are deprecated and will be removed in a future release.   * `enabled` * `ownerType` * `lastModified` (use `lastModifiedDate` instead) * `ownerSourceId` (use `source.sourceId` instead) * `name` (use `visualName` instead) * `dashboardLinks` ((this field is now defined and stored in the new dashboard API response payload) |
| description | --- | A new property called `description` is added to the visual payload. |
| /api/visuals/source/<sourceId>/summary | GET | This API endpoint now checks for READ permission to the data source when reading a summary of all the visual defaults. |
| /api/user/permissions/visuals/<visualId> | GET | This new endpoint can be used to retrieve a user's permissions for a visual. |
| /api/visdefs/<sourceId> | --- | This API endpoint has now been removed from the product. It was deprecated in a previous release. |
| /api/visdefs/default/<sourceId> | --- | This API endpoint has now been removed from the product. It was deprecated in a previous release. |
| /api/visdefs/default/<sourceId>/<visualId> | GET | This API endpoint now checks for READ permission to the data source when generating a single visual default. |
| /api/dashboards/\* | DELETE  GET  POST  PUT | This endpoint in the v1 version of the API (`application/vnd.composer.dashboard.v1+json`) is deprecated and will be removed in a future release. Use the new version of the endpoint in the v2 version of the API (`application/vnd.composer.dashboard.v2+json`) instead. |
| DELETE  GET  PUT | The new `/api/dashboards` API endpoint no longer relies on visuals. Instead, it uses widgets.   * The `visualizations` container is renamed to `widgets`. * The new `widgets` array contains `widget` objects, which contain only widget-specific information: `id`, `name`, `description`, `layout`, `visualId`, and `dashboardLink`.   In addition, the `bookmarksMap` object returned in the response when using the v3 version of the Composer API (`application/vnd.composer.v3+json`) has been renamed `content`.  **Note:** The `/api/dashboard` family of API endpoints were updated with a new payload in this release. To use `vnd.composer.dashboards.v1+json` for backward compatibility, including the use of the `bookmarksMap` object (instead of the new `content` object), turn on the `dashboard-v1-api` variable on the Server-Level Variables page (only a Composer supervisor can make this change). See Server-Level Variables. |
| /api/visualizations/libs/\* | DELETE  GET  POST  PUT | The `/api/visualizations/libs` endpoint is deprecated and will be removed in a future release. Use the custom chart CLI instead. See Maintain Custom Charts Using the Custom Chart CLI. |
| /api/sources/<id>/key | GET | These security-related endpoints are deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See Trusted Access and Embed Components Using JavaScript and Trusted Access. |
| /api/sources/remove/<id> | DELETE |
| /api/sources/key | GET |
| /api/screenshot/\* | GET  POST  PUT | The screenshot-related endpoints are deprecated and will be removed in a future release. |
| /oauth/authorize | GET | This endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access API Endpoints. |
| /oauth2/client | DELETE  GET  POST  PUT | This endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access API Endpoints. |
| /oauth2/token | DELETE  GET  POST | This endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access API Endpoints. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **6.8 API Updates** | | |
| OpenAPI Updates | --- | The Composer API specification is now generated in OpenAPI 3.0 format. |
| Group Updates | --- | Groups can no longer be transferred to a different account using the API. |
| /api/export/generate/rawdata | --- | This endpoint is deprecated and will be removed in a future release. Use `/api/export/csv/raw` instead. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **6.7 API Updates** | | |
| /api/keysets/upload | POST | This new endpoint creates a keyset from a CSV file. See Upload Keyset Data From a CSV File Using the API. |
| /api/keysets/upload/<keyset-id> | PUT | This new endpoint updates a keyset from a CSV file. See Update Keyset Values From a CSV File Using the API. |
| /api/dashboards/<dashboard-ID>/interactivity | GET | This new endpoint returns the dashboard's interactivity profile. If you do not have authorization for a dashboard, errors are returned. |
| PUT | This new endpoint saves a dashboard's interactivity profile. |
| DELETE | This new endpoint deletes a dashboard's interactivity profile. |
| /api/dashboards/interactivity | GET | This new endpoint lists the existing dashboard interactivity profiles. |
| /api/dashboard/<dashboard-ID>?interactivityProfile={linked | readonly | interactive} | GET | This new endpoint returns the dashboard payload with one of the following three profile names:   * `linked`: Uses the dashboard interactivity profile set for the dashboard. * `readonly`: Overrides the dashboard interactivity profile, setting all visual interactivity settings to `false`, so users can view the dashboard and its visuals, but not interact with them. * `interactive`: Overrides the dashboard interactivity profile and all visual interativity settings to `true`, so users can view and interact with the dashboard and its visuals. This is the opposite of `readonly`. |
| /api/sources/<source-ID>/fields/meta | GET | This new endpoint is an experimental endpoint that returns information about all the fields and metrics in a data source. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **6.6 API Updates** | | |
| Group privilege renamed | The API privilege **ROLE\_MANAGE\_VISUALS** was renamed to **ROLE\_ADMINISTER\_VISUALS**. Customers who use the API to manage groups must manually make this change wherever **ROLE\_MANAGE\_VISUALS** is currently used. | |
| /api/dashboards/<dashboard-id>/acls/bulk | PATCH | This new endpoint assigns permissions for a dashboard to a list of security identities (groups, users, accounts). |
| /api/sources/<source-id>/acls/bulk | PATCH | This new endpoint assigns permissions for a data source to a list of security identities (groups, users, accounts). |
| /api/user/permissions/visuals/<visual-id> | GET | This new endpoint retrieves the permissions for a visual for the currently logged in user. |
| /api/visuals | GET | The payload from this API now can include permission information for the visual, if the query parameter `includePermissions=true` is included, enabling this capability. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **6.5 API Updates** | | |
| /api/trusted-access/clients | GET | Returns all the Trusted Access client information in the metadata. Included with this information is the access token validity time (in seconds), client ID, client name, client secret expiration time (in seconds), and the token authentication method. For a description of these, see Trusted Access Client Properties. |
| /api/trusted-access/clients | POST | Creates a Trusted Access client. The request must specify the number of seconds for which the access token is valid and the client name. The client name must be unique. When you create the client, the client ID, client secret, secret expiration time, and the token authentication method are automatically generated. |
| /api/trusted-access/clients/<id> | GET | Returns the Trusted Access client information for a specific client. The request must specify the client ID. |
| /api/trusted-access/clients/<id> | DELETE | Deletes a specific Trusted Access client. The request must specify the client ID. |
| /api/trusted-access/clients/<id> | PATCH | Updates the Trusted Access client information for a specific client. The request must specify the client ID and the number of seconds for which the access token is valid. |
| /api/trusted-access/token | POST | Generates a new access token for a user. The request must specify the Composer user name. The user must already exist, and have an active Composer user account (unless you are using LDAP with automatic provisioning for Composer). |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **6.4 API Updates** | | |
| /api/sources/<source-id>/cache/visdata | DELETE | Clears the visual data cache. |
| /api/sources/<source-id>/cache/metadata | DELETE | Clears the metadata cache. |
| /api/sources/<source-id>/cache | DELETE | Clears both the visual and metadata caches. |
| Source definition endpoints | --- | A new boolean `cacheableMetadata` property indicates whether metadata caching is enabled for a data source. The existing `cacheable` property indicates whether caching, in general, is enabled for the data source. |
| --- | A new `statsCached` property allows you to control metadata (field statistics) caching on a per-field basis. This property can be used to configure the field statistics look-up via materialized views (ignoring internal caches and redirecting the requests from the original source) and to improve the performance of statistics requests when precreated statistics data exists. Please contact your Technical Support representative to get guidance on how to configure this. |
| /api/visdefs/<source-id> | --- | This endpoint is deprecated. It is replaced by a new `/api/visuals/source/<sourcid>/summary` endpoint. The response produced by the new endpoint has also changed to include a new `visualId` setting. |
| /api/visuals/source/<source-id>/summary | GET | This endpoint obtains the default visual definitions for a data source configuration. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **6.3 API Updates** | | |
| /api/user/permissions/sources | GET | Lists the permission levels for the logged in user for all data source configurations in the system. |
| /api/user/permissions/sources/<sourceid> | GET | Retrieves the currently logged in user's source permissions for a data source. |
| /api/sources/<sourceid>/acls | GET | Retrieves a list of access rights for a data source. You can restrict the list to specific users, groups, or accounts using the `sidTypes` parameter. In addition, you can use the `returnSids` parameter to restrict the list so it retrieves only users, groups, or accounts with access to the data sources or to only users, groups, or accounts without access. |
| /api/sources/<sourceid>/acls/bulk | PUT | Grants or revokes permissions to a data source configuration a list of groups, users, or accounts. |
| /api/sources/<source-id>/security/attributes | --- | These endpoints now support the specification of multiple groups for a data source column security filter. |
| /api/sources/<source-id>/security/attributes/<id> | --- |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **6.2 API Updates** | | |
| Visual placement | --- | An error is now produced when you try to place the same visual on a dashboard twice. |
| /api/groups |  | The `sources` field is deprecated and will be removed in a future release. |
|  | The `configType` field is deprecated and will be removed in a future release. |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **6.1 API Updates** | | |
| /api/sources/<source-id>/security/filters | --- | This endpoint is enhanced to support account and user security identifiers. In past releases, only group security identifiers were supported. |
| /api/security/sids | --- | This new endpoint is introduced to retrieve security ID information. The `sidTypes` parameter can be specified with this new endpoint to limit the type of security ID information retrieved. Valid values for `sidTypes` are `GROUP`, `USER`, `ACCOUNT`, or `ALL` (the default). |

[Return to top](#top "return to top")

| Endpoint | Method | Description |
| --- | --- | --- |
| **6.0 API Updates** | | |
| With this release, you can no longer use `<hostname>:8080/zoomdata/api/version`. This is no longer supported. Use `<hostname>:8080/composer/api/version` instead. | | |

[Return to top](#top "return to top")

## Deprecated and Removed Features

### Composer v26

#### Deprecated Features

| Title | Description |
| --- | --- |
| **26.1.2 Deprecated Features** | |
| None. |  |
| **26.1.1 Deprecated Features** | |
| None. |  |
| **26.1 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

#### Removed Features

| Title | Description |
| --- | --- |
| **26.1.2 Removed Features** | |
| None. |  |
| **26.1.1 Removed Features** | |
| None. |  |
| **26.1 Removed Features** | |
| None. |  |

### Composer v25

#### Deprecated Features

| Title | Description |
| --- | --- |
| **25.4.4 Deprecated Features** | |
| None. |  |
| **25.4.3 Deprecated Features** | |
| None. |  |
| **25.4.2 Deprecated Features** | |
| None. |  |
| **25.4.1 Deprecated Features** | |
| None. |  |
| **25.4 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **25.3.7 Deprecated Features** | |
| None. |  |
| **25.3.6 Deprecated Features** | |
| None. |  |
| **25.3.5 Deprecated Features** | |
| None. |  |
| **25.3.4 Deprecated Features** | |
| None. |  |
| **25.3.3 Deprecated Features** | |
| None. |  |
| **25.3.2 Deprecated Features** | |
| None. |  |
| **25.3.1 Deprecated Features** | |
| None. |  |
| **25.3 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **25.2.10 Deprecated Features** | |
| None. |  |
| **25.2.9 Deprecated Features** | |
| None. |  |
| **25.2.8 Deprecated Features** | |
| None. |  |
| **25.2.7 Deprecated Features** | |
| None. |  |
| **25.2.6 Deprecated Features** | |
| None. |  |
| **25.2.5 Deprecated Features** | |
| None. |  |
| **25.2.4 Deprecated Features** | |
| None. |  |
| **25.2.3 Deprecated Features** | |
| None. |  |
| **25.2.2 Deprecated Features** | |
| None. |  |
| **25.2.1 Deprecated Features** | |
| None. |  |
| **25.2 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **25.1.11 Deprecated Features** | |
| None. |  |
| **25.1.10 Deprecated Features** | |
| None. |  |
| **25.1.9 Deprecated Features** | |
| None. |  |
| **25.1.8 Deprecated Features** | |
| None. |  |
| **25.1.7 Deprecated Features** | |
| None. |  |
| **25.1.6 Deprecated Features** | |
| None. |  |
| **25.1.5 Deprecated Features** | |
| None. |  |
| **25.1.4 Deprecated Features** | |
| None. |  |
| **25.1.3 Deprecated Features** | |
| None. |  |
| **25.1.2 Deprecated Features** | |
| None. |  |
| **25.1.1 Deprecated Features** | |
| None. |  |
| **25.1 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

#### Removed Features

| Title | Description |
| --- | --- |
| **25.4.4 Removed Features** | |
| None. |  |
| **25.4.3 Removed Features** | |
| None. |  |
| **25.4.2 Removed Features** | |
| None. |  |
| **25.4.1 Removed Features** | |
| None. |  |
| **25.4 Removed Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **25.3.7 Removed Features** | |
| None. |  |
| **25.3.6 Removed Features** | |
| None. |  |
| **25.3.5 Removed Features** | |
| None. |  |
| **25.3.4 Removed Features** | |
| None. |  |
| **25.3.3 Removed Features** | |
| None. |  |
| **25.3.2 Removed Features** | |
| None. |  |
| **25.3.1 Removed Features** | |
| None. |  |
| **25.3 Removed Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **25.2.10 Removed Features** | |
| None. |  |
| **25.2.9 Removed Features** | |
| None. |  |
| **25.2.8 Removed Features** | |
| None. |  |
| **25.2.7 Removed Features** | |
| None. |  |
| **25.2.6 Removed Features** | |
| None. |  |
| **25.2.5 Removed Features** | |
| None. |  |
| **25.2.4 Removed Features** | |
| None. |  |
| **25.2.3 Removed Features** | |
| None. |  |
| **25.2.2 Removed Features** | |
| None. |  |
| **25.2.1 Removed Features** | |
| None. |  |
| **25.2 Removed Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **25.1.11 Removed Features** | |
| None. |  |
| **25.1.10 Removed Features** | |
| None. |  |
| **25.1.9 Removed Features** | |
| None. |  |
| **25.1.8 Removed Features** | |
| None. |  |
| **25.1.7 Removed Features** | |
| None. |  |
| **25.1.6 Removed Features** | |
| None. |  |
| **25.1.5 Removed Features** | |
| None. |  |
| **25.1.4 Removed Features** | |
| None. |  |
| **25.1.3 Removed Features** | |
| None. |  |
| **25.1.2 Removed Features** | |
| None. |  |
| **25.1.1 Removed Features** | |
| None. |  |
| **25.1 Removed Features** | |
| None. |  |

[Return to top](#top "return to top")

### Composer v24

#### Deprecated Features

| Title | Description |
| --- | --- |
| **24.4.15 Deprecated Features** | |
| None. |  |
| **24.4.14 Deprecated Features** | |
| None. |  |
| **24.4.13 Deprecated Features** | |
| None. |  |
| **24.4.12 Deprecated Features** | |
| None. |  |
| **24.4.11 Deprecated Features** | |
| None. |  |
| **24.4.10 Deprecated Features** | |
| None. |  |
| **24.4.9 Deprecated Features** | |
| None. |  |
| **24.4.8 Deprecated Features** | |
| None. |  |
| **24.4.7 Deprecated Features** | |
| None. |  |
| **24.4.6 Deprecated Features** | |
| None. |  |
| **24.4.5 Deprecated Features** | |
| None. |  |
| **24.4.4 Deprecated Features** | |
| None. |  |
| **24.4.3 Deprecated Features** | |
| None. |  |
| **24.4.2 Deprecated Features** | |
| None. |  |
| **24.4.1 Deprecated Features** | |
| None. |  |
| **24.4 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **24.3.10 Deprecated Features** | |
| None. |  |
| **24.3.9 Deprecated Features** | |
| None. |  |
| **24.3.8 Deprecated Features** | |
| None. |  |
| **24.3.7 Deprecated Features** | |
| None. |  |
| **24.3.6 Deprecated Features** | |
| None. |  |
| **24.3.5 Deprecated Features** | |
| None. |  |
| **24.3.4 Deprecated Features** | |
| None. |  |
| **24.3.3 Deprecated Features** | |
| None. |  |
| **24.3.2 Deprecated Features** | |
| None. |  |
| **24.3.1 Deprecated Features** | |
| None. |  |
| **24.3 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **24.2.12 Deprecated Features** | |
| None. |  |
| **24.2.11 Deprecated Features** | |
| None. |  |
| **24.2.10 Deprecated Features** | |
| None. |  |
| **24.2.9 Deprecated Features** | |
| None. |  |
| **24.2.8 Deprecated Features** | |
| None. |  |
| **24.2.7 Deprecated Features** | |
| None. |  |
| **24.2.6 Deprecated Features** | |
| None. |  |
| **24.2.5 Deprecated Features** | |
| None. |  |
| **24.2.4 Deprecated Features** | |
| None. |  |
| **24.2.3 Deprecated Features** | |
| None. |  |
| **24.2.2 Deprecated Features** | |
| None. |  |
| **24.2.1 Deprecated Features** | |
| None. |  |
| **24.2 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **24.1.12 Deprecated Features** | |
| None. |  |
| **24.1.11 Deprecated Features** | |
| None. |  |
| **24.1.10 Deprecated Features** | |
| None. |  |
| **24.1.9 Deprecated Features** | |
| None. |  |
| **24.1.8 Deprecated Features** | |
| None. |  |
| **24.1.7 Deprecated Features** | |
| None. |  |
| **24.1.6 Deprecated Features** | |
| None. |  |
| **24.1.5 Deprecated Features** | |
| None. |  |
| **24.1.4 Deprecated Features** | |
| None. |  |
| **24.1.3 Deprecated Features** | |
| None. |  |
| **24.1.2 Deprecated Features** | |
| None. |  |
| **24.1.1 Deprecated Features** | |
| None. |  |
| **24.1 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

#### Removed Features

| Title | Description |
| --- | --- |
| **24.4.15 Removed Features** | |
| None. |  |
| **24.4.14 Removed Features** | |
| None. |  |
| **24.4.13 Removed Features** | |
| None. |  |
| **24.4.12 Removed Features** | |
| None. |  |
| **24.4.11 Removed Features** | |
| None. |  |
| **24.4.10 Removed Features** | |
| None. |  |
| **24.4.9 Removed Features** | |
| None. |  |
| **24.4.8 Removed Features** | |
| None. |  |
| **24.4.7 Removed Features** | |
| None. |  |
| **24.4.6 Removed Features** | |
| None. |  |
| **24.4.5 Removed Features** | |
| None. |  |
| **24.4.4 Removed Features** | |
| None. |  |
| **24.4.3 Removed Features** | |
| None. |  |
| **24.4.2 Removed Features** | |
| None. |  |
| **24.4.1 Removed Features** | |
| None. |  |
| **24.4 Removed Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **24.3.10 Removed Features** | |
| None. |  |
| **24.3.9 Removed Features** | |
| None. |  |
| **24.3.8 Removed Features** | |
| None. |  |
| **24.3.7 Removed Features** | |
| None. |  |
| **24.3.6 Removed Features** | |
| None. |  |
| **24.3.5 Removed Features** | |
| None. |  |
| **24.3.4 Removed Features** | |
| None. |  |
| **24.3.3 Removed Features** | |
| None. |  |
| **24.3.2 Removed Features** | |
| None. |  |
| **24.3.1 Removed Features** | |
| None. |  |
| **24.3 Removed Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **24.2.13 Removed Features** | |
| None. |  |
| **24.2.11 Removed Features** | |
| None. |  |
| **24.2.10 Removed Features** | |
| None. |  |
| **24.2.9 Removed Features** | |
| None. |  |
| **24.2.8 Removed Features** | |
| None. |  |
| **24.2.7 Removed Features** | |
| None. |  |
| **24.2.6 Removed Features** | |
| None. |  |
| **24.2.5 Removed Features** | |
| None. |  |
| **24.2.4 Removed Features** | |
| None. |  |
| **24.2.3 Removed Features** | |
| None. |  |
| **24.2.2 Removed Features** | |
| None. |  |
| **24.2.1 Removed Features** | |
| None. |  |
| **24.2 Removed Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **24.1.12 Removed Features** | |
| None. |  |
| **24.1.11 Removed Features** | |
| None. |  |
| **24.1.10 Removed Features** | |
| None. |  |
| **24.1.9 Removed Features** | |
| None. |  |
| **24.1.8 Removed Features** | |
| None. |  |
| **24.1.7 Removed Features** | |
| None. |  |
| **24.1.6 Removed Features** | |
| None. |  |
| **24.1.5 Removed Features** | |
| None. |  |
| **24.1.4 Removed Features** | |
| None. |  |
| **24.1.3 Removed Features** | |
| None. |  |
| **24.1.2 Removed Features** | |
| None. |  |
| **24.1.1 Removed Features** | |
| None. |  |
| **24.1 Removed Features** | |
| None. |  |

[Return to top](#top "return to top")

### Composer v23

#### Deprecated Features

| Title | Description |
| --- | --- |
| **23.4.13 Deprecated Features** | |
| None. |  |
| **23.4.12 Deprecated Features** | |
| None. |  |
| **23.4.11 Deprecated Features** | |
| None. |  |
| **23.4.10 Deprecated Features** | |
| None. |  |
| **23.4.9 Deprecated Features** | |
| None. |  |
| **23.4.8 Deprecated Features** | |
| None. |  |
| **23.4.7 Deprecated Features** | |
| None. |  |
| **23.4.6 Deprecated Features** | |
| None. |  |
| **23.4.5 Deprecated Features** | |
| None. |  |
| **23.4.4 Deprecated Features** | |
| None. |  |
| **23.4.3 Deprecated Features** | |
| None. |  |
| **23.4.2 Deprecated Features** | |
| None. |  |
| **23.4.1 Deprecated Features** | |
| None. |  |
| **23.4 Deprecated Features** | |
| Tenancy and Default Account Changes | * The **superaccount** work area is renamed to **Visual Data Discovery**. * The company tenant is no longer created by Composer for new installations, existing company tenants remain unchanged. * The default admin user is now the **system administrator** and has all supervisor user privileges, as a member of the **Visual Data Discovery** tenant. * The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead. * Tenant Accounts are now known as Tenants in the user interface. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **23.3.14 Deprecated Features** | |
| None. |  |
| **23.3.13 Deprecated Features** | |
| None. |  |
| **23.3.12 Deprecated Features** | |
| None. |  |
| **23.3.11 Deprecated Features** | |
| None. |  |
| **23.3.10 Deprecated Features** | |
| None. |  |
| **23.3.9 Deprecated Features** | |
| None. |  |
| **23.3.8 Deprecated Features** | |
| None. |  |
| **23.3.7 Deprecated Features** | |
| None. |  |
| **23.3.6 Deprecated Features** | |
| None. |  |
| **23.3.5 Deprecated Features** | |
| None. |  |
| **23.3.4 Deprecated Features** | |
| None. |  |
| **23.3.3 Deprecated Features** | |
| None. |  |
| **23.3.2 Deprecated Features** | |
| None. |  |
| **23.3.1 Deprecated Features** | |
| None. |  |
| **23.3 Deprecated Features** | |
| Cloudmade for Map Visuals | Cloudmade’s tile support is no longer available, and has been removed from map visuals.  Existing visuals that use the Cloudmade Tile Provider are migrated to Open Street Maps when you upgrade to this release or later. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **23.2.15 Deprecated Features** | |
| None. |  |
| **23.2.14 Deprecated Features** | |
| None. |  |
| **23.2.13 Deprecated Features** | |
| None. |  |
| **23.2.12 Deprecated Features** | |
| None. |  |
| **23.2.11 Deprecated Features** | |
| None. |  |
| **23.2.10 Deprecated Features** | |
| None. |  |
| **23.2.9 Deprecated Features** | |
| None. |  |
| **23.2.8 Deprecated Features** | |
| None. |  |
| **23.2.7 Deprecated Features** | |
| None. |  |
| **23.2.6 Deprecated Features** | |
| None. |  |
| **23.2.5 Deprecated Features** | |
| None. |  |
| **23.2.4 Deprecated Features** | |
| None. |  |
| **23.2.3 Deprecated Features** | |
| None. |  |
| **23.2.2 Deprecated Features** | |
| Alerts Icon | The alerts icon is no longer present in dashboards for users who do not have the Create Alerts or Administer Alerts privilege. |
| **23.2.1 Deprecated Features** | |
| None. |  |
| **23.2 Deprecated Features** | |
| Materialized Views | Materialized views are disabled by default. To enable, contact technical support for assistance. |
| Connector Properties for Integer to Datetime Conversion in Timezone Offsets | The properties `datasource.timestamp-millis-fields-names` and `datasource.timestamp-millis-fields-pattern` are deprecated and will be removed in a future release. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **23.1.14 Deprecated Features** | |
| None. |  |
| **23.1.13 Deprecated Features** | |
| None. |  |
| **23.1.12 Deprecated Features** | |
| None. |  |
| **23.1.11 Deprecated Features** | |
| None. |  |
| **23.1.10 Deprecated Features** | |
| None. |  |
| **23.1.9 Deprecated Features** | |
| None. |  |
| **23.1.8 Deprecated Features** | |
| None. |  |
| **Composer 23.1.7 Deprecated Features** | |
| None. |  |
| **23.1.6 Deprecated Features** | |
| None. |  |
| **23.1.5 Deprecated Features** | |
| None. |  |
| **23.1.4 Deprecated Features** | |
| None. |  |
| **23.1.3 Deprecated Features** | |
| None. |  |
| **23.1.2 Deprecated Features** | |
| None. |  |
| **23.1.1 Deprecated Features** | |
| None. |  |
| **23.1 Deprecated Features** | |
| Materialized Views API | The Materialized Views API is deprecated. This API will be removed in a future release. |
| Scheduled Dashboard Reports | `sendOnlyToMe` is deprecated and will be removed in a future release. |
| Raw Data Export Endpoint | The endpoint `/api/export/csv/raw` is deprecated and will be removed in a future release. When used, returns payload as `DeprecatedRawDataExportResource`. Use `/api/export/rawdataforvisual` instead. |
| Visual Data Export Endpoint | The endpoint `/api/export/chartdata/{file_name}` is deprecated and will be removed in a future release. When used, returns payload as `DeprecatedVisualDataExportResource`. Use `/api/export/visualdata` instead. |
| Admin Service | The Admin Service microservice, used for capturing common logs, is deprecated and will be removed in a future release.   * For non-Kubernetes environments: Use the Consul UI to observe the general health state of your deployment. Adjust logging levels using the `service.properties` file or the Consul API. * For Kubernetes environments: Configuration management compatible with Kubernetes will replace the Admin Service microservice.   See How Do I Enable Debug Mode in Services?. |
| Activity Logging | Activity logging in `zoomdata-activity.log` is deprecated and will be removed in a future release.  Information previously captured in `zoomdata-activity.log` can be found in other log files such as `access.log`, `service.log`, and by using Composer's User Auditing feature. |

[Return to top](#top "return to top")

#### Removed Features

| Title | Description | Alternative |
| --- | --- | --- |
| **23.4.13 Removed Features** | | |
| None. |  |  |
| **23.4.12 Removed Features** | | |
| None. |  |  |
| **23.4.11 Removed Features** | | |
| None. |  |  |
| **23.4.10 Removed Features** | | |
| None. |  |  |
| **23.4.9 Removed Features** | | |
| None. |  |  |
| **23.4.8 Removed Features** | | |
| None. |  |  |
| **23.4.7 Removed Features** | | |
| None. |  |  |
| **23.4.6 Removed Features** | | |
| None. |  |  |
| **23.4.5 Removed Features** | | |
| None. |  |  |
| **23.4.4 Removed Features** | | |
| None. |  |  |
| **23.4.3 Removed Features** | | |
| None. |  |  |
| **23.4.2 Removed Features** | | |
| None. |  |  |
| **23.4.1 Removed Features** | | |
| None. |  |  |
| **23.4 Removed Features** | | |
| None. |  |  |

[Return to top](#top "return to top")

| Title | Description | Alternative |
| --- | --- | --- |
| **23.3.14 Removed Features** | | |
| None. |  |  |
| **23.3.13 Removed Features** | | |
| None. |  |  |
| **23.3.12 Removed Features** | | |
| None. |  |  |
| **23.3.11 Removed Features** | | |
| None. |  |  |
| **23.3.10 Removed Features** | | |
| None. |  |  |
| **23.3.9 Removed Features** | | |
| None. |  |  |
| **23.3.8 Removed Features** | | |
| None. |  |  |
| **23.3.7 Removed Features** | | |
| None. |  |  |
| **23.3.6 Removed Features** | | |
| None. |  |  |
| **23.3.5 Removed Features** | | |
| None. |  |  |
| **23.3.4 Removed Features** | | |
| None. |  |  |
| **23.3.3 Removed Features** | | |
| None. |  |  |
| **23.3.2 Removed Features** | | |
| None. |  |  |
| **23.3.1 Removed Features** | | |
| None. |  |  |
| **23.3 Removed Features** | | |
| api/trusted-access/token | The API `/api/trusted-access/token`, deprecated in an earlier release (Composer v7.5), is now removed. | Use `/api/trusted-access/push/tokens` or `/api/trusted-access/pull/tokens` instead. See Trusted Access API Endpoints. |
| `/api/visualizations/*` and API for Visualizations components | All APIs in the control `/api/visualizations/*`, deprecated in an earlier release (Composer v7), are now removed.  The complete list of removed APIs:   * `GET /api/visualizations/{id}` * `PUT /api/visualizations/{id}` * `DELETE /api/visualizations/{id}` * `GET /api/visualizations` * `POST /api/visualizations` * `POST /api/visualizations/import` * `GET /api/visualizations/export/{visId}` * `POST /api/visualizations/thumbnail` * `GET /api/visualizations/{visId}/thumbnail/{thumbnailId}` * `GET /api/visualizations/{visualizationId}/source/{componentId}` | Use the APIs `/api/visual-types/*` instead:   * `GET /api/visual-types/{id}` * `PUT /api/visual-types/{id}` * `DELETE /api/visual-types/{id}` * `GET /api/visual-types` * `POST /api/visuals-types`   Export and import visual types:   * `GET /api/visual-types/export/{visTypeId}` * `POST /api/visual-types/import`   Thumbnail management:   * `POST /api/visual-types/thumbnail` * `GET /api/visual-types/{visTypeId}/thumbnail/{thumbnailId}`   Visualizations components:   * `GET /api/visual-types/components/{componentId}` |
| /api/system/systemInfo | The API `api/system/systemInfo`, deprecated in an earlier release, is now removed. | Use `/api/version` to see the current application version and system information. |
| The `userId` and `disabledMessage` fields | The fields `userId` and `disabledMessage` used in the connections-related endpoints and deprecated in an earlier release are now removed.  Affected APIs:   * All APIs in the `connections` control (including `GET`, `POST`, `PUT``/api/connections` etc.) * All APIs in the `dashboard-migration` control (`GET``/api/dashboards/export` and `POST``/api/dashboards/import`)   Use `createdByUserID` and `lastModifiedByUserID` as references instead of `userId`. | Use `createdByUserID` and `lastModifiedByUserID` as references instead of `userId`. |
| Filter Snippet Source Field | The Field column, used to select a data field from a linked source, has been removed. | Select a data field in Value Column, and if available, add a Display Column. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **23.2.15 Removed Features** | |
| None. |  |
| **23.2.14 Removed Features** | |
| None. |  |
| **23.2.13 Removed Features** | |
| None. |  |
| **23.2.12 Removed Features** | |
| None. |  |
| **23.2.11 Removed Features** | |
| None. |  |
| **23.2.10 Removed Features** | |
| None. |  |
| **23.2.9 Removed Features** | |
| None. |  |
| **23.2.8 Removed Features** | |
| None. |  |
| **23.2.7 Removed Features** | |
| None. |  |
| **23.2.6 Removed Features** | |
| None. |  |
| **23.2.5 Removed Features** | |
| None. |  |
| **23.2.4 Removed Features** | |
| None. |  |
| **23.2.3 Removed Features** | |
| None. |  |
| **23.2.2 Removed Features** | |
| None. |  |
| **23.2.1 Removed Features** | |
| None. |  |
| **23.2 Removed Features** | |
| Legends for KPI Visuals | Legends have been removed from KPI visuals. |
| `hasRawData`, `hasRawDataOnly` | Support for these fields are removed for the endpoint `/api/sources/{sourceId}/visual-types/variables-values/`. Use `RAW_DATA` instead. |
| Media Type `application/vnd.composer.dashboard.v2+json` | The media type `application/vnd.composer.dashboard.v2+json` for `api/dashboards`, deprecated in an earlier release, is now removed. |
| `page` and `size` Parameters | The parameters `page` and `size`for the Users autocomplete endpoint `GET /api/users/autocomplete`, deprecated in a previous release, have been removed. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **23.1.14 Removed Features** | |
| None. |  |
| **23.1.13 Removed Features** | |
| None. |  |
| **23.1.12 Removed Features** | |
| None. |  |
| **23.1.11 Removed Features** | |
| None. |  |
| **23.1.10 Removed Features** | |
| None. |  |
| **23.1.9 Removed Features** | |
| None. |  |
| **23.1.8 Removed Features** | |
| None. |  |
| **23.1.7 Removed Features** | |
| None. |  |
| **23.1.6 Removed Features** | |
| None. |  |
| **23.1.5 Removed Features** | |
| None. |  |
| **23.1.4 Removed Features** | |
| None. |  |
| **23.1.3 Removed Features** | |
| None. |  |
| **23.1.2 Removed Features** | |
| None. |  |
| **23.1.1 Removed Features** | |
| None. |  |
| **23.1 Removed Features** | |
| Tracing Microservice | The Composer Tracing Microservice (`zoomdata-tracing-server`), deprecated in a previous release, is now removed. |

[Return to top](#top "return to top")

### Composer v22

#### Deprecated Features

| Title | Description |
| --- | --- |
| **22.4.14 Deprecated Features** | |
| None. |  |
| **22.4.13 Deprecated Features** | |
| None. |  |
| **22.4.12 Deprecated Features** | |
| None. |  |
| **22.4.11 Deprecated Features** | |
| None. |  |
| **22.4.10 Deprecated Features** | |
| None. |  |
| **22.4.9 Deprecated Features** | |
| None. |  |
| **22.4.8 Deprecated Features** | |
| None. |  |
| **22.4.7 Deprecated Features** | |
| None. |  |
| **22.4.6 Deprecated Features** | |
| None. |  |
| **22.4.5 Deprecated Features** | |
| None. |  |
| **22.4.4 Deprecated Features** | |
| None. |  |
| **22.4.3 Deprecated Features** | |
| None. |  |
| **22.4.2 Deprecated Features** | |
| None. |  |
| **22.4.1 Deprecated Features** | |
| None. |  |
| **22.4 Deprecated Features** | |
| Tracing Microservice Support | The Composer Tracing Microservice (`zoomdata-tracing-server`) is deprecated. This service will be removed in a future release, replaced by an alternative feature. |
| Edit Visual Menu Options | The **More** menu option **Edit Visual** is renamed **Settings** for visuals and rich text snippets. |

[Return to top](#top "return to top")

#### Removed Features

| Title | Description |
| --- | --- |
| **22.4.14 Removed Features** | |
| None. |  |
| **22.4.13 Removed Features** | |
| None. |  |
| **22.4.12 Removed Features** | |
| None. |  |
| **22.4.11 Removed Features** | |
| None. |  |
| **22.4.10 Removed Features** | |
| None. |  |
| **22.4.9 Removed Features** | |
| None. |  |
| **22.4.8 Removed Features** | |
| None. |  |
| **22.4.7 Removed Features** | |
| None. |  |
| **22.4.6 Removed Features** | |
| None. |  |
| **22.4.5 Removed Features** | |
| None. |  |
| **22.4.4 Removed Features** | |
| None. |  |
| **22.4.3 Removed Features** | |
| None. |  |
| **22.4.2 Removed Features** | |
| None. |  |
| **22.4.1 Removed Features** | |
| None. |  |
| **22.4 Removed Features** | |
| Radial Menu | Radial menu functionality has been streamlined into and replaced by the Context Menu. |

[Return to top](#top "return to top")

### Composer v8.4 and Earlier

#### Deprecated Features

| Title | Description |
| --- | --- |
| **8.4.1 Deprecated Features** | |
| None. |  |
| **8.4 Deprecated Features** | |
| Logging Updates | The logback.zoomdata property, previously used to control the log level of some loggers, has been removed. Use a standard spring boot approach to specify appropriate properties. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **8.3 Deprecated Features** | |
| Elasticsearch Support Update | Composer no longer supports the use of Elasticsearch version 6. Use Elasticsearch 7 or 8 instead. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **8.2 Deprecated Features** | |
| Support for Presto Connectors | Composer no longer supports use of the Presto connector version 319; the Presto connector will be removed in a future release. Use the new Trino connector; see Manage the Trino Connector. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **8.1 Deprecated Features** | |
| `visualId` | `visualId` is now deprecated from the widgets payload of `/api/dashboards/`. |
| Scheduled Reports API Updates | The behavior of the attribute `sendOnlyToOwner` is changed. When the attribute is set to `true`, the current user is now added to the list of `users`, and `sendOnlyToOwner` is reset by Logi Composer to `false`. The attribute `sendOnlyToOwner` is deprecated, and will be removed in a future release. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **8.0 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

#### Removed Features

| Title | Description |
| --- | --- |
| **8.4.1 Removed Features** | |
| None. |  |
| **8.4 Removed Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **8.3 Removed Features** | |
| Composer SDK | The Composer SDK is no longer supported. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **8.2 Removed Features** | |
| Visual Info Sidebar Menu Update | The field **Default Title** has been removed from the Info sidebar menu of visuals. |
| Visual Gallery Updates | The Usage column has been removed. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **8.1 Removed Features** | |
| Scheduled Reports | The **Send to me** toggle is removed, replaced by a field you can use to add report recipients, prepopulated with the current user’s information. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **8.0 Removed Features** | |
| WebSocket Authentication | Authentication of WebSocket connections in embedded mode using trusted access tokens in the WebSocket URL, deprecated in Composer v7.10, is now removed. Authentication is handled by the Embed Manager. |

[Return to top](#top "return to top")

### Composer v7.10 and Earlier

#### Deprecated Features

| Title | Description |
| --- | --- |
| **7.10.23 Deprecated Features** | |
| None. |  |
| **7.10.22 Deprecated Features** | |
| None. |  |
| **7.10.21 Deprecated Features** | |
| None. |  |
| **7.10.20 Deprecated Features** | |
| None. |  |
| **7.10.19 Deprecated Features** | |
| None. |  |
| **7.10.18 Deprecated Features** | |
| None. |  |
| **7.10.17 Deprecated Features** | |
| None. |  |
| **7.10.16 Deprecated Features** | |
| None. |  |
| **7.10.15 Deprecated Features** | |
| None. |  |
| **7.10.14 Deprecated Features** | |
| None. |  |
| **7.10.13 Deprecated Features** | |
| None. |  |
| **7.10.12 Deprecated Features** | |
| Composer SDK | The Composer SDK is deprecated, and is not supported in later versions of Composer. |
| **7.10.11 Deprecated Features** | |
| None. |  |
| **7.10.10 Deprecated Features** | |
| None. |  |
| **7.10.9 Deprecated Features** | |
| None. |  |
| **7.10.8 Deprecated Features** | |
| None. |  |
| **7.10.7 Deprecated Features** | |
| None. |  |
| **7.10.6 Deprecated Features** | |
| None. |  |
| **7.10.5 Deprecated Features** | |
| None. |  |
| **7.10.4 Deprecated Features** | |
| None. |  |
| **7.10.3 Deprecated Features** | |
| None. |  |
| **7.10.2 Deprecated Features** | |
| None. |  |
| **7.10.1 Deprecated Features** | |
| None. |  |
| **7.10 Deprecated Features** | |
| zoomdata-client | The zoomdata-client is deprecated, and will be removed in a future release. You can embed Composer components using JavaScript and Trusted Access. |
| /api/visuals/ | The field `defaultTitle` is deprecated, and will be removed in a future release. |
| User Resource Update | Several unused fields for user resource have been made read only and are deprecated in this release and removed in a future release.   * groupRoles * external * deletable * userId |
| WebSocket Authentication | Authentication of WebSocket connections in embedded mode using trusted access tokens in the WebSocket URL has been deprecated. Authentication is now handled by the Embed Manager. |
| Embed Manager Update | The `initialToken` parameter is deprecated for the Embed Manager and will be removed in a future release. |
| System Activity API | These system activity endpoints are deprecated in v7.10 and may be removed in a future release.  `GET /api/system/activity/type/{activityType}`  `PUT /api/system/activity/type/{activityType}`  `GET /api/system/activity/type` |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.9 Deprecated Features** | |
| /api/inventory/ | The endpoint `/api/inventory/` has been expanded to return additional information about dashboards and sources. If no parameter `type` is sent, DASHBOARD information is returned. This feature is deprecated and will be removed in a future release. |
| /api/connections/{connectionId}/preview | This endpoint has been deprecated and will be removed in a future release. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.8 Deprecated Features** | |
| /api/visuals/source/<source-id>/summary/ | The end point `/api/visuals/source/<source-id>/summary/` is deprecated and will be removed in a future release. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.7 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.6 Deprecated Features** | |
| GET /api/visuals | We have removed the following fields for the GET api/visuals payload:   * `ownerType` * `name` * `>enabled`   We have removed the following fields from the response payload of all other /api/visuals endpoints:   * `enabled` * `ownerType` * `lastModified` * `ownerSourceId` * `name` |
| visualizations | Deprecated. Use `/visual-types/`. |
| visualization component | Deprecated. Use `/visual-types/components/`. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.5 Deprecated Features** | |
| /api/trusted-access/token | Deprecated. Use `/api/trusted-access/pull/tokens`. This is primarily a name change for the endpoint; payloads and functionality remain unchanged. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.4 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.3 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.2 Deprecated Features** | |
| Standardized Max Threads Property | Composer Web and Query Engine microservices no longer use the `jetty.threadpool.maxThreads` property. We have replaced it with `server.jetty.max-threads` for all microservices.  Property File Configuration (`server.jetty.max-threads`)   * For QE and Zoomdata(Composer Web) is The number of threads to serve the HTTP & WebSocket clients. * For all other microservices is The number of threads to serve the HTTP clients. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.1 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.0 Deprecated Features** | |
| None. |  |

[Return to top](#top "return to top")

#### Removed Features

| Title | Description |
| --- | --- |
| **7.10 Removed Features** | |
| OAuth Support Update | OAuth connection and token support, deprecated in a previous release, is now removed from the Composer interface and API. See Trusted Access. |
| `${User.zoomdataUserName}` Support Update | The context variable, `${User.zoomdataUserName}`, deprecated in an earlier release, is now removed from Composer. Use `${User.composerUserName}` in connections, in security filters, and in custom SQL instead. |
| /api/visuals/source/<source-id>/summary/ | The end point `/api/visuals/source/<source-id>/summary/`, deprecated in v7.8, is now removed. |
| /api/visdefs/default/{sourceId}/{visId} | The endpoint `/api/visdefs/default/{sourceId}/{visId}`, deprecated in an earlier release, is now removed. Use `/api/sources/{sourceId}/visual-types/{visualTypeId}/initial-visual` instead. |
| Removal of Group Fields | Two previously deprecated fields from group resources have now been removed:   * `configType` from `GroupResource` * `sources` from `GroupAclResource`   Use `/api/sources/{sourceId}/acls` to manage source permissions. |
| Source Creation Changes | As part of the redesigned source creation process, the source creation wizard has been removed. Available Visual Type selection is now managed by users with appropriate permissions on the Sources page. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.9 Removed Features** | |
| API | `/user/source-acl` is now removed from Composer. It was deprecated in a previous release.  `/user/source-acl/{sourceID}` is now removed from Composer. It was deprecated in a previous release. |
| CLI API Endpoints | Visualization library endpoints used by the CLI and deprecated in Composer v6.9 have been removed. These include:   * `GET /api/visualizations/libs` * `POST /api/visualizations/libs` * `DELETE /api​/visualizations​/libs​/{id}` * `GET /api​/visualizations​/libs​/{id}/*` |
| `application/vnd.composer.v2+json` Media Type | The media type `application/vnd.composer.v2+json`, deprecated in v6.9, has been removed. Use the `application/vnd.composer.v3+json` media type instead. |
| Custom Chart CLI Updates | The ability to edit the visibility of a custom chart using the CLI has been removed. |
| Activity Logging Updates | The system property `activity.remember_me`, deprecated in a previous release, has been removed from `zoomdata.properties`. The associated log file, `Remember_me.log`, is no longer generated. |
| Duplicate Custom Metrics | The ability to duplicate custom metrics in the Composer interface has been removed. You can continue to use the appropriate API endpoints to create multiple custom metrics with different names that use the same underlying formula. |
| Removal of Deprecated Endpoints | Several groups of endpoints, deprecated in the Swagger specification in Composer 6.9, are now removed. This includes endpoints for sources from connections, file uploads, derived fields, formulas, and dashboards import and export. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.8 Removed Features** | |
| /api/preferences/ | The endpoint `/api/preferences/`, deprecated in 6.9, has been removed. |
| /api/inventory/ | The endpoint `/api/inventory/` no longer returns a `thumbnailDate` field. |
| /api/dashboards/ | The endpoint `/api/dashboards/` no longer returns a `thumbnailDate` field. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.7 Removed Features** | |
| Library View Support Update | URL links to quick filters have been removed from the Dashboard Library to provide a more streamlined interface and embedding experience. Functionality of the quick filter icons remain unchanged. |
| Security Keys Authentication Update | * Security Keys have been deprecated as an authentication option in Composer. As part of this change, existing public links previously tied to security keys cannot be used. * The `/api/dashboards/{id}/key` endpoint, used to generate security keys, has been removed.   This change additionally removes:   * Application Property: `activity.security_key` * Activity Logging type: `security_key` * A field from activity logging records: `userType`   Support for iFrame embedding reliant on security keys has been removed. Use Trusted Access instead for all embedded workflows. See Trusted Access. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.6 Removed Features** | |
| Security Key Updates | Previously deprecated Security Keys endpoints are now removed from Composer. Use Trusted Access instead for all embedded workflows. See Trusted Access. |
| Group Privilege Update | The privilege **Can Generate Dashboard Link** has been removed. The API privilege `ROLE_SHARE_DASHBOARDS` has been removed. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.5 Removed Features** | |
| Remove Deprecated Security Keys-Related /api/sources endpoints | APIs affected:  `GET /api/sources/{id}/key`  `GET​ /api​/sources​/key`  `DELETE ​/api​/sources​/remove​/{id}`  These APIs were deprecated in release v6.9 and have now been removed from the platform. Use Trusted Access instead for all embedded workflows. For more information about trusted access, see Trusted Access. For more information about embedding Composer components, see Embed Composer Components Using JavaScript and Trusted Access. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.4 Removed Features** | |
| `/api/screenshot/*` `/api/screenshot-management` | The `/api/screenshot/*` endpoint and `/api/screenshot-management` endpoint were deprecated in v6.9 and are now removed.  This includes, for the screenshot-management tag:   * GET `/api/screenshot/{dasbhoardId}` * PUT `/api/screenshot/{dashboardId}` * POST `/api/screenshot/{dashboardId}`   This includes, for the screenshot tag:   * PUT `/api/screenshot/{dasbhoardId}`   This change additionally removes:   * The `screenshot` field from the `Import-Export` payload * The `thumbnailDate` field from `/api/inventory` * The `thumbnailDate` field from `/api/dashboards` * The screenshot refresh job in the `scheduler`   Several screenshot-related properties are no longer in the property files:   * `screenshot.daemon.enabled` * `screenshots.dashboard.enabled` * `screenshot.daemon.schedule.rate` * `screenshot.webdriver.timeout` * `screenshot.height` * `screenshot.width` * `export.dashboard.screenshot.timeout.seconds` * `screenshot.daemon.threads.maximum` |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.3 Removed Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.2 Removed Features** | |
| Dashboard Library | The thumbnail view and dashboard preview views have been removed from the dashboard library. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.1 Removed Features** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.0 Removed Features** | |
| None. |  |

[Return to top](#top "return to top")

### Composer v6.9 and Earlier

#### Deprecated Features

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **6.9.29 Deprecated Features** | |
| None. | |
| **6.9.28 Deprecated Features** | |
| None. | |
| **6.9.27 Deprecated Features** | |
| None. | |
| **6.9.26 Deprecated Features** | |
| None. | |
| **6.9.25 Deprecated Features** | |
| None. | |
| **6.9.24 Deprecated Features** | |
| None. | |
| **6.9.23 Deprecated Features** | |
| None. | |
| **6.9.22 Deprecated Features** | |
| None. | |
| **6.9.21 Deprecated Features** | |
| None. | |
| **6.9.20 Deprecated Features** | |
| None. | |
| **6.9.19 Deprecated Features** | |
| None. | |
| **6.9.18 Deprecated Features** | |
| None. | |
| **6.9.17 Deprecated Features** | |
| None. | |
| **6.9.16 Deprecated Features** | |
| None. | |
| **6.9.15 Deprecated Features** | |
| None. | |
| **6.9.14 Deprecated Features** | |
| None. | |
| **6.9.13 Deprecated Features** | |
| None. | |
| **6.9.12 Deprecated Features** | |
| None. | |
| **6.9.11 Deprecated Features** | |
| None. | |
| **6.9.10 Deprecated Features** | |
| None. | |
| **6.9.9 Deprecated Features** | |
| None. | |
| **6.9.8 Deprecated Features** | |
| None. | |
| **6.9.7 Deprecated Features** | |
| None. | |
| **6.9.6 Deprecated Features** | |
| None. | |
| **6.9.5 Deprecated Features** | |
| None. | |
| **6.9.4 Deprecated Features** | |
| None. | |
| **6.9.3 Deprecated Features** | |
| API | The `/api/sources` and `/api/upload` endpoints are deprecated and will be removed in a future release. |
| **6.9.2 Deprecated Features** | |
| Custom Metric Date and Time Aggregation Functions | The custom metric `DATE()`, `DateADD`, and `DateSUB` functions still work but should no longer be used. They are deprecated in this release and will be removed in a future release. Instead, use the `now()` and `time_add` functions. See Date and Time Filter Aggregation Functions. |
| **6.9.1 Deprecated Features** | |
| None. | |
| **6.9 Deprecated Features** | |
| API | The media type `application/vnd.composer.v2+json` is deprecated and will be removed in a future release. Use the `application/vnd.composer.v3+json` media type instead. |
| The `GET /api` (`/composer/api`) endpoint is now deprecated and will be removed from the product in a future release. |
| The `/api/dashboards/*` endpoint used in the v1 version of the API (`application/vnd.composer.dashboard.v1+json`) is deprecated and will be removed in a future release. Use the new version of the endpoint in the v2 version of the API (`application/vnd.composer.dashboard.v2+json`) or `application/vnd.composer.v2` instead. Errors will result if you attempt to use `application/vnd.composer.dashboard.v1+json`.  Contact Customer Support to use `vnd.composer.dashboards.v1+json` for backward compatibility, including the use of the `bookmarksMap` object (instead of the new `content` object).  **Note:** When no `content-type` header is specified, Composer defaults to using `application/vnd.composer.dashboard.v1+json`. |
| The `/api/upload` endpoint is deprecated and will be removed in a future release. |
| The `/api/visualizations/lib/*` endpoint is deprecated and will be removed in a future release. Use the custom chart CLI instead. See Maintain Custom Charts Using the Custom Chart CLI. |
| The `/api/sources` endpoint is deprecated and will be replaced in a future release. |
| The `GET /api/sources/<id>/key` endpoint is now deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See Trusted Access and Embed Components Using JavaScript and Trusted Access. |
| The `DELETE /api/sources/remove/<id>` endpoint is now deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See Trusted Access and Embed Components Using JavaScript and Trusted Access. |
| The `GET /api/sources/key` endpoint is now deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See Trusted Access and Embed Components Using JavaScript and Trusted Access. |
| The `/api/screenshot/*` endpoint and `/api/screenshot-management` endpoint are deprecated and will be removed in a future release. |
| The `GET /oauth/authorize` endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access API Endpoints. |
| The `/oauth2/client` endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access API Endpoints. |
| The `/oauth2/token` endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access API Endpoints. |
| The following fields in the response payload of the `GET /api/visuals` endpoint are deprecated and will be removed in a future release.   * `enabled` * `ownerType` * `name` (use `visualName` instead) * `dashboardLinks` (this field is now defined and stored in the new dashboard API response payload) |
| The following fields in the response payload of all other `/api/visuals` endpoints are deprecated and will be removed in a future release.   * `enabled` * `ownerType` * `lastModified` (use `lastModifiedDate` instead) * `ownerSourceId` (use `source.sourceId` instead) * `name` (use `visualName` instead) * `dashboardLinks` ((this field is now defined and stored in the new dashboard API response payload) |
| Data Sources | The **Enabled** column on the Sources page of the UI is deprecated and will be removed in a future release. You can no longer disable data source configuration definitions, so when the column is removed, all disabled data sources will automatically be enabled. If you do not want the data sources disabled, you should delete them. You can control access to a data source configuration using data source permissions, as well as row and column data source restrictions. |
| The import and export JSON definition functions for data source configurations are deprecated and will be removed in a future release. Plans are underway to replace this functionality with an improved option in a future release. |
| Dashboards | The import and export JSON definition functions for dashboard configurations are deprecated and will be removed in a future release. Plans are underway to replace this functionality with an improved option in a future release. |
| OAuth Security | The OAuth Authentication Service is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access. |
| Security Keys | Security keys are deprecated in this release and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See Trusted Access. |
| Older Dashboard Embed Structure | Support for the iFrameless dashboard embed structure used in Composer 5.9 and older versions is deprecated in this release and will be removed in a future release. Use the new embed structure and methodology documented in Embed Components Into Your Application instead. |

| Title | Description |
| --- | --- |
| **6.8 Deprecated Features** | |
| API | The `/api/export/generate/rawdata` endpoint is deprecated and will be removed in a future release. Use `/api/export/csv/raw` instead. |
| Custom Chart CLI | The following custom chart CLI libraries are deprecated: `nvd3.multiline.js`, `fabric.js`, `require/require.js`. |

| Title | Description |
| --- | --- |
| **6.7 Deprecated Features** | |
| Embedded Dashboards | The `mode` property of the `createComponent` Javascript method used when embedding dashboards is deprecated. Use dashboard interactivity instead. See Control How Users Interact With a Dashboard. |

| Title | Description |
| --- | --- |
| **6.6 Deprecated Features** | |
| None. | |

| Title | Description |
| --- | --- |
| **6.5 Deprecated Features** | |
| JavaScript properties | The `application.banner` and `application.logo` JavaScript properties are deprecated. See Supported Embedded Dashboard Properties and Objects. |

| Title | Description |
| --- | --- |
| **6.4 Deprecated Features** | |
| None. | |

| Title | Description |
| --- | --- |
| **6.3 Deprecated Features** | |
| None. | |

| Title | Description |
| --- | --- |
| **6.2 Deprecated Features** | |
| API | The `sources` field in the `/api/groups` endpoint is deprecated and will be removed in a future release. |
| The `configType` field in the `/api/groups` endpoint is deprecated and will be removed in a future release. |

| Title | Description |
| --- | --- |
| **6.1 Deprecated Features** | |
| None. | |

| Title | Description |
| --- | --- |
| **6.0 Deprecated Features** | |
| Properties | The `server.multiple-context-path.primary` and `server.multiple-context-path.secondary` properties in the `zoomdata.properties` file are deprecated. This release does not support multiple context paths. |
| API | You can no longer use `<hostname>:8080/zoomdata/api/version`. Use `<hostname>:8080/composer/api/version` instead. |

| Title | Description |
| --- | --- |
| **5.9.1 Deprecated Features** | |
| API | The `/api/security/attributes` endpoint is replaced with the new `/api/sources/<source-id>/security/attributes` endpoint, used for column security. |
| The `/api/filters` endpoint is replaced with the new `/api/sources/<source-id>/security/filters` endpoint, used for row security. |
| The `/api/dashboards/<dashboard-id>/key` endpoint. When removed, you will no longer be able to share a dashboard by generating a public link. |

| Title | Description |
| --- | --- |
| **5.9 Deprecated Features** | |
| Authorization | The UI privilege **Can Share Visuals & Dashboards** (API privilege ROLE\_SHARE\_DASHBOARDS) associated with sharing a dashboard via a dashboard link is renamed **Can Generate Dashboard Public Link** (same API privilege), but is officially deprecated in release 5.9. |

#### Removed Features

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **6.9 Removed Features** | |
| API | The `GET /api/visdefs/<sourceid>/<visid>` API endpoint is now removed from the product. It was deprecated in a previous release. |
| The `PUT /api/visdefs/<sourceid>/<visid>` API endpoint is now removed from the product. It was deprecated in a previous release. |
| The `POST /api/visdefs/<sourceid>/<visid>` API endpoint is now removed from the product. It was deprecated in a previous release. |
| The `DELETE /api/visdefs/<sourceid>/<visid>` API endpoint is now removed from the product. It was deprecated in a previous release. |
| The `GET /api/visdefs/<sourceid>`API endpoint is now removed from the product. It was deprecated in a previous release. |
| The `POST /api/visdefs/default/<sourceid>/<visid>` API endpoint is now removed from the product. |
| The `PUT /api/visdefs/default/<sourceid>/<visid>` API endpoint is now removed from the product. |
| Licensing | In support of the new license structure, the following license properties have been removed from the `api/license`endpoint response: `type` and `enforcementLevel`. |
| Context Variables | The `${User.zoomdataUserName}` context variable is removed from the product. You can no longer use this variable in new connection, data source, or forced filter definitions. Existing definitions that use this context variable will continue to work. For new definitions, use the `${User.composerUserName}` context variable instead. |
| **6.8 Removed Features** | |
| None. | |
| **6.7 Removed Features** | |
| None. | |
| **6.6 Removed Features** | |
| None. | |
| **6.5 Removed Features** | |
| None. | |
| **6.4 Removed Features** | |
| Fields | * `com.zoomdata.resource.GroupAclResource#bookmarks` * `com.zoomdata.resource.GroupAclResource#connections` * `com.zoomdata.resource.InventoryItemResource#ownerFullName` * `com.zoomdata.resource.InventoryItemResource#ownerUserId` * `com.zoomdata.resource.dashboard.DashboardResource#userId` * `com.zoomdata.resource.dashboard.DashboardResource#shareState` * `com.zoomdata.resource.dashboard.DashboardResource#ownerName` |
| Sorting Option | The `com.zoomdata.web.controller.InventoryController.SortableField#OWNER` sorting option that relied on the OWNER field that was deprecated in 5.9 is removed from the code. |
| Authorization | The API privilege ROLE\_SAVE\_DASHBOARDS, deprecated in 5.9, is removed from the code. Use ROLE\_CREATE\_DASHBOARDS instead. All existing groups that had the ROLE\_SAVE\_DASHBOARDS privilege granted are automatically migrated to ROLE\_CREATE\_DASHBOARDS. However, if your organization has integrated Composer API calls into third-party software, you will need to manually change all references of ROLE\_SAVE\_DASHBOARDS to ROLE\_CREATE\_DASHBOARDS. See Group Privilege Reference. |
| API | The `visualizations` container in the response from a GET or PATCH `/api/sources/<id>` request was deprecated in 5.9 and support for it is removed from the Composer code. |
| **6.3 Removed Features** | |
| Linux | CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead. |
| Red Hat Linux 6 and Scientific Linux are no longer supported. |
| JSON | The `Content-Type` header `vnd.zoomdata.v2+json` is no longer supported in version 6.3 and later and can no longer be used as the `Content-Type` for API routes. It is removed from the product. Use `vnd.composer.v2+json` as the `Content-Type` for API routes instead. |
| Group Definitions | As a result of the introduction of data source permissions in version 6.3, the ability to restrict data sources within group definitions is removed. Use data source permissions instead. For information about data source permissions, see About Data Source Permissions. |
| Custom Chart CLI | Support for Version 3 of the custom chart CLI is now removed because it only supported Zoomdata version 3 and earlier and support for those Zoomdata versions is dropped. Use version 4 or the new version 5 of the custom chart CLI instead. See Supported Custom Chart CLI Versions. |
| Authorization | The API privileges ROLE\_DELETE\_ALL\_SOURCES, ROLE\_MANAGE\_ALL\_SOURCES, ROLE\_VIEW\_ALL\_SOURCES, and ROLE\_MANAGE\_SOME\_SOURCES are removed from the product. When you upgrade, groups with these roles will be automatically upgraded with new source privilege settings as follows:   * Groups with the ROLE\_VIEW\_ALL\_SOURCES privilege are automatically granted read permissions for all data sources. * Groups with the ROLE\_MANAGE\_ALL\_SOURCES privilege are automatically granted write permissions for all data sources. * Groups with the ROLE\_DELETE\_ALL\_SOURCES privilege are automatically granted delete permissions for all data sources. |
| **6.2 Removed Features** | |
| API | The `accountId` parameter, which was deprecated in Composer 5.9, has now been removed from the following API endpoints:   * `GET /api/actions` * `DELETE /api/actions/{id}` * `POST /api/actions/{id}/invoke` * `GET /api/dashboards/export` * `GET /api/groups` * `GET /api/inventory` * `GET /api/sources/name/{name}` * `GET /api/sources` * `POST /api/upload/{sourceId}` * `DELETE /api/upload/{sourceId}` * `GET /api/preferences` * `GET /api/users` * `GET /api/visuals` |
| Authorization | The supplied **View All** group, which was officially deprecated in Composer 5.9, has now been removed from *new* installations of the product.  If you are upgrading to this release, the description provided for the **View All** group has changed, indicating that the group is no longer a default system group and no longer gives users implicit read-only permissions to all sources in the account. Pre-existing data sources will still be accessible for **View All** group members, but new data sources will not. |
| **6.1 Removed Features** | |
| **None.** | |
| **6.0 Removed Features** | |
| **None.** | |
