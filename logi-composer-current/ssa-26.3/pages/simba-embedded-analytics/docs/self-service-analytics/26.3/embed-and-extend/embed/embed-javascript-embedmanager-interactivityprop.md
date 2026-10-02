> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Interactivity Properties

You can add interactivity override settings to your embed script to provide granular control over what your users can do with an embedded Self-Service Analytics component. Properties can be passed with parameters in the [`interactivityOverrides` object](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-dashboard-properties-and-objects) of the [`createComponent` method](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods) when embedding Self-Service Analytics components.

The `interactivityProfileName` property must be specified before the interactivity overrides (`interactivityOverrides` object) can work. See [Embedded Dashboard Properties and Objects](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-dashboard-properties-and-objects).

The `interactivityOverrides` object includes several property settings: `visualSettings`, `InteractivityValue`and `editorUserSettings`.

* The parameters of the `settings` property affect the current embedded dashboard interactivity. See [Dashboard Interactivity Parameters (settings Property)](#dashboard-interactivity-parameters-settings-property).
* The parameters of the `visualSettings` object property affect the current embedded visual interactivity. See [Visual Interactivity Parameters (visualSettings Property)](#visual-interactivity-parameters-visualsettings-property).
* The parameters of the `InteractivityValue` property define the source inventory dashboard. See [Sources Inventory Interactivity Parameters (InteractivityValue Property)](#sources-inventory-interactivity-parameters-interactivityvalue) .
* The parameters of the `editorUserSettings` property define the editor configuration dashboard. See [Editor Configuration (editorUserSettings Property)](#editor-configuration-editorusersettings-property).

The following example depicts the use and placement of dashboard and visual interactivity parameters.

```xml theme={null}
<script>
   src="../../../../embed/<server>:8443/composer/embed/embed.js",
     {
        "type": "dashboard",
        "dashboardId": "<dashboard-ID>",
        "theme": "modern",
        "interactivityProfileName": "interactive",
        "interactivityOverrides": {
          "settings":{
             "CHANGE_LAYOUT": true
          },
          "visualSettings":{
             "FILTER": false
          },
        }
     }
</script>
```

Custom user attributes can be used as variables in these property value settings. For example, the following property setting is valid and will insert the value of the `var2` custom user attribute in the property setting. If a `var2` custom user attribute is not found for a user, a value of `true` is assumed.

While it is possible to save a dashboard profile using custom user attributes, you cannot pass the dashboard profile with custom user attributes in the JavaScript.

```yaml theme={null}
"CHANGE_LAYOUT": "${User.var2|true}"
```

<h3 id="dashboard-interactivity-parameters-settings-property">
  Dashboard Interactivity Parameters (`settings` Property)
</h3>

Use the `settings` property to specify interactivity parameters for the dashboard. The default for all dashboard interactivity parameters is `true`.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`"ADD_TO_FAVORITES": false`</td>

      <td>
        When set to `true`, users can mark the dashboard as a favorite. When set to `false`, they cannot mark dashboard favorites and the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-fav.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=b316dd7cb31ab07c459eb50f712f6211" alt="select the favorite icon to add or remove the item from your favorited items" width="35" height="34" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '35px', height: '34px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-fav.png" />[dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"ADD_VISUALS": false`</td>

      <td>
        When set to `true`, these options are accessible in the dashboard UI:

        <br />

        * Select the dashboard icon <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-addcht.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=9b7cb57094fa7c7543c4acb22c33b03b" alt="select the add icon to add widgets to a dashboard" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-addcht.png" /> to add existing visuals to the dashboard (**Add Existing Visual**).
        * Select **Add to Visual Gallery** from the <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> menu to replace local visuals with Visual Gallery visuals. See [Create and Add Visuals to the Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery).

        <br />

        When set to `false`, users cannot add existing visuals or replace visuals in the dashboard.

        <br />

        Type: boolean

        <br />

        <Note>
          If all menu item parameters are `false`, the dashboard icon is not shown in the UI. If any menu item parameters are `true`, the dashboard icon is shown in the UI, and includes any items set to `true`.
        </Note>
      </td>
    </tr>

    <tr>
      <td>`"CHANGE_LAYOUT": true`</td>

      <td>
        When set to `true`, users can resize or move visuals in the dashboard. When set to `false`, they cannot resize or move visuals in the dashboard.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"COMMENTS": true`</td>

      <td>
        When set to `true`, users with appropriate permissions can access comments (read, write, edit their own, and delete comments, depending on their access level). When set to `false`, comments are not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"CREATE_FILTER_SNIPPETS": false`</td>

      <td>
        When set to `true`, users can add new filter snippets (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add-filter-snippet.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=499601ef1705bb1d3ad3838d4b141b1a" alt="select the add filter snippet icon to add a filter snippet to a dashboard" width="20" height="19" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add-filter-snippet.png" />) to the dashboard using the dashboard icons. When set to `false`, they cannot create new snippets to add to the dashboard.

        <br />

        Type: boolean

        <br />

        <Note>
          If all menu item parameters are `false`, the dashboard icon is not shown in the UI. If any menu item parameters are `true`, the dashboard icon is shown in the UI, and includes any items set to `true`.
        </Note>
      </td>
    </tr>

    <tr>
      <td>`"CREATE_TEXT_SNIPPETS": false`</td>

      <td>
        When set to `true`, users can add new text snippets (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/rts-add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=b69f086e70f0d10816d924ba9225dc95" alt="select to add a rich text snippet" width="20" height="20" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/rts-add.png" />) to the dashboard using the dashboard icons. When set to `false`, they cannot create new snippets to add to the dashboard.

        <br />

        Type: boolean

        <br />

        <Note>
          If all menu item parameters are `false`, the dashboard icon is not shown in the UI. If any menu item parameters are `true`, the dashboard icon is shown in the UI, and includes any items set to `true`.
        </Note>
      </td>
    </tr>

    <tr>
      <td>`"CREATE_VISUALS": false`</td>

      <td>
        When set to `true`, users with **Owner** and **Editor** access levels or the **Administer Visuals** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), these options are accessible in the dashboard UI:

        <br />

        * Select the dashboard icon <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-addcht.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=9b7cb57094fa7c7543c4acb22c33b03b" alt="select the add icon to add widgets to a dashboard" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-addcht.png" /> to add new local visuals to the dashboard (**Add New Visual**).
        * Select **Convert to Local** from the <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> menu to convert Visual Gallery visuals to local visuals. See [Convert Visual Gallery Visuals and Local Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#convert-visual-gallery-visuals-and-local-visuals).

        <br />

        When set to `false`, they cannot create new local visuals or convert Visual Gallery visuals in the dashboard.

        <br />

        Type: boolean

        <br />

        <Note>
          If all menu item parameters are `false`, the dashboard icon is not shown in the UI. If any menu item parameters are `true`, the dashboard icon is shown in the UI, and includes any items set to `true`.
        </Note>
      </td>
    </tr>

    <tr>
      <td>`"DASHBOARD_ALERTS": false`</td>
      <td>When set to `true`, users with appropriate [privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) can create and edit dashboard alerts using the dashboard icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/alert.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=483e2b94aeb3aceb00d26f4b19728c88" alt="select to manage alerts" width="20" height="20" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/alert.png" />. When set to `false`,the dashboard icon is hidden and users cannot create or edit dashboard alerts.</td>
    </tr>

    <tr>
      <td>`"DASHBOARD_INTERACTIONS": true`</td>
      <td>When set to `true`, users can link fields between disparate data sources to create cross-source links. When set to `false`, they cannot create cross-source links and the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-xsourcelink.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=a0bac4bcf53aa484043898173bc91e9b" alt="select to manage cross source links in your environment" width="23" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-xsourcelink.png" />[dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available in the UI.</td>
    </tr>

    <tr>
      <td>`"DASHBOARD_LINKS": true`</td>

      <td>
        When set to `true`, users can link dashboards. When set to `false`, they cannot link dashboards and the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-link.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=6b46f3f4e6fa2bdc72ae8dee012401c0" alt="select to manage dashboard links and visual links" width="21" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-link.png" />[dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"DELETE": true`</td>

      <td>
        When set to `true`, users can delete the dashboard. When set to `false`, they cannot delete the dashboard and the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-delete.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c083bb7faa9c686e4c8572cc5c69aa4f" alt="" width="19" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '19px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-delete.png" />[dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"EXPORT_CONFIGURATION": true`</td>

      <td>
        When set to `true`, users can export the JSON configuration for the dashboard. When set to `false`, the [Export dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import#export-dashboards) in the UI no longer provides an option to export the configuration. If this setting and the `EXPORT_PNG_PDF` setting are both turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=e8b1d12ba47dbfb0aa811319cc4af59b" alt="select to export this item" width="23" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png" />[dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"EXPORT_CSV": true`</td>

      <td>
        When set to `true`, users can Export the dashboard as a CSV file. When set to `false`, they cannot export the dashboard as a CSV file and the [Export dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import#export-dashboards) in the UI no longer provides this export option. If all export settings and the `EXPORT_CONFIGURATION` setting are both turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=e8b1d12ba47dbfb0aa811319cc4af59b" alt="select to export this item" width="23" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png" />[dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"EXPORT_PNG_PDF": true`</td>

      <td>
        When set to `true`, users can Export the dashboard as a PNG or PDF file. When set to `false`, they cannot export the dashboard as a PNG or PDF file and the [Export dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import#export-dashboards) in the UI no longer provides this export option. If all export settings and the `EXPORT_CONFIGURATION` setting are both turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=e8b1d12ba47dbfb0aa811319cc4af59b" alt="select to export this item" width="23" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png" />[dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"EXPORT_XLSX": true`</td>

      <td>
        When set to `true`, users can Export the dashboard as an Excel (.xlsx) file. When set to `false`, they cannot export the dashboard as an Excel (.xlsx) file and the [Export dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import#export-dashboards) in the UI no longer provides this export option. If all export settings and the `EXPORT_CONFIGURATION` setting are both turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=e8b1d12ba47dbfb0aa811319cc4af59b" alt="select to export this item" width="23" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png" />[dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"FILTER": true`</td>

      <td>
        When set to `true`, users can apply filters to the dashboard. When set to `false`, they cannot apply dashboard filters and the <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=68279f203a0950b32bfab88e7273d5ba" alt="" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png" />[dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"REFRESH": true`</td>

      <td>
        When set to `true`, users can refresh the dashboard data. When set to `false`, they cannot refresh dashboard data and the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-refresh.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=53cc532b6fce4e41f7756425d1b87639" alt="select to refresh the underlying data behind an object, or the specific field" width="34" height="34" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '34px', height: '34px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-refresh.png" />[dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"RENAME": true`</td>

      <td>
        When set to `true`, users can rename the dashboard. When set to `false`, they cannot rename the dashboard.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"SAVE_AS": true`</td>

      <td>
        When set to `true`, users can save the dashboard (make a copy) using a new name. When set to `false`, they cannot save the dashboard with a new name and the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save-as.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=0a1f29aed30da7ee353c14aac6c1c591" alt="" width="18" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '18px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save-as.png" /> [dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"SAVE": true`</td>

      <td>
        When set to `true`, users can save the dashboard. When set to `false`, they cannot save the dashboard and the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" /> [dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"SCHEDULE_REPORTS": true`</td>

      <td>
        When set to `true`, users with appropriate [privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) can schedule dashboard reports using the dashboard icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dashboard-schedule.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9e7a1179faaedda7e8026e3ccd40ddcd" alt="select the schedule report icon to schedule a dashboard or report with others" width="18" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '18px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dashboard-schedule.png" />. When set to `false`, the dashboard icon is hidden and they cannot schedule dashboard reports.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"SHARE_DASHBOARD": true`</td>

      <td>
        When set to `true`, users can share dashboards using the dashboard icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/share-dash-22-4.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=2845181af743f45892dc64f7fe42f0eb" alt="select to share a visual, dashboard, or report" width="20" height="20" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/share-dash-22-4.png" />. When set to `false`, the dashboard icon is hidden and they cannot share dashboards.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"SHARE_FILTER_SETS": true`</td>

      <td>
        When set to `true`, users can share saved filter sets with other users. When set to `false`, users cannot view or use filter sets for the dashboard.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"WIDGETS": true`</td>

      <td>
        When set to `true`, users can share saved filter sets with other users. When set to `false`, users cannot view or use the widget settings sidebar menu.

        <br />

        Type: boolean
      </td>
    </tr>
  </tbody>
</table>

<h3 id="visual-interactivity-parameters-visualsettings-property">
  Visual Interactivity Parameters (`visualSettings` Property)
</h3>

Use the `visualSettings` property to specify visual interactivity parameters for the embedded visuals. If the `overrideVisualInteractivity` property is set to `true` within these settings, the visual interactivity parameters will override any interactivity properties specified for the individual visuals.

The defaults for these parameters are determined by the interactivity profile.

* If the interactivity profile is `readonly`, then the `overrideVisualInteractivity` property is `true` and all `visualSettings` parameters are `false`. If the interactivity profile is `interactive`, then the `overrideVisualInteractivity` property is set to `false`, all `visualSettings` parameters are empty, and the visual interactivity settings for the individual visuals are used.
* When a custom interactivity profile is saved for a dashboard and `overrideVisualInteractivity` is set to `false`, then all `visualSettings` parameters are empty and the visual interactivity settings for the individual visuals are used. If `overrideVisualInteractivity` is set to `true`, then the `visualSettings` for the dashboard are used.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`"ACTIONS": false`</td>

      <td>
        When set to `true`, users can invoke an action using the **Actions** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). When set to `false`, they cannot invoke actions.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"ACTIONS_ACTION": false`</td>

      <td>
        When set to `true`, users can invoke an action using the **Actions** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu). When set to `false`, they cannot invoke actions.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"COLORS": false`</td>

      <td>
        When set to `true`, users can change the color palette used by the visual.

        <br />

        When set to `false`, they cannot change the color palette . The color settings (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-color.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=23086f978c60bc7f5eaff8f93de81ae3" alt="" width="28" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-color.png" />) [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) option is disabled and they cannot access the color sidebar.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"CONDITIONAL_FORMATTING": false`</td>

      <td>
        When set to `true`, users define conditional formatting for the visual.

        <br />

        When set to `false`, they cannot define conditional formatting. The conditional formatting [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) option is disabled and can not be accessed.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"COPY": false`</td>

      <td>
        When set to `true`, users can copy a visual using the **Copy Visual** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). When set to `false`, they cannot copy visuals.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"DETAILS_ACTION": false`</td>

      <td>
        When set to `true`, users can display additional information about a specific visual data element using the **Details** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu). When set to `false`, users cannot display additional information about a specific visual data element using the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu).

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"EXPORT_CSV": false`</td>

      <td>
        When set to `true`, users can Export the visual as a CSV file. When set to `false`, they cannot export the visual this way, and the UI no longer provides this export option. If all export settings are turned off, the export menu is removed.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"EXPORT_PNG_PDF": false`</td>

      <td>
        When set to `true`, users can Export the visual as a PNG or PDF file. When set to `false`, they cannot export the visual this way, and the UI no longer provides this export option. If all export settings are turned off, the export menu is removed.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"EXPORT_XLSX": false`</td>

      <td>
        When set to `true`, users can Export the visual as an Excel (.xlsx) file. When set to `false`, they cannot export the visual this way, and the UI no longer provides this export option. If all export settings are turned off, the export menu is removed.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"FILTER": false`</td>

      <td>
        When set to `true`, users can filter visual data using the **Filter** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) and to the left of the visual name on a visual, or display name if viewed in a dashboard. When set to `false`, they cannot filter visual data.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"FILTER_ACTION": false`</td>

      <td>
        When set to `true`, users can filter data using the **Filter** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu). When set to false, users cannot filter data using the **Filter** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu).

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"FORMAT": false`</td>

      <td>
        When set to `true`, users can [Format specific data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#format-numeric-table-data-using-the-table-context-menu) in a visual. When set to `false`, they cannot format visual data.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"GROUPING": false`</td>

      <td>
        When set to `true`, users can change the **Group** field on the x-axis of the visual. When set to `false`, they cannot change the **Group** field.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"INFO": false`</td>

      <td>
        When set to `true`, users can see visual details in the Info sidebar menu. When set to `false`, they cannot see those details.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"KEYSET": false`</td>

      <td>
        When set to `true`, users can create a keyset from the visual data using the **Create Keyset** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). When set to `false`, users cannot create keysets.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"KEYSET_ACTION": false`</td>
      <td>When set to `true`, users can create a keyset from a selected data point using the **Keyset** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu). When set to `false`, users cannot create a keyset using the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu).</td>
    </tr>

    <tr>
      <td>`"LINK_ACTION": false`</td>

      <td>
        When set to `true`, users can link to another dashboard using the **Link** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu). When set to `false`, users cannot link to another dashboard using the **Link** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu).

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"MAXIMIZE": false`</td>

      <td>
        When set to `true`, users can maximize a visual for optimal viewing. When set to `false`, they cannot maximize a visual.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"METRICS": false`</td>

      <td>
        When set to `true`, users can change metric fields (other than a metric that might be in the **Group** field) on the axes for the visual. This setting also controls whether a user can control the aggregation method (SUM, AVG, MIN, MAX, etc.) used for [metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#metrics) in a table. When set to `false`, users cannot change metric fields or control the aggregation method used for metrics on a visual.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"overrideVisualInteractivity": false`</td>

      <td>
        When set to `true`, the individual visual interactivity settings for each visual on the dashboard are overridden and ignored. Instead, the visual interactivity settings set for the dashboard are used for all of the visuals in the dashboard. These settings are only applied to the visuals when they are used in this dashboard and not universally.

        <br />

        When set to `false`, the individual visual interactivity settings for each visual are honored.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"REMOVE": false`</td>

      <td>
        When set to `true`, users can remove a visual using the **Remove Visual** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). When set to `false`, users cannot remove visuals.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"RENAME": false`</td>

      <td>
        When set to `true`, users can change the display name of a visual. When set to `false`, they cannot change the display name of visual.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"RULERS": false`</td>

      <td>
        When set to `true`, users can add visual reference lines and customize the markers used on the metric axis.

        <br />

        When set to `false`, users cannot add reference lines and markers. The ruler settings (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-ruler.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=cd5637e5e6fa36eb5d66445f626f44b4" alt="" width="22" height="26" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '22px', height: '26px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-ruler.png" />) [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) option is disabled when this switch is off and you cannot access the ruler sidebar.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"SAVE_AS": false`</td>

      <td>
        When set to `true`, users can save a shared visual (make a copy) using a new name. When set to `false`, they cannot save the shared visual with a new name and the option is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"SAVE": false`</td>

      <td>
        When set to `true`, users can save the shared visual. When set to `false`, they cannot save the shared visual and the option is not available in the UI.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"SETTINGS": false`</td>

      <td>
        When set to `true`, users can specify settings for the visual using the visual settings option on the [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).

        <br />

        When set to `false`, users cannot specify visual settings. The visual settings (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=74af55ee44cca52b9f7f4ae157440a81" alt="Select the settings icon on the sidebar menu to open settings options" width="28" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png" />) [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) option is disabled and users cannot access the visual settings sidebar.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"SORT": false`</td>

      <td>
        When set to `true`, users can sort and limit the data in a visual.

        <br />

        When set to `false`, users cannot sort and limit visual data. The sort and limit (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-sort.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=4fc0c54db55344620adb5335ad462296" alt="" width="15" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '15px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-sort.png" />) [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) option is disabled when this switch is off and you cannot access the Sort & Limit sidebar.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"TIMEBAR_FIELD": false`</td>

      <td>
        When set to `true`, users can change the time field on the [time bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar). When set to `false`, users cannot change the time field.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"TIMEBAR_PANEL": false`</td>

      <td>
        When set to `true`, users can show and hide the time bar on a visual. When set to `false`, the time bar is hidden for this visual.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"TREND_ACTION": false`</td>

      <td>
        When set to `true`, users can view trends for a selected data point using the **Trend** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu). When set to `false`, users cannot view trends for a selected data point using the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu).

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"VISUAL_STYLE": false`</td>

      <td>
        When set to `true`, users can change the type of visual to another type.

        <br />

        When set to `false`, users cannot change the visual type. The re-visualize (was *visual style*) settings (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chttype.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=559a7028c6be23336aa84a37bdb73f20" alt="" width="26" height="25" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '26px', height: '25px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chttype.png" />) [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) option is disabled when this switch is off and users cannot access this sidebar menu option.

        <br />

        Type: boolean
      </td>
    </tr>

    <tr>
      <td>`"ZOOM_ACTION": false`</td>

      <td>
        When set to `true`, users can drill down in a selected data point on a visual using the **Drill Down** (formerly *Zoom*) option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu). When set to `false`, users cannot drill down in a selected data point on a visual using the **Drill Down** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu).

        <br />

        Type: boolean
      </td>
    </tr>
  </tbody>
</table>

<h3 id="sources-inventory-interactivity-parameters-interactivityvalue">
  Sources Inventory Interactivity Parameters (`InteractivityValue` Property)
</h3>

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

<h3 id="editor-configuration-editorusersettings-property">
  Editor Configuration (`editorUserSettings` Property)
</h3>

Use the `editorUserSettings` property to configure the interactivity parameters for the dashboard.

```json theme={null}
{
			"type": "dashboard",
			editorUserSettings: {
			isViewMode: true,
			canSwitchMode: false,
			allowInteractivityConfiguration: false,
			}
		}
```

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`isViewMode`</td>

      <td>
        When set to `true`, the dashboard opens for editors and creators in View mode. When set to `false`, the dashboard opens for editors and creators in Edit mode.

        <br />

        Type: boolean

        <br />

        Default: `false`
      </td>
    </tr>

    <tr>
      <td>`canSwitchMode`</td>

      <td>
        When set to `true`, editors can toggle between View and Edit modes. When set to `false`, editors can not toggle between View and Edit modes.

        <br />

        Type: boolean

        <br />

        Default: `true`
      </td>
    </tr>

    <tr>
      <td>`allowInteractivityConfiguration`</td>

      <td>
        When set to `true`, editors can change interactivity settings for the dashboard and visuals. When set to `false`, editors can not change interactivity settings for the dashboard and visuals.

        <br />

        Type: boolean

        <br />

        Default: `false`
      </td>
    </tr>
  </tbody>
</table>

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

#### Caching Interactivity Settings

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
