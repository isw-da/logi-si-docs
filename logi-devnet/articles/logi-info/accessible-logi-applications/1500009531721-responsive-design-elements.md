---
title: "Responsive Design Elements"
id: 1500009531721
section: "Accessible Logi Applications"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531721-Responsive-Design-Elements
updated_at: 2022-03-25T19:20:32Z
---

# Responsive Design Elements

# Responsive Design Elements

This topic discusses use of the Responsive Design elements, which provide a dynamic layout and visibility mechanism for Logi reports on a variety of devices.

* About Responsive Design
* [Use Responsive Rows and Columns](#Columns)
* [Use Responsive Visibility](#Visibility)

## About Responsive Design

Responsive web design has the goal of creating pages that provide an optimal viewing
experience, including easy reading and navigation with a minimum of resizing,
panning, and scrolling, across a wide range of devices (from mobile
phones to desktop computer monitors).

In a Logi application, this is accomplished using Responsive Design elements, introduced in v11.4.046. They dynamically adapt the report layout to the viewing environment by using fluid, proportion-based grids and controlled visibility. When these elements are used, viewport sizes are automatically determined using CSS3 media queries and are standardized in Logi apps as the following:

|  |  |  |
| --- | --- | --- |
| **Device** | **Width** | **Attribute Name** |
| Extra small devices: phones | < 768 pixels | Extra Small Screen |
| Small devices: tablets | ≥ 768 pixels | Small Screen |
| Medium devices: desktops | ≥ 992 pixels | Medium Screen |
| Large devices: desktops | ≥ 1200 pixels | Large Screen |

## Use Responsive Rows and Columns

Logi applications have long had Rows, Row, and Column Cell elements available for construction of an HTML table object as a container for content. The **Response Row** and **Responsive Column** elements provide similar functionality but also dynamically resize to accommodate viewport sizes.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771625751/respdesign_01.png)

The **Responsive Row** element adds a "fluid grid" to the report page, as shown above, which fills 100% of the width of its parent element. The grid consists of 12 columns. This is similar to grids found in the Bootstrap and Foundation frameworks.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778521879/respdesign_02.png)

The **Responsive Column** element is a child of Responsive Row and is the container for column contents. Developers can configure how many grid columns each Responsive Column will span for each viewport size (or whether it will be displayed at all). In the example shown above, there are three Responsive Columns and, for the Large Screen viewport, they span two, five, and five Responsive Row grid columns.

Normally these two elements are transparent, without borders or background color, though they can be styled.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778522135/respdesign_03.png)

In the example above, we see how content fits into the Responsive Column elements and how they span the grid in a Large Screen viewport.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771626007/respdesign_04.png)

Notice what happens when the viewport width is changed to a Medium Screen size: the Responsive Row grid columns get proportionally smaller, as shown above. Responsive Column elements can be configured by the developer to react when the viewport window gets smaller, too. In this case, the first column is no longer visible at all and the other two now span six Responsive Row grid columns each.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771626263/respdesign_05.png)

And, finally, as the viewports gets even smaller, the Responsive Column elements can be configured to span *all* the Responsive Row grid columns, as shown above, producing a "stacked" appearance.

### Implementation

Here's an example showing how the elements discussed above are used:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771626519/respdesign_06.png)

The **Responsive Row** element can be the child of a variety of other elements. In the example above, it's been added directly beneath the Body element. It has no required attributes.

However, take note its **Collision Behavior** attribute. Responsive Row content works best when it dynamically shrinks and grows to fit
the column width. Normally, report developers should give
Responsive Column elements enough width so that the content fits. But there are times when, as the viewport gets smaller, content
just can't shrink enough to fit. For example, a data table can only become so small or
an image may have a fixed width. The Collision Behavior attribute specifies what to do when Responsive Columns "collide" in different viewport sizes because their contents can't
shrink appropriately. Attribute value options include

* *HorizontalScrollbar* - (the default) displays a horizontal scroll-bar and some of the content
  is out of view.
* *Wrap* - moves the Responsive Column down to the next
  row.
* *Overlap* - makes the contents overlap each other.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771626775/respdesign_07.png)

Next, you need to add one or more **Responsive Column** elements to the definition. It has no required attributes.

Its **Colspan** attributes are used to specify how many Responsive Row grid columns each Responsive Column should span, for each viewport size. With a value of *12,* the Responsive Column will span the entire grid, while a value of *0* will cause it to be hidden. In the example above, this column will only be visible for Large Screens, where it will span two grid columns.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  If you specify a value for a larger viewport size, make sure you also specify values for smaller viewport sizes or you may get a surprise when a smaller viewport is used.

If more than 12 Responsive Column elements are used, they'll be wrapped into another row below the first 12 elements when displayed.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771627031/respdesign_08.png)

Another Responsive Column element example is shown above. Its Colspan attributes are set to produce the behavior seen in the examples at the beginning of this section.

## Responsive Visibility

The **Responsive Visibility** element can be the child of a variety of other elements and, as its name implies, it controls their visibility. Developers can use its attributes to specify which viewport sizes cause the parent element to be hidden from view.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771630743/respdesign_09_690x705.png)

In the example above, Data Table Columns elements have been given child Responsive Visibility elements and, as the browser window gets progressively smaller, additional data table columns are hidden.

### Implementation

Here's an example showing how the element discussed above is used:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778522391/respdesign_10.png)

In the example shown above, a **Responsive Visibility** element has been added as a child of a Data Layer Column element. Its attributes are set as shown. The column will not be displayed for Small Screen size viewports.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778522647/respdesign_11.png)

Now we've added more data table columns and another **Responsive Visibility** element. Note that if you decide to hide an element at a larger viewport size, you will most likely also want to hide it at smaller sizes, otherwise it will disappear then reappear for progressively smaller viewports.
