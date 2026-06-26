---
title: "Logi Scheduler Terminology"
id: 4419723027735
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723027735-Logi-Scheduler-Terminology
updated_at: 2022-07-17T02:07:12Z
---

# Logi Scheduler Terminology

# Logi Scheduler Terminology

For the sake of clarity, the following terms are used in these Scheduler
documents:

| Term | Description |
| --- | --- |
| Scheduler | The Windows service or Linux daemon that runs in the background and runs events at the times and intervals detailed in its database. |
| Scheduler Task | An event (one record) in the Scheduler's database. Contains details of time, frequency, interval, and the ID of the target process to run. |
| Process Task | A task within a Logi Info process definition in a Logi application. A Scheduler Task "runs" a Process Task at the desired time/interval. |
| Schedule XML | The XML representation of the scheduling details for a Scheduler Task. May include date, time, frequency, etc. |
| Schedule | An element used in report definitions which includes a user interface with controls, for the purpose of creating or editing a Scheduler Task. |
| Schedule Intervals | The time intervals that can be used in a Scheduler Task: *Once*, *Daily*, *Weekly*, *Monthly,**Minutes,* and *Hourly.* |

The Scheduler is supported by special elements for both report and process
definitions and these are introduced later on.
