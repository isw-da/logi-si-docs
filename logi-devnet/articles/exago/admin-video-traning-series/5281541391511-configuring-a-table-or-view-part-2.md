---
title: "Configuring a Table or View Part 2"
id: 5281541391511
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281541391511-Configuring-a-Table-or-View-Part-2
updated_at: 2022-05-03T22:08:29Z
---

# Configuring a Table or View Part 2

# Configuring a Table or View Part 2

This video explains how to configure column metadata for a data object in Exago. Complete the configuration of your table and view by watching this video after ‘Configuring A Table or View Part 1’.

[<< Configuring a Table or View Pt 1](https://devnet.logianalytics.com/hc/en-us/articles/5281548881175-Configuring-a-Table-or-View-Part-1) Previous Video

Next Video [Configuring a Stored Procedure Pt 1 >>](https://devnet.logianalytics.com/hc/en-us/articles/5281541282711-Configuring-a-Stored-Procedure-Part-1)

## Transcript

Welcome back to the Exago Technical Training Series! In this video, we will demonstrate configuring column metadata for a table or view previously added to the Exago configuration.

Here, we can create metadata for each column in the table by first clicking the Read Schema button, and then continue to configure each column further if we so choose. Choose the column’s data type from one of the available Exago data types. Columns may also be disabled from filtering, sorting or even visibility in the user interface with these dropdowns. Like a Data Object Alias and Description, a Column Alias and Description sets the name and description of this column as it appears to users in the front end. The Sort and Group-By Value tells Exago how to sort and group this column. We’ll show an example of this functionality in just a moment.

Additionally, we can create custom columns for this Data Object using the Add New button. Custom columns are formula columns that live in the Exago configuration and are built from an Exago formula, using database columns in a single Data Object. They appear to the end user identically to the native database columns. We need to give the custom column an ID, followed by a data type, an alias, and a value. We’ll open the Formula Editor to give the column a value of MonthName of OrderDate. Exago will sort it alphabetically, and not necessarily in chronological order. By providing a separate formula for the Sort and Group-By Value, we can tell Exago to use a function that returns the month’s ordinal number. We can press OK to save the custom column, and Apply to save the metadata changes that we’ve just made.

The final setting here is the Schema Access Type, and this is set to Metadata by default. That’s why it’s so important to generate metadata for Data Objects. We want Exago to be able to look right at the configuration file for metadata information. The alternative, reading the Data Source each time has a tendency to incur latency.

Congratulations! You’ve successfully configured column metadata for a table or view to the Exago base configuration file!
