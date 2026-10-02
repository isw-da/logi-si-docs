> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Embedded Source Editor

Use Self-Service Analytics to embed a source editor for your users, enabling them to view, edit, or configure data sources directly in your application. Define the editor for users as needed for your custom solution.

You can embed the complete source editor, or limit what your users can access and use.

* [Step 1. Define a Connection to Create a Source](#step-1-define-a-connection-to-create-a-source)
* [Step 2. Create a Component for the Source Editor](#step-2-create-a-component-for-the-source-editor)
* [Step 3. Define Interactivity Settings](#step-3-define-interactivity-settings)
* [Step 4. Define Breadcrumbs Configuration](#step-4-define-breadcrumbs-configuration)

<h2 id="step-1-define-a-connection-to-create-a-source">
  Step 1. Define a Connection to Create a Source
</h2>

Define a connection users can access to create a source. See [Embed Source Editor Properties](#embed-source-editor-properties) for more information on the properties for creating a source.

```yaml theme={null}
{
	create: {
		visible: true,
		connections: {
			ids: ["6347eca23d231b5c3c2a2f79", "633d6ef33d27115c3c2a2e45"],
			defaultId: "6347eca22d271b5c3c2a2f79"
		}
	},
	fields: {
		visible: true
	},
	caching: {
		visible: true
	},
	settings: {
		visible: true
	}
}
```

<h2 id="step-2-create-a-component-for-the-source-editor">
  Step 2. Create a Component for the Source Editor
</h2>

```javascript theme={null}
// First initialize embed manager const sourceEditor = await embedManager.createComponent('source-editor', { sourceId: "633167d188f857721d2f70dd", // existing Source ID activeTab: "fields", theme: "composer", tabs: { ... }, breadcrumbs: { ... }, interactivityOverrides: { ... }, notificationSettings: { ... }, });
```

<h2 id="step-3-define-interactivity-settings">
  Step 3. Define Interactivity Settings
</h2>

```yaml theme={null}
interactivityOverrides: { create: { ADD_FROM_CONNECTION: false, UPLOAD_NEW_FILE: 'false' // value can be string as well }, fields: { ADD_DERIVED_FIELD: false, ADD_HIERARCHY_FIELD: 'false' // value can be string as well }, caching: { STATISTICS_CACHE: false, SCHEDULE_REFRESH: 'false' // value can be string as well } }
```

<h2 id="step-4-define-breadcrumbs-configuration">
  Step 4. Define Breadcrumbs Configuration
</h2>

```javascript theme={null}
{ title: "Back to Sources", href: "https://company.com/sources", target: "_blank", onClick: () => { console.log("do action"); } }
```

<h2 id="embed-source-editor-properties">
  Embed Source Editor Properties
</h2>

Use the following properties when creating an embedded source editor.

### Top Level Properties

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`sourceId`</td>
      <td>`undefined`</td>

      <td>
        The ID of the source for the editor to connect to. If an ID is not passed, an empty editor is embedded.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td>`activeTab`</td>
      <td>`'create'`</td>
      <td>The Active Tab presented to the user when the editor is loaded. Options include `'create'`, `'fields'`, `'caching'`, and `'settings'` .</td>
    </tr>

    <tr>
      <td>`theme`</td>
      <td>`undefined`</td>

      <td>
        The theme to use for the source editor. If a theme name is not passed, the default theme is used. Options include `modern`, `dark`, and `<custom>` .

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td>`header`</td>

      <td />

      <td>
        Type: HeaderProps

        <br />

        See [Header Properties](#header-properties).
      </td>
    </tr>

    <tr>
      <td>`breadcrumbs`</td>

      <td />

      <td>
        Type: BreadcrumbsProps

        <br />

        See [Breadcrumb Properties](#breadcrumb-properties).
      </td>
    </tr>

    <tr>
      <td>`tabs`</td>

      <td />

      <td>
        Type: TabsProps

        <br />

        See [Tab Properties](#tab-properties).
      </td>
    </tr>

    <tr>
      <td>`interactivityOverrides`</td>

      <td />

      <td>
        Type: InteractivityOverrides

        <br />

        See [Interactivity Overrides](#interactivity-overrides).
      </td>
    </tr>

    <tr>
      <td>`notificationSettings`</td>
      <td>`{ enabled: true, position: 'top-right' }`</td>

      <td>
        Use to show or hide the notifications and define their position.

        <br />

        Type: NotificatonSettings
      </td>
    </tr>
  </tbody>
</table>

<h3 id="header-properties">
  Header Properties
</h3>

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`visible`</td>
      <td>true</td>

      <td>
        Defines the visibility of the header.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`showTitle`</td>
      <td>true</td>

      <td>
        Defines the visibility of the source name.

        <br />

        Type: boolean
      </td>
    </tr>
  </tbody>
</table>

<h3 id="breadcrumb-properties">
  Breadcrumb Properties
</h3>

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`title`</td>
      <td>`"Sources"`</td>

      <td>
        The title of the first item in the breadcrumbs path.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td>`href`</td>
      <td>`""`</td>

      <td>
        The link address for the first item in the breadcrumbs path.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td>`target`</td>
      <td>`""`</td>

      <td>
        The link target parameter. Use `"_blank"` to open the editor in a new tab.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td>`onClick`</td>
      <td>`undefined`</td>

      <td>
        The action handler for selection of the breadcrumb.

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

<h3 id="tab-properties">
  Tab Properties
</h3>

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`create.visible`</td>
      <td>`true`</td>

      <td>
        Define visibility of the Source Creation tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`create.connections`</td>
      <td>`undefined`</td>

      <td>
        Configure the Connections list as a data entity.

        <br />

        Type: ConnectionsProps
      </td>
    </tr>

    <tr>
      <td>`fields.visible`</td>
      <td>`true`</td>

      <td>
        Define visibility of the Fields tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`caching.visible`</td>
      <td>`true`</td>

      <td>
        Define visibility of the Cache tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`settings.visible`</td>
      <td>`true`</td>

      <td>
        Define visibility of the Global Settings tab.

        <br />

        Type: boolean
      </td>
    </tr>
  </tbody>
</table>

### Connection Properties

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`ids`</td>
      <td>`undefined`</td>

      <td>
        The Connection IDs to use in the source editor for Data Entity creation.

        <br />

        * If no values are defined, all connections are visible.
        * If the value is an empty array, users can only connect to the connection defined in `defaultId`.
        * If a selected Data Entity is not in the list, the connection for that entity is added to the list of available connections for the data entity.

        <br />

        Type: string array
      </td>
    </tr>

    <tr>
      <td>`defaultId`</td>
      <td>`undefined`</td>

      <td>
        Define the default connection ID. If this value is not defined, no default connection selection is available.

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

<h3 id="interactivity-overrides">
  Interactivity Overrides
</h3>

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`create`</td>
      <td>`undefined`</td>

      <td>
        The overrides for the interactivity settings related to the Source Creation tab.

        <br />

        Type: CreationInteractivitySettings
      </td>
    </tr>

    <tr>
      <td>`fields`</td>
      <td>`undefined`</td>

      <td>
        The overrides for the interactivity settings related to the Fields tab.

        <br />

        Type: FieldsInteractivitySettings
      </td>
    </tr>

    <tr>
      <td>`caching`</td>
      <td>`undefined`</td>

      <td>
        The overrides for the interactivity settings related to the Fields tab.

        <br />

        Type: CachingInteractivitySettings
      </td>
    </tr>
  </tbody>
</table>

### Creation Interactivity Settings

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`"ADD_FROM_CONNECTION" : true`</td>

      <td>
        When set to `true`, users can see and use the **Add From Connection** menu item on the Source Creation tab. When set to `false`, it is hidden.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"ADD_FROM_FILE_UPLOAD" : true`</td>

      <td>
        When set to `true`, users can see and use the **Add From File** menu item on the Source Creation tab. When set to `false`, it is hidden.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"SELECT_FILE_UPLOAD" : true`</td>

      <td>
        When set to `true`, users can see and use the **Select File** control on the Source Creation tab. When set to `false`, it is hidden.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"UPLOAD_NEW_FILE" : true`</td>

      <td>
        When set to `true`, users can see and use the **Upload New File** button on the Source Creation tab. When set to `false`, it is hidden.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"CREATE_JOINS" : true`</td>

      <td>
        When set to `true`, users can see and use the **Add** control. When set to `false`, it is hidden.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"FILTER_VALUES_ENTITIES" : true`</td>

      <td>
        When set to `true`, users can see and use the **Filter Values Entity** option on the Source Creation tab. When set to `false`, it is hidden.

        <br />

        Type: boolean
      </td>
    </tr>
  </tbody>
</table>

### Fields Interactivity Settings

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`ADD_DERIVED_FIELD`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Add Derived Field button on the Fields tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`ADD_HIERARCHY_FIELD`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Add Hierarchy Field button on the Fields tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`ADD_CUSTOM_METRIC`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Add Custom Metric button on the Fields tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`VISIBILITY`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Visibility column on the Fields tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`SETTINGS`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Settings menu on the Fields tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`FILTER_VALUES`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Filter Values menu on the Fields tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`INFO`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Info menu on the Fields tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`DELETE`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Delete button on the Fields tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`FILTER_VALUE_OVERRIDES`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Filter Values tab on the Fields tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`FIELD_CAPABILITIES`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Field Capabilities button on the Fields tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`MANAGE_TRANSLATIONS`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Upload Translation File button on the Fields tab.

        <br />

        Type: boolean
      </td>
    </tr>
  </tbody>
</table>

### Caching Interactivity Settings

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`DATA_CACHE`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Data Cache control on the Cache tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`STATISTICS_CACHE`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Statistics Cache control on the Cache tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`SCHEDULE_REFRESH`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Schedule Refresh control on the Cache tab.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`STATISTICS_CACHE`</td>
      <td>`true`</td>

      <td>
        Defines the visibility of the Statistics Cache control on the Cache tab.

        <br />

        Type: boolean
      </td>
    </tr>
  </tbody>
</table>
