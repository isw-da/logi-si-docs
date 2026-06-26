---
title: "Alert Definition Notification Structure"
id: 4405850875415
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850875415-Alert-Definition-Notification-Structure
updated_at: 2021-09-21T01:26:40Z
---

# Alert Definition Notification Structure

# Alert Definition Notification Structure

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) This is an experimental feature.

Here is a sample of the general object structure for the notification object of an alert definition:

```
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

| Parameter | Specifies |
| --- | --- |
| `notificationType` | The notification type. Currently only `EMAIL` is supported. |
| `subject` | The subject of the notification email. |
| `body` | The body text of the notification email. |
| `recipients` | The users who should be notified. Users must be defined to Composer and all user definitions must have email addresses provided in their user definition. See [*Add User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850861463-Add-User-Definitions).  Use the following field pairs to define the recipients for the alert notification:   * `id`: The Composer user ID (the user ID). This is the only required field (unless the `sendToMe` field is set to `true`). Composer automatically returns the user full name. * `name`: The user's login name. This is not required.   Repeat user field pairs, as needed, to alert more than one person. |
| `sendtoMe` | Whether or not the alert notifications should be sent to the author of the alert definition. Specify `true` (send notifications to the author) or `false` (do not send notifications to the author).  You can elect to send alert notifications only to the author of the alert definition. To do this, eliminate the field pairs in the recipients list and replace it with `sendToMe` set to `true`. |

See [*Alert Definition Examples*](https://devnet.logianalytics.com/hc/en-us/articles/4405850874519-Alert-Definition-Examples) for complete examples of some alert definitions.
