> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Single Metric Visuals

## Arc Gauges

Arc gauges are based on a single metric. They are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

## Display Arc Gauge Label Description

You can show a description of the arc gauge label. The label shows the value that is plotted, but the label description shows the calculation for the plotted value in the format `<actual value>/<maximum value>`. By default, the label description is not shown.

**To display the arc gauge label description:**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. Select the settings icon on the [visual sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Settings sidebar menu for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/settings-arcs-23-1.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=bd5fe45e960079a84df948fae4c4b9ea" alt="define the label positions and values in this work area" width="352" height="336" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/settings-arcs-23-1.png" />

3. Slide the **Show label description** switch on (to the right).

   The changes are made to the arc gauge and the label description is shown.

4. Optionally, enable **Display Null as Zero** by sliding the switch on (to the right).

5. Select the save icon to save the visual.

## Adjust the Arc Gauge Value Range

**Configure minimum and maximum arc gauge values for a specific arc gauge**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. Select the rulers icon on the [visual sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Rulers sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/rulers-arcs.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=198bab049ea7f63bb40e73d816141046" alt="" width="325" height="698" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/rulers-arcs.png" />

3. In the **Metric** section of the sidebar, configure the settings as described below.

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>**Min**</td>
         <td>Specify the minimum value for the gauge. Select the **Auto** checkbox to have Self-Service Analytics automatically determine the minimum value from the data for the arc gauge metric.</td>
       </tr>

       <tr>
         <td>**Min**</td>

         <td>
           If the **Static maximum value** switch is on, specify the maximum value for the gauge. Select the **Auto** checkbox to have Self-Service Analytics automatically determine the maximum value from the data for the arc gauge metric.

           <br />

           If the **Static maximum value** switch is off, select a second metric to use for the maximum value of the gauge. For example, if the arc metric was the number of apples, you might select a second metric representing the total number of fruit. In this way, the arc gauge would plot the total number of apples as it relates to the total number of fruit.
         </td>
       </tr>

       <tr>
         <td>**Static maximum value**</td>

         <td>
           This switch allows you to plot the arc gauge metric as it relates to a second metric.

           <br />

           By default, this switch is on. When it is on, the maximum value of the arc gauge is determined by the **Max** setting for the arc metric or the maximum value of the data for the selected arc metric. Only the values of the selected arc metric are used.

           <br />

           You can select and format the numeric attribute used for this field. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting).

           <br />

           Slide the **Static maximum value** switch off (to the left) to select a second metric to use for the maximum value of the gauge.
         </td>
       </tr>
     </tbody>
   </table>

4. Select **Apply**. The changes are made to the arc gauge.

5. Select the save icon to save the visual.

## Adjust Arc Gauge Color Metric Value Range

The color metric determines the color used by the arc gauge. Color settings are mostly specified on the Color sidebar for the arc gauge, but you can adjust the range for the color metric of an arc gauge using the Rulers sidebar.

**Configure minimum and maximum values for the color metric selected for a specific arc gauge**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. Select the rulers icon on the [visual sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Rulers sidebar for the visual appears.

3. In the **Color Metric** section of the sidebar, configure the settings as described below.

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>**Min**</td>
         <td>Specify the minimum value for the color metric. Select the **Auto** checkbox to have Self-Service Analytics automatically determine the minimum value from the data for the color metric.</td>
       </tr>

       <tr>
         <td>**Max**</td>

         <td>
           If the **Static maximum value** switch is on, specify the maximum value of the color metric used for the arc gauge. Select the **Auto** checkbox to have Self-Service Analytics automatically determine the maximum value from the color metric.

           <br />

           If the **Static maximum value** switch is off, select a second metric to use for the maximum value of the color metric used for the arc gauge.
         </td>
       </tr>

       <tr>
         <td>**Static maximum value**</td>

         <td>
           This switch allows you to set the color of the arc gauge as it relates to a second metric.

           <br />

           By default, this switch is on. When it is on, the color range of the arc gauge is determined by the **Max** setting for the color metric or the maximum value of the data for the selected color metric. Only the values of the selected color metric are used.

           <br />

           Slide the **Static maximum value** switch off (to the left) to select a different metric to use for the color of the gauge.
         </td>
       </tr>
     </tbody>
   </table>

4. Select **Apply**. The changes are made to the arc gauge.

5. Select the save icon to save the visual.

## Display Arc Gauge Values as Percentages

When you first create an arc gauge visual, the values shown on the gauge are the raw values of the plotted metric. You can alter this to show the values as a percentage of the maximum value of the gauge.

**Display arc gauge values as percentages in an a specific arc gauge**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. Select the settings icon on the [visual sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Settings sidebar for the visual appears. The arc gauge shows raw values by default.

3. Under **Show Values As**, select **Relative**. The arc gauge values are shown as percentages.

   To show raw values again, select **Absolute**. This is the default setting.

4. After making your display choice, select the save icon to save the visual.

Adjust the percentage to round it to an appropriate number of decimal places (or none) by adjusting [the format](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) for the value.

## Configure Colors for a Specific Arc Gauge

**Specify the color settings for a specific arc gauge using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. Select the color icon on the [visual sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar menu for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-arc-23-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=e85612ef7589abd6519bdce58340e23b" alt="define the color settings for this visual" width="317" height="777" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-arc-23-1.png" />

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

         <td>
           Enable or disable to display a dynamic legend in this visual. Dynamic legends allow you to temporarily add or remove data shown in the visual.

           <br />

           * For distinct color styles, select a data point in the legend to turn it off and on in the visual.
           * For gradient color styles, use the legend’s gradient slider to show and hide your data.

           <br />

           If available, enable or disable a static legend for this visual.
         </td>
       </tr>

       <tr>
         <td>Label Color</td>
         <td>The inherited label color from the theme. Select to clear the **Inherit from theme** checkbox to define a different color manually.</td>
       </tr>

       <tr>
         <td>Label Description Color</td>
         <td>Select a color for the label description. Select the **Inherit from theme** checkbox to use the color palette specified by the [theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).</td>
       </tr>

       <tr>
         <td>Color Metric</td>
         <td>Select the metric that affects the segment color in the visual. You can also define the default aggregation function used for the metric values: SUM, AVG, MAX, MIN, or (for some data sources) LAST VALUE. See [Metric Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#metric-aggregation-functions).</td>
       </tr>

       <tr>
         <td>Color Palette</td>
         <td>If a color palette is specified for this visual type in the data source defaults, select the color palette for this specific visual. If a color range is selected for KPI visuals in the data source defaults, this setting is not available. Select the **Inherit from theme** checkbox to use the color palette specified by the [theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).</td>
       </tr>

       <tr>
         <td>Color Mode</td>
         <td>Select **Distinct Colors** or **Gradient** to identify the way colors are used on the screen. Your selection determines if specific distinct colors or a gradient of colors are used.</td>
       </tr>

       <tr>
         <td>Threshold Mode</td>

         <td>
           If you select the **Gradient** color mode, this setting cannot be changed.

           <br />

           If you select the **Distinct Colors** color mode, select either **Auto** or **Manual** from the drop-down list.

           <br />

           * **Auto**: Automatically assigns thresholds and colors for the visual.
           * **Manual**: You can change the thresholds and colors used in the visual.
         </td>
       </tr>

       <tr>
         <td>Number of colors</td>
         <td>Specify the number of colors to use for the visual.</td>
       </tr>

       <tr>
         <td>Color Rules</td>

         <td>
           Change the assigned color for each color used for the visual.

           <br />

           If you specify **Manual** threshold mode, select the thresholds used for color settings in the visual.
         </td>
       </tr>

       <tr>
         <td>Thresholds in Percentage</td>

         <td>
           This switch allows you to set the color thresholds for the arc gauge in percentages. Slide the **Thresholds in percentage** switch on (to the right) to specify color thresholds in percentages.

           <br />

           By default, this switch is off and color threshold settings must be raw values.

           <br />

           This setting is only available if **Threshold Mode** is set to **Manual**.
         </td>
       </tr>
     </tbody>
   </table>

4. Close the Color sidebar and the color settings are dynamically applied to the visual.

5. Select the save icon to save the dashboard and the visual with its updated settings.

<h3 id="configure-colors-for-a-specific-arc-gauge-understand-visual">
  Understand Visual Color Condition Thresholds
</h3>

You can set threshold color conditions for metric-based visuals. At least two color settings are required. In addition, thresholds are specified between each color setting. (So three color settings require two threshold settings; four color settings require three threshold settings, etc.)

* The color for Color 1 is used when the value of the color metric is less than the first threshold value.

* The color for Color 2 is used when the value of the color metric falls between the first and second threshold values.

* If only three colors are used for the visual, the color for Color 3 is used when the value of the color metric is greater than or equal to the second threshold value.

  If more than three colors are used, the color for Color 3 is used when the value of the color metric falls between the second and third threshold values.

  When more than three colors are used, the colors continue to be applied in this pattern for all threshold settings; any color metric values greater than the last threshold setting have the final color applied.

You can have Self-Service Analytics automatically set the thresholds or you can manually set them.

For information about supported color encoding, see [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

<h2 id="bullet-gauges">
  Bullet Gauges
</h2>

Bullet gauges are based on a single metric. The metric is mapped against a background bar that shows value ranges using color. A metric scale is also shown. Finally, a small vertical bar represents a marker for the target value of the metric. Bullet gauges are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bullet-gauge.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=b4db974a27afcd3efd129777336403d2" alt="" width="710" height="181" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bullet-gauge.png" />

This topic describes:

* [Configure Settings for a Specific Bullet Gauge](#configure-settings-for-a-specific-bullet-gauge)
* [Adjust the Bullet Gauge Value Range](#adjust-the-bullet-gauge-value-range)
* [Configure Colors for a Specific Bullet Gauge](#configure-colors-for-a-specific-bullet-gauge)
* [Understand Visual Color Condition Thresholds](#configure-colors-for-a-specific-bullet-gauge-understand-visual)
* Understand Visual Color Condition Thresholds

<h3 id="configure-settings-for-a-specific-bullet-gauge">
  Configure Settings for a Specific Bullet Gauge
</h3>

**Change the settings for a specific bullet gauge**

1. Edit the bullet gauge you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=74af55ee44cca52b9f7f4ae157440a81" alt="Select the settings icon on the sidebar menu to open settings options" width="28" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Bullet Gauge Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bullet-settings.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=26c77b9b2f8da02c6b96addba5c2da0a" alt="" width="437" height="625" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bullet-settings.png" />

4. Alter the settings as needed:

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>**Orientation**</td>
         <td>Select an orientation (horizontal or vertical) for the bullet gauge.</td>
       </tr>

       <tr>
         <td>**Target Value**</td>
         <td>Slide the **Target Value** slider on (to the right) to show the target value bar on the gauge.</td>
       </tr>

       <tr>
         <td>**Show label description**</td>

         <td>
           Slide the **Show label description** slider on (to the right) to show label description on the gauge. The label description includes the metric value and maximum value in addition to the metric name.

           <br />

           For example, when this slider is on, if the Planned Sales metric value is 15,000 and its maximum value is 32,000, the label description would read "Planned Sales 15,000 of 32,000". When this slider is off, only "Planned Sales" would show.

           <br />

           <Note>
             When **Show Values As** is set to **Relative** and **Show label description** is on, the percentage of the metric value in relation to the maximum value is also shown.
           </Note>
         </td>
       </tr>

       <tr>
         <td>**Show Values As**</td>
         <td>Select how values should be shown on the gauge. Select **Absolute** to show raw data values. Select **Relative** to show percentages.</td>
       </tr>
     </tbody>
   </table>

5. Select <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" /> to save the dashboard and the visual with its updated settings.

<h3 id="adjust-the-bullet-gauge-value-range">
  Adjust the Bullet Gauge Value Range
</h3>

**Configure minimum and maximum values for a specific bullet gauge**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. Select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-ruler.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=cd5637e5e6fa36eb5d66445f626f44b4" alt="" width="22" height="26" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '22px', height: '26px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-ruler.png" /> on the [visual sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Rulers sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/rulers-bullets.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=c7972af9cc31b1e1479ebb4081d0bdd6" alt="" width="436" height="631" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/rulers-bullets.png" />

3. In the **Metric** section of the sidebar, configure the settings as described below.

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>**Min**</td>
         <td>Specify the minimum value for the gauge. Select the **Auto** checkbox to have Self-Service Analytics automatically determine the minimum value from the data for the bullet gauge metric.</td>
       </tr>

       <tr>
         <td>**Max**</td>

         <td>
           If the **Static maximum value** switch is on, specify the maximum value for the gauge. Select the **Auto** checkbox to have Self-Service Analytics automatically determine the maximum value from the data for the bullet gauge metric.

           <br />

           If the **Static maximum value** switch is off, select a second metric to use for the maximum value of the gauge. For example, if the bullet gauge metric was the number of apples, you might select a second metric representing the total number of fruit. In this way, the bullet gauge would plot the total number of apples as it relates to the total number of fruit.
         </td>
       </tr>

       <tr>
         <td>**Static maximum value**</td>

         <td>
           This switch allows you to plot the bullet gauge metric as it relates to a second metric.

           <br />

           By default, this switch is on. When it is on, the maximum value of the bullet gauge is determined by the **Max** setting for the bullet gauge metric or the maximum value of the data for the selected bullet gauge metric. Only the values of the selected bullet gauge metric are used.

           <br />

           You can select and format the numeric attribute used for this field. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting).

           <br />

           Slide the **Static maximum value** switch off (to the left) to select a second metric to use for the maximum value of the gauge.
         </td>
       </tr>

       <tr>
         <td>**Set Target As**</td>
         <td>Select how the target value for the bullet gauge metric is set. Select **Value** if a raw data value should be used. Select **Percent of Maximum** if a percentage of the maximum value should be used.</td>
       </tr>

       <tr>
         <td>**Target Value**</td>

         <td>
           Specify a target value for the bullet gauge metric.

           <br />

           If **Set Target** As is set to **Percent of Maximum**, this field name changes to **Target Value (%)**. In this case, remember to specify the target value as a percentage of the maximum value for the gauge.
         </td>
       </tr>
     </tbody>
   </table>

4. Select **Apply**. The changes are made to the bullet gauge.

5. Select the Save icon (<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" />) to save the visual.

<h3 id="configure-colors-for-a-specific-bullet-gauge">
  Configure Colors for a Specific Bullet Gauge
</h3>

**Specify the color settings for a specific bullet gauge using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-color.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=23086f978c60bc7f5eaff8f93de81ae3" alt="" width="28" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-color.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-bullet.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=0e0b25f7115cfdffb92844b2bfde2da6" alt="" width="333" height="858" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-bullet.png" />

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

         <td>
           Enable or disable to display a dynamic legend in this visual. Dynamic legends allow you to temporarily add or remove data shown in the visual.

           <br />

           * For distinct color styles, select a data point in the legend to turn it off and on in the visual.
           * For gradient color styles, use the legend’s gradient slider to show and hide your data.

           <br />

           If available, enable or disable a static legend for this visual.
         </td>
       </tr>

       <tr>
         <td>Bar Color</td>

         <td>
           Select the bar color for the gauge.

           <br />

           If **Inherit from Theme** is selected, the color palette is determined by the theme selected for the Self-Service Analytics UI. You cannot select the color in this field to access the color dialog.
         </td>
       </tr>

       <tr>
         <td>Target Color</td>

         <td>
           Select the color for the target bar.

           <br />

           If **Inherit from Theme** is selected, the color palette is determined by the theme selected for the Self-Service Analytics UI. You cannot select the color in this field to access the color dialog.
         </td>
       </tr>

       <tr>
         <td>Color Metric</td>

         <td>
           Select the metric that affects the segment color in the visual. You can also define the default aggregation function used for the metric values: SUM, AVG, MAX, MIN, or (for some data sources) LAST VALUE.

           <br />

           See [Metric Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#metric-aggregation-functions).
         </td>
       </tr>

       <tr>
         <td>Color Palette</td>

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

           **Auto** will automatically assign thresholds and colors for the visual. **Manual** allows you to change the thresholds and colors used on the visual.
         </td>
       </tr>

       <tr>
         <td>Number of colors</td>
         <td>Specify the number of colors to use for the visual.</td>
       </tr>

       <tr>
         <td>Color Rules</td>

         <td>
           Color rules allow you to change the colors for each color used for the visual. In addition, if you specified a **Manual** threshold mode, you can select the thresholds used for color settings in the visual.

           <br />

           See [Understand Visual Color Condition Thresholds](#configure-colors-for-a-specific-bullet-gauge-understand-visual).
         </td>
       </tr>
     </tbody>
   </table>

4. Close the Color sidebar and the color settings are dynamically applied to the visual.

5. Select the save icon to save the dashboard and the visual with its updated settings.

<h4 id="configure-colors-for-a-specific-bullet-gauge-understand-visual">
  Understand Visual Color Condition Thresholds
</h4>

You can set threshold color conditions for metric-based visuals. At least two color settings are required. In addition, thresholds are specified between each color setting. (So three color settings require two threshold settings; four color settings require three threshold settings, etc.)

* The color for Color 1 is used when the value of the color metric is less than the first threshold value.

* The color for Color 2 is used when the value of the color metric falls between the first and second threshold values.

* If only three colors are used for the visual, the color for Color 3 is used when the value of the color metric is greater than or equal to the second threshold value.

  If more than three colors are used, the color for Color 3 is used when the value of the color metric falls between the second and third threshold values.

  When more than three colors are used, the colors continue to be applied in this pattern for all threshold settings; any color metric values greater than the last threshold setting have the final color applied.

You can have Self-Service Analytics automatically set the thresholds or you can manually set them.

For information about supported color encoding, see [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

<h2 id="kpi-charts">
  KPI Charts
</h2>

KPI charts are based on two metrics: a primary metric and a comparison metric. They allow you to visualize the results of comparing the metrics and show positive or negative dynamics. KPI charts are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

This topic describes:

* [Configure Settings for a Specific KPI Chart](#configure-settings-for-a-specific-kpi-chart)
* [Configure Colors for a Specific KPI Chart](#configure-colors-for-a-specific-kpi-chart)

<h3 id="configure-settings-for-a-specific-kpi-chart">
  Configure Settings for a Specific KPI Chart
</h3>

**Change the settings for a specific KPI chart**

1. Edit the KPI chart you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select settings <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=74af55ee44cca52b9f7f4ae157440a81" alt="Select the settings icon on the sidebar menu to open settings options" width="28" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The KPI Chart Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/kpi-settings-22-4.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=f79a4978b80dbf0142b8f6620d14915b" alt="" width="349" height="745" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/kpi-settings-22-4.png" />

4. Alter the settings as needed:

   #### General

   | Setting | Description |
   | - | - |
   | Display Null as Zero | Enable **Display Null as Zero** to show null values as zeros. |

   #### Comparison Mode

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Show Comparison</td>
         <td>Enable **Show Comparison** to show comparison data.</td>
       </tr>

       <tr>
         <td>Show Variance</td>
         <td>Enable **Show Variance** to see variance data.</td>
       </tr>

       <tr>
         <td>Show Arrow Indicators</td>
         <td>Enable **Show Arrow Indicator** to show up and down arrows that indicate whether the change is positive or negative.</td>
       </tr>

       <tr>
         <td>Show Comparison</td>
         <td>Enable **Show Comparison** to show comparison data.</td>
       </tr>

       <tr>
         <td>Comparison Format</td>

         <td>
           If the **Show Comparison** option is enabled, select an option to show variance data as raw data or as percentages.

           <br />

           Select **Value** to see raw data differences; select **Percentage** to see percentages.
         </td>
       </tr>
     </tbody>
   </table>

5. Optionally, edit the number format for this visual. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting).

6. Select the **Save** icon <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" /> to save the visual and dashboard or the visual with its updated settings.

<h3 id="configure-colors-for-a-specific-kpi-chart">
  Configure Colors for a Specific KPI Chart
</h3>

Define the look and feel of your KPI using the Color sidebar to define a Color Palette and Color Rules.

You can apply a color palette to the Color Metric of the visual, and color rules to one or more parts of the visual. Optionally, add conditions to color rules to change the appearance of your visual when specific conditions are met.

Rules are applied in the order they are listed in the Color Rules work area. If two rules are applied to the same Target, the first rule is applied, and may be overwritten by the second rule. Select and drag a rule to reorder as needed.

**Specify a Color Palette for the Color Metric**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the colors icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-kpi-23-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=e89e1bb40968beff2c224b702d3d089d" alt="Define your color rules for KPI visuals here" width="350" height="539" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-kpi-23-2.png" />

3. Select the color rule for the Color Metric. In this example, the top rule, Volume Metric, which displays the gradient color indicator. The Color Metric work area opens.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-metric-kpi-23-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=c6b5c21775097ea2687ed83631d16bab" alt="Define your color rules for the color metric here" width="349" height="804" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-metric-kpi-23-2.png" />

4. Configure the color settings as described below. Supported color specifications are described in [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Color Metric</td>

         <td>
           Select to open the **Choose a Field** work area. Select a field to use as the Color Metric for this visual, then select **Continue** to return to the Color Metric work area.

           <br />

           The metric you select affects the segment color in the visual. You can also define the default aggregation function used for the metric values: SUM, AVG, MAX, MIN, or (for some data sources) LAST VALUE. See [Metric Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#metric-aggregation-functions).
         </td>
       </tr>

       <tr>
         <td>Select Where To Apply Formatting</td>

         <td>
           Select an element of the visual to use the color palette.

           <br />

           Target options include: **Background**, **Metric**, **Label text**, **Comparison data**, **Up arrow color**, or **Down arrow color**.
         </td>
       </tr>

       <tr>
         <td>Formatting</td>
         <td>Change or define the **Color Palette**, enable or disable **Inherit from Theme**, **Reset Palette**, define a **Color Mode**, **Threshold Mode**, and **Number of Colors** available in Color Rules.</td>
       </tr>

       <tr>
         <td>Inherit from Theme</td>

         <td>
           If **Inherit from Theme** is selected, the color palette is determined by the theme selected for the Self-Service Analytics UI. To override the palette selected by the theme, clear the **Inherit from Theme** checkbox. You can then either:

           <br />

           * Select a different color palette from predefined color palettes
           * Change the colors defined in the next work area, Color Rules
         </td>
       </tr>

       <tr>
         <td>Reset Palette</td>
         <td>Select to reset the color palette if you have made changes to any individual colors in the next work area, Color Rules.</td>
       </tr>

       <tr>
         <td>Color Mode</td>
         <td>Select **Distinct Colors** or **Gradient** to identify the way colors are used on the screen. Either specific distinct colors will be used or a gradient of colors will be used.</td>
       </tr>

       <tr>
         <td>Threshold Mode</td>
         <td>If you selected the **Gradient** color mode, this setting cannot be changed. If you selected the Distinct Colors color mode, select either **Auto** or **Manual** from the drop-down list. **Auto** will automatically assign thresholds and colors for the visual. **Manual** allows you to change the thresholds and colors used on the visual.</td>
       </tr>

       <tr>
         <td>Number of Colors</td>
         <td>Select the number of colors to use in the next work area, Color Rules.</td>
       </tr>

       <tr>
         <td>Color Rules</td>
         <td>These Color Rules allow you to change the colors for each color used for the visual. In addition, if you specified a **Manual** threshold mode, you can select the thresholds used for color settings in the visual.</td>
       </tr>
     </tbody>
   </table>

5. Select Apply to apply your changes to the visual.

   <Note>
     If you delete the Color Metric rule, create a new one by selecting **Add Palette**.
   </Note>

**Specify the color rules and conditional formatting for a specific KPI chart using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the colors icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-kpi-23-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=e89e1bb40968beff2c224b702d3d089d" alt="Define your color rules for KPI visuals here" width="350" height="539" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-kpi-23-2.png" />

3. Select Add Rule to add a new color rule, or select a Color Rule to edit. The Color Rule work area opens.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-kpi-color-rule-23-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=c9e1d16963fb05ba973f43cdaa1c642e" alt="Define your color rule for a target in the visual here" width="349" height="483" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-kpi-color-rule-23-2.png" />

   <Note>
     Select the delete icon to delete a color rule or formatting definition.
   </Note>

4. Configure the color settings as described below. If a target is not assigned a rule, its color settings are inherited from the Self-Service Analytics theme, regardless of other settings. Supported color specifications are described in [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

   <table>
     <thead>
       <tr>
         <th colSpan={2}>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td colSpan={2}>Select When to Apply Formatting</td>

         <td>
           If **Always apply this rule** is disabled, you can select the add icon to define the conditions to apply your formatting for the selected **Target**.

           <br />

           See [Configure Conditional Formatting Rules](#configure-conditional-formatting-rules).
         </td>
       </tr>

       <tr>
         <td colSpan={2}>Always apply this rule</td>

         <td>
           Enable to always apply the formatting to the selected **Target**.

           <br />

           Disable to define conditions for applying this rule.
         </td>
       </tr>

       <tr>
         <td colSpan={2}>Select Where To Apply Formatting</td>
         <td>Select an element of the visual to use the color rules. Target options include: **Background**, **Metric**, **Label text**, **Comparison data**, **Up arrow color**, or **Down arrow color**.</td>
       </tr>

       <tr>
         <td colSpan={2}>Formatting</td>

         <td>
           Select the add icon to define the conditions to apply your formatting for the selected **Target**.

           <br />

           If all format definitions have been defined for the target, this option is not available. The format definitions you can apply to a target vary depending on the target selected.
         </td>
       </tr>

       <tr>
         <td />

         <td>Text Color</td>

         <td>
           The text color for the selected target.

           <br />

           Clear the **Inherit from Theme** checkbox to select a different color.

           <br />

           Select to enable the **Optimize contrast** option. This defines the color as **Auto**, and is black or white, depending on the color defined for the **Background** target.
         </td>
       </tr>

       <tr>
         <td />

         <td>Background Color</td>

         <td>
           Define the background color for the selected target.

           <br />

           For the **Metric**, **Label text**, and **Comparison data** targets, this color acts as a highlight color behind the text or numbers.

           <br />

           For the Background target, this defines the background color of the visual. This color is used to select the **Auto** color for **Text Color** definitions that use the **Optimize contrast** option.
         </td>
       </tr>

       <tr>
         <td />

         <td>Text Size</td>
         <td>Adjust the size of the selected target's text.</td>
       </tr>

       <tr>
         <td />

         <td>Bold, Italic, Underline</td>
         <td>Adjust the formatting of the selected target's text.</td>
       </tr>
     </tbody>
   </table>

5. Select **Apply** to apply your changes to the visual.

<h4 id="configure-conditional-formatting-rules">
  Configure Conditional Formatting Rules
</h4>

Select a group attribute to define the values for applying the formatting rule. Optionally, select the add icon to add a derived field or custom metric.

<img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/kpi-conditonal-format.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=f23dcd2db65aa942e8f809e53f4d7007" alt="Select a group attribute to define when to apply formatting" width="349" height="570" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/kpi-conditonal-format.png" />

##### Metric

<table>
  <thead>
    <tr>
      <th>Selection</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Operator</td>

      <td>
        Select an operator to use. Options may include **Between**, **Equal**, **Not Equal**, **Greater Than**, **Greater Than or Equal**, **Less Than**, and **Less than or Equal**.

        <br />

        Depending on the Operator you select, different definition fields are available to use.
      </td>
    </tr>

    <tr>
      <td>From, To</td>
      <td>Define a value range for **Between**.</td>
    </tr>

    <tr>
      <td>Value</td>

      <td>
        Define a value for **Equal**, **Not Equal**, **Greater Than**, **Greater Than** or **Equal**, **Less Than**, and **Less than or Equal**.

        <br />

        * Numeric: Define a numeric value.
        * Variables: Define a variable value, such as `${User.attribute|true}`.
      </td>
    </tr>
  </tbody>
</table>

<h5 id="numbers-number-attribute-custom-metrics-count-of">
  Numbers, Number Attribute Custom Metrics, Count Of
</h5>

<table>
  <thead>
    <tr>
      <th>Selection</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Range</td>
      <td>Displays the range for this value.</td>
    </tr>

    <tr>
      <td>Aggregation</td>

      <td>
        Select the aggregation method you want to use. Available aggregation methods may include **Avg**, **Min**, **Max**, **Sum**, **Last Value**, **Count**, and **Distinct Count**.

        <br />

        For information about aggregation methods, see [Metric Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#metric-aggregation-functions).
      </td>
    </tr>

    <tr>
      <td>Operator</td>

      <td>
        Select an operator to use. Options may include **Between**, **Equal**, **Not Equal**, **Greater Than**, **Greater Than or Equal**, **Less Than**, and **Less than or Equal**.

        <br />

        Depending on the Operator you select, different definition fields are available to use.
      </td>
    </tr>

    <tr>
      <td>From, To</td>
      <td>Define a value range for **Between**and **Not Between**.</td>
    </tr>

    <tr>
      <td>Value</td>
      <td>Define a value for **Equal**, **Not Equal**, **Greater Than**, **Greater Than** or **Equal**, **Less Than**, and **Less than or Equal**.</td>
    </tr>
  </tbody>
</table>
