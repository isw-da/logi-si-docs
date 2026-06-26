---
title: "Using Responsive Visibility"
id: 4406817976471
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817976471-Using-Responsive-Visibility
updated_at: 2022-04-06T06:09:22Z
---

# Using Responsive Visibility

# Using Responsive Visibility

The **Responsive Visibility** element can be the child of a variety of
other elements and, as its name implies, it controls their visibility.
Developers can use its attributes to specify which viewport sizes cause
the parent element to be hidden from view.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563035543/respdesign_09_553x565.png)

In the example above, Data Table Columns elements have been given child
Responsive Visibility elements and, as the browser window gets
progressively smaller, additional data table columns are hidden.

## Implementation

Here's an example showing how the element discussed above is used:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575507223/respdesign_10_633x281.png)

In the example shown above, a **Responsive Visibility** element has
been added as a child of a Data Layer Column element. Its attributes are
set as shown. The column will not be displayed for Small Screen size
viewports.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583683607/respdesign_11_605x316.png)

Now we've added more data table columns and another
**Responsive Visibility** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) If you decide to hide an
element at a larger viewport size, you will most likely also want to hide
it at smaller sizes, otherwise it will disappear then reappear for
progressively smaller viewports.
