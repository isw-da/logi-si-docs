# Logi Composer Rest API, endpoint index across two instances

346 distinct operations across 76 tags, from two separate Composer
instances rather than one. Every row is marked with where it was actually observed.

| key | instance | spec file | paths | operations |
|---|---|---|---|---|
| `B` | SI-bundled 26.2.1, pulled live 2026-08-27 | `composer-openapi-26.2.1-bundled.json` | 223 | 344 |
| `H` | hosted simba.logisymphony.com, pulled 2026-06-26 | `composer-openapi-simba-logisymphony.json` | 220 | 338 |

Present on both: **336**. Only on the bundled instance: **8**. Only on the hosted one: **2**.

**Why this is a union and not a replacement.** The two specs disagree, so a single file
would have to pick one and silently drop the other's endpoints. An OpenAPI document
describes the instance that served it, not the product: each declares its own origin in
`servers[0].url`. Treat a `B`-only or `H`-only row as conditional on deployment shape,
and confirm against the instance in front of you before promising it to anyone.

`composer-openapi.json` is kept as a stable filename for existing tooling and currently
points at the bundled 26.2.1 pull, which is the newer of the two and the only one
verified against a running instance by this project.

## connections (13)

- `GET /api/connections` — Returns a list of connections
- `POST /api/connections` — Create connection (requires the ROLE_MANAGE_CONNECTIONS privilege)
- `GET /api/connections/statistics` — Load connection statistics
- `POST /api/connections/validate` — Validate connection (requires the ROLE_MANAGE_CONNECTIONS privilege)
- `DELETE /api/connections/{connectionId}` — Delete connection (requires the ROLE_MANAGE_CONNECTIONS privilege)
- `GET /api/connections/{connectionId}` — Load connection
- `PUT /api/connections/{connectionId}` — Update or create connection (requires the ROLE_MANAGE_CONNECTIONS privilege)
- `GET /api/connections/{connectionId}/objects` — Returns a list of connection objects
- `POST /api/connections/{connectionId}/preview` — Preview data available over provided connection
- `GET /api/connections/{connectionId}/schema` — Returns a list of connection schemas
- `GET /api/connections/{connectionId}/schema/compact` — Returns compacted JSON schemas for connection **[H only]**
- `PUT /api/connections/{connectionId}/schema/{schemaName}/configuration` — Updates or creates a connection schema configuration
- `GET /api/connections/{connectionId}/schema/{schemaName}/describe` — Returns a schema definition for provided schema name

## sources / fields (13)

- `GET /api/sources/{sourceId}/fields` — Returns a list of fields for the source
- `POST /api/sources/{sourceId}/fields` — Creates a data source field
- `PUT /api/sources/{sourceId}/fields` — Updates a data source fields (requires WRITE permission to the source)
- `POST /api/sources/{sourceId}/fields/statistics/refresh` — Refreshes all source fields statistics
- `POST /api/sources/{sourceId}/fields/validate` — Validates a source field
- `DELETE /api/sources/{sourceId}/fields/{fieldName}` — Deletes a data source field by name
- `GET /api/sources/{sourceId}/fields/{fieldName}` — Returns a data source field by name
- `PATCH /api/sources/{sourceId}/fields/{fieldName}` — Updates data source field visibility
- `PUT /api/sources/{sourceId}/fields/{fieldName}` — Updates or creates a data source field
- `GET /api/sources/{sourceId}/fields/{fieldName}/statistics/distinct-values` — Returns source field distinct values
- `POST /api/sources/{sourceId}/fields/{fieldName}/statistics/refresh` — Refreshes single source field statistics
- `GET /api/sources/{sourceId}/fields/{fieldName}/statistics/total` — Returns source field total statistics
- `GET /api/sources/{sourceId}/fields/{fieldName}/usage` — Returns source field usages

## sources (12)

- `GET /api/sources` — Returns a list of the sources
- `POST /api/sources` — Creates a new source
- `POST /api/sources/ai-enhancer` — Validates and resolves source parameters for visual creation **[H only]**
- `GET /api/sources/statistics` — Load sources statistics
- `DELETE /api/sources/{id}/cache` — Deletes cached statistics and visuals data for specified datasource
- `DELETE /api/sources/{sourceId}` — Deletes a source
- `GET /api/sources/{sourceId}` — Returns a data source by id
- `PUT /api/sources/{sourceId}` — Updates or creates a source
- `POST /api/sources/{sourceId}/clone` — Clone a source
- `GET /api/sources/{sourceId}/expression-syntax` — Returns functions and operators for a given source
- `GET /api/sources/{sourceId}/features` — Returns a list of features for the data source
- `POST /api/v2/sources` — Creates a new source

## connection-types (11)

- `GET /api/connection/types` — Returns a list of connection types
- `POST /api/connection/types` — Create new Connection Type
- `DELETE /api/connection/types/icon/{fileName}` — Delete Connection Type Icon by file name
- `GET /api/connection/types/icon/{fileName}` — Retrieve Connection Type Icon by file name
- `POST /api/connection/types/icon/{fileName}` — Create new Connection Type icon
- `DELETE /api/connection/types/{id}` — Delete specific Connection Type by Id
- `GET /api/connection/types/{id}` — Retrieve specific Connection Type by Id
- `PATCH /api/connection/types/{id}` — Update properties of a specific Connection Type by Id
- `PUT /api/connection/types/{id}` — Update specific Connection Type by Id
- `GET /api/connection/types/{id}/accounts` — Retrieve Connection Type accounts
- `PUT /api/connection/types/{id}/accounts` — Update Connection Type accounts. Empty list - available to all accounts

## visual-types (10)

- `GET /api/visual-types` — Returns a list of Visual Types
- `POST /api/visual-types` — Create Visual Type
- `GET /api/visual-types/components/{componentId}` — Produce wrapped body output for visual type
- `GET /api/visual-types/export/{visTypeId}` — Export Visual Type
- `POST /api/visual-types/import` — Import Visual Type
- `POST /api/visual-types/thumbnail` — Upload Visual Type thumbnail
- `DELETE /api/visual-types/{id}` — Delete Visual Type
- `GET /api/visual-types/{id}` — Get Visual Type by id
- `PUT /api/visual-types/{id}` — Update Visual Type
- `GET /api/visual-types/{visTypeId}/thumbnail/{thumbnailId}` — Load thumbnail object

## connectors (9)

- `GET /api/connectors` — Returns a list of connectors
- `POST /api/connectors` — Create a new Connector
- `DELETE /api/connectors/{id}` — Delete a connector with a specific id
- `GET /api/connectors/{id}` — Retrieve a Connector with a specific id
- `PUT /api/connectors/{id}` — Update a Connector with a specific id
- `GET /api/connectors/{id}/status` — Retrieve the status of a Connector with a specific id
- `GET /api/connectors/{id}/storage-types` — Returns a list of storage type descriptions
- `GET /api/connectors/{id}/storage-types/{storagetype}` — Retrieve a Storage Type Descriptions with a specific storage type and id
- `GET /api/connectors/{id}/storage-types/{storagetype}/icon` — Retrieve the Storage Icon with a specific storage type and id

## customization (9)

- `GET /api/customization/themes` — Returns a list of themes
- `POST /api/customization/themes` — Create theme
- `POST /api/customization/themes/activate` — Set active theme
- `GET /api/customization/themes/active` — Get active theme
- `GET /api/customization/themes/name/{name}` — Get by name
- `DELETE /api/customization/themes/{id}` — Delete theme
- `GET /api/customization/themes/{id}` — Read theme
- `PATCH /api/customization/themes/{id}` — Patch theme
- `PUT /api/customization/themes/{id}` — Update theme

## dashboards (9)

- `GET /api/dashboards` — Returns a list of acceptable dashboards (requires READ permission to the dashboards)
- `POST /api/dashboards` — Creates a new dashboard (requires the ROLE_CREATE_DASHBOARDS privilege)
- `GET /api/dashboards/sources` — Returns a list of brief info of sources
- `GET /api/dashboards/sources/{sourceId}/fields` — Returns a list of brief info for all source fields associated with a source
- `GET /api/dashboards/statistics` — Load dashboards statistics
- `DELETE /api/dashboards/{id}` — Deletes a dashboard (requires DELETE permission to the dashboard)
- `GET /api/dashboards/{id}` — Loads a dashboard (requires READ permission to the dashboard)
- `PUT /api/dashboards/{id}` — Updates a dashboard (requires WRITE permission to the dashboard) or creates a new dashboard with custom id (requires the ROLE_CREATE_DASHBOARDS privilege)
- `PATCH /api/dashboards/{id}/author` — Updates a dashboard author details (requires admin privileges to tenant)

## export (9)

- `POST /api/export/chartdata/{file_name}` — (deprecated since 23.1, to be removed in 24.1)Export chart data in CSV or JSON format. If "data" field is empty, data is requested from data accumulator using cid provided.
- `POST /api/export/csv/raw` — (deprecated since 23.1, to be removed in 24.1)Download raw data CSV file by a StartVis message.
- `POST /api/export/rawdataforvisual` — Export raw data for visual in CSV, JSON or XLSX format.
- `POST /api/export/rawdataforvisual/bulk` — Bulk export raw data for visual in XLSX format.
- `POST /api/export/rawdataforvisual/{id}` — Export raw data for visual in CSV, JSON or XLSX format, using Visual-Id
- `POST /api/export/visualdata` — Export visual data in CSV, JSON or XLSX format.
- `POST /api/export/visualdata/bulk` — Bulk export visual data in XLSX format.
- `POST /api/export/visualdata/enriched` — Export visual data in XLSX format with full formatting applied. **[B only]**
- `POST /api/export/visualdata/{id}` — Export visual data in CSV, JSON or XLSX format, using Visual-Id

## permissions (9)

- `GET /api/dashboards/{dashboardId}/acls` — Retrieve a list of Security Identities (groups, users, account) with their permissions on the dashboard
- `PATCH /api/dashboards/{dashboardId}/acls/bulk` — Grant/revoke permissions on the dashboard to/from a list of Security Identities (groups, users, account)
- `PUT /api/dashboards/{dashboardId}/acls/bulk` — Assign permissions on the dashboard to a list of Security Identities (groups, users, account)
- `GET /api/sources/{sourceId}/acls` — Retrieve a list of Security Identities (groups, users, account) with their permissions on the source
- `PATCH /api/sources/{sourceId}/acls/bulk` — Grant/revoke permissions on the source to/from a list of Security Identities (groups, users, account)
- `PUT /api/sources/{sourceId}/acls/bulk` — Assign permissions on the source to a list of Security Identities (groups, users, account)
- `GET /api/visuals/{id}/acls` — Retrieve a list of Security Identities (groups, users, account) with their permissions on the visual
- `PATCH /api/visuals/{id}/acls/bulk` — Grant/revoke permissions on the visual to/from a list of Security Identities (groups, users, account)
- `PUT /api/visuals/{id}/acls/bulk` — Assign permissions on the visual to a list of Security Identities (groups, users, account)

## uploads (9)

- `GET /api/uploads` — Returns a list of uploads
- `POST /api/uploads` — Creates an upload
- `POST /api/uploads/preview` — Returns data preview of the provided file
- `DELETE /api/uploads/{id}` — Deletes an upload
- `GET /api/uploads/{id}` — Returns an upload by id
- `PUT /api/uploads/{id}` — Updates uploads
- `DELETE /api/uploads/{id}/data` — Deletes upload data
- `POST /api/uploads/{id}/data` — Appends data to the upload
- `PUT /api/uploads/{id}/data` — Replaces upload data

## sources / security / fields (8)

- `GET /api/sources/{sourceId}/security/attributes` — Returns a list of security attribute settings
- `POST /api/sources/{sourceId}/security/attributes` — Create SecurityAttributeSetting
- `DELETE /api/sources/{sourceId}/security/attributes/{id}` — Delete SecurityAttributeSetting
- `PUT /api/sources/{sourceId}/security/attributes/{id}` — Update SecurityAttributeSetting
- `GET /api/sources/{sourceId}/security/fields` — Returns a list of security attribute settings
- `POST /api/sources/{sourceId}/security/fields` — Create SecurityAttributeSetting
- `DELETE /api/sources/{sourceId}/security/fields/{id}` — Delete SecurityAttributeSetting
- `PUT /api/sources/{sourceId}/security/fields/{id}` — Update SecurityAttributeSetting

## user (8)

- `GET /api/user` — Current user information
- `POST /api/user/initUsers` — Initialize Default Users
- `POST /api/user/interpolate` — Interpolate a value with user attributes
- `GET /api/user/permissions/dashboards/{dashboardId}` — Retrieve currently logged-in user's access level and permissions to a dashboard
- `GET /api/user/permissions/sources` — Returns a list of permissions for sources by current user
- `GET /api/user/permissions/sources/{sourceId}` — Retrieve currently logged-in user's permissions to a source
- `GET /api/user/permissions/visuals/{visualId}` — (experimental) Retrieve currently logged-in user's permissions to a visual
- `GET /api/user/switch/{accountId}` — (deprecated since 5.9, to be removed in 7.X) Switch user accounts.Account switch via logout/login to be introduced

## users (8)

- `GET /api/users` — Returns a list of users
- `POST /api/users` — Create user
- `GET /api/users/autocomplete` — Searches for user names by a fragment of their name, email or full name
- `PATCH /api/users/current` — Patch user, only showQuickstart are supported at this moment
- `POST /api/users/password` — Change user's password
- `DELETE /api/users/{id}` — Delete user
- `GET /api/users/{id}` — Load user
- `PUT /api/users/{id}` — Update user

## visuals (8)

- `POST /api/v2/visuals` — Create Custom Visual
- `GET /api/visuals` — Returns list of visuals
- `POST /api/visuals` — Create a new visual (requires the CREATE_VISUALS privilege)
- `POST /api/visuals/name/usage` — Show if visual name is used by TOP level visual or not
- `GET /api/visuals/statistics` — Load visuals statistics
- `DELETE /api/visuals/{id}` — Deletes a visual (requires DELETE permission to the visual)
- `GET /api/visuals/{id}` — Retrieve a visual (requires READ permission to the visual)
- `PUT /api/visuals/{id}` — Updates a visual (requires WRITE permission to the visual) or creates a new visual with custom id (requires the ROLE_CREATE_VISUALS privilege)

## accounts (7)

- `GET /api/accounts` — Returns a list of accounts
- `POST /api/accounts` — Create account
- `GET /api/accounts/multitenant` — Returns boolean based on application multi-tenant configuration
- `GET /api/accounts/name/{name}` — Load account by name
- `DELETE /api/accounts/{id}` — Delete account
- `GET /api/accounts/{id}` — Load account
- `PUT /api/accounts/{id}` — Update or create account

## alerts (7)

- `GET /api/alerts` — Return all alerts
- `POST /api/alerts` — Create a new alert (requires the ROLE_CREATE_ALERTS privilege)
- `DELETE /api/alerts/{id}` — Delete the existing alert
- `GET /api/alerts/{id}` — Return an alert by id
- `PATCH /api/alerts/{id}` — Patch the existing alert (modify selected attributes)
- `PUT /api/alerts/{id}` — Update the existing alert (completely replace the previous version)
- `POST /api/alerts/{id}/evaluate-condition` — Evaluate alert condition

## branding (7)

- `GET /api/branding` — Get branding configuration
- `POST /api/branding` — Update branding configuration
- `PUT /api/branding` — Update branding configuration
- `GET /api/branding/images/{imageName}` — Load branding image
- `GET /api/branding/{fileName}` — Load branding file
- `POST /api/branding/{fileName}` — Upload file for branding
- `DELETE /api/branding/{filename}` — Delete branding file

## data-gateway-client (7)

- `GET /api/data-gateway/clients` — Return all Data Gateway clients **[B only]**
- `POST /api/data-gateway/clients` — Create a Data Gateway client **[B only]**
- `POST /api/data-gateway/clients/authenticate` — Authenticate a Data Gateway client **[B only]**
- `DELETE /api/data-gateway/clients/{id}` — Delete a Data Gateway client **[B only]**
- `GET /api/data-gateway/clients/{id}` — Return a Data Gateway client **[B only]**
- `PATCH /api/data-gateway/clients/{id}` — Update a Data Gateway client **[B only]**
- `POST /api/data-gateway/clients/{id}/reset-secret` — Reset a Data Gateway client's secret **[B only]**

## sources / custom-metrics (7)

- `GET /api/sources/{sourceId}/custom-metrics` — Returns a list of custom metrics for the source
- `POST /api/sources/{sourceId}/custom-metrics` — Creates a data source custom metric
- `POST /api/sources/{sourceId}/custom-metrics/validate` — Validates a custom metric
- `DELETE /api/sources/{sourceId}/custom-metrics/{customMetricName}` — Deletes a custom metric
- `PATCH /api/sources/{sourceId}/custom-metrics/{customMetricName}` — Updates custom metric visibility
- `PUT /api/sources/{sourceId}/custom-metrics/{customMetricName}` — Updates existing custom metric or creates a new one if custom metric with {customMetricName} doesn't exist
- `GET /api/sources/{sourceId}/custom-metrics/{name}` — Retrieve a custom metric by its source and name

## calendars (6)

- `GET /api/calendars` — (experimental) Returns a list of calendars
- `POST /api/calendars` — (experimental) Create calendar
- `DELETE /api/calendars/{calendarId}` — (experimental) Delete calendar by id
- `GET /api/calendars/{calendarId}` — (experimental) Load calendar by its id
- `PUT /api/calendars/{calendarId}` — (experimental) Update calendar
- `GET /api/calendars/{calendarId}/periods` — (experimental) Get list of a calendar time periods

## groups (6)

- `GET /api/groups` — Returns a list of groups
- `POST /api/groups` — Create group
- `PUT /api/groups` — Update or create group
- `GET /api/groups/autocomplete` — Searches for group names by a fragment of their label
- `DELETE /api/groups/{id}` — Delete a group
- `GET /api/groups/{id}` — Load group ACL

## keyset (6)

- `GET /api/keysets` — Returns a list of keysets
- `POST /api/keysets/upload` — (experimental) Create keyset from uploaded data as CSV body. CSV should not contain header
- `PUT /api/keysets/upload/{keySetId}` — (experimental) Update keyset from uploaded data as CSV body. CSV should not contain header
- `DELETE /api/keysets/{keySetId}` — Delete keyset
- `GET /api/keysets/{keySetId}` — Retrieve keyset
- `GET /api/keysets/{keySetId}/values` — Retrieve keyset values

## materialized-view (6)

- `GET /api/materialized-views` — (deprecated since 23.1)Returns a list of materialized views
- `POST /api/materialized-views` — (deprecated since 23.1)Create Materialized view
- `DELETE /api/materialized-views/{id}` — (deprecated since 23.1)Delete Materialized view.
- `GET /api/materialized-views/{id}` — (deprecated since 23.1)Get Materialized view by id.
- `PATCH /api/materialized-views/{id}` — (deprecated since 23.1)Update only specific properties (name, description, enabled) of a Materialized view.
- `PUT /api/materialized-views/{id}` — (deprecated since 23.1)Update Materialized view

## sources / dictionaries (6)

- `DELETE /api/sources/{sourceId}/dictionaries` — Delete all source dictionaries
- `GET /api/sources/{sourceId}/dictionaries` — Returns a list of source dictionaries
- `PUT /api/sources/{sourceId}/dictionaries` — Bulk create or update from file with replace all source dictionaries
- `DELETE /api/sources/{sourceId}/dictionaries/{language}` — Delete source dictionary by language
- `GET /api/sources/{sourceId}/dictionaries/{language}` — Read source dictionary by language
- `PUT /api/sources/{sourceId}/dictionaries/{language}` — Create or update source dictionary by language

## actions (5)

- `GET /api/actions` — Returns a list of action templates
- `POST /api/actions` — Create a new Action Template
- `DELETE /api/actions/{id}` — Delete an Action Template
- `PUT /api/actions/{id}` — Update an existing Action Template
- `POST /api/actions/{id}/invoke` — Invoke an action from an Action Template

## comments (5)

- `GET /api/dashboards/{dashboardId}/comments` — Returns a list of dashboard comments
- `POST /api/dashboards/{dashboardId}/comments` — Create related dashboard comment
- `DELETE /api/dashboards/{dashboardId}/comments/{commentId}` — Delete related dashboard comment
- `GET /api/dashboards/{dashboardId}/comments/{commentId}` — Get related dashboard comment
- `PUT /api/dashboards/{dashboardId}/comments/{commentId}` — Update related dashboard comment

## dashboard-reports (5)

- `GET /api/dashboards/{dashboardId}/reports` — Retrieve dashboard report settings by dashboard ID
- `POST /api/dashboards/{dashboardId}/reports` — Create dashboard report settings
- `DELETE /api/dashboards/{dashboardId}/reports/{reportId}` — Delete dashboard report settings
- `GET /api/dashboards/{dashboardId}/reports/{reportId}` — Retrieve dashboard report settings by report ID
- `PUT /api/dashboards/{dashboardId}/reports/{reportId}` — Update dashboard report settings

## dashboard-sharing (5)

- `PATCH /api/dashboards/{dashboardId}/permissions` — (experimental) Share/revoke access level on the dashboard
- `GET /api/dashboards/{id}/account-permissions` — Retrieve a list of Accounts Security Identities with their access level on the dashboard
- `GET /api/dashboards/{id}/all-permissions` — Retrieve a list of Security Identities (groups, users, account) with their access level on the dashboard
- `GET /api/dashboards/{id}/group-permissions` — Retrieve a list of Groups Security Identities with their access level on the dashboard
- `GET /api/dashboards/{id}/permissions` — Retrieve a list of Users Security Identities with their access level on the dashboard

## filter-sets (5)

- `GET /api/filter-sets` — Returns a list of filter-sets for a source
- `POST /api/filter-sets` — Create filter
- `DELETE /api/filter-sets/{id}` — Delete filter
- `GET /api/filter-sets/{id}` — Get filter
- `PUT /api/filter-sets/{id}` — Update filter

## locale, currency, language (5)

- `GET /api/currencies` — Returns a list of currencies
- `GET /api/languages` — Returns a list of languages
- `GET /api/languages/file` — Get vocabulary json for language
- `GET /api/locales` — Returns a list of locales
- `GET /api/locales/{id}` — Get locale by id

## sources / security / row (5)

- `GET /api/sources/{sourceId}/security/filters` — Returns a list of forced filters for a source
- `POST /api/sources/{sourceId}/security/filters` — Add forced filter
- `DELETE /api/sources/{sourceId}/security/filters/{id}` — Delete forced filter by id
- `PATCH /api/sources/{sourceId}/security/filters/{id}` — Update forced filter partially
- `PUT /api/sources/{sourceId}/security/filters/{id}` — Update forced filter, replacing it completely

## trusted-access-client (5)

- `GET /api/trusted-access/clients` — Return all Trusted Access clients
- `POST /api/trusted-access/clients` — Create a Trusted Access client
- `DELETE /api/trusted-access/clients/{id}` — Delete a Trusted Access client
- `GET /api/trusted-access/clients/{id}` — Return a Trusted Access client
- `PATCH /api/trusted-access/clients/{id}` — Update a Trusted Access client

## interactivity (4)

- `GET /api/dashboards/interactivity` — (experimental) Returns a list of system dashboard interactivity profiles
- `DELETE /api/dashboards/{dashboardId}/interactivity` — (experimental) Delete related dashboard interactivity
- `GET /api/dashboards/{dashboardId}/interactivity` — (experimental) Get related dashboard interactivity
- `PUT /api/dashboards/{dashboardId}/interactivity` — (experimental) Create or update related dashboard interactivity

## jobs (4)

- `GET /api/jobs` — Returns a list of jobs
- `GET /api/jobs/{name}` — Show job
- `GET /api/jobs/{name}/executions` — Returns a list of job executions
- `GET /api/jobs/{name}/executions/{executionId}` — Returns a list of progress reports for the job

## quota (4)

- `PUT /api/quota` — Update or create quota for an account
- `PATCH /api/quota/refresh/{accountId}` — Re evaluate the consumption for the account
- `DELETE /api/quota/{accountId}` — Delete Quota of a account
- `GET /api/quota/{accountId}` — Load Quota

## snippets (4)

- `POST /api/snippets` — (experimental) Creates a new snippet
- `DELETE /api/snippets/{snippetId}` — (experimental) Deletes the snippet
- `GET /api/snippets/{snippetId}` — (experimental) Returns the snippet by ID
- `PUT /api/snippets/{snippetId}` — (experimental) Updates the snippet. Creates a new one if snippet with provided ID does not exist

## sources / security / custom metrics (4)

- `GET /api/sources/{sourceId}/security/custom-metrics` — (experimental) Returns a list of custom metric security settings
- `POST /api/sources/{sourceId}/security/custom-metrics` — (experimental) Create custom metric security setting
- `DELETE /api/sources/{sourceId}/security/custom-metrics/{id}` — (experimental) Delete custom metric security setting
- `PUT /api/sources/{sourceId}/security/custom-metrics/{id}` — (experimental) Update custom metric security setting

## sources / visual-types (4)

- `GET /api/sources/{sourceId}/visual-types` — Returns visual types for the data source
- `PUT /api/sources/{sourceId}/visual-types` — Updates source visual types
- `GET /api/sources/{sourceId}/visual-types/variables-values` — Returns available fields, metrics and aggregations for this source to be used on visual
- `GET /api/sources/{sourceId}/visual-types/{visualTypeId}/initial-visual` — Returns initial visual for the data source

## tags (4)

- `GET /api/tags` — Returns tags present in the account
- `POST /api/tags` — Creates tag in the account
- `DELETE /api/tags/name/{name}` — delete tag in the account
- `DELETE /api/tags/{id}` — delete tag in the account

## toggle (4)

- `GET /api/toggles/{prefix}` — Get variables by prefix
- `DELETE /api/toggles/{prefix}/{key}` — Delete variable by prefix and key
- `GET /api/toggles/{prefix}/{key}` — Get variable by prefix and key
- `PUT /api/toggles/{prefix}/{key}` — Set variable by prefix and key

## users segregation (4)

- `POST /api/users/permissions` — Assign permissions based on a condition used to segregate users of a account into tenants
- `DELETE /api/users/permissions/{sid}` — Delete the conditions for user segregation in the account
- `GET /api/users/permissions/{sid}` — Get the conditions for user segregation in the account
- `PUT /api/users/permissions/{sid}` — Update the conditions for user segregation in the account

## activity (3)

- `GET /api/system/activity/type` — Get a key/value list of supported activity types and their current status
- `GET /api/system/activity/type/{activityType}` — Get the toggle status of a specific activity type
- `PUT /api/system/activity/type/{activityType}` — Update an activity type to toggle its logging

## sources / preview and describe (3)

- `POST /api/sources/data-entities/describe` — Returns the details of all data entity fields
- `POST /api/sources/data-entities/preview` — Returns data preview of the provided data entity
- `POST /api/sources/preview` — Returns data preview of the provided data source

## trusted-access-token (3)

- `POST /api/trusted-access/pull/tokens` — Create an access token using the user information stored in the Composer platform
- `POST /api/trusted-access/push/tokens` — Create an access token using the user information provided in the API request
- `DELETE /api/trusted-access/tokens/{tokenId}` — Revoke the access token

## accounts / admins (2)

- `GET /api/accounts/{accountId}/admins` — Returns a list of account administrators
- `PUT /api/accounts/{accountId}/admins` — Updates account administrators

## accounts / users (2)

- `GET /api/accounts/{accountId}/users` — Returns a list of account members
- `PUT /api/accounts/{accountId}/users` — Updates account members

## branding-extentions (2)

- `GET /api/branding-extensions` — Load branding extensions
- `PUT /api/branding-extensions` — Update branding extensions

## dashboard-migration (2)

- `GET /api/dashboards/export` — Export dashboards [necessary permissions: 'read']
- `POST /api/dashboards/import` — Import dashboards

## favorites (2)

- `POST /api/favorites` — Favorite an object
- `DELETE /api/favorites/{id}` — Unfavorite an object

## global (2)

- `GET /api/security/global` — Get global security config
- `PUT /api/security/global` — Update global security config

## inventory (2)

- `GET /api/inventory` — Returns a list of inventory items (sources, visuals, dashboards or reports)
- `GET /api/inventory/{type}/{id}` — Retrieve an item (Source, Visual, Reports, or Dashboard) by its type and Id

## joins (2)

- `POST /api/joins/metadata` — Creates joins metadata
- `POST /api/joins/suggestions` — Retrieves join suggestions

## license (2)

- `GET /api/license` — Get license information.
- `POST /api/license` — Update license information

## register (2)

- `GET /api/register` — Returns registration form URL
- `POST /api/register` — Submit registration

## self-service-reports (2)

- `POST /api/self-service-reports/export` — Exports Self Service Report
- `GET /api/self-service-reports/statistics` — Load reports statistics

## sources / cache-settings (2)

- `GET /api/sources/{sourceId}/cache-settings` — Returns cache settings for the data source
- `PUT /api/sources/{sourceId}/cache-settings` — Updates cache settings for data source

## sources / global-settings (2)

- `GET /api/sources/{sourceId}/global-settings` — Returns global settings for the data source
- `PUT /api/sources/{sourceId}/global-settings` — Updates global settings for the data source

## sources / migration (2)

- `GET /api/sources/export` — Export sources [necessary export sources permissions: 'read' + ROLE_MANAGE_CONNECTIONS]
- `POST /api/sources/import` — Import sources

## sources / security (2)

- `GET /api/sources/{sourceId}/security` — (experimental) Returns source security settings
- `PUT /api/sources/{sourceId}/security` — (experimental) Updates source security settings

## sources / unique-key (2)

- `GET /api/sources/{sourceId}/unique-key` — Returns unique key for the data source
- `PUT /api/sources/{sourceId}/unique-key` — Updates unique key for the data source

## stream (2)

- `POST /api/stream/search` — Search on visualization
- `GET /api/stream/{sourceId}/facet/{attribute}` — Get facet

## timezones (2)

- `GET /api/timezones` — Returns a list of timezones
- `GET /api/timezones/**` — Retrieve a timezone by zone ID

## trusted-access-session (2)

- `POST /api/trusted-access/sessions` — Create a user session for a given Composer user
- `DELETE /api/trusted-access/sessions/{session}` — Delete a user session

## visuals / migration (2)

- `GET /api/visuals/export` — Export visuals [necessary permissions: 'read' + ROLE_EXPORT_VISUALS]
- `POST /api/visuals/import` — Import visuals

## account-attributes (1)

- `GET /api/account-attributes/reserved` — Lists all supported account attribute keys

## dashboard-conversion (1)

- `POST /api/dashboards/convert-layout` — (experimental) Convert dashboards layout

## frontend / environment variables (1)

- `GET /api/fe/env` — Returns frontend-only environment variables specified by fe.env or FE_ENV property in application.properties, env variables or JVM system properties. Will not be changed in application runtime

## group-membership (1)

- `PATCH /api/group-membership/{id}` — Update Group Users

## odata (1)

- `GET /api/sources/odata/*` — (experimental) The entry point to the Source Data Retrieval OData service.

## recentlyAccessed (1)

- `GET /api/recently-accessed-elements` — Returns a list of recently accessed elements

## security (1)

- `GET /api/security/sids` — Retrieve sids info

## sources / raw data (1)

- `GET /api/sources/{sourceId}/data` — (experimental) Returns raw data for the data source

## start-vis (1)

- `POST /api/start-vis` — Execute an inbound message (start-vis, meta, etc.)

## topics (1)

- `GET /api/topics` — List of topics

## version (1)

- `GET /api/version` — Shows Composer application version
