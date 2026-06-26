---
title: "Alert Definition Notification Structure"
id: 34932697156877
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932697156877-Alert-Definition-Notification-Structure
updated_at: 2026-05-26T22:06:13Z
---

# Alert Definition Notification Structure

# Alert Definition Notification Structure

Here is a sample of the general object structure for the notification object of an alert definition:

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

Each parameter in this structure is described below.

| Parameter | Specifies |
| --- | --- |
| `notificationType` | The notification type. Currently only `EMAIL` is supported. |
| `subject` | The subject of the notification email. |
| `body` | The body text of the notification email. |
| `recipients` | The users who should be notified. Users must be defined to Logi Composer and all user definitions must have email addresses provided in their user definition. See [Add Users](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932642412173-Add-Users).  Use the following field pairs to define the recipients for the alert notification:   * `id`: The Logi Composer user ID (the user ID). This is the only required field (unless the `sendToMe` field is set to `true`). Logi Composer automatically returns the user full name. * `name`: The user's login name. This is not required.   Repeat user field pairs, as needed, to alert more than one person. |
| `sendtoMe` | Whether or not the alert notifications should be sent to the author of the alert definition. Specify `true` (send notifications to the author) or `false` (do not send notifications to the author).  **Note:**  You can elect to send alert notifications only to the author of the alert definition. To do this, eliminate the field pairs in the recipients list and replace it with `sendToMe` set to `true`. |

See [Alert Definition Examples](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932665812365-Alert-Definition-Examples) for complete examples of some alert definitions.
