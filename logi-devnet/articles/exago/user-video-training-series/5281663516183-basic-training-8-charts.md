---
title: "Basic Training 8. Charts"
id: 5281663516183
section: "User Video Training Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281663516183-Basic-Training-8-Charts
updated_at: 2022-05-03T22:07:35Z
---

# Basic Training 8. Charts

# Basic Training 8. Charts

[Previous: CrossTabs](https://devnet.logianalytics.com/hc/en-us/articles/5281633248791-Basic-Training-7-CrossTab-Reports)

[Next: Filters](https://devnet.logianalytics.com/hc/en-us/articles/5281655095319-Basic-Training-9-Filters)

## Transcript

Welcome back to the Exago Video Training Series! In this segment we’ll discuss charting, a way to visually display the relationship between 2 or more metrics of data.

We’re currently looking at an advanced report displaying revenue summed per order, for each employee. Let’s begin by adding a chart in our group footer on employee last name that will show us that employee’s orders as well as their revenue totals. We can select the large cell we’ve created for our chart, and click our chart icon here. This opens the chart wizard, which will walk us through the chart creation process. We’ll start by selecting the type of chart we’d like to display, and in this case I’ll use the doughnut option.

Next we come to our data tab, where we define what information will be displayed in the chart. Depending on how our report is structured, we have three different data layouts we might use. ‘Cell based’ is used when pairs of cells on the report directly map to points on the chart. We’d use this layout if we wanted to display something like the minimum, maximum, and average revenue values for employee orders. ‘Column based’ is used when we have one metric for data labels, but may have more than one series we’d like to display. One example would be showing the order count and total revenue for each employee. ‘Row based’ is used when a single column on the report can provide the data values for the chart. This could be displaying revenue per employee per order.

Since we want to simply show revenue for each order, we’ll use the column based layout. We can then define our data labels to be our Order ID’s. This means our x-axis labels will populate with Order ID’s. Our series values can be our aggsum of the revenue, and so now the chart will show the total revenue for each order. If we’d like we can modify how our chart is sorted using the dropdown here.

Hitting next, we have the ability to modify our charts’ aesthetic. Let’s use the ‘blue grey’ theme, and give our chart a title so it’s clear what information is being displayed.

Hitting next again, we arrive at the size and preview tab. We can set the chart to be a specific size if we’d like, or let the chart automatically resize to fit to the cell it lives in. At this point we’ve completed our chart, so we can hit finish.

We now have a chart to show us an employees’ revenue total for each order, but we may want to see a report wide chart to show us how employee’s orders compare against one another. We’ll select the available cell in our report footer, and again open our chart wizard. This time, let’s use a stacked column chart. Moving to the data tab, this time we want to see revenue per order per employee, so we’ll want to ensure we’re using the row based chart layout.

Next we’ll select our revenue sum to be our data values. Since we want to see employees broken down by their orders, we want our data labels to the employee last names, and our series labels to be the order ID’s.

Moving to appearance, let’s again use the blue gray theme, and give our chart a title so it’s clear what information is being displayed. We can move to our size and preview tab and verify we’re fitting to cell, and then hit finish.

Executing the report, we can see a chart for each employee to show their individual order revenue totals. Jumping to the bottom of the report, we can see our employees compared against one another, with each bar chunked out by Order ID. Here in our report viewer, we have the ability to check or uncheck specific series. By right clicking, we have the ability to modify our chart on the fly, changing things like chart type, theme, legend location and sort order. We can even invert our data, which will switch our data and series labels.

This concludes our discussion on charting. Be sure to check out our segment on Dashboards, and as always, Happy Reporting!
