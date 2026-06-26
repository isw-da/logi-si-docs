---
title: "Embedded Source Inventory Properties and Objects"
id: 34932897921165
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932897921165-Embedded-Source-Inventory-Properties-and-Objects
updated_at: 2026-05-26T22:07:19Z
---

# Embedded Source Inventory Properties and Objects

# Embedded Source Inventory Properties and Objects

The source inventory embed feature allows you to define the look and feel of the Sources page for your embedded users.

When you embed a list of sources, you can define which columns to include, order them in your preferred layout, and define what controls are available by enabling and disabling interactivity settings. Your users can filter sources, search for sources, and add sources to favorites.

Use the `InteractivityValue` property to specify interactivity parameters for the sources inventory.

| Parameter | Description |
| --- | --- |
| `"ADD_NEW": true` | When set to `true`, users can create a new data source configuration. When set to `false`, the button to create a new data source is hidden.  Type: boolean |
| `"FILTER": true` | When set to `true`, users can filter sources using the quick filter icons to the left of the **Search** field on the sources page. When set to `false`, they cannot filter sources.  Type: boolean |
| `"DELETE": true` | When set to `true`, users can delete data source configurations not currently in use by a visual.  When set to `false`, they cannot delete data source configurations, and the delete icon is not visible in the UI.  Type: boolean |
| `"DESCRIPTION": true` | When set to `true`, users can view and search for items (sources, visual gallery visuals, dashboard in the library) by the contents of an item's description.  When set to `false`, description options are not available to users.  Type: boolean |
| `"EXPORT": true` | When set to `true`, users can export data source configurations.  When set to `false`, users cannot export data source configurations, and the option is not visible in the UI.  Type: boolean |
| `"PERMISSIONS": false` | When set to `true`, users can manage user and group permissions for data sources. When set to `false`, they cannot manage permissions for data sources, and the related icons are not visible in the UI.  Type: boolean |
| `"FAVORITES": true` | When set to `true`, users can mark the data source as a favorite. When set to `false`, they cannot mark data source favorites and the favorites icons are not visible in the UI.  Type: boolean |
| `"ROW_SECURITY": false` | When set to `true`, users can define row security for data sources. When set to `false`, they cannot define row security for data sources, and the related icons are not visible in the UI.  Type: boolean |
| `"COLUMN_SECURITY": false` | When set to `true`, users can define column security for data sources. When set to `false`, they cannot define column security for data sources, and the related icons are not visible in the UI.  Type: boolean |
| `"CLEAR_CACHE": true` | When set to `true`, users can clear the cache for a data source. When set to `false`, users cannot clear the cache for a data source and the related icons are not visible in the UI.  Type: boolean |
| `"AVAILABLE_VISUAL_TYPES": true` | When set to `true`, users invoke the **Available Visual Types** work area to enable and disable available visual types for a source. When set to `false`, they cannot affect available visual types, or see related icons are not visible in the UI.  Type: boolean |
