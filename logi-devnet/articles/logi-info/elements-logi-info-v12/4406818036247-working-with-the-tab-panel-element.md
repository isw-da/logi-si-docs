---
title: "Working with the Tab Panel Element"
id: 4406818036247
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818036247-Working-with-the-Tab-Panel-Element
updated_at: 2022-04-06T06:09:48Z
---

# Working with the Tab Panel Element

# Working with the Tab Panel Element

The **Tab Panel** elements are the visible component of tabbed panels and include the little tab that users click to change panels and the area that's displayed when they do so.

The attributes of the Tab Panel element are:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique element identifier. |
| Caption | (Required) Specifies the text that will appear on the little tab that a user clicks (the selection tab) to change panels. This text appears as a link and, like all links, its appearance can be controlled using style sheet classes. If your caption seems too long, consider using an abbreviation and putting longer text into a Tooltip. |
| Class | Specifies the style sheet class to apply to the tab panel.  Classes are applied to the text in the selection tab link *and* to elements that appear within the Tab Panel, such as labels. For example, padding applied using classes will affect *both* the Caption text and elements in the Tab Panel. To isolate elements in the panel from the Caption text, consider adding a Division element within the panel, moving the panel contents within it, and then applying a class to it. |
| Security Right ID | Controls access to this element using Logi Security. Provide the ID of a Right defined in the application's \_settings definition and only users that have a Role referenced in the Right will be able to see the element. Multiple Right IDs, separated by commas, may be entered. |
| Show Modes | Specifies whether the tab panel is visible or hidden. This attribute can be used to dynamically increase or reduce the number of tabs available for selection, based on runtime criteria. With this attribute set to an arbitrary string, such as "showMyPanel", you can control panel visibility by manipulating the *rdShowModes* request variable. For example, if you create a Default Request Parameter named rdShowModes and give it a value of showMyPanel, the panel will be displayed. If the value is something else, it will be hidden. Similarly, if instead you pass a request parameter named rdShowModes when calling or refreshing the report, its value will determine whether the tab panel is displayed. |
| Tooltip | Specifies text that appears when the mouse is **hovered** over a tab.   If this attribute is left blank, the word "active" will appear as a default tooltip. |

## Changing Tab Panel Content Dynamically

This next example illustrates two more important ideas about working with Tabs. The first is that embedded subreports can be placed into tab panels, allowing you to develop panel contents as independent reports first, before integrating them into your tab panel. This can make debugging and report polishing much easier.

The second is that tab panel contents, through the use of **Division** elements, can be dynamic. By showing and hiding divisions, based on request variables, one tab panel can have multiple uses.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583646615/tabpanels_06.png)

Suppose we want a tab panel to show a data table and then be able to edit the data for a single row in that table, using a data entry form, in the same tab panel, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575470359/tabpanels_07.png)

To achieve this, we'll begin by placing two Division elements in the Tab Panel "pnlSuppliers", as shown above. The first division contains the elements that display the data table of supplier information. A column in this table, such as a SupplierID, is a link that refreshes the report, passing both the Supplier ID value and a variable indicating whether we're in "View" or "Edit" mode. This "mode" request variable is used in the divisions' Condition attribute
to determine which division will be displayed.

The second division, as shown above, uses a **SubReport** element, in *Embedded* mode, to include a separate definition which contains the data entry form. The **Link Parameters** element is used to pass the request variable containing the Supplier ID to the subreport, so it knows which supplier record to look up and present in the data entry form.

Did you follow all that? It depends entirely on the fact that reports can call themselves ("refresh" themselves) and also pass request variables to the refreshed report in the process.

In summary, tabbed panels provide a useful, well-recognized, and convenient mechanism for arranging and displaying data without using separate report pages, and Logi Info provides an easy way to implement them.
