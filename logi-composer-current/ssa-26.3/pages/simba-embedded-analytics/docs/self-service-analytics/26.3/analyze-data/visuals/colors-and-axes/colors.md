> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Change Color Schemes

Color schemes provide ways to identify and highlight metrics and attributes on a visual using color. Color schemes are specified for visuals in different ways, based on the visual type.

* The colors on [standard bar charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard), [heat maps](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#heat-maps), [KPI charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc#kpi-charts), [US region maps](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/map-chart-styles#us-region-maps), [world country maps](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/map-chart-styles#world-maps), [packed bubble charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#packed-bubble-charts), [tree maps](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#tree-maps), and [word cloud charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#word-clouds) are based on the color metric selected for the visual. Colors can be changed using the Color sidebar.
* The color of [multiple metric bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-multiple-metric-charts) and [multiple-metric line](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#line-trend-multiple-metric-charts) charts are based on the y-axis metric you have selected. Colors can be changed using the Color sidebar.
* Visual colors are not available for [map marker charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/map-chart-styles#marker-maps), [pivot tables](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pivot-tables), and [tables of raw data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt).
* For all other visuals ([box plots](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#box-plots), [donut charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#donut-charts), [floating bubble charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#floating-bubble-charts), [line-trend attribute charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#line-trend-attribute-value-charts), [pie charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie), and [scatter plot charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot)), the visual colors are based on an x-axis Group field you have selected. Colors can be changed using the Color sidebar.

Color palettes for your Self-Service Analytics environment are defined using themes. In addition, the default color palette used for visuals and for specific visual types is defined using themes. See [Manage User Interface Themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).

**Access the Color sidebar for a visual**

1. Select the visual in the Visual Gallery or on a dashboard.

2. Select **Settings** on the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) to access the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual. Then select the color button on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).

   The **Color** sidebar for the selected visual opens.

3. Make changes as needed. For details about the color options, refer to the description of the specific [visual type](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/application-framework/getting-started-with-the-application-framework#self-service-analytics-visual-metrics-and-attributes-reference) used to display the information from your sources as a visual.

4. If you want to use the palette specified by the theme defined for the environment, select the **Inherit from theme** checkbox. The colors specified in the theme activated for the Self-Service Analytics environment and for this visual type is used and overrides other palette settings you might have specified on the Color sidebar. For more information about themes, see [Manage User Interface Themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).

The ability to control colors on a visual is provided using the interactivity sidebar. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

<h2 id="change-the-visual-color-metric">
  Change the Visual Color Metric
</h2>

You can change the metric used to determine the colors used on a visual while you are viewing it.

**Change the color metric while you are viewing a visual**

1. Select the color metric directly on your visual. A Color dialog appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-metric.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=dcd08619fb2293d53ed15eb594372067" alt="" width="286" height="303" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-metric.png" />

2. Select a new metric to be used to determine the colors on your visual.

3. Select the aggregation function that should be used with the color metric: SUM, AVG, MAX, MIN, or (for some data sources) LAST VALUE. See [Metric Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#metric-aggregation-functions).

   The visual renders using colors determined by the select metric and its aggregated values.

<h2 id="change-the-axes">
  Change the Axes
</h2>

Many visual types show data on a standard coordinate grid, with axes labels identifying the values depicted horizontally and vertically on the visual. Examples include [bar charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/available-visual-types#bar-chart-styles), [line charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/available-visual-types#line-charts), and [scatter charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/available-visual-types#scatter-bubble-charts).

Use the axes labels on these visuals to change the metric (y-axis) and attribute (x-axis) fields graphed in the visual. The number of labels displayed on a visual depend on the [number of metrics and attributes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/application-framework/getting-started-with-the-application-framework#self-service-analytics-visual-metrics-and-attributes-reference) on which the visual is based.

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/axes-labels-23-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=e1d6154c5c27d0a775e6484a0cb9b4a1" alt="select an axis label to change the field used in this visual" width="1239" height="769" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/axes-labels-23-1.png" />

You can specify the default labels for visuals on the [Fields tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) of your data source configurations. Controls for these options are provided using the interactivity sidebar. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

See the following topics:

* [Change a Group Attribute](#change-a-group-attribute)
* [Change a Metric Field](#change-a-metric-field)

You can also change the metric used to determine the colors on the visual. See [Change the Visual Color Metric](#change-the-visual-color-metric).

<h3 id="change-a-group-attribute">
  Change a Group Attribute
</h3>

You can change the x-axis field, or group attribute, on a visual that plots data on a coordinated grid.

**Change the visual group (x-axis) attribute**

1. Select the group attribute (x-axis) label on your visual. A Group dialog appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/group-dialog-23-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=68af80d3079fe35afe6f1951e069b396" alt="select a group attribute for the visual" width="348" height="638" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/group-dialog-23-1.png" />

2. Select a new field to be viewed on the x-axis of your visual.

   The visual renders the newly selected attribute.

<h3 id="change-a-metric-field">
  Change a Metric Field
</h3>

You can change the y-axis field, or metric, on a visual that plots data on a coordinated grid.

**Change the visual metric (y-axis field)**

1. Select the metric (y-axis) label on your visual. A Metric dialog appears.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/metric-dialog-23-1.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=ab9e2db8febc11708f2ae0d7bee0ab67" alt="Select a metric for this visual" width="347" height="597" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/metric-dialog-23-1.png" />

2. Select a new metric to use as the y-axis of your visual and a metric function to use to aggregate the data on the visual. See [Metric Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#metric-aggregation-functions).

   The visual is updated and renders the newly selected metric. If you need to perform more complex analysis of your data set, you can [add custom metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics).

<h2 id="supplied-color-palettes">
  Supplied Color Palettes
</h2>

Self-Service Analytics comes with a number of color palettes. You can add a color palette to your environment using themes. See [Manage User Interface Themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).

The following table lists the supplied color palettes that are available for use in visuals. If a palette name has `-accessible` appended to its name, it is colorblind friendly.

| Palette Name | Hex Color Values |
| - | - |
| Accent | \['#7fc97f', '#beaed4', '#fdc086', '#ffff99', '#386cb0', '#f0027f', '#bf5b17', '#666666'] |
| Blues-accessible | \['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#08519c', '#08306b'] |
| BrBG-accessible | \['#543005', '#8c510a', '#bf812d', '#dfc27d', '#f6e8c3', '#f5f5f5', '#c7eae5', '#80cdc1', '#35978f', '#01665e', '#003c30'] |
| BuGn-accessible | \['#f7fcfd', '#e5f5f9', '#ccece6', '#99d8c9', '#66c2a4', '#41ae76', '#238b45', '#006d2c', '#00441b'] |
| BuPu-accessible | \['#f7fcfd', '#e0ecf4', '#bfd3e6', '#9ebcda', '#8c96c6', '#8c6bb1', '#88419d', '#810f7c', '#4d004b'] |
| Dark2-accessible | \['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d', '#666666'] |
| GnBu-accessible | \['#f7fcf0', '#e0f3db', '#ccebc5', '#a8ddb5', '#7bccc4', '#4eb3d3', '#2b8cbe', '#0868ac', '#084081'] |
| Greens-accessible | \['#f7fcf5', '#e5f5e0', '#c7e9c0', '#a1d99b', '#74c476', '#41ab5d', '#238b45', '#006d2c', '#00441b'] |
| Greys-accessible | \['#ffffff', '#f0f0f0', '#d9d9d9', '#bdbdbd', '#969696', '#737373', '#525252', '#252525', '#000000'] |
| Oranges-accessible | \['#fff5eb', '#fee6ce', '#fdd0a2', '#fdae6b', '#fd8d3c', '#f16913', '#d94801', '#a63603', '#7f2704'] |
| OrRd-accessible | \['#fff7ec', '#fee8c8', '#fdd49e', '#fdbb84', '#fc8d59', '#ef6548', '#d7301f', '#b30000', '#7f0000'] |
| Paired-accessible | \['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#ffff99', '#b15928'] |
| Pastel1 | \['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#ffffcc', '#e5d8bd', '#fddaec', '#f2f2f2'] |
| Pastel2 | \['#b3e2cd', '#fdcdac', '#cbd5e8', '#f4cae4', '#e6f5c9', '#fff2ae', '#f1e2cc', '#cccccc' ] |
| PiYG-accessible | \['#8e0152', '#c51b7d', '#de77ae', '#f1b6da', '#fde0ef', '#f7f7f7', '#e6f5d0', '#b8e186', '#7fbc41', '#4d9221', '#276419'] |
| PRGn-accessible | \['#40004b', '#762a83', '#9970ab', '#c2a5cf', '#e7d4e8', '#f7f7f7', '#d9f0d3', '#a6dba0', '#5aae61', '#1b7837', '#00441b'] |
| PuBu-accessible | \['#fff7fb', '#ece7f2', '#d0d1e6', '#a6bddb', '#74a9cf', '#3690c0', '#0570b0', '#045a8d', '#023858'] |
| PuBuGn-accessible | \['#fff7fb', '#ece2f0', '#d0d1e6', '#a6bddb', '#67a9cf', '#3690c0', '#02818a', '#016c59', '#014636'] |
| PuOr-accessible | \['#7f3b08', '#b35806', '#e08214', '#fdb863', '#fee0b6', '#f7f7f7', '#d8daeb', '#b2abd2', '#8073ac', '#542788', '#2d004b'] |
| PuRd-accessible | \['#f7f4f9', '#e7e1ef', '#d4b9da', '#c994c7', '#df65b0', '#e7298a', '#ce1256', '#980043', '#67001f'] |
| Purples-accessible | \['#fcfbfd', '#efedf5', '#dadaeb', '#bcbddc', '#9e9ac8', '#807dba', '#6a51a3', '#54278f', '#3f007d'] |
| RdBu-accessible | \['#67001f', '#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#f7f7f7', '#d1e5f0', '#92c5de', '#4393c3', '#2166ac', '#053061'] |
| RdGy | \['#67001f', '#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#ffffff', '#e0e0e0', '#bababa', '#878787', '#4d4d4d', '#1a1a1a'] |
| RdOrYI-accessible | \['#eea8b6', '#de536f', '#bd2525', '#772b28', '#e44838', '#ee5502', '#ffbf1f', '#ffdc85'] |
| RdPu-accessible | \['#fff7f3', '#fde0dd', '#fcc5c0', '#fa9fb5', '#f768a1', '#dd3497', '#ae017e', '#7a0177', '#49006a'] |
| RdYlBu-accessible | \['#a50026', '#d73027', '#f46d43', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4', '#313695'] |
| RdYlGn | \['#a50026', '#d73027', '#f46d43', '#fdae61', '#fee08b', '#ffffbf', '#d9ef8b', '#a6d96a', '#66bd63', '#1a9850', '#006837'] |
| Reds-accessible | \['#fff5f0', '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a', '#ef3b2c', '#cb181d', '#a50f15', '#67000d'] |
| Set2-accessible | \['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3'] |
| Set1 | \['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999'] |
| Set3 | \['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd', '#ccebc5', '#ffed6f'] |
| Spectral | \['#9e0142', '#d53e4f', '#f46d43', '#fdae61', '#fee08b', '#ffffbf', '#e6f598', '#abdda4', '#66c2a5', '#3288bd', '#5e4fa2'] |
| YlGn-accessible | \['#ffffe5', '#f7fcb9', '#d9f0a3', '#addd8e', '#78c679', '#41ab5d', '#238443', '#006837', '#004529'] |
| YlGnBu-accessible | \['#ffffd9', '#edf8b1', '#c7e9b4', '#7fcdbb', '#41b6c4', '#1d91c0', '#225ea8', '#253494', '#081d58'] |
| YlOrBr-accessible | \['#ffffe5', '#fff7bc', '#fee391', '#fec44f', '#fe9929', '#ec7014', '#cc4c02', '#993404', '#662506'] |
| YlOrRd-accessible | \['#ffffcc', '#ffeda0', '#fed976', '#feb24c', '#fd8d3c', '#fc4e2a', '#e31a1c', '#bd0026', '#800026'] |
| DefaultQualitative | \['#0095b7', '#a0b774', '#f4c658', '#fe8b3e', '#cf2f23', '#756c56', '#007896', '#47a694'] |
| DefaultSequential-accessible | \['#ffdc9c', '#ffc65f', '#efc15e', '#9eb778', '#7eb184', '#43a79b', '#008db6', '#097bb1'] |

## Specify Colors

You can specify colors using:

* The color name (for example "cornflowerblue" or "red"). For valid color names, see [https://www.w3schools.com/cssref/css\_colors.asp](https://www.w3schools.com/cssref/css_colors.asp).
* RGB color encoding (for example, `rgb(255,0,0)`). For RGB color values, see [https://www.rapidtables.com/web/color/RGB\_Color.html](https://www.rapidtables.com/web/color/RGB_Color.html).
* Hexadecimal color encoding (for example, `#0096b6`). For hexadecimal color values, see [https://www.rapidtables.com/web/color/RGB\_Color.html](https://www.rapidtables.com/web/color/RGB_Color.html).
