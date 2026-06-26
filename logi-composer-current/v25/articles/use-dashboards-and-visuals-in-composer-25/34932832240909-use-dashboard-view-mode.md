---
title: "Use Dashboard View Mode"
id: 34932832240909
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932832240909-Use-Dashboard-View-Mode
updated_at: 2026-05-26T22:10:04Z
---

# Use Dashboard View Mode

# Use Dashboard View Mode

Dashboard view mode allows you, as a dashboard owner or editor, to see the same layout and options for dashboards you share with users. Toggle between View and Edit modes using the dashboard view mode icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167924888461)).

See [Share a Dashboard with Users](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932824740749-Share-a-Dashboard-with-Users).

## View Mode

Users with Viewer access can see a shared dashboard and data in visuals at the same level of access you as have for that dashboard. You don't need to grant access to individual visuals and sources. Viewers can navigate and adjust the dashboard and visuals on a temporary basis. Any changes made are discarded when they navigate away from the dashboard.

Toggle into View mode to generally see what your dashboard viewers see. Icons, options, or settings they can't access are disabled or hidden from view. If you are an editor or owner toggled into View mode, any changes you make are temporary as well. When you navigate away from the dashboard or switch back to Edit mode, the temporary changes are discarded.

You can configure your embedded dashboards to hide widgets for unavailable visuals from Viewer users using `hideRestrictedVisuals`. When enabled, available widgets adjust to fit the dashboard, replacing unavailable visuals. If no visuals are available, the dashboard displays a message that no visuals are available.

**Note:** 
Your access and permission levels as a dashboard owner are different from your typical viewer users. The icons and options you see when working in View mode may be different from users with Viewer access.

## Edit Mode

Users with Editor access can see a shared dashboard and data in visuals at the same level of access you have for that dashboard. You don't need to grant access individually to visuals and sources. Editors can adjust the dashboard and visuals, saving changes to the dashboard while in Edit mode.

Dashboards are opened in Edit mode for dashboard owner and editor users. Toggle between Viewer and Edit modes to see generally what your dashboard viewers and editors see. Icons, options, or settings Viewers can't access are disabled or hidden from view..

**Note:** 
Your access and permission levels as a dashboard owner are different from your typical editor users. The icons and options you see when working in Edit mode may be different from users with Editor access.

## Interactivity

When you create or edit a dashboard for your users using Logi Composer, you can also control what options they see and changes they can make by defining appropriate interactivity settings. For both standalone and embedded environments:

* You can define preferred interactivity settings
* Interactivity profile settings are applied

In embedded environments, you can filter dashboards by dashboard tags for your users. See [Embed Composer Components Using JavaScript and Trusted Access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932930219405-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).

See [Control How Users Interact With a Dashboard](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932814650893-Control-How-Users-Interact-With-a-Dashboard).

## Embedded Environments

In embedded environments, dashboards open in Edit mode for all Owners and Editors. Toggle between Viewer and Edit modes to see generally what your dashboard viewers and editors see. Any icons, options, or settings they can't access are disabled or hidden from their view.

You can also define a preferred embed configuration by

* Defining the default mode for Editors
* Enabling or disabling access to interactivity settings for Editors

See [Control How Users Interact With a Dashboard](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932814650893-Control-How-Users-Interact-With-a-Dashboard) and [Editor Configuration (editorUserSettings Property)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932920874253-Interactivity-Properties#Editor).

## Controls Visibility

Controls visibility for dashboards are shown below. If **Hidden**, the visibility can't be overridden. If **Default**, visibility is controlled by the interactivity profile, interactivity overrides, or user permissions.

| Control | View Mode | Edit Mode |
| --- | --- | --- |
| Dashboard Interactivity | Hidden | Default |
| Dashboard Layout | Hidden | Default |
| Changing Layout | Hidden | Default |
| Save | Hidden | Default |
| Add new or Place existing Visuals / Add Snippets | Hidden | Default |
| Dashboard Links | Hidden | Default |
| Cross-Source Links / Cross-Visual Links | Hidden | Default |
| Delete | Hidden | Default |
| Unsaved Changes (Label, Alert) | Hidden | Default |
| Alerts | Default | Default |
| Save As | Default | Default |
| Share Dashboard | Hidden | Default |
| Export | Default | Default |
| Favorite | Default | Default |
| Refresh | Default | Default |
| Schedule | Default | Default |
| Filter | Default | Default |

Controls visibility for widgets are shown below. If **Hidden**, the visibility can't be overridden. If **Default**, visibility is controlled by the interactivity profile, interactivity overrides, or user permissions.

| Control | View Mode | Edit Mode |
| --- | --- | --- |
| Widget Header | Default | Default |
| Widget Pickers | Default | Default |
| Maximize Widget | Default | Default |
| Export Visual Data | Default | Default |
| Export Raw Data | Default | Default |
| Export PDF/PNG | Default | Default |
| Change Widget Settings | Hidden | Default |
| Change Settings for Snippets | Hidden | Default |
| Copy Visual | Hidden | Default |
| Remove Widget | Hidden | Default |
| Add to Visual Gallery | Hidden | Default |
| Convert to Local Visual | Hidden | Default |
| Undo Changes | Default | Default |
| Save as Visual | Default | Default |
| Create Keyset | Hidden | Default |
| Visual Permissions | Hidden | Default |
| Edit Snippet | Hidden | Default |
