---
title: "Using a SubReport with More Info Row"
id: 4419715631639
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715631639-Using-a-SubReport-with-More-Info-Row
updated_at: 2022-07-17T01:25:45Z
---

# Using a SubReport with More Info Row

# Using a SubReport with More Info Row

We've seen the elements and attributes used to place a subreport in the *body* of a main report, and now let's see how we can use a subreport to display information on demand, inside a Data Table row. In this topic, we'll see it in use with a More Info Row element and an Analysis Grid. For more information on More Info Row, see [Working with "More Info Rows"](https://devnet.logianalytics.com/hc/en-us/articles/4419715208471-Working-with-More-Info-Rows-).

![](https://devnet.logianalytics.com/hc/article_attachments/4419707232151/subreports_09.png)

The example above shows an Analysis Grid (AG) and its columns. A **More Info Row** element has been added beneath the AG and configured, as shown above, to span all of the AG columns and to be hidden, using Show Modes, by default.
By default, the width of a subreport embedded in a More Info Row will be limited by the width of the parent AG and will start under the first column of the AG. You can configured this differently by using the More Info Row element's **Span First Column** and **Span Last Column** attributes to adjust the placement of the subreport. In the example above, we're going to start the detail subreport in column 2.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707232791/subreports_10.png)

Next we need to add the trigger that will display and hide the More Info Row, by placing an **Action.Show Element** element beneath the Label element in the AG's first column, and configuring its attributes as shown.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png)

* Its **Element ID** attribute value matches the element ID given to the More Info Row element. With this in place, clicking the data value in the first AG column will cause the More Info Row to appear and disappear.
* You can't use Action.Show Element as the child of an Analysis Grid Column, so you need to use a regular **Data Table Column** to display the data that you want to use as a link. This column will therefore be unable to be selected in the AG's Formula, Filter, and other configuration panels.

Now let's create the subreport to be shown in the More Info Row:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707233047/subreports_11.png)

In a new definition, we'll create the subreport content. As you can see in the example above, it does not need Report Header or Report Footer elements, and may not need a Style element. The example uses a **Data Table** and has its own datalayer and some kind of filter element that restricts the data to a unique identifier that will be passed to the report as a Request variable.   
If we were using DataLayer.SQL, the query's SELECT statement could use the Request variable in its WHERE clause, and a filter element would not
be necessary.
The subreport can be tested independently of the rest of the application, by passing it test Request variables, to ensure that it's retrieving the correct data and displaying it properly. Now we're ready to put the subreport into the main report:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707233303/subreports_12.png)

As shown above, a **SubReport** element is added beneath the More Info Row element. Beneath it, **Target.Report** and **Link Parameters** elements are added. Their attributes are configured as shown.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The SubReport and Target.Report elements have slightly different internal names, which appear at the top of the Attributes panel.
The target report is, of course, the subreport definition that we created in previous step, and the parameter passed is the unique identifying value that the subreport
is expecting.

![](https://devnet.logianalytics.com/hc/article_attachments/4419715018647/subreports_13.png)

And, the resulting Analysis Grid should look like the one shown above, when an Order ID column value is clicked.

## Linking Datalayers

When the Logi Server Engine renders a report with a More Info Row, it runs the subreport datalayer for *each row* of the AG before it displays the AG, which could produce an undesirable delay.
If this is problematic, you may be able to avoid it: the Target.Report element has a **Link Data Layers** attribute which, when set, will cause the AG's datalayer's cached data to be used for the subreport. The subreport
then
uses a **DataLayer.Linked**
element in its definition to access the data.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) When a SubReport in *Embedded* mode is used beneath a More Info Row, any **Sort** elements used beneath individual Data Table columns and **Interactive Paging** elements in the subreport definition will be *ignored* and will not be rendered.
There are a lot of ways subreports can be used, and the Action.Show Element element can be used to make them appear/disappear in a variety of places in a report, not just within a More Info Row.
