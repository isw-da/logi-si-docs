---
title: "Chart Advanced Features: Spark Line"
id: 5281579556887
section: "Charts and Visualizations"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281579556887-Chart-Advanced-Features-Spark-Line
updated_at: 2022-05-03T22:08:23Z
---

# Chart Advanced Features: Spark Line

# Chart Advanced Features: Spark Line

The following sections provide a list of available advanced attributes available for controlling and customizing **Spark Line** chart elements.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic contains documentation for advanced attributes which are third-party customizations that must be manually entered into the chart wizard. These topics were converted directly from the documentation provided by this third-party source. Not every attribute listed may be supported in Exago BI as some unexpected conflicts may occur in their integration within the application.

## Functional Attributes

These attributes let you control a variety of functional elements on the chart. For example, you can opt to show/hide data labels, data values. You can also set chart limits and extended properties.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| animation | True/False | 0/1 | This attribute lets you set the configuration whether the chart should appear in an animated fashion. If you do not want to animate any part of the chart, set this as 0. |
| animationDuration | Number | In seconds | This attribute sets the animation duration of the chart. `animationDuration` attribute is applicable only if animation of the chart is enabled. Default value: 1 sec |
| connectNullData | True/False | 0/1 | This attributes lets you control whether empty data sets in your data will be connected to each other OR will they appear as broken data sets? |
| setAdaptiveYMin | True/False | 0/1 | This attribute lets you set whether the y-axis lower limit will be 0 (in case of all positive values on chart) or should the y-axis lower limit adapt itself to a different figure based on values provided to the chart. |
| clickURL | URL in Exago BI format | Any | The entire chart can now act as a hotspot. Use this URL to define the hotspot link for the chart. The link can be specified in Exago BI Link Format. |
| clickURLOverridesPlotLinks | True/False | 0/1 | Sets whether the `clickURL` attribute (that sets a link to which the user is directed when the chart is clicked) overrides the `link` attribute (that sets a link to which the user is directed when a data plot is clicked). Default value: 0 (`clickURL` does not override `link`) |
| palette | Number | 1-5 | Each chart has 5 pre-defined color palettes which you can choose from. Each palette renders the chart in a different color theme. |
| paletteThemeColor | Color | Hex Color Code | If you want your own palette derived from a particular hex color, you can specify the same here. All other colors on the chart will automatically derive from that palette. |
| showPrintMenuItem | True/False | 0/1 | Whether to show “Print Chart” item in the context menu of the chart? Even if you opt to hide the item in context menu, you can still opt to invoke `print()` JavaScript method of the chart to print the same. |
| showValues | True/False | 0/1 | Sets the configuration whether data values will be displayed along with the data plot on chart. |
| manageResize | True/False | 0/1 | Setting this attribute to 1, you can allow the chart to automatically resize itself when the parent container of the chart is resized. |
| useEllipsesWhenOverflow | True/False | 0/1 | When enabled in auto mode, long data labels are truncated by adding ellipses to prevent them from overflowing the chart background. The default value is 1. |
| hasRTLText | Number | Any | This attribute, when set to `1`, indicates to the chart that the text (rendered on the chart) may contain RTL characters and the textual display has to be managed accordingly. |
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

## Chart captions

Using these attributes, you can set the various headings and titles of chart like caption, sub-caption.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| caption | Text | Any | Caption of the chart. |
| subCaption | Text | Any | Sub-caption of the chart. |

## Chart Caption Cosmetics

These attributes let you configure the cosmetics of chart caption and sub-caption.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| captionPosition | Text | “top”, “middle”, “bottom” | Sets the position of the caption according to the canvas. |
| captionOnRight | True/False | 0/1 | Whether caption should be on right of the canvas. Default Value: 0 |
| captionFontSize | Number | 6 – 72 | Sets the caption font size in pixels |
| subCaptionFontSize | Number | 6 – 72 | Sets the sub-caption font size (in pixels) |
| captionFont | Text | Font Name | Sets the caption font family |
| subCaptionFont | Text | Font Name | Sets the sub-caption font family |
| captionFontColor | Color | Hex Color Code | Sets the caption font color |
| subCaptionFontColor | Color | Hex Color Code | Sets the sub-caption font color |
| captionFontBold | True/False | 0/1 | Whether the caption font should be displayed in bold |
| subCaptionFontBold | True/False | 0/1 | Whether the sub caption font should be displayed in bold |

## Number Formatting Properties

Using the attributes below, you can control a myriad of options like: Formatting of commas and decimals Number prefixes and suffixes Decimal places to which the numbers will round to Scaling of numbers based on a user defined scale Custom number input formats

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| formatNumber | True/False | 0/1 | This configuration determines whether the numbers displayed on the chart will be formatted using commas, for example, 40,000 if ‘formatNumber’: ‘1’; and 40000 if ‘formatNumber’: ‘0’; |
| numberPrefix | Text | Any | Using this attribute, you could add prefix to all the numbers visible on the graph. For example, to represent all dollars figure on the chart, you could specify this attribute to $ to show like $40000, $50000. |
| numberSuffix | Text | Any | Using this attribute, you could add suffix to all the numbers visible on the graph. For example, to represent all figures quantified as per annum on the chart, you could specify this attribute to ‘/a’ to show like 40000/a, 50000/a. |
| decimals | Number | Any | Number of decimal places to which all numbers on the chart will be rounded to. |
| forceDecimals | True/False | 0/1 | Whether to add 0 padding at the end of decimal numbers? For example, if you set decimals as 2 and a number is 23.4. If `forceDecimals` is set to 1, the number will automatically be converted to 23.40 (note the extra 0 at the end). |
| formatNumberScale | True/False | 0/1 | Configuration whether to add K (thousands) and M (millions) to a number after truncating and rounding it – for example, if `formatNumberScale` is set to 1, 1043 will become 1.04K (with decimals set to 2 places). Same with numbers in millions – an M will be added at the end. |
| defaultNumberScale | Text | Any | The default unit of the numbers that you’re providing to the chart. |
| numberScaleUnit | Text | Any | Unit of each block of the scale. |
| numberScaleValue | Text | Any | Range of the various blocks that constitute the scale. |
| forceNumberScale | True/False | 0/1 | If a data value is less than the lowest given number is the number scale, this attribute forces the lower value of the `numberScaleUnit` to be applied to that data value. This attribute works only when `“formatNumberScale”: “1”` and the `defaultNumberScale` attribute is not defined. For example, if `“numberScaleUnit”: “K, M”`, `“numberScaleValue”: “1000, 1000”`, and `“forceNumberScale”: “1”`, a data value of `400` will be rendered as `0.40K`. |
| scaleRecursively | True/False | 0/1 | Whether recursive scaling should be applied. |
| maxScaleRecursion | Number | Any | How many recursions to complete during recursive scaling? -1 completes the entire set of recursion. |
| scaleSeparator | Text | Any | What character to use to separate the scales that are generated after recursion? |
| decimalSeparator | Text | Any | This attribute helps you specify the character to be used as the decimal separator in a number. |
| thousandSeparator | Text | Any | This attribute helps you specify the character to be used as the thousands separator in a number. |
| thousandSeparatorPosition | Number | Any | This option helps you specify the position of the thousand separator. |
| inDecimalSeparator | Text | Any | In some countries, commas are used as decimal separators and dots as thousand separators. In XML/JSON, if you specify such values, it will give an error while converting to number. The chart accepts the input decimal and thousand separators from user, so that it can convert it accordingly into the required format. This attribute lets you input the decimal separators. |
| inThousandSeparator | Text | Any | In some countries, commas are used as decimal separators and dots as thousand separators. In XML/JSON, if you specify such values, it will give an error while converting to number. The chart accepts the input decimal and thousand separators from user, so that it can convert it accordingly into the required format. This attribute lets you input the thousand separators. |

## Data Plot (line) Properties

These attributes let you configure how your plot (lines) will appear on the chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| lineColor | Color | Hex Color Code | Color using which the lines on the chart will be drawn. |
| lineThickness | Number | In pixels | Thickness of the lines on the chart. |
| lineAlpha | Number | 0 – 100 | Alpha of the lines on the chart. |
| showShadow | True/False | 0/1 | Whether to apply the shadow effect for the data plot. |

## Anchor Properties

In line charts, anchors (or marker points) are polygons which appear at the joint of two consecutive line points. These are indicators to show the position of data points. The anchors handle tool tips and links for the data points. So, if you opt to not render anchors on a chart, the tool tips and links won’t function. You can, however, hide them by setting alpha to 0 and still enable tool tips and links. In area charts, anchors are set transparent by default. In case you wish to show the anchor, use anchorAlpha=”100″ attribute. You can customize all the facets of anchors using the properties below.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| drawAnchors | True/False | 0/1 | Whether to draw anchors on the chart. |
| anchorSides | Number | Any | This attribute sets the number of sides the anchor will have. For for example, an anchor with 3 sides will represent a triangle, with 4 it will be a square and so on. |
| anchorStartAngle | Number | 0 – 360 | This attribute sets the starting angle of anchors. Default value: 90 |
| anchorRadius | Number | In pixels | This attribute sets the radius (in pixels) of the anchor. |
| anchorColor | Color | Hex Color Code | Lets you set the color of anchors. |
| anchorAlpha | Number | 0 – 100 | Lets you set the alpha of anchors. |
| anchorImageUrl | Exago BI link format | URL | If you want to use an external image (JPG/PNG) as an anchor, this attribute lets you specify the URL. **Note:** Due to cross domain security restrictions it is advised to use an image from the same domain name as your charts. |
| anchorImageAlpha | Number | 0 – 100 | This attribute allows to set a transparency for images displayed as anchors in charts. Default value: 100 |
| anchorImageScale | Number | 0 – 100 | This attribute allows to set a scale for magnifying images displayed as anchors. Default value: 100 |
| anchorImagePadding | Number | In Pixels | This attribute sets the padding between the anchor image and the border of the anchor. For the anchor image, instead of decreasing the size of the image this attribute crops the image. Default value: 1 |

## Open, close, high & low properties

The spark line chart highlights the open, close, high & low points and also shows their value. Using the following attributes, you can configure the chart to: Change color of open, close, high, low points Opt whether to highlight each one using anchors Whether to show values for each one of them

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| openColor | Color | Hex Color Code | Color for opening value anchor. |
| closeColor | Color | Hex Color Code | Color for closing value anchor. |
| highColor | Color | Hex Color Code | Color for high value anchor. |
| lowColor | Color | Hex Color Code | Color for low value anchor. |
| showOpenAnchor | True/False | 0/1 | Whether to show anchor for opening value? By default this attribute is set to 1. |
| showCloseAnchor | True/False | 0/1 | Whether to show anchor for closing value? By default this attribute is set to 1. |
| showHighAnchor | True/False | 0/1 | Whether to show anchor for high value? By default this attribute is set to 1. |
| showLowAnchor | True/False | 0/1 | Whether to show anchor for low value? By default this attribute is set to 1. |
| showOpenValue | True/False | 0/1 | Whether to show the opening value beside the chart? By default this attribute is set to 1. |
| showCloseValue | True/False | 0/1 | Whether to show the closing value beside the chart? By default this attribute is set to 1. |
| showHighLowValue | True/False | 0/1 | Whether to show the high/low value beside the chart? By default this attribute is set to 1. |

## Period block properties

Period blocks are alternate colored bands to easily interpret periods on the chart. The following attributes helps in configuring Period blocks.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| periodLength | Number | Any | How many data points will each period block encapsulate? |
| periodColor | Color | Hex Color Code | Color for the period block. |
| periodAlpha | Number | 0 – 100 | Alpha for the period block. |

## Chart Cosmetics

The following attributes let you configure chart cosmetics like background color, background alpha, canvas color & alpha etc.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| bgColor | Color | Hex Color Code | This attribute sets the background color for the chart. You can set any hex color code as the value of this attribute. To specify a gradient as background color, separate the hex color codes of each color in the gradient using comma. Example: `#FF5904, #FFFFFF`. |
| bgAlpha | Number | 0 – 100 | Sets the alpha (transparency) for the background. If you’ve opted for gradient background, you need to set a list of alpha(s) separated by comma. |
| bgRatio | Numbers separated by comma | Any | If you’ve opted for a gradient background, this attribute lets you set the ratio of each color constituent. |
| bgAngle | Number | 0-360 | Angle of the background color, in case of a gradient. |
| showBorder | True/False | 0/1 | Whether to show a border around the chart or not? |
| borderColor | Color | Hex Color Code | Border color of the chart. |
| borderThickness | Number | In pixels | Border thickness of the chart. |
| borderAlpha | Number | 0 – 100 | Border alpha of the chart. |
| bgImage | Text | Any | To place any image (JPG/PNG/GIF) as background of the chart, enter the (path and) name of the background image as a URL without quotes around it. It should be in the same domain as the chart. |
| bgImageAlpha | Number | 0 – 100 | This attribute specifies the opacity for the loaded background image. |
| bgImageDisplayMode | Text | ‘stretch’, ’tile’, ‘fit’, ‘fill’, ‘center’, ‘none’ | Helps you specify the mode in which the background image is to be displayed. Stretch – expands the image to fit the entire chart area, without maintaining original image constraints. Tile – the image is repeated as a pattern on the entire chart area. Fit – fits the image proportionately on the chart area. Fill -proportionately fills the entire chart area with the image. Center – the image is positioned at the center of the chart area. None – Default mode. |
| bgImageVAlign | Text | ‘top’, ‘middle’, ‘bottom’ | Helps you to vertically align the background image. |
| bgImageHAlign | Text | ‘left’, ‘middle’, ‘right’ | Helps you to horizontally align the background image. |
| bgImageScale | Number | 0-300 | Helps you magnify the background image. This attribute will only work when the attribute `bgImageDisplayMode` is set to none, center, or tile. |
| logoURL | Text | Any | You can load an external logo (JPEG/PNG) to your chart, this attribute lets you specify the URL. Due to cross domain security restrictions it is advised to use a logo from the same domain name as your charts. |
| logoLeftMargin | Number | In Pixels | This attribute helps you set the amount of empty space that you want to put on the left side of your logo image. Nothing is rendered in this space. |
| logoTopMargin | Number | In Pixels | This attribute helps you set the amount of empty space that you want to put on top of your logo image. Nothing is rendered in this space. |
| logoPosition | Text | ‘TL’, ‘TR’, ‘BL’, ‘BR’, ‘CC’ | Where to position the logo on the chart: TL – Top-left TR – Top-right BR – Bottom right BL – Bottom left CC – Center of screen |
| logoAlpha | Number | 0 – 100 | Once the logo has loaded on the chart, you can configure its opacity using this attribute. |
| logoScale | Number | 0 – 100 | You can also change the size of externally loaded logo at run-time by specifying a value for this parameter. |
| logoLink | Text | Any | If you want to link the logo to an external URL, specify the link in this attribute. The link can be in Exago BI link format, allowing you to link to new windows, pop-ups, frames etc. |

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

## Font Properties

Using the attributes below, you can define the generic font properties for all the text on the chart. These attributes allow you a high level control over font properties. If you intend to specify font properties for individual chart elements (like Caption, sub-caption etc.), you’ll need to use the Styles feature. Using Styles, you can also specify advanced font properties like Bold, Italics, HTML Mode etc. Using Styles you can also configure real-time values.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| baseFont | Text | Font Name | This attribute lets you set the font face (family) of all the text (data labels, values etc.) on chart. If you specify outCnvBaseFont attribute also, then this attribute controls only the font face of text within the chart canvas bounds. |
| baseFontSize | Number | Any | This attribute sets the base font size of the chart that is, all the values and the names in the chart which lie on the canvas will be displayed using the font size provided here. |
| baseFontColor | Color | Hex Color Code | This attribute sets the base font color of the chart that is, all the values and the names in the chart which lie on the canvas will be displayed using the font color provided here. |

## Tool tip Attributes

These attributes let you control the tooltip. You can set the background color, border color, separator character and few other details.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| showToolTip | True/False | 0/1 | Whether to show tooltip for the annotations? |
| toolTipBgColor | Color | Hex Color Code | Background color for the tooltip |
| toolTipColor | Color | Hex Color Code | Font color for the tool-tip. |
| toolTipBorderColor | Color | Hex Color Code | Border Color for the tooltip. |
| tooltipBorderAlpha | Number | 0 – 100 | Sets the border transparency for tool tip. |
| showToolTipShadow | True/False | 0/1 | Whether to show shadow for tooltips. |
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
| openHoverColor | Color | Hex color code | This attribute sets the hover color for opening value anchor. |
| closeHoverColor | Color | Hex color code | This attribute sets the hover color for closing value anchor. |
| highHoverColor | Color | Hex color code | This attribute sets the hover color for high value anchor. |
| lowHoverColor | Color | Hex color code | This attribute sets the hover color for low value anchor. |

## Chart Padding & Margins

The following attributes help you control chart margins and padding. Exago BI allows you manually customize the padding of various elements on the chart to allow advanced manipulation and control over chart visualization. Padding in Exago BI is always defined in pixels, unless the attribute itself suggests some other scale (like `plotSpacePercent`, which configures the spacing using percentage values). You can also define the chart margins. Chart Margins refer to the empty space left on the top, bottom, left and right of the chart. It’s not necessary for you to specify any padding/margin values. Exago BI automatically assumes the best values for the same, if you do not specify the same.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| captionPadding | Number | In pixels | This attribute lets you control the horizontal space (in pixels) between the caption and left side of chart canvas. |
| valuePadding | Number | In pixels | This attribute lets you control the horizontal space between value textboxes and chart. |
| chartLeftMargin | Number | In pixels | Amount of empty space that you want to put on the left side of your chart. Nothing is rendered in this space. |
| chartRightMargin | Number | In pixels | Amount of empty space that you want to put on the right side of your chart. Nothing is rendered in this space. |
| chartTopMargin | Number | In pixels | Amount of empty space that you want to put on the top of your chart. Nothing is rendered in this space. |
| chartBottomMargin | Number | In pixels | Amount of empty space that you want to put at the bottom of your chart. Nothing is rendered in this space. |
| canvasLeftMargin | Number | In pixels | Left margin of canvas. Canvas will start from that position. |
| canvasRightMargin | Number | In pixels | Right margin of canvas. Canvas will end at that position. |

## The data Object

n single-series charts, each instance of the `data` object represents a data value to be plotted on the chart. For a single-series chart, one instance of the `data` object looks as shown in the example below:

```
"data"[{
		"label": "Jan",
		"value": "10000"
	}]
```

Attributes of the `data` object are used to set and configure the data values for the chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| alpha | Number | 0 – 100 | This attribute determines the transparency of a data item. The range for this attribute is 0 to 100. 0 means complete transparency (the data item wont be shown on the graph) and 100 means opaque. |
| color | Color | Hex Color Code | If you want to define your own colors for the data items on chart, use this attribute to specify color for the data item. |
| dashed | True/False | 0/1 | Whether the border of this data item should appear as dashed. This is particularly useful when you want to highlight a data (such as forecast or trend etc.). |
| displayValue | Text |  | If instead of the numerical value of this data, you wish to display a custom string value, you can specify the same here. Examples are annotation for a data item etc. |
| link | Text | Any | You can define links for individual data items. That enables the end user to click on data items (columns, lines, bars etc.) and drill down to other pages. To define the link for data items, use the link attribute. You can define links that open in same window, new window, pop-up window or frames. Please see “Drill-Down > Using JavaScript Functions as Links” for more information. Also, you’ll need to Url Encode all the special characters (like ? and &) present in the link. |
| showValue | True/False | 0/1 | You can individually opt to show/hide values of individual data items using this attribute. |
| valueFontColor | Color | Hex Color Code | Specifies the font color of a data value for an individual data plot. |
| valueBgColor | Color | Hex Color Code | Sets the background color of a value text for an individual data plot. |
| valueBorderColor | Color | Hex Color Code | Sets the border color around the value text for an individual data plot. |

## Trend-lines

Trend-lines are horizontal lines that aid in interpretation of data with respect to some pre-determined value. For example, if you are plotting the sales data for the current year, you might want to show the previous year’s average monthly sales as a trend indicator for ease of comparison. The `lines` object, child of the `trendlines` object is used to add trend-lines to a chart. Although the `line` object has to be defined within the `trendlines` object, the latter cannot be used to collectively customize trend-lines, because it does not have any attributes of its own. The attributes of the `lines` object, child of the `trendlines` object, are used to create and customize trend-lines for charts.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| alpha | Number | Any | Alpha of the trend line. |
| color | Color | Hex Color Code | Color of the trend line and its associated text |
| dashed | True/False | 0/1 | Whether the trendline should be rendered as dashed lines. Default value: 0 (trendline rendered using straight lines) |
| dashLen | Number | In pixels | Sets the length of each dash when trendline is rendered as dashed lines. |
| dashGap | Number | In pixels | Sets the gap between consecutive dashes when trendline is rendered as dashed lines. |
| endValue | Number | Any | The ending y-axis value for the trendline. Say, if you want to plot a slanted trendline from value 102 to 109, the `endValue` will be 109. If you do not specify a value for `endValue`, it will automatically assume the same value as `startValue`. |
| isTrendZone | True/False | 0/1 | Whether the trend will be displayed as a line or a zone (fill-colored rectangle). |
| showOnTop | True/False | 0/1 | By default, the trendline/trendzone appears below the dataplots. This attribute allows you to display the trendline/trendzone on top of the dataplots. |
| startValue | Number | Any | The starting value for the trendline. Say, if you want to plot a slanted trendline from value 102 to 109, the `startValue` will be 102. |
| thickness | Number | In pixels | If you’ve opted to show the trend as a line, this attribute lets you define the thickness of trend line. |

## Trend-lines (Chart level attributes)

Trend-lines are horizontal lines that aid in interpretation of data with respect to some pre-determined value. For example, if you are plotting the sales data for the current year, you might want to show the previous year’s average monthly sales as a trend indicator for ease of comparison. Cosmetics for all the trend-lines rendered can be attained using this set of attributes. Although there are set of attributes of the `line object`, used to create and customize trend-lines, these set of attributes effect all the trend-lines rendered in your chart.

| Attribute | Type | Value | Description |
| --- | --- | --- | --- |
| trendlineColor | Color | Hex Color Code | Sets color of all the trend lines and its associated text in the chart. |
| trendlineThickness | Number | In Pixels | If you’ve opted to show the trend as a line, this attribute lets you define the thickness of all the trend lines in your chart. |
| trendlineAlpha | Number | 0 – 100 | Sets transparency for all the trend lines in your charts. |
| trendLineToolText | Text | Any | Sets the tooltip text of the trend-line. It accepts macros, plain text, and HTML tags, as string. |
| showTrendlinesOnTop | True/False | 0/1 | Whether all the trend line/zone will be displayed over data plots or under them. |
