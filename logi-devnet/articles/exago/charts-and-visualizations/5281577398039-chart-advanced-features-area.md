---
title: "Chart Advanced Features: Area"
id: 5281577398039
section: "Charts and Visualizations"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281577398039-Chart-Advanced-Features-Area
updated_at: 2022-05-03T22:08:28Z
---

# Chart Advanced Features: Area

# Chart Advanced Features: Area

The following sections provide a list of available advanced attributes available for controlling and customizing **Area** chart elements.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic contains documentation for advanced attributes which are third-party customizations that must be manually entered into the chart wizard. These topics were converted directly from the documentation provided by this third-party source. Not every attribute listed may be supported in Exago BI as some unexpected conflicts may occur in their integration within the application.

## Functional Attributes

These attributes let you control a variety of functional elements on the chart. For example, you can opt to show/hide data labels, data values. You can also set chart limits and extended properties.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| animation | True/False | 0/1 | This attribute gives you the option to control animation in your charts. If you do not want to animate any part of the chart, set this as 0. |
| animationDuration | Number | In seconds | This attribute sets the animation duration of the chart. `animationDuration` attribute is applicable only if animation of the chart is enabled. Default value: 1 sec |
| palette | Number | 1-5 | Exago BI uses the concept of Color Palettes. Each chart has 5 pre-defined color palettes which you can choose from. Each palette renders the chart in a different color theme. |
| paletteColors | Text | List of hex color codes separated by comma | While the `palette` attribute allows to select a palette theme that applies to chart background, canvas, font and tool-tips, it does not change the colors of data items (that is, column, line, pie etc.). Using `paletteColors` attribute, you can specify your custom list of hex colors for the data items. The list of colors have to be separated by comma for example, `”paletteColors”: “#FF0000, #0372AB, #FF5904…”`. The chart will cycle through the list of specified colors and then render the data plot accordingly. To use the same set of colors throughout all your charts in a web application, you can store the list of palette colors in your application globally and then provide the same in each chart JSON. |
| connectNullData | True/False | 0/1 | This attribute lets you control whether empty data sets in your data will be connected to each other OR do they appear as broken data sets. |
| showLabels | True/False | 0/1 | It sets the configuration whether the x-axis labels will be displayed or not. |
| maxLabelHeight | Number | In Pixels | This attribute can be used to set the maximum height for the x-axis labels (data labels) excluding the x-axis title. If any label goes beyond this height, the label will be truncated. In stagger mode, the number of stagger lines will be reduced if they exceed this value. |
| labelDisplay | Text | ‘AUTO’, ‘WRAP’, ‘STAGGER’, ‘ROTATE’, ‘NONE’ | Using this attribute, you can customize the alignment of data labels (x-axis labels). There are 5 options: AUTO, WRAP, STAGGER, ROTATE or NONE. By default, this attribute is set to AUTO mode which means that the alignment of the data labels is determined automatically depending on the size of the chart. WRAP wraps the label text if it is too long to fit in one line. ROTATE rotates the labels vertically. STAGGER divides the labels into multiple lines. |
| useEllipsesWhenOverflow | True/False | 0/1 | When enabled in auto mode, long data labels are truncated by adding ellipses to prevent them from overflowing the chart background. The default value is 1. |
| rotateLabels | True/False | 0/1 | This attribute lets you set whether the data labels will show up as rotated labels on the chart. |
| slantLabels | True/False | 0/1 | If you’ve opted to show rotated labels on chart, this attribute lets you set the configuration whether the labels will show as slanted labels or fully vertical ones. |
| labelStep | Number | 1 or above | By default, all the labels are displayed on the chart. However, if you’ve a set of streaming data (like name of months or days of week), you can opt to show every n-th label for better clarity. This attribute just lets you do so. When a value greater than 1 (n) is set to this attribute, the first label from left and every label at the n-th position from left will be displayed. for example, a chart showing data for 12 months and set with `labelStep: 3` will show labels for January, April, July, and October. The rest of the labels will be skipped. |
| staggerLines | Number | 2 or above | If you’ve opted for STAGGER mode as `labelDisplay`, using this attribute you can control how many lines to stagger the label to. By default, all labels are displayed in a single line. |
| showValues | True/False | 0/1 | Sets the configuration whether data values will be displayed along with the data plot on chart. |
| valuePosition | Text | “ABOVE”, “BELOW”, “AUTO” | If you’ve opted to show data values on the chart, this attribute lets you adjust the vertical alignment of data values with respect to dataplots. By default, this attribute is set to AUTO mode in which the alignment of each data value is determined automatically based on the position of each plot point. In ABOVE mode, data values are displayed above the plot points unless a plot point is too close to the upper edge of the canvas while in BELOW mode, data values are displayed below the plot points unless a plot point is too close to the lower edge of the canvas. |
| rotateValues | True/False | 0/1 | If you’ve opted to show data values, you can rotate them using this attribute. |
| showLimits | True/False | 0/1 | Whether to show chart limit values. If not specified `showYAxisValues` attribute overrides this value. |
| showDivLineValues | True/False | 0/1 | Whether to show div line values. If not specified `showYAxisValues` attribute overrides this value. |
| adjustDiv | True/False | 0/1 | Exago BI automatically tries to adjust divisional lines and limit values based on the data provided. However, if you want to set your explicit lower and upper limit values and number of divisional lines, first set this attribute to false. That will disable automatic adjustment of divisional lines. |
| clickURL | Text | Any | The entire chart can now act as a hotspot. Use this URL to define the hotspot link for the chart. The link can be specified in Exago BI Link format. |
| clickURLOverridesPlotLinks | True/False | 0/1 | Sets whether the `clickURL` attribute (that sets a link to which the user is directed when the chart is clicked) overrides the `link` attribute (that sets a link to which the user is directed when a data plot is clicked). Default value: 0 (`clickURL` does not override `link`) |
| setAdaptiveYMin | True/False | 0/1 | This attribute lets you set whether the y-axis lower limit will be 0 (in case of all positive values on chart) or should the y-axis lower limit adapt itself to a different figure based on values provided to the chart. |
| hasRTLText | Number | Any | This attribute, when set to `1`, indicates to the chart that the text (rendered on the chart) may contain RTL characters and the textual display has to be managed accordingly. |
| showPrintMenuItem | True/False | 0/1 | Whether to show “Print Chart” item in the context menu of the chart? Even if you opt to hide the item in context menu, you can still opt to invoke `print()` JavaScript method of the chart to print the same. |
| plotBinSize | Number | In Pixels | This attribute is used to skip the data plot without any change in visualization. When set to `1`, minimum one data plot will be rendered within the width of one pixel. Example, if `plotBinSize: 1`, minimum one column plot will be rendered within the width of one pixel. For line and area charts, minimum of two anchors connecting one single line will be drawn. If `plotBinSize: 0.5`, minimum two column plot will be rendered within the width of one pixel. Data skipping can be disabled by setting this attribute to `0`. Default value: `0.5` |
| labelBinSize | Number | In Pixels | This attribute is used to skip the labels of the data plots. When set to `1`, minimum one label will be displayed within the width of one pixel. To disable this label skipping, set this attribute to `0`. Default value: `1` |
| theme | Text | ‘fusion’, ‘gammel’, ‘candy’, ‘ocean’, ‘zune’, ‘carbon’, ‘umber’ | This attribute changes the theme of the chart. There are 7 types of themes which have been made according to the different color combinations. |

## Chart Message-related Attributes

These attributes let you set and configure custom chart messages, using text as well as images. These attributes are supported in Exago BI constructor (`Exago BI({ })`).

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
| axisLineAlpha | Number | 0 – 100 | Sets the transparency of the x-axis line. Will work only when \_showxaxisline\_ is set to 1. |
| showYAxisValues | True/False | 0/1 | Exago BI y-axis is divided into vertical sections using div (divisional) lines. Each div line assumes a value based on its position. Using this attribute you can set whether to show those div line (y-axis) values or not. This attribute shows or hides the y-axis divisional lines and limits. The values of `showLimits` and `showDivLineValues`, if specified explicitly, overrides the value of this attribute. |
| yAxisValuesStep | Number | 1 or above | By default, all div lines show their values. However, you can opt to display every x(th) div line value using this attribute. |
| rotateYAxisName | True/False | 0/1 | If you do not wish to rotate y-axis name, set this as 0. It specifically comes to use when you’ve the special characters (UTF-8) in your y-axis name that do not show up in rotated mode. |
| yAxisNameWidth | Number | (In Pixels) | If you opt to not rotate y-axis name, you can choose a maximum width that will be applied to y-axis name. |
| yAxisMinValue | Number | Numeric Value | This attribute helps you explicitly set the lower limit of the chart. If you don’t specify this value, it is automatically calculated by Exago BI based on the data provided by you. |
| yAxisMaxValue | Number | Numeric Value | This attribute helps you explicitly set the upper limit of the chart. If you don’t specify this value, it is automatically calculated by Exago BI based on the data provided by you. |
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

## Chart Cosmetics

The following attributes let you configure chart cosmetics like background color, background alpha, canvas color & alpha etc.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
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
| showBorder | True/False | 0/1 | Whether to show a border around the chart or not. |
| borderColor | Color | Hex Color Code | Border color of the chart. |
| borderThickness | Number | In Pixels | Border thickness of the chart. |
| borderAlpha | Number | 0 – 100 | Border alpha of the chart. |
| drawFullAreaBorder | True/False | 0/1 | When set to `0`, instead of drawing a border for the entire chart canvas, this attribute will draw line on the canvas only to connect the data-points. Default Value: `1` |
| showVLineLabelBorder | True/False | 0/1 | If you’ve opted to show a label for any of your vLines in the chart, you can collectively configure whether to show border for all such labels using this attribute. If you want to show label border for just a particular vLine, you can over-ride this value by specifying border configuration for that specific vLine. |
| rotateVLineLabels | True/False | 0/1 | This attribute lets you set whether the vline labels will show up as rotated labels on the chart. Default value: 0 |
| logoURL | Text | URL | You can load an external logo (JPEG/PNG) to your chart, this attribute lets you specify the URL. Due to cross domain security restrictions it is advised to use a logo from the same domain name as your charts. |
| logoLeftMargin | Number | In Pixels | This attribute helps you set the amount of empty space that you want to put on the left side of your logo image. Nothing is rendered in this space. |
| logoTopMargin | Number | In Pixels | This attribute helps you set the amount of empty space that you want to put on top of your logo image. Nothing is rendered in this space. |
| logoPosition | Text | TL, TR, BL, BR, CC | Where to position the logo on the chart: TL – Top-left TR – Top-right BR – Bottom right BL – Bottom left CC – Center of screen |
| logoAlpha | Number | 0 – 100 | Once the logo has loaded on the chart, you can configure its opacity using this attribute. |
| logoScale | Number | 0-300 | You can also change the scale of an externally loaded logo at run-time by specifying a value for this parameter. |
| logoLink | Text | URL | If you want to link the logo to an external URL, specify the link in this attribute. The link can be in Exago BI Link format, allowing you to link to new windows, pop-ups, frames etc. |

## Data Plot Cosmetics

These attributes let you configure how your plot (area in case of Area chart) will appear on the chart. If the plots can show borders, you can control the border properties using the attributes listed below. Or, if they support gradient fills, you can again configure various properties of the gradient using these attributes. Various other controls over plot cosmetics can be attained using this set of attributes.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showPlotBorder | True/False | 0/1 | Whether the column, area, pie etc. border will show up. |
| plotBorderColor | Color | Hex Color Code | Color for column, area, pie border |
| plotBorderThickness | Number | 0-5 | Thickness for column, area, pie border |
| plotBorderAlpha | Number | 0 – 100 | Alpha for column, area, pie border |
| plotBorderDashed | True/False | 0/1 | Whether the border around the data plots should be rendered using dashed lines. Default value: 0 (border rendered using straight lines) |
| plotBorderDashLen | Number | In pixels | Sets the length of each dash when the border around the data plots are rendered using dashed lines. |
| plotBorderDashGap | Number | In pixels | Sets the gap between two consecutive dashes when the border around the data plots are rendered using dashed lines. |
| plotFillAngle | Number | 0-360 | If you’ve opted to fill the plot (column, area etc.) as gradient, this attribute lets you set the fill angle for gradient. |
| plotFillRatio | Number | 0 – 100 | If you’ve opted to fill the plot (column, area etc.) as gradient, this attribute lets you set the ratio for gradient. |
| plotFillAlpha | Number | 0 – 100 | If you’ve opted to fill the plot (column, area etc.) as gradient, this attribute lets you set the fill alpha for gradient. |
| plotGradientColor | Color | Hex Color Code | You can globally add a gradient color to the entire plot of chart by specifying the second color as this attribute. For example, if you’ve specified individual colors for your dataplots and now you want a gradient that ends in white. You need to specify FFFFFF (white) as this color and the chart will now draw plots as gradient. |
| showShadow | True/False | 0/1 | Whether to apply the shadow effect for the data plot. |
| plotFillColor | Color | Hex Color Code | Fill Color for the area (Hex Color Code) |
| usePlotGradientColor | True/False | 0/1 | Gradient color is a color added globally to the entire plot of chart by specifying the second color in an attribute. This attribute sets the gradient color to \_true\_. Default value: 1 |
| drawFullAreaBorder | True/False | 0/1 | If the `showPlotBorder` attribute is set to `1`, set this attribute to `0` to draw only the top border of the data plot. |
| inheritPlotBorderColor | True/False | 0/1 | Set this attribute to `1` to inherit the data plot color of the area chart as the color of the data plot border. |

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

## Anchors

On area charts, anchors (or marker points) are polygons which appear at the joint of two consecutive line/area points. These are indicators to show the position of data points. The anchors handle tool tips and links for the data points. So, if you opt to not render anchors on a chart, the tool tips and links won’t function. You can, however, hide them by setting alpha to 0 and still enable tool tips and links. In area charts, anchors are set transparent by default. In case you wish to show the anchor, use anchorAlpha=”100″ attribute. You can customize all the facets of anchors using the properties below.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| drawAnchors | True/False | 0/1 | Whether to draw anchors on the chart. |
| anchorSides | Number | 3-20 | This attribute sets the number of sides the anchor will have. For for example, an anchor with 3 sides will represent a triangle, with 4 it will be a square and so on. |
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
| numVDivLines | Number | Numeric value > 0 | Number of vertical axis division lines |
| vDivLineColor | Color | Hex Color Code | Color of vertical axis division lines. |
| vDivLineThickness | Number | In Pixels | Thickness of vertical axis division lines. |
| vDivLineAlpha | Number | 0 – 100 | Alpha of vertical axis division lines. |
| vDivLineDashed | True/False | 0/1 | Whether the vertical divisional lines should be rendered as dashed lines. Default value: 0 (vertical divisional lines using straight lines) |
| vDivLineDashLen | Number | In pixels | Sets the width of each dash when vertical divisional lines are rendered as dashed lines. |
| vDivLineDashGap | Number | In pixels | Sets the gap between two consecutive dashes when vertical divisional lines are rendered as dashed lines. |
| showAlternateVGridColor | True/False | 0/1 | Whether to show alternate vertical colored grid bands. |
| alternateVGridColor | Color | Hex Color Code | Color of alternate vertical colored grid bands. |
| alternateVGridAlpha | Number | 0 – 100 | Alpha of alternate vertical colored grid bands. |

## Number Formatting

Exago BI offers you a lot of options to format your numbers on the chart. Using the attributes below, you can control a myriad of options like: Formatting of commas and decimals Number prefixes and suffixes Decimal places to which the numbers will round to Scaling of numbers based on a user defined scale Custom number input formats

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| formatNumber | True/False | 0/1 | This configuration determines whether the numbers displayed on the chart will be formatted using commas, for example, 40,000 if ‘formatNumber’: ‘1’; and 40000 if ‘formatNumber’: ‘0’;. |
| formatNumberScale | True/False | 0/1 | Configuration whether to add K (thousands) and M (millions) to a number after truncating and rounding it – for example, if `formatNumberScale` is set to 1, 1043 will become 1.04K (with decimals set to 2 places). Same with numbers in millions – an M will be added at the end. |
| defaultNumberScale | Text | Any | The default unit of the numbers that you’re providing to the chart. |
| numberScaleUnit | Text | Any | Unit of each block of the scale. |
| numberScaleValue | Text | Any | Range of the various blocks that constitute the scale. |
| forceNumberScale | True/False | 0/1 | If a data value is less than the lowest given number is the number scale, this attribute forces the lower value of the `numberScaleUnit` to be applied to that data value. This attribute works only when `”formatNumberScale”: “1”` and the `defaultNumberScale` attribute is not defined. For example, if `”numberScaleUnit”: “K, M”`, `”numberScaleValue”: “1000, 1000″`, and `”forceNumberScale”: “1”`, a data value of \*\*400\*\* will be rendered as \*\*0.40K\*\*. |
| scaleRecursively | True/False | 0/1 | Whether recursive scaling should be applied. |
| maxScaleRecursion | Number | Any | How many recursions to complete during recursive scaling? -1 completes the entire set of recursion. |
| scaleSeparator | Text | Any | What character to use to separate the scales that are generated after recursion? |
| numberPrefix | Text | Character | Using this attribute, you could add prefix to all the numbers visible on the graph. For example, to represent all dollars figure on the chart, you could specify this attribute to $ to show like $40000, $50000. |
| numberSuffix | Text | Character | Using this attribute, you could add a suffix to all the numbers visible on the graph. For example, to represent all figures quantified as per annum on the chart, you could specify this attribute to ‘/a’ to show like 40000/a, 50000/a. |
| decimalSeparator | Text | Character | This attribute helps you specify the character to be used as the decimal separator in a number. |
| thousandSeparator | Text | Character | This attribute helps you specify the character to be used as the thousands separator in a number. |
| thousandSeparatorPosition | Number |  | This option helps you specify the position of the thousand separator. |
| inDecimalSeparator | Text | Character | In some countries, commas are used as decimal separators and dots as thousand separators. In XML, if you specify such values, it will give an error while converting to number. So, Exago BI accepts the input decimal and thousand separator from user, so that it can convert it accordingly into the required format. This attribute lets you input the decimal separator. |
| inThousandSeparator | Text | Character | In some countries, commas are used as decimal separators and dots as thousand separators. In XML, if you specify such values, it will give an error while converting to number. So, Exago BI accepts the input decimal and thousand separator from user, so that it can convert it accordingly into the required format. This attribute lets you input the thousand separator. |
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
| labelLink | URL | Any | Sets a link for all x-axis labels. |

## Cross Line Attributes

Using these attributes, you can set and configure cross line and set its cosmetics like color, alpha, etc.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| drawCrossLine | True/False | 0/1 | This attribute sets a cross line (vertical line/area), when you hover a data plot. Default value: `0` |
| crossLineColor | Color | Hex Color Code | This attribute sets the color of the cross line. Default value: `#EEEEEE` |
| crossLineAlpha | Number | 0 – 100 | This attribute sets the opacity of the cross line. Default value: `50` |
| crossLineAnimation | True/False | 0/1 | This attributes enables the animation for the cross line. Default value: `0` |
| crossLineAnimationDuration | Number | In seconds | This attribute sets the animation duration of the cross line. Default value: `0.09 seconds` |
| plotColorinTooltip | True/False | 0/1 | This attribute displays the color of each plot with their labels in tooltip. Default value: `0` |
| drawCrossLineOnTop | True/False | 0/1 | This attribute is used to determine if the cross line will be drawn above the data plot or below the data plot. Default value: `0` |

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
| showToolTipShadow | True/False | 0/1 | Whether to show shadow for tool-tips on the chart. |
| tooltipbgalpha | Number | 0 – 100 | Sets the transparency of the tooltip. |
| tooltipborderradius | Number | In Pixels | Sets the border radius of the tooltip. |
| tooltipborderthickness | Number | In Pixels | Sets the border thickness of the tooltip. |
| toolTipPadding | Number | In Pixels | This attribute sets the vertical space between the value and the border of the tooltip. If you want more space between the value and the border, you can use this attribute to control it. |
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
| anchorHoverColor | Color | Hex Color Code | This attribute sets the hover color for anchors. |
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

The following attributes help you control chart margins and padding. Exago BI allows you manually customize the padding of various elements on the chart to allow advanced manipulation and control over chart visualization. You can also define the chart margins. Chart Margins refer to the empty space left on the top, bottom, left and right of the chart. That means, Exago BI will not plot anything in that space. It’s not necessary for you to specify any padding/margin values. Exago BI automatically assumes the best values for the same, if you do not specify the same.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| captionPadding | Number | In Pixels | This attribute lets you control the space (in pixels) between the sub-caption and top of the chart canvas. If the sub-caption is not defined, it controls the space between caption and top of chart canvas. If neither caption, nor sub-caption is defined, this padding does not come into play. |
| xAxisNamePadding | Number | In Pixels | Using this, you can set the distance between the top end of x-axis title and the bottom end of data labels (or canvas, if data labels are not to be shown). |
| yAxisNamePadding | Number | In Pixels | Using this, you can set the distance between the right end of y-axis title and the start of y-axis values (or canvas, if the y-axis values are not to be shown). |
| yAxisValuesPadding | Number | In Pixels | This attribute helps you set the horizontal space between the canvas left edge and the y-axis values or trend line values (on left/right side). This is particularly useful, when you want more space between your canvas and y-axis values. |
| labelPadding | Number | In Pixels | This attribute sets the vertical space between the labels and canvas bottom edge. If you want more space between the canvas and the x-axis labels, you can use this attribute to control it. |
| valuePadding | Number | In Pixels | It sets the vertical space between the end of columns and start of value textboxes. This basically helps you control the space you want between your columns/anchors and the value textboxes. |
| chartLeftMargin | Number | In Pixels | Amount of empty space that you want to put on the left side of your chart. Nothing is rendered in this space. |
| chartRightMargin | Number | In Pixels | Amount of empty space that you want to put on the right side of your chart. Nothing is rendered in this space. |
| chartTopMargin | Number | In Pixels | Amount of empty space that you want to put on the top of your chart. Nothing is rendered in this space. |
| chartBottomMargin | Number | In Pixels | Amount of empty space that you want to put at the bottom of your chart. Nothing is rendered in this space. |
| canvasPadding | Number | In Pixels | Lets you set the space between the canvas border and first & last data points |
| canvasLeftPadding | Number | In Pixels | This attribute lets you set the space between the left of the canvas border and the canvas of the chart. This attribute is particularly useful when your data plot gets clipped by the left border of the canvas. Using this attribute, you can control the amount of empty space between the chart left side and data plot which might get clipped. |
| canvasRightPadding | Number | In Pixels | This attribute lets you set the space between the right of the canvas border and the canvas of the chart. This attribute is particularly useful when your data plot gets clipped by the right border of the canvas. Using this attribute, you can control the amount of empty space between the chart right side and data plot which might get clipped. |
| canvasTopPadding | Number | In Pixels | This attribute lets you set the space between the top of the canvas border and the canvas of the chart. This attribute is particularly useful when your data plot gets clipped by the top border of the canvas. Using this attribute, you can control the amount of empty space between the chart’s top and data plot which might get clipped. |
| canvasBottomPadding | Number | In Pixels | This attribute lets you set the space between the bottom of the canvas border and the canvas of the chart. This attribute is particularly useful when your data plot gets clipped by the bottom border of the canvas. Using this attribute, you can control the amount of empty space between the chart’s bottom and data plot which might get clipped. |
| canvasLeftMargin | Number | In Pixels | This attribute lets you control the space between the start of chart canvas and the start (x) of chart. In case of 2D charts, the canvas is the visible rectangular box. In case of 3D charts, the canvas box is the imaginary box around the 3D canvas. Using this attribute, you can control the amount of empty space between the chart left side and canvas left side. By default, Exago BI automatically calculates this space depending on the elements to be placed on the chart. However, if you want to over-ride this value with a higher value, you can use this attribute to specify the same. Please note that you cannot specify a margin lower than what has been calculated by the chart. This attribute is particularly useful, when you’ve multiple charts placed in a page and want all their canvas start position to align with each other – so in such a case, you can set same margin value (a value large enough that it doesn’t get rejected by chart owing to it being lower than the calculated value) for all such charts in the page. |
| canvasRightMargin | Number | In Pixels | Like `canvasLeftMargin`, this attribute lets you set the space between end of canvas and end of chart. |
| canvasTopMargin | Number | In Pixels | Like `canvasLeftMargin`, this attribute lets you set the space between top of canvas and top of chart. |
| canvasBottomMargin | Number | In Pixels | Like `canvasLeftMargin`, this attribute lets you set the space between bottom of canvas and bottom of chart. |

## The data Object

In single-series charts, each instance of the `data` object represents a data value to be plotted on the chart. For a single-series chart, one instance of the `data` object looks as shown in the example below:

```
"data"[{
		"label": "Jan",
		"value": "10000"
	}]
```

Attributes of the `data` object are used to set and configure the data values for the chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| anchorAlpha | Number | 0 – 100 | If you want to configure data item specific anchor properties, this attribute lets you set the alpha for the anchor of that particular data item. |
| anchorBgAlpha | Number | 0 – 100 | If you want to configure data item specific anchor properties, this attribute lets you set the background alpha for the anchor of that particular data item. |
| anchorBgColor | Color | Hex Color Code | If you want to configure data item specific anchor properties, this attribute lets you set the background color for the anchor of that particular data item. |
| anchorBorderColor | Color | Hex Color Code | If you want to configure data item specific anchor properties, this attribute lets you set the border color for the anchor of that particular data item. |
| anchorBorderThickness | Number | In Pixels | If you want to configure data item specific anchor properties, this attribute lets you set the border thickness for the anchor of that particular data item. |
| anchorRadius | Number | In Pixels | If you want to configure data item specific anchor properties, this attribute lets you define the radius for the anchor of that particular data item. |
| anchorSides | Number | 3 or more | If you want to configure data item specific anchor properties, this attribute lets you define the number of sides for the anchor of that particular data item. |
| anchorStartAngle | Number | 0 – 360 | This attribute sets the starting angle for an anchor of a particular data. Default value: 90 |
| displayValue | Text | Any | If instead of the numerical value of this data, you wish to display a custom string value, you can specify the same here. Examples are annotation for a data item etc. |
| label | Text | Any | This attribute determines the label for the data item. The label appears on the x-axis of chart. **Note:** The `label` attribute replaces the `name` attribute. Previously, either one of the attributes could be used to set the label. Support for the `name` attribute has been discontinued since v3.10.0. |
| link | Text | Any | You can define links for individual data items. That enables the end user to click on data items (columns, lines, bars etc.) and drill down to other pages. To define the link for data items, use the link attribute. You can define links that open in same window, new window, pop-up window or frames. Please see “Drill-Down > Using JavaScript Functions as Links” for more information. Also, you’ll need to Url Encode all the special characters (like ? and &) present in the link. |
| showLabel | True/False | 0/1 | You can individually opt to show/hide labels of individual data items using this attribute. |
| showValue | True/False | 0/1 | You can individually opt to show/hide values of individual data items using this attribute. |
| valueFontColor | Color | Hex Color Code | Specifies the font color of a data value for an individual data plot. |
| valueBgColor | Color | Hex Color Code | Sets the background color of a value text for an individual data plot. |
| valueBorderColor | Color | Hex Color Code | Sets the border color around the value text for an individual data plot. |
| toolText | Text | Any | By default, Exago BI shows the data item name and value as tool tip text for that data item. But, if you want to display more information for the data item as tool tip, you can use this attribute to specify the same. |
| value | Number | Any | Numerical value for the data item. This value will be plotted on the chart. |
| valuePosition | Text | “ABOVE”, “BELOW”, “AUTO” | If you’ve opted to show data values on the chart, this attribute lets you adjust the vertical alignment of data values with respect to dataplots. By default, this attribute is set to AUTO mode in which the alignment of each data value is determined automatically based on the position of each plot point. In ABOVE mode, data values are displayed above the plot points unless a plot point is too close to the upper edge of the canvas while in BELOW mode, data values are displayed below the plot points unless a plot point is too close to the lower edge of the canvas. |
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
| labelBorderDashed | True/False | 0/1 | Whether the border around x-axis label should be rendered using dashed lines. Default value: 0 (border rendered using straight lines) |
| labelBorderDashLen | Number | In pixels | Sets the length of each dash when the border around the x-axis label is rendered using dashed lines. |
| labelBorderDashGap | Number | In pixels | Sets the gap between two consecutive dashes when the border around x-axis label is rendered using dashed lines. |
| labelLink | URL | Any | Sets the link for each individual x-axis label. |
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

## Vertical Data Separator Lines

Vertical data separator lines help you separate data blocks. These lines run through the height of the chart, thereby segregating the data into two different blocks. Vertical lines are defined as shown in the example below:

```
"data": [{
			"label": "Grade 1",
		},
		{
			"vLine": "true",
			"label": "Appraisal"
		}]
	}]
```

You can configure the cosmetics of vertical separator lines using the following attributes:

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| vLine | Text | Any | Set this attribute to `true` to render a vertical data separator line. |
| color | Color | Hex Color Code | This attribute defines the color of vertical separator line |
| thickness | Number | In Pixels | Thickness in pixels of the vertical separator line. |
| alpha | Number | 0 – 100 | Alpha of the vertical separator line. |
| dashed | True/False | 0/1 | Whether the vertical separator line should be rendered as dashed lines. Default value: 0 (vertical separator line rendered using straight lines) |
| dashLen | Number | In pixels | Sets the width of each dash when vertical separator line is rendered as dashed lines. |
| dashGap | Number | In pixels | Sets the gap between consecutive dashes when vertical separator line is rendered as dashed lines. |
| label | Text |  | Label for the vertical separator line, if to be shown. **Note:** The `label` attribute replaces the `name` attribute. Previously, either one of the attributes could be used to set the label. Support for the `name` attribute has been discontinued since v3.10.0. |
| showLabelBorder | True/False | 0/1 | Whether to show a border around the vLine label. |
| linePosition | Number | 0-1 | Helps configure the position of vertical line that is, if a vLine is to be plotted between 2 points Jan and Feb, user can set any position between 0 and 1 to indicate the relative position of vLine between these two points (0 means Jan and 1 means Feb). By default, it’s 0.5 to show in between the points. |
| labelPosition | Number | 0-1 | Helps configure the position of the vLine label by setting a relative position between 0 and 1. In vertical charts, 0 means top of canvas and 1 means bottom. In horizontal charts, 0 means left of canvas and 1 means right. |
| labelHAlign | Text | left, center, right | Horizontal anchor point for the alignment of vLine label. |
| labelVAlign | Text | top, middle, bottom | Vertical anchor point for the alignment of vLine label. |

## Trend-lines

Trend-lines are horizontal lines that aid in interpretation of data with respect to some pre-determined value. For example, if you are plotting the sales data for the current year, you might want to show the previous year’s average monthly sales as a trend indicator for ease of comparison. The `line` object, child of the `trendlines` object is used to add trend-lines to a chart. Although the `line` object has to be defined within the `trendlines` object, the latter cannot be used to collectively customize trend-lines, because it does not have any attributes of its own. The attributes of the `line` object, child of the `trendlines` object, are used to create and customize trend-lines for charts.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| startValue | Number | Numeric Value | The starting value for the trendline. Say, if you want to plot a slanted trendline from value 102 to 109, the `startValue` will be 102. |
| endValue | Number | Numeric Value | The ending y-axis value for the trendline. Say, if you want to plot a slanted trendline from value 102 to 109, the `endValue` will be 109. If you do not specify a value for `endValue`, it will automatically assume the same value as `startValue`. |
| displayValue | Text | Any | If you want to display a string caption for the trend line by its side, you can use this attribute. Example: `displayValue=’Last Month High’`. When you don’t supply this attribute, it automatically takes the value of `startValue`. |
| color | Text | Hex Color Code | Color of the trend line and its associated text |
| isTrendZone | True/False | 0/1 | Whether the trend will be displayed as a line or a zone (fill-colored rectangle). |
| showOnTop | True/False | 0/1 | Whether the trend line/zone will be displayed over data plots or under them. |
| thickness | Number | In Pixels | If you’ve opted to show the trend as a line, this attribute lets you define the thickness of trend line. |
| alpha | Number | 0 – 100 | Alpha of the trend line. |
| dashed | True/False | 0/1 | Whether the trendline should be rendered as dashed lines. Default value: 0 (trendline rendered using straight lines) |
| dashLen | Number | In pixels | Sets the width of each dash when trendline is rendered as dashed lines. |
| dashGap | Number | In pixels | Sets the gap between consecutive dashes when trendline is rendered as dashed lines. |
| valueOnRight | True/False | 0/1 | Whether to show the trend line value on left side or right side of chart. This is particularly useful when the trend line display values on the chart are colliding with divisional lines values on the chart. |
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

These attributes let you customize the display value set for trend-lines.  
**Note:** These attributes belong to the `chart` object and not to the `line` object (child of the `trendline` object). They are, therefore, applied to all trend-lines on your chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| trendValueFont | Text | Font Name | Sets the font family for the trend-line display value. |
| trendValueFontSize | Number | In pixels | Sets the font size for the trend-line display value. |
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
