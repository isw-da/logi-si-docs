---
title: "Word - Cascading Style Sheet Support"
id: 4406817439895
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817439895-Word-Cascading-Style-Sheet-Support
updated_at: 2022-04-06T06:06:06Z
---

# Word - Cascading Style Sheet Support

# Word - Cascading Style Sheet Support

When a Word export is being generated, the export engine processes any style sheet information along with the report data. The style sheet assigned to the report is used; you do not need to do anything additional to specify the style sheet.
If desired, you can use two different style sheets in your report definition, one for the report and one for the Word export:

1. Select the root element of your report definition and set its **Default Show Modes** attribute value to an arbitrary string, such as "Normal".
2. Add two Style Sheet elements to your report definition.
3. Assign one Style Sheet element's **Show Modes** attribute a value that matches the string used in Step 1, "Normal". This style sheet will be used for the regular HTML report.
4. Assign the other Style Sheet element's Show Modes attribute a value that matches the Target.Native Word element's Report Show Modes attribute value (both should be an arbitrary string that *does not match* the string from Step 1, such as "Export".

Now when the report runs in a browser, the first style sheet will be applied; when it's exported to Word, the second style sheet will be applied.
What if you want to combine the effects from this topic and [Word - Hiding Elements When Exporting](https://devnet.logianalytics.com/hc/en-us/articles/4406817446807-Word-Hiding-Elements-When-Exporting), i.e. hide some elements and use different spreadsheets? Just remember that the Show Modes attribute can accept several values, separated by a comma. To combine the examples from these two sections, ensure that the root element's Default Show Modes attribute includes both Show Modes values: "Normal,NoExport" (do not enter the double quotes).

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The following
considerations should be noted when working with style sheets for Word exports. Failure to
follow these guidelines will result in style sheet information being ignored by
the Word exporter, or, in some cases, failure of the export process.

1. When defining CSS classes in their style sheet(s), you *must* include a space or line feed between the name of a class and the opening curly-brace. These are **valid** classes:

.myClass1{ color: Blue; }  
.myClass2  
 {  
 color: Blue;  
 }

but this is in *invalid* class:

.myBadClass{ color: Blue; }

2. You may combine classes using the CLASS attribute of elements in a report definition file:

CLASS="class1 class2"

3. You *must* use the **Width** and **Width Scale** attributes when setting table and cell widths. The CSS "width" property is not supported.
4. If duplicate class definitions exist, only the first definition is used.
5. If duplicate properties appear inside a class, only the last occurrence is used.
6. The following CSS *Selectors* are supported by the Word export engine:

| Selector | Example |
| --- | --- |
| Type | TABLE |
| Class | .*<classname>* (begins with a period) |
| ID | #second\_table |
| Type-prefixed Class | TABLE.*<classname>* |

7. The following CSS Level 1 *Properties* are supported by the Word exporter. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The *order* of the values for properties with multiple values is significant. Multiple values must be listed in the order defined in this table or the Word exporter will ignore the property altogether:

| Property | Value/Example |
| --- | --- |
| background | <background-color> |
| background-color | Web colors (examples: #00FF00 or Green) |
| border | <border-width> <border-style> <border-color> <border-style> <border-color> <border-color> |
| border-bottom | <border-width> <border-style> <border-color> <border-style> <border-color> <border-color> |
| border-color | Web colors (examples: #00FF00 or Green) |
| border-style | Example: solid |
| border-top | <border-width> <border-style> <border-color> <border-style> <border-color> <border-color> |
| border-width | Pixels (example: 25px) |
| color | Web colors (examples: #00FF00 or Green) |
| filter | Examples: flipv, fliph |
| font | <font-style> <font-weight> <font-size> <font-family>; |
| font-family | Base-14 & TrueType fonts (example: Arial) |
| font-size | Points (example: 12pt) |
| font-style | Example: italic |
| font-weight | Example: bold |
| padding | <padding-top> <padding-right> <padding-bottom> <padding-left> |
| height | Pixels (example: 25px) |
| padding-top | Pixels (example: 25px) |
| padding-right | Pixels (example: 25px) |
| padding-bottom | Pixels (example: 25px) |
| padding-left | Pixels (example: 25px) |
| text-align (see Note below) | Examples: left, right, center, justify |
| text-decoration | Examples: underline, overline |
| vertical-align | Examples: top, middle, bottom |
| writing-mode | Examples: lr-tb, tb-rl |

## Style Tips

* With a limited list of CSS properties, if Native Word exporting is going to be used in an application, it's a good idea to design the CSS classes used for elements to be exported with these limitations in mind. That way a single style sheet could be used for all exports and the HTML display of a report. Many of these property limitations stem from the fact that there isn't a good way to translate certain CSS properties into a formatting setting in a native Word document; the formatting options available
  in a native Word document are much more limited than those available with CSS.
* When it comes to specifying font-size, Word can't handle pixel values. All pixel values specified in CSS classes for font-size will be converted to point values. Therefore, it's highly recommended that points be used to specify the font-size.
* Word builds tables sequentially, cell-by-cell, left-to-right, top-to-bottom. Word will attempt to apply all the properties of the previous cell to the cell currently being created unless the properties are explicitly defined differently for the current cell using a different CSS class which overwrites all the properties of the previous cell. For instance, if the first cell has a "border-bottom: 1px solid black;" class applied and you want the next cell to appear without a bottom border,
  you would have to apply a class with the following property: "border-bottom: 1px solid white;".
* Use **text-align** to set the alignment of tables. This is not generally allowed by the rules of CSS, however, an exception is made because the **align** attribute is not supported.
