---
title: "Basic Training 9. Filters"
id: 5281655095319
section: "User Video Training Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281655095319-Basic-Training-9-Filters
updated_at: 2022-05-03T22:08:45Z
---

# Basic Training 9. Filters

# Basic Training 9. Filters

[Previous: Charts](https://devnet.logianalytics.com/hc/en-us/articles/5281663516183-Basic-Training-8-Charts)

[Next: Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/5281648635543-Basic-Training-10-Conditional-Formatting)

## Transcript

Welcome back to the Exago Video Training Series! Today we’ll be discussing filters in the advanced report designer, which allow us to narrow down the amount of data being displayed.

We’re currently looking at an advanced report displaying various orders grouped by company. Executing this report as is, we can see a full 36 pages of data are being returned. While this works as an all inclusive view, we can apply filters to this report to take a closer look at a specific snapshot of our data. Perhaps we’d like to see a specific company’s sales in quarter 4 of two subsequent years. Navigating back to the editor, we’ll start by clicking our report options cogwheel, and selecting ‘filters’. We now see our data fields on the left pane, and on the right is where our actual filters will live. To add a filter, we can select the appropriate data field, and click and drag it over to the right. We’d like to filter this report to show a specific company, so we’ll add our filter on company name.

As we add the filter, notice we have the ability to modify the operator in our dropdown here. The operator defines how the filter relates to the selected values, and we can see there’s a variety of options to cover all our standard use cases. For this filter, we’ll leave the operator as ‘equal to’, since we want our company name to be equal to one specific value.

The dropdown here is where we specify the value we’d like to use to filter by. We can manually key our value in, or use the dropdown to select from a list of available values. Let’s set our filter to ‘B’s Beverages’.

Next, we have to define how this filter will relate to the next filter we add to this list. AND means that both this filter and the next filter’s conditions must be satisfied, while OR means that at least one of this and the next filter’s conditions must be satisfied. We also have two checkboxes, the first of which allows to group this filter with the next filter in the list. The second box will make the filter prompt the user for a value when checked. Let’s check that box here, so that when this report is executed, we can select which company we’d like to see data for.

We currently have a filter that will allow us to only see one specific company’s data, however we’d also like to narrow our data down to quarter 4 of two subsequent years. To accomplish this we’ll add another filter on our order date field, and this time we’ll use the ‘is between’ operator. Since this is a date filter, we have the ability to add values using our calendar date picker in addition to keying in values or selecting dates from our dropdown. We can also use date filter functions which are an easy way to dynamically calculate a filter’s value.

For this filter’s values, let’s select October 1st and December 31st of 1996. Next, we’ll check ‘group with next filter’, and modify the relationship so this filter will OR with the next filter we add. We can add another filter on order date, set the operator to is between, and select October 1st and December 31st of 1997. As these two date filters are grouped together and have an OR relationship, we’ll include all data that falls in quarter 4 of 1996 and 1997. Coupling this combined date filter with our first filter on company name, our report will now show us one specific company’s orders in quarter 4 of both 1996 and 1997.

Now that our filters are created, the last step is to check our filter summary before hitting okay to apply our filters. The filter summary shows us how the filters we created relate to one another, and reading this summary aloud is a good way to verify we created our filters correctly. Here, we can see our company name is equal to ‘B’s Beverages’, and our order date is in between October 1st and December 31st of 1996 or our order date is between October 1st and December 31st of 1997. That sounds correct, so we can hit okay to apply our filters, and finally execute our report.

We can see our filter menu pops us asking us to provide a value for company name. Perhaps we’re interested in orders for ‘Around the Horn’. Hitting okay, we can see now where we had 36 pages of data, we now only have one page showing orders in quarter 4 of 1996 and 97 for ‘Around the Horn’.

This concludes our discussion on filters. Be sure to check out our segments on Dashboards, and as always, Happy Reporting!
