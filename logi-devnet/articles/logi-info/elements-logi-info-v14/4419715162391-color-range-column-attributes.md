---
title: "Color Range Column Attributes"
id: 4419715162391
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715162391-Color-Range-Column-Attributes
updated_at: 2022-07-17T01:57:13Z
---

# Color Range Column Attributes

# Color Range Column Attributes

The attributes for the Color Range Column element are described below:

| Attribute | Description |
| --- | --- |
| Data Column | (Required) Specifies the data column in the datalayer to be evaluated. |
| ID | (Required) Specifies a unique ID for the Color Range Column element. This becomes the name of the first column added to the datalayer, which typically contains the **background color** values. |
| Color Range Style | Specifies the type of data to be used when evaluating data ranges. Options include *NumericRange* and *TextList*. See the information below about Color Range element attributes to see how this selection affects its behavior. Default value: *NumericRange* |
| Contrast Color Column ID | Specifies the name of the second column that will be added to the datalayer, which typically provides the **text color** values. This column is *automatically* populated with color values that will contrast well with the background colors determined for the Data Table cells. |
| Contrast Dark Color | If you prefer to specify a text color to be used when a cell background color is "dark", rather than let the choice be automatic, you can do so here. For example, white text for a black background.  Default: *automatic color selection* |
| Contrast Light Color | If you prefer to specify a text color to be used when a cell background color is "light", rather than let the choice be automatic, you can do so here. For example, brown text for a yellow background. Default: *automatic color selection* |

  

## Color Range Element Attributes

The Color Range Column element uses one or more **Color Range** child elements to specify the data ranges and colors. Multiple Color Range elements can be used to set different colors for different ranges of data.

The attributes of this child element are:

| Attribute | Description |
| --- | --- |
| Color | Specifies the color that will be used for the cell background color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. *Click the browse button to display theColor Picker tool.* |
| ID | Specifies a unique ID for the Color Range element. |
| Range End Value | Specifies the *ending* value of the data range that will be associated with this color. If the Color Range Column element's **Color Range Style** = *NumericRange*, then this value is assumed to be the end of a numeric range that:  * Begins at a lower value (if there are *no* other Color Range elements), or * Begins at the previous Range End Value ((if there are other Color Range elements)  When adding these elements with a numeric range, configure them so that their Range End values get progressively larger. If the Color Range Column element's **Color Range Style** = *TextList*, then this should be a specific text string value, such as "Profit" or "France". You may use the asterisk wildcard "\*" in the string to broaden the range of text values that will be associated with this color. |
