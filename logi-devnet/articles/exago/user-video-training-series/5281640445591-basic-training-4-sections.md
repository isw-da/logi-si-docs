---
title: "Basic Training 4. Sections"
id: 5281640445591
section: "User Video Training Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281640445591-Basic-Training-4-Sections
updated_at: 2022-05-03T22:07:36Z
---

# Basic Training 4. Sections

# Basic Training 4. Sections

[Previous: Advanced Reports](https://devnet.logianalytics.com/hc/en-us/articles/5281663342871-Basic-Training-3-Advanced-Reports)

[Next: Formatting](https://devnet.logianalytics.com/hc/en-us/articles/5281663440791-Basic-Training-5-Formatting)

## Transcript

Welcome back to the Exago Video Training Series. In today’s video we’ll be discussing sections in the advanced report designer.

Sections determine how data will appear in a report. Each section can contain multiple rows, and each of those respective rows will appear as their sections dictate. Selecting any existing section will open our sections menu, and hovering our ‘add’ option will show us our available sections.

The page header and footer sections will show up at the top and bottom of each page of our report, and are commonly used to display column headers, or page numbers. The report header and footer sections will show up once at the beginning and end of our report, and are often used for titles or report wide totals.

The detail section will show one row for each row of information returned from our data source, and is most often used to see individual data values.

The next sections must always correspond with an existing sort on our report, and will be used to break up the information we choose to display in our detail. The group header section will appear once for each new value of the sorted field, and is most commonly used to label groupings of data. For example, if we grouped on a field like order month, we’d see one header for each of our 12 months, and our detail rows would be chunked out by month as well. The group footer section will again appear once for each new value of the sorted field, and is usually used to display aggregate information.

Finally we have our repeating group section, which is rarely used except under special circumstances. Be sure to check out our segment on repeating groups for more info there.

Looking at the other options in our sections menu, we can remove any section from our report. For our grouping sections, we can modify which of our sort fields we’re grouping on, as well as change their relative position. Finally we can alter our shading to give the section’s rows some color that we define.

For this report, we’d like to see each employee’s order data, and see the total revenue by employee as well. We’d also like to see a report wide total for our revenue. We’ve already got our page header that has our report title and column labels, as well as our detail with each specific row of information.

We’ll first add a group header and we’ll group on employee last names. We know this header will show up once for each unique employee last name, and will break up the detail rows according to which last name they correspond to. Let’s add the last name field to our header, and enlarge it a bit so it’s a nice clear label.

Next, let’s add a group footer. We’ll again group by the last name field, and let’s go ahead and add a simple aggregate sum calculation on our revenue field.

We’ll finally add a report footer, and we can again sum our revenue here to see the total across all employees.

Executing our report, we can now see each chunk of our detail section will be introduced by a group header with the employee’s last name as a label, and followed by a group footer that calculates the total revenue for that employee. Jumping to the last page, we can see the report total revenue here as well.

This concludes our walk through on sections. Be sure to check out our segments on formatting and formulas, and as always, Happy Reporting!
