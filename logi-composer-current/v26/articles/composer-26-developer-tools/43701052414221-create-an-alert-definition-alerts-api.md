---
title: "Create an Alert Definition - Alerts API"
id: 43701052414221
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701052414221-Create-an-Alert-Definition-Alerts-API
updated_at: 2026-05-29T14:07:09Z
---

# Create an Alert Definition - Alerts API

# Create an Alert Definition - Alerts API

Use alerts to alert yourself and other users when a metric reaches a specified threshold. Use the Logi Composer alerts endpoints to create alert definitions. These definitions describe an alert condition, determine a schedule to evaluate the alert condition, and how notifications are handled when an alert condition is met. See [Create an Alert Definition](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036492941-Create-an-Alert-Definition) to create alerts using the Logi Composer UI.

Use the endpoint `/api/alerts` to manage (list, create, update, and delete) alert definitions.

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/alerts/{id}` | GET | Returns a specific alert definition, identified by its ID. In a multi tenancy environment, respects Recipients rules. |
| `/api/alerts/{id}` | PUT | Updates a specific alert definition, identified by its ID. Completely replaces the previous version of the alert definition. |
| `/api/alerts/{id}` | DELETE | Deletes a specific alert definition, identified by its ID. |
| `/api/alerts/{id}` | PATCH | Patches a specific alert definition, identified by its ID. |
| `/api/alerts` | GET | Returns all alert definitions. |
| `/api/alerts` | POST | Creates a new alert. This endpoint requires the ROLE\_CREATE\_ALERT privilege. |
| `/api/alerts/{id}/evaluate-condition` | POST | Evaluates an alert condition in a specific alert definition. |

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.
