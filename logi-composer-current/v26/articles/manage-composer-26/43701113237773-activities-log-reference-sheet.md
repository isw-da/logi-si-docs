---
title: "Activities Log Reference Sheet"
id: 43701113237773
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113237773-Activities-Log-Reference-Sheet
updated_at: 2026-05-29T14:09:11Z
---

# Activities Log Reference Sheet

# Activities Log Reference Sheet

This reference sheet lists the types of activities and corresponding fields that are logged in the Composer activity log. By default, activity logging is enabled with a few exceptions (described later in this topic).

## Activity Logging Defaults

The following table lists the activities that are logged by default and those that are not. Activities that are not logged by default must have logging manually enabled. See [Activity Logging](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701106334605-Activity-Logging).

**Important:** 
Activity logging in `zoomdata-activity.log` is deprecated and will be removed in a future release.
Information previously captured in `zoomdata-activity.log` can be found in other log files such as `access.log`, `service.log`, and by using Composer's [User Auditing](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701124523021-User-Auditing) feature.

| Activity Log File | Activities Logged by Default | Activity Not Logged by Default |
| --- | --- | --- |
| `zoomdata-activity.log` | [account](#ACCOUNT:) [authentication](#AUTHENTI) [group](#GROUP:) [SOURCE](#SOURCE:) [USER](#USER:) [VIS](#VIS:) | [raw\_data\_export](#RAW_DATA) [raw\_data\_export\_csv](#RAW_DATA2) [upload](#UPLOAD:) |

If logging or specific activity logging is disabled in a previous version, the disabled status is retained
after an upgrade.

## Common Log Fields

For each activity, the following common fields are logged as part of each activity record:

| Field Name | Description |
| --- | --- |
| user | contains information about the tenant user and the actions performed |
| accountID | contains the user's current tenant ID |
| userGroups | list of the groups to which the user belongs |
| IP | contains IP address from which the event has been performed |

Additional fields are logged as part of each [activity](#Activity).

## Activity Log Fields

The following activity types can be logged by Composer. For each activity, specific fields are logged, in addition to the [common fields](#Common).

* [account: Account Maintenance](#ACCOUNT:)
* [authentication: User Authentication](#AUTHENTI)
* [group: Group Maintenance](#GROUP:)
* [raw\_data\_export: Text Search](#RAW_DATA)
* [raw\_data\_export\_csv: Data Export to CSV](#RAW_DATA2)
* [source: Data Source Maintenance](#SOURCE:)
* [upload: Flat File Upload](#UPLOAD:)
* [user: User Account Maintenance](#USER:)
* [vis: Visual Maintenance](#VIS:)

### `account`: Account Maintenance

This activity is logged when a Composer tenant account is created, updated, or deleted. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

| Field Name | Description |
| --- | --- |
| activityType | account |
| status | CREATED / UPDATED / DELETED |
| accountId | Generated tenant account ID |
| name | Name of the tenant account from which the event has been triggered |
| createdBy | User who created this tenant account. |
| createdDate | Tenant account creation date |
| lastModifiedBy | User who modified the tenant account |
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
| authenticationType | BASE, SAML, LDAP, x.509 |

### `group`: Group Maintenance

This activity is logged when a user group is created, updated, or updated. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

|
|  |
| Field | Value |
| --- | --- |
| groupId | Group ID |
| label | Name of the group |
| description | Group description added by the user |
| group | Privileges that have been assigned for the group |

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
| accounts | Tenant a ccounts, which a user is assigned to |

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
