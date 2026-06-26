---
title: "Action.Show Element Example: Show/Hide a More Info Row"
id: 4419715546135
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715546135-Action-Show-Element-Example-Show-Hide-a-More-Info-Row
updated_at: 2022-07-17T01:32:13Z
---

# Action.Show Element Example: Show/Hide a More Info Row

# Action.Show Element Example: Show/Hide a More Info Row

This example illustrates the use of the Action.Show element to show and hide a More Info Row within a Data Table. For more information, see [Data Table Rows](https://devnet.logianalytics.com/hc/en-us/articles/4419707464855-Data-Table-Rows).

![](https://devnet.logianalytics.com/hc/article_attachments/4419699947159/showelement_06.png)

In the image shown above, the Logi Scheduler Console sample application displays two scheduled tasks. The Task Name is a link that can be clicked to show detail information,

![](https://devnet.logianalytics.com/hc/article_attachments/4419714934167/showelement_07.png)

as shown above. Clicking the Task Name link again hides the detail information. This is a handy way of making lots of information available in a Data Table when you have limited horizontal space on the page or a large number of data columns. Here's how this was done:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707127319/showelement_08.png)

1. In the example report definition above, an **Action.Show** element has been added as the child of the **Label** element used to display the data in the table's Task Name column, making the data itself a link.
2. The new element's **Element ID** attribute value has been set to the name ("miTaskDetail"). This name will also be given to a More Info Row element added in the next step.
3. The **Display** attribute's default value is *Toggle*, so it has been left blank.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707127575/showelement_09.png)

4. Next, a **More Info Row** element has been added to the table, as shown above.
5. Its **ID** has been set to match the ID used in the previous step ("miTaskDetail") and its **Show Modes** attribute has been set to an arbitrary text value, *None*.

The **More Info Row Column** element can be used to closely align More Info Row columns with the columns of its parent table. When this element is used, the More Info Row element's **Span First Column** and **Span Last Column** attributes are left *blank*, and the More Info Row Column element's **Column Span** attribute is used instead to control spanning of parent table columns.

The **More Info Row** element has a **Condition** attribute, so you can conditionally include the element, for greater control over when the element can be seen, primarily when the More Info Rows are displayed by default.

Now, when run, the report will display its Data Table and clicking the Task Name will insert a row of additional detail information right below the row that was clicked, as desired. A second click will hide the detail information.
