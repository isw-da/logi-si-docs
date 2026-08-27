---
title: "Themes and UI Updates"
id: 47077251302669
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077251302669-Themes-and-UI-Updates
updated_at: 2026-08-26T07:08:54Z
---

# Themes and UI Updates

# Themes and UI Updates

Themes provide the color and styling of your analytics software environment. Match your corporate colors, or use one of the default themes included with installation or upgrade.

If you're upgrading to v26.2 or later from an earlier release, the user interface has changed. Roll out this experience in your staging environment, then production environment by [enabling the enhanced-experience](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables) toggle. The enhanced experience expands the classic experience with changes to navigation though the [main menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Main-Menu) and the [home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page).

[Update your existing theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210155405-Themes-JSON-File#JSON%C2%A0Upd) to [include color properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210155405-Themes-JSON-File#JSON%C2%A0Upd) for these new UI elements. If you don't update your classic theme (**composer**, **modern** (light) , **dark**) or any custom theme you've built on these classic themes, the new navigation elements will render unstyled, missing your desired accent colors, or rendering plain black text on a default white background. See [User Interface Interaction With Themes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-User-Interface-Themes#User3).

**Caution:** Update your custom theme and enable the `enhanced-experience` toggle before upgrading past version 26.2. The enhanced homepage and navigation will become the standard experience for all users in the near future. We recommend making these updates now to ensure a smooth transition.

## General Theme Update Workflow

1. Determine your update scenario, as laid out in [Themes and UI Update Scenarios](#Themes).
2. Identify your current theme by sending a `GET` request to the `/api/customization/themes/active` endpoint, then [download the JSON](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210283277-Review-and-Download-the-Theme-JSON-Code#top "download the JSON") of the theme you want to update.
3. Add or edit the [properties of your JSON file](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210155405-Themes-JSON-File). If you are updating a classic theme, see [Expand a Theme to Support the Enhanced Experience](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210155405-Themes-JSON-File#Update). If you are updating a theme that supports the enhanced experience, see [JSON File Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210155405-Themes-JSON-File#JSON).
4. Upload your updated theme. See [Update a Theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701166643213-Update-a-Theme) or [Patch a Theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163854733-Patch-a-Theme).
5. Test in staging by [enabling the enhanced-experience](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables) toggle, refresh your browser, then verify colors in your environment.
6. Rollout to your production environment when ready.

### Safe Update and Editing Tips

1. Keep the same JSON structure and property names as in the [Themes JSON File](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210155405-Themes-JSON-File).
2. When you apply updates to your existing theme, PATCH it using the appropriate API endpoint.
3. Replace hex values with your brand colors.
4. Keep non-color style values as-is unless you specifically want to change behavior:

   * `mixBlendMode`
   * `tabBg`
5. Ensure your selected text and icon colors have enough contrast against your background colors.
6. Keep your active and hover states visually distinct from default states.

## Themes and UI Update Scenarios

Depending on the version of your current instance, you may need to complete several tasks to support your roll out of an [enabled enhanced experience](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables).

| Previous Environment | Default User Interface on update to v26.2 | Default Theme on update to v26.2 | Actions |
| --- | --- | --- | --- |
| Symphony 26.1 or earlier | `enhanced-experience` (enabled) | Your existing theme remains unchanged. | No action required. You can continue using your custom theme, `d+a_light` theme, or `__platform__` theme. |
| New install: v26.2 | Classic experience. | `composer` theme. | Enable the enhanced-experience toggle, and select the `d+a_light` theme, or `__platform__` theme. Alternatively, expand and update a classic theme. |
| Composer v26.1 or earlier (custom theme) | Classic experience. | Your custom classic theme is applied. | * Enable the enhanced-experience in a staging environment. * Update your custom classic theme and test. * Roll out updated theme and new interface to production.   Alternatively, apply the `d+a_light` theme, or `__platform__` theme. |
| Composer v26.1 or earlier (composer, modern, or dark theme) | Classic experience. | Your existing theme selection is applied. | * Enable the enhanced-experience in a staging environment. * Update your preferred classic theme and test. * Roll out updated theme and new interface to production.   Alternatively, apply the `d+a_light` theme, or `__platform__` theme. |

## User Interface Changes

When you enable the enhanced-experience toggle, the following broad changes are applied to your environment.

| Previous Interface Element | When Enhanced Experience is enabled | Notes |
| --- | --- | --- |
| Login Page | Updated User Interface | White background may not show white images or text well. |
| Home Page | Replaced with a new Home Page layout.  The specific layout is dependent on the user's privileges. | Card functionality is similar to the previous home page. Supports advanced features such as AI integration. |
| Side Bar (Main Menu) | New User Interface, replacing UI menu. | Replaces and reorganizes features available to users in the UI menu. Supports advanced features such as AI integration. |
| Top Navigation Bar | Removed. Functionality replicated by the new main menu and home page. | This element has been retired. |
| Optional Side Navigation | Replaced. Functionality moved to Main Menu. | This element, enabled in some environments optionally using a sever-level variable, has been retired. |
| Tenant Switching | Moved. | Tenant switching and some administrative functions have been moved and reorganized into sub menus. |

## IFrame Access URL References

The enhanced experience user interface changes also have back end url address changes you will need to be aware of when updating your environment. Items that were in the main UI menu for Administrators and members of the Supervisor group have been reorganized into an Administration menu and Tools dropdown menu. The Switch Tenant menu has moved to a sub menu of the Profile menu option.

| Admin Page | v26.1 and Earlier Retiring Reference | v26.2+ Enhanced-Experience |
| --- | --- | --- |
| Users | `{baseURL}/composer/admin.html#users-and-groups` | `{baseURL}/composer/admin.html#users` |
| Groups | `{baseURL}/composer/admin.html#groups` |
| Group Privileges | `{baseURL}/composer/admin.html#group-privileges` |
| Tenants | No change. See v26.2 column. | `{baseURL}/composer/admin.html#accounts` |
| System Users | `{baseURL}/composer/admin.html#users` | Removed. Use the Users page or Groups page as needed. |
| License |  | `{baseURL}/composer/admin.html#license` |
| Custom Charts |  | `{baseURL}/composer/admin.html#visualizations` |
| Console |  | `{baseURL}/composer/admin.html#scheduler` |
| Actions |  | `{baseURL}/composer/admin.html#actions` |
| Customize UI |  | `{baseURL}/composer/admin.html#customize` |
| Security |  | `{baseURL}/composer/admin.html#security` |
| Connectors |  | `{baseURL}/composer/admin.html#connectors` |
| Advanced (Admin-Level Variables) |  | `{baseURL}/composer/admin.html#advanced` |
| Configuration (if the configuration microservice is enabled) |  | `{baseURL}/composer/admin.html#configuration` |
