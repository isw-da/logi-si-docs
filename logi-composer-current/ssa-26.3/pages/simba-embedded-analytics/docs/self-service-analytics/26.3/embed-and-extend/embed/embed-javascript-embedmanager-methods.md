> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# EmbedManager Methods

The following `EmbedManager` methods can be used to manage embedded Self-Service Analytics components. Sample code showing the use of these methods in an application are provided. See [Embedded JavaScript Examples](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript#embedded-javascript-examples) for a complete example of how these methods might be coded in JavaScript.

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`createComponent()`</td>

      <td>
        Creates a Self-Service Analytics component in your application. This method is asynchronous and returns a promise that resolves the created component.

        <br />

        The parameters input to this method include:

        <br />

        * a string that identifies the type of component you want created (the component types currently supported are `dashboard` and `visual-builder`). An error occurs if an invalid component type is specified.
        * the configuration of the component, which includes the properties described in [Embedded Dashboard Properties and Objects](#embedded-dashboard-properties-and-objects) and [Embedded Visual Authoring Properties and Objects](#embedded-visual-authoring-properties-and-objects).

        <br />

        Use a standard `render` method (for example, `dashboard.render` or `visualBuilder.render`) to render the component in your application after it has been created. Examples are provided in [Embedded JavaScript Examples](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript#embedded-javascript-examples).

        <br />

        The following example embeds a dashboard:

        <br />

        ```javascript theme={null}
        const dashboard = await embedManager.createComponent('dashboard', {
            dashboardId: <id>,
            theme: 'composer',
            interactivityProfileName: '<interactivity-profile-name>',
            interactivity {
                settings:{
                   CHANGE_LAYOUT: "true",
                },
                visualSettings:{
                   FILTER: "false",
                   overrideVisualInteractivity: "true",
                },
            }
            editor: {
                placement: 'dockRight' // use eve sidepanel
            },
            header: {
                visible: true,
                showTitle: true,
                showActions: false, // will hide actions bar
                title: "Static custom title"
            }
        });
        ```
      </td>
    </tr>

    <tr>
      <td>`getComponentById()`</td>

      <td>
        Returns an instance of a Self-Service Analytics component, based on its component instance ID. The parameter input to this method is a string representing the component instance ID.

        <br />

        ```javascript theme={null}
        async function getComponent(<componentInstanceId>) {
             const embedManager = await createOrGetEmbedManager();
             return embedManager.getComponentById(<componentInstanceId>);
        }
        ```
      </td>
    </tr>

    <tr>
      <td>`refresh()`</td>

      <td>
        Refreshes all embedded components. This is useful when the token is expired. No parameters are passed to this method.

        <br />

        ```javascript theme={null}
        async function refreshComponent(<newToken>) {
             const embedManager = await createOrGetEmbedManager();
             embedManager.updateToken(<newToken>).then(() => {
                  embedManager.refresh();
             });
        }
        ```
      </td>
    </tr>

    <tr>
      <td>`refreshComponent()`</td>

      <td>
        Refreshes a particular component. The parameter used with this method is a string representing the component instance ID.

        <br />

        The following example refreshes a specific dashboard:

        <br />

        ```javascript theme={null}
        async function refreshDashboard(<newToken>, <componentInstanceId>) {
             const embedManager = await createOrGetEmbedManager();
             embedManager.updateToken(<newToken>).then(() => {
                  embedManager.refreshComponent(<componentInstanceId>);
             });
        }
        ```
      </td>
    </tr>

    <tr>
      <td>`refreshWithToken()`</td>

      <td>
        Combines an update token and refresh request for all components. The parameter input to this method is a string representing the new token.

        <br />

        ```javascript theme={null}
        async function refreshComponent(<newToken>) {
             const embedManager = await createOrGetEmbedManager();
             embedManager.refreshWithToken(<newToken>);
        }
        ```
      </td>
    </tr>

    <tr>
      <td>`removeComponent()`</td>

      <td>
        Removes an embedded component from your application. This method returns the value `true` when the removal is successful and `false` when it fails. When a component is removed, its watchers are also removed.

        <br />

        The parameter input to this method is a string representing the component instance ID.

        <br />

        ```javascript theme={null}
        async function clearComponent(id) {
             const embedManager = await createOrGetEmbedManager();
             embedManager.removeComponent(<componentInstanceId>);
        }
        ```
      </td>
    </tr>

    <tr>
      <td>`updateToken()`</td>

      <td>
        Refreshes the authorization token for an embedded component. This method is asynchronous and should be called prior to a refresh.

        <br />

        The parameter input to this method is either a string representing the new token or a function requesting a new token.

        <br />

        ```javascript theme={null}
        async function refreshDashboard(<newToken>) {
             const embedManager = await createOrGetEmbedManager();
             embedManager.updateToken(<newToken>).then(() => {
                  embedManager.refresh();
             });
        }
        ```
      </td>
    </tr>
  </tbody>
</table>

<h2 id="embedded-dashboard-properties-and-objects">
  Embedded Dashboard Properties and Objects
</h2>

Properties can be passed as parameters to the `createComponent` method when embedding dashboards.

Here is a sample embedding `"componentInstanceId":"<id>"`:

```javascript theme={null}
embedManager.createComponent('dashboard',
	const componentConfig = {
		"dashboardId": "<dashboard-ID>",
		"componentInstanceId":"<component-instance-ID>",
	}
);
```

The following table describes available options for these properties and objects.

See: [`dashboardId`](#dashboardId), [`componentInstanceId`](#componentInstanceId).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="dashboardId" />`"dashboardId":"<dashboard-ID>"`</td>
      <td>none</td>

      <td>
        The dashboard ID. If no dashboard ID is specified, an empty dashboard is embedded.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td><a id="componentInstanceId" />`"componentInstanceId":"<component-instance-ID>"`</td>
      <td>none</td>

      <td>
        The instance ID for the dashboard is generated when the dashboard is created.

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

Here is a sample embedding `"type"`:

```javascript theme={null}
embedManager.createComponent('dashboard',
	const componentConfig = {
		"dashboardId": "<dashboard-ID>",
		"componentInstanceId":"<component-instance-ID>",
		"type":"dashboard",
	}
);
```

The following table describes available options for these properties and objects.

See: [`type`](#type).

| Property/Object | Default | Description |
| - | - | - |
| <a id="type" />`"type":"dashboard"` | | The type of embedded component. |

Here is a sample embedding `"application"`:

```javascript theme={null}
embedManager.createComponent('dashboard',
	const componentConfig = {
		"dashboardId": "<dashboard-ID>",
		"componentInstanceId":"<component-instance-ID>",
		"type":"dashboard",
		"application":{
			"banner":false,
			"logo":true
		}
	}
);
```

The following table describes available options for these properties and objects.

See: [`application.banner`](#application.banner), [`application.logo`](#application.logo).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="application.banner" />`"application.banner": true`</td>
      <td>`false`</td>

      <td>
        Indicates whether the [top-level navigation banner](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-top-level-navigation-banner) should be shown with the embedded dashboard. Valid values are `true` or `false`.

        <br />

        Type: boolean

        <br />

        This property is deprecated and will be removed in a future release.
      </td>
    </tr>

    <tr>
      <td><a id="application.logo" />`"application.logo": true`</td>
      <td>`false`</td>

      <td>
        Indicates whether the logo should be shown with the embedded dashboard. Valid values are `true` or `false`.

        <br />

        Type: boolean

        <br />

        This property is deprecated and will be removed in a future release.
      </td>
    </tr>
  </tbody>
</table>

Here is a sample embedding `"interactivityProfileName"`:

```javascript theme={null}
embedManager.createComponent('dashboard',
	const componentConfig = {
		"dashboardId": "<dashboard-ID>",
		"componentInstanceId":"<component-instance-ID>",
		"type":"dashboard",
		"application":{
			"banner":false,
			"logo":true
		}
		"interactivityProfileName":"interactive",
	}
);
```

The following table describes available options for these properties and objects.

See: [`interactivityProfileName`](#interactivityProfileName).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="interactivityProfileName" />`"interactivityProfileName":"interactive"`</td>
      <td>`interactive`</td>

      <td>
        Determines the way in which your users will be able to work with the embedded dashboard. Valid values are `readonly` and `interactive`. If you do not want the user of your application to change anything and only be able to view the dashboard, specify `readonly`. If you want your users to be able to make changes to the dashboard, specify `interactive`.

        <br />

        When the mode is `readonly`, the dashboard cannot be changed.

        <br />

        <Note>
          This setting is backward-compatible with the `interactive` option for public shared link embeds. If you are migrating to Self-Service Analytics's JavaScript embed technology, specify `interactive` for this setting to ease the migration.
        </Note>

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

Here is a sample embedding `"interactivityOverrides"`:

```javascript theme={null}
embedManager.createComponent('dashboard',
	const componentConfig = {
		"dashboardId": "<dashboard-ID>",
		"componentInstanceId":"<component-instance-ID>",
		"type":"dashboard",
		"application":{
			"banner":false,
			"logo":true
		}
		"interactivityProfileName":"interactive",
		"interactivityOverrides":"<interactivity-overrides-ID>",
	}
);
```

The following table describes available options for these properties and objects.

See: [`interactivityOverrides`](#interactivityOverrides).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="interactivityOverrides" />`"interactivityOverrides":"<interactivity-overrides-ID>"`</td>
      <td>none</td>

      <td>
        Specifies specific dashboard and visual interactivity settings for an embedded dashboard. The visual interactivity settings specified in this object will override any interactivity settings specified for the individual visuals.

        <br />

        These settings will also override the dashboard interactivity profile linked to the dashboard (the one saved with the dashboard) and the dashboard interactivity profile passed by the `interactivityProfileName` property.

        <br />

        Type: object
      </td>
    </tr>
  </tbody>
</table>

Here is a sample embedding `"mode"`:

```javascript theme={null}
embedManager.createComponent('dashboard',
	const componentConfig = {
		"dashboardId": "<dashboard-ID>",
		"componentInstanceId":"<component-instance-ID>",
		"type":"dashboard",
		"application":{
			"banner":false,
			"logo":true
		}
		"interactivityProfileName":"interactive",
		"interactivityOverrides":"<interactivity-overrides-ID>",
		"mode":"interactive",
	}
);
```

The following table describes available options for these properties and objects.

See: [`mode`](#mode).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="mode" />`"mode":"interactive"`</td>
      <td>`interactive`</td>

      <td>
        When a dashboard interactivity profile is specified (using the `interactivityOverrides` object or the `interactivityProfileName` parameter), the `mode` parameter is ignored. The `mode` parameter is also deprecated in Self-Service Analytics and will be removed in a future release.

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

Here is a sample embedding `"theme"`:

```javascript theme={null}
embedManager.createComponent('dashboard',
	const componentConfig = {
		"dashboardId": "<dashboard-ID>",
		"componentInstanceId":"<component-instance-ID>",
		"type":"dashboard",
		"application":{
			"banner":false,
			"logo":true
		}
		"interactivityProfileName":"interactive",
		"interactivityOverrides":"<interactivity-overrides-ID>",
		"mode":"interactive",
		"theme":"modern",
	}
);
```

The following table describes available options for these properties and objects.

See: [`theme`](#theme).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="theme" />`"theme":"dark"`</td>
      <td>`composer`</td>

      <td>
        The theme for the embedded visual. Valid values are `d+a_light`, `__platform__`, `composer`, `modern`, `dark`. The initial default theme, `composer`, is the same as the `modern` theme. However, if you [add your own themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov) to the application, more options are available in this list and you may have introduced a different default.

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

Here is a sample embedding `"editor"`:

```javascript theme={null}
embedManager.createComponent('dashboard',
	const componentConfig = {
		"dashboardId": "<dashboard-ID>",
		"componentInstanceId":"<component-instance-ID>",
		"type":"dashboard",
		"application":{
			"banner":false,
			"logo":true
		}
		"interactivityProfileName":"interactive",
		"interactivityOverrides":"<interactivity-overrides-ID>",
		"mode":"interactive",
		"theme":"modern",
		"editor":{
			"placement": "docRight"
		}
	}
);
```

The following table describes available options for these properties and objects.

See: [`editor.placement`](#editor.placement).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="editor.placement" />`"editor.placement":"docRight"`</td>
      <td>`modals`</td>

      <td>
        Indicates where the dashboard editor appears. Valid editor placements are `dockRight` and `modals`.

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

Here is a sample embedding `"header"`:

```javascript theme={null}
embedManager.createComponent('dashboard',
	const componentConfig = {
		"dashboardId": "<dashboard-ID>",
		"componentInstanceId":"<component-instance-ID>",
		"type":"dashboard",
		"application":{
			"banner":false,
			"logo":true
		}
		"interactivityProfileName":"interactive",
		"interactivityOverrides":"<interactivity-overrides-ID>",
		"mode":"interactive",
		"theme":"modern",
		"editor":{
			"placement": "docRight"
		}
		"header": {
			"title": "My Dash"
			"showActions": false,
			"showTitle": false,
			"visible": false
		}
	}
);
```

The following table describes available options for these properties and objects.

See: [`header.title`](#header.title), [`header.showActions`](#header.showActions), [`header.showTitle`](#header.showTitle), [`header.visible`](#header.visible).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="header.title" />`"header.title":"<newtitle>"`</td>
      <td>none</td>

      <td>
        Allows you to overwrite the title of the embedded dashboard. The embedded dashboard title is read only; it cannot be changed while the dashboard is embedded.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td><a id="header.showActions" />`"header.showActions": false`</td>
      <td>`true`</td>

      <td>
        Indicates whether dashboard actions should be visible for the embedded dashboard. Valid values are `true` or `false`.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td><a id="header.showTitle" />`"header.showTitle": false`</td>
      <td>`true`</td>

      <td>
        Indicates whether the dashboard title should be shown for the embedded dashboard. Valid values are `true` or `false`.

        <br />

        Type: Boolean
      </td>
    </tr>

    <tr>
      <td><a id="header.visible" />`"header.visible": false`</td>
      <td>`true`</td>
      <td>Indicates whether the dashboard header should be shown for the embedded dashboard. Valid values are `true` or `false`.</td>
    </tr>
  </tbody>
</table>

Here is a sample embedding `"intialFilters"`:

```yaml theme={null}
intialFilters: {
	sourceId: "<source-id>"
	timeFilter: {
		from: "+$start_of_data",
		to: "+$end_of_data",
		timeField: "_saledate",
		},
	filters: [{
		"operation": "BETWEEN"
		"paths": "returns",
		"value": [ 1, 25 ]
	}]
}
```

The following table describes available options for these properties and objects.

See: [`initialFilters`](#initialFilters), [`applyFiltersStrategy`](#applyFiltersStrategy).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="initialFilters" />`initialFilters`</td>
      <td>none</td>

      <td>
        Allows you to pass initial filters to the specified dashboard. Pass parameters for `filters`, `sourceId`, `timeFilter`, and `applyFiltersStrategy`.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td><a id="applyFiltersStrategy" />`applyFiltersStrategy`</td>
      <td>`overrideSamePath`</td>

      <td>
        Use `overrideSamePath` to overwrite filters using the same path.

        <br />

        Use `replaceExisting` to remove all filters and use only defined `initialFilters`.
      </td>
    </tr>
  </tbody>
</table>

You can also refresh your data in the dashboard as needed.

| Method | Description |
| - | - |
| `component.refreshData()` | Refreshes data in the dashboard when called. |

## Embedded Library Properties and Objects

The library embed feature also includes pre-defined actions for adding a dashboard and opening a dashboard.

Here's what you can do with pre-defined actions:

* Specify an action for embed action
* Specify an action for navigate to link
* Change a cursor if a column has onClick action specified
* Pass an item id to the link ("[https://dashboards.company.com/edit/\\\$\&#123;inventoryitemId\&#125](https://dashboards.company.com/edit/\\\$\&#123;inventoryitemId\&#125);")
* Filter dashboards by dashboard tags (See [Embed Components Using JavaScript and Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript))

The following Actions are supported:

| Action |
| - |
| Embed |
| Open |

Below is a code sample for using the onClick property:

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Example</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>FunctionClickHandler</td>

      <td>
        ```javascript theme={null}
        (data?: InventoryItem) => console.log(data)
        ```
      </td>
    </tr>

    <tr>
      <td>EmbedClickHandler</td>

      <td>
        ```
        { type: "embed", parentElement: "#editor-container", // OR document.querySelector("#editor-container") replaceComponent: true, componentParams: { ... } }
        ```
      </td>
    </tr>

    <tr>
      <td>LinkClickHandler</td>

      <td>
        ```
        { type: "link", href: "https://dashboards.com/edit/${inventoryItemId}", target: "_blank" }
        ```
      </td>
    </tr>
  </tbody>
</table>

## Embedded Source Inventory Properties and Objects

The source inventory embed feature allows you to define the look and feel of the Sources page for your embedded users.

When you embed a list of sources, you can define which columns to include, order them in your preferred layout, and define what controls are available by enabling and disabling interactivity settings. Your users can filter sources, search for sources, and add sources to favorites.

Use the `InteractivityValue` property to specify interactivity parameters for the sources inventory.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`"ADD_NEW": true`</td>

      <td>
        When set to `true`, users can create a new data source configuration. When set to `false`, the button to create a new data source is hidden.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"FILTER": true`</td>

      <td>
        When set to `true`, users can filter sources using the quick filter icons to the left of the **Search** field on the sources page. When set to `false`, they cannot filter sources.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"DELETE": true`</td>

      <td>
        When set to `true`, users can delete data source configurations not currently in use by a visual.

        <br />

        When set to `false`, they cannot delete data source configurations, and the delete icon is not visible in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"DESCRIPTION": true`</td>

      <td>
        When set to `true`, users can view and search for items (sources, visual gallery visuals, dashboard or self-service report in the library) by the contents of an item's description.

        <br />

        When set to `false`, description options are not available to users.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"EXPORT": true`</td>

      <td>
        When set to `true`, users can export data source configurations.

        <br />

        When set to `false`, users cannot export data source configurations, and the option is not visible in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"PERMISSIONS": false`</td>

      <td>
        When set to `true`, users can manage user and group permissions for data sources. When set to `false`, they cannot manage permissions for data sources, and the related icons are not visible in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"FAVORITES": true`</td>

      <td>
        When set to `true`, users can mark the data source as a favorite. When set to `false`, they cannot mark data source favorites and the favorites icons are not visible in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"ROW_SECURITY": false`</td>

      <td>
        When set to `true`, users can define row security for data sources. When set to `false`, they cannot define row security for data sources, and the related icons are not visible in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"COLUMN_SECURITY": false`</td>

      <td>
        When set to `true`, users can define column security for data sources. When set to `false`, they cannot define column security for data sources, and the related icons are not visible in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"CLEAR_CACHE": true`</td>

      <td>
        When set to `true`, users can clear the cache for a data source. When set to `false`, users cannot clear the cache for a data source and the related icons are not visible in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"AVAILABLE_VISUAL_TYPES": true`</td>

      <td>
        When set to `true`, users invoke the **Available Visual Types** work area to enable and disable available visual types for a source. When set to `false`, they cannot affect available visual types, or see related icons are not visible in the UI.

        <br />

        Type: boolean
      </td>
    </tr>
  </tbody>
</table>

<h2 id="embedded-visual-authoring-properties-and-objects">
  Embedded Visual Authoring Properties and Objects
</h2>

The following properties can be passed as parameters to the `createComponent` method when embedding visual authoring components.

Here is a sample.

<Note>
  This example assumes that the EmbedManager has already been initialized, and the ID of a visual template is passed.
</Note>

```javascript theme={null}
const getToken = async () => { const response = await fetch('<playground-uri-and-username-token>', { method: 'GET', credentials: 'same-origin' }); return response.json().then((result) => { return { access_token: result.token, expires_in: result.expiresIn, }; }); }; const embedManagerPromise = window.initComposerEmbedManager({ getToken: getToken }); const componentConfig = { "theme":"modern", "header": { "showTitle": false, "visible": false, "showActions": false, "title": "<title-text>", } } const createEmbedComponent = (embedManager, config, containerElementId = 'widget-holder') => { embedManager.createComponent("visual-builder", config).then(component => { component.render(document.getElementById(containerElementId), { width:"100%", height: "100%" }); }) } embedManagerPromise.then(embedManager => { createEmbedComponent(embedManager, componentConfig, 'widget-holder'); });
```

The following table describes the available properties for `componentConfig`.

See: [`theme`](#theme-2).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="theme-2" />`"theme":"dark"`</td>
      <td>`composer`</td>

      <td>
        The theme for the embedded visual. Valid values are `d+a_light`, `__platform__`, `composer`, `modern`, `dark`. The initial default theme, `composer`, is the same as the `modern` theme. However, if you [add your own themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov) to the application, more options are available in this list and you may have introduced a different default.

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

The following table describes the available `header` properties.

See: [`showTitle`](#showTitle), [`visible`](#visible), [`showActions`](#showActions), [`title`](#title).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="showTitle" />`"showTitle": true`</td>
      <td>`true`</td>

      <td>
        Indicates whether the visual header title should be shown for the embedded visual. Valid values are `true` or `false`.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td><a id="visible" />`"visible": false`</td>
      <td>`true`</td>

      <td>
        Indicates whether the visual header should be visible for the embedded visual. Valid values are `true` or `false`.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td><a id="showActions" />`"showActions": false`</td>
      <td>`true`</td>

      <td>
        Indicates whether the visual header actions should be shown for the embedded visual. Valid values are `true` or `false`.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td><a id="title" />`"title": <text>`</td>
      <td>none</td>

      <td>
        Specifies a static title for the visual.

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

The following table describes the available `breadcrumb` properties.

See: [`breadcrumbs.onClick`](#breadcrumbs.onClick), [`breadcrumbs.target`](#breadcrumbs.target), [`breadcrumbs.title`](#breadcrumbs.title).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`<optional breadcrumb properties>`</td>

      <td />

      <td>Optional breadcrumb properties are described in [Optional Embedded Visual Authoring Breadcrumb Properties](#optional-embedded-visual-authoring-breadcrumb-properties).</td>
    </tr>

    <tr>
      <td><a id="breadcrumbs.onClick" />`"breadcrumbs.onClick"`</td>
      <td>none</td>

      <td>
        The click action handler for the breadcrumb title.

        <br />

        Type: function
      </td>
    </tr>

    <tr>
      <td><a id="breadcrumbs.target" />`"breadcrumbs.target":"_blank"`</td>
      <td>none</td>

      <td>
        The link target parameter. Use `"_blank"` to open in a new tab. A valid link target should be specified in quotes (`"<target>"`).

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td><a id="breadcrumbs.title" />`"breadcrumbs.title":"<title>"`</td>
      <td>none</td>

      <td>
        The first item breadcrumbs title. A valid title should be specified in quotes (`"<title>"`).

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

The following table describes the available properties for source visualID.

See: [`source.visualId`](#source.visualId), [`interactivityOverrides`](#interactivityOverrides-2), [`visualId`](#visualId).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="source.visualId" />`"source.visualId":"<id>"`</td>
      <td>null</td>

      <td>
        The source ID of a visual template, used for creating a new visual in visual authoring. This represents a predefined visual template. A valid source ID should be specified in quotes (`"<source-visual-ID>"`). If neither `visualId` or `source.visualId` is specified, an empty visual authoring instance will be opened. If both are provided, `visualId` is used.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td><a id="interactivityOverrides-2" />`"interactivityOverrides"`</td>
      <td>none</td>

      <td>
        Specifies interactivity override settings for visual authoring. The interactivity settings specified in this object will override any interactivity settings specified for the individual visuals. For a list of visual interactivity settings you can specify, see [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

        <br />

        Type: object
      </td>
    </tr>

    <tr>
      <td><a id="visualId" />`"visualId":"<id>"`</td>
      <td>null</td>

      <td>
        The visual ID for an existing visual for visual authoring. A valid visual ID should be specified in quotes (`"<visual-ID>"`). If neither `visualId` or `source.visualId` is specified, an empty visual authoring instance will be opened. If both are provided, `visualId` is used.

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

The following table describes all of the available properties.

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`<optional breadcrumb properties>`</td>
      <td colSpan={2}>Optional breadcrumb properties are described in [Optional Embedded Visual Authoring Breadcrumb Properties](#optional-embedded-visual-authoring-breadcrumb-properties).</td>
    </tr>

    <tr>
      <td><a id="breadcrumbs.onClick-2" />`"breadcrumbs.onClick"`</td>
      <td>none</td>

      <td>
        The click action handler for the breadcrumb title.

        <br />

        Type: function
      </td>
    </tr>

    <tr>
      <td><a id="breadcrumbs.target-2" />`"breadcrumbs.target":"_blank"`</td>
      <td>none</td>

      <td>
        The link target parameter. Use `"_blank"` to open in a new tab. A valid link target should be specified in quotes (`"<target>"`).

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td><a id="breadcrumbs.title-2" />`"breadcrumbs.title":"<title>"`</td>
      <td>none</td>

      <td>
        The first item breadcrumbs title. A valid title should be specified in quotes (`"<title>"`).

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td><a id="header.showActions-2" />`"header.showActions": false`</td>
      <td>`true`</td>

      <td>
        Indicates whether the visual header actions should be shown for the embedded visual. Valid values are `true` or `false`.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td><a id="header.showTitle-2" />`"header.showTitle": false`</td>
      <td>`true`</td>

      <td>
        Indicates whether the visual header title should be shown for the embedded visual.

        <br />

        Valid values are `true` or `false`.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td><a id="header.title-2" />`"header.title": <text>`</td>
      <td>none</td>

      <td>
        Specifies a static title for the visual.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td><a id="header.visible-2" />`"header.visible": false`</td>
      <td>`true`</td>

      <td>
        Indicates whether the visual header should be visible for the embedded visual.

        <br />

        Valid values are `true` or `false`.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td><a id="interactivityOverrides-3" />`"interactivityOverrides"`</td>
      <td>none</td>

      <td>
        Specifies interactivity override settings for visual authoring.

        <br />

        The interactivity settings specified in this object will override any interactivity settings specified for the individual visuals.

        <br />

        For a list of visual interactivity settings you can specify, see [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

        <br />

        Type: object
      </td>
    </tr>

    <tr>
      <td><a id="source.visualId-2" />`"source.visualId":"<id>"`</td>
      <td>null</td>

      <td>
        The source ID of a visual template, used for creating a new visual in visual authoring. This represents a predefined visual template. A valid source ID should be specified in quotes (`"<source-visual-ID>"`).

        <br />

        If neither `visualId` or `source.visualId` is specified, an empty visual authoring instance will be opened.

        <br />

        If both are provided, `visualId` is used.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td><a id="theme-3" />`"theme":"dark"`</td>
      <td>`composer`</td>

      <td>
        The theme for the embedded visual. Valid values are `d+a_light`, `__platform__`, `composer`, `modern`, `dark`. The initial default theme, `composer`, is the same as the `modern` theme. However, if you [add your own themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov) to the application, more options are available in this list and you may have introduced a different default.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td><a id="visualId-2" />`"visualId":"<id>"`</td>
      <td>null</td>

      <td>
        The visual ID for an existing visual for visual authoring. A valid visual ID should be specified in quotes (`"<visual-ID>"`).

        <br />

        If neither `visualId` or `source.visualId` is specified, an empty visual authoring instance will be opened.

        <br />

        If both are provided, `visualId` is used.

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

<Note>
  You can include several controls for embedded visuals, allowing users to select and deselect favorite visuals, as well as filter the list of visuals in the embedded Visual Gallery by favorite status. See [Use the Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery).
</Note>

<h2 id="optional-embedded-visual-authoring-breadcrumb-properties">
  Optional Embedded Visual Authoring Breadcrumb Properties
</h2>

Optionally, you can pass breadcrumb properties as parameters to the `createComponent` method when embedding Self-Service Analytics visual authoring components.

Here is a sample:

```javascript theme={null}
			"breadcrumbs": {
			"title": "<title>",
			"onClick": () => {console.log('clicked')},
			"href": "<uri-or-fqdn>",
			"target": "_blank"
		}
```

The following table describes the optional breadcrumb properties.

See: [`title`](#title-2), [`onClick`](#onClick), [`href`](#href), [`target`](#target).

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="title-2" />`"title":"<title>"`</td>
      <td>none</td>

      <td>
        The first item breadcrumbs title. A valid title should be specified in quotes (`"<title>"`).

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td><a id="onClick" />`"onClick"`</td>
      <td>none</td>

      <td>
        The click action handler for the breadcrumb title.

        <br />

        Type: function
      </td>
    </tr>

    <tr>
      <td><a id="href" />`"href":"<uri-or-fqdn>"`</td>
      <td>none</td>

      <td>
        The link address of the breadcrumb title.

        <br />

        A valid link address, such as a URI or Fully Qualified Domain Name should be specified in quotes (`"<uri-or-fqdn>"`).

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td><a id="target" />`"target":"_blank"`</td>
      <td>none</td>

      <td>
        The link target parameter. Use `"_blank"` to open in a new tab.

        <br />

        A valid link target should be specified in quotes (`"<uri-or-fqdn>"`).

        <br />

        Type: string
      </td>
    </tr>
  </tbody>
</table>

<h2 id="token-related-configuration-properties">
  Token-Related Configuration Properties
</h2>

The `initComposerEmbedManager` window function supports the following token-related configuration properties.

See: [`getToken`](#getToken).

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="getToken" />`getToken`</td>

      <td>
        This method returns a token using [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov). This is the same as the `window.composerGetToken` method. There is no default.

        <br />

        ```javascript theme={null}
        getToken: () => {
          return Promise.resolve({ // this is an example function. server side should be called in production
            "access_token": "60a26b4f-c5d7-49af-a90b-1da4e6eb12b8",
            "expires_in": "6000"
        });
        						}
        ```
      </td>
    </tr>
  </tbody>
</table>
