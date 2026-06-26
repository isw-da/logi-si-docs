---
title: "Basic Training 10. Conditional Formatting"
id: 5281648635543
section: "User Video Training Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281648635543-Basic-Training-10-Conditional-Formatting
updated_at: 2022-05-03T22:07:37Z
---

# Basic Training 10. Conditional Formatting

# Basic Training 10. Conditional Formatting

[Previous: Filters](https://devnet.logianalytics.com/hc/en-us/articles/5281655095319-Basic-Training-9-Filters)

[Next: Dashboards](https://devnet.logianalytics.com/hc/en-us/articles/5281654826519-Basic-Training-11-Dashboards)

## Transcript

Welcome back to the Exago Video Training Series! Today’s segment will focus on conditional formatting in the advanced report designer, which allows us to apply special cell formatting only if a certain condition is met.

We’re currently looking at an advanced report displaying total revenue per employee. Say we have specific sales quotas that need to be met, so if an employee’s total revenue is under $100,000, we’d like to display that value in red. We’ll first select the cell we want to apply our conditional formatting to, and then we’ll select the ‘format cells’ icon. From here, we can select ‘conditional’ to get to our conditional formatting options.

Using the ‘add’ button will create our first condition. The action determines what will be modified if our condition is met. We can modify cell foreground and background color, alter how our font is displayed, change our alignment, suppress a row or section, or add a page break. We’d like our employee’s revenue total to appear red if under $100,000, so we’ll set our action to ‘Foreground Color’.

Next, we’ll modify our attribute. Since our action is modifying the foreground color, our attribute will be where we select the color we’d like to use. Not every action has an associated attribute – if we switch our action to simply underline the cell contents, the ‘attribute’ will be grayed out, since underlining doesn’t require an attribute.

Swapping the action back to ‘foreground color’, we can key in a hex value here, or we can select the paper icon to use the color picker. Finally, we’ll select our F of X icon, and this opens the conditional formula editor. This is where we define the condition that determines whether or not we perform the associated action. The conditional formula editor is different from the standard formula editor in that we’re defining an expression, meaning our formula’s result must always be true or false. We also have this cell value icon, and selecting it will add a call to the CellValue function. This will get the value being displayed in the cell so we can use it for our comparison. We know our cell displays each employee’s revenue total, so we can check to see if that value is less than 100,000. With this conditional formula, our revenue total will appear in red if the value is less than 100,000.

We have the ability to add conditional colors to our charts as well. Double clicking on the chart in our report footer section, we can navigate to the appearance tab, and select ‘conditional colors’. We’ll start by selecting ‘add’, and select the red color we’d like to use. Next, we’ll click the F of X icon, and here we can see we’re provided with the ability to use either the data labels or data values from our chart. Highlighting either option will display the actual value in the box here, so we can see our data labels are the employee last names, and our values are the revenue sums. Let’s add the data value parameter to our conditional formula. Now, we can use the less than operator to check to see if our revenue sum is less than 100,000. If the formula is true – if an employee’s total revenue is less than 100,000 – we’ll color that bar red in our chart. Next we’ll hit okay, and execute the report.

Looking at the output, we can see each employee’s summed revenue, with values less than 100,000 appearing in red. We can see our chart’s appearance has been modified to display the corresponding bars in red as well.

This concludes our discussion on conditional formatting. Be sure to check out our segment on formulas, and as always, Happy Reporting!
