---
title: "Basic Training 7. CrossTab Reports"
id: 5281633248791
section: "User Video Training Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281633248791-Basic-Training-7-CrossTab-Reports
updated_at: 2022-05-03T22:07:34Z
---

# Basic Training 7. CrossTab Reports

# Basic Training 7. CrossTab Reports

[Previous: Formulas](https://devnet.logianalytics.com/hc/en-us/articles/5281640504087-Basic-Training-6-Formulas)

[Next: Charts](https://devnet.logianalytics.com/hc/en-us/articles/5281663516183-Basic-Training-8-Charts)

## Transcript

Welcome back to the Exago Video Training Series! Today we’ll be creating a new CrossTab report, which will allow us to expand our data vertically and horizontally.

To begin, let’s select ‘CrossTab Report’ from our list of available report types. We can see this opens the CrossTab wizard, which may look familiar to the advanced report wizard we saw earlier on. We’ll give it a name and a folder to live in, and we have the option to include a description here.

Clicking next  opens the categories tab, where we decide what data will be available to us on the report. We’d like to see various product sales over time, so let’s add Categories, Products, Order Detail, and Orders. We’ll hit next again, and for now we won’t include any filters on this report. Hitting next one more time, we’ll come to the layout tab.

We can see data fields on the left, and on the right is where we’ll begin to construct the CrossTab. Our CrossTab can expand in both the X and Y direction. Our row header source is where we define how we’ll expand vertically. Since we want to see product sales, let’s populate the rows of our CrossTab with product names. Notice the interactive preview below begins to populate with dummy values so I have an idea of what the final output will be.

Now I may want to see products grouped by their respective categories. To do so, I’ll add category name to the row header source, and use the arrows on the right to make it my highest level of grouping for my rows.

Next we have our column header source, where we choose how our data will expand horizontally. I’d like to show product sales for each month, as well as for each year. We have access to the order date field, and if we recall from our formulas discussion, we can use date functions to get the month and year from those dates. First we’ll add order date to our column headers, and then we’ll click the F of X icon here. This opens our formula editor, and here we’ll wrap our order date in the month() function. Now we’ll show one column for each month. Looking at our preview below, we can see the label for these columns still says order date. By selecting the paper icon here, we have the ability to change that label to say ‘month’. We can also change how the column will be sorted, and since we know these columns will show month numbers, let’s set the sort to be numeric.

We have our months being displayed, but let’s add the year above the months as well. We’ll first add our order date field again, navigate to our formula editor, and this time use the year() function. We’ll again change the label to say ‘year’, and modify the sort order to be numeric. Last, we’ll push this row up one, so the years appear above their respective months.

Next we need a field for our tabulation, or the intersection between our rows and columns. I’ll add my revenue field, and selecting the paper icon, we’ll ensure we’re summing the revenue here.

To add some totals to the CrossTab, we can select our options icon, and add grand totals for both our rows and columns here. In order to add intermediate totals for each year, I can select my year options, and set the yearly total to display here. I can do the same for my category totals as well.

To give our CrossTab some aesthetic appeal, we can apply a theme using the dropdown here. At this point we can hit finish to exit the CrossTab wizard. Should we need to go back in and make any changes, we can do so by double clicking the CrossTab here.

When executed, CrossTabs will attempt to reformat to fit into single page PDF format by default. Navigating into our report options cogwheel, and digging into our report viewer options, we can uncheck ‘simulate pdf’, which will ensure our CrossTab has enough room when exporting to Html.

Executing this report, we can see our categories and their respective products populating our rows, and the months for each year for our columns. In our tabulation we can see the revenue generated for any product by month. We can also see sub totals for categories and years, as well as grand totals along the bottom and right hand side.

This concludes our discussion on CrossTabs. Be sure to check out our segments on charting and Dashboards, and as always, Happy Reporting!
