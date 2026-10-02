> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Map Visuals

Map visuals you can use with your data include marker maps, US region maps, and world country maps. Most data sources can support the maps available in Self-Service Analytics.

Elements map visuals support include:

* **Start Zoom** and **Max Zoom** settings.
* Support for the ISO-3166 standard.
* An initial map center definition: Include **Start Latitude** and **Start Longitude** coordinates. When used win combination with **Start Zoom**, you can specifically define your initial view for a visual.

<h2 id="marker-maps">
  Marker Maps
</h2>

Marker maps are supported by most Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference). To include your data, the data for marker maps must contain latitude and longitude fields.

Self-Service Analytics supports a variety of tile providers which offer an overlay design for the map visual types available in the program. These include: OpenStreetMap, MapQuest, and MapBox. MapQuest and MapBox require an API key.

<Note>
  If you select OpenStreetMap as your tile provider, you can optionally set a custom URL. See the [Global Settings tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#other-settings).
</Note>

Coordinates for this visual are shown by default as a tooltip when a user hovers over a marker point. You can disable this by toggling off the setting `Show Coordinates Int Tooltip`.

You can disable the **Limit** property to allow processing of all available data instead of limiting the rows processed to a user-defined number.

<Note>
  To edit the number format for this visual, edit Tooltip Fields in the Settings sidebar menu. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting).
</Note>

<h2 id="us-region-maps">
  US Region Maps
</h2>

US region maps are based on up to three attributes (state name, county, and zip code) and one metric. They are supported by most Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference), however the data must include state names to see results.

* The state name must be spelled out with the first letter capitalized. For example, **California** is an accepted format, not **CA**. For a list of valid state names, see [State Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/country-name-reference#state-name-reference).
* County names and zip codes can also be used to display results at the county and zip code level. These fields are not required: hide these values by selecting **None** for these fields in the Settings sidebar menu.

Self-Service Analytics supports a variety of tile providers which offer an overlay design for the map visual types available in the program. These include: OpenStreetMap, MapQuest, and MapBox. MapQuest, CloudMade and MapBox require an API key.

If you select OpenStreetMap as your tile provider, you can optionally set a custom URL. See the [Global Settings tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#other-settings).

<Note>
  To edit the number format for this visual, see [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting).
</Note>

### Use the Drill Down Function

If your US region map includes county and zip codes in your data, you can use the drill down function (formerly *zoom*) to display county and zip code-level results within a state.

**Drill down in to a county or zip code**

1. On your US region map, select a state. Select **Zoom** in the context menu. The map zooms in to the level of state counties.
2. On the state, select a county within the state. Select **Zoom** in the context menu. The map zooms in to the level of zip codes within that county.

<h2 id="world-maps">
  World Maps
</h2>

World maps are based on one attribute (country name) and two metrics. They are supported by most Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference), however the data must include country names to see results.

<Note>
  To edit the number format for this visual, see [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting).
</Note>

### Configure Colors for a US Region or World Map

**Specify the color settings for a specific map using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the color icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar for the visual appears.

3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Legend</td>
         <td>Slide the bar to the right if you want the legend to be displayed on the visual or to the left to hide the legend.</td>
       </tr>

       <tr>
         <td>Color Metric</td>
         <td>Select the metric that affects the segment color in the visual.</td>
       </tr>

       <tr>
         <td>\<type> Color Palette</td>

         <td>
           If **Inherit from Theme** is selected, the color palette is determined by the theme selected for the Self-Service Analytics UI.

           <br />

           To override the palette selected by the theme, clear the **Inherit from Theme** checkbox and select a different color palette.
         </td>
       </tr>

       <tr>
         <td>Color Mode</td>
         <td>Select **Distinct Colors** or **Gradient** to identify the way colors are used on the screen. Either specific distinct colors will be used or a gradient of colors will be used.</td>
       </tr>

       <tr>
         <td>Threshold Mode</td>

         <td>
           If you selected the **Gradient** color mode, this setting cannot be changed. If you selected the Distinct Colors color mode, select either **Auto** or **Manual** from the drop-down list.

           <br />

           **Auto** will automatically assign thresholds and colors for the visual. **Manual** enables you to change the thresholds and colors used on the visual.
         </td>
       </tr>

       <tr>
         <td>Number of colors</td>
         <td>Specify the number of colors to use for the visual.</td>
       </tr>

       <tr>
         <td>Color Rules</td>
         <td>Color rules allow you to change the colors for each color used for the visual. Additionally, if you specified a **Manual** threshold mode, you can select the thresholds used for color settings in the visual.</td>
       </tr>
     </tbody>
   </table>

4. Close the Color sidebar and the color settings are dynamically applied to the visual.

5. Select the save icon to save the dashboard and the visual with its updated settings.

#### Understand Visual Color Condition Thresholds

You can set threshold color conditions for metric-based visuals. At least two color settings are required. In addition, thresholds are specified between each color setting. (So three color settings require two threshold settings; four color settings require three threshold settings, etc.)

* The color for Color 1 is used when the value of the color metric is less than the first threshold value.

* The color for Color 2 is used when the value of the color metric falls between the first and second threshold values.

* If only three colors are used for the visual, the color for Color 3 is used when the value of the color metric is greater than or equal to the second threshold value.

  If more than three colors are used, the color for Color 3 is used when the value of the color metric falls between the second and third threshold values.

  When more than three colors are used, the colors continue to be applied in this pattern for all threshold settings; any color metric values greater than the last threshold setting have the final color applied.

You can have Self-Service Analytics automatically set the thresholds or you can manually set them.

For information about supported color encoding, see [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).
