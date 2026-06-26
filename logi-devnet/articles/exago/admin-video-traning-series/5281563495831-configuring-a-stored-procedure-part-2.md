---
title: "Configuring a Stored Procedure Part 2"
id: 5281563495831
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281563495831-Configuring-a-Stored-Procedure-Part-2
updated_at: 2022-05-03T22:08:31Z
---

# Configuring a Stored Procedure Part 2

# Configuring a Stored Procedure Part 2

This video explains how to configure parameters and column metadata for a stored procedure in Exago. Complete the configuration of your stored procedure by watching this video after ‘Configuring a Stored Procedure Part 1’ and ‘Programmable Object Settings’.

[<< Programmable Object Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281555184023-Programmable-Object-Settings) Previous Video

Next Video [Storage Management Permissioning and Setup >>](https://devnet.logianalytics.com/hc/en-us/articles/5281571962903-Storage-Management-Permissioning-and-Setup)

## Transcript

Welcome back to the Exago Technical Training Series! In previous videos, we added a stored procedure to the configuration and configured our programmable object settings. In this video, we will finish configuration for this stored procedure with additional parameters and column metadata.

If the stored procedure expects additional parameters, we are required to create them first in the Admin Console and then assign them to the stored procedure via the dropdown on the object’s menu.

Before returning to the Data Object, we’ll create a new system level parameter to be passed to the Data Object when it is called. To create a new parameter, right-click Parameters and then click Add. This stored procedure expects startDate and endDate parameters. The name of the parameter in Exago must match the name of the parameter in the stored procedure exactly. Choose the parameter type from one of the available Exago parameter types. Each parameter can have a default value. This value is intended to be overwritten via the API or via user input when running a report. To allow users to interact with this parameter, and supply values when calling the stored procedure, Hidden must be set to false. Prompt text can be supplied to shown to the user when calling the stored procedure or when using the parameter directly on a report. Parameter Dropdown Objects allow the assignment of an optional Data Object for populating the parameter as a dropdown selection list. Click Apply to save the parameter.

Returning to the Data Object, we will add the parameters to the stored procedure. To do so, click the Parameter menu on the Data Object menu and click Add twice. Choose both of the system parameters to add to the Data Object. The parameters must be listed in this menu in the exact order the stored procedure expects them. Then, we can continue our configuration and choose a unique key as well as create metadata for the object.

We will create column metadata for each column in the stored procedure by clicking the Read Schema button, and then continue to configure each column further if we choose. We can choose the column’s data type from one of the available Exago data types. Columns may also be disabled from filtering, sorting or even visibility in the user interface via these dropdowns. Like a Data Object Alias and Description, a column Alias and Description sets the name and description of the column as it appears to users on the front end. The Sort and Group-By Value tells Exago how to sort and group this column. For example, if this column contained a list of month names, Exago will sort alphabetically and not necessarily in chronological order. By providing a formula here, we can tell Exago how to sort the column, in this case, by an Exago function that returns the month’s ordinal number. The last setting here is the Schema Access Type, and this is set to metadata by default. That’s why is its so important to generate metadata for our Data Objects. WE want Exago to be able to look directly at the Exago configuration file for metadata information. The alternative, reading the Data Source each time, has a tendency to incur latency.

Congratulations! You’ve successfully added and configured a stored procedure to the Exago configuration!
