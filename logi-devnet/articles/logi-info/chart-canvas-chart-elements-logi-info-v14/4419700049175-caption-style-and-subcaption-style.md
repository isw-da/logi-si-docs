---
title: "Caption Style and SubCaption Style"
id: 4419700049175
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700049175-Caption-Style-and-SubCaption-Style
updated_at: 2022-07-17T02:25:42Z
---

# Caption Style and SubCaption Style

# Caption Style and SubCaption Style

The Chart Canvas element's Caption and SubCaption attributes let you specify text that appears at the top (or elsewhere) on the canvas. Its **Caption Style** and **SubCaption Style** child elements can be used to format and position this text. For example:

![](https://devnet.logianalytics.com/hc/article_attachments/7522852675351/introcccharts_05.png)

The examples above show some variations in the format and positioning of Caption and SubCaption text.

## Attributes

Both elements have the following attributes, except as noted:

| Attribute | Description |
| --- | --- |
| Alignment Horizontal | Sets the horizontal alignment of the text as *Left*, *Center*, or *Right*, within the canvas. The default value is *Center*. |
| Alignment Vertical | Sets the vertical alignment of the text as *Top*, *Middle*, or *Bottom*, within the canvas. The default value is *Top*. |
| Caption Spacing | Sets the space between the caption and its subject, in pixels. |
| Font Color | Sets the caption font color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g.#112233. |
| Font Family | Specifies the names of one or more fonts. When multiple fonts are specified, with commas between each, the browser uses the first recognized font. |
| Font Italic | Specifies whether the font is *Italic.* |
| Font Size | Sets the caption font size, in pixels. |
| Font Weight | Specifies the weight (thickness) of characters in the caption text. Options include *Lighter*, *Normal*, *Bold*, and *Bolder*. The default value is *Normal*. |
| Format | Specifies a format for the text displayed. For more information, see [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722930327-Format-Data). |
| Inside Plot Area | Specifies whether space in the canvas will be reserved for the caption (*False*) or whether it will overlap other content (*True*). The default value is *False*. |
| Offset X | Sets the horizontal position offset of the caption relative to the horizontal alignment, in pixels. |
| Offset Y | Sets the vertical position offset of the caption relative to the vertical alignment, in pixels. |

The **Inside Plot Area** attribute causes the Caption to be displayed *inside* the plot area, instead of between it and the edge of the canvas:

![](https://devnet.logianalytics.com/hc/article_attachments/7522858673815/introcccharts_06.png)

As shown in the example above, when Inside Plot Area is set to *True*, the plot area is scaled to create space for the Caption text.
