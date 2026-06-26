---
title: " Using Logi Scheduler"
id: 4419723264407
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723264407--Using-Logi-Scheduler
updated_at: 2022-07-17T02:05:37Z
---

#  Using Logi Scheduler

# Using Logi Scheduler

The Logi Scheduler provides the ability to execute reports and other activities on a scheduled basis. Developers can build Logi applications that take advantage of Scheduler features.

The following topics provide guidance in the use of these features:

* [Communicating with the Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/4419723258775-Communicating-with-the-Scheduler#Communicating)
* [Getting Data with DataLayer.Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/4419715555095-Getting-Data-with-DataLayer-Scheduler-#Datalayer)
* [The Schedule Element](https://devnet.logianalytics.com/hc/en-us/articles/4419723262231-The-Schedule-Element#Schedule)
* [Creating and Editing Scheduler Tasks](https://devnet.logianalytics.com/hc/en-us/articles/4419723259671-Creating-and-Editing-Scheduler-Tasks#Creating)
* [Working with Process Parameters](https://devnet.logianalytics.com/hc/en-us/articles/4419723265303-Working-with-Process-Parameters#Parameters)
* [Running and Deleting Scheduler Tasks](https://devnet.logianalytics.com/hc/en-us/articles/4419723261335-Running-and-Deleting-Scheduler-Tasks#RunDel)
* [Scheduler Results and Logging](https://devnet.logianalytics.com/hc/en-us/articles/4419715557143-Scheduler-Results-and-Logging#Logging)
* [Scheduled Task Data Storage Options](https://devnet.logianalytics.com/hc/en-us/articles/4419723263127-Scheduled-Task-Data-Storage-Options#Data)
* [Implementing Multiple Scheduler Instances](https://devnet.logianalytics.com/hc/en-us/articles/4419715556119-Implementing-Multiple-Scheduler-Instances#Instances)
* [Customizing Scheduler UI Appearance](https://devnet.logianalytics.com/hc/en-us/articles/4419715554199-Customizing-Scheduler-Appearance#Customizing)

## Developer Overview

Developers who have not already done so are encouraged to read our introductory topic [Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/4419715378455-Logi-Scheduler) in order to get a basic understanding of the Scheduler product and its installation before proceeding.
From a development perspective, the Logi Scheduler consists of three parts:

1. An autonomous service that automatically runs scheduled reports and other Logi application activities without direct user interaction (much like the Windows Task Scheduler).
2. A database of scheduled tasks which is read and updated by the Scheduler service.
3. Special elements that let developers build definitions for creating and managing the scheduled task database. These may be used to create administrative tools for system admins, or they may be incorporated into reports so that end-users can do their own runtime scheduling. The **Schedule** element, for example, is a "super-element" with built-in user input controls for presenting scheduled task data.
