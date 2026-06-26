---
title: "Embed Source Editor Properties"
id: 34932982468749
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932982468749-Embed-Source-Editor-Properties
updated_at: 2026-05-26T22:07:10Z
---

# Embed Source Editor Properties

# Embed Source Editor Properties

Use the following properties when creating an embedded source editor.

## Top Level Properties

| Property | Default Value | Description |
| --- | --- | --- |
| `sourceId` | `undefined` | The ID of the source for the editor to connect to. If an ID is not passed, an empty editor is embedded.  Type: string |
| `activeTab` | `'create'` | The Active Tab presented to the user when the editor is loaded. Options include `'create'`, `'fields'`, `'caching'`, and `'settings'` . |
| `theme` | `undefined` | The theme to use for the source editor. If a theme name is not passed, the default theme is used. Options include `modern`, `dark`, and `<custom>` .  Type: string |
| `header` |  | Type: HeaderProps  See [Header Properties](#Header). |
| `breadcrumbs` |  | Type: BreadcrumbsProps  See [Breadcrumb Properties](#Breadcrumb). |
| `tabs` |  | Type: TabsProps  See [Tab Properties](#Tab). |
| `interactivityOverrides` |  | Type: InteractivityOverrides  See [Interactivity Overrides](#Interactivity). |
| `notificationSettings` | `{ enabled: true, position: 'top-right' }` | Use to show or hide the notifications and define their position.  Type: NotificatonSettings |

## Header Properties

| Property | Default Value | Description |
| --- | --- | --- |
| `visible` | true | Defines the visibility of the header.  Type: boolean |
| `showTitle` | true | Defines the visibility of the source name.  Type: boolean |

## Breadcrumb Properties

| Property | Default Value | Description |
| --- | --- | --- |
| `title` | `"Sources"` | The title of the first item in the breadcrumbs path.  Type: string |
| `href` | `""` | The link address for the first item in the breadcrumbs path.  Type: string |
| `target` | `""` | The link target parameter. Use `"_blank"` to open the editor in a new tab.  Type: string |
| `onClick` | `undefined` | The action handler for selection of the breadcrumb.  Type: string |

## Tab Properties

| Property | Default Value | Description |
| --- | --- | --- |
| `create.visible` | `true` | Define visibility of the Source Creation tab.  Type: boolean |
| `create.connections` | `undefined` | Configure the Connections list as a data entity.  Type: ConnectionsProps |
| `fields.visible` | `true` | Define visibility of the Fields tab.  Type: boolean |
| `caching.visible` | `true` | Define visibility of the Cache tab.  Type: boolean |
| `settings.visible` | `true` | Define visibility of the Global Settings tab.  Type: boolean |

## Connection Properties

| Property | Default Value | Description |
| --- | --- | --- |
| `ids` | `undefined` | The Connection IDs to use in the source editor for Data Entity creation.   * If no values are defined, all connections are visible. * If the value is an empty array, users can only connect to the connection defined in `defaultId`. * If a selected Data Entity is not in the list, the connection for that entity is added to the list of available connections for the data entity.   Type: string array |
| `defaultId` | `undefined` | Define the default connection ID. If this value is not defined, no default connection selection is available.  Type: string |

## Interactivity Overrides

| Property | Default Value | Description |
| --- | --- | --- |
| `create` | `undefined` | The overrides for the interactivity settings related to the Source Creation tab.  Type: CreationInteractivitySettings |
| `fields` | `undefined` | The overrides for the interactivity settings related to the Fields tab.  Type: FieldsInteractivitySettings |
| `caching` | `undefined` | The overrides for the interactivity settings related to the Fields tab.  Type: CachingInteractivitySettings |

## Creation Interactivity Settings

| Property | Description |
| --- | --- |
| `"ADD_FROM_CONNECTION" : true` | When set to `true`, users can see and use the **Add From Connection** menu item on the Source Creation tab. When set to `false`, it is hidden.  Type: boolean |
| `"ADD_FROM_FILE_UPLOAD" : true` | When set to `true`, users can see and use the **Add From File** menu item on the Source Creation tab. When set to `false`, it is hidden.  Type: boolean |
| `"SELECT_FILE_UPLOAD" : true` | When set to `true`, users can see and use the **Select File** control on the Source Creation tab. When set to `false`, it is hidden.  Type: boolean |
| `"UPLOAD_NEW_FILE" : true` | When set to `true`, users can see and use the **Upload New File** button on the Source Creation tab. When set to `false`, it is hidden.  Type: boolean |
| `"CREATE_JOINS" : true` | When set to `true`, users can see and use the **Add** control. When set to `false`, it is hidden.  Type: boolean |
| `"FILTER_VALUES_ENTITIES" : true` | When set to `true`, users can see and use the **Filter Values Entity** option on the Source Creation tab. When set to `false`, it is hidden.  Type: boolean |

## Fields Interactivity Settings

| Property | Default Value | Description |
| --- | --- | --- |
| `ADD_DERIVED_FIELD` | `true` | Defines the visibility of the Add Derived Field button on the Fields tab.  Type: boolean |
| `ADD_HIERARCHY_FIELD` | `true` | Defines the visibility of the Add Hierarchy Field button on the Fields tab.  Type: boolean |
| `ADD_CUSTOM_METRIC` | `true` | Defines the visibility of the Add Custom Metric button on the Fields tab.  Type: boolean |
| `VISIBILITY` | `true` | Defines the visibility of the Visibility column on the Fields tab.  Type: boolean |
| `SETTINGS` | `true` | Defines the visibility of the Settings menu on the Fields tab.  Type: boolean |
| `FILTER_VALUES` | `true` | Defines the visibility of the Filter Values menu on the Fields tab.  Type: boolean |
| `INFO` | `true` | Defines the visibility of the Info menu on the Fields tab.  Type: boolean |
| `DELETE` | `true` | Defines the visibility of the Delete button on the Fields tab.  Type: boolean |
| `FILTER_VALUE_OVERRIDES` | `true` | Defines the visibility of the Filter Values tab on the Fields tab.  Type: boolean |
| `FIELD_CAPABILITIES` | `true` | Defines the visibility of the Field Capabilities button on the Fields tab.  Type: boolean |
| `MANAGE_TRANSLATIONS` | `true` | Defines the visibility of the Upload Translation File button on the Fields tab.  Type: boolean |

## Caching Interactivity Settings

| Property | Default Value | Description |
| --- | --- | --- |
| `DATA_CACHE` | `true` | Defines the visibility of the Data Cache control on the Cache tab.  Type: boolean |
| `STATISTICS_CACHE` | `true` | Defines the visibility of the Statistics Cache control on the Cache tab.  Type: boolean |
| `SCHEDULE_REFRESH` | `true` | Defines the visibility of the Schedule Refresh control on the Cache tab.  Type: boolean |
| `STATISTICS_CACHE` | `true` | Defines the visibility of the Statistics Cache control on the Cache tab.  Type: boolean |
