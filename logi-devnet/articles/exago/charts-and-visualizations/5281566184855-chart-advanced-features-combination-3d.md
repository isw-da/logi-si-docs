---
title: "Chart Advanced Features: Combination 3D"
id: 5281566184855
section: "Charts and Visualizations"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281566184855-Chart-Advanced-Features-Combination-3D
updated_at: 2022-05-03T22:08:27Z
---

# Chart Advanced Features: Combination 3D

# Chart Advanced Features: Combination 3D

The following sections provide a list of available advanced attributes available for controlling and customizing **3D Combination** chart elements.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic contains documentation for advanced attributes which are third-party customizations that must be manually entered into the chart wizard. These topics were converted directly from the documentation provided by this third-party source. Not every attribute listed may be supported in Exago BI as some unexpected conflicts may occur in their integration within the application.

## Functional Attributes

These attributes let you control a variety of functional elements on the chart. For example, you can opt to show/hide data labels, data values. You can also set chart limits and extended properties.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| animation | True/False | 0/1 | This attribute gives you the option to control animation in your charts. If you do not want to animate any part of the chart, set this as 0. `By default, `animation` is set to 1. |
| animationDuration | Number | In seconds | This attribute sets the animation duration of the chart. `animationDuration` attribute is applicable only if animation of the chart is enabled. Default value: 1 sec |
| animate3D | True/False | 0/1 | This attribute enables you to set whether the initial animation of the 3D elements in chart canvas will occur or not. If set to 0, it will also set off chart canvas’ rotation while using JavaScript API functions like `view2D(), resetView(), rotateView(). `The view will be updated instantly without any rotation or animation. |
| exeTime | Number | 0.00 – 10.00 | It sets the time in seconds (can accept decimals) that the 3D elements of the chart take to animate when the chart is rendered initially. This attribute also sets the time that the chart canvas will take to animate when the chart is transformed to any view (View3D, View 2D, Reset View) using context menu (right click menu). This is also applicable while using JavaScript API functions – `view2D(), view3D, resetView() or rotateView()`. Default value is 0.5. |
| palette | Number | 1-5 | Exago BI uses the concept of Color Palettes. Each chart has 5 pre-defined color palettes which you can choose from. Each palette renders the chart in a different color theme. |
| paletteColors | Text | List of hex color codes separated by comma | While the `palette` attribute allows to select a palette theme that applies to chart background, canvas, font and tool-tips, it does not change the colors of data items (that is, column, line, pie etc.). Using `paletteColors` attribute, you can specify your custom list of hex colors for the data items. The list of colors have to be separated by comma for example, `”paletteColors”: “#FF0000, #0372AB, #FF5904…”`. The chart will cycle through the list of specified colors and then render the data plot accordingly. To use the same set of colors throughout all your charts in a web application, you can store the list of palette colors in your application globally and then provide the same in each chart JSON. |
| connectNullData | True/False | 0/1 | This attribute lets you control whether empty data sets in your data will be connected to each other OR do they appear as broken data sets. |
| areaOverColumns | True/False | 0/1 | If you’ve both area and column plots on the combination chart, this attribute lets you configure whether area chart will appear over column chart. |
| showLabels | True/False | 0/1 | It sets the configuration whether the x-axis labels will be displayed or not. |
| maxLabelHeight | Number | In Pixels | This attribute can be used to set the maximum height for the x-axis labels (data labels) excluding the x-axis title. If any label goes beyond this height, the label will be truncated. In stagger mode, the number of stagger lines will be reduced if they exceed this value. |
| labelDisplay | Text | ‘AUTO’, ‘WRAP’, ‘STAGGER’, ‘ROTATE’, ‘NONE’ | Using this attribute, you can customize the alignment of data labels (x-axis labels). There are 5 options: AUTO, WRAP, STAGGER, ROTATE or NONE. By default, this attribute is set to AUTO mode which means that the alignment of the data labels is determined automatically depending on the size of the chart. WRAP wraps the label text if it is too long to fit in one line. ROTATE rotates the labels vertically. STAGGER divides the labels into multiple lines. |
| useEllipsesWhenOverflow | True/False | 0/1 | When enabled in auto mode, long data labels are truncated by adding ellipses to prevent them from overflowing the chart background. The default value is 1. |
| rotateLabels | True/False | 0/1 | This attribute lets you set whether the data labels will show up as rotated labels on the chart. |
| slantLabels | True/False | 0/1 | If you’ve opted to show rotated labels on chart, this attribute lets you set the configuration whether the labels will show as slanted labels or fully vertical ones. |
| showValues | True/False | 0/1 | Sets the configuration whether data values will be displayed along with the data plot on chart. |
| valuePosition | Text | “ABOVE”, “BELOW”, “AUTO” | If you’ve opted to show data values on the chart, this attribute lets you adjust the vertical alignment of data values with respect to dataplots. By default, this attribute is set to AUTO mode in which the alignment of each data value is determined automatically based on the position of each plot point. In ABOVE mode, data values are displayed above the plot points unless a plot point is too close to the upper edge of the canvas while in BELOW mode, data values are displayed below the plot points unless a plot point is too close to the lower edge of the canvas. |
| rotateValues | True/False | 0/1 | If you’ve opted to show data values, you can rotate them using this attribute. |
| placeValuesInside | True/False | 0/1 | If you’ve opted to show data values, you can show them inside the columns using this attribute. By default, the data values show outside the column. |
| labelStep | Number | 1 or above | By default, all the labels are displayed on the chart. However, if you’ve a set of streaming data (like name of months or days of week), you can opt to show every n-th label for better clarity. This attribute just lets you do so. When a value greater than 1 (n) is set to this attribute, the first label from left and every label at the n-th position from left will be displayed. for example, a chart showing data for 12 months and set with `labelStep: 3` will show labels for January, April, July, and October. The rest of the labels will be skipped. |
| staggerLines | Number | 2 or above | If you’ve opted for STAGGER mode as `labelDisplay`, using this attribute you can control how many lines to stagger the label to. By default, all labels are displayed in a single line. |
| showLimits | True/False | 0/1 | Whether to show chart limit values. If not specified `showYAxisValues` attribute overrides this value. |
| showDivLineValues | True/False | 0/1 | Whether to show div line values. If not specified `showYAxisValues` attribute overrides this value. |
| showShadow | True/False | 0/1 | Whether to apply the shadow effects for data plot. |
| adjustDiv | True/False | 0/1 | Exago BI automatically tries to adjust divisional lines and limit values based on the data provided. However, if you want to set your explicit lower and upper limit values and number of divisional lines, first set this attribute to false. That will disable automatic adjustment of divisional lines. |
| clickURL | Text | Any | The entire chart can now act as a hotspot. Use this URL to define the hotspot link for the chart. The link can be specified in Exago BI Link format. |
| clickURLOverridesPlotLinks | True/False | 0/1 | Sets whether the `clickURL` attribute (that sets a link to which the user is directed when the chart is clicked) overrides the `link` attribute (that sets a link to which the user is directed when a data plot is clicked). Default value: 0 (`clickURL` does not override `link`) |
| setAdaptiveYMin | True/False | 0/1 | This attribute lets you set whether the y-axis lower limit will be 0 (in case of all positive values on chart) or should the y-axis lower limit adapt itself to a different figure based on values provided to the chart. |
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
| transposeAxis | True/False | 0/1 | If you hide a data set using legend icon, this attribute (when set to `1`) will compute the axes limit with respect to maximum and minimum value of the visible data set(s). Default value: 0 |
| showYAxisValues | True/False | 0/1 | Exago BI y-axis is divided into vertical sections using div (divisional) lines. Each div line assumes a value based on its position. Using this attribute you can set whether to show those div line (y-axis) values or not. This attribute shows or hides the y-axis divisional lines and limits. The values of `showLimits` and `showDivLineValues`, if specified explicitly, overrides the value of this attribute. |
| yAxisValuesStep | Number | 1 or above | By default, all div lines show their values. However, you can opt to display every x(th) div line value using this attribute. |
| rotateYAxisName | True/False | 0/1 | If you do not wish to rotate y-axis name, set this as 0. It specifically comes to use when you’ve the special characters (UTF-8) in your y-axis name that do not show up in rotated mode. |
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

The following attributes let you configure chart cosmetics like background color, background alpha, canvas color etc.

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
| showcanvasborder | True/False | 0/1 | This attribute if set to \_1\_, shows a border around the canvas of the chart. Default value: 0 |
| canvasBgAlpha | Number | 0 – 100 | This attribute sets the background transparency for the chart canvas. For gradient, separate the alpha value using comma. Example: 15, 50. |
| canvasBgColor | Color | Hex Color Code | This attribute sets the background color for the chart canvas. You can set any hex color code as the value of this attribute. To specify a gradient as canvas background color, separate the hex color codes of each color in the gradient using comma. Example: #FF5904, #FFFFFF. |
| showVLineLabelBorder | True/False | 0/1 | If you’ve opted to show a label for any of your vLines in the chart, you can collectively configure whether to show border for all such labels using this attribute. If you want to show label border for just a particular vLine, you can over-ride this value by specifying border configuration for that specific vLine. |
| rotateVLineLabels | True/False | 0/1 | This attribute lets you set whether the vline labels will show up as rotated labels on the chart. Default value: 0 |
| logoURL | Text | URL | You can load an external logo (JPEG/PNG) to your chart, this attribute lets you specify the URL. Due to cross domain security restrictions it is advised to use a logo from the same domain name as your charts. |
| logoLeftMargin | Number | In Pixels | This attribute helps you set the amount of empty space that you want to put on the left side of your logo image. Nothing is rendered in this space. |
| logoTopMargin | Number | In Pixels | This attribute helps you set the amount of empty space that you want to put on top of your logo image. Nothing is rendered in this space. |
| logoPosition | Text | TL TR BL BR CC | Where to position the logo on the chart: TL – Top-left TR – Top-right BR – Bottom right BL – Bottom left CC – Center of screen |
| logoAlpha | Number | 0 – 100 | Once the logo has loaded on the chart, you can configure its opacity using this attribute. |
| logoScale | Number | 0-300 | You can also change the scale of an externally loaded logo at run-time by specifying a value for this parameter. |
| logoLink | Text | URL | If you want to link the logo to an external URL, specify the link in this attribute. The link can be in Exago BI Link format, allowing you to link to new windows, pop-ups, frames etc. |

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

## Divisional Lines, Grids & Zero Plane

Using this set of attributes, you can control the properties of divisional lines, zero plane and alternate color bands. Divisional Lines are horizontal or vertical lines running through the canvas. Each divisional line signifies a smaller unit of the entire axis thus aiding the users in interpreting the chart. The zero plane is a plane that signifies the 0 position on the chart. If there are no negative numbers on the chart, you won’t see a visible zero plane. Alternate color bands are colored blocks between two successive divisional lines.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| numDivLines | Number | Numeric value > 0 | Number of horizontal axis division lines that you want on the chart. |
| divLineEffect | Text | EMBOSS or BEVEL or NONE | This attribute enables you to apply an effect, for example, EMBOSS, or BEVEL to the divisional lines as well as to the trendlines. |
| divLineColor | Color | Hex Color Code | Color for divisional lines. |
| divLineThickness | Number | 1-5 | Thickness of divisional lines. |
| divLineAlpha | Number | 0 – 100 | Alpha of divisional lines. |
| divLineDashed | True/False | 0/1 | Whether the divisional lines should be rendered as dashed lines. Default value: 0 (divisional lines rendered using straight lines) |
| divLineDashLen | Number | In pixels | Sets the length of each dash when divisional lines are rendered as dashed lines. |
| divLineDashGap | Number | In pixels | Sets the gap between two consecutive dashes when divisional lines are rendered as dashed lines. |
| zeroPlaneMesh | True/False | 0/1 | Whether to draw the zero plane as a wire frame mesh or as a filled plane. If set to 1, a mesh on the zero plane of the chart will be drawn. |
| zeroPlaneColor | Color | Hex Color Code | Color of the Zero Plane. |
| zeroPlaneThickness | Number | In Pixels | Thickness of zero plane. |
| zeroPlaneAlpha | Number | 0 – 100 | Alpha of zero plane. |
| showZeroPlaneValue | True/False | 0/1 | Allows you to show or hide the value on which the zero plane exists on the y-axis. By default, the value is displayed. |
| showAlternateHGridColor | True/False | 0/1 | Whether to show alternate colored horizontal grid bands. |
| alternateHGridColor | Color | Hex Color Code | Color of the alternate horizontal grid bands. |

## Anchor Properties

In line and area charts, anchors (or marker points) are polygons which appear at the joint of two consecutive line/area points. These are indicators to show the position of data points. The anchors handle tool tips and links for the data points. So, if you opt to not render anchors on a chart, the tool tips and links won’t function. You can, however, hide them by setting alpha to 0 and still enable tool tips and links. In area charts, anchors are set transparent by default. In case you wish to show the anchor, use anchorAlpha=”100″ attribute. You can customize all the facets of anchors using the properties below.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| drawAnchors | True/False | 0/1 | Whether to draw anchors on the chart. |
| anchorSides | Number | Any | This attribute sets the number of sides the anchor will have. For for example, an anchor with 3 sides will represent a triangle, with 4 it will be a square and so on. |
| anchorStartAngle | Number | 0 – 360 | This attribute sets the starting angle of anchors. Default value: 90 |
| anchorRadius | Number | In pixels | This attribute sets the radius (in pixels) of the anchor. |
| anchorColor | Color | Hex Color Code | Lets you set the color of anchors. |
| anchorBorderColor | Color | Hex Color Code | Lets you set the border color of anchors. |
| anchorBorderThickness | Number | In Pixels | Helps you set border thickness of anchors. |
| anchorBgColor | Color | Hex Color Code | Helps you set the background color of anchors. |
| anchorAlpha | Number | 0 – 100 | Helps you set the alpha of entire anchors. If you need to hide the anchors on chart but still enable tool tips, set this as 0. |
| anchorBgAlpha | Number | 0 – 100 | Helps you set the alpha of anchor background. |
| anchorImageUrl | Exago BI link format | URL | If you want to use an external image (JPG/PNG) as an anchor, this attribute lets you specify the URL. **Note:** Due to cross domain security restrictions it is advised to use an image from the same domain name as your charts. |
| anchorImageAlpha | Number | 0 – 100 | This attribute allows to set a transparency for images displayed as anchors in charts. Default value: 100 |
| anchorImageScale | Number | 0 – 100 | This attribute allows to set a scale for magnifying images displayed as anchors. Default value: 100 |
| anchorImagePadding | Number | In Pixels | This attribute sets the padding between the anchor image and the border of the anchor. For the anchor image, instead of decreasing the size of the image this attribute crops the image. Default value: 1 |

## Legend Properties

In combination charts, the series name of each data set shows up in the legend of the chart. If you do not need the legend, you can opt to hide the same. Also, the legend can be placed at the bottom of the chart or to the right of the chart. Using the attributes below, you can configure the functional and cosmetic properties of the legend.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showLegend | True/False | 0/1 | Whether to show legend for the chart. |
| legendItemFontBold | True/False | 0/1 | Whether legend keys should be displayed in bold |
| legendItemFont | Text | Font Name | Sets legend item font |
| legendItemFontSize | Number | 6 – 72 | Sets legend item font size |
| legendItemFontColor | Color | Hex Color Code | Sets legend item font color |
| legendItemHoverFontColor | Color | Hex Color Code | Sets legend item font color on hover |
| interactiveLegend | True/False | 0/1 | Whether |
| legendCaptionAlignment | Text | “left”, “center”, “right” | Sets the legend caption horizontal alignment . |
| legendCaptionFontBold | True/False | 0/1 | Whether legend caption should be displayed in bold |
| legendCaptionFont | Text | Font Name | Sets legend caption font |
| legendCaptionFontSize | Number | 6 – 72 | Sets legend caption font size |
| legendCaptionFontColor | Color | Hex Color Code | Sets legend caption font color |
| legendPosition | Text | bottom, right, top, top-left, top-right, bottom-left, bottom-right, left, left-top, left-bottom, right, right-top, right-bottom, and absolute | The legend can be plotted at different positions with respect to the chart. Note that if the value of `legendPosition` is set to `absolute`, you also need to set the coordinates of the legend. You can do that using the attributes `legendXPosition` and `legendYPosition`, both of which accept absolute or percentage values. |
| legendXPosition | Number | 0 to chart width (in pixels) | When the value of `legendPosition` is set to `absolute`, use this attribute to set the X-coordinate of the legend. It accepts absolute or percentage values. By default, its value is set to `0`. |
| legendYPosition | Number | 0 to chart height (in pixels) | When the value of `legendPosition` is set to `absolute`, use this attribute to set the Y-coordinate of the legend. It accepts absolute or percentage values. By default, its value is set to `0`. |
| legendNumRows | Number | Any | Sets the number of rows the legend should display. |
| legendNumColumns | Number | Any | Sets the number of columns the legend should display. |
| reverseLegend | True/False | 0/1 | You can reverse the ordering of data sets in the legend by setting this attribute to 1. |
| legendItemHiddenColor | Color | Hex Color Code | Sets the color that applies on both text font and icon when they are in a disabled / hidden state |
| legendCaption | Text |  | You can add a caption for the entire legend by setting the same here. |
| legendIconScale | Number | 1-5 | Scaling of legend icon is possible in Exago BI. This attribute lets you control the size of legend icon. |
| legendBgColor | Color | Hex Color Code | Background color for the legend. |
| legendBgAlpha | Number | 0 – 100 | Background alpha for the legend. |
| legendBorderColor | Color | Hex Color Code | Border Color for the legend. |
| legendBorderThickness | Number | In Pixels | Border thickness for the legend. |
| legendBorderAlpha | Number | 0 – 100 | Border alpha for the legend. |
| legendShadow | True/False | 0/1 | Whether to show a shadow for legend. |
| legendAllowDrag | True/False | 0/1 | The legend can be made drag-able by setting this attribute to 1. End viewers of the chart can drag the legend around on the chart. |
| legendScrollBgColor | Color | Hex Color Code | If you’ve too many items on the legend, a scroll bar shows up on the same. This attribute lets you configure the background color of the scroll bar. |
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
| formatNumberScale | True/False | 0/1 | Configuration whether to add K (thousands) and M (millions) to a number after truncating and rounding it – for example, if `formatNumberScale` is set to 1, 1043 will become 1.04K (with decimals set to 2 places). Same with numbers in millions – an M will be added at the end. |
| defaultNumberScale | Text | Any | The default unit of the numbers that you’re providing to the chart. |
| numberScaleUnit | Text | Any | Unit of each block of the scale. |
| numberScaleValue | Text | Any | Range of the various blocks that constitute the scale. |
| forceNumberScale | True/False | 0/1 | If a data value is less than the lowest given number is the number scale, this attribute forces the lower value of the `numberScaleUnit` to be applied to that data value. This attribute works only when `“formatNumberScale”: “1”` and the `defaultNumberScale` attribute is not defined. For example, if `“numberScaleUnit”: “K, M”`, `“numberScaleValue”: “1000, 1000”`, and `“forceNumberScale”: “1”`, a data value of `400` will be rendered as `0.40K`. |
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
| seriesNameInToolTip | True/False | 0/1 | For combination charts, Exago BI shows the following information in tool tip (unless tool text is explicitly defined): “Series Name, Category Name, Data Value”. This attribute lets you control whether series name will show up in tool tip or not. |
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
| plotHoverEffect | True/False | 0/1 | Whether to enable hover effect on charts for data plots (for example, column, pie) only |
| plotFillHoverColor | Color | Hex Color Code | Specifies the hover color for the data plots |
| plotFillHoverAlpha | Number | 1 – 100 | Specifies the hover alpha for data plots |
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
| columnHoverColor | Color | Hex Color Code | This attribute specifies the hover color for the columns. |
| columnHoverAlpha | Number | 0 – 100 | This attribute specifies the transparency of the column when you hover. |
| anchorHoverDip | Number | 0 – 1 | This attribute adds a dip effect (different shapes) to the anchors on hover. When hovered a star shaped anchor is created. Using `anchorSides` attribute, you can specify the no. of sides for anchors. `Note : If the anchors are of circular shape, this attribute won’t be applied on it.` |
| anchorHoverAnimation | True/False | 0/1 | Anchors get animated when the normal radius and the hover radius are different. To disable this effect you can set anchorHoverAnimation = `0`. Default value: `1` |

## Chart Padding & Margins

The following attributes help you control chart margins and padding. Exago BI allows you manually customize the padding of various elements on the chart to allow advanced manipulation and control over chart visualization. Padding in Exago BI is always defined in pixels, unless the attribute itself suggests some other scale (like `plotSpacePercent`, which configures the spacing using percentage values). You can also define the chart margins. Chart Margins refer to the empty space left on the top, bottom, left and right of the chart. That means, Exago BI will not plot anything in that space. It’s not necessary for you to specify any padding/margin values. Exago BI automatically assumes the best values for the same, if you do not specify the same.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| captionPadding | Number | In Pixels | This attribute lets you control the space (in pixels) between the sub-caption and top of the chart canvas. If the sub-caption is not defined, it controls the space between caption and top of chart canvas. If neither caption, nor sub-caption is defined, this padding does not come into play. |
| xAxisNamePadding | Number | In Pixels | Using this, you can set the distance between the top end of x-axis title and the bottom end of data labels (or canvas, if data labels are not to be shown). |
| yAxisNamePadding | Number | In Pixels | Using this, you can set the distance between the right end of y-axis title and the start of y-axis values (or canvas, if the y-axis values are not to be shown). |
| yAxisValuesPadding | Number | In Pixels | This attribute helps you set the horizontal space between the canvas left edge and the y-axis values or trend line values (on left/right side). This is particularly useful, when you want more space between your canvas and y-axis values. |
| labelPadding | Number | In Pixels | This attribute sets the vertical space between the labels and canvas bottom edge. If you want more space between the canvas and the x-axis labels, you can use this attribute to control it. |
| yLabelGap | Number | In Pixels | This attribute helps you set the horizontal space between the canvas wall edge and the y-axis values or trend line values (on left/right side). This is particularly useful, when you want more space between your canvas and y-axis values. |
| xLabelGap | Number | In Pixels | This attribute sets the vertical space between the labels and canvas wall edge. If you want more space between the canvas and the x-axis labels, you can use this attribute to control it. |
| valuePadding | Number | In Pixels | It sets the vertical space between the end of columns and start of value textboxes. This basically helps you control the space you want between your columns/anchors and the value textboxes. |
| plotSpacePercent | Number | 0-80 (In Percent) | On a column chart, there is spacing defined between two columns. By default, the spacing is set to 20% of canvas width. If you intend to increase or decrease the spacing between columns, you can do so using this attribute. For example, if you wanted all columns to stick to each other without any space in between, you can set `plotSpacePercent` to 0. Similarly, if you want very thin columns, you can set `plotSpacePercent` to its max value of 80. |
| plotPaddingPercent | Number | 0 – 100 | This attribute adds white space between columns/bars representing a single category. Applicable only when there are more than one data sets. |
| chartLeftMargin | Number | In Pixels | Amount of empty space that you want to put on the left side of your chart. Nothing is rendered in this space. |
| chartRightMargin | Number | In Pixels | Amount of empty space that you want to put on the right side of your chart. Nothing is rendered in this space. |
| chartTopMargin | Number | In Pixels | Amount of empty space that you want to put on the top of your chart. Nothing is rendered in this space. |
| chartBottomMargin | Number | In Pixels | Amount of empty space that you want to put at the bottom of your chart. Nothing is rendered in this space. |
| legendPadding | Number | In Pixels | Padding of legend from right/bottom side of canvas |
| canvasPadding | Number | In Pixels | Allows you to set empty space on the left and right side of Line data set or Area data set on the chart canvas. This setting won’t work if one or more Column data sets are present. |
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

## The category Object

The attributes of the `category` object are used to define and customize individual x-axis labels for multi-series charts.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| label | Text | Any | This attribute determines the label for the data item. The label appears on the x-axis of chart. **Note:** The `label` attribute replaces the `name` attribute. Previously, either one of the attributes could be used to set the label. Support for the `name` attribute has been discontinued since v3.10.0. |
| showLabel | True/False | 0/1 | You can individually opt to show/hide labels of individual data items using this attribute. |
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
| renderAs | Text | COLUMN, AREA or LINE | This attribute defines what the particular data set will be plotted as. Valid values are COLUMN, AREA or LINE. |
| seriesName | Text | Any | Lets you specify the series name for a particular data set. For example, if you’re plotting a chart to indicate monthly sales analysis for 2005 and 2006, the `seriesName` for the first data set will be 2005 and that of the second will be 2006. The `seriesName` of a data set is shown in legend. |
| showPlotBorder | True/False | 0/1 | Whether to show the border of this data set (area or column only). |
| plotBorderColor | Color | Hex Color Code | Color for data plot border of this data set (area or column only) |
| plotBorderThickness | Number | 0-5 | Thickness for data plot border of this data set (area or column only) |
| plotBorderAlpha | Number | 0 – 100 | Alpha for data plot border of this data set (area or column only) |
| color | Color | Hex Color Code | This attribute sets the color using which columns, lines, area of that data set will be drawn |
| alpha | Text | 0 – 100 or Comma Separated List | This attribute sets the alpha (transparency) of the entire data set. |
| showValues | True/False | 0/1 | Whether to show the values for this data set. |
| valueFontColor | Color | Hex Color Code | Specifies the font color of data values for a particular data set. |
| valueBgColor | Color | Hex Color Code | Sets the background color of value text for a particular data set. |
| valueBorderColor | Color | Hex Color Code | Sets the border color around the value text for a particular data set. |
| valuePosition | Text | “ABOVE”, “BELOW”, “AUTO” | This attribute lets you adjust the vertical alignment of data values for all dataplots in the data set. The alignment is set with respect to the position of the dataplots on the chart. By default, the attribute is set to AUTO mode in which the alignment of each data value is determined automatically based on the position of each plot point. In ABOVE mode, data values are displayed above the plot points unless a plot point is too close to the upper edge of the canvas. While in BELOW mode, data values are displayed below the plot points unless a plot point is too close to the lower edge of the canvas. The attribute will function only if `showValue` attribute is set to 1 in this particular data set. |
| dashed | True/False | 0/1 | Whether this data set will appear as dashed. |
| includeInLegend | True/False | 0/1 | Whether to include the seriesName of this data set in legend. In combination charts, this can be particularly useful when you’ve used the area/line chart to plot a trend but do not want the seriesName of that trend to appear in legend. |
| drawAnchors | True/False | 0/1 | Whether to draw anchors for a particular data set. |
| anchorSides | Number | 3-20 | Sets the number of sides that the anchors of the particular data set will have. For for example, an anchor with 3 sides will represent a triangle, with 4 it will be a square and so on. |
| anchorStartAngle | Number | 0 – 360 | This attribute sets the starting angle for anchors of particular data set. Default value: 90 |
| anchorRadius | Number | In Pixels | This attribute sets the radius (in pixels) of the anchors of the particular data set. |
| anchorBorderColor | Color | Hex Color Code | Lets you set the border color of anchors of the particular data set. |
| anchorBorderThickness | Number | In Pixels | Helps you set border thickness of anchors of the particular data set. |
| anchorBgColor | Color | Hex Color Code | Helps you set the background color of anchors of the particular data set. |
| anchorAlpha | Number | 0 – 100 | Helps you set the alpha of entire anchors of the particular data set. If you need to hide the anchors for the data set but still enable tool tips, set this as 0. |
| lineThickness | Number | In Pixels | Thickness of the lines for the particular data set. |
| lineDashLen | Number | In pixels | Sets the length of each dash when lines for a data-set is rendered as dashed lines. |
| lineDashGap | Number | In pixels | Sets the gap between consecutive dashes when lines for a data-set is rendered as dashed lines. |
| visible | True/False | 0/1 | Sets whether a data set will be visible on the chart, when the chart is first loaded. This attribute overrides the `initiallyHidden` attribute. `Default Value` : 1 |
| anchorHoverSides | Number | In Pixels | This attribute sets the number of sides for anchors of a particular data set when hovered. |
| anchorBgHoverColor | Color | Hex color code | This attribute sets the background color for anchors of a particular data set when hovered. |
| anchorBgHoverAlpha | Number | 0 – 100 | This attribute sets the transparency for anchor’s background of a particular data set when hovered. |
| anchorBorderHoverColor | Color | Hex color code | Sets the border color for anchors of a particular data set when hovered. |
| anchorBorderHoverAlpha | Number | 0 – 100 | Sets the border’s transparency for anchors of a particular data set when hovered. |
| anchorBorderHoverThickness | Number | In pixels | This attribute sets the border thickness for anchors of a particular data set when hovered. |
| anchorHoverStartAngle | Number | In pixels | This attribute sets the starting angle for anchors of a particular data set when hovered. |
| anchorHoverDip | Number | 0 – 1 | This attribute adds a dip effect (different shapes) for anchors of a particular data set on hover. When hovered a star shaped anchor is created. Using `anchorSides` attribute, you can specify the no. of sides for anchors. `Note : If the anchors are of circular shape, this attribute won’t be applied on it.` |

## The data Object

Attributes of the `data` object, child of the `dataset` object, are used to define the values to be plotted for individual data series. The `dataset` and `data` objects defined for one data series are shown in the example below:

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
| value | Number | Any | Numerical value for the data item. This value will be plotted on the chart. |
| displayValue | Text |  | If instead of the numerical value of this data, you wish to display a custom string value, you can specify the same here. Examples are annotation for a data item etc. |
| color | Color | Hex Color Code | For combination charts, you can define the color of data sets at data set level. However, if you wish to highlight a particular data element, you can specify its color at “set” level using this attribute. **Note:** This attribute is not applicable on spline data plots. |
| link | Text | Any | You can define links for individual data items. That enables the end user to click on data items (columns, lines, bars etc.) and drill down to other pages. To define the link for data items, use the link attribute. You can define links that open in same window, new window, pop-up window or frames. Please see “Drill-Down > Using JavaScript Functions as Links” for more information. Also, you’ll need to Url Encode all the special characters (like ? and &) present in the link. |
| showValue | True/False | 0/1 | You can individually opt to show/hide values of individual data items using this attribute. This value over-rides the data set level value. |
| valueFontColor | Color | Hex Color Code | Specifies the font color of a data value for an individual data plot. |
| valueBgColor | Color | Hex Color Code | Sets the background color of a value text for an individual data plot. |
| valueBorderColor | Color | Hex Color Code | Sets the border color around the value text for an individual data plot. |
| valuePosition | Text | “ABOVE”, “BELOW”, “AUTO” | If you’ve opted to show a particular data value on the chart, this attribute lets you adjust the vertical alignment of individual data values with respect to dataplots. By default, this attribute is set to AUTO mode in which the alignment of a data value is determined automatically based on the position of its plot point. In ABOVE mode, a data value is displayed above the plot point unless a plot point is too close to the upper edge of the canvas while in BELOW mode, a data value is displayed below the plot point unless a plot point is too close to the lower edge of the canvas. |
| dashed | True/False | 0/1 | Whether the border of this data item should appear as dashed. This is particularly useful when you want to highlight a data (such as forecast or trend etc.). This value over-rides the data set level value. |
| alpha | Number | 0 – 100 | For combination charts, you can define the alpha of data sets at data set level. However, if you wish to highlight a particular data element, you can specify its alpha at “set” level using this attribute. |
| toolText | Text | Any | By default, Exago BI shows the series name, category name, and value as tool tip text for that data item. But, if you want to display more information for the data item as tool tip, you can use this attribute to specify the same. |
| anchorSides | Number | 3-20 | Lets you specify “set” specific sides of the anchor. |
| anchorStartAngle | Number | 0 – 360 | This attribute sets the starting angle for an anchor of a particular data. Default value: 90 |
| anchorRadius | Number | In Pixels | Lets you specify “set” specific radius (in pixels) of the anchor. |
| anchorBorderColor | Color | Hex Color Code | Lets you specify “set” specific border color of the anchor. |
| anchorBorderThickness | Number | In Pixels | Lets you specify “set” specific border thickness of the anchor. |
| anchorBgColor | Color | Hex Color Code | Lets you specify “set” specific background color of the anchor. |
| anchorAlpha | Number | 0 – 100 | Lets you specify “set” specific alpha of the anchor. |
| anchorBgAlpha | Number | 0 – 100 | Lets you specify “set” specific alpha of the anchor background. |

## Trend-lines

Trend-lines are horizontal lines that aid in interpretation of data with respect to some pre-determined value. For example, if you are plotting the sales data for the current year, you might want to show the previous year’s average monthly sales as a trend indicator for ease of comparison. The `lines` object, child of the `trendlines` object is used to add trend-lines to a chart. Although the `line` object has to be defined within the `trendlines` object, the latter cannot be used to collectively customize trend-lines, because it does not have any attributes of its own. The attributes of the `lines` object, child of the `trendlines` object, are used to create and customize trend-lines for charts.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| startValue | Number | Numeric Value | The starting value for the trendline. Say, if you want to plot a slanted trendline from value 102 to 109, the `startValue` will be 102. |
| endValue | Number | Numeric Value | The ending y-axis value for the trendline. Say, if you want to plot a slanted trendline from value 102 to 109, the `endValue` will be 109. If you do not specify a value for `endValue`, it will automatically assume the same value as `startValue`. |
| displayValue | Text | Any | If you want to display a string caption for the trend line by its side, you can use this attribute. Example: `displayValue=’Last Month High’`. When you don’t supply this attribute, it automatically takes the value of `startValue`. |
| color | Text | Hex Color Code | Color of the trend line and its associated text |
| isTrendZone | True/False | 0/1 | Whether the trend will be displayed as a line or a zone (fill-colored rectangle). |
| thickness | Number | In Pixels | If you’ve opted to show the trend as a line, this attribute lets you define the thickness of trend line. |
| alpha | Number | 0 – 100 | Alpha of the trend line. |
| dashed | True/False | 0/1 | Whether the trendline should be rendered as dashed lines. Default value: 0 (trendline rendered using straight lines) |
| dashLen | Number | In pixels | Sets the width of each dash when trendline is rendered as dashed lines. |
| dashGap | Number | In pixels | Sets the gap between consecutive dashes when trendline is rendered as dashed lines. |
| valueOnRight | True/False | 0/1 | Whether to show the trendline value on left side or right side of chart. This is particularly useful when the trend line display values on the chart are colliding with divisional lines values on the chart. |
| toolText | Text |  | Custom tool-text for this trendline/zone. |

## Trend-lines (Chart level attributes)

Trend-lines are horizontal lines that aid in interpretation of data with respect to some pre-determined value. For example, if you are plotting the sales data for the current year, you might want to show the previous year’s average monthly sales as a trend indicator for ease of comparison. Cosmetics for all the trend-lines rendered can be attained using this set of attributes. Although there are set of attributes of the `line object`, used to create and customize trend-lines, these set of attributes effect all the trend-lines rendered in your chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| trendlineColor | Color | Hex Color Code | Sets color of all the trend lines and its associated text in the chart. |
| trendlineThickness | Number | In Pixels | If you’ve opted to show the trend as a line, this attribute lets you define the thickness of all the trend lines in your chart. |
| trendlineAlpha | Number | 0 – 100 | Sets transparency for all the trend lines in your charts. |
| trendLineToolText | Text | Any | Sets the tooltip text of the trend-line. It accepts macros, plain text, and HTML tags, as string. |

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
