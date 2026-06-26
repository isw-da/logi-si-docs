---
title: "Build a Chart Definition"
id: 4419715585175
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715585175-Build-a-Chart-Definition
updated_at: 2022-07-17T01:29:59Z
---

# Build a Chart Definition

# Build a Chart Definition

And now, let's build a Mobile Report that displays a chart. In the example
that follows, we'll be displaying data that can be filtered by year, and
include an **Input Select List** to allow the user to select different
years to display.

1. Once again, create a new definition duplicating the initial steps used
   for the mDefault definition or copy and alter the mDefault definition as
   described in [Build a Data Table Definition](https://devnet.logianalytics.com/hc/en-us/articles/4419723293975-Build-a-Data-Table-Definition). However,
   *no second Division* for left-alignment is necessary this time.
Make sure the name of your definition agrees with its entry in the menu
data (static or otherwise) in the mDefault definition, so tapping the
right menu item will redirect to this report.  
  
![](https://devnet.logianalytics.com/hc/article_attachments/4419714970263/workmobile_21.png)

2. To ensure that our data filtering always has a default value, add a
   **Default Request Parameters** element to the definition, and set its
   attributes as shown above.
![](https://devnet.logianalytics.com/hc/article_attachments/4419707174167/workmobile_22.png)

3. Next, add an **Input Select List** element, with datalayer and
   supporting elements, shown above, to your definition. In the example,
   we've used **Static Data Rows** to provide the years 2010-2013 in the
   select list. The list's default value will be its last selected value
   or, the first time the report is run, the value of the Default Request
   Parameter you created in the previous step.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419707174679/workmobile_23.png)
4. Next, add an **Event Handler** element beneath the Input Select List
   and set its attributes as shown above. Beneath it, add
   **Action.Report** and **Target.Report** elements. The
   Target.Report element's **Report Definition File** attribute should
   be set to the name of the current report definition, i.e.
   *mMonthlyReg* or whatever your definition is named.
![](https://devnet.logianalytics.com/hc/article_attachments/4419714971671/workmobile_24.png)

5. Add a **Chart** element, as shown above, and a datalayer to retrieve
   the data for it. Configure their attributes appropriately. The chart's
   **Height** and **Width** attributes do not have to be completely
   accurate, as we'll be automatically sizing it, but the *ratio* of
   the values you enter is relevant, as it will be preserved during the
   automatic sizing. You may care to experiment with different values later
   to get the right aspect ratio.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699992215/workmobile_25.png)

6. Add a **Condition Filter** element beneath your datalayer and set its
   attributes as shown above. This will ensure that the data displayed
   matches the selection the user makes in the Input Select List.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714972055/workmobile_26.png)

7. Now add an **Auto Sizer** element beneath the chart element, as shown
   above. There are no attributes to set for this element. It will
   automatically resize the chart to fit the available width in the mobile
   device browser window, and resize it if the device is rotated to
   landscape orientation.

8. Finally, finish up by adding a Label element as a footer, if desired, as
   you did in the mDefault definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699992599/workmobile_27.png)

Preview your definition and it should look similar to the example above.
You can click the Input Select List and select another year to see how it
works. Use your mobile device to browse to the mDefault definition, then
tap the menu to navigate to your mobile chart definition.
