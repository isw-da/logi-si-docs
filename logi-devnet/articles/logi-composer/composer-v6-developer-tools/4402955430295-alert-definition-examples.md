---
title: "Alert Definition Examples"
id: 4402955430295
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955430295-Alert-Definition-Examples
updated_at: 2021-08-07T17:29:14Z
---

# Alert Definition Examples

# Alert Definition Examples

Two complete examples of alert definition JSON are provided in this section. One uses a raw data query and the other uses a single-group query with dynamic time.

![](https://devnet.logianalytics.com/hc/article_attachments/4404952805911/criticalicon.gif) This is an experimental feature.

## Raw Data Query Example

This example produces an alert when the sales price exceeds $1000. The alert notification is sent to the author of the alert definition.

```
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

## Single-Group Query Example

This example produces an alert when sales numbers exceed $100,000 in selected states during the last hour of collected data. The alert notification is sent to author of the alert definition.

```
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
