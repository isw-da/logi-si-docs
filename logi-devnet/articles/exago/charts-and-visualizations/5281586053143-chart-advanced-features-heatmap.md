---
title: "Chart Advanced Features: Heatmap"
id: 5281586053143
section: "Charts and Visualizations"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281586053143-Chart-Advanced-Features-Heatmap
updated_at: 2022-05-03T22:08:26Z
---

# Chart Advanced Features: Heatmap

# Chart Advanced Features: Heatmap

The following sections provide a list of available advanced attributes available for controlling and customizing **Heatmap** elements.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic contains documentation for advanced attributes which are third-party customizations that must be manually entered into the chart wizard. These topics were converted directly from the documentation provided by this third-party source. Not every attribute listed may be supported in Exago BI as some unexpected conflicts may occur in their integration within the application.

## Functional Attributes

These attributes let you control a variety of functional elements on the chart. For example, you can opt to show or hide data labels, data values. You can also set chart limits and extended properties.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| animation | True/False | 0/1 | This attribute gives you the option to control animation in your charts. If you do not want to animate any part of the chart, set this as 0. |
| animationDuration | Number | In seconds | This attribute sets the animation duration of the chart. `animationDuration` attribute is applicable only if animation of the chart is enabled. Default value: 1 sec |
| palette | Number | 1-5 | Each chart has 5 pre-defined color palettes which you can choose from. Each palette renders the chart in a different color theme. |
| paletteColors | Text | List of hex color codes separated by comma | While the `palette` attribute allows to select a palette theme that applies to chart background, canvas, font and tool-tips, it does not change the colors of data items (that is, column, line, pie etc.). Using `paletteColors` attribute, you can specify your custom list of hex colors for the data items. The list of colors have to be separated by comma, for example, `”paletteColors”: “#FF0000, #0372AB, #FF5904…”`. The chart will cycle through the list of specified colors and then render the data plot accordingly. To use the same set of colors throughout all your charts in a web application, you can store the list of palette colors in your application globally and then provide the same in each chart JSON. |
| useEllipsesWhenOverflow | True/False | 0/1 | When enabled in auto mode, long data labels are truncated by adding ellipses to prevent them from overflowing the chart background. The default value is 1. |
| trType | Text |  | Specifies the type of data provided in the top-right label. This value is displayed in the tool tip. |
| tlType | Text |  | Specifies the type of data provided in the top-left label. This value is displayed in the tool tip. |
| brType | Text |  | Specifies the type of data provided in the bottom-right label. This value is displayed in the tool tip. |
| blType | Text |  | Specifies the type of data provided in the bottom-left label. This value is displayed in the tool tip. |
| staggerLines | Number | 2 or above | If you have opted for STAGGER mode as `labelDisplay`, using this attribute you can control how many lines to stagger the label to. By default, all labels are displayed in a single line. |
| showValues | True/False | 0/1 | Sets the configuration whether data values would be displayed along with the data plot on chart. |
| showLimits | True/False | 0/1 | Whether to show chart limit values. |
| showDivLineValues | True/False | 0/1 | Whether to show div line values. |
| showShadow | True/False | 0/1 | Whether to apply the shadow effects for dataplot. |
| clickURL | Text | Any | The entire chart can now act as a hotspot. Use this Url to define the hotspot link for the chart. The link can be specified in Exago BI Link Format. |
| clickURLOverridesPlotLinks | True/False | 0/1 | Sets whether the `clickURL` attribute (that sets a link to which the user is directed when the chart is clicked) overrides the `link` attribute (that sets a link to which the user is directed when a data plot is clicked). Default value: 0 (`clickURL` does not override `link`) |
| interactiveAnimationDuration | Number | Any | Sets the duration of the animation that takes place when the legends are used to show or hide dataplots. |
| mapByCategory | True/False | 0/1 | Allows you to render a category based heat map chart. |
| plotFillAlpha | Numeric | 0 – 100 | Sets the transparency of all the dataplots in the chart. |
| unescapeLinks | True/False | 0/1 | Internally the chart decodes a Url that you set as link. Before invoking the link it again encodes the Url. If you are passing multilingual characters via a Url or do not want this decode-encode mechanism to be handled by chart you can set,`unescapeLinks=’0’`. |
| showPrintMenuItem | True/False | 0/1 | When you right click on the chart it shows a context menu. This attribute allows you to show or hide the “Print” option in the context menu. |
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
| xAxisPosition | Text | Top, Bottom | This attribute sets the position of the x-axis in the chart. Default value: Bottom |
| yAxisPosition | Text | Left, Right | This attribute sets the position of the y-axis in the chart. Default value: Left |
| showXaxisLabels | True/False | 0/1 | This attribute is used to show or hide the x axis or the column labels. |
| rotatexAxisLabels | True/False | 0/1 | This attribute lets you set whether the data labels would show up as rotated labels on the chart. |
| showYaxisLabels | True/False | 0/1 | This attribute is used to show or hide y axis or the row labels. |
| rotateYAxisName | True/False | 0/1 | If you do not wish to rotate y-axis name, set this as 0. It specifically comes to use when you have special characters (UTF8) in your y-axis name that do not show up in rotated mode. |
| yAxisNameWidth | Number | (In Pixels) | If you opt to not rotate y-axis name, you can choose a maximum width that will be applied to y-axis name. |

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
| showBorder | True/False | 0/1 | Whether to show a border around the chart or not. |
| borderColor | Color | Hex Color Code | Border color of the chart. |
| borderThickness | Number | In Pixels | Border thickness of the chart. |
| borderAlpha | Number | 0 – 100 | Border alpha of the chart. |
| bgColor | Color | Hex Color Code | This attribute sets the background color for the chart. You can set any hex color code as the value of this attribute. To specify a gradient as background color, separate the hex color codes of each color in the gradient using comma. Example: `#FF5904, #FFFFFF`. |
| bgAlpha | Number | 0 – 100 | Sets the alpha (transparency) for the background. If you have opted for gradient background, you need to set a list of alpha(s) separated by comma. |
| bgRatio | Number | 0 – 100 | If you have opted for a gradient background, this attribute lets you set the ratio of each color constituent. |
| bgAngle | Number | 0-360 | Angle of the background color, in case of a gradient. |
| bgImage | Text | Any | To place any image (JPG/PNG/GIF) as background of the chart, enter the (path and) name of the background image as a URL without quotes around it. It should be in the same domain as the chart. |
| bgImageAlpha | Number | 0 – 100 | This attribute specifies the opacity for the loaded background image. |
| bgImageDisplayMode | Text | stretch, tile, fit, fill, center, none | Helps you specify the mode in which the background image is to be displayed. Stretch – expands the image to fit the entire chart area, without maintaining original image constraints. Tile – the image is repeated as a pattern on the entire chart area. Fit – fits the image proportionately on the chart area. Fill -proportionately fills the entire chart area with the image. Center – the image is positioned at the center of the chart area. None – Default mode. |
| bgImageValign | Text | left, center, right | Helps you to vertically align the background image. |
| bgImageHalign | Text | left, center, right | Helps you to horizontally align the background image. |
| bgImageScale | Number | 0-300 | Helps you magnify the background image.This attribute will only work when the attribute `bgImageDisplayMode` is set to none, center, or tile. |
| canvasBgColor | Color | Hex Color Code | This attribute sets the background color for the chart canvas. You can set any hex color code as the value of this attribute. To specify a gradient as canvas background color, separate the hex color codes of each color in the gradient using comma. Example: #FF5904, #FFFFFF. |
| canvasBgAlpha | Number | 0 – 100 | This attribute sets the background transparency for the chart canvas. For gradient, separate the alpha value using comma. Example: 15, 50. |
| canvasBgRatio | Numbers separated by comma | 0 – 100 | When a gradient is used to set the color of the canvas background, this attribute sets the ratio of the colors. Example : If the value of the `canvasBgColor` attribute is set as `#FF5904, #FFFFFF`, `canvasBgRatio` can be used to specify their ratio in the background. |
| canvasBgAngle | Number | 0-360 | Helps you specify canvas background angle in case of gradient. |
| canvasBorderColor | Color | Hex Color Code | Lets you specify canvas border color. |
| canvasBorderThickness | Number | 0-5 | Lets you specify canvas border thickness. |
| canvasBorderAlpha | Number | 0 – 100 | Lets you control transparency of canvas border. |
| showVLineLabelBorder | True/False | 0/1 | If you have opted to show a label for any of your vLines in the chart, you can collectively configure whether to show border for all such labels using this attribute. If you want to show label border for just a particular vLine, you can over-ride this value by specifying border configuration for that specific vLine. |
| rotateVLineLabels | True/False | 0/1 | This attribute lets you set whether the vline labels will show up as rotated labels on the chart. Default value: 0 |
| logoURL | Text | Url | You can load an external logo (JPEG/PNG) to your chart, this attribute lets you specify the URL. Due to cross domain security restrictions it is advised to use a logo from the same domain name as your charts. |
| logoLeftMargin | Number | In Pixels | This attribute helps you set the amount of empty space that you want to put on the left side of your logo image. Nothing is rendered in this space. |
| logoTopMargin | Number | In Pixels | This attribute helps you set the amount of empty space that you want to put on top of your logo image. Nothing is rendered in this space. |
| logoPosition | Text | TL, TR, BL, BR, CC | Where to position the logo on the chart: TL – Top-left TR – Top-right BR – Bottom right BL – Bottom left CC – Center of screen |
| logoAlpha | Number | 0 – 100 | Once the logo has loaded on the chart, you can configure its opacity using this attribute. |
| logoScale | Number | 0-300 | You can also change the scale of an externally loaded logo at run-time by specifying a value for this parameter. |
| logoLink | Text | Url | If you want to link the logo to an external URL, specify the link in this attribute. The link can be in Exago BI Link Format, allowing you to link to new windows, pop-ups, frames etc. |

## Data Plot Cosmetics

These attributes let you configure how your plot (columns, lines, area, pie or any data that you’re plotting) would appear on the chart. If the plots can show borders, you can control the border properties using the attributes listed below. Or, if they support gradient fills, you can again configure various properties of the gradient using these attributes. Various other controls over plot cosmetics can be attained using this set of attributes.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showPlotBorder | True/False | 0/1 | Whether the column, area, pie etc. border would show up. |
| plotBorderColor | Color | Hex Color Code | Color for column, area, pie border. |
| plotBorderThickness | Number | 0-5 | Thickness for column, area, pie border. |
| plotBorderAlpha | Number | 0 – 100 | Alpha for column, area, pie border. |
| plotBorderDashed | True/False | 0/1 | Whether the border around the data plots should be rendered using dashed lines. Default value: 0 (border rendered using straight lines) |
| plotBorderDashLen | Number | In pixels | Sets the length of each dash when the border around the data plots are rendered using dashed lines. |
| plotBorderDashGap | Number | In pixels | Sets the gap between two consecutive dashes when the border around the data plots are rendered using dashed lines. |
| plotFillAngle | Number | 0-360 | If you have opted to fill the plot (column, area etc.) as gradient, this attribute lets you set the fill angle for gradient. |
| plotFillRatio | Number | 0 – 100 | If you have opted to fill the plot (column, area etc.) as gradient, this attribute lets you set the ratio for gradient. |

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

## Chart Padding & Margins

The following attributes help you control chart margins and padding. Exago BI allows you manually customize the padding of various elements on the chart to allow advanced manipulation and control over chart visualization. Padding in Exago BI is always defined in pixels, unless the attribute itself suggests some other scale (like `plotSpacePercent`, which configures the spacing using percentage values). You can also define the chart margins. Chart Margins refer to the empty space left on the top, bottom, left and right of the chart. That means, Exago BI would not plot anything in that space. It is not necessary for you to specify any padding or margin values. Exago BI automatically assumes the best values for the same, if you do not specify the same.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| captionPadding | Number | In Pixels | This attribute lets you control the space (in pixels) between the sub-caption and top of the chart canvas. If the sub-caption is not defined, it controls the space between caption and top of chart canvas. If neither caption, nor sub-caption is defined, this padding does not come into play. |
| xAxisNamePadding | Number | In Pixels | Using this, you can set the distance between the top end of x-axis title and the bottom end of data labels (or canvas, if data labels are not to be shown). |
| yAxisNamePadding | Number | In Pixels | Using this, you can set the distance between the right end of y-axis title and the start of y-axis values (or canvas, if the y-axis values are not to be shown). |
| labelXPadding | Number | In Pixels | This attribute sets the vertical space between the x-axis labels and canvas bottom edge. |
| labelYPadding | Number | In Pixels | It sets the horizontal space between the y-axis labels and the canvas right edge. |
| chartLeftMargin | Number | In Pixels | Amount of empty space that you want to put on the left side of your chart. Nothing is rendered in this space. |
| chartRightMargin | Number | In Pixels | Amount of empty space that you want to put on the right side of your chart. Nothing is rendered in this space. |
| chartTopMargin | Number | In Pixels | Amount of empty space that you want to put on the top of your chart. Nothing is rendered in this space. |
| chartBottomMargin | Number | In Pixels | Amount of empty space that you want to put at the bottom of your chart. Nothing is rendered in this space. |
| legendPadding | Number | In Pixels | Padding of legend from right or bottom side of canvas |
| canvasLeftMargin | Number | In Pixels | This attribute lets you control the space between the start of chart canvas and the start (x) of chart. In case of 2D charts, the canvas is the visible rectangular box. Using this attribute, you can control the amount of empty space between the chart left side and canvas left side. By default, the chart automatically calculates this space depending on the elements to be placed on the chart. However, if you want to over-ride this value with a higher value, you can use this attribute to specify the same. Please note that you cannot specify a margin lower than what has been calculated by the chart. This attribute is particularly useful, when you have multiple charts placed in a page and want all their canvas start position to align with each other – so in such a case, you can set same margin value (a value large enough that it does not get rejected by chart owing to it being lower than the calculated value) for all such charts in the page. |
| canvasRightMargin | Number | In Pixels | Like `canvasLeftMargin`, this attribute lets you set the space between end of canvas and end of chart. |
| canvasTopMargin | Number | In Pixels | Like `canvasLeftMargin`, this attribute lets you set the space between top of canvas and top of chart. |
| canvasBottomMargin | Number | In Pixels | Like `canvasLeftMargin`, this attribute lets you set the space between bottom of canvas and bottom of chart. |

## Data Label Cosmetics

These attributes let you configure the cosmetics of all data labels of the chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showLabels | True/False | 0/1 | It sets the configuration whether the categorical axis labels will be displayed or not. |
| maxLabelHeight | Number | In Pixels | This attribute can be used to set the maximum height for the categorical axis labels (data labels) excluding the axis title. If any label goes beyond this height, the label will be truncated. In stagger mode, the number of stagger lines will be reduced if they exceed this value. |
| maxLabelWidthPercent | Numeric | In Pixels | Restricts the maximum space allotted for the y-axis data labels with respect to the chart’s width. If a data label is longer than the specified percentage width then it will either be wrapped or get truncated, subject to the availability of vertical space. Unnecessary space is not reserved for the labels. If all the labels are shorter than the specified maximum width, this value is not applied. |
| minLabelWidthPercent | Number | 1-100 | Restricts the minimum length of data labels in terms of percentage of the chart’s width that the data labels can occupy. The space thus calculated stays reserved even if the label width is less than the minimum width. |
| labelDisplay | Text | ‘AUTO’, ‘WRAP’, ‘STAGGER’, ‘ROTATE’, ‘NONE’ | Using this attribute, you can customize the alignment of data labels (categorical axis labels). There are 5 options: AUTO, WRAP, STAGGER, ROTATE or NONE. By default, this attribute is set to AUTO mode which means that the alignment of the data labels is determined automatically depending on the size of the chart. WRAP wraps the label text if it is too long to fit in one line. ROTATE rotates the labels vertically. STAGGER divides the labels into multiple lines. |
| labelFont | Text | Font Name | Sets the categorical axis label font family for the text. |
| labelFontColor | Color | Hex Color Code | Sets the categorical axis label font color. |
| labelFontSize | Number | 6 – 72 | Specifies the categorical axis label font size. |
| labelFontBold | True/False | 0/1 | Flag indicating whether categorical axis label font should be bold or not. |
| labelFontItalic | True/False | 0/1 | Flag indicating whether categorical axis label font should be italicized or not. |
| labelBgColor | Color | Hex Color Code | Sets the background color for categorical axis label text. |
| labelBorderColor | Color | Hex Color Code | Sets the color of the border around the categorical axis label text. |
| labelAlpha | Number | 0 – 100 | Sets the categorical axis label alpha for both font and background. |
| labelBgAlpha | Number | 0 – 100 | Sets the categorical axis label background alpha. |
| labelBorderAlpha | Number | 0 – 100 | Sets the categorical axis label border alpha. |
| labelBorderPadding | Number | In Pixels | Sets the categorical axis label border padding. |
| labelBorderRadius | Number | In Pixels | Sets the categorical axis label border radius. |
| labelBorderThickness | Number | In Pixels | Sets the categorical axis label border thickness. |
| labelBorderDashed | True/False | 0/1 | Whether the border around categorical axis labels should be rendered using dashed lines. Default value: 0 (border rendered using straight lines) |
| labelBorderDashLen | Number | In pixels | Sets the length of each dash when the border around the categorical axis labels are rendered using dashed lines. |
| labelBorderDashGap | Number | In pixels | Sets the gap between two consecutive dashes when the border around categorical axis labels are rendered using dashed lines. |
| labelLink | URL | Any | Sets a link for every data plot. |
| tlFont | Text | Font Name | Allows user to set Top Left font for the tooltext |
| tlFontSize | Number | 6 – 72 | Allows user to set Top Left font size for the tooltext |
| tlFontColor | Color | Hex color code | Allows user to set Top Left font color for the tooltext |
| trFont | Text | Font Name | Allows user to set Top Right font for the tooltext |
| trFontSize | Number | 6 – 72 | Allows user to set Top Right font size for the tooltext |
| trFontColor | Color | Hex color code | Allows user to set Top Right font color for the tooltext |
| blFont | Text | Font Name | Allows user to set Bottom Left font for the tooltext |
| blFontSize | Number | 6 – 72 | Allows user to set Bottom Left font size for the tooltext |
| blFontColor | Color | Hex color code | Allows user to set Bottom Left font color for the tooltext |
| brFont | Text | Font Name | Allows user to set Bottom Right font for the tooltext |
| brFontSize | Number | 6 – 72 | Allows user to set Bottom Right font size for the tooltext |
| brFontColor | Color | Hex color code | Allows user to set Bottom Right font color for the tooltext |

## Tool tip

These attributes let you control the tooltip. You can set the background color, border color, separator character and few other details.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showToolTip | True/False | 0/1 | Whether to show tool tip on chart. |
| toolTipBgColor | Color | Hex Color Code | Background color for tool tip. |
| toolTipColor | Color | Hex Color Code | Font color for the tool-tip. |
| toolTipBorderColor | Color | Hex Color Code | Border color for tool tip. |
| tooltipBorderAlpha | Number | 0 – 100 | Sets the border transparency for tool tip. |
| toolTipSepChar | Text | Any | The character specified as the value of this attribute separates the name and value displayed in tool tip. |
| plottooltext | Text | Any | Specify custom text for the tooltip You can either specify a constant string as the tooltip text or you can use variable values from the data level by prefixing a `$` to the attribute name, for example, `$name`, `$value`. |
| showToolTipShadow | True/False | 0/1 | Whether to show shadow for tool tips on the chart. |
| tooltipbgalpha | Number | 0 – 100 | Sets the transparency of the tooltip. |
| tooltipborderradius | Number | In Pixels | Sets the border radius of the tooltip. |
| tooltipborderthickness | Number | In Pixels | Sets the border thickness of the tooltip. |
| toolTipPadding | Number | In Pixels | This attribute sets the vertical space between the value and the border of the tooltip. If you want more space between the value and the border, you can use this attribute to control it. |

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

## Legend Properties

In multi-series charts, the series name of each data-set shows up in the legend of the chart. If you do not need the legend, you can opt to hide the same. Also, the legend can be placed at the bottom of the chart or to the right of the chart. Using the attributes below, you can configure the functional and cosmetic properties of the legend.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showLegend | True/False | 0/1 | Whether to show legend on the chart. |
| legendItemFontBold | True/False | 0/1 | Whether legend keys should be displayed in bold |
| legendItemFont | Text | Font Name | Sets legend item font |
| legendItemFontSize | Number | 6 – 72 | Sets legend item font size |
| legendItemFontColor | Color | Hex Color Code | Sets legend item font color |
| legendCaption | Text |  | You can add a caption for the entire legend by setting the same here. |
| legendItemHoverFontColor | Color | Hex Color Code | Sets legend item font color on hover |
| legendCaptionAlignment | Text | “left”, “center”, “right” | Sets the legend caption horizontal alignment . |
| legendCaptionFontBold | True/False | 0/1 | Whether legend caption should be displayed in bold |
| legendCaptionFont | Text | Font Name | Sets legend caption font |
| legendCaptionFontSize | Number | 6 – 72 | Sets legend caption font size |
| legendCaptionFontColor | Color | Hex Color Code | Sets legend caption font color |
| legendIconScale | Number | 1-5 | This attribute lets you control the size of legend icon. |
| legendItemHiddenColor | Color | Hex Color Code | Sets the color that applies on both text font and icon when they are in a disabled / hidden state |
| legendPosition | Text | bottom, right, top, top-left, top-right, bottom-left, bottom-right, left, left-top, left-bottom, right, right-top, right-bottom, and absolute | The legend can be plotted at different positions with respect to the chart. Note that if the value of `legendPosition` is set to `absolute`, you also need to set the coordinates of the legend. You can do that using the attributes `legendXPosition` and `legendYPosition`, both of which accept absolute or percentage values. |
| legendXPosition | Number | 0 to chart width (in pixels) | When the value of `legendPosition` is set to `absolute`, use this attribute to set the X-coordinate of the legend. It accepts absolute or percentage values. By default, its value is set to `0`. |
| legendYPosition | Number | 0 to chart height (in pixels) | When the value of `legendPosition` is set to `absolute`, use this attribute to set the Y-coordinate of the legend. It accepts absolute or percentage values. By default, its value is set to `0`. |
| legendNumRows | Number | Any | Sets the number of rows the legend should display. |
| legendNumColumns | Number | Any | Sets the number of columns the legend should display. |
| legendBgColor | Color | Hex Color Code | Background color for the legend. |
| legendBgAlpha | Number | 0 – 100 | Background alpha for the legend. |
| legendBorderColor | Color | Hex Color Code | Border Color for the legend. |
| legendBorderThickness | Number | In Pixels | Border thickness for the legend. |
| legendBorderAlpha | Number | 0 – 100 | Border alpha for the legend. |
| legendShadow | True/False | 0/1 | Whether to show a shadow for legend. |
| legendAllowDrag | True/False | 0/1 | The legend can be made drag-able by setting this attribute to 1. End viewers of the chart can drag the legend around on the chart. |
| legendScrollBgColor | Color | Hex Color Code | If you have too many items on the legend, a scroll bar shows up on the same. This attribute lets you configure the background color of the scroll bar. |
| reverseLegend | True/False | 0/1 | You can reverse the order of data sets in the legend by setting this attribute to 1. |
| interactiveLegend | True/False | 0/1 | This attribute lets you interact with the legend in your chart. When you click a legend key, the dataplots associated with that series are eliminated from the chart. Re-clicking the key causes the dataplots to reappear. |
| legendNumColumns | Number | Positive Integer | If your chart contains multiple series, the legend is displayed as a grid comprising of multiple legend keys. With the help of this attribute you can specify the number of columns that are to be displayed in the legend. |
| minimiseWrappingInLegend | True/False | 0/1 | Whether to minimize legend item text wrapping. |
| legendPointerColor | Color | Hex Color Code | Sets the legend pointer color for a gradient legend. |
| legendPointerAlpha | Number | 0 – 100 | Sets the legend pointer transparency for a gradient legend. |
| legendPointerBorderAlpha | Number | 0 – 100 | Sets the transparency for the legend pointer border for a gradient legend. |
| legendpointerbordercolor | Color | Hex color code | Sets the color for the border of the legend pointer. |
| legendScaleLineColor | Hex Color Code | Any | Allows you to set the color of the scale in gradient legend. |
| legendaxisbordercolor | Color | Hex Color Code | Sets color for the gradient legend’s axis border. |
| legendaxisborderalpha | Number | 0 – 100 | Sets transparency for the gradient legend’s axis border. |
| legendScaleLineAlpha | Numeric | 0 – 100 | Allows you to set the transparency of the scale in gradient legend. |
| legendScaleLineThickness | Numeric | Any | Allows you to set the thickness of the scale in gradient legend. |
| autoOrderLegendIcon | True/False | 0/1 | Allows you to show the legend icon in ascending order in icon legend. |
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
| defaultNumberScale | Text | Any | The default unit of the numbers that you are providing to the chart. |
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
| inDecimalSeparator | Text | Character | In some countries, commas are used as decimal separators and dots as thousand separators. In XML, if you specify such values, it will give an error while converting to number. So, the chart accepts the input decimal and thousand separator from user, so that it can convert it accordingly into the required format. This attribute lets you input the decimal separator. |
| inThousandSeparator | Text | Character | In some countries, commas are used as decimal separators and dots as thousand separators. In XML, if you specify such values, it will give an error while converting to number. So, the chart accepts the input decimal and thousand separator from user, so that it can convert it accordingly into the required format. This attribute lets you input the thousand separator. |
| decimals | Number | 0-10 | Number of decimal places to which all numbers on the chart would be rounded to. |
| forceDecimals | True/False | 0/1 | Whether to add 0 padding at the end of decimal numbers. For example, If you limit the maximum number of decimal digits to 2, a number like 55.345 will be rounded to 55.34. This does not mean that all numbers will be displayed with a fixed number of decimal places. For instance 55 will not be displayed as 55.00 and 55.1 will not become 55.10. In order to have fixed number of decimal places attached to all the numbers, set this attribute to 1. |

## Font Properties

Using the attributes below, you can define the generic font properties for all the text on the chart. These attributes allow you a high level control over font properties. If you intend to specify font properties for individual chart elements (like Caption, sub-caption etc.), you’ll need to use the Styles feature of Exago BI. Using Styles, you can also specify advanced font properties like Bold, Italics, HTML Mode etc.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| baseFont | Text | Font Name | This attribute lets you set the font face (family) of all the text (data labels, values etc.) on chart. If you specify the `outCnvBaseFont` attribute also, then this attribute controls only the font face of text within the chart canvas bounds. |
| baseFontSize | Number | 6 – 72 | This attribute sets the base font size of the chart, that is, all the values and the names in the chart which lie on the canvas will be displayed using the font size provided here. |
| baseFontColor | Color | Hex Color Code | This attribute sets the base font color of the chart, that is, all the values and the names in the chart which lie on the canvas will be displayed using the font color provided here. |
| outCnvBaseFont | Text | Font Name | This attribute sets the base font family of the chart text which lies outside the canvas, that is, all the values and the names in the chart which lie outside the canvas will be displayed using the font name provided here. |
| outCnvBaseFontSize | Number | 6 – 72 | This attribute sets the base font size of the chart, that is, all the values and the names in the chart which lie outside the canvas will be displayed using the font size provided here. |
| outCnvBaseFontColor | Color | Hex Color Code | This attribute sets the base font color of the chart, that is, all the values and the names in the chart which lie outside the canvas will be displayed using the font color provided here. |

## The rows Object and the row Object

While the `dataset` object and its child object, the `data` object can be used to define the rows and columns for a heat map chart, you have to be careful about the order of the values for the rows and columns. The `rows` object and its child object, the `row` object are used to create rows and predefine their order, enabling you to specify the data values in any order. Although the `row` object has to be defined within the `rows` object, rows cannot be collectively customized using the `rows` object, because it does not have any attributes of its own. These attributes let you define the order of rows for a heat map chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| id | Number/String | Any | Allows you to specify a unique Id for the rows. This id is used in the `data` object to place the data values in the pre-defined position. |
| label | Text | Any | Allows you to specify a label for the rows. If you do not specify the label the unique id will be displayed as the label for the rows in the chart. **Note:** The `label` attribute replaces the `name` attribute. Previously, either one of the attributes could be used to set the label. Support for the `name` attribute has been discontinued since v3.10.0. |
| showLabel | Text | Any | Allows you to show or hide the label of a particular row. |

## The columns Object and the column Object

While the `dataset` object and its child object, the `data` object can be used to define rows and columns for a heat map chart, you have to be careful about the order of the values for the rows and columns. The `columns` object and its child object, the `column` object are used to create columns and predefine their order, enabling you to specify the data values in any order. Although the `column` object has to be defined within the `columns ` object, note that columns cannot be collectively customized because the `columns` object does not have any attributes of its own. These attributes let you define the order of columns for a heat map chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| id | Number/String | Any | Allows you to specify a unique Id for the columns. This id is used in the `data` object to place the data values in the pre-defined position. |
| label | Text | Any | Allows you to specify a label for the columns. If you do not specify the label the unique id will be displayed as the label for the rows in the chart. **Note:** The `label` attribute replaces the `name` attribute. Previously, either one of the attributes could be used to set the label. Support for the `name` attribute has been discontinued since v3.10.0. |
| showLabel | Text | Any | Allows you to show or hide the label of a particular column. |

## The data set Object and the data Object

The `dataset` object contains a series of data defined through the `data` object. There are no attributes for the `dataset` object. The attributes used for the `data` object are mentioned below:

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| rowId | Text | Any | Specifies the position of the row where the data it is to be placed in the chart. If the `rows` object is used then it is mandatory to use the same id which is defined in the `row` object by the `id` attribute. |
| columnId | Text | Any | Specifies the position of the column where the data it is to be placed in the chart. If the `columns` object is used then it is mandatory to use the same id which is defined in the `column` object by the `id` attribute. |
| colorRangeLabel | Text | Any | This attribute is used to provide the color-range label which is defined in the `color` object of the `colorRange` object. It is used only in category based heat map chart. |
| value | Number | Any | This attribute allows you to display a value at the center of a data plot. |
| displayValue | Number/String | Any | Allows you to display any numeric value or string at the center of the dataplot. The settings of this attribute overwrites the settings of the ` value` attribute when both are used at the same time. |
| tlLabel | Number/String | Any | This attribute allows you to display a label on the top-left corner of a data plot. |
| trLabel | Number/String | Any | This attribute allows you to display a label on the top-right corner of a data plot. |
| blLabel | Number/String | Any | This attribute allows you to display a label on the bottom-left corner of a data plot. |
| brLabel | Number/String | Any | This attribute allows you to display a label on the bottom-left corner of a data plot. |
| color | Color | Hex Color Code | In Heat map chart, if you wish to highlight a particular cell, you can specify it’s color at “set” level using this attribute. |
| link | Text | Any | You can define links for individual data items. That enables the end user to click on data items (columns, lines, bars etc.) and drill down to other pages. To define the link for data items, use the link attribute. You can define links that open in same window, new window, pop-up window or frames. Please see “Drill Down Charts > Exago BI Link format” for more information. Also, you need to Url Encode all the special characters (like ? and &) present in the link. |
| toolText | Text | Any | By default, the tooltip text for a data item in the heat map chart includes the values of the `trLabel`, `tlLabel`, `brlabel`, `bllabel`, `trType`, `tlType`, `brType`, and `blType` attributes. Additionally, you can display more customized information using the `toolText` attribute. |
| showValue | True/False | 0/1 | You can individually opt to show or hide values of individual data items using this attribute. This value over-rides the data-set level value. |
| valueFontColor | Color | Hex Color Code | Specifies the font color of a data value for an individual data plot. |
| valueBgColor | Color | Hex Color Code | Sets the background color of a value text for an individual data plot. |
| valueBorderColor | Color | Hex Color Code | Sets the border color around the value text for an individual data plot. |
| alpha | Number | 0 – 100 | For Multi-series charts, you can define the alpha of data-sets at data set level. However, if you wish to highlight a particular data element, you can specify its alpha at “set” level using this attribute. |

## The colorRange Object

Attributes of the `colorRange` object for the heat map chart are used to define the type of legend, the lower limit of the scale, and the start and end labels. Note that the `colorRange` object is not used to collectively configure all ranges; the `color` object (child of the `colorRange` object) is used to do that.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| code | Color | Hex Color Code | Hex code of the color range using which it will be filled. |
| endLabel | Text | Any | Specifies the label for the upper limit of the gradient scale. |
| gradient | True/False | 0/1 | Allows you to display gradient legend. |
| mapByPercent | True/False | 0/1 | Allows you to display the data values in percentage. |
| minValue | Number | Any | Sets the minimum value or the lower limit of the numeric range and the gradient scale. |
| startLabel | Text | Any | Specifies the label for the lower limit of the gradient scale. |

## The color Object

The attributes of the `color` object, child of the `colorRange` object, are used to configure individual ranges on the gauge scale.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| alpha | Number | 0 – 100 | Sets the transparency of each range in the color range. |
| code | Color | Hex Color Code | Hex code of the color range using which it will be filled. |
| label | Text | Any | This attribute determines the label for each numeric range. The label appears either on the gradient scale or on icon legends depending on the legend type used. **Note:** The `label` attribute replaces the `name` attribute. Previously, either one of the attributes could be used to set the label. Support for the `name` attribute has been discontinued since v3.10.0. |
| maxValue | Number | Any | Specifies the upper limits of each numeric range. This attribute is mandatory in each `color` object for both gradient and icon legend. |
| minValue | Number | Any | Specifies the lower limits of each numeric range. This attribute is mandatory in each `color` object when icon legend is used. |
