---
title: "Chart Advanced Features: Zoom Line"
id: 5281567885335
section: "Charts and Visualizations"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281567885335-Chart-Advanced-Features-Zoom-Line
updated_at: 2022-05-03T22:08:20Z
---

# Chart Advanced Features: Zoom Line

# Chart Advanced Features: Zoom Line

The following sections provide a list of available advanced attributes available for controlling and customizing **Zoom Line** chart elements.

## Functional Attributes

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic contains documentation for advanced attributes which are third-party customizations that must be manually entered into the chart wizard. These topics were converted directly from the documentation provided by this third-party source. Not every attribute listed may be supported in Exago BI as some unexpected conflicts may occur in their integration within the application.

These attributes let you control a variety of functional elements on the chart. For example, you can opt to show/hide data labels, data values. You can also set chart limits and extended properties.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| palette | Number | 1-5 | Exago BI uses the concept of Color Palettes. Each chart has 5 pre-defined color palettes which you can choose from. Each palette renders the chart in a different color theme. |
| paletteColors | Text | List of hex color codes separated by comma | While the `palette` attribute allows to select a palette theme that applies to chart background, canvas, font and tool-tips, it does not change the colors of data items (that is, column, line, pie etc.). Using `paletteColors` attribute, you can specify your custom list of hex colors for the data items. The list of colors have to be separated by comma for example, `”paletteColors”: “#FF0000, #0372AB, #FF5904…”`. The chart will cycle through the list of specified colors and then render the data plot accordingly. To use the same set of colors throughout all your charts in a web application, you can store the list of palette colors in your application globally and then provide the same in each chart JSON. |
| connectNullData | True/False | 0/1 | This attribute lets you control whether empty data sets in your data will be connected to each other OR do they appear as broken data sets. |
| showTerminalValidData | True/False | 0/1 | In Zoomline charts, to display the data at the initial level, data are compressed. Initial level fails to display the first and last data from the data set provided. This attribute if set to `1`, displays the first and last valid data even if the value arises between the broken data set. |
| showLabels | True/False | 0/1 | It sets the configuration whether the x-axis labels will be displayed or not. |
| maxLabelHeight | Number | In Pixels | This attribute can be used to set the maximum height for the x-axis labels (data labels) excluding the x-axis title. If any label goes beyond this height, the label will be truncated. In stagger mode, the number of stagger lines will be reduced if they exceed this value. |
| pixelsperlabel | Number | In Pixels | Sets the distance between the labels of the x-axis. |
| useEllipsesWhenOverflow | True/False | 0/1 | When enabled in auto mode, long data labels are truncated by adding ellipses to prevent them from overflowing the chart background. The default value is 1. |
| rotateLabels | True/False | 0/1 | This attribute lets you set whether the data labels will show up as rotated labels on the chart. |
| showShadow | True/False | 0/1 | Whether to apply the shadow effects for data plot. |
| setAdaptiveYMin | True/False | 0/1 | This attribute lets you set whether the y-axis lower limit will be 0 (in case of all positive values on chart) or should the y-axis lower limit adapt itself to a different figure based on values provided to the chart. |
| compactDataMode | True/False | 0/1 | Indicates whether the XML is in compact form or not. |
| dataSeparator | Character | Any character | Specifies the separation character used in compact XML. |
| allowPinMode | True/False | 0/1 | Used for enabling/disabling the pin mode feature, which is active by default. |
| numVisibleLabels | Number | Any number | Specifies the number of data labels that are to be visible in one screen. As this attribute imposes the equispace constraint, values greater than 5 and less than 10 (if total data plots `=` 10) will not be applicable due to violation of this constraint. |
| displayStartIndex | Number | Any number > 1 | Indicates the index of the data label that will appear to the extreme left of the chart. |
| displayEndIndex | Number | Any Number > 1 | Indicates the index of the data label that is to appear at the extreme right of the chart. Using `displayStartIndex` and `displayEndIndex` attributes you can set the range of data labels that will be visible when the chart first renders. |
| pixelsPerPoint | Number | Any number | Specifies the number of pixels to be used for producing a data point. A greater number will result in high quality display. |
| hasRTLText | Number | Any | This attribute, when set to `1`, indicates to the chart that the text (rendered on the chart) may contain RTL characters and the textual display has to be managed accordingly. |
| plotHighlightEffect | Text | Any | This attribute lets you enable/disable the highlight effect, in the form of a `fadeout`, for the data plots corresponding to a legend item. When this attribute is enabled and the mouse pointer is hovered over a legend item label, plots belonging to the other data series fadeout, by reducing their opacity. The fadeout effect can be customized by specifying the fadeout color and opacity using the `color` and `alpha` attributes. for example . `fadeout|color=#ff0000, alpha=60` |
| showPrintMenuItem | True/False | 0/1 | Whether to show “Print Chart” item in the context menu of the chart? Even if you opt to hide the item in context menu, you can still opt to invoke `print()` JavaScript method of the chart to print the same. |
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
| xAxisName | Text | Any | X-axis title of the chart. |
| yAxisName | Text | Any | Y-axis title of the chart. |

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

## Chart Axis Configuration Attributes

Using these attributes, you can set and configure x-axis labels, y-axis values and set chart cosmetics for the axis like color, alpha, etc.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showXAxisLine | True/False | 0/1 | This attribute if set to \_0\_, hides the x-axis of the chart. Default value: 1 |
| xAxisPosition | Text | Top, Bottom | This attribute sets the position of the x-axis in the chart. Default value: Bottom |
| yAxisPosition | Text | Left, Right | This attribute sets the position of the y-axis in the chart. Default value: Left |
| xAxisLineColor | Color | Hex Color Code | Sets color of the x-axis of the chart. |
| xaxislinethickness | Number | In Pixels | Sets the thickness of the x-axis line of the chart. |
| showYAxisLine | True/False | 0/1 | This attribute if set to \_0\_, hides the y-axis of the chart. Default value: 1 |
| yAxisLineColor | Color | Hex Color Code | Sets color of the y-axis of the chart. |
| yAxisLineThickness | Number | In Pixels | Sets the thickness of the y-axis line of the chart. |
| showYAxisValues | True/False | 0/1 | Exago BI y-axis is divided into vertical sections using div (divisional) lines. Each div line assumes a value based on its position. Using this attribute you can set whether to show those div line (y-axis) values or not. This attribute shows or hides the y-axis divisional lines and limits. The values of `showLimits` and `showDivLineValues`, if specified explicitly, overrides the value of this attribute. |
| yAxisValuesStep | Number | 1 or above | By default, all div lines show their values. However, you can opt to display every x(th) div line value using this attribute. |
| rotateYAxisName | True/False | 0/1 | If you do not wish to rotate y-axis name, set this as 0. It specifically comes to use when you have special characters (UTF8) in your y-axis name that do not show up in rotated mode. |
| yAxisNameWidth | Number | (In Pixels) | If you opt to not rotate y-axis name, you can choose a maximum width that will be applied to y-axis name. |
| yAxisMinValue | Number | Numeric Value | This attribute helps you explicitly set the lower limit of the chart. If you don’t specify this value, it is automatically calculated by the chart based on the data provided by you. |
| yAxisMaxValue | Number | Numeric Value | This attribute helps you explicitly set the upper limit of the chart. If you don’t specify this value, it is automatically calculated by the chart based on the data provided by you. |
| forceYAxisValueDecimals | True/False | 0/1 | Whether to forcefully attach decimal places to all y-axis values. For example, If you limit the maximum number of decimal digits to 2, a number like 55.345 will be rounded to 55.34. This does not mean that all y-axis numbers will be displayed with a fixed number of decimal places. For instance 55 will not be displayed as 55.00 and 55.1 will not become 55.10. In order to have fixed number of decimal places attached to all y-axis numbers, set this attribute to 1. |
| yAxisValueDecimals | Number | 0-10 | If you’ve opted to not adjust div lines, you can specify the div line values decimal precision using this attribute. |

## x-Axis Name Cosmetics

To configure the font cosmetics of x-axis name (title), you can use the following attributes.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| xAxisNameFont | Text | Font Name | Sets the x-axis font family for the text |
| xAxisNameFontColor | Color | Hex Color Code | Sets the x-axis font color |
| xAxisNameFontSize | Number | 6 – 72 | Specifies the x-axis font size |
| xAxisNameFontBold | True/False | 0/1 | Whether x-axis font should be bold |
| xAxisNameFontItalic | True/False | 0/1 | Whether x-axis font should be italicized |
| xAxisNameBgColor | Color | Hex Color Code | Sets the background color for x-axis text |
| xAxisNameBorderColor | Color | Hex Color Code | Sets the border around the x-axis text |
| xAxisNameAlpha | Number | 0 – 100 | Sets the x-axis alpha including font and background |
| xAxisNameFontAlpha | Number | 0 – 100 | Sets the x-axis font alpha |
| xAxisNameBgAlpha | Number | 0 – 100 | Sets the x-axis background alpha |
| xAxisNameBorderAlpha | Number | 0 – 100 | Sets the x-axis border alpha |
| xAxisNameBorderPadding | Number | In Pixels | Sets the x-axis border padding |
| xAxisNameBorderRadius | Number | In Pixels | Sets the x-axis border radius |
| xAxisNameBorderThickness | Number | In Pixels | Sets the x-axis border thickness |
| xAxisNameBorderDashed | True/False | 0/1 | Whether the border around the x-axis name should be rendered using dashed lines. Default value: 0 (border rendered using straight lines) |
| xAxisNameBorderDashLen | Number | In pixels | Sets the length of each dash when the border around the x-axis name is rendered using dashed lines. |
| xAxisNameBorderDashGap | Number | In pixels | Sets the gap between consecutive dashes when the border around the x-axis name is rendered using dashed lines. |

## y-Axis Name Cosmetics

To configure the font cosmetics of y-axis name (title), you can use the following attributes.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| yAxisNameFont | Text | Font Name | Sets the y-axis (primary / secondary) font family for the text |
| yAxisNameFontColor | Color | Hex Color Code | Sets the y-axis (primary / secondary) font color |
| yAxisNameFontSize | Number | 6 – 72 | Specifies the y-axis (primary / secondary) font size |
| yAxisNameFontBold | True/False | 0/1 | Whether y-axis (primary / secondary) font should be bold |
| yAxisNameFontItalic | True/False | 0/1 | Whether y-axis (primary / secondary) font should be italicized |
| yAxisNameBgColor | Color | Hex Color Code | Sets the background color for y-axis (primary / secondary) text |
| yAxisNameBorderColor | Color | Hex Color Code | Sets the border around the y-axis (primary / secondary) text |
| yAxisNameAlpha | Number | 0 – 100 | Sets the y-axis (primary / secondary) alpha including font and background |
| yAxisNameFontAlpha | Number | 0 – 100 | Sets the y-axis (primary / secondary) font alpha |
| yAxisNameBgAlpha | Number | 0 – 100 | Sets the y-axis (primary / secondary) background alpha |
| yAxisNameBorderAlpha | Number | 0 – 100 | Sets the y-axis (primary / secondary) border alpha |
| yAxisNameBorderPadding | Number | In Pixels | Sets the y-axis (primary / secondary) border padding |
| yAxisNameBorderRadius | Number | In Pixels | Sets the y-axis (primary / secondary) border radius |
| yAxisNameBorderThickness | Number | In Pixels | Sets the y-axis (primary / secondary) border thickness |
| yAxisNameBorderDashed | True/False | 0/1 | Whether the border around the y-axis name should be rendered using dashed lines. Default value: 0 (border rendered using straight lines) |
| yAxisNameBorderDashLen | Number | In pixels | Sets the length of each dash when the border around the y-axis name is rendered using dashed lines. |
| yAxisNameBorderDashGap | Number | In pixels | Sets the gap between two consecutive dashes when the border around the y-axis name is rendered using dashed lines. |

## Y-Axis Value Cosmetics

These attributes let you configure font, background and border cosmetics, of the Y-axis value text.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| yAxisValueFont | Text | Font Name | Set the font family for the Y-axis value texts. Default value: verdana,sans |
| yAxisValueFontColor | Color | Hex Color Code | Sets the font color for the Y-axis value texts. Default value: #555555 |
| yAxisValueFontSize | Number | 6 – 72 | Sets the font size for the Y-axis value texts. Default value: 10 pixels |
| yAxisValueFontBold | True/False | 0/1 | Displays the Y-axis value texts in bold. Default value: 0 |
| yAxisValueFontItalic | True/False | 0/1 | Displays the Y-axis value texts in italic. Default value: 0 |
| yAxisValueBgColor | Color | Hex Color Code | Sets the background color for the Y-axis values. |
| yAxisValueBorderColor | Color | Hex Color Code | Sets the border color for the Y-axis values. |
| yAxisValueAlpha | Number | 0 – 100 | Sets the transparency for the Y-axis values between transparent (for `0`) and opaque (for `100`). Default value: 100 |
| yAxisValueBgAlpha | Number | 0 – 100 | Sets the transparency for the Y-axis value backgrounds between transparent (for `0`) and opaque (for `100`). |
| yAxisValueBorderAlpha | Number | 0 – 100 | Sets the transparency for the Y-axis values between transparent (for `0`) and opaque (for `100`). |
| yAxisValueBorderPadding | Number | In Pixels | Sets the border padding for the Y-axis values. |
| yAxisValueBorderRadius | Number | In Pixels | Sets the border radius for the Y-axis values. |
| yAxisValueBorderThickness | Number | In Pixels | Sets the border thickness for the Y-axis values. |
| yAxisValueBorderDashed | True/False | 0/1 | Makes the Y-axis value borders dashed. Default value: 0 (border rendered using straight lines) |
| yAxisValueBorderDashLen | Number | In pixels | Sets the lengths of the individual dashes when the Y-axis value borders are dashed. |
| yAxisValueBorderDashGap | Number | In pixels | Sets the gaps between individual dashes when the Y-axis value borders are dashed. |
| yAxisValueLink | URL | Any | Sets a target link for all Y-axis values. |

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
| bgAngle | Number | 0-360 | Sets the angle of the background color, in case of a gradient. |
| bgImage | Text | Any | To place any image (JPG/PNG/GIF) as background of the chart, enter the (path and) name of the background image as a URL without quotes around it. It should be in the same domain as the chart. |
| bgImageAlpha | Number | 0 – 100 | This attribute specifies the opacity for the loaded background image. |
| bgImageDisplayMode | Text | stretch, tile, fit, fill, center, none | Helps you specify the mode in which the background image is to be displayed. Stretch – expands the image to fit the entire chart area, without maintaining original image constraints. Tile – the image is repeated as a pattern on the entire chart area. Fit – fits the image proportionately on the chart area. Fill -proportionately fills the entire chart area with the image. Center – the image is positioned at the center of the chart area. None – Default mode. |
| bgImageVAlign | Text | top, middle, bottom | Helps you to vertically align the background image. |
| bgImageHAlign | Text | left, middle, right | Helps you to horizontally align the background image. |
| bgImageScale | Number | 0-300 | Helps you magnify the background image.This attribute will only work when the attribute `bgImageDisplayMode` is set to none, center, or tile. |
| canvasBgColor | Color | Hex Color Code | This attribute sets the background color for the chart canvas. You can set any hex color code as the value of this attribute. To specify a gradient as canvas background color, separate the hex color codes of each color in the gradient using comma. Example: #FF5904, #FFFFFF. |
| canvasBgAlpha | Number | 0 – 100 | This attribute sets the background transparency for the chart canvas. For gradient, separate the alpha value using comma. Example: 15, 50. |
| canvasBgRatio | Numbers separated by comma | 0 – 100 | When a gradient is used to set the color of the canvas background, this attribute sets the ratio of the colors. Example : If the value of the `canvasBgColor` attribute is set as `#FF5904, #FFFFFF`, `canvasBgRatio` can be used to specify their ratio in the background. |
| canvasBgAngle | Number | 0-360 | Helps you specify canvas background angle in case of gradient. |
| showcanvasborder | True/False | 0/1 | This attribute if set to \_1\_, shows a border around the canvas of the chart. Default value: 0 |
| canvasBorderColor | Color | Hex Color Code | Lets you specify canvas border color. |
| canvasBorderThickness | Number | 0-5 | Lets you specify canvas border thickness. |
| canvasBorderAlpha | Number | 0 – 100 | Lets you control transparency of canvas border. |
| showVLineLabelBorder | True/False | 0/1 | If you’ve opted to show a label for any of your vLines in the chart, you can collectively configure whether to show border for all such labels using this attribute. If you want to show label border for just a particular vLine, you can over-ride this value by specifying border configuration for that specific vLine. |
| rotateVLineLabels | True/False | 0/1 | This attribute lets you set whether the vline labels will show up as rotated labels on the chart. Default value: 0 |
| logoURL | Text | URL | You can load an external logo (JPEG/PNG) to your chart, this attribute lets you specify the URL. Due to cross domain security restrictions it is advised to use a logo from the same domain name as your charts. |
| logoLeftMargin | Number | In Pixels | This attribute helps you set the amount of empty space that you want to put on the left side of your logo image. Nothing is rendered in this space. |
| logoTopMargin | Number | In Pixels | This attribute helps you set the amount of empty space that you want to put on top of your logo image. Nothing is rendered in this space. |
| logoPosition | Text | TL, TR, BL, BR, CC | Where to position the logo on the chart: TL – Top-left TR – Top-right BR – Bottom right BL – Bottom left CC – Center of screen |
| logoAlpha | Number | 0 – 100 | Once the logo has loaded on the chart, you can configure its opacity using this attribute. |
| logoScale | Number | 0-300 | You can also change the scale of an externally loaded logo at run-time by specifying a value for this parameter. |
| logoLink | Text | URL | If you want to link the logo to an external URL, specify the link in this attribute. The link can be in Exago BI Link format, allowing you to link to new windows, pop-ups, frames etc. |
| paletteThemeColor | Color | Any (color code without the # prefix) | Specifies a color theme that will be applied throughout the chart. |
| zoomPaneBorderColor | Color | Any (color code without the # prefix) | Sets the color of the zoom pane border. |
| zoomPaneBgColor | Color | Any (color code without the # prefix) | Sets the background color of the zoom pane. |
| zoomPaneBgAlpha | Number | 0 – 100 | Sets the alpha of the zoom pane. |
| pinLineThicknessDelta | Number | Any number | Sets the thickness of the pinned line when the chart is put to pin line mode. |
| pinPaneBgColor | Color | Any (color code without the # prefix) | Sets the background color of the pin pane. |
| pinPaneBgAlpha | Number | 0 – 100 | Sets the alpha of the pin pane. |
| showToolBarButtonTooltext | True/False | 0/1 | Enables/disables display of tooltips for toolbar buttons. |
| btnSwitchToPinModeTooltext | Text | Any string. | Replaces the default tooltext of ‘Switch to Pin Mode’ button with provided string. |

## Data Plot Cosmetics

These attributes let you configure how your plot (columns, lines, area, pie or any data that you’re plotting) will appear on the chart. If the plots can show borders, you can control the border properties using the attributes listed below. Or, if they support gradient fills, you can again configure various properties of the gradient using these attributes. Various other controls over plot cosmetics can be attained using this set of attributes.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| lineColor | Color | Hex Color Code | Color using which the lines on the chart will be drawn. |
| lineThickness | Number | In Pixels | Thickness of the lines on the chart. |
| lineAlpha | Number | 0 – 100 | Alpha of the lines on the chart. |

## Peak Data Attributes

These attributes let you enable peak data to be shown on the chart and set limits for it.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showPeakData | True/False | 0/1 | Specifies whether peak data will be shown. Default value: 0 (disabled) |
| maxPeakDataLimit | Number | Any | Defines the upper limit for peak data. Any value greater than this value will be considered peak data. If the value of `minPeakDataLimit` attribute is set more than `maxPeakDataLimit` attribute, the values between the range will be considered as peak data. |
| minPeakDataLimit | Number | Any | Defines the lower limit for peak data. Any value lower than this value will be considered peak data. If the value of `maxPeakDataLimit` attribute is set less than `minPeakDataLimit` attribute, the values between the range will be considered as peak data. |

## Scroll Properties

The following attributes let you set the scroll bar properties.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| scrollColor | Color | Hex Color Code | Color for scroll bar. |
| scrollPosition | Text | Top, Bottom | Sets the position of the scroll bar in the chart. `Default Value:` Bottom |
| flatscrollbars | True/False | 0/1 | This attribute can be used to set the scroll bar to flat or the basic one. Default value: 1 |
| scrollHeight | Number | In Pixels | Required height for scroll bar. |
| scrollPadding | Number | In Pixels | Distance between the end of canvas (bottom part) and start of scroll bar. This feature is not available in JavaScript charts. |
| scrollshowbuttons | True/False | 0/1 | Sets whether to show the left and right scroll button. |

## Anchors

On line/area charts, anchors (or marker points) are polygons which appear at the joint of two consecutive line/area points. These are indicators to show the position of data points. The anchors handle tool tips for the data points. So, if you opt to not render anchors on a chart, the tool tips won’t function. You can, however, hide them by setting alpha to 0 and still enable tool tips. You can customize all the facets of anchors using the properties below.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| drawAnchors | True/False | 0/1 | Whether to draw anchors on the chart. |
| anchorSides | Number | 3-20 | This attribute sets the number of sides the anchor will have. For for example, an anchor with 3 sides will represent a triangle, with 4 it will be a square and so on. |
| anchorStartAngle | Number | 0 – 360 | This attribute sets the starting angle of anchors. Default value: 90 |
| anchorRadius | Number | In pixels | This attribute sets the radius (in pixels) of the anchor. |
| anchorBorderColor | Color | Hex Color Code | Lets you set the border color of anchors. |
| anchorBorderThickness | Number | In Pixels | Helps you set border thickness of anchors. |
| anchorBgColor | Color | Hex Color Code | Helps you set the background color of anchors. |
| anchorBgAlpha | Number | 0 – 100 | Helps you set the alpha of anchor background. |
| anchorMinRenderDistance | Number |  | This attribute is used for specifying the minimum distance (between dataplots) for the anchors to become visible. |
| anchorImageUrl | Exago BI link format | URL | If you want to use an external image (JPG/PNG) as an anchor, this attribute lets you specify the URL. **Note:** Due to cross domain security restrictions it is advised to use an image from the same domain name as your charts. |
| anchorImageAlpha | Number | 0 – 100 | This attribute allows to set a transparency for images displayed as anchors in charts. Default value: 100 |
| anchorImageScale | Number | 0 – 100 | This attribute allows to set a scale for magnifying images displayed as anchors. Default value: 100 |
| anchorImagePadding | Number | In Pixels | This attribute sets the padding between the anchor image and the border of the anchor. For the anchor image, instead of decreasing the size of the image this attribute crops the image. Default value: 1 |

## Divisional Lines & Grids

Using this set of attributes, you can control the properties of divisional lines, zero plane and alternate color bands. Divisional Lines are horizontal lines running through the canvas. Each divisional line signifies a smaller unit of the entire axis thus aiding the users in interpreting the chart. The zero plane is a 2D/3D plane that signifies the 0 position on the chart. If there are no negative numbers on the chart, you won’t see a visible zero plane. Alternate color bands are colored blocks between two successive divisional lines.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| numDivLines | Number | Numeric value > 0 | Number of horizontal axis division lines that you want on the chart. |
| divLineColor | Color | Hex Color Code | Color for divisional lines. |
| divLineThickness | Number | 1-5 | Thickness of divisional lines. |
| divLineAlpha | Number | 0 – 100 | Alpha of divisional lines. |
| divLineDashed | True/False | 0/1 | Whether the divisional lines should be rendered as dashed lines. Default value: 0 (divisional lines rendered using straight lines) |
| divLineDashLen | Number | In pixels | Sets the length of each dash when divisional lines are rendered as dashed lines. |
| divLineDashGap | Number | In pixels | Sets the gap between two consecutive dashes when divisional lines are rendered as dashed lines. |
| zeroPlaneColor | Color | Hex Color Code | Color for the Zero Plane. Zero Plane is the line/plane that appears at position 0 on the y-axis, when negative data is being shown on the chart. |
| zeroPlaneThickness | Number | In Pixels | Thickness of zero plane. |
| zeroPlaneAlpha | Number | 0 – 100 | Alpha of zero plane. |
| showZeroPlaneValue | True/False | 0/1 | Allows you to show or hide the value on which the zero plane exists on the y-axis. By default, the value is displayed. |
| showAlternateHGridColor | True/False | 0/1 | Whether to show alternate colored horizontal grid bands. |
| alternateHGridColor | Color | Hex Color Code | Color of the alternate horizontal grid bands. |
| alternateHGridAlpha | Number | 0 – 100 | Alpha (transparency) of the alternate horizontal grid bands. |

## Legend Properties

In multi-series charts, the series name of each data set shows up in the legend of the chart. If you do not need the legend, you can opt to hide the same. Also, the legend can be placed at the bottom of the chart or to the right of the chart. Using the attributes below, you can configure the functional and cosmetic properties of the legend.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showLegend | True/False | 0/1 | Whether to show legend on the chart. |
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
| legendIconScale | Number | 1-5 | Scaling of legend icon is possible in Exago BI. This attribute lets you control the size of legend icon. |
| legendBgColor | Color | Hex Color Code | Background color for the legend. |
| legendBgAlpha | Number | 0 – 100 | Background alpha for the legend. |
| legendBorderColor | Color | Hex Color Code | Border Color for the legend. |
| legendBorderThickness | Number | In Pixels | Border thickness for the legend. |
| legendBorderAlpha | Number | 0 – 100 | Border alpha for the legend. |
| legendShadow | True/False | 0/1 | Whether to show a shadow for legend. |
| legendAllowDrag | True/False | 0/1 | The legend can be made drag-able by setting this attribute to 1. End viewers of the chart can drag the legend around on the chart. |
| legendScrollBgColor | Color | Hex Color Code | If you’ve too many items on the legend, a scroll bar shows up on the same. This attribute lets you configure the background color of the scroll bar. |
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

Exago BI offers you a lot of options to format your numbers on the chart. Using the attributes below, you can control a myriad of options like: Formatting of commas and decimals Number prefixes and suffixes Decimal places to which the numbers will round to Scaling of numbers based on a user defined scale Custom number input formats

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| formatNumber | True/False | 0/1 | This configuration determines whether the numbers displayed on the chart will be formatted using commas, for example, 40,000 if ‘formatNumber’: ‘1’; and 40000 if ‘formatNumber’: ‘0’;. |
| formatNumberScale | True/False | 0/1 | Configuration whether to add K (thousands) and M (millions) to a number after truncating and rounding it – for example, if `formatNumberScale` is set to 1, 10434 will become 1.04K . Same with numbers in millions – an M will be added at the end. |
| defaultNumberScale | Text | Any | The default unit of the numbers that you’re providing to the chart. |
| numberScaleUnit | Text | Any | Unit of each block of the scale. |
| numberScaleValue | Text | Any | Range of the various blocks that constitute the scale. |
| forceNumberScale | True/False | 0/1 | Forces the specified lower `numberScaleUnit` value to be applied to data values less than the specified `numberScaleValue`. This attribute works only when `“formatNumberScale”: “1”` and the `defaultNumberScale` attribute is not defined. For example, if `“numberScaleUnit”: “K, M”`, `“numberScaleValue”: “1000, 1000”`, and `“forceNumberScale”: “1”`, a data value of `400` will be rendered as `0.40K`. |
| scaleRecursively | True/False | 0/1 | Whether recursive scaling should be applied. |
| maxScaleRecursion | Number | Any | How many recursions to complete during recursive scaling? -1 completes the entire set of recursion. |
| scaleSeparator | Text | Any | What character to use to separate the scales that are generated after recursion? |
| numberPrefix | Text | Character | Using this attribute, you could add prefix to all the numbers visible on the graph. For example, to represent all dollars figure on the chart, you could specify this attribute to $ to show like $40000, $50000. |
| numberSuffix | Text | Character | Using this attribute, you could add prefix to all the numbers visible on the graph. For example, to represent all figures quantified as per annum on the chart, you could specify this attribute to ‘/a’ to show like 40000/a, 50000/a. |
| decimalSeparator | Text | Character | This attribute helps you specify the character to be used as the decimal separator in a number. |
| thousandSeparator | Text | Character | This attribute helps you specify the character to be used as the thousands separator in a number. |
| thousandSeparatorPosition | Number |  | This option helps you specify the position of the thousand separator. |
| decimals | Number | 0-10 | Number of decimal places to which all numbers on the chart will be rounded to. |
| forceDecimals | True/False | 0/1 | Whether to add 0 padding at the end of decimal numbers. For example, If you limit the maximum number of decimal digits to 2, a number like 55.345 will be rounded to 55.34. This does not mean that all numbers will be displayed with a fixed number of decimal places. For instance 55 will not be displayed as 55.00 and 55.1 will not become 55.10. In order to have fixed number of decimal places attached to all the numbers, set this attribute to 1. |

## Font Properties

Using the attributes below, you can define the generic font properties for all the text on the chart. These attributes allow you a high level control over font properties. If you intend to specify font properties for individual chart elements (like Caption, sub-caption etc.), you’ll need to use the Styles feature of Exago BI. Using Styles, you can also specify advanced font properties like Bold, Italics, HTML Mode etc.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| baseFont | Text | Font Name | This attribute lets you set the font face (family) of all the text (data labels, values etc.) on chart. If you specify the `outCnvBaseFont` attribute also, then this attribute controls only the font face of text within the chart canvas bounds. |
| baseFontSize | Number | 6 – 72 | This attribute sets the base font size of the chart that is, all the values and the names in the chart which lie on the canvas will be displayed using the font size provided here. |
| baseFontColor | Color | Hex Color Code | This attribute sets the base font color of the chart that is, all the values and the names in the chart which lie on the canvas will be displayed using the font color provided here. |
| outCnvBaseFont | Text | Font Name | This attribute sets the base font family of the chart text which lies outside the canvas that is, all the values and the names in the chart which lie outside the canvas will be displayed using the font name provided here. |
| outCnvBaseFontSize | Number | 6 – 72 | This attribute sets the base font size of the chart that is, all the values and the names in the chart which lie outside the canvas will be displayed using the font size provided here. |
| outCnvBaseFontColor | Color | Hex Color Code | This attribute sets the base font color of the chart that is, all the values and the names in the chart which lie outside the canvas will be displayed using the font color provided here. |

## Data Label Cosmetics

These attributes let you configure the cosmetics of all data labels of the chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| labelFont | Text | Font Name | Sets the x-axis label font family for the text. |
| labelFontColor | Color | Hex Color Code | Sets the x-axis label font color. |
| labelFontSize | Number | 6 – 72 | Specifies the x-axis label font size. |

## Tool-tip

These attributes let you control the tool tip. You can set the background color, border color, separator character and few other details.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showToolTip | True/False | 0/1 | Whether to show tool tip on chart. |
| toolTipBgColor | Color | Hex Color Code | Background color for tool tip. |
| toolTipColor | Color | Hex Color Code | Font color for the tool-tip. |
| toolTipBorderColor | Color | Hex Color Code | Border color for tool tip. |
| tooltipBorderAlpha | Number | 0 – 100 | Sets the border transparency for tool tip. |
| toolTipSepChar | Text | Any | The character specified as the value of this attribute separates the name and value displayed in tool tip. |
| showToolTipShadow | True/False | 0/1 | Whether to show shadow for tool-tips on the chart. |
| useCrossLine | True/False | 0/1 | There are two ways of displaying tool-tips in a zoomline chart. One is to use a cross-line, which is a vertical line that displays data values for all series on that data point. The other way is to use traditional tool-tips that display values on a data point when hovered upon. Default value is 1 which uses cross-line. Set this attribute value to 0 to use traditional tool-tips. |
| crossLineThickness | Number | In Pixels | If you’ve opted to show the tool-tips using cross-line, this attribute lets you define the thickness of cross-line. |
| crossLineColor | Color | Hex Color Code | If you’ve opted to show the tool-tips using cross-line, this attribute lets you define the color of cross-line. |
| crossLineAlpha | Number | 0 – 100 | If you’ve opted to show the tool-tips using cross-line, this attribute lets you define the transparency of cross-line. |
| crossLineLabelSize | Number | In Pixels | This attribute lets you define the label font size of cross-line. |
| crossLineLabelFont | Text | Font Name | This attribute lets you define the label font of cross-line. |
| crossLineValueSize | Number | In Pixels | This attribute lets you define the font size of values getting displayed using cross-line. |
| crossLineValueFont | Text | Font Name | This attribute lets you define the font of values getting displayed using cross-line. |

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
| reverseToolbarIcons | True/False | 0/1 | You can reverse the order in which the toolbar icons are rendered using this attribute. |

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
| plotHoverEffect | True/False | 0/1 | Whether to enable hover effect on charts for data plots (for example, column, pie) only |
| plotFillHoverColor | Color | Hex Color Code | Specifies the hover color for the data plots |
| plotFillHoverAlpha | Number | 1 – 100 | Specifies the hover alpha for data plots |

## Chart Padding & Margins

The following attributes help you control chart margins and padding. Exago BI allows you to manually customize the padding of various elements on the chart to allow advanced manipulation and control over chart visualization. You can also define the chart margins. Chart Margins refer to the empty space left on the top, bottom, left and right of the chart. That means, Exago BI will not plot anything in that space. It’s not necessary for you to specify any padding/margin values. Exago BI automatically assumes the best values for the same, if you do not specify the same.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| captionPadding | Number | In Pixels | This attribute lets you control the space (in pixels) between the sub-caption and top of the chart canvas. If the sub-caption is not defined, it controls the space between caption and top of chart canvas. If neither caption, nor sub-caption is defined, this padding does not come into play. |
| xAxisNamePadding | Number | In Pixels | Using this, you can set the distance between the top end of x-axis title and the bottom end of data labels (or canvas, if data labels are not to be shown). |
| yAxisNamePadding | Number | In Pixels | Using this, you can set the distance between the right end of y-axis title and the start of y-axis values (or canvas, if the y-axis values are not to be shown). |
| yAxisValuesPadding | Number | In Pixels | This attribute helps you set the horizontal space between the canvas left edge and the y-axis values or trend line values (on left/right side). This is particularly useful, when you want more space between your canvas and y-axis values. |
| valuePadding | Number | In Pixels | It sets the vertical space between the end of columns and start of value textboxes. This basically helps you control the space you want between your columns/anchors and the value textboxes. |
| chartLeftMargin | Number | In Pixels | Amount of empty space that you want to put on the left side of your chart. Nothing is rendered in this space. |
| chartRightMargin | Number | In Pixels | Amount of empty space that you want to put on the right side of your chart. Nothing is rendered in this space. |
| chartTopMargin | Number | In Pixels | Amount of empty space that you want to put on the top of your chart. Nothing is rendered in this space. |
| chartBottomMargin | Number | In Pixels | Amount of empty space that you want to put at the bottom of your chart. Nothing is rendered in this space. |
| legendPadding | Number | In Pixels | Padding of legend from right/bottom side of canvas |
| canvasPadding | Number | In Pixels | Lets you set the space between the canvas border and first & last data points |
| canvasLeftPadding | Number | In Pixels | This attribute lets you set the space between the left of the canvas border and the canvas of the chart. This attribute is particularly useful when your data plot gets clipped by the left border of the canvas. Using this attribute, you can control the amount of empty space between the chart left side and data plot which might get clipped. |
| canvasRightPadding | Number | In Pixels | This attribute lets you set the space between the right of the canvas border and the canvas of the chart. This attribute is particularly useful when your data plot gets clipped by the right border of the canvas. Using this attribute, you can control the amount of empty space between the chart right side and data plot which might get clipped. |
| canvasTopPadding | Number | In Pixels | This attribute lets you set the space between the top of the canvas border and the canvas of the chart. This attribute is particularly useful when your data plot gets clipped by the top border of the canvas. Using this attribute, you can control the amount of empty space between the chart’s top and data plot which might get clipped. |
| canvasBottomPadding | Number | In Pixels | This attribute lets you set the space between the bottom of the canvas border and the canvas of the chart. This attribute is particularly useful when your data plot gets clipped by the bottom border of the canvas. Using this attribute, you can control the amount of empty space between the chart’s bottom and data plot which might get clipped. |
| canvasLeftMargin | Number | In Pixels | This attribute lets you control the space between the start of chart canvas and the start (x) of chart. In case of 2D charts, the canvas is the visible rectangular box. In case of 3D charts, the canvas box is the imaginary box around the 3D canvas. Using this attribute, you can control the amount of empty space between the chart left side and canvas left side. By default, Exago BI automatically calculates this space depending on the elements to be placed on the chart. However, if you want to over-ride this value with a higher value, you can use this attribute to specify the same. Please note that you cannot specify a margin lower than what has been calculated by the chart. This attribute is particularly useful, when you’ve multiple charts placed in a page and want all their canvas start position to align with each other – so in such a case, you can set same margin value (a value large enough that it doesn’t get rejected by chart owing to it being lower than the calculated value) for all such charts in the page. |
| canvasRightMargin | Number | In Pixels | Like `canvasLeftMargin`, this attribute lets you set the space between end of canvas and end of chart. |
| canvasTopMargin | Number | In Pixels | Like `canvasLeftMargin`, this attribute lets you set the space between top of canvas and top of chart. |
| canvasBottomMargin | Number | In Pixels | Like `canvasLeftMargin`, this attribute lets you set the space between bottom of canvas and bottom of chart. |

## The categories Object

The `categories` object and the `category` object (child of the `categories` object) are used to specify x-axis labels for multi-series charts. The attributes of the `categories` object are used to set the font properties of all x-axis labels collectively.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| font | Text | Valid font face | Lets you specify font face for the x-axis data labels. |
| fontColor | Color | Hex Color Code | Lets you specify font color for the x-axis data labels. |
| fontSize | Number | Any | Lets you specify font size for the x-axis data labels. |

## The data set Object

Each `dataset` object contains a series of data. For example, for a monthly sales comparison chart for two successive years, the first data-set would contain the data for first year and the next one for the second year. You can provide data-set level cosmetics so that all data within that data-set will be plotted in the same color/alpha/etc. Depending on the chart type, there are a number of attributes that you can define for each `dataset` object.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| seriesName | Text | Any | Lets you specify the series name for a particular data set. For example, if you’re plotting a chart to indicate monthly sales analysis for 2005 and 2006, the `seriesName` for the first data set will be 2005 and that of the second will be 2006. The `seriesName` of a data set is shown in legend. |
| color | Color | Hex Color Code | This attribute sets the color using which line of that data set will be drawn |
| alpha | Text | 0 – 100 or Comma Separated List | This attribute sets the alpha (transparency) of the entire data set. |
| drawAnchors | True/False | 0/1 | Whether to draw anchors for the particular data set. |
| anchorRadius | Number | In Pixels | This attribute sets the radius (in pixels) of the anchors of the particular data set. |
| lineThickness | Number | In Pixels | Thickness of the lines for the particular data set. |
| anchorBorderColor | Color | Hex Color Code | Lets you set the border color of anchors of the particular data set. |
| anchorBorderThickness | Number | In Pixels | Helps you set border thickness of anchors of the particular data set. |
| anchorBgColor | Color | Hex Color Code | Helps you set the background color of anchors of the particular data set. |
| anchorBgAlpha | Number | 0 – 100 | Helps you set the alpha of anchor background of the particular data set. |
| includeInLegend | True/False | 0/1 | Whether to include the seriesName of this data set in legend. |
| dashed | True/False | 0/1 | Whether the line should appear as dashed. |

## Trend-lines

Trend-lines are horizontal lines that aid in interpretation of data with respect to some pre-determined value. For example, if you are plotting the sales data for the current year, you might want to show the previous year’s average monthly sales as a trend indicator for ease of comparison. The `lines` object, child of the `trendlines` object is used to add trend-lines to a chart. Although the `line` object has to be defined within the `trendlines` object, the latter cannot be used to collectively customize trend-lines, because it does not have any attributes of its own. The attributes of the `lines` object, child of the `trendlines` object, are used to create and customize trend-lines for charts.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| valueOnRight | True/False | 0/1 | Whether to show the trend line value on left side or right side of chart. This is particularly useful when the trend line display values on the chart are colliding with divisional lines values on the chart. |
| color | Text | Hex Color Code | Color of the trend line and its associated text |
| isTrendZone | True/False | 0/1 | Whether the trend will be displayed as a line or a zone (fill-colored rectangle). |
| showOnTop | True/False | 0/1 | Whether the trend line/zone will be displayed over data plots or under them. |
| thickness | Number | In Pixels | If you’ve opted to show the trend as a line, this attribute lets you define the thickness of trend line. |
| alpha | Number | 0 – 100 | Alpha of the trend line. |
| dashed | True/False | 0/1 | Whether the trendline should be rendered as dashed lines. Default value: 0 (trendline rendered using straight lines) |
| dashLen | Number | In pixels | Sets the width of each dash when trendline is rendered as dashed lines. |
| dashGap | Number | In pixels | Sets the gap between consecutive dashes when trendline is rendered as dashed lines. |
| startValue | Number | Numeric Value | The starting value for the trendline. Say, if you want to plot a slanted trendline from value 102 to 109, the `startValue` will be 102. |
| endValue | Number | Numeric Value | The ending y-axis value for the trendline. Say, if you want to plot a slanted trendline from value 102 to 109, the `endValue` will be 109. If you do not specify a value for `endValue`, it will automatically assume the same value as `startValue`. |
| displayValue | Text | Any | If you want to display a string caption for the trend line by its side, you can use this attribute. Example:` displayValue=’Last Month High’`. When you don’t supply this attribute, it automatically takes the value of `startValue`. |
| toolText | Text |  | Custom tool-text for this trendline/zone. |

## Trend-lines (Chart level attributes)

Trend-lines are horizontal lines that aid in interpretation of data with respect to some pre-determined value. For example, if you are plotting the sales data for the current year, you might want to show the previous year’s average monthly sales as a trend indicator for ease of comparison. Cosmetics for all the trend-lines rendered can be attained using this set of attributes. Although there are set of attributes of the `line object`, used to create and customize trend-lines, these set of attributes effect all the trend-lines rendered in your chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| trendlineColor | Color | Hex Color Code | Sets color of all the trend lines and its associated text in the chart. |
| trendlineThickness | Number | In Pixels | If you’ve opted to show the trend as a line, this attribute lets you define the thickness of all the trend lines in your chart. |
| trendlineAlpha | Number | 0 – 100 | Sets transparency for all the trend lines in your charts. |
| trendLineToolText | Text | Any | Sets the tooltip text of the trend-line. It accepts macros, plain text, and HTML tags, as string. |
| showTrendlinesOnTop | True/False | 0/1 | Whether all the trend line/zone will be displayed over data plots or under them. |

## Trend-lines Display Value Cosmetics

These attributes let you customize the text displayed with a trend-line.  
**Note:** These attributes belong to the `chart` object and not to the `line` object (child of the `trendline` object). They are, therefore, applied to all trend-lines on your chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| trendValueFont | Text | Font Name | Sets the font family for the trend-line display value. |
| trendValueFontSize | Number |  | Sets the font size for the trend-line display value. |
| trendValueFontBold | True/False | 0/1 | Sets whether the trend-line display value will be bold formatted. Default value: 0 (not bold formatted) |
| trendValueFontItalic | True/False | 0/1 | Sets whether the trend-line display value will be italicized. Default value: 0 (not italicized) |
| trendValueBgColor | Color | Hex Color Code | Sets the background color for the trend-line display value. |
| trendValueBorderColor | Color | Hex Color Code | Sets the border color for the trend-line display value. |
| trendValueAlpha | Number | 0 – 100 | Sets the transparency for the trend-line display value. Default value: 100 |
| trendValueBgAlpha | Number | 0 – 100 | Sets the transparency for the background of the trend-line display value. Default value: 100 |
| trendValueBorderAlpha | Number | 0 – 100 | Sets the transparency for the border around the trend-line display value. Default value: 100 |
| trendValueBorderPadding | Number | In pixels | Sets padding for the border around the trend-line display value. |
| trendValueBorderRadius | Number | In pixels | Sets the radius for the border around the trend-line display value. |
| trendValueBorderThickness | Number | In pixels | Sets the thickness for the border around the trend-line display value. |
| trendValueBorderDashed | True/False | 0/1 | Whether the border around the trend-line display value should be rendered as dashed lines. Default value: 0 (border rendered using straight lines) |
| trendValueBorderDashLen | Number | In pixels | Sets the length of each dash when the border around the trend-line display value is rendered as dashed lines. |
| trendValueBorderDashGap | Number | In pixels | Sets the gap between two consecutive dashes when the border around the trend-line display value is rendered as dashed lines. |
