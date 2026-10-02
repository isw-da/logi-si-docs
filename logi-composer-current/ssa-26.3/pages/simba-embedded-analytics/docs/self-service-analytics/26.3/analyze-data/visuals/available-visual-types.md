> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Available Visual Types

You can use the Available Visual Types work area to make specific visual types available or unavailable for a data source.

<Note>
  If you have the **Administer Initial Visuals** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), you can update available visual types as needed.
</Note>

**Define visual types for a source**

1. Make sure you are logged in as a user with the **Administer Initial Visuals** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select the **Source** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. On the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page, locate a data source configuration to edit, and select the more menu (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) button.

4. Select **Available Visual Types**. The Available Visual Types work area for this source opens.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/sources-page-visual-types-710.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=cfca781afb673d3107ff56a5d897c86c" alt="" width="1242" height="219" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/sources-page-visual-types-710.png" />

5. Select to enable and disable the visuals you want user to be able to use for this source. All Visual Types are shown by default: select Standard Visual Types or Custom Visual Types to edit those lists only, or use the search field to find a specific visual.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/available-visual-types-710.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=3ecfa3c68e725fe9fd0060cfa9e5b603" alt="" width="499" height="629" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/available-visual-types-710.png" />

   If a visual type exists for this source that you later disable, existing visuals remain, but new visuals of that type can not be made. For example, disable Bar visual types for a source to prevent users from creating Bar visual types from that source. Existing Bar visuals from that source remain unchanged.

6. After completing your changes, close the work area to save your changes for this source. All available data fields are automatically included in these default visual settings.

Access and update settings common for all visual types on the [Global Settings Work Areas](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab). Global default settings allow you to set time bar and search box settings that apply to all visual types for the data source. See [Configure Time Bar Defaults](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#configure-time-bar-defaults), [Configure Search Box Defaults](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#configure-search-box-defaults), and [Enable Data Sharpening and Configure Its Defaults](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-sharpening-ov#enable-data-sharpening-and-configure-its-defaults).

For information on the specific settings available for a standard visual type, select it below.

* [Single Metric Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc)
* [Bar Chart Styles](#bar-chart-styles) (includes [standard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard), [histogram](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-histograms), and [multiple metric](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-multiple-metric-charts) charts)
* [Box Plots](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#box-plots)
* [Bullet Gauges](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc#bullet-gauges)
* [Combo Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#combo-charts)
* [Donut Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#donut-charts)
* [Floating Bubble Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#floating-bubble-charts)
* [Heat Maps](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#heat-maps)
* [KPI Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc#kpi-charts)
* [Line Charts](#line-charts) (includes [line & bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#edit-line-bar-trend-charts), [attribute value](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#line-trend-attribute-value-charts), and [multiple metric](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#line-trend-multiple-metric-charts) charts)
* [Map Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/map-chart-styles) (includes [marker](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/map-chart-styles#marker-maps), [US region](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/map-chart-styles#us-region-maps), and [world](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/map-chart-styles#world-maps) maps)
* [Circular, Tree, and Cloud Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie)
* [Pivot Tables](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pivot-tables)
* [Scatter (Bubble) Charts](#scatter-bubble-charts) (includes [floating bubble](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#floating-bubble-charts), [packed bubble](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#packed-bubble-charts), and [scatter plot](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot) charts)
* [Sunburst](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#sunburst)
* [Tables](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt)
* [Tree Maps](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#tree-maps)
* [Waterfall](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#waterfall)
* [Word Clouds](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#word-clouds)

<h2 id="re-visualize-change-a-visual-type">
  Re-Visualize (Change a Visual Type)
</h2>

After creating a visual, you can change to a different visual type and re-visualize the data in a different format, with emphasis on more or different data. Based on the data source you are using, certain visual types may not be available.

**Change a visual's type**

1. Select the visual in the dashboard or in the Visual Gallery.

2. Select the re-visualize (was *visual style*) icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chttype.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=559a7028c6be23336aa84a37bdb73f20" alt="" width="26" height="25" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '26px', height: '25px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chttype.png" />) on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual. The [Re-Visualize sidebar](#use-the-re-visualize-sidebar) opens.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/re-viz-menu-26-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=85c02e542db846b5c3db381497d06635" alt="use this work area to select a different visual type to display your data" width="381" height="729" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/re-viz-menu-26-2.png" />

3. In the Re-Visualize sidebar, select the visual style you want to use. Use the search bar at the top of the sidebar to quickly locate a style in the list. Type any letter in the search bar and sidebar is filtered to show only visual style names that include that letter.

<h2 id="use-the-re-visualize-sidebar">
  Use the Re-Visualize Sidebar
</h2>

The Re-Visualize sidebar (formerly *Visual Style* sidebar) lets you quickly change the type of visual displayed in a dashboard visual or when you are editing a visual in the Visual Gallery. Controls for changing the type of a visual are provided using the interactivity sidebar. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

<Note>
  When you re-visualize a visual, its [published and subscribed links](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/pubsub-ov) are removed. See [Control How Cross-Visual Filters Interact in a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/pubsub-ov).
</Note>

<Note>
  A list filter visual cannot be converted to a different type. Likewise, other visual types cannot be converted to the list filter visual type.
</Note>

**Access the Re-Visualize sidebar for a visual**

1. Select the visual in the Visual Gallery or on a dashboard.

2. If you selected the visual on a dashboard, select **Settings** on the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) to access the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual.

3. Select the re-visualize option (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chttype.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=559a7028c6be23336aa84a37bdb73f20" alt="" width="26" height="25" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '26px', height: '25px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chttype.png" />) on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual. The Re-Visualize sidebar opens.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/re-viz-menu-26-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=85c02e542db846b5c3db381497d06635" alt="use this work area to select a different visual type to display your data" width="381" height="729" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/re-viz-menu-26-2.png" />

4. Select a visual option from the list.

<h2 id="bar-chart-styles">
  Bar Chart Styles
</h2>

Supported bar chart styles include standard bar charts, histograms, and multiple metric bar charts. You can configure the defaults for all bar chart styles for a data source configuration.

For more information, select one of the following links:

* [Bar, Line, and Combo Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard)
* [Bars: Histograms](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-histograms)
* [Bars: Multiple Metric Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-multiple-metric-charts)
* [Modify Bar Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#modify-bar-charts)

<h2 id="line-charts">
  Line Charts
</h2>

Line charts include line-bar charts, attribute trend charts, and multiple metric trend charts. These visual types are supported by almost all data sources. To configure line charts, see:

* [Edit Line & Bar Trend Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#edit-line-bar-trend-charts)
* [Line Trend: Attribute Value Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#line-trend-attribute-value-charts)
* [Line Trend: Multiple Metric Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#line-trend-multiple-metric-charts)

<h2 id="scatter-bubble-charts">
  Scatter (Bubble) Charts
</h2>

Scatter charts include floating bubbles, packed bubbles, and scatter plot styles. For more information, select one of the following scatter chart styles:

* [Floating Bubble Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#floating-bubble-charts)
* [Packed Bubble Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#packed-bubble-charts)
* [Comparison and Relationship Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot)
