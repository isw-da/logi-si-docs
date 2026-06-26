---
title: "Themes API\u00a0Endpoint"
id: 4405851184407
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851184407-Themes-API-Endpoint
updated_at: 2021-09-21T01:29:40Z
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

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) Some API endpoints are marked as “experimental” in the Swagger documentation we provide. These endpoints are in the early stages of design and are subject to change. In addition, Logi Analytics makes no commitment to their stability and may remove them without notice. These experimental endpoints are not recommended for use in production.
