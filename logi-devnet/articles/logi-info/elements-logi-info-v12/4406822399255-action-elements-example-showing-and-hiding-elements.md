---
title: "Action Elements Example: Showing and Hiding Elements"
id: 4406822399255
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822399255-Action-Elements-Example-Showing-and-Hiding-Elements
updated_at: 2022-04-06T06:07:00Z
---

# Action Elements Example: Showing and Hiding Elements

# Action Elements Example: Showing and Hiding Elements

The **Action.Show Element** element allows you to dynamically change part of your web page when the user clicks on a link, image, or button, using *Show Modes*. This is very useful for revealing and hiding page sections, best defined by "container" elements such as HTML Rows or the **Division** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583866519/introacts_08.png)

Here's how to use this element to show and hide other elements:

1. We begin by determining which elements we want to show and hide. In the example above, we've added two Division elements in order to control the visibility of their Chart Canvas child elements.
2. Label links, one for each Division, have been added with **Action.Show Element** elements beneath them. At runtime, these will initiate the showing and hiding of our divisions.
3. Next, set the Action.Show Element element's **Element ID** attribute values to the element IDs of the Divisions.
4. Leave the **Display** attribute blank; its default setting is *Toggle*, so alternate mouse clicks will show and then hide the Divisions.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583866775/introacts_09.png)

5. Finally, we need to set the **Show Modes** attribute for the elements being shown and hidden, as shown above. We want the division be hidden initially, so we set the attribute value to *None*.

This example will display two links when run. When either link is clicked, their respective division will be displayed. Another click, and they'll be hidden. Neither division is dependent on the other, so any combination of shown and hidden is possible.
Here's another use case: one link that *alternates* which divisionis visible:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583867287/introacts_10.png)

As shown above, this is accomplished by placing the IDs of *both* of the elements to be shown/hidden in the **Element ID** attribute of a single Action.Show Element element, separated by a comma. Change the **Show Modes** attribute value of one of the two Divisions to *All* so that it will initially be visible. Any number of elements can be included this way.
Finally, it also possible to specify which action, Show or Hide, to apply to each Division independently:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583867543/introacts_11.png)

As shown above, by adding *:Show* or *:Hide* after the element ID you can independently assign the desired action to each element. This is often useful in a menu-type situation.
More examples of Show Modes in action are available in [Show Modes](https://devnet.logianalytics.com/hc/en-us/articles/4406818147095-Show-Modes).
