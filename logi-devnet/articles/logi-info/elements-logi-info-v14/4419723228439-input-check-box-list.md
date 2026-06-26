---
title: "Input Check Box List"
id: 4419723228439
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723228439-Input-Check-Box-List
updated_at: 2022-07-17T02:23:11Z
---

# Input Check Box List

# Input Check Box List

The Input Check Box List element combines the features of the [Input Select List](https://devnet.logianalytics.com/hc/en-us/articles/4419707905175-Input-Select-List) and [Input Check Box](https://devnet.logianalytics.com/hc/en-us/articles/4419715534871-Input-Check-Box) elements: it displays items in a list, each with its own check box.

![](https://devnet.logianalytics.com/hc/article_attachments/7522735818007/introui_17.png)

This user input element operates using **collections of data** and requires a datalayer to provide that data.

## Using the Input Check Box List

This element requires a datalayer to provide the items that will appear in the list. If the list of items is short and unchanging, the **DataLayer.Static** element can be used to "hard code" the items. If the list is longer, the **DataLayer.XML** element can be used to read the data from an XML file. If the list is dynamic, elements such as **DataLayer.SQL** can be used to retrieve the items from a datasource, possibly with grouping to provide unique values.

If the datasource provides one, the value passed to the next report or process task can be *different* from the displayed text. The control automatically sizes itself to accommodate the *widest* display text, or you can specify a width.

The element has many of the attributes common to all Input elements and includes these additional attributes:

| Attribute | Description |
| --- | --- |
| Caption Column | (Required) Specifies the name of the datalayer column that contains the text to be displayed in the selection list. |
| Value Column | (Required) Specifies the name of the datalayer column that contains the value to be passed to the next report or process task *if* the check box is checked. |
| Check All Caption | Specifies the text for the "Check all" check box. Enter a value of "none" to hide it altogether. |
| Check Box List Dropdown | Specifies whether the list is rendered as a drop-down list. Default: *False* (i.e. static list). If the check box List Dropdown attribute is set to *True*, then the drop-down element is rendered. When the drop-down is rendered, you can utilize the search feature via input box. The search will be performed every time the search content changes. Basic conditions are: ignoring case, not full word matching, and the search content will not be treated as regular. |
| Column Count | Specifies how many columns of items should be displayed. Default: *1* |
| Default Value | Specifies the value of the item to be pre-checked in the control. Enter the actual the value (from the "Value" column), not the displayed text, in order to set this. Can be used with @Request tokens passed from another report or a process task, and other tokens.  To specify multiple items to be pre-checked, add a child Default Values element. |
| Dropdown Button Class | Specifies the style sheet class used to control the drop-down header and button appearance, such as font color. The actual button icon image can be overridden by creating a class named  .rd-check boxlist-icon and setting its background-image selector to the desired image file. |
| Dropdown None Selected Caption | Specifies the text that appears in the drop-down header when there are no items selected. Default: *Select options* |
| Dropdown Selected Caption | As items are checked, their Caption text is displayed in a comma-separated list in the drop-down header. When there are too many items to be shown, the text changes to show the number of items selected. This attribute specifies the text displayed at that time. The "#" character is the placeholder for the number of selected items. Default: *# selected* |
| Enable Search | Specifies whether the search box displays. Default: *True*. Setting the attribute to *False* turns off the search box.  New for 14.2 You can also enter any value to specify the threshold for the search box. If the value is a valid integer, the search box will be visible if the item count is equal to or greater than the value. Any invalid input will be treated as *True*, the search box displays. |
| Height Height Scale | Specifies the height of the element, in pixels or as a percent of its containing element. If left blank, a default value is automatically applied. |
| List Captions Element ID | Specifies the element ID of an Input Hidden element, which will contain the Caption Column values for the items selected when the definition is submitted. The values will be available in a @Request token using the same ID. |
| Multiple Selections | Specifies if multiple list check boxes can be checked at the same time. Default: *True* |
| Tooltip | Specifies text to be displayed as a tooltip when the mouse is hovered over the control and, if no Tooltip Column is specified, over the list of options. |
| Tooltip Column | Specifies the datalayer column that contains text to be shown as a tooltip when the mouse is hovered over *each item* in the list of options. Can be used with or without the Tooltip attribute. |
| Width Width Scale | Specifies the width of the element , in pixels or as a percent of its containing element. If left blank, a default value is automatically applied. |

This element can be used by itself or within an **Input Grid** element to make alignment with other Input elements easier.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 Adding **HTML Attribute Params** to your User Input elements enables you to apply your application to work with other frameworks or libraries easier. Depending on the type of HTML Attribute Params you add, there will be different parameters available to use, or you can define your own parameters. If an attribute was set in both Element and HTML Attribute Params, the one set in the HTML Attribute Params will be ignored.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) If the Input Check Box List is placed under a **Data Table** that produces multiple rows, the Input Check Box List's datalayer only runs once and thus all check box lists will have the same rows. In such an arrangement, you cannot reference @Data tokens from the parent Data Table in the Input Check Box List's datalayer.

## Displaying Hierarchical List Items

The **Check Box List Branch** element allows the items inside Input Check Box List to be displayed in a hierarchical arrangement. The example below shows two levels of items below the major item:

![](https://devnet.logianalytics.com/hc/article_attachments/7522754616215/introui_18_583x307.png)

When one or more Check Box List Branch elements are used, data for the Input Check Box List must come from a *hierarchical* datalayer. This can be
created by using a datalayer that has a **Group Filter** element with its **Hierarchical** attribute set to *True*.
The data should have the same number of hierarchical levels as there are Check Box List Branch elements or, put more simply, the number of Group
Filters under the datalayer should equal the number of Check Box List Branch elements.

As with the Input Check Box List element, Check Box List Branch provides optional custom expanded/collapsed image attributes, and Class and initial state attributes

## Getting Its Data

The value (from the "Value column") associated with a checked item (from the "Caption column") is available in the next Report or Process task with an @Request token. For example, if the element's **ID** is set to *inpCity* then the token @Request.inpCity~will equal that value.

If nothing is checked in the list and the page is submitted, then this @Request token will equal an empty string ("").

If the **Multiple Selections** attribute is not set to *False*, the @Request token will contain a **comma-separated list** of the checked values. For use with SQL statements, it may be desirable to surround each individual value in the list with single quotes. This can be done using the SingleQuote token modifier. Thus

@Request.MySelections~ which hasa value of London,Berlin,Rome becomes   
@SingleQuote.Request.MySelections~ which has a value of 'London','Berlin','Rome'

If you want to access the caption(s) of the item(s) selected, instead of or in addition to their values, set the **List Captions Element ID** attribute to the ID of an Input Hidden element. The caption(s) will be placed in this element when the report is submitted and will be available using a @Request token with the same ID. Gettings multiple captions is dependent on setting the Multiple
Selections attribute = *True*.

If you're using Input Check Box List to show a hierarchical list of items, its @Request token will contain the value for the lowest checked item in a branch, but the values of the other checked items above it in the branch are not available in the same way.

Default values for an Input Check Box List element with multiple selections can be provided using a child **Default Values** element. The default values are retrieved by a child datalayer beneath the Default Values element. If a Default Values element is present, then the Input Check Box List's default value attribute is ignored.

## More Information

For additional information, see the Element Reference entry for [Input Check Box List](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2600&iName=Inputcheck%20boxList&iType=Element&iLabel=Input+check%20box+List&lnkpg=0).
