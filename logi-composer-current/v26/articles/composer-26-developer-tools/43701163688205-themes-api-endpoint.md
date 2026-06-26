---
title: "Themes API\u00a0Endpoint"
id: 43701163688205
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163688205-Themes-API-Endpoint
updated_at: 2026-05-29T14:09:29Z
---

# Themes API Endpoint

# Themes API Endpoint

The API endpoint used to manage themes is `customization/themes`.

| Endpoint | Method | Description |
| --- | --- | --- |
| `customization/themes` | GET | List all themes. |
| `customization/themes` | POST | Create a theme. |
| `customization/themes/<id>` | GET | Review a specific theme by theme ID. |
| `customization/themes/<id>` | PUT | Update a specific theme. |
| `customization/themes/<id>` | DELETE | Delete a specific theme. |
| `customization/themes/<id>` | PATCH | Patch a specific theme. |
| `customization/themes/activate` | POST | Set the active theme. |
| `customization/themes/active` | GET | List the active theme. |
| `customization/themes/name/<name>` | GET | Review a specific theme by name. |

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

**Important:** 
Some API endpoints are marked as `experimental` in the Swagger documentation we provide. These endpoints are in the early stages of design and are subject to change. We make no commitment to their stability and may remove them without notice. These experimental endpoints are not recommended for use in production.
