---
title: "Considerations When Sizing an Exago System"
id: 5281627689367
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281627689367-Considerations-When-Sizing-an-Exago-System
updated_at: 2023-04-03T17:52:19Z
---

# Considerations When Sizing an Exago System

# Considerations When Sizing an Exago System

A **quad-core VM with 32GB RAM on a gigabit network running Windows 10 or Linux**should support dozens of simultaneous users running average-sized reports. From this most generic specification, there are a number of considerations that should be reviewed in order to strategically expand hardware specifications according to any additional known input. It’s also recommended that a certain amount of system growth is calculated into the final specification.

## Assumptions

Rather than starting with considerations immediately, here are a number of base assumptions that will help focus the initiative.

* A quad-core VM with 32GB RAM is a base configuration.
* Gigabit network (or better) wherever possible.
* All server clusters (web application, state, scheduler, database(s), etc) should be located within close geographical “zones”. If multiple geographical zones need to be supported to address the full user base, consider mirroring server clusters in multiple zones, managing zone traffic using load balancing technology to distribute traffic based on locale.
* Use persistent (not transient) local storage such that optional log and monitoring data is retained across potential server bounces.
* The database and/or database server will not be taken into consideration here. It’s assumed that the database/database server can handle any additional load Exago may put on it appropriately and without being a bottleneck.
* Aside from the possibility that Exago runs on the same server as the host software within which it is embedded, as in the case of a full .NET implementation, it’s assumed that there are no other systems running on this server.
* Windows and the IIS web application server arguably requires more CPU/RAM than Linux equivalents (including mono), if only slightly. That said, for these purposes, an attempt will be made to consider the OS and web application server generically.

## Web Application Server

There are a number of considerations pertaining to sizing the main server that runs Exago’s core software.

* Within Exago, API choice is largely irrelevant. In isolation, there is negligible latency associated with the REST API due to it simply serving as an interface to the .NET API behind the scenes. The real difference, however, between the two would be associated latency due to network packaging and traffic intrinsic to REST as compared to the **.**NET API “communicating” in machine memory. This can be mitigated somewhat by using Exago’s batch REST interface. Of course, while a .NET API solution would likely have the host application on the same web application server, requiring the server to be sized accordingly, using the REST API affords greater load distribution across servers.
* Web application servers can typically handle >10k “requests” per second. Each Exago user hit, however, typically includes up to hundreds of “requests,” including images, styling, code executions, and so on. This is why a given web application server typically handles up to dozens of Exago users simultaneously. The more simultaneous users expected to be supported by a given server, the more RAM will be necessary to do so. Once the server approaches maximum RAM configuration, it’s better to build a server farm of web application servers horizontally to host a growing user base. This is especially true for a user base distributed across wide geographical zones, as described above. A multi-server web farm also [affords a level of redundancy](https://devnet.logianalytics.com/hc/en-us/articles/5281609148567-High-Availability) should a server failure ensue. See [Set Up Exago in a Web Farm](https://devnet.logianalytics.com/hc/en-us/articles/5281607747991-Set-Up-Exago-in-a-Web-Farm).

## Scheduler Service

The **Scheduler Service** allows for the offloading and distribution of report execution to zero or more separate hardware servers for both load balancing and execution isolation. For maximum benefit, it should be installed on separate servers in order to isolate immediate and/or remote executions or scheduled executions across multiple machines as appropriate.

* **A [Scheduler Queue](https://devnet.logianalytics.com/hc/en-us/articles/5281598212247-Scheduler-Queue) (software) should be considered in a production environment**. While the Scheduler Queue can typically live on the Exago Web Application Server with little to no additional hardware considerations, answers to the following questions may or may not necessitate more hardware-intensive servers.
  + Is there a heavier than average reliance on schedulers and scheduled report execution?
  + Does the implementation require a database for scheduled job storage?
* **A Scheduler Service configured as a stand-alone server could be less hardware-intensive than a full web application server** installation of Exago since, by itself, it is lighter-weight server software and does not need to support web application server software.
* If the web application server is becoming taxed one or more Scheduler Services can be installed to offload report execution to a separate VM, thus reducing or eliminating the report execution “responsibility” of the web application server itself.

* If there are a significant number of scheduled reports, long-running reports, or reports running concurrently, one or more Scheduler Services can be installed on separate servers to offload report execution reducing or eliminating report execution “responsibility” of the web application server itself. Load will be distributed by Exago’s core engine based on available resources (CPU and RAM primarily).

* If there is a specific time window within which report execution must complete, separate scheduler servers will help ensure that these execution windows are adhered to.
* Report execution servers and scheduler servers, both achieved using the Scheduler service software but configured separately in Exago’s Admin Console, should not be configured to be on the same installed server. Remote execution will take priority over scheduled executions, if on the same server, potentially delaying scheduled jobs and pushing the execution window.

## CPU- and RAM-Optimization

Whether report execution is isolated to Scheduler Services or continues to be done by the Web Application, the reports themselves may help further dictate hardware specifications. Some data centers, and certainly many IaaS and PaaS vendors offer optimized hardware and auto-scaling options that can be taken advantage of when considering hardware specifications.

* **CPU-Optimized server:**
  + Are reports heavily formatted, include significant cross-platform joining, conditional logic, custom fields, or formulas?
  + Dashboard component will, optimally, run in its own thread/core. Therefore, if Dashboard executions are common, increased CPU cores would be beneficial.
  + Are extensive CrossTab reports commonly executed?
* **RAM-Optimized server**:
  + Are reports longer or wider than average? The more data that needs to be brought into the system from the database, the more RAM needed  to complete report execution.
  + Are extensive CrossTab reports commonly executed?
  + Do you have default filters, optional filters, or the ability for users to inadvertently execute reports on massive data sets?
* **Auto-scaling:** some vendors have the ability to combine monitoring features with auto-scaling to ramp up hardware specifications should the load require.

## Extensibility

* Extensibility (Server Events/Action Events/Scheduler Queue) will all be loaded and executed on the same server as the Exago Web Application. Assuming a configurable file system connection between the Exago Web Application and Extensibility implementation, Extensibility code can be stored on a separate server. It still will execute on the same server as the Exago core code.
* Folder Management also executes as part of the Exago Web Application; however, it typically interfaces with external components (database, web services, etc.).
* Extensibility code may necessitate a stronger Exago Web Application server and/or networking in the following scenarios:
  + Extensibility code performs long-running tasks. Generally, Extensibility hooks are blocking calls and would need to return in a timely fashion, so the idea of long-running Extensibility should be avoided whenever possible.
  + Extensibility code requires hardware-intensive operations (for example, significant mathematical computation).
  + Extensibility code requires extensive database queries or data manipulation outside of what is done within Exago.

## Client’s Installations

Two clients offered their hardware specifications as currently installed on AWS. Approximate users supported and associated costs are provided. (Prices as of August 2018.)

### Client 1:

* 4 x m4.xLarge EC2 instance farm (4 x $0.20/hr = $576/mo) for web application and report execution
* Elastic Load Balancing w/ sticky sessions ($0.0225/hr = $16.20; additional cost for average traffic rates at $0.008/LCU-hour)
* Exago Scheduler(s) run on aforementioned EC2 instances
* CPU Utilization averages < 20%
* No auto-scaling configured at this time
* Approximately 24,000 users/mo
* Approximate cost < $600/mo

### Client 2:

* 1 x c3.4xLarge EC2 instance ($0.84/hr = $604.80/mo) for web application and report execution
* 1 x c3.8xLarge EC2 instance ($1.68/hr = $1,209.60/mo) for Dashboard execution
* 2 x c3.xLarge EC2 instance (2 x $0.21/hr = $302.40/mo) for Exago Schedulers/scheduled report execution and back-up on-demand report execution
* No auto-scaling configured
* Approximately 10,000 users/day (45,000 users in the system)
* Approximate costs < $2200/mo
