---
title: "Chart Advanced Features: Radar"
id: 5281559125783
section: "Charts and Visualizations"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281559125783-Chart-Advanced-Features-Radar
updated_at: 2022-05-03T22:08:24Z
---

# Chart Advanced Features: Radar

# Chart Advanced Features: Radar

The following sections provide a list of available advanced attributes available for controlling and customizing **Radar** elements.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic contains documentation for advanced attributes which are third-party customizations that must be manually entered into the chart wizard. These topics were converted directly from the documentation provided by this third-party source. Not every attribute listed may be supported in Exago BI as some unexpected conflicts may occur in their integration within the application.

## Functional Attributes

These attributes let you control a variety of functional elements on the chart. For example, you can opt to show or hide data labels, data values. You can also set chart limits and extended properties.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| animation | True/False | 0/1 | This attribute lets you set the configuration whether the chart should appear in an animated fashion. If you do not want to animate any part of the chart, set this as 0. |
| animationDuration | Number | In seconds | This attribute sets the animation duration of the chart. `animationDuration` attribute is applicable only if animation of the chart is enabled. Default value: 1 sec |
| palette | Number | 1-5 | Each chart has 5 pre-defined color palettes which you can choose from. Each palette renders the chart in a different color theme. |
| paletteColors | Text | List of hex color codes separated by comma | While the `palette` attribute allows to select a palette theme that applies to chart background, canvas, font and tool-tips, it does not change the colors of data items (that is, column, line, pie etc.). Using `paletteColors` attribute, you can specify your custom list of hex colors for the data items. The list of colors have to be separated by comma. For example, `”paletteColors”: “#FF0000, #0372AB, #FF5904…”`. The chart will cycle through the list of specified colors and then render the data plot accordingly. To use the same set of colors throughout all your charts in a web application, you can store the list of palette colors in your application globally and then provide the same in each chart JSON. |
| showLabels | True/False | 0/1 | It sets the configuration whether the x-axis labels will be displayed or not. |
| showValues | True/False | 0/1 | Sets the configuration whether data values would be displayed along with the data plot on chart. |
| showLimits | True/False | 0/1 | Whether to show chart limit values. If not specified `showYAxisValues` overrides this attribute. |
| showDivLineValues | True/False | 0/1 | Whether to show div line values. If not specified `showYAxisValues` overrides this attribute. |
| labelStep | Number | 1 or above | By default, all the labels are displayed on the chart. However, if you’ve a set of streaming data (like name of months or days of week), you can opt to show every n-th label for better clarity. This attribute just lets you do so. When a value greater than 1 (n) is set to this attribute, the first label from left and every label at the n-th position from left will be displayed. for example, a chart showing data for 12 months and set with `labelStep: 3` will show labels for January, April, July, and October. The rest of the labels will be skipped. |
| adjustDiv | True/False | 0/1 | The chart automatically tries to adjust divisional lines and limit values based on the data provided. However, if you want to set your explicit lower and upper limit values and number of divisional lines, first set this attribute to false. That would disable automatic adjustment of divisional lines. |
| showPrintMenuItem | True/False | 0/1 | When you right click on the chart it shows a context menu. This attribute allows you to show or hide the “Print” option in the context menu. |
| unescapeLinks | True/False | 0/1 | Internally the chart decodes a Url that you set as link. Before invoking the link it again encodes the Url. If you are passing multilingual characters via a Url or do not want this decode-encode mechanism to be handled by chart you can set,`unescapeLinks=’0’`. |
| showZeroPlaneValue | True/False | 0/1 | Allows you to show or hide the value of the zero plane. |
| clickURL | Text | Any | The entire chart can now act as a hotspot. Use this URL to define the hotspot link for the chart. The link can be specified in Exago BI Link Format. |
| clickURLOverridesPlotLinks | True/False | 0/1 | Sets whether the `clickURL` attribute (that sets a link to which the user is directed when the chart is clicked) overrides the `link` attribute (that sets a link to which the user is directed when a data plot is clicked). Default value: 0 (`clickURL` does not override `link`) |
| radarRadius | Number | In Pixels | If you want to explicitly specify a radius for the radar chart, use this attribute. Otherwise, the chart will automatically calculate the best-fit radius. |
| setAdaptiveYMin | True/False | 0/1 | This attribute lets you set whether the y-axis lower limit would be 0 (in case of all positive values on chart) or should the y-axis lower limit adapt itself to a different figure based on values provided to the chart. |
| hasRTLText | Number | Any | This attribute, when set to `1`, indicates to the chart that the text (rendered on the chart) may contain RTL characters and the textual display has to be managed accordingly. |
| plotHighlightEffect | Text | Any | This attribute lets you enable/disable the highlight effect, in the form of a `fadeout`, for the data plots corresponding to a legend item. When this attribute is enabled and the mouse pointer is hovered over a legend item label, plots belonging to the other data series fadeout, by reducing their opacity. The fadeout effect can be customized by specifying the fadeout color and opacity using the `color` and `alpha` attributes. for example . `fadeout|color=#ff0000, alpha=60` |
| theme | Text | ‘fusion’, ‘gammel’, ‘candy’, ‘ocean’, ‘zune’, ‘carbon’, ‘umber’ | This attribute changes the theme of the chart. There are 7 types of themes which have been made according to the different color combinations. |

## Chart Message-related Attributes

These attributes let you set and configure custom chart messages, using text as well as images.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| baseChartMessageFont | Text | Any | This attribute allows to set a custom font for all chart messages. |
| baseChartMessageFontSize | Number | In pixels | This attribute allows to set a custom font size for all chart messages. |
| baseChartMessageColor | Color | Hex Color Code | This attribute allows to set a custom font color for all chart messages. |
| baseChartMessageImageHAlign | Text | left, middle, right | This attribute allows to set a custom horizontal alignment for all images displayed as chart messages. Default value: middle |
| baseChartMessageImageVAlign | Text | top, middle, bottom | This attribute allows to set a custom vertical alignment for all images displayed as chart messages. Default value: middle |
| baseChartMessageImageAlpha | Number | 0 – 100 | This attribute allows to set a transparency for all images displayed as chart messages. Default value: 100 |
| baseChartMessageImageScale | Number | 0-300 | This attribute allows to set a scale for magnifying all images displayed as chart messages. Default value: 100 |
| loadMessage | Text | Any | This attribute allows to set the message to be displayed when a chart begins to load. To display an image as the chart message, prefix `I-` to the image URL. |
| loadMessageFont | Text | Font Name | This attribute allows to set the font for the message displayed when a chart begins to load. |
| loadMessageFontSize | Number | In pixels | This attribute allows to set the font size for the message displayed when a chart begins to load. |
| loadMessageColor | Color | Hex Color Code | This attribute allows to set the font color for the message displayed when a chart begins to load. |
| loadMessageImageHAlign | Text | left, middle, right | If an image is displayed as the chart `loadMessage`, this attribute allows to set a custom horizontal alignment for the image. Default value: value assigned to the `baseChartMessageImageHAlign` attribute |
| loadMessageImageVAlign | Text | top, middle, bottom | If an image is displayed as the chart `loadMessage`, this attribute allows to set a custom vertical alignment for the image. Default value: value assigned to the `baseChartMessageImageVAlign` attribute |
| loadMessageImageAlpha | Number | 0 – 100 | If an image is displayed as the chart `loadMessage`, this attribute allows to set the transparency of the image. Default value: 100 |
| loadMessageImageScale | Number | 0-300 | If an image is displayed as the chart `loadMessage`, this attribute allows to set the scale for magnifying the image. Default value: 100 |
| typeNotSupportedMessage | Text | Any | This attribute allows to set the message to be displayed when the specified chart type is not supported. To display an image as the chart message, prefix `I-` to the image URL. |
| typeNotSupportedMessageFont | Text | Font Name | This attribute allows to set the font for the message displayed when the specified chart type is not supported. |
| typeNotSupportedMessageFontSize | Number | In pixels | This attribute allows to set the font size for the message displayed when the specified chart type is not supported. |
| typeNotSupportedMessageColor | Color | Hex Color Code | This attribute allows to set the font color for the message displayed when the specified chart type is not supported. |
| typeNotSupportedMessageImageHAlign | Text | left, middle, right | If an image is displayed as the chart `typeNotSupportedMessage`, this attribute allows to set a custom horizontal alignment for the image. Default value: value assigned to the `baseChartMessageImageHAlign` attribute |
| typeNotSupportedMessageImageVAlign | Text | top, middle, bottom | If an image is displayed as the chart `typeNotSupportedMessage`, this attribute allows to set a custom vertical alignment for the image. Default value: value assigned to the `baseChartMessageImageVAlign` attribute |
| typeNotSupportedMessageImageAlpha | Number | 0 – 100 | If an image is displayed as the chart `typeNotSupportedMessage`, this attribute allows to set the transparency of the image. Default value: 100 |
| typeNotSupportedMessageImageScale | Number | 0-300 | If an image is displayed as the chart `typeNotSupportedMessage`, this attribute allows to set the scale for magnifying the image. Default value: 100 |
| renderErrorMessage | Text | Any | This attribute allows to set the message to be displayed if an error is encountered while rendering the chart. To display an image as the chart message, prefix `I-` to the image URL. |
| renderErrorMessageFont | Text | Font Name | This attribute allows to set a font for the message displayed if an error is encountered while rendering the chart. |
| renderErrorMessageFontSize | Number | In pixels | This attribute allows to set the font size for the message displayed if an error is encountered while rendering the chart. |
| renderErrorMessageColor | Color | Hex Color Code | This attribute allows to set the font color for the message displayed if an error is encountered while rendering the chart. |
| renderErrorMessageImageHAlign | Text | left, middle, right | If an image is displayed as the chart `renderErrorMessage`, this attribute allows to set a custom horizontal alignment for the image. Default value: value assigned to the `baseChartMessageImageHAlign` attribute |
| renderErrorMessageImageVAlign | Text | top, middle, bottom | If an image is displayed as the chart `renderErrorMessage`, this attribute allows to set a custom vertical alignment for the image. Default value: value assigned to the `baseChartMessageImageVAlign` attribute |
| renderErrorMessageImageAlpha | Number | 0 – 100 | If an image is displayed as the chart `renderErrorMessage`, this attribute allows to set the transparency of the image. Default value: 100 |
| renderErrorMessageImageScale | Number | 0-300 | If an image is displayed as the chart `renderErrorMessage`, this attribute allows to set the scale for magnifying the image. Default value: 100 |
| dataLoadStartMessage | Text | Any | This attribute allows to set the message to be displayed when chart data begins loading. To display an image as the chart message, prefix `I-` to the image URL. |
| dataLoadStartMessageFont | Text | Font Name | This attribute allows to set a font for the message displayed when chart data begins loading. |
| dataLoadStartMessageFontSize | Text | In pixels | This attribute allows to set the font size for the message displayed when chart data begins loading. |
| dataLoadStartMessageColor | Color | Hex Color Code | This attribute allows to set the font color for the message displayed when chart data begins loading. |
| dataLoadStartMessageImageHAlign | Text | left, middle, right | If an image is displayed as the chart `dataLoadStartMessage`, this attribute allows to set a custom horizontal alignment for the image. Default value: value assigned to the `baseChartMessageImageHAlign` attribute |
| dataLoadStartMessageImageVAlign | Text | top, middle, bottom | If an image is displayed as the chart `dataLoadStartMessage`, this attribute allows to set a custom vertical alignment for the image. Default value: value assigned to the `baseChartMessageImageVAlign` attribute |
| dataLoadStartMessageImageAlpha | Number | 0 – 100 | If an image is displayed as the chart `dataLoadStartMessage`, this attribute allows to set the transparency of the image. Default value: 100 |
| dataLoadStartMessageImageScale | Number | 0-300 | If an image is displayed as the chart `dataLoadStartMessage`, this attribute allows to set the scale for magnifying the image. Default value: 100 |
| dataEmptyMessage | Text | Any | This attribute allows to set the message to be displayed if the data loaded for a chart is empty. To display an image as the chart message, prefix `I-` to the image URL. |
| dataEmptyMessageFont | Text | Font Name | This attribute allows to set the font for the message displayed if the data loaded for a chart is empty |
| dataEmptyMessageFontSize | Number | In pixels | This attribute allows to set the font size for the message displayed if the data loaded for a chart is empty. |
| dataEmptyMessageColor | Color | Hex Color Code | This attribute allows to set the font color for the message displayed if the data loaded for a chart is empty. |
| dataEmptyMessageImageHAlign | Text | left, middle, right | If an image is displayed as the chart `dataEmptyMessage`, this attribute allows to set a custom horizontal alignment for the image. Default value: value assigned to the `baseChartMessageImageHAlign` attribute |
| dataEmptyMessageImageVAlign | Text | top, middle, bottom | If an image is displayed as the chart `dataEmptyMessage`, this attribute allows to set a custom vertical alignment for the image. Default value: value assigned to the `baseChartMessageImageVAlign` attribute |
| dataEmptyMessageImageAlpha | Number | 0 – 100 | If an image is displayed as the chart `dataEmptyMessage`, this attribute allows to set the transparency of the image. Default value: 100 |
| dataEmptyMessageImageScale | Number | 0-300 | If an image is displayed as the chart `dataEmptyMessage`, this attribute allows to set the scale for magnifying the image. Default value: 100 |
| dataLoadErrorMessage | Text | Any | This attribute allows to set the message to be displayed if an error is encountered while loading chart data. To display an image as the chart message, prefix `I-` to the image URL. |
| dataLoadErrorMessageFont | Text | Font Name | This attribute allows to set a font for the message displayed if an error is encountered while loading chart data. |
| dataLoadErrorMessageFontSize | Number | In pixels | This attribute allows to set the font size for the message displayed if an error is encountered while loading chart data. |
| dataLoadErrorMessageColor | Color | Hex Color Code | This attribute allows to set the font color for the message displayed if an error is encountered while loading chart data. |
| dataLoadErrorMessageImageHAlign | Text | left, middle, right | If an image is displayed as the chart `dataLoadErrorMessage`, this attribute allows to set a custom horizontal alignment for the image. Default value: value assigned to the `baseChartMessageImageHAlign` attribute |
| dataLoadErrorMessageImageVAlign | Text | top, middle, bottom | If an image is displayed as the chart `dataLoadErrorMessage`, this attribute allows to set a custom vertical alignment for the image. Default value: value assigned to the `baseChartMessageImageVAlign` attribute |
| dataLoadErrorMessageImageAlpha | Number | 0 – 100 | If an image is displayed as the chart `dataLoadErrorMessage`, this attribute allows to set the transparency of the image. Default value: 100 |
| dataLoadErrorMessageImageScale | Number | 0-300 | If an image is displayed as the chart `dataLoadErrorMessage`, this attribute allows to set the scale for magnifying the image. Default value: 100 |
| dataInvalidMessage | Text | Any | This attribute allows to set the message to be displayed if the data to be loaded for the chart is invalid. To display an image as the chart message, prefix `I-` to the image URL. |
| dataInvalidMessageFont | Text | Font Name | This attribute allows to set the font for the message displayed if the specified chart data is invalid. |
| dataInvalidMessageFontSize | Number | In pixels | This attribute allows to set the font size for the message displayed if the specified chart data is invalid. |
| dataInvalidMessageColor | Color | Hex Color Code | This attribute allows to set the font color for the message displayed if the specified chart data is invalid. |
| dataInvalidMessageImageHAlign | Text | left, middle, right | If an image is displayed as the chart `dataInvalidMessage`, this attribute allows to set a custom horizontal alignment for the image. Default value: value assigned to the `baseChartMessageImageHAlign` attribute |
| dataInvalidMessageImageVAlign | Text | top, middle, bottom | If an image is displayed as the chart `dataInvalidMessage`, this attribute allows to set a custom vertical alignment for the image. Default value: value assigned to the `baseChartMessageImageVAlign` attribute |
| dataInvalidMessageImageAlpha | Number | 0 – 100 | If an image is displayed as the chart `dataInvalidMessage`, this attribute allows to set the transparency of the image. Default value: 100 |
| dataInvalidMessageImageScale | Number | 0-300 | If an image is displayed as the chart `dataInvalidMessage`, this attribute allows to set the scale for magnifying the image. Default value: 100 |

## Chart Titles and Axis Names

Using these attributes, you can set the various headings and titles of chart like caption, sub-caption, x-axis and y-axis names etc.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| caption | Text | Any | Caption of the chart. |
| subCaption | Text | Any | Sub-caption of the chart. |

## Chart Axis Configuration Attributes

Using these attributes, you can set and configure x-axis labels, y-axis values and set chart cosmetics for the axis like color, alpha, etc.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showYAxisValues | True/False | 0/1 | The y-axis of the chart is divided into vertical sections using div (divisional) lines. Each div line assumes a value based on its position. Using this attribute you can set whether to show those div line (y-axis) values or not. The values of `showLimits` and `showDivLineValues`, if specified explicitly, overrides the value of this attribute. |
| yAxisValuesStep | Number | 1 or above | By default, all div lines show their values. However, you can opt to display every x(th) div line value using this attribute. |
| yAxisMinValue | Number | Numeric Value | This attribute helps you explicitly set the lower limit of the chart. If you do not specify this value, it is automatically calculated by the chart based on the data provided by you. |
| yAxisMaxValue | Number | Numeric Value | This attribute helps you explicitly set the upper limit of the chart. If you do not specify this value, it is automatically calculated by the chart based on the data provided by you. |
| forceYAxisValueDecimals | True/False | 0/1 | Whether to forcefully attach decimal places to all y-axis values. For example, If you limit the maximum number of decimal digits to 2, a number like 55.345 will be rounded to 55.34. This does not mean that all y-axis numbers will be displayed with a fixed number of decimal places. For instance 55 will not be displayed as 55.00 and 55.1 will not become 55.10. In order to have fixed number of decimal places attached to all y-axis numbers, set this attribute to 1. |
| yAxisValueDecimals | Number | 0-10 | Specifies the decimal precision of yAxis values when adjustDiv is set to 0. |

## Chart Caption Cosmetics

These attributes let you configure the cosmetics of chart caption and sub-caption.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| captionAlignment | Text | “left”, “center”, “right” | Sets horizontal alignment of caption |
| captionOnTop | True/False | 0/1 | Whether caption should be on top of the data plot area |
| captionFontSize | Number | 6 – 72 | Sets the caption font size in pixels |
| subCaptionFontSize | Number | 6 – 72 | Sets the sub-caption font size (in pixels) |
| captionFont | Text | Font Name | Sets the caption font family |
| subCaptionFont | Text | Font Name | Sets the sub-caption font family |
| captionFontColor | Color | Hex Color Code | Sets the caption font color |
| subCaptionFontColor | Color | Hex Color Code | Sets the sub-caption font color |
| captionFontBold | True/False | 0/1 | Whether the caption font should be displayed in bold |
| subCaptionFontBold | True/False | 0/1 | Whether the sub caption font should be displayed in bold |
| alignCaptionWithCanvas | True/False | 0/1 | Whether the caption is aligned with the canvas. Else, it will be aligned with the entire chart area |
| captionHorizontalPadding | Number | In Pixels | If caption is not center aligned, lets you configure the padding (in pixels) from either edge. Will be ignored if caption is center aligned. |

## Chart Cosmetics

The following attributes let you configure chart cosmetics like background color, background alpha, canvas color & alpha etc.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showBorder | True/False | 0/1 | Whether to show a border around the chart or not. |
| borderColor | Color | Hex Color Code | Border color of the chart. |
| borderThickness | Number | In Pixels | Border thickness of the chart. |
| borderAlpha | Number | 0 – 100 | Border alpha of the chart. |
| bgColor | Color | Hex Color Code | This attribute sets the background color for the chart. You can set any hex color code as the value of this attribute. To specify a gradient as background color, separate the hex color codes of each color in the gradient using comma. Example: `#FF5904, #FFFFFF`. |
| bgAlpha | Number | 0 – 100 | Sets the alpha (transparency) for the background. If you’ve opted for gradient background, you need to set a list of alpha(s) separated by comma. |
| bgRatio | Number | 0 – 100 | If you’ve opted for a gradient background, this attribute lets you set the ratio of each color constituent. |
| bgAngle | Number | 0-360 | Angle of the background color, in case of a gradient. |
| bgImage | Text | Any | To place any image (JPG/PNG/GIF) as background of the chart, enter the (path and) name of the background image as a URL without quotes around it. It should be in the same domain as the chart. |
| bgImageAlpha | Number | 0 – 100 | This attribute specifies the opacity for the loaded background image. |
| bgImageDisplayMode | Text | stretch, tile, fit, fill, center, none | Helps you specify the mode in which the background image is to be displayed. Stretch – expands the image to fit the entire chart area, without maintaining original image constraints. Tile – the image is repeated as a pattern on the entire chart area. Fit – fits the image proportionately on the chart area. Fill -proportionately fills the entire chart area with the image. Center – the image is positioned at the center of the chart area. None – Default mode. |
| bgImageValign | Text | left, center, right | Helps you to vertically align the background image. |
| bgImageHalign | Text | left, center, right | Helps you to horizontally align the background image. |
| bgImageScale | Number | 0-300 | Helps you magnify the background image.This attribute will only work when the attribute `bgImageDisplayMode` is set to none, center, or tile. |
| logoURL | Text | URL | You can load an external logo (JPEG/PNG) to your chart, this attribute lets you specify the URL. Due to cross domain security restrictions it is advised to use a logo from the same domain name as your charts. |
| logoLeftMargin | Number | In Pixels | This attribute helps you set the amount of empty space that you want to put on the left side of your logo image. Nothing is rendered in this space. |
| logoTopMargin | Number | In Pixels | This attribute helps you set the amount of empty space that you want to put on top of your logo image. Nothing is rendered in this space. |
| logoPosition | Text | TL, TR, BL, BR, CC | Where to position the logo on the chart: TL – Top-left TR – Top-right BR – Bottom right BL – Bottom left CC – Center of screen |
| logoAlpha | Number | 0 – 100 | Once the logo has loaded on the chart, you can configure its opacity using this attribute. |
| logoScale | Number | 0-300 | You can also change the scale of an externally loaded logo at run-time by specifying a value for this parameter. |
| logoLink | Text | URL | If you want to link the logo to an external URL, specify the link in this attribute. The link can be in Exago BI Link Format, allowing you to link to new windows, pop-ups, frames etc. |

## Data Plot Cosmetics

These attributes let you configure how your plot (columns, lines, area, pie or any data that you are plotting) would appear on the chart. If the plots can show borders, you can control the border properties using the attributes listed below. Or, if they support gradient fills, you can again configure various properties of the gradient using these attributes. Various other controls over plot cosmetics can be attained using this set of attributes.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showPlotBorder | True/False | 0/1 | Whether the radar plot border would show up. |
| plotBorderColor | Color | Hex Color Code | Color for radar plot border |
| plotBorderThickness | Number | 0-5 | Thickness for radar plot border |
| plotBorderAlpha | Number | 0 – 100 | Alpha for radar plot border |
| plotFillAlpha | Number | 0 – 100 | Lets you set the fill alpha for radar plot. |
| plotFillColor | Color | Hex Color Code | Fill Color for the radar plot(hex code) |
| showRadarBorder | True/False | 0/1 | Whether a border should be rendered around the radar chart. |
| radarBorderColor | Color | Hex Color Code | Border color of radar outline. |
| radarBorderThickness | Number | In Pixels | Border thickness of radar outline. |
| radarBorderAlpha | Number | 0 – 100 | Border alpha of radar outline. |
| radarFillColor | Color | Hex Color Code | Fill color for the radar. |
| radarFillAlpha | Number | 0 – 100 | Fill alpha for the radar. |
| radarSpikeColor | Color | Hex Color Code | Color for radar spikes. Radar spikes are the lines that emanate from the center to the vertex of radar. |
| radarSpikeThickness | Number | In Pixels | Thickness for radar spikes. Radar spikes are the lines that emanate from the center to the vertex of radar. |
| radarSpikeAlpha | Number | 0 – 100 | Alpha for radar spikes. Radar spikes are the lines that emanate from the center to the vertex of radar. |

## Data Value Cosmetics

These attributes let you configure font, background and border cosmetics, of value text-field that appear for each data plot.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| valueFont | Text | Font Name | Sets the font of the values in the chart |
| valueFontColor | Color | Hex Color Code | Specifies the value font color |
| valueFontSize | Number | 6 – 72 | Specifies the value font size |
| valueFontBold | True/False | 0/1 | Whether value font should be bold |
| valueFontItalic | True/False | 0/1 | Whether value font should be italicized |
| valueBgColor | Color | Hex Color Code | Sets the background color for value text |
| valueBorderColor | Color | Hex Color Code | Sets the border color around the value text |
| valueAlpha | Number | 0 – 100 | Sets the value alpha including font and background |
| valueFontAlpha | Number | 0 – 100 | Sets the value font alpha |
| valueBgAlpha | Number | 0 – 100 | Sets the value background alpha |
| valueBorderAlpha | Number | 0 – 100 | Sets the value border alpha |
| valueBorderThickness | Number | In Pixels | Sets the value border thickness |
| valueBorderPadding | Number | In Pixels | Sets the padding between the value and its surrounding border |
| valueBorderRadius | Number | In Pixels | Sets the value border radius |
| valueBorderDashed | True/False | 0/1 | Whether the border around the data values should be rendered using dashed lines. Default value: 0 (border rendered using straight lines) |
| valueBorderDashLen | Number | In pixels | Sets the length of each dash when the border around the data values is rendered using dashed lines. |
| valueBorderDashGap | Number | In pixels | Sets the gap between two consecutive dashes when the border around the data values is rendered using dashed lines. |
| textOutline | True/False | 0/1 | Set this attribute to `1` to draw a border on the data value text. Default value: 0 |

## Anchors

On radar charts, anchors (or marker points) are polygons which appear at the joint of two consecutive line or area points. These are indicators to show the position of data points. The anchors handle tool tips and links for the data points. So, if you opt to not render anchors on a chart, the tool tips and links won’t function. You can, however, hide them by setting alpha to 0 and still enable tool tips and links. You can customize all the facets of anchors using the properties below.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| drawAnchors | True/False | 0/1 | Whether to draw anchors on the chart. |
| anchorSides | Number | 3-20 | This attribute sets the number of sides the anchor will have. For example, an anchor with 3 sides would represent a triangle, with 4 it would be a square and so on. |
| anchorStartAngle | Number | 0 – 360 | This attribute sets the starting angle of anchors. Default value: 90 |
| anchorRadius | Number | In pixels | This attribute sets the radius (in pixels) of the anchor. |
| anchorBorderColor | Color | Hex Color Code | Lets you set the border color of anchors. |
| anchorBorderThickness | Number | In Pixels | Helps you set border thickness of anchors. |
| anchorBgColor | Color | Hex Color Code | Helps you set the background color of anchors. |
| anchorAlpha | Number | 0 – 100 | Helps you set the alpha of entire anchors. If you need to hide the anchors on chart but still enable tool tips, set this as 0. |
| anchorBgAlpha | Number | 0 – 100 | Helps you set the alpha of anchor background. |
| anchorImageUrl | Exago BI link format | URL | If you want to use an external image (JPG/PNG) as an anchor, this attribute lets you specify the URL. **Note:** Due to cross domain security restrictions it is advised to use an image from the same domain name as your charts. |
| anchorImageAlpha | Number | 0 – 100 | This attribute allows to set a transparency for images displayed as anchors in charts. Default value: 100 |
| anchorImageScale | Number | 0 – 100 | This attribute allows to set a scale for magnifying images displayed as anchors. Default value: 100 |
| anchorImagePadding | Number | In Pixels | This attribute sets the padding between the anchor image and the border of the anchor. For the anchor image, instead of decreasing the size of the image this attribute crops the image. Default value: 1 |

## Divisional Lines & Grids

Using this set of attributes, you can control the properties of divisional lines, zero plane and alternate color bands. Divisional Lines are horizontal or vertical lines running through the canvas. Each divisional line signifies a smaller unit of the entire axis thus aiding the users in interpreting the chart. The zero plane is a 2D plane that signifies the 0 position on the chart. If there are no negative numbers on the chart, you won’t see a visible zero plane. Alternate color bands are colored blocks between two successive divisional lines.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| numDivLines | Number | Numeric value > 0 | Number of horizontal axis division lines that you want on the chart. |
| divLineColor | Color | Hex Color Code | Color for divisional lines |
| divLineThickness | Number | 1-5 | Thickness of divisional lines |
| divLineAlpha | Number | 0 – 100 | Alpha of divisional lines. |

## Legend Properties

In radar charts, the series name of each data-set shows up in the legend of the chart. If you do not need the legend, you can opt to hide the same. Also, the legend can be placed at the bottom of the chart or to the right of the chart. Using the attributes below, you can configure the functional and cosmetic properties of the legend.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showLegend | True/False | 0/1 | Whether to show legend for the chart. |
| legendItemFontBold | True/False | 0/1 | Whether legend keys should be displayed in bold |
| legendItemFont | Text | Font Name | Sets legend item font |
| legendItemFontSize | Number | 6 – 72 | Sets legend item font size |
| legendItemFontColor | Color | Hex Color Code | Sets legend item font color |
| legendItemHoverFontColor | Color | Hex Color Code | Sets legend item font color on hover |
| legendPosition | Text | bottom, right, top, top-left, top-right, bottom-left, bottom-right, left, left-top, left-bottom, right, right-top, right-bottom, and absolute | The legend can be plotted at different positions with respect to the chart. Note that if the value of `legendPosition` is set to `absolute`, you also need to set the coordinates of the legend. You can do that using the attributes `legendXPosition` and `legendYPosition`, both of which accept absolute or percentage values. |
| legendXPosition | Number | 0 to chart width (in pixels) | When the value of `legendPosition` is set to `absolute`, use this attribute to set the X-coordinate of the legend. It accepts absolute or percentage values. By default, its value is set to `0`. |
| legendYPosition | Number | 0 to chart height (in pixels) | When the value of `legendPosition` is set to `absolute`, use this attribute to set the Y-coordinate of the legend. It accepts absolute or percentage values. By default, its value is set to `0`. |
| legendNumRows | Number | Any | Sets the number of rows the legend should display. |
| legendNumColumns | Number | Any | Sets the number of columns the legend should display. |
| legendCaptionAlignment | Text | “left”, “center”, “right” | Sets the legend caption horizontal alignment . |
| legendCaptionFontBold | True/False | 0/1 | Whether legend caption should be displayed in bold |
| legendCaptionFont | Text | Font Name | Sets legend caption font |
| legendCaptionFontSize | Number | 6 – 72 | Sets legend caption font size |
| legendCaptionFontColor | Color | Hex Color Code | Sets legend caption font color |
| legendCaption | Text |  | You can add a caption for the entire legend by setting the same here. |
| legendItemHiddenColor | Color | Hex Color Code | Sets the color that applies on both text font and icon when they are in a disabled / hidden state |
| legendIconScale | Number | 1-5 | Scaling of legend icon is possible starting Exago BI. This attribute lets you control the size of legend icon. |
| legendBgColor | Color | Hex Color Code | Background color for the legend. |
| legendBgAlpha | Number | 0 – 100 | Background alpha for the legend. |
| legendBorderColor | Color | Hex Color Code | Border Color for the legend. |
| legendBorderThickness | Number | In Pixels | Border thickness for the legend. |
| legendBorderAlpha | Number | 0 – 100 | Border alpha for the legend. |
| legendShadow | True/False | 0/1 | Whether to show a shadow for legend. |
| legendAllowDrag | True/False | 0/1 | The legend can be made drag-able by setting this attribute to 1. End viewers of the chart can drag the legend around on the chart. |
| legendScrollBgColor | Color | Hex Color Code | If you have too many items on the legend, a scroll bar shows up on the same. This attribute lets you configure the background color of the scroll bar. |
| reverseLegend | True/False | 0/1 | You can reverse the ordering of data sets in the legend by setting this attribute to 1. |
| interactiveLegend | True/False | 0/1 | This attribute lets you interact with the legend in your chart. When you click a legend key, the dataplots associated with that series are eliminated from the chart. Re-clicking the key causes the dataplots to reappear. |
| legendNumColumns | Number | Positive Integer | If your chart contains multiple series, the legend is displayed as a grid comprising of multiple legend keys. With the help of this attribute you can specify the number of columns that are to be displayed in the legend. |
| minimiseWrappingInLegend | True/False | 0/1 | Whether to minimize legend item text wrapping. |
| drawCustomLegendIcon | True/False | 0/1 | Specifies whether drawing a custom legend icon will be enabled. All legend icon customization attributes will work only if this feature is enabled. Default value: 0 (disabled) |
| legendIconBorderColor | Color | Hex Color Code | Sets the border color for the legend icon. Default value: Data plot border color |
| legendIconBgColor | Color | Hex Color Code | Sets the background color for the legend icon. Default value: Data plot fill color |
| legendIconAlpha | Number | 0 – 100 | Sets the legend icon transparency. Default value: 100 |
| legendIconBgAlpha | Number | 0 – 100 | Sets the legend icon background transparency. Default value: 100 |
| legendIconSides | Number | Any | Sets the number of sides for the legend icon. Default value: 4 |
| legendIconBorderThickness | Number | 1-5 | Sets the thickness of the legend icon border. Default value: 1 |
| legendIconStartAngle | Number | Any | Sets the starting angle of for drawing the legend icon. Default value: 45 |
| alignLegendWithCanvas | True/False | 0/1 | This attribute if set to `0`, the legend box will be center aligned with respect to the entire width of the chart only if the total width of the legend box is more than the canvas width. By default, the legend box is center aligned with respect to the canvas width and it remains the same if the width of the legend box is less than the canvas width. |

## Number Formatting

Exago BI offers you a lot of options to format your numbers on the chart. Using the attributes below, you can control a myriad of options like: Formatting of commas and decimals Number prefixes and suffixes Decimal places to which the numbers would round to Scaling of numbers based on a user defined scale Custom number input formats

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| formatNumber | True/False | 0/1 | This configuration determines whether the numbers displayed on the chart will be formatted using commas, for example, 40,000 if ‘formatNumber’: ‘1’; and 40000 if ‘formatNumber’: ‘0’;. |
| formatNumberScale | True/False | 0/1 | Configuration whether to add K (thousands) and M (millions) to a number after truncating and rounding it – for example, if `formatNumberScale` is set to 1, 1043 would become 1.04K (with decimals set to 2 places). Same with numbers in millions – an M will be added at the end. |
| defaultNumberScale | Text | Any | The default unit of the numbers that you’re providing to the chart. |
| numberScaleUnit | Text | Any | Unit of each block of the scale. |
| numberScaleValue | Text | Any | Range of the various blocks that constitute the scale. |
| forceNumberScale | True/False | 0/1 | If a data value is less than the lowest given number is the number scale, this attribute forces the lower value of the `numberScaleUnit` to be applied to that data value. This attribute works only when `“formatNumberScale”: “1”` and the `defaultNumberScale` attribute is not defined. For example, if `“numberScaleUnit”: “K, M”`, `“numberScaleValue”: “1000, 1000”`, and `“forceNumberScale”: “1”`, a data value of `400` will be rendered as `0.40K`. |
| scaleRecursively | True/False | 0/1 | Whether recursive scaling should be applied. |
| maxScaleRecursion | Number | Any | How many recursions to complete during recursive scaling? -1 completes the entire set of recursion. |
| scaleSeparator | Text | Any | What character to use to separate the scales that are generated after recursion? |
| numberPrefix | Text | Character | Using this attribute, you could add prefix to all the numbers visible on the graph. For example, to represent all dollars figure on the chart, you could specify this attribute to $ to show like $40000, $50000. |
| numberSuffix | Text | Character | Using this attribute, you could add suffix to all the numbers visible on the graph. For example, to represent all figures quantified as per annum on the chart, you could specify this attribute to ‘/a’ to show like 40000/a, 50000/a. |
| decimalSeparator | Text | Character | This attribute helps you specify the character to be used as the decimal separator in a number. |
| thousandSeparator | Text | Character | This attribute helps you specify the character to be used as the thousands separator in a number. |
| thousandSeparatorPosition | Number |  | This option helps you specify the position of the thousand separator. |
| inDecimalSeparator | Text | Character | In some countries, commas are used as decimal separators and dots as thousand separators. In XML, if you specify such values, it will give an error while converting to number. So, the chart accepts the input decimal and thousand separator from user, so that it can convert it accordingly into the required format. This attribute lets you input the decimal separator. |
| inThousandSeparator | Text | Character | In some countries, commas are used as decimal separators and dots as thousand separators. In XML, if you specify such values, it will give an error while converting to number. So, the chart accepts the input decimal and thousand separator from user, so that it can convert it accordingly into the required format. This attribute lets you input the thousand separator. |
| decimals | Number | 0-10 | Number of decimal places to which all numbers on the chart would be rounded to. |
| forceDecimals | True/False | 0/1 | Whether to add 0 padding at the end of decimal numbers. For example, if you set decimals as 2 and a number is 23.4. If `forceDecimals` is set to 1, the number will automatically be converted to 23.40 (note the extra 0 at the end). |

## Font Properties

Using the attributes below, you can define the generic font properties for all the text on the chart. These attributes allow you a high level control over font properties. If you intend to specify font properties for individual chart elements (like Caption, sub-caption etc.), you need to use the Styles feature of Exago BI. Using Styles, you can also specify advanced font properties like Bold, Italics, HTML Mode etc.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| baseFont | Text | Font Name | This attribute lets you set the font face (family) of all the text (data labels, values etc.) on chart. If you specify the `outCnvBaseFont` attribute also, then this attribute controls only the font face of text within the chart canvas bounds. |
| baseFontSize | Number | 6 – 72 | This attribute sets the base font size of the chart, that is, all the values and the names in the chart which lie on the canvas will be displayed using the font size provided here. |
| baseFontColor | Color | Hex Color Code | This attribute sets the base font color of the chart, that is, all the values and the names in the chart which lie on the canvas will be displayed using the font color provided here. |
| outCnvBaseFont | Text | Font Name | This attribute sets the base font family of the chart text which lies outside the canvas, that is, all the values and the names in the chart which lie outside the canvas will be displayed using the font name provided here. |
| outCnvBaseFontSize | Number | 6 – 72 | This attribute sets the base font size of the chart, that is, all the values and the names in the chart which lie outside the canvas will be displayed using the font size provided here. |
| outCnvBaseFontColor | Color | Hex Color Code | This attribute sets the base font color of the chart, that is, all the values and the names in the chart which lie outside the canvas will be displayed using the font color provided here. |

## Data Label Cosmetics

These attributes let you configure the cosmetics of all data labels of the chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| labelFont | Text | Font Name | Sets the x-axis label font family for the text. |
| labelFontColor | Color | Hex Color Code | Sets the x-axis label font color. |
| labelFontSize | Number | 6 – 72 | Specifies the x-axis label font size. |
| labelFontBold | True/False | 0/1 | Flag indicating whether x-axis label font should be bold or not. |
| labelFontItalic | True/False | 0/1 | Flag indicating whether x-axis label font should be italicized or not. |
| labelBgColor | Color | Hex Color Code | Sets the background color for x-axis label text. |
| labelBorderColor | Color | Hex Color Code | Sets the color of the border around the x-axis label text. |
| labelAlpha | Number | 0 – 100 | Sets the x-axis label alpha for both font and background. |
| labelBgAlpha | Number | 0 – 100 | Sets the x-axis label background alpha. |
| labelBorderAlpha | Number | 0 – 100 | Sets the x-axis label border alpha. |
| labelBorderPadding | Number | In Pixels | Sets the x-axis label border padding. |
| labelBorderRadius | Number | In Pixels | Sets the x-axis label border radius. |
| labelBorderThickness | Number | In Pixels | Sets the x-axis label border thickness. |
| labelBorderDashed | True/False | 0/1 | Whether the border around x-axis labels should be rendered using dashed lines. Default value: 0 (border rendered using straight lines) |
| labelBorderDashLen | Number | In pixels | Sets the length of each dash when the border around the x-axis labels are rendered using dashed lines. |
| labelBorderDashGap | Number | In pixels | Sets the gap between two consecutive dashes when the border around x-axis labels are rendered using dashed lines. |
| labelLink | URL | Any | Sets a link for every data plot labels. |

## Tool tip Attributes

These attributes let you control the tool tip. You can set the background color, border color, separator character and few other details.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showToolTip | True/False | 0/1 | Whether to show tool tip on chart. |
| toolTipBgColor | Color | Hex Color Code | Background color for tool tip. |
| toolTipColor | Color | Hex Color Code | Font color for the tool-tip. |
| toolTipBorderColor | Color | Hex Color Code | Border color for tool tip. |
| tooltipBorderAlpha | Number | 0 – 100 | Sets the border transparency for tool tip. |
| toolTipSepChar | Text | Any | The character specified as the value of this attribute separates the name and value displayed in tool tip. |
| seriesNameInToolTip | True/False | 0/1 | For Multi-series charts, Exago BI shows the following information in tool tip (unless tool text is explicitly defined): “Series Name, Category Name, Data Value”. This attribute lets you control whether series name would show up in tool tip or not. |
| showToolTipShadow | True/False | 0/1 | Whether to show shadow for tool tips on the chart. |
| plottooltext | Text | Any | Specify custom text for the tooltip You can either specify a constant string as the tooltip text or you can use variable values from the data level by prefixing a `$` to the attribute name, for example, `$name`, `$value`. |

## Toolbar Attributes

Using this set of attributes, you can customize the toolbar on the chart. The advantage of having a toolbar is that it manages all the UI action elements (context menus, checkboxes, buttons) centrally. This provides a clean, uniform look and a better, more meaningful and logical grouping.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| toolbarPosition | Text | TL, TR, BL, BR, CC | Where to position the toolbar on the chart: TL – Top-left TR – Top-right BR – Bottom right BL – Bottom left CC – Center of screen |
| toolbarX | Number | Any | Sets the toolbox position on the chart with respect to x-axis. |
| toolbarY | Number | Any | Sets the toolbox position on the chart with respect to y-axis. |
| toolbarHAlign | Text | Left, Right | Sets the horizontal alignment of the toolbar on the chart. |
| toolbarVAlign | Text | Top, Bottom | Sets the vertical alignment of the toolbar on the chart |
| toolbarButtonColor | Color | Any (color code without the # prefix) | Sets the color of the toolbar buttons. |
| showToolBarButtonTooltext | True/False | 0/1 | Enables/disables display of tooltips for toolbar buttons. |
| toolbarButtonScale | Number | Any | You can change the scale of the toolbar by specifying a value for this attribute. |

## Attributes for Exporting Charts

These attributes allow you to control the saving of chart as image, SVG or XLSX.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| exportEnabled | True/False | 0/1 | Whether the chart will allow exporting to images, PDFs, SVG, XLSX or CSV format. Default value: 0 |
| exportAction | Text | ‘save’ or ‘download’ | In case of server-side exporting, the action specifies whether the exported image will be sent back to client as download, or whether it’ll be saved on the server. Default value: download |
| exportHandler | Text | Any | In case of server side exporting, this refers to the path of the server-side export handler (the ready-to-use scripts that we provide). |
| exportFormats | Text | Any | Lets you configure what output formats to allow for export of chart, in the export context menu, and also customize the label for each menu item. The attribute value should be a pipe (|) delimited separated key-value pair. Example: `exportFormats: ‘PNG=Export as High Quality Image|JPG|PDF=Export as PDF File’` |
| exportMode | Text | Any | This attributes sets the modes of export. To enable client-side exporting, set this attribute to `client`. Default value: auto.  **Note:** Starting v3.12.1, the `exportMode` attribute replaces the `exportAtClientSide` attribute. However, you don’t need to make any changes to the existing setup because, the Exago BI library comes with the proper mapping already provided. |
| exportShowMenuItem | True/False | 0/1 | Whether the menu items related to export (for example, Save as JPEG etc.) will appear in the context menu of chart. |
| exportTargetWindow | Text | ‘\_self’ or ‘\_blank’ | In case of server-side exporting and when using download as action, this lefts you configure whether the return image, PDF, SVG or XLSX will open in same window (as an attachment for download), or whether it will open in a new window. Default value: \_self |
| exportFileName | Text | Any | Using this attribute you can specify the name (excluding the extension) of the output (export) file. |

## Data Plot Hover Effects

If you wish to show an effect on the data plot (column, line anchor, pie etc.) when the user hovers his mouse over the data plot, these attributes let you configure the cosmetics of the hover for all data plots in the chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showHoverEffect | True/False | 0/1 | Whether to enable hover effect on charts for all elements |
| anchorHoverEffect | True/False | 0/1 | Sets whether to enable the hover effect on charts for anchors. |
| anchorHoverAlpha | Number | 0 – 100 | This attribute specifies the transparency for the anchors when hovered. |
| anchorHoverSides | Number | In Pixels | This attribute sets the number of sides of the anchor when hovered. |
| anchorHoverRadius | Number | In pixels | This attribute sets the radius of the anchor when hovered. |
| anchorBgHoverColor | Color | Hex color code | This attribute sets the background color of anchor when hovered. |
| anchorBgHoverAlpha | Number | 0 – 100 | This attribute sets the transparency of anchor’s background when hovered. |
| anchorBorderHoverColor | Color | Hex color code | Sets the border color of anchors when hovered. |
| anchorBorderHoverAlpha | Number | 0 – 100 | Sets the border’s transparency of anchors when hovered. |
| anchorBorderHoverThickness | Number | In pixels | This attribute sets the border thickness of the anchors when hovered. |
| anchorHoverStartAngle | Number | In pixels | This attribute sets the starting angle of the anchors when hovered. |
| anchorHoverDip | Number | 0 – 1 | This attribute adds a dip effect (different shapes) to the anchors on hover. When hovered a star shaped anchor is created. Using `anchorSides` attribute, you can specify the no. of sides for anchors. `Note : If the anchors are of circular shape, this attribute won’t be applied on it.` |
| anchorHoverAnimation | True/False | 0/1 | Anchors get animated when the normal radius and the hover radius are different. To disable this effect you can set anchorHoverAnimation = `0`. Default value: `1` |

## Chart Padding & Margins

The following attributes help you control chart margins and padding. Exago BI allows you manually customize the padding of various elements on the chart to allow advanced manipulation and control over chart visualization. Padding in Exago BI is always defined in pixels, unless the attribute itself suggests some other scale (like `plotSpacePercent`, which configures the spacing using percentage values). You can also define the chart margins. Chart Margins refer to the empty space left on the top, bottom, left and right of the chart. That means, Exago BI would not plot anything in that space. It is not necessary for you to specify any padding/margin values. Exago BI automatically assumes the best values for the same, if you do not specify the same.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| captionPadding | Number | In Pixels | This attribute lets you control the space (in pixels) between the sub-caption and top of the chart canvas. If the sub-caption is not defined, it controls the space between caption and top of chart canvas. If neither caption, nor sub-caption is defined, this padding does not come into play. |
| labelPadding | Number | In Pixels | This attribute sets the vertical space between the labels and canvas bottom edge. If you want more space between the canvas and the x-axis labels, you can use this attribute to control it. |
| chartLeftMargin | Number | In Pixels | Amount of empty space that you want to put on the left side of your chart. Nothing is rendered in this space. |
| chartRightMargin | Number | In Pixels | Amount of empty space that you want to put on the right side of your chart. Nothing is rendered in this space. |
| chartTopMargin | Number | In Pixels | Amount of empty space that you want to put on the top of your chart. Nothing is rendered in this space. |
| chartBottomMargin | Number | In Pixels | Amount of empty space that you want to put at the bottom of your chart. Nothing is rendered in this space. |
| legendPadding | Number | In Pixels | Padding of legend from right or bottom side of canvas |

## The categories Object

The `categories` object and the `category` object (child of the `categories` object) are used to specify x-axis labels for multi-series charts. The attributes of the `categories` object are used to set the font properties of all x-axis labels collectively.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| font | Text | Valid font face | Lets you specify font face for the x-axis data labels. |
| fontColor | Color | Hex Color Code | Lets you specify font color for the x-axis data labels. |
| fontSize | Number | Any | Lets you specify font size for the x-axis data labels. |

## The category Object

The attributes of the `category` object are used to define and customize individual x-axis labels for multi-series charts.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| label | Text | Any | This attribute determines the label for the data item. The label appears on the x-axis of chart. **Note:** The `label` attribute replaces the `name` attribute. Previously, either one of the attributes could be used to set the label. Support for the `name` attribute has been discontinued since v3.10.0. |
| showLabel | True/False | 0/1 | You can individually opt to show or hide labels of individual data items using this attribute. |
| toolText | Text | Any | The tooltip defined in the `category` object appears only when the mouse cursor is hovered over the data plots. However, this will not appear when the cursor is moved over the data labels (except for a situation when long labels are automatically truncated with ellipses. In this situation, if the mouse cursor is hovered over a truncated label, the tooltip will appear with the full label). In case you want to set a short label and show the full label in tooltip, define the full label using this attribute within the `category` object. The tooltip with the full label will appear only when the mouse is hovered on the dataplot. |
| font | Text | Any | Sets the x-axis label font family for the text. |
| fontColor | Color | Hex Color Code | Sets the x-axis label font color. |
| fontSize | Number | 6 – 72 | Specifies the x-axis label font size. |
| fontBold | True/False | 0/1 | Flag indicating whether x-axis label font should be bold or not. |
| fontItalic | True/False | 0/1 | Flag indicating whether x-axis label font should be italicized or not. |
| bgColor | Color | Hex Color Code | Sets the background color for x-axis label text. |
| borderColor | Color | Hex Color Code | Sets the color of the border around the x-axis label text. |
| alpha | Number | 0 – 100 | Sets the x-axis label alpha for both font and background. |
| bgAlpha | Number | 0 – 100 | Sets the x-axis label background alpha. |
| borderAlpha | Number | 0 – 100 | Sets the x-axis label border alpha. |
| borderPadding | Number | In Pixels | Sets the x-axis label border padding. |
| borderRadius | Number | In Pixels | Sets the x-axis label border radius. |
| borderThickness | Number | In Pixels | Sets the x-axis label border thickness. |
| borderDashed | True/False | 0/1 | Whether the border around x-axis label should be rendered using dashed lines. Default value: 0 (border rendered using straight lines) |
| borderDashLen | Number | In pixels | Sets the length of each dash when the border around the x-axis label is rendered using dashed lines. |
| borderDashGap | Number | In pixels | Sets the gap between two consecutive dashes when the border around x-axis label is rendered using dashed lines. |

## The data set Object

Each `dataset` object contains a series of data. For example, for a monthly sales comparison chart for two successive years, the first data-set would contain the data for first year and the next one for the second year. You can provide data-set level cosmetics so that all data within that data-set will be plotted in the same color/alpha/etc. Depending on the chart type, there are a number of attributes that you can define for each `dataset` object.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| seriesName | Text | Any | Lets you specify the series name for a particular data-set. For example, if you are plotting a chart to indicate monthly sales analysis for 2005 and 2006, the `seriesName` for the first data set would be 2005 and that of the second would be 2006. The `seriesName` of a data-set is shown in legend. |
| color | Color | Hex Color Code | This attribute sets the color using which columns, lines, area of that data-set would be drawn. For column chart, you can specify a list of comma separated hex codes to get a gradient plot |
| alpha | Text | 0 – 100 or Comma Separated List | This attribute sets the alpha (transparency) of the entire data-set. |
| showValues | True/False | 0/1 | Whether to show the values for this data-set. |
| valueFontColor | Color | Hex Color Code | Specifies the font color of data values for a particular data set. |
| valueBgColor | Color | Hex Color Code | Sets the background color of value text for a particular data set. |
| valueBorderColor | Color | Hex Color Code | Sets the border color around the value text for a particular data set. |
| includeInLegend | True/False | 0/1 | Whether to include the `seriesName` of this data-set in legend. This can be particularly useful when you are using combination charts and you have used the area or line chart to plot a trend, and you do not want the seriesName of that trend to appear in legend. |
| showPlotBorder | True/False | 0/1 | Whether to show the border of this data-set. |
| plotBorderColor | Color | Hex Color Code | Color for data plot border of this data-set. |
| plotBorderThickness | Number | 0-5 | Thickness for data plot border of this data-set. |
| plotBorderAlpha | Number | 0 – 100 | Alpha for data plot border of this data-set. |
| drawAnchors | True/False | 0/1 | Whether to draw anchors for a particular data set. |
| anchorSides | Number | 3-20 | Sets the number of sides that the anchors of the particular data-set will have. For example, an anchor with 3 sides would represent a triangle, with 4 it would be a square and so on. |
| anchorStartAngle | Number | 0 – 360 | This attribute sets the starting angle for anchors of particular data set. Default value: 90 |
| anchorRadius | Number | In Pixels | This attribute sets the radius (in pixels) of the anchors of the particular data-set. |
| anchorBorderColor | Color | Hex Color Code | Lets you set the border color of anchors of the particular data-set. |
| anchorBorderThickness | Number | In Pixels | Helps you set border thickness of anchors of the particular data-set. |
| anchorBgColor | Color | Hex Color Code | Helps you set the background color of anchors of the particular data-set. |
| anchorAlpha | Number | 0 – 100 | Helps you set the alpha of entire anchors of the particular data-set. If you need to hide the anchors for the data-set but still enable tool tips, set this as 0. |
| anchorBgAlpha | Number | 0 – 100 | Helps you set the alpha of anchor background of the particular data-set. |
| anchorHoverColor | Color | Hex Color Code | This attribute can set the hover color for anchors of a particular data set. |
| anchorHoverAlpha | Number | 0 – 100 | This attribute sets the transparency for anchors of a particular data set when hovered. |
| anchorHoverSides | Number | In Pixels | This attribute sets the number of sides for anchors of a particular data set when hovered. |
| anchorBgHoverColor | Color | Hex color code | This attribute sets the background color for anchors of a particular data set when hovered. |
| anchorBgHoverAlpha | Number | 0 – 100 | This attribute sets the transparency for anchor’s background of a particular data set when hovered. |
| anchorBorderHoverColor | Color | Hex color code | Sets the border color for anchors of a particular data set when hovered. |
| anchorBorderHoverAlpha | Number | 0 – 100 | Sets the border’s transparency for anchors of a particular data set when hovered. |
| anchorBorderHoverThickness | Number | In pixels | This attribute sets the border thickness for anchors of a particular data set when hovered. |
| anchorHoverStartAngle | Number | In pixels | This attribute sets the starting angle for anchors of a particular data set when hovered. |
| anchorHoverDip | Number | 0 – 1 | This attribute adds a dip effect (different shapes) for anchors of a particular data set on hover. When hovered a star shaped anchor is created. Using `anchorSides` attribute, you can specify the no. of sides for anchors. `Note : If the anchors are of circular shape, this attribute won’t be applied on it.` |

## The data Object

Attributes of the `data` object, child of the `dataset` object, are used to define the values to be plotted for individual data series. The `dataset` and `data` objects are defined for one data series as shown in the example below:

```
"data set": [{
	"seriesname": "Previous Year",
	"data": [{
			"value": "10000",
		},
		{
			"value": "11500",
		},
		{
			"value": "12500",
		},
		{
			"value": "15000"
		}]
}]
```

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| value | Number | Any | Numerical value for the data item. This value would be plotted on the chart. |
| color | Color | Hex Color Code | For Multi-series charts, you can define the color of data-sets at data set level. However, if you wish to highlight a particular data element, you can specify its color at “set” level using this attribute. |
| displayValue | Text |  | If instead of the numerical value of this data, you wish to display a custom string value, you can specify the same here. Examples are annotation for a data item etc. |
| link | Text | Any | You can define links for individual data items. That enables the end user to click on data items (columns, lines, bars etc.) and drill down to other pages. To define the link for data items, use the link attribute. You can define links that open in same window, new window, pop-up window or frames. Please see Advanced Charting > Drill Down Charts for more information. Also, you’ll need to URL Encode all the special characters (like ? and &) present in the link. |
| toolText | Text | Any | By default, Exago BI shows the series name, category name, and value as tool tip text for that data item. But, if you want to display more information for the data item as tool tip, you can use this attribute to specify the same. |
| showValue | True/False | 0/1 | You can individually opt to show or hide values of individual data items using this attribute. This value over-rides the data-set level value. |
| valueFontColor | Color | Hex Color Code | Specifies the font color of a data value for an individual data plot. |
| valueBgColor | Color | Hex Color Code | Sets the background color of a value text for an individual data plot. |
| valueBorderColor | Color | Hex Color Code | Sets the border color around the value text for an individual data plot. |
| alpha | Number | 0 – 100 | For Multi-series charts, you can define the alpha of data-sets at data set level. However, if you wish to highlight a particular data element, you can specify it’s alpha at “set” level using this attribute. |
| anchorSides | Number | 3-20 | Lets you specify “set” specific sides of the anchor. |
| anchorStartAngle | Number | 0 – 360 | This attribute sets the starting angle for an anchor of a particular data. Default value: 90 |
| anchorRadius | Number | In Pixels | Lets you specify “set” specific radius (in pixels) of the anchor. |
| anchorBorderColor | Color | Hex Color Code | Lets you specify “set” specific border color of the anchor. |
| anchorBorderThickness | Number | In Pixels | Lets you specify “set” specific border thickness of the anchor. |
| anchorBgColor | Color | Hex Color Code | Lets you specify “set” specific background color of the anchor. |
| anchorAlpha | Number | 0 – 100 | Lets you specify “set” specific alpha of the anchor. |
| anchorBgAlpha | Number | 0 – 100 | Lets you specify “set” specific alpha of the anchor background. |
| anchorHoverColor | Color | Hex Color Code | This attribute can set the hover color for a particular anchor. |
| anchorHoverAlpha | Number | 0 – 100 | This attribute sets the transparency for an anchor when hovered. |
| anchorHoverSides | Number | In Pixels | This attribute sets the number of sides for a particular anchor when hovered. |
| anchorBgHoverColor | Color | Hex color code | This attribute sets the background color of a particular anchor when hovered. |
| anchorBgHoverAlpha | Number | 0 – 100 | This attribute sets the transparency for a particular anchor’s background when hovered. |
| anchorBorderHoverColor | Color | Hex color code | Sets the border color of an anchor when hovered. |
| anchorBorderHoverAlpha | Number | 0 – 100 | Sets the border’s transparency of an anchor when hovered. |
| anchorBorderHoverThickness | Number | In pixels | This attribute sets the border thickness of an anchor when hovered. |
| anchorHoverStartAngle | Number | In pixels | This attribute sets the starting angle of an anchor when hovered. |
| anchorHoverDip | Number | 0 – 1 | This attribute adds a dip effect (different shapes) to a particular anchor on hover. When hovered a star shaped anchor is created. Using `anchorSides` attribute, you can specify the no. of sides for anchors. `Note : If the anchors are of circular shape, this attribute won’t be applied on it.` |
