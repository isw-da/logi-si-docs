---
title: "Using the Layout Editor"
id: 4419715436567
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715436567-Using-the-Layout-Editor
updated_at: 2022-07-17T01:40:10Z
---

# Using the Layout Editor

# Using the Layout Editor

To begin using the Layout editor, click the Layout tab at the bottom of the Workspace panel. The Layout editor displays the report definition as it appears in a browser window.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707022615/positionele_06.png)

Selecting certain types of objects in the layout encloses that object in a green outline, as shown above, with one or more "grab points". The table object shown above provides three types of grab points:

> 1. Click and drag here to reposition the entire table.
> 2. Click and drag here to resize the object horizontally (in this case, each table column can be resized).
> 3. Click and drag here to resize the object vertically.

The Layout editor also provides additional functionality beyond absolute positioning and resizing:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699863447/positionele_07.png)

A selected object can be right-clicked to view its context menu, as shown above. Options here allow the following operations:

* Move the selected element in front of or behind other elements
* Set the text for Caption attributes
* Apply style sheet classes
* Locate hard-to-find elements by name
* Return the report to Flow Positioning

Menu options are dynamic and will change depending on the nature of the selected element.

## Overlaying Elements

Absolute positioning provides a method of allowing one object to overlay another. This gives you the ability, for example, to create a foreground and a background for report definitions.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699863703/positionele_08.png)

To overlay objects:

1. Position two objects such that one overlaps the other.
2. Select the overlaying (top) object, right-click it, and select **Bring to Front** from the popup menu.

The same results can be achieved with Flow positioning by using the CSS *position: absolute* property and value combination.
