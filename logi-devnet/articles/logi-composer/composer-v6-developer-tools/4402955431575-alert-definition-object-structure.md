---
title: "Alert Definition Object Structure"
id: 4402955431575
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955431575-Alert-Definition-Object-Structure
updated_at: 2021-08-07T17:29:15Z
---

# Alert Definition Object Structure

# Alert Definition Object Structure

Alert definitions are created by submitting a `POST api/alerts` endpoint with a request body that uses the object structure defined here.

![](https://devnet.logianalytics.com/hc/article_attachments/4404952805911/criticalicon.gif) This is an experimental feature.

Here is a sample of the general object structure required to create an alert definition:

```
{
  "name": "React on high sales prices",
  "description": "We have a price > $1000",
  "enabled": true,
  "schedule": { ... },
  "condition": { ... },
  "notification": { ... }
}
```

Each object in this structure is described below.

| Object | Specifies |
| --- | --- |
| `name` | The name of the alert definition. |
| `description` | A description of the alert definition. |
| `enabled` | Whether or not the definition is enabled. A value of `true` indicates that it is enabled; `false` indicates that it is not. If an alert is not enabled, it is not scheduled at all. |
| `schedule` | The frequency by which the alert condition in the definition should be evaluated. Valid values are `ONCE`, `MONTHLY`, `WEEKLY`, and `DAILY`. Each of these values requires additional fields to more specifically identify when the alert condition should be evaluated:   * `frequency`: Specify `ONCE`, `MONTHLY`, `WEEKLY`, or `DAILY`. Each of these values requires additional fields to more specifically identify when the alert condition should be evaluated:    + `ONCE` requires that fields `startDate` and `timeOfDay` be specified.   + `MONTHLY` requires that fields `startDate`, `endDate`, `dayOfMonth`, and `timeOfDay` be specified.   + `WEEKLY` requires that fields `startDate`, `endDate`, `dayOfWeek`, and `timeOfDay` be specified.   + `DAILY` requires that fields `startDate`, `endDate`, and `timeOfDay` be specified. * `startDate`: specify the starting date, in `yyyy-mm-dd` format, at which the alert condition should be evaluated. * `timeOfDay`: specify the time of day, in `hh:mm:ss` format, at which the alert condition should be evaluated. * `endDate`: specify the ending date, in yyyy-mm-dd format, at which the alert condition should be evaluated. * `dayOfMonth`: specify the day of the month, using values from 1 through 31, at which the alert should be evaluated. * `dayOfWeek`: specify the day of the month, using values Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday, at which the alert should be evaluated.   Here is an example:   ``` {    ...      "schedule": {    "frequency": "ONCE",    "timeOfDay": "12:30:00",    "startDate": "2021-05-14",    "endDate": "2021-05-14"    }    ... } ``` |
| `condition` | The alert condition that should be evaluated. The alert condition requires the following fields:   * `sourceId`: identifies the data source used for the condition query * `dataQuery`: a VisQuery object for a raw, KPI, single group by, or multigroup by data query using simple and aggregate filters to define the condition. Data query structures and filters are described in detail in [*Alert Definition Data Query Structures*](https://devnet.logianalytics.com/hc/en-us/articles/4402955429655-Alert-Definition-Data-Query-Structures). * `activateAlertWhenData`: Indicates when the alert should be activated. Valid values are `EXISTS` or `NOT_EXISTS`. When `EXISTS` is specified, the data query must determine that data exists to trigger the alert. When `NOT_EXISTS` is specified, the data query must determine that data does not exists to trigger the alert. |
| `notification` | The notification information for the alert.The notification structure is fully described in detail in [*Alert Definition Notification Structure*](https://devnet.logianalytics.com/hc/en-us/articles/4402955430935-Alert-Definition-Notification-Structure). It includes a notification type (only `EMAIL` is currently supported), a subject for the email message, text for the body of the email message, and recipient information. |

See [*Alert Definition Examples*](https://devnet.logianalytics.com/hc/en-us/articles/4402955430295-Alert-Definition-Examples) for complete examples of some alert definitions.
