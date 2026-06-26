---
title: "Group Min/Max Filters"
id: 5281549738775
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281549738775-Group-Min-Max-Filters
updated_at: 2022-05-03T22:09:20Z
---

# Group Min/Max Filters

# Group Min/Max Filters

**Group Min/Max Filters** cause the report output to display detail containing either the highest/latest or lowest/earliest values in a field for either one group, multiple groups, or an entire data set.

This tool is especially useful if interested in viewing the highest or lowest values, such as the most recent hire date or highest revenue figure, in a given set. Group Min/Max filters are compatible with standard filters, and there is no limit to the number of group filters that can be defined.  
To add a Group Min/Max Filter to a report:

1. Open the **Filters** dialog then, click the **Group Min/Max** tab. To open the dialog:
   * *(v2021.1+)* Click the **Filters** ![funnel](https://devnet.logianalytics.com/hc/article_attachments/5432253309335/filtermenu.png) icon on the toolbar
   * *(pre-v2021.1)* From the **Report Settings ![report-settings-menu.png](https://devnet.logianalytics.com/hc/article_attachments/5432394966167/report-settings-menu.png)**menu, click **Filters**.
2. Add a data field to filter by, called the **Filter Field** by first selecting a Data Object from the dropdown, and then either:
   * clicking the arrow icon to the right of the data field’s name
   * clicking the ![+](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Add** button at the bottom of the data field’s tree
   * double-clicking on the field’s name
   * drag-and-dropping the data object from the tree to the Filter By panel
3. From the **Minimum** dropdown, choose either *Minimum* to see the smallest or earliest values, or *Maximum* to see the largest or latest values.
4. From the **For Each** dropdown, choose the data set to group the minimums or maximums by. Choose *Entire Data Set* to show the minimum or maximum of the entire data set, or a data object or sort field to show the minimum or maximum of a group. See details in the sections below
5. If necessary, change the order of the filters by either:
   * clicking the **Move Item Up ![MoveGridRowUp.png](https://devnet.logianalytics.com/hc/article_attachments/5432225168663/movegridrowup.png)**or **Move Item Down** ![MoveGridRowDown.png](https://devnet.logianalytics.com/hc/article_attachments/5432338912791/movegridrowdown.png) icons
   * click and drag the **Grip** ![DragGrip.png](https://devnet.logianalytics.com/hc/article_attachments/5432389235351/draggrip.png) icon to move the filter to the desired location

Like standard filters, multiple **Group Min/Max Filter Fields** may be added. Subsequent filter fields will further filter the report in the event of a tie.  
Consider a report that lists the orders placed by customers grouped by the employee that took the order. The report design may look like this:

![NSBCys01TH.png](https://devnet.logianalytics.com/hc/article_attachments/5432322122007/nsbcys01th.png)

Figure 1 — Report Designer layout of the example report used in this section

In the Report Viewer, this report looks like this:

![YhXVrijKgs.png](https://devnet.logianalytics.com/hc/article_attachments/5432381907735/yhxvrijkgs.png)

Figure 2 — Report Viewer view of the above example report

This report will be used in each of the following examples

### Entire Data Set

The most basic usage of a **Group Min/Max Filter** is to limit the whole report to a singe record, representing either the minimum or maximum value for entire data set. To do this, at step 4 above choose *Entire Data Set*.  
Setting a Group Maximum Filter on the example report’s `OrderDetails.Quantity` field will reduce it to one record with the line item with the largest quantity of a single product out of all of the orders for all of the salespeople.

![GgYizlGeWw.png](https://devnet.logianalytics.com/hc/article_attachments/5432412670231/ggyizlgeww.png)

Figure 3 — The Report Filters dialog for the Entire Data Set Group Min/Max Filter

![aEY46lA50x.png](https://devnet.logianalytics.com/hc/article_attachments/5432322213143/aey46la50x.png)

Figure 4 — The resulting output after applying the Entire Data Set Group Min/Max Filter on the report from Figure 1

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> To see more than one maximum or minimum for a data set, use a Top/Bottom filter instead.

### Min/Max for each Group

Another common usage for **Group Min/Max Filters** is to see the min or max value for each instance of a group.

To do this:

1. Add a sort on the field to do the min/max grouping on. Since sorts are implicit groups, adding a Group section is optional.
2. At step 4 above, choose the sort field from the dropdown.

![dYqBl24ZyJ.png](https://devnet.logianalytics.com/hc/article_attachments/5432412834583/dyqbl24zyj.png)

Figure 5 — Report Filters dialog when filtering with a group

Since the customers are grouped by employee, the resulting report output will show the product with the highest quantity ordered by each customer handled by each employee.

![n3HCMcMGXM.png](https://devnet.logianalytics.com/hc/article_attachments/5432412893719/n3hcmcmgxm.png)

Figure 6 — Showing the products with the largest quantity on an order for each customer and each employee

To show the highest quantity ordered by each customer regardless of who placed the order, check the **Ignore other groupings on report** checkbox in the Report Filters dialog. In other words, show the largest product quantity ignoring the Employees group.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If applying a Group Min/Max filter to an outer group, then checking the Ignore other groupings checkbox has no effect on the report output because the outermost group takes precedence anyway. If applying a Group Min/Max filter to an inner group, however, the button takes effect.

![B56NW4uJPq.png](https://devnet.logianalytics.com/hc/article_attachments/5432412944023/b56nw4ujpq.png)

Figure 7 — Report Filters dialog when filtering with a group while ignoring other groups

Notice that Bon app’ (BONAP) appears only once in Figure 8 in contrast with Figure 6. Due to the fact that BONAP’s order of Spegesild from Robert King is greater than its order of Pavolova from Steven Buchanan, BONAP appears only once on the report. If BONAP had ordered the same quantity from both Buchanan and King, it would appear under both names, even with the **Ignore other groupings checkbox** checked.

![UxuXI2rUkx.png](https://devnet.logianalytics.com/hc/article_attachments/5432365464215/uxuxi2rukx.png)

Figure 8 — Showing the products with the largest quantity on an order for each customer regardless of the employee that placed it
