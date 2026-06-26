---
title: "Data Table Column Attributes"
id: 4419722793623
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722793623-Data-Table-Column-Attributes
updated_at: 2022-07-17T02:08:20Z
---

# Data Table Column Attributes

# Data Table Column Attributes

The **Data Table Column** element has the following attributes:

| Attribute | Description |
| --- | --- |
| Background Color | Specifies the background color of the of the column. Enter a color by name, decimal RGB value, or hex RGB value (prefix hex values with the pound sign, e.g. #112233). *Click the browse button to display the Color Picker tool.*  Data tokens can also be used here, potentially resulting in a different background color for each table cell. For more information, see [The Color Range Column](https://devnet.logianalytics.com/hc/en-us/articles/4419722746263-The-Color-Range-Column). |
| Class | Specifies a style class to be applied to the column. |
| Column Header | Specifies the text to be displayed in the column's heading. In special cases in which an Extra Header Row element is used to make grouped column headings, and one of its columns has a Row Span greater than 1, this attribute's value may be set to *None*. This prevents the header column from getting created and thus pushing other column headers into the wrong positions. An image file can be specified here instead of text, if Header Type is set to *Image*. |
| Column Header Class | Specifies a class for the Column Header text or image. Use this attribute to set the alignment and other styling of the Column Header text or image. If left blank, the text or image will be centered. |
| Condition | Specifies an expression that evaluates to a value of *True* or *False*. If *True*, then the column is displayed, otherwise it's removed. Expressions should be in JavaScript or intrinsic functionsyntax. Typically, expressions compare values using a token, such as @Data.value~ < 0. Enclose both sides of the expression in quotes when working with strings: "@Data.myColumn~" == "SomeValue". |
| Header Type | Specifies if the header will be text (the default) or an image. |
| ID | Specifies a unique element ID. |
| Scope Row Header | Specifies if the HTML output for data cells will be modified to improve Section 508 accessibility. Set to *True*  to output a column which includes header information for each row, changing the <TD> tags to <TH Scope="Row"> tags. |
| Security Right ID | When specified, access to this element can be controlled with Logi Security. Specify the ID of a Right defined in the application's \_Settings Security element. Only users with matching rights will be able to see the element. |
| Show Modes *removed,* *use Condition instead* | Specifies a text string that controls whether elements will be displayed or hidden. Leave this blank for the element to always be displayed or set it to *None* to hide it (it can be displayed again later with an Action.Show Element element). Set it to your own string value to have it appear only when the report's (root element's) Show Modes includes that value. Show Modes can contain multiple, comma-delimited values. |
| Text Color | Specifies the color of the text in the column. Enter a color by name, decimal RGB value, or hex RGB value (prefix hex values with the pound sign, e.g. #112233). *Click the browse button to display the Color Picker tool.*  Data tokens can also be used here, potentially resulting in a different text color for each table cell. For more information, see [The Color Range Column](https://devnet.logianalytics.com/hc/en-us/articles/4419722746263-The-Color-Range-Column). |
| Tooltip | Specifies text that appears when the user hovers the mouse over the column header. |
| Width | Specifies the width of the element, in Width Scale units. |
| Width Scale | Specifies the units, pixels or percentage, to be used with the Width attribute. |

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 Adding "HTML Attribute Params" to your Data Table enables you to apply your application to work with other frameworks or libraries easier. Depending on the type of HTML Attribute Params you add, there will be different parameters available to use, or you can define your own parameters. If an attribute was set in both Element and HTML Attribute Params, the one set in the HTML Attribute Params will be ignored.
