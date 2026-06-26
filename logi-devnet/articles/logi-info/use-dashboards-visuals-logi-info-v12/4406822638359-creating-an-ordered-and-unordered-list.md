---
title: "Creating an Ordered and Unordered List"
id: 4406822638359
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822638359-Creating-an-Ordered-and-Unordered-List
updated_at: 2022-04-06T06:10:14Z
---

# Creating an Ordered and Unordered List

# Creating an Ordered and Unordered List

To add an ordered or unordered list to a report definition, start by adding a **Data List** element:

![](https://devnet.logianalytics.com/hc/article_attachments/4417562956823/datalist_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417575429399/datalist_01a.png)

The Data List element is included in the **Data Tables** folder of the Element Toolbox and context menus. As shown in the example above, it uses a datalayer element to retrieve its data. The Data List element's **Ordered** attribute determines whether the list is ordered (numbered) or unordered (bulleted).

![](https://devnet.logianalytics.com/hc/article_attachments/4417575429783/datalist_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417575429911/datalist_02a.png)

A single **List Item** element is used beneath the Data List element as a container for the list items, as shown above. Multiple List Item elements *may* be used but they are not necessary; using more than one can will result in interwoven lists of items.

The element's **Class** attribute can be set, if desired, to one of the Theme-related Data List classes, which are discussed in [Using the Data List with a Theme](https://devnet.logianalytics.com/hc/en-us/articles/4406822640279-Using-the-Data-List-with-a-Theme). If the attribute is left blank, an unordered list will be shown with black bullets and an ordered
list will be shown with decimal numbers.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575430295/datalist_02b.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417575430423/datalist_02c.png)

Finally, an element is added beneath the List Item to show or represent the data. This can be a **Label**, as shown above, or an Image or other elements, or several elements. The usual @Data tokens are used to reference data for display and additional style classes can be assigned.
