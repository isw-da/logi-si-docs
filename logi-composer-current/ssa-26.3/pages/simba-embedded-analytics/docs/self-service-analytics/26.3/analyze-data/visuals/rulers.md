> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Rulers and Reference Lines

## Use Rulers

Rulers can be used to customize the markers used on the metric axis. You can change the (metric) axis range in a visual along with the markers along the axis. Customizing this range may help you focus your data exploration to specific data points. You can set minimum and maximum values for your axis, define the steps, enable the gridlines, and use a logarithmic scale.

Rulers functionality is available only for bar charts, line charts, and waterfall visuals. Controls for rulers are provided using the interactivity sidebar. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

Rulers can be customized for a visual using the Rulers sidebar.

See the following topics:

* [The Rulers Sidebar](#the-rulers-sidebar)
* [Enable and Disable Ruler Grid Lines](#enable-and-disable-ruler-grid-lines)
* [Configure the Ruler Y-Axis Range Settings](#configure-the-ruler-y-axis-range-settings)
* [Use the Ruler Log Scale Function](#use-the-ruler-log-scale-function)

<Note>
  Arc gauges use the Rulers sidebar to control some different settings than are used by most visuals. See [Single Metric Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc).
</Note>

<h2 id="the-rulers-sidebar">
  The Rulers Sidebar
</h2>

The Rulers sidebar for a visual allows you to customize the rulers and reference lines used by the visual. When you save or export your visual, the settings configured on the Rulers sidebar are saved or exported respectively.

**Access the Rulers sidebar**

1. Select the visual in the [Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery) or on a dashboard.

2. Select **Settings** on the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) to access the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual. Then select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-ruler.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=cd5637e5e6fa36eb5d66445f626f44b4" alt="" width="22" height="26" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '22px', height: '26px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-ruler.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Rulers sidebar opens.

   The sidebar consists of two sections: the (metric) ruler settings and, possibly, reference lines. If the visual does not support reference lines, this section is not available. See [Enable and Disable Ruler Grid Lines](#enable-and-disable-ruler-grid-lines) and [Use Reference Lines](#use-reference-lines).

   <Note>
     Arc gauges use the Rulers sidebar to control some different settings than are used by most visuals. See [Single Metric Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc).
   </Note>

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-rulers-new.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4c377f89e97a459756261ad7687ac8c3" alt="" width="293" height="713" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-rulers-new.png" />

3. Select **Apply** to apply any changes you make.

<h2 id="enable-and-disable-ruler-grid-lines">
  Enable and Disable Ruler Grid Lines
</h2>

Grid lines provide a visual cue between data elements and metric ranges in a visual. They are displayed as light gray lines on the visual canvas horizontally and vertically. When enabled, they extend from the tick marks on the axes.

Grid lines may help you to analyze and compare the data elements in your visual.

<Note>
  Arc gauges use the Rulers sidebar to control some different settings than are used by most visuals. See [Single Metric Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc).
</Note>

**Enable grid lines**:

1. Access the Rulers sidebar for the visual. See [The Rulers Sidebar](#the-rulers-sidebar).

2. In the **X Gridlines** section of the sidebar, select (check) the **X Axis** checkbox to enable vertical rulers on the visual.

3. In the **Y Gridlines** section of the sidebar, select (check)the **Y Axis** checkbox to enable horizontal rulers on the visual. By default, the **Y Axis** checkbox is selected.

   <Note>
     On a [combo chart](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#combo-charts), four y-axis checkboxes are available: **Y1 Axis**, **Y2 Axis**, **Y3 Axis**, and **Y4 Axis**. By default only the **Y1 Axis** checkbox is selected.
   </Note>

4. You can specify the minimum (**Min**) and maximum (**Max**) values of the metrics that are plotted. Also specify the value used between grid lines (the **Step**) shown on the chart. In all cases, you can select the **Auto** checkbox to have Self-Service Analytics automatically select the minimum, maximum, and step values automatically, based on the data.

   <Note>
     On a [combo chart](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#combo-charts), you can specify minimum, maximum, and step values for all four y-axes.
   </Note>

5. Select the **Log Scale** checkbox for any metric to change the axis based on orders of magnitude of the metric selected for that axis. See [Use the Ruler Log Scale Function](#use-the-ruler-log-scale-function).

6. Select **Apply** to apply the ruler settings to the visual.

**Disable grid lines**

1. Access the Rulers sidebar for the visual. See [The Rulers Sidebar](#the-rulers-sidebar).

2. In the **Rulers** section of the sidebar, clear the **X Axis** checkbox to disable vertical rulers on the visual. Clear the **Y Axis** checkbox to disable horizontal rulers on the visual.

   <Note>
     On a [combo chart](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#combo-charts), four axis checkboxes are available: **Y1 Axis**, **Y2 Axis**, **Y3 Axis**, and **Y4 Axis**. Clear the appropriate checkboxes to disable horizontal rulers for the appropriate combo chart dependent variables.
   </Note>

3. Select **Apply** to apply the ruler settings to the visual.

<h2 id="use-the-ruler-log-scale-function">
  Use the Ruler Log Scale Function
</h2>

The log scale function changes the axis based on orders of magnitude of the metric selected for that axis. A log scale is nonlinear and best used when there is a large range in quantity. Log scales can only be used for positive values. In addition, when this option is selected, the **Auto** option is enabled for **Min**, **Max**, and **Step**.

The scale is built for whole the data range.

To enable the log scale function for the visual, select the **Log Scale** checkbox to enable. To disable, clear the checkbox.

<Warning>
  If your dataset includes zero values or negative values, the log scale function will not work as expected.
</Warning>

<Note>
  The Log Scale function is not available for arc gauges. Arc gauges use the Rulers sidebar to control some different settings than are used by most visuals. See [Single Metric Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc).
</Note>

<h2 id="configure-the-ruler-y-axis-range-settings">
  Configure the Ruler Y-Axis Range Settings
</h2>

The y-axis range settings on the Ruler sidebar control the minimum and maximum values for the metric shown in the visual. You can configure the default values for Min, Max, and Step. When the Rulers sidebar is initially opened, these settings are set to **Auto**.

To customize the range, clear the **Auto** checkbox next to the **Min** and **Max** boxes and then enter your custom value ranges in the boxes. Customizing the axis in this way can create a view into your data that drills into specific information, explores anomalies, and otherwise explores more relevant information.

You can further this exploration by clearing the **Auto** checkbox next to **Step**, and specifying the interval for the tick marks along the y-axis. Steps can be specified down to the tenth place, or one decimal point. For example, you can step the tick marks by .5 tenths. If you specify a step that cannot be displayed on the axis, the default minimal step value is applied.

<h2 id="use-reference-lines">
  Use Reference Lines
</h2>

Reference lines on a visual can be used to mark limits, thresholds, and critical values. They can mark both positive and negative values on an axis. Multiple reference lines can be added in a visual.

Reference lines are available only for bar and line charts. Controls are provided using the Rulers interactivity sidebar. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

Reference lines can be customized for a visual using the Rulers sidebar.

See the following topics:

* [The Rulers Sidebar](#the-rulers-sidebar)
* [Create a Reference Line](#create-a-reference-line)
* [Modify a Reference Line](#modify-a-reference-line)
* [Delete a Reference Line](#delete-a-reference-line)

<h2 id="create-a-reference-line">
  Create a Reference Line
</h2>

You can add multiple reference lines to a visual.

**Create a reference line on a visual**

1. Access the Rulers sidebar for the visual. See [The Rulers Sidebar](#the-rulers-sidebar).

2. In the **Reference Lines** section of the sidebar, select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> to start a new reference line definition.

3. Fill in the following fields for the reference line as needed:

   * **Title** - Specify the name for the line. The default name of the line is Reference line #.
   * **Position** - By default, the reference line is added to the middle of the visible axis. You can specify a different position on the axis by either entering a specific number value. The reference line changes its position depending on your input.
   * **Color** - Select the desired color for the line.
   * **Width** - Specify the line’s thickness: enter a specific value or use the slider.
   * **Line type** - Select from the following types: Solid, Dashed, or Dotted.

4. Select **Apply** to apply the reference line to the visual.

<h2 id="modify-a-reference-line">
  Modify a Reference Line
</h2>

You can modify a visual's reference lines using the Rulers sidebar.

**Modify a reference line on a visual**

1. Access the Rulers sidebar for the visual. See [The Rulers Sidebar](#the-rulers-sidebar).

2. In the **Reference Lines** section of the sidebar, locate the reference line you want to modify.

3. Modify the fields for the reference line as needed:

   * **Title** - Specify the name for the line. The default name of the line is Reference line #.
   * **Position** - By default, the reference line is added to the middle of the visible axis. You can specify a different position on the axis by either entering a specific number value. The reference line changes its position depending on your input.
   * **Color** - Select the desired color for the line.
   * **Width** - Specify the line’s thickness: enter a specific value or use the slider.
   * **Line type** - Select from the following types: Solid, Dashed, or Dotted.

4. Select **Apply** to apply the reference line changes to the visual.

<h2 id="delete-a-reference-line">
  Delete a Reference Line
</h2>

**Delete a reference line on a visual**

1. Access the Rulers sidebar for the visual. See [The Rulers Sidebar](#the-rulers-sidebar).
2. In the **Reference Lines** section of the sidebar, locate the reference line you want to delete.
3. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=02c9cbe530b9f34bd9a73851fdf499e2" alt="" width="16" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png" /> to the right of the reference line definition on the Rulers sidebar.
4. Select **Apply** to delete the reference line on the visual.
