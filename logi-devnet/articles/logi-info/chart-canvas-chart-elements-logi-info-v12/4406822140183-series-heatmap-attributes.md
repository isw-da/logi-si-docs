---
title: "Series.Heatmap - Attributes"
id: 4406822140183
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822140183-Series-Heatmap-Attributes
updated_at: 2022-04-06T06:03:54Z
---

# Series.Heatmap - Attributes

# Series.Heatmap - Attributes

The Series.Heatmap element has the following attributes:

| Attribute | Description |
| --- | --- |
| Heat Map Color Data Column | (Required) Specifies the name of a datalayer column whose values will determine the color of the cells, using a high-to-low gradient based on the three Value Color attributes. |
| Heat Map Label Data Column | (Required) Specifies the name of a datalayer column whose values will be used as labels inside the cells. |
| Heat Map Size Data Column | (Required) Specifies the name of a datalayer column whose values will determine the size of the cells. |
| Cell Border Color | Sets the color of the cell borders. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. |
| Cell Border Color Transparency | Specifies the transparency of the Cell Border Color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Cell Border Thickness | Sets the thickness of the cell border lines, in pixels, when the related Cell Border Color attribute has a value. The default value is *1* pixel. |
| Disable Mouse Tracking | Disables mouse tracking for the series, when set to *True*. This affects tooltips and click events on cells. For large datasets, this may improve performance.  The default value is *False*. |
| High Value Color | Specifies the color for the highest data value. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #D5F484. |
| Hover Brightness | Specifies the amount to change a cell's color when the mouse pointer is hovered over it. Values can be between *0* (no change) and *15* (lighter). The default value is *2*. |
| ID | Specifies the unique element ID. |
| Low Value Color | Specifies the color for the lowest data value. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #D5F484. |
| Medium Value Color | Specifies the color for the data values in the middle of the dataset. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #D5F484. |
