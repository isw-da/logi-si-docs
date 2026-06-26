---
title: "Using Responsive Rows and Columns"
id: 4406817975319
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817975319-Using-Responsive-Rows-and-Columns
updated_at: 2022-04-06T06:09:24Z
---

# Using Responsive Rows and Columns

# Using Responsive Rows and Columns

Logi applications have long had Rows, Row, and Column Cell elements
available for construction of an HTML table object as a container for
content. The **Response Row** and **Responsive Column** elements
provide similar functionality but also dynamically resize to accommodate
viewport sizes.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583683863/respdesign_01_627x160.png)

The **Responsive Row** element adds a "fluid grid" to the
report page, as shown above, which fills 100% of the width of its parent
element. The grid consists of 12 columns. This is similar to grids found
in the Bootstrap and Foundation frameworks.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583683991/respdesign_02_651x199.png)

The **Responsive Column** element is a child of Responsive Row and is
the container for column contents. Developers can configure how many grid
columns each Responsive Column will span for each viewport size (or
whether it will be displayed at all). In the example shown above, there
are three Responsive Columns and, for the Large Screen viewport, they span
two, five, and five Responsive Row grid columns.
Normally these two elements are transparent, without borders or background
color, though they can be styled.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575507607/respdesign_03_591x401.png)

In the example above, we see how content fits into the Responsive Column
elements and how they span the grid in a Large Screen viewport.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575507991/respdesign_04_591x398.png)

Notice what happens when the viewport width is changed to a Medium Screen
size: the Responsive Row grid columns get proportionally smaller, as shown
above. Responsive Column elements can be configured by the developer to
react when the viewport window gets smaller, too. In this case, the first
column is no longer visible at all and the other two now span six
Responsive Row grid columns each.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583684119/respdesign_05.png)

And, finally, as the viewports gets even smaller, the Responsive Column
elements can be configured to span *all* the Responsive Row grid
columns, as shown above, producing a "stacked" appearance.

## Implementation

Here's an example showing how the elements discussed above are used:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563036439/respdesign_06_566x149.png)

The **Responsive Row** element can be the child of a variety of other
elements. In the example above, it's been added directly beneath the Body
element. It has no required attributes.

However, take note its **Collision Behavior** attribute. Responsive Row
content works best when it dynamically shrinks and grows to fit the column
width. Normally, report developers should give Responsive Column elements
enough width so that the content fits. But there are times when, as the
viewport gets smaller, content just can't shrink enough to fit. For
example, a data table can only become so small or an image may have a
fixed width. The Collision Behavior attribute specifies what to do when
Responsive Columns "collide" in different viewport sizes because
their contents can't shrink appropriately. Attribute value options include

* *HorizontalScrollbar* - (the default) displays a horizontal
  scroll-bar and some of the content is out of view.
* *Wrap* - moves the Responsive Column down to the next row.
* *Overlap* - makes the contents overlap each other.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583684503/respdesign_07_601x185.png)

Next, you need to add one or more **Responsive Column** elements to the
definition. It has no required attributes.

Its **Colspan** attributes are used to specify how many Responsive Row
grid columns each Responsive Column should span, for each viewport size.
With a value of *12,* the Responsive Column will span the entire
grid, while a value of *0* will cause it to be hidden. In the example
above, this column will only be visible for Large Screens, where it will
span two grid columns.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) If you specify a value for a larger viewport size, make sure you
also specify values for smaller viewport sizes or you may get a surprise
when a smaller viewport is used.

If more than 12 Responsive Column elements are used, they'll be wrapped
into another row below the first 12 elements when displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563036695/respdesign_08_614x229.png)

Another Responsive Column element example is shown above. Its Colspan
attributes are set to produce the behavior seen in the examples at the
beginning of this topic.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) You cannot refresh **Responsive Row** and
**Responsive Column** elements directly by specifying their IDs in an
**Action.Refresh Element** element. However, you can enclose the entire
table in a Division and refresh it, or place the Responsive Column's child
elements in a Division and refresh it.
