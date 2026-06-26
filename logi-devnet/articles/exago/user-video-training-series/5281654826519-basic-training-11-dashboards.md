---
title: "Basic Training 11. Dashboards"
id: 5281654826519
section: "User Video Training Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281654826519-Basic-Training-11-Dashboards
updated_at: 2022-05-03T22:07:38Z
---

# Basic Training 11. Dashboards

# Basic Training 11. Dashboards

There have been several iterations of the Dashboard Designer and Dashboard Viewer tools in the application.

## *v2019.2+*

[Previous: Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/5281648635543-Basic-Training-10-Conditional-Formatting)

[Next: Dashboard Visualizations](https://devnet.logianalytics.com/hc/en-us/articles/5281654851735-Basic-Training-11a-Dashboard-Visualizations)

### Transcript

Welcome back to the Exago video training series! This segment will focus on Dashboards, an interactive way to display reports, visualizations and more all in one place.

We’ll begin by clicking the Create New Report icon in the top left corner and then clicking on Dashboard to open the Dashboard Designer. The Dashboard Designer is comprised of three main sections: the Toolbar, the Canvas, and the Tile Properties Pane.

Each element on a Dashboard is contained within a rectangular tile that can be dragged and placed onto the canvas. Tiles are arranged onto a grid and snap into place next to each other.

The top of the Dashboard Designer contains the Toolbar with tools for creating and interacting with the canvas and the tiles. General formatting settings such as default tile background and border colors or canvas resizing options are available in the Canvas Format menu in the toolbar.

On the right side of the screen is the Tile Properties Pane where the look, feel and behavior of individual tiles can be changed as we build our Dashboard.

We’ll begin building our Dashboard by going to the Toolbar and dragging the New Tile icon on to the canvas. This creates a new tile placeholder that can resize and move around the canvas. This new tile can populate with a graphical visualization, a web page, an image, a static text box, an interactive filter or a pre-existing report.

For this Dashboard, we’d like to display various employee’s revenue totals as well as a count of their respective orders. We’d also like to be able to filter which specific employee’s information is displayed and what year the orders were placed.

I have an existing report that shows revenue per employee in a chart, so I’ll click Existing Report on the new tile placeholder and then drag the desired report from the Report Tree on the left side of the screen. We’re now displaying employee revenue totals but we’d also like to see an order count for each employee. As I don’t already have a report with this information on it, I can now add a new visualization tile and build the chart right here in the Dashboard Designer. To do this, we can add another New Tile to the canvas. This time by clicking on the New Tile icon in the toolbar and then dragging the Visualization tile type to the canvas.

We’ll see we’re prompted to add Groups and Values to the tile. All visualization tiles start off as Column charts, but we can easily change to a different type by clicking on the corresponding chart type icon in the Tile Properties Pane.

We can now start adding data to the visualization. Using the Data Fields pane on the left side of the screen, we can click through to find the fields we want, or use the search field at the top. We’ll first add the Employee Last Name field as a Group. Next, we’ll add OrderID as the Values in the chart. If we’d like to use a different type of aggregation, we can set that on a field-by-field basis here. We can modify how the visualization appears using the Style tab of the Tile Properties Pane. Finally, let’s resize the visualization tile so it fits nice next to our first report tile.

Now that our Employee Revenue report and our Order Count visualization are completed we still need to add interactive filters so we can modify which employee’s information and order date are displayed. Let’s dock the employee name filter in the Filter Pane and we’ll create a slider on the canvas to adjust the order date.

First, we’ll click on the Filters menu in the Toolbar and then click the Add Filter button. Next, I’ll select the field to filter on, in this case Employee’s Last Name. I’ll set my Operator to be Is One Of so we can select multiple employees. Next, we can specify which tiles we’d like the filter to affect. For this Dashboard, we’ll select both the Employee Revenue chart and our visualization of employee order count.

Notice that when the mouse is hovered over the tile name the tile is highlighted in blue. We can also set default values for the filter here.

We will repeat this process for the Order Date filter. This time, select Order Date as the Filter Field, Is Between as the Operator and apply it to both tiles by checking their check boxes.

In our example, the Order Date field contains the month, day and year of each order. But we’re only interested in filtering by year. We can use a formula to select the year information. To do this, we’ll click on the Formula Editor icon to open the Formula Editor. Here we can enter a formula directly or use the built-in functions to build one. We can use the Year() function to select only the year portion of each order date. In the Formula Editor we can navigate to the Date category, or we can search for it with the Search field at the top of the dialog. Double-clicking the function in the list adds it to the formula. The Formula Editor automatically applies the function to our data field.

This time, I will drag the filter item to the canvas and we’ll see a new tile appears with a slider in it. Again, we can use the Tile Properties Pane to set styling and behavior for the tile.

At this point we can save our Dashboard by hitting the Save icon and giving it a name, a folder and an optional description.

Once the Dashboard is saved, we can click Run and the Dashboard will execute and launch us into the Dashboard Viewer.

We can now see both our existing employee revenue chart and the employee order count visualization. The Dashboard Viewer is an interactive space that allows us to view and work with the Dashboard we just built. On the left side of the screen are the floating icons — refresh and filters. If reports on our Dashboard also included Parameters, an additional Parameters icon would appear here. Clicking the Refreshing icon will reload the data for all the reports and visualizations on the canvas.

If we click on the floating Filters icon, the Filter Pane will open and show our docked Employee Name filter. We can modify which employees we’re showing information for, and our tiles will automatically update to reflect those newly selected values. The Parameters pane would work in a similar way.

We can slide the Year filter on the canvas as well.

Hovering the mouse over either the docked or canvas filter will highlight the tiles the filter affects. In our case, both filters affect both tiles.

From each tile’s individual Tile Menu, they can manually Refresh either of our charts, or export them to any of Exago’s available export types. We even have the ability to drill down into the detail of any visualization simply by clicking on specific series.

We’ve just begun to scratch the surface of what we can accomplish with Exago’s Dashboard tools. For more information about building Dashboards, check out the Dashboard Design Cheat Sheet and The Dashboard Design Handbook for SaaS Companies available online at exagoinc.com/learn/library

The Dashboard Designer is a very powerful application and you’ll soon be creating meaningful and attractive Dashboards just like these in no time.

This concludes our segment on Dashboards. Be sure to check our other segments in the Video Training Series if you haven’t already and as always, happy reporting!

## *v2017.2* – *v2019.1*

### Transcript

Welcome back to the Exago Video Training Series! This segment will focus on Dashboards, an interactive way to display reports, visualizations, and more all on the same page.

We’ll begin by hitting the new report icon, and selecting Dashboard. This opens our Dashboard canvas, and we’ll begin by dragging a new tile onto our Dashboard. Our fit options will dictate how much of our Dashboard the tile takes up when the Dashboard is executed. Once the tile is on the canvas, we can manually resize the tile as well. This new tile can populate with a new visualization that we build on the fly, a web page via URL, an image, a static text box, an interactive filter, or a pre-existing report.

For this Dashboard, we’d like to display various employee’s revenue totals, as well as a count of their respective orders. We’d also like to be able to filter which specific employee’s information is displayed. We have an existing report that shows revenue per employee in a chart, so I’ll select ‘Existing Report’ on the new tile here, and then drag the desired report from the actual report tree.

In the top right, we’ll see we can delete or duplicate a tile, or expand the tile to encompass the entire Dashboard. We can also refresh the report manually, and even directly open the report designer if we’d like to modify the report’s structure.

We’re now displaying employee revenue totals, but we’d also like to see an order count for each employee as well. As this isn’t a report we have previously created, we can now add a new visualization to build this chart out on the fly. We’ll see we’re prompted to add values and labels to the visualization, and we can do so by selecting fields from the data fields pane on the left hand side. We can click through to find the fields we want, or use our search bar. When searching, we also have the ability to filter our results to only show text, numeric, date/time, or other fields. We’ll first add the employee last name field as a label. Next, we’ll add order ID as a value to count. We can switch to a tabular view using the icon on the bottom right, and if we’d like to use a different type of aggregation we can set that on a field by field basis here. Clicking back to our chart display, we can modify how the visualization appears in our style menu, and modify the actual data being displayed as needed in the data menu. Finally, let’s resize the visualization, so it fits nice next to our first tile.

Our employee revenue report and our order count visualization are completed, but we still need to add an interactive filter so we can modify which employee’s information is displayed. On the Dashboard output we have two options for filters. We can choose to display an interactive filter directly on the canvas, or a docked filter that can be opened or closed. Dragging over a new tile will create a filter to be displayed on the canvas, however I think I’d prefer to just display my charts on the output, so in this case we can add a docked filter instead.  Next, I’ll select the field to filter on, in this case employee last name. I’ll set my operator to be ‘is one of’ so we can select multiple employees. Next we can specify which reports or visualizations we’d like the filter to control. For this Dashboard, we’ll select both the employee revenue chart, and our visualization of employee order counts. We can also set default values for this filter here if we’d like.

At this point, we can save our Dashboard by hitting the save icon and giving it a name, a folder to live in, and an optional description. Once the Dashboard is saved, we can hit run Dashboard to execute.

We can now see both our visualization and chart, along with our docked multi select filter. We can modify which employees we’re showing information for, and our charts will automatically update to reflect the newly selected values. We can manually refresh either of our charts, or export them to any of Exago’s available export types. We even have the ability to drill into the detail of any visualization simply by clicking a specific series.

This concludes our segment on Dashboards. Be sure to check out some of our earlier segments if you haven’t already, and as always, Happy Reporting!

## *pre-v2017.2*

### Transcript

Welcome back to the Exago Video Training Series! This segment will focus on Dashboards, an interactive way to display reports, visualizations, and more all on the same page.

We’ll begin by hitting the new report icon, and selecting Dashboard. This opens our Dashboard canvas, where we can begin to include components from our toolbox on the left hand side. In our toolbox, we’re able to select pre-existing reports, new visualizations we can build on the fly, a static text box, an image, a web page, or an interactive filter.

For this Dashboard, we’d like to display various employee’s revenue totals, as well as a count of their respective orders. We’d also like to be able to filter the date range of the information being displayed. We have an existing report that shows revenue per employee in a chart, so I can add that to the Dashboard by clicking and dragging on the pre-existing report icon, or dragging the report from the actual report tree.

Once the report is on the canvas, we can manually resize the Dashboard item, or use the box icon here to automatically resize the item to the size of our report. We can also refresh the report manually, and even directly open the report designer if we’d like to modify the report’s structure. Navigating back to our Dashboard, we can access our report options here, and use the red x to remove the report from the Dashboard.

We’re now displaying employee revenue totals, but we’d also like to see an order count for each employee as well. As this isn’t a report we have previously created, we can now add a new visualization to build this chart out on the fly. We’ll see we’re prompted to add fields to the visualization, and we can do so by selecting fields from the data fields pane on the left hand side. We can click through to find the fields we want, or use our search bar. When searching, we also have the ability to filter our results to only show text, numeric, date/time, or other fields. We’ll first add the employee last name field, and as we click and drag, we’ll see our visualization splits, prompting us to drop into the top to begin making a chart, and the bottom to begin making a tabular display. We’ll drop this field into the top to begin creating a chart, and now we can check the ‘group by’ box, since we know we’ll be tracking a count of the orders for each employee.

Next we’ll add the Order ID field, and since we want to count the number of orders, we’ll set our dropdown here to be ‘count’. Now the visualization will display a count of the number of orders per employee. At this point, we can resize our visualization to match our pre-existing report, and we’ll notice the borders will snap together to help us easily modify our Dashboards’ display. Right clicking our visualization, we can modify the chart, so let’s swap our theme to blue grey to match the report on the left.

We now have our employee revenue report, and our visualization, but we still need to add an interactive filter so we can modify the date range of the data being displayed. We’ll click and drag to add a filter, and the first thing we have to do here is select the reports and visualizations we want the filter to control. For this Dashboard, we’ll select both the employee revenue chart, and our visualization of employee order counts. Next we’ll specify the field we’d like to filter by. The available fields are only those that belong to data categories included on controlled reports or visualizations. Because both reports use information from Employees and Orders, we have the ability to filter by any field from either of those categories.

Let’s filter by order date, and modify the type of filter of we choose to use. We can use a single or multi select, as well as a range or single slider. Since we’re filtering by a date range, let’s use the range slider. Hitting okay, we can resize the filter to have a good amount of space to populate under our charts. At this point, we can save our Dashboard by hitting the save icon and giving it a name, a folder to live in, and an optional description. Once the Dashboard is saved, we can hit run report to execute.

We can now see both our visualization and chart, along with our date range slider. We can modify the date range by clicking and dragging, and our charts will automatically update to reflect the newly selected values. We can manually refresh either our charts, or export them to any of Exago’s available export types. We even have the ability to modify how the charts are displayed directly in the viewer by right clicking here.

This concludes our segment on Dashboards. Be sure to check out some of our earlier segments if you haven’t already, and as always, Happy Reporting!
