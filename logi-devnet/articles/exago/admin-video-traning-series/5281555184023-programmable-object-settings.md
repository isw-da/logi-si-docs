---
title: "Programmable Object Settings"
id: 5281555184023
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281555184023-Programmable-Object-Settings
updated_at: 2022-05-03T22:08:31Z
---

# Programmable Object Settings

# Programmable Object Settings

This video explains how to configure your programmable object settings for use with a stored procedure. Watch this video along with ‘Configuring a Stored Procedure Part 1’ and ‘Configuring a Stored Procedure Part 2’ to set up your Stored Procedure start to finish.

[<< Configuring a Stored Procedure Pt 1](https://devnet.logianalytics.com/hc/en-us/articles/5281541282711-Configuring-a-Stored-Procedure-Part-1) Previous Video

Next Video [Configuring a Stored Procedure Pt 2 >>](https://devnet.logianalytics.com/hc/en-us/articles/5281563495831-Configuring-a-Stored-Procedure-Part-2)

## Transcript

Welcome back to the Exago Technical Training Series! In a previous video, we added a stored procedure to the Exago configuration. In this video, we will continue configuration for this stored procedure using Programmable Object Settings.

Using these parameters causes filtering to be done before the data is sent to Exago. This can increase performance and reduce server resources when using programmable objects, such as stored procedures. To setup your Programmable Object Settings, first expand the General node, then double-click the Programmable Object Settings. Provide the desired parameter name for each use case on the line provided. Any combination of programmable object parameters can be used here. Simply by providing parameter name in this menu, Exago will assign the proper values when the procedure is called. Specifically, this means whenever we need the schema information for the procedure, run a report using the procedure or click a filter dropdown, the call type will specify to the procedure what to return to the user. We are required to supply the programmable object settings and press Apply before we can choose unique keys or create metadata for our stored procedure.

Since those actions require us to execute the stored procedure at the database. Since the procedure is written to expect those parameters, it will not execute without them. So, make sure you do this step before moving on to part 3 of our stored procedure configuration.

Congratulations! You’ve successfully configured your Programmable Object Settings!
