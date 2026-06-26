---
title: "Basic Training 11a. Dashboard Visualizations"
id: 5281654851735
section: "User Video Training Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281654851735-Basic-Training-11a-Dashboard-Visualizations
updated_at: 2022-05-03T22:07:36Z
---

# Basic Training 11a. Dashboard Visualizations

# Basic Training 11a. Dashboard Visualizations

[Previous: Dashboards](https://devnet.logianalytics.com/hc/en-us/articles/5281654826519-Basic-Training-11-Dashboards)

[Next: Exercises](https://devnet.logianalytics.com/hc/en-us/articles/5281671666967-Basic-Training-12-Practice-Exercises)

## Transcript

Welcome back to the Exago video training series! This segment will focus on Dashboard Visualizations, a quick way to build charts and tables right in the Dashboard Designer, without first creating a report in a separate Report Designer.

This video assumes you have already watched the first Video Training Series segment on Dashboards. If you haven’t done so already, stop this video and watch that one first.

In this video, we are going to build the four visualizations you see on this Dashboard. They are in order, from top to bottom and left to right: a bar chart showing the number of products ordered per category, a tabular report showing total revenue for each salesperson and a company wide total, an area chart showing the average revenue made per year, and finally a Key Performance Indicator (also known as a KPI) visualization showing company wide total revenue and sales tax paid.

I’ve already opened the Dashboard Designer and we are looking at a blank canvas that I have set some default background colors on. Exago is ready for us to begin adding tiles. The first visualization we will build is a bar chart that shows the total number of products ordered on a per category basis. The category names will be displayed on the Y axis and the product quantity along the X axis.

The tile asks us to Drag and Drop Groups and Values to the tile. Groups represent the categorization of data on the report and values represent the quantities of each of those categories. For this tile, the Category Name will be the Groups, and the sum of each Order quantities will be the Values.

Let’s first set the title for this tile by providing a name in this field at the top of the Tile Properties Pane. Once we add the title, it becomes visible in the tile. We can click this Hide Title icon to hide it if we don’t want it to be displayed. Next we can change the type of chart by clicking on the icon in the Chart Type section and choosing the type we want. We can drag fields from the Data Fields pane on the left side of the screen to the tile, or to the corresponding Inputs on the Tile Properties Pane. We can also change the aggregation type from the Tile Properties Pane. Since this chart will show a total quantity of all products ordered, the aggregation we’ll use is Sum.

The Style tab is where we can change the colors of the bars and set titles and labels on the chart. I can use this dropdown to change the way the X-axis labels are displayed. Number Format is where we can change how the numbers along the Y-axis will appear.

The Advanced tab in the Tile Properties Pane has controls for refreshing, sorting and filtering the content in the chart. We can change the Data Display Sort By box to sort the values in ascending (or descending) order.

The next visualization we’ll build on this Dashboard is a table of data showing each employee’s contribution to the company’s revenue, with a total at the bottom of the table for all employees.

Again, we’ll add a new tile to the canvas, provide a title, and change it to the Tabular visualization type in the Tile Properties Pane. In this case, the groups are our Employee’s Last Names, and the Values are the revenues from each order placed by that employee. Let’s add those fields to the tile with the Data Fields pane on the left. You can see the visualization beginning to take shape as we add the employee last name field.

Now let’s add order revenue field for the values. You’ll notice we have an entry for every single order placed by that employee. But our goal with this chart is to show the overall revenue total for the employee. To do this, we can simply check the Hide Details checkbox…and then only the summary data is displayed.

We’ll head back to the Style tab to set the theme and number formatting for this tile as well. Since these are dollar values of sales, we can check the Decimal checkbox to lock in the number of decimal places displayed, the 1000 Separator checkbox to break the place values into groups of thousands, and the Currency checkbox to put the prefix the dollar sign in front of each value. The symbols and number of decimal places can all be customized with the corresponding fields on the style tab. Our tabular visualization is looking good now!

The third visualization we’ll build on this Dashboard will be an Area chart, which is a version of a line chart, that shows the average revenue of all orders placed for each year. We’ll add a new tile, set a title for it and change it to an Area chart type and begin adding data fields. We’ll use the OrderDate field for the Groups, and an average of the Order Revenues for the values. As we did in the previous video, since we are only interested in seeing data categorized by Year, we can use the Year function in the Formula Editor to create a Formula which only return the year portion of each order’s date.

Again, we can use the Tile Properties Pane to set the theme to match the styling of the rest of the Dashboard. And it looks like some of the data in the database is incorrect. But that’s OK, as we can use the Advanced Filters button on the Tile Properties Pane Advanced tab to set a filter limiting the range of years for this chart to be 2014 and later. We’ll use the Tile Menu Refresh option to reload the data from the source and the chart will reflect our filter settings.

The final tile will have two KPIs in it. By now, you know the drill…create a new tile, provide a title and change the chart type to KPI. KPI visualizations are a little different than the others, as they don’t have Groups, only Values. We want to show the total revenue for all orders, so we’ll drag Revenue to the tile from the Data Fields pane. We’ll need to change the aggregation type since we want to sum all of the order revenue values together.

We can show more than one value in each KPI tile. For our Dashboard, we also want to show an estimated sales tax paid. We can do this by multiplying the revenue figure by a tax rate. To do this, we can use a formula on the data field. So, let’s add Revenue to the tile again. We can see that the tile now has two KPIs on it. To apply the formula to the field, click on the Formula Editor icon. Remember, we need to sum all of the order revenue rows together, so we will first apply the AggSum() function to the data field. Next, we will multiply each revenue value by our tax rate of 8%). Now, let’s enter series names here to label the KPIs. We will also want to do some number formatting on this tile as this chart shows a dollar value, similar to our tabular visualization. You’ll see that the same number formatting rules applied to the total revenue is also applied to the sales tax figure. We can use the Number Format settings to change how this KPI displays its value.

Now that is looking like a great Dashboard! But we’re not done yet! There are a few neat things we can do with our visualizations. For example we can have more than Group on a chart. Let’s revisit our bar chart. We can change this chart to show the total number pieces sold grouped by employee and then by category. To do this, I’ll add the Employee Last Name as a group, simply by dragging and dropping it to the tile. We can re-order the groups to make Last Name our primary group and then we can change the chart type to a Stacked Bar. Now we can see how much of each category each employee has orders for. On the Style tab, we can add a legend to the tile and select its location.

A bit simpler but equally as important — visualizations can easily be changed from one type to another. Our tabular visualization might look better as a Pie chart. That is easily accomplished with a few clicks in the Tile Properties Pane.

For more information about building Dashboards, check out the Dashboard Design Cheat Sheet and The Dashboard Design Handbook for SaaS Companies available online at exagoinc.com/learn/library

This concludes our segment on Dashboards. Be sure to check our other segments in the Video Training Series if you haven’t already and as always, happy reporting!
