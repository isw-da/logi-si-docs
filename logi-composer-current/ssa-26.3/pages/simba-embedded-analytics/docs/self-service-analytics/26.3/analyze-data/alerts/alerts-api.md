> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Alerts API

Alerts allow you to alert your end users when a metric reaches a specified threshold. Alerts API endpoints can be used to create, update, and delete alert definitions, each describing an alert condition, the schedule by which it is evaluated, and how notification is handled when the alert condition is met.

API support for alerting is performed using the REST API endpoint `/api/alerts`, as described below.

| Endpoint | Method | Description |
| - | - | - |
| `/api/alerts/{id}` | GET | Returns a specific alert definition, identified by its ID. In a multi tenancy environment, respects Recipients rules. |
| `/api/alerts/{id}` | PUT | Updates a specific alert definition, identified by its ID. Completely replaces the previous version of the alert definition. |
| `/api/alerts/{id}` | DELETE | Deletes a specific alert definition, identified by its ID. |
| `/api/alerts/{id}` | PATCH | Patches a specific alert definition, identified by its ID. |
| `/api/alerts` | GET | Returns all alert definitions. |
| `/api/alerts` | POST | Creates a new alert. This endpoint requires the ROLE\_CREATE\_ALERT privilege. |
| `/api/alerts/{id}/evaluate-condition` | POST | Evaluates an alert condition in a specific alert definition. |

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<h2 id="create-an-alert-definition-alerts-api">
  Create an Alert Definition - Alerts API
</h2>

Use alerts to alert yourself and other users when a metric reaches a specified threshold. Use the alerts endpoints to create alert definitions. These definitions describe an alert condition, determine a schedule to evaluate the alert condition, and how notifications are handled when an alert condition is met. See [Create an Alert Definition](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/alerts/alerts-ov#create-an-alert-definition) to create alerts using the User Interface.

Use the endpoint `/api/alerts` to manage (list, create, update, and delete) alert definitions.

| Endpoint | Method | Description |
| - | - | - |
| `/api/alerts/{id}` | GET | Returns a specific alert definition, identified by its ID. In a multi tenancy environment, respects Recipients rules. |
| `/api/alerts/{id}` | PUT | Updates a specific alert definition, identified by its ID. Completely replaces the previous version of the alert definition. |
| `/api/alerts/{id}` | DELETE | Deletes a specific alert definition, identified by its ID. |
| `/api/alerts/{id}` | PATCH | Patches a specific alert definition, identified by its ID. |
| `/api/alerts` | GET | Returns all alert definitions. |
| `/api/alerts` | POST | Creates a new alert. This endpoint requires the ROLE\_CREATE\_ALERT privilege. |
| `/api/alerts/{id}/evaluate-condition` | POST | Evaluates an alert condition in a specific alert definition. |

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

## Alert Definition Object Structure

Alert definitions are created by submitting a `POST api/alerts` endpoint with a request body that uses the object structure defined here.

Here is a sample of the general object structure required to create an alert definition:

```json theme={null}
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

<table>
  <thead>
    <tr>
      <th>Object</th>
      <th>Specifies</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>The name of the alert definition.</td>
    </tr>

    <tr>
      <td>`description`</td>
      <td>A description of the alert definition.</td>
    </tr>

    <tr>
      <td>`enabled`</td>
      <td>Whether or not the definition is enabled. A value of `true` indicates that it is enabled; `false` indicates that it is not. If an alert is not enabled, it is not scheduled at all.</td>
    </tr>

    <tr>
      <td>`schedule`</td>

      <td>
        The frequency by which the alert condition in the definition should be evaluated. Valid values are `ONCE`, `MONTHLY`, `WEEKLY`, and `DAILY`. Each of these values requires additional fields to more specifically identify when the alert condition should be evaluated:

        <br />

        * `frequency`: Specify `ONCE`, `MONTHLY`, `WEEKLY`, or `DAILY`. Each of these values requires additional fields to more specifically identify when the alert condition should be evaluated:

        <br />

        * `ONCE` requires that fields `startDate` and `timeOfDay` be specified.
        * `MONTHLY` requires that fields `startDate`, `endDate`, `dayOfMonth`, and `timeOfDay` be specified.
        * `WEEKLY` requires that fields `startDate`, `endDate`, `dayOfWeek`, and `timeOfDay` be specified.
        * `DAILY` requires that fields `startDate`, `endDate`, and `timeOfDay` be specified.

        <br />

        * `startDate`: specify the starting date, in `yyyy-mm-dd` format, at which the alert condition should be evaluated.

        <br />

        * `timeOfDay`: specify the time of day, in `hh:mm:ss` format, at which the alert condition should be evaluated.

        <br />

        * `endDate`: specify the ending date, in yyyy-mm-dd format, at which the alert condition should be evaluated.

        <br />

        * `dayOfMonth`: specify the day of the month, using values from 1 through 31, at which the alert should be evaluated.

        <br />

        * `dayOfWeek`: specify the day of the month, using values Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday, at which the alert should be evaluated.

        <br />

        Example:

        <br />

        ```json theme={null}
        {
           ...
           "schedule": {
           "frequency": "ONCE",
           "timeOfDay": "12:30:00",
           "startDate": "2021-05-14",
           "endDate": "2021-05-14"
           }
           ...
        }
        ```
      </td>
    </tr>

    <tr>
      <td>`condition`</td>

      <td>
        The alert condition that should be evaluated. The alert condition requires the following fields:

        <br />

        * `sourceId`: identifies the data source used for the condition query
        * `dataQuery`: a VisQuery object for a raw, KPI, single group by, or multigroup by data query using simple and aggregate filters to define the condition. Data query structures and filters are described in detail in [Alert Definition Data Query Structures](#alert-definition-data-query-structures).
        * `activateAlertWhenData`: Indicates when the alert should be activated. Valid values are `EXISTS` or `NOT_EXISTS`. When `EXISTS` is specified, the data query must determine that data exists to trigger the alert. When `NOT_EXISTS` is specified, the data query must determine that data does not exists to trigger the alert.
      </td>
    </tr>

    <tr>
      <td>`notification`</td>
      <td>The notification information for the alert. The notification structure is fully described in detail in [Alert Definition Notification Structure](#alert-definition-notification-structure). It includes a notification type (only `EMAIL` is currently supported), a subject for the email message, text for the body of the email message, and recipient information.</td>
    </tr>
  </tbody>
</table>

See [Alert Definition Examples](#alert-definition-examples) for complete examples of some alert definitions.

<h2 id="alert-definition-data-query-structures">
  Alert Definition Data Query Structures
</h2>

The data query used in an alert definition always specifies a filter condition to be evaluated. Different kinds of data query conditions can be specified: raw, KPI, single group by, or multigroup by queries. Simple filters and aggregate filters are used to establish these query conditions.

This section describes and provides examples for the filter structure and the structures for all query types.

* [Simple Filters](#simple-filters)
* [Aggregate Filters](#aggregate-filters)
* [Raw Data Query Conditions](#raw-data-query-conditions)
* [KPI Data Query Conditions](#kpi-data-query-conditions)
* [Single Group By Queries](#single-group-by-queries)
* [Multigroup By Queries](#multigroup-by-queries)

<h3 id="simple-filters">
  Simple Filters
</h3>

<Note>
  Because alert conditions are checked periodically, filter conditions must be set properly, especially if the queried data is limited to a dynamic timeframe.
</Note>

Filters are specified using the following structure. The example specifies a dynamic filter that looks for sales records with sale dates that occurred in the last month.

```
"filters": [
   {
      "operation": "BETWEEN",
      "path": {
         "name": "sale_date"
      },
      "value": [
         "$start_of_month_-1_month",
         "$end_of_month_-1_month"
      ]
   }
],
```

The following parameters are included in the filter structure.

| Parameter | Specifies |
| - | - |
| `operation` | The filter operation. |
| `path` | The field in the data source that should be evaluated. Use the `name` field to specify the field name. |
| `value` | The values or range of values for the filter. |

<h3 id="aggregate-filters">
  Aggregate Filters
</h3>

Aggregate filters define thresholds using the `aggregateFilters` object in the following structure. Usually a single threshold is defined, but more complex aggregate filters can be specified. The following aggregate filter example searches for groups (for example, product categories) with 1 to 1000 sales records in which the sum of the sales price fell between \$2 and \$700,000.

```javascript theme={null}
"aggregateFilters": [
   {
      "metric": {
         "type": "COUNT"
       },
      "operation": "BETWEEN",
      "value": [
         1,
         1000
      ]
   },
   {
      "metric": {
         "type": "FIELD",
         "field": {
            "name": "price"
         },
         "function": "SUM"
      },
      "operation": "BETWEEN",
      "value": [
         2,
         700000
      ]
   }
],
```

The following parameters are included in the `aggregateFilters` query structure.

| Parameter | Specifies |
| - | - |
| `metric` | The type of metric. |
| `operation` | The filter operation. |
| `value` | The values or range of values for the filter. |

<h3 id="raw-data-query-conditions">
  Raw Data Query Conditions
</h3>

A raw data query condition supports only simple filters. The following sample raw query condition searches for sales records with sale dates that occurred in the last month and with prices that equal or exceed \$1,000,000.00. When records are found meeting these conditions, and alert notification is sent.

```json theme={null}
{
   ...
   "condition": {
      "sourceId": "<rts-source-id>",
      "dataQuery": {
         "queryType": "RAW",
         "filters": [
            {
               "operation": "BETWEEN",
               "path": {
                  "name": "sale_date"
               },
               "value": [
                  "$start_of_month_-1_month",
                  "$end_of_month_-1_month"
               ]
            },
            {
               "path": {
                  "name": "price"
               },
               "operation": "GE",
               "value": 1000000
            }
         ]
      },
      "activateAlertWhenData": "EXISTS"
   }
}
```

The following parameters are included in the raw data query structure.

| Parameter | Specifies |
| - | - |
| `queryType` | The type of query. For raw data query conditions, this is always `RAW`. The other possible value for this parameter (but not for raw query conditions) is `AGGREGATE`. |
| `filters` | The [filter conditions](#simple-filters) for the raw data query. |

<h3 id="kpi-data-query-conditions">
  KPI Data Query Conditions
</h3>

A KPI query condition is a single-dimension query, without aggregations. Filters can be used to reduce the data to be evaluated. The threshold is defined by aggregate filters.

The following sample KPI query condition searches for sales records from the state of Alabama with sale dates that occurred in the last month and with total planned sales between \$1 and \$3,035.00. If no records can be found that meet these conditions, an alert notification is sent.

```json theme={null}
{
   ...
   "condition": {
      "sourceId": "<rts-source-id>",
      "dataQuery": {
         "queryType": "AGGREGATE",
         "filters": [
            {
               "operation": "BETWEEN",
               "path": {
                  "name": "sale_date"
               },
               "value": [
                  "$start_of_month_-1_month",
                  "$end_of_month_-1_month"
               ]
            },
            {
               "path": {
                  "name": "state"
               },
               "operation": "EQ",
               "value": "Alabama"
            }
         ],
         "dimensions": [
            {
               "aggregations": []
            }
         ],
         "aggregateFilters": [
            {
               "metric": {
                  "type": "FIELD",
                  "field": {
                     "name": "plannedsales"
                  },
                  "function": "SUM"
               },
               "operation": "BETWEEN",
               "value": [
                  1.00,
                  3035.00
               ]
            }
         ]
      },
      "activateAlertWhenData": "NOT_EXISTS"
   }
}
```

The following parameters are included in the KPI data query structure.

| Parameter | Specifies |
| - | - |
| `queryType` | The type of query. For KPI data query conditions, this is always `AGGREGATE`. The other possible value for this parameter (but not for KPI query conditions) is `RAW`. |
| `filters` | The [filter conditions](#simple-filters) for the KPI data query. |
| `dimensions` | The aggregation type (`TERM` or `TIME`). No aggregation type is supported for KPI data query conditions. |
| `aggregateFilters` | The [threshold conditions](#aggregate-filters) for the KPI data query. |

<h3 id="single-group-by-queries">
  Single Group By Queries
</h3>

Single group by queries are similar to KPI data queries, but add one aggregation. Filters can be used to reduce the data to be evaluated. The threshold is defined by aggregate filters. The window attribute may be defined for the dimension section. But it does not affect the query execution logic.

The following sample single group by query condition searches for sales records from the state of Alabama, aggregated by product group, with sale dates that occurred in the last month and with total planned sales between \$1 and \$3,035.00. If no records can be found that meet these conditions, an alert notification is sent.

```json theme={null}
{
   ...
   "condition": {
      "sourceId": "<rts-source-id>",
      "dataQuery": {
         "queryType": "AGGREGATE",
         "filters": [
            {
               "operation": "BETWEEN",
               "path": {
                  "name": "sale_date"
               },
               "value": [
                  "$start_of_month_-1_month",
                  "$end_of_month_-1_month"
               ]
            },
            {
               "path": {
                  "name": "state"
               },
               "operation": "EQ",
               "value": "Alabama"
            }
         ],
         "dimensions": [
            {
               "aggregations": [
                  {
                  "type": "TERMS",
                  "field": {
                     "name": "product_group"
                  }
               }
            ]
         }
      ],
      "aggregateFilters": [
         {
            "metric": {
               "type": "FIELD",
               "field": {
                  "name": "planned_sales"
               },
               "function": "SUM"
            },
            "operation": "BETWEEN",
            "value": [
               1.00,
               3035.00
            ]
         }
      ]
   },
   "activateAlertWhenData": "NOT_EXISTS"
   }
}
```

The following parameters are included in the single group data query structure.

| Parameter | Specifies |
| - | - |
| `queryType` | The type of query. For single group by data query conditions, this is always `AGGREGATE`. The other possible value for this parameter (but not for single group by query conditions) is `RAW`. |
| `filters` | The [filter conditions](#simple-filters) for the single group by data query. |
| `dimensions` | The aggregation type (`TERM` or `TIME`). Both `TERM` and `TIME` aggregations are supported. However, time aggregations cannot request the **Include Blanks** function. |
| `aggregateFilters` | The [threshold conditions](#aggregate-filters) for the single group by data query. |

<h3 id="multigroup-by-queries">
  Multigroup By Queries
</h3>

Multigroup by queries are the same as Single Group By queries, except that they allow for more than one aggregation.

<Note>
  Top of the Top sorting is not supported; only simple sorting is supported. We recommend that no sorting be specified at all.
</Note>

The following sample multigroup by query condition searches for sales records from the state of Alabama, aggregated by sales day and city, with sale dates that occurred in the last month and with total planned sales between \$1 and \$1.050.00. If records can be found that meet these conditions, an alert notification is sent.

```json theme={null}
{
   ...
   "condition": {
   "sourceId": "<rts-source-id>",
   "dataQuery": {
      "queryType": "AGGREGATE",
      "filters": [
         {
            "operation": "BETWEEN",
            "path": {
               "name": "sale_date"
            },
            "value": [
               "$start_of_month_-1_month",
               "$end_of_month_-1_month"
            ]
         },
         {
            "path": {
               "name": "state"
            },
            "operation": "EQ",
            "value": "Alabama"
         }
      ],
      "dimensions": [
         {
            "aggregations": [
               {
                  "type": "TERMS",
                  "field": {
                     "name": "user_city"
                  }
               },
               {
                  "type": "TIME",
                  "field": {
                     "name": "saledate"
                  },
                  "granularity": "DAY"
               }
            ]
         }
      ],
      "aggregateFilters": [
         {
            "metric": {
               "type": "FIELD",
               "field": {
                  "name": "planned_sales"
               },
               "function": "SUM"
            },
            "operation": "BETWEEN",
            "value": [
               1000.00,
               1050.00
            ]
         }
      ]
   },
   "activateAlertWhenData": "EXISTS"
   }
}
```

The following parameters are included in the multigroup by data query structure.

| Parameter | Specifies |
| - | - |
| `queryType` | The type of query. For multigroup by data query conditions, this is always `AGGREGATE`. The other possible value for this parameter (but not for multigroup by query conditions) is `RAW`. |
| `filters` | The [filter conditions](#simple-filters) for multigroup by data query. |
| `dimensions` | The aggregation type (`TERM` or `TIME`). Both `TERM` and `TIME` aggregations are supported. However, time aggregations cannot request the **Include Blanks** function. |
| `aggregateFilters` | The [threshold conditions](#aggregate-filters) for the multigroup by data query. |

<h2 id="alert-definition-notification-structure">
  Alert Definition Notification Structure
</h2>

Here is a sample of the general object structure for the notification object of an alert definition:

```json theme={null}
{
   ...
   "notification": {
      "notificationType": "EMAIL",
      "subject": "RTS: High price",
      "body": "We have a price > $1000",
      "recipients": {
         "users": [
            {
               "id": "user-1",
               "name": "User 1"
            },
            {
               "id": "user-2",
               "name": "User 2"
            }
         ],
         "sendToMe": false
      }
   }
}
```

Each parameter in this structure is described below.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Specifies</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`notificationType`</td>
      <td>The notification type. Currently only `EMAIL` is supported.</td>
    </tr>

    <tr>
      <td>`subject`</td>
      <td>The subject of the notification email.</td>
    </tr>

    <tr>
      <td>`body`</td>
      <td>The body text of the notification email.</td>
    </tr>

    <tr>
      <td>`recipients`</td>

      <td>
        The users who should be notified. Users must be defined in your environment and all user definitions must have email addresses provided in their user definition. See [Add Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#add-users).

        <br />

        Use the following field pairs to define the recipients for the alert notification:

        <br />

        * `id`: The Self-Service Analytics user ID (the user ID). This is the only required field (unless the `sendToMe` field is set to `true`). Self-Service Analytics automatically returns the user full name.
        * `name`: The user's login name. This is not required.

        <br />

        Repeat user field pairs, as needed, to alert more than one person.
      </td>
    </tr>

    <tr>
      <td>`sendtoMe`</td>

      <td>
        Whether or not the alert notifications should be sent to the author of the alert definition. Specify `true` (send notifications to the author) or `false` (do not send notifications to the author).

        <br />

        <Note>
          You can elect to send alert notifications only to the author of the alert definition. To do this, eliminate the field pairs in the recipients list and replace it with `sendToMe` set to `true`.
        </Note>
      </td>
    </tr>
  </tbody>
</table>

See [Alert Definition Examples](#alert-definition-examples) for complete examples of some alert definitions.

<h2 id="alert-definition-examples">
  Alert Definition Examples
</h2>

Two complete examples of an alert definition in JSON format are provided in this section. One uses a raw data query and the other uses a single-group query with dynamic time.

### Raw Data Query Example

This example produces an alert when the sales price exceeds \$1000. The alert notification is sent to the author of the alert definition.

```json theme={null}
{
   "name": "React on high sales prices",
   "description": "We have a price > $1000",
   "enabled": true,
   "schedule": {
      "frequency": "ONCE",
      "timeOfDay": "12:30:00",
      "startDate": "2021-05-14",
      "endDate": "2021-05-14"
   },
   "condition": {
      "sourceId": "<rts-source-id>",
      "dataQuery": {
         "queryType": "RAW",
         "filters": [
            {
               "path": {
                  "name": "price"
               },
               "operation": "GE",
               "value": 1000
            }
         ]
      },
      "activateAlertWhenData": "EXISTS"
   },
   "notification": {
      "notificationType": "EMAIL",
      "subject": "RTS: High price",
      "body": "We have a price > $1000",
      "recipients": {
         "sendToMe": true
      }
   }
}
```

<h3 id="single-group-query-example">
  Single-Group Query Example
</h3>

This example produces an alert when sales numbers exceed \$100,000 in selected states during the last hour of collected data. The alert notification is sent to author of the alert definition.

```json theme={null}
{
   "name": "Some State has > $100,000 sales (during last hour)",
   "description": "Celebrate good sales",
   "enabled": true,
   "schedule": {
      "frequency": "ONCE",
      "timeOfDay": "12:30:00",
      "startDate": "2021-05-14",
      "endDate": "2021-05-14"
   },
   "condition": {
      "sourceId": "<rts-source-id>",
      "dataQuery": {
         "queryType": "AGGREGATE",
         "dimensions": [
            {
               "aggregations": [
                  {
                     "type": "TERMS",
                     "field": {
                        "name": "userstate"
                     }
                  }
               ]
            }
         ],
         "filters": [
            {
               "operation": "BETWEEN",
               "path": {
                  "name": "ts"
               },
               "value": [
                  "$end_of_data_-1_hour",
                  "$end_of_data"
               ]
            }
         ],
         "aggregateFilters": [
            {
               "metric": {
                  "type": "FIELD",
                  "field": {
                     "name": "price"
                  },
               "function": "SUM"
            },
            "operation": "GT",
            "value": 100000
         }
      ]
   },
   "activateAlertWhenData": "EXISTS"
 },
 "notification": {
   "notificationType": "EMAIL",
   "subject": "Some State has > $100,000 sales (during last hour)",
   "body": "Wow!",|
   "recipients": {
      "sendToMe": true
    }
  }
}
```
