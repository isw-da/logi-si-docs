---
title: "Legend Attributes"
id: 4406817017495
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817017495-Legend-Attributes
updated_at: 2022-04-06T06:03:23Z
---

# Legend Attributes

# Legend Attributes

The Legend element has the following attributes:

| Attribute | Description |
| --- | --- |
| Alignment Horizontal | Sets the horizontal alignment of the legend at the *Left*, *Center*, or *Right*, of the plot area. The default value is *Right*. |
| Alignment Vertical | Sets the vertical alignment of the legend at the *Top*, *Middle*, or *Bottom*, of the plot area. The default value is *Top*. |
| Background Color | Sets the legend background color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. *#112233*. |
| Background Color Transparency | Specifies the transparency of the legend background color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Border Color | Sets the legend border line color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. *#112233*. |
| Border Color Transparency | Specifies the transparency of the legend border line color. The lowest value of *0* specifies that the border line is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent line. Use medium-level transparency to allow different chart layers to show through each other. |
| Border Radius | Sets the amount of rounding for legend border line corners, in pixels. The default value is *4* pixels. |
| Border Thickness | Sets the canvas border line thickness, in pixels. The default value is *0*, for no border. |
| Caption | Specifies the text of a caption that will appear at the top of the legend. |
| Format | Specifies a format for the legend items, i.e. the data or text from the Series element's Legend Label attribute. |
| Inside Plot Area | Specifies whether space in the canvas will be reserved for the legend (*False*) or whether it will overlap other content (*True*). The default value is *False*. |
| Legend Orientation | Specifies whether the legend will be displayed in a *Horizontal* format at the center-bottom of the canvas (the default) or a *Vertical* format at the top-right of the canvas. |
| Maximum Height | Specifies the maximum height, in pixels, of the legend. If the number of legend items causes the height of the legend to exceed this value, scroll arrows will be displayed to allow scrolling of the items. |
| Offset X | Sets the horizontal position offset of the legend relative to the chosen horizontal alignment, in pixels. |
| Offset Y | Sets the vertical position offset of the legend relative to the chosen vertical alignment, in pixels. |
| Reversed Item Order | Set to *True* to reverse the order of legend items. The default value is *False*. |
| Show All Caption | Specifies the caption for the clickable "Show All" link, which shows or hides all legend items. The link appears when the number of items is equal to or greater than the Show All Threshold attribute's value. To hide the link, set Show All Threshold to a large number, such as 9999. The default value is *Show All*. |
| Show All Threshold | Specifies the legend item threshold number that determines when the "Show All" link will appear. When the number of items is equal to or greater than this value, the link appears. To hide the link, set this attribute to a large number, such as *9999*. The default value is *4*. |
| Spacing | Sets the space, in pixels, between the legend and chart plot area. The default value is *10* pixels. |
| Symbol Width | Sets the width, in pixels, of the symbol preceding legend items. The default value is *16* pixels. |
| Width | Sets the width, in pixels, of the legend. If left blank, a width will be automatically determined. |
