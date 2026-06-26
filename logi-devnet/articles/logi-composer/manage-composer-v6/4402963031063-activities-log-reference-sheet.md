---
title: "Activities Log Reference Sheet"
id: 4402963031063
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963031063-Activities-Log-Reference-Sheet
updated_at: 2021-08-07T17:31:39Z
---

# Activities Log Reference Sheet

# Activities Log Reference Sheet

This reference sheet lists the types of activities and corresponding fields that are logged in the Composer activity log. By default, activity logging is enabled with a few exceptions (described later in this topic).

## Activity Logging Defaults

The following table lists the activities that are logged by default and those that are not. Activities that are not logged by default must have logging manually enabled. See [*Activity Logging*](https://devnet.logianalytics.com/hc/en-us/articles/4402963014679-Activity-Logging).

| Activity Log File | Activities Logged by Default | Activity Not Logged by Default |
| --- | --- | --- |
| `zoomdata-activity.log` | [account](#ACCOUNT:) [authentication](#AUTHENTI) [group](#GROUP:) [security\_key](#SECURITY) [SOURCE](#SOURCE:) [USER](#USER:) [VIS](#VIS:) [VIS\_DEF](#VIS_DEF:) | [oauth\_client](#OAUTH_CL) [oauth\_token](#OAUTH_TO) [raw\_data\_export](#RAW_DATA) [raw\_data\_export\_csv](#RAW_DATA2) [upload](#UPLOAD:) |

If logging or specific activity logging is disabled in a previous version, the disabled status is retained
after an upgrade.

## Common Log Fields

For each activity, the following common fields are logged as part of each activity record:

| Field Name | Description |
| --- | --- |
| user | contains information about the account user and the actions performed |
| userType | contains information about the way the user has accessed Composer, either via: (1) security key (for shared visuals, value=KEY) or (2) user credentials (value=USER |
| accountID | contains the user's current account ID |
| userGroups | list of the groups to which the user belongs |
| IP | contains IP address from which the event has been performed |

Additional fields are logged as part of each [activity](#Activity).

## Activity Log Fields

The following activity types can be logged by Composer. For each activity, specific fields are logged, in addition to the [common fields](#Common).

* [*account: Account Maintenance*](#ACCOUNT:)
* [*authentication: User Authentication*](#AUTHENTI)
* [*group: Group Maintenance*](#GROUP:)
* [*oauth\_client: OAuth Client Registry Maintenance*](#OAUTH_CL)
* [*oauth\_token: OAuth Access Token Processing*](#OAUTH_TO)
* [*raw\_data\_export: Text Search*](#RAW_DATA)
* [*raw\_data\_export\_csv: Data Export to CSV*](#RAW_DATA2)
* [*security\_key: Security Key Usage*](#SECURITY)
* [*source: Data Source Maintenance*](#SOURCE:)
* [*upload: Flat File Upload*](#UPLOAD:)
* [*user: User Account Maintenance*](#USER:)
* [*vis: Visual Maintenance*](#VIS:)
* [*vis\_def: Visual Label Maintenance*](#VIS_DEF:)

### `account`: Account Maintenance

This activity is logged when a Composer account is created, updated, or deleted. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

| Field Name | Description |
| --- | --- |
| activityType | account |
| status | CREATED / UPDATED / DELETED |
| accountId | Generated account ID |
| name | Name of the account from which the event has been triggered. |
| createdBy | User who created this account. |
| createdDate | Account creating date |
| lastModifiedBy | User who modified the account |
| disabled | TRUE / FALSE |

### `authentication`: User Authentication

This activity is logged while user authentication at login. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

|
|  |
| Field | Value |
| --- | --- |
| activityType | authentication |
| status | SUCCEEDED / FAILED |
| authenticationType | BASE, SAML, LDAP, OAUTH, x509 |

### `group`: Group Maintenance

This activity is logged when a user group is created, updated, or updated. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

|
|  |
| Field | Value |
| --- | --- |
| activityType | group |
| status | CREATED / UPDATED / DELETED |
| groupId | Group ID |
| label | Name of the group |
| description | Group description added by the user |
| groupRoles | Privileges that have been assigned for the group |

### `oauth_client`: OAuth Client Registry Maintenance

Logs the actions taken from the OAuth client application registry - whether records are created, updated or deleted. Logging for this activity is disabled by default. After you have manually enabled logging for this activity, its log records are captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

| Field | Value |
| --- | --- |
| activityType | oauth\_client |
| status | CREATED / UPDATED / DELETED |
| clientId |  |
| clientName |  |
| autoApprove |  |

### `oauth_token`: OAuth Access Token Processing

Tracks when OAuth access tokens are granted (or created) or deleted. Logging for this activity is disabled by default. After you have manually enabled logging for this activity, its log records are captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

| Field | Value |
| --- | --- |
| activityType | oauth\_token |
| status | CREATED / DELETED |
| tokenId |  |
| clientId |  |
| tokenUsername |  |
| tokenAccountID |  |

### `raw_data_export`: Text Search

This activity is logged when a text search (applicable only for Elasticsearch, Apache Solr, and Cloudera Search sources) is performed using the `/api/stream/search` endpoint. Logging for this activity is disabled by default. After you have manually enabled logging for this activity, its log records are captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

|
|  |
| Field | Value |
| --- | --- |
| activityType | raw\_data\_export |
| status | SUCCEEDED |
| exportType | REST (view details) FILE (export file) |
| count | Number of exported rows |
| storageType | Data source |
| query | Queries sent to the data source |
| cid | Created ID |
| actionStartedOn | Export start time |
| duration | Request processing time |

### `raw_data_export_csv`: Data Export to CSV

This activity is logged when a user exports the raw data to a
CSV
file. Logging for this activity is disabled by default. After you have manually enabled logging for this activity, its log records are captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

|
|  |
| Field | Value |
| --- | --- |
| activityType | raw\_data\_export\_csv |
| status | SUCCEEDED |
| count | Number of exported rows |
| location | DB or FILE |
| file | location=FILE - the full path to the file in local file system |
| cid | Created ID |
| actionStartedOn | Export start time |
| duration | Request processing time |

### `security_key`: Security Key Usage

This activity is logged while working with security key.
A security key is created when a user chooses to share a dashboard and the interactive or non interactive link is created. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

| Field | Value |
| --- | --- |
| activityType | security\_key |
| status | CREATED / UPDATED / DELETED |
| keyId | ID of the generated key |
| created | Security key creation date |
| expire | Security key expiration date |
| description | Description added by the user |
| keyType | SOURCE / DASHBOARD |
| objectIds | *IDs of sources and dashboards which are allowed with this key* |

### `source`: Data Source Maintenance

This activity is logged when a source is created, updated, or deleted. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

|
|  |
| Field | Value |
| --- | --- |
| activityType | source |
| status | SAVED, UPDATED, DELETED |
| sourceId | Generated source ID |
| sourceName | Name of the source |
| streamType | Demo\_record, CSV, API |
| storageType | Data source type |
| sourceAsString | Contains microservice info about the data source |
| sourceDescription | Source description added by the user |

### `upload`: Flat File Upload

This activity is logged when a user uploads the flat file while creating a new data source. Logging for this activity is disabled by default. After you have manually enabled logging for this activity, its log records are captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

|
|  |
| Field | Value |
| --- | --- |
| activityType | upload |
| status | SUCCEEDED |
| source | Data source ID to which the file will be uploaded |
| fileName | Name of the uploaded file |
| contentType | Type of the uploaded file |
| filesize | Size of the uploaded file |

### `user`: User Account Maintenance

This activity is logged when user account is created, updated, assigned to or removed from a group, or deleted. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

| Field | Value |
| --- | --- |
| activityType | user |
| status | CREATED / UPDATED / DELETED |
| userID |  |
| userName |  |
| userFullname |  |
| email |  |
| subjectUserGroups | Groups which a user belongs to |
| userOrigin | NATIVE / SAML / LDAP |
| accounts | Accounts, which a user is assigned to |

### `vis`: Visual Maintenance

This activity is logged when a visual is created or updated. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

|
|  |
| Field | Value |
| --- | --- |
| activityType | vis |
| status | CREATED / UPDATED |
| visualizationID |  |
| visualizationName |  |

### `vis_def`: Visual Label Maintenance

This activity is logged when a user is creating or updating the visual label. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

|
|  |
| Field | Value |
| --- | --- |
| activityType | vis\_def |
| status | CREATED / UPDATED |
| cid | Created ID |
| visualizationId | Unique identifier for the visual |
| visualizationName | Name assigned to the visual |
