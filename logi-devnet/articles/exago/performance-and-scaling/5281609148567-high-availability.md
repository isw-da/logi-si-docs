---
title: "High Availability"
id: 5281609148567
section: "Performance and Scaling"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281609148567-High-Availability
updated_at: 2022-05-03T22:08:50Z
---

# High Availability

# High Availability

This topic highlights recommendations for designing a highly available Exago environment. By creating multiple areas of redundancy, single points of failure are eliminated. A system which is adaptable to component failures is highly available. This topic focuses on how to make Exago highly available and is not an exhaustive discussion on the concept of high availability.

It is assumed that the host application integrating Exago will be made highly available on its own. Any reference to a host app in this topic refers to the embedding host application.

## Components

A highly available system will require a series of architecture choices that support redundancy. This includes implementation of:

* Exago’s [REST Web Service API](#REST)
* Exago’s [Scheduler Service](#Schedule) for Remote Execution and the [Scheduler Queue](#Schedule2) if scheduling reports
* A [Web Farm](#Web)
* A [State Server](#State)
* Use of highly available [network or cloud storage for temporary files](#Temporar)
* Use of [databases or other distributed storage mechanism](#Use) for content storage, Scheduler Queue storage and session storage

### REST Web Service API

Since all high availability architectures are distributed, utilizing the **REST Web Service API** separates the host application from Exago. Clients looking to build a highly available system should use the REST Web Service API instead of the the .NET API, since the .NET API requires the host app and Exago reside on the same server.

When deployed in a [Web Farm](#Web), each instance of the REST Web Service API will be duplicated for each instance of the Web Application.

#### REST Web Service API Resources

* [REST — Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281660927895-REST-Introduction)
* [Admin Support Lab – .NET and REST APIs](https://devnet.logianalytics.com/hc/en-us/articles/5281562235671--NET-and-REST-APIs) (video)
* [Admin Support Lab – Batch REST API](https://devnet.logianalytics.com/hc/en-us/articles/5281531616407-Batch-REST-API) (video)
* [Admin Training Series — Install REST on Windows](https://devnet.logianalytics.com/hc/en-us/articles/5281563077271-Installing-REST-Windows-) (video)
* [Admin Training Series — Installing REST on Linux](https://devnet.logianalytics.com/hc/en-us/articles/5281540942103-Installing-REST-Linux-) (video)

### Scheduler Service and Remote Execution

The **Scheduler Service** lays the foundation for moving the execution of reports off of the Exago Web Application server and on to redundant execution servers. As the name suggests, Scheduler Services handle scheduled report execution but they also support distributed report execution.

**Remote Execution** servers are simply Exago Scheduler Services configured to process all report execution activity from the application immediately. A highly available implementation should include multiple Remote Execution servers, eliminating single points of failure.

With Remote Execution configured, when a user runs a report from the application either by exporting it or clicking the run button, the first available scheduler configured for remote execution will execute that report. If a report is scheduled with a recurrence pattern, it will be run on schedulers configured for scheduled report executions.

#### Scheduler Service Resources

* [Installing the Scheduler Service](https://devnet.logianalytics.com/hc/en-us/articles/5281624674327-Installing-the-Scheduler-Service)
* [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration)
* [Scheduler Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281608723095-Scheduler-Settings)
* [Remote Execution](https://devnet.logianalytics.com/hc/en-us/articles/5281588803095-Remote-Execution)
* [Admin Support Lab — Scheduler Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281547794071-Scheduler-Configuration) (video)
* [Admin Training Series — Installing the Scheduler on Windows](https://devnet.logianalytics.com/hc/en-us/articles/5281563159831-Installing-the-Scheduler-Windows-) (video)
* [Admin Training Series — Installing the Scheduler on Linux](https://devnet.logianalytics.com/hc/en-us/articles/5281548496791-Installing-the-Scheduler-Linux-) (video)

### Scheduler Queue

The **Scheduler Queue** is an extensibility feature that builds upon out-of-the-box functionality of the Scheduler Service. The Scheduler Queue provides additional behavior that contributes to a high availability environment:

* **Centralized work control** — without the Scheduler Queue, the Exago Web Application will assign jobs to Scheduler Services in a round-robin fashion. Once the Web Application sends a job off to a Scheduler Service, that Service “owns” the job from then on. When a **Scheduler Queue** is implemented, the Queue owns the jobs and delegates work as required to the individual Scheduler Services.
* **Handling of Scheduler Service outages** — the Scheduler Queue is aware of the online status of the Scheduler Services. Should one go offline for any reason, the queue can reassign work to the others. Work for the individual Scheduler Services is managed by the Scheduler Queue instead of each isolated Scheduler Service.

The Scheduler Queue is replicated for each Exago Web Application and Scheduler Service. A database can store the scheduled job information and the Scheduler Queue instances access the shared information from that database.

The Scheduler Queue will only handle scheduled jobs, and is not utilized for remote execution jobs. Therefore, it is not necessary to implement the Queue when using the Scheduler Service exclusively for Remote Execution.

#### Scheduler Queue Resources

* [Scheduler Queue](https://devnet.logianalytics.com/hc/en-us/articles/5281598212247-Scheduler-Queue)

### Web Farm

A **Web Farm** is a group of two or more servers supporting multiple instances of the application, managing user data transparently between them. While not an Exago-specific technology, a Web Farm increases availability by decreasing the likelihood of an outage due to Web Application and REST Web Service API servers being unavailable.

Exago web farms require a load balancer, the [use of a state server](#State) and [shared temporary file storage](#Temporar). Sharing the Exago configuration file is also recommended.

#### Web Farm Resources

* [Set Up Exago in a Web Farm](https://devnet.logianalytics.com/hc/en-us/articles/5281607747991-Set-Up-Exago-in-a-Web-Farm)

### State Server

In a standalone environment an Exago server will track its own user sessions. In a web farm, a user’s requests may be handled by several different Exago servers over the lifetime of the session. A centralized **State Server** keeps track of user sessions so that many Exago instances can share the session information among them. The State Server should use a database for storing user session data.

#### State Server Resources

* [Setting up a State Server](https://devnet.logianalytics.com/hc/en-us/articles/5281581463959-Setting-up-a-State-Server)
* [Set Up Exago in a Web Farm](https://devnet.logianalytics.com/hc/en-us/articles/5281607747991-Set-Up-Exago-in-a-Web-Farm)

### Temporary File Storage

Over the course of the report execution cycle, several **temporary files** are generated. As mentioned previously, in a web farm requests from a single user may be handled by several Exago servers. Therefore, all of the Exago servers in the farm need access to these temporary files.

Exago supports network and cloud storage of temporary files. This could be a mapped network drive, a symbolic file system link or a cloud solution such as Amazon S3 or Azure file storage.

Cloud storage, although it requires an Internet connection, typically comes with high availability from the service provider.

#### Temporary File Storage Resources

* [Amazon S3 File Storage](https://devnet.logianalytics.com/hc/en-us/articles/5281592475287-Amazon-S3-File-Storage)
* [File Storage](https://devnet.logianalytics.com/hc/en-us/articles/5281601143191-Installing-Exago-on-Azure#File)
* [Main Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281644565527-Main-Settings)

### Use of Databases

Databases manufacturers support high availability. As each database is different, Exago doesn’t make any specific recommendations on *how* to make them highly available. Consult with the database administrator or the documentation from the database provider for more information.

At a minimum, Exago suggests using databases for the following components:

* **Content Storage** — reports, themes, folders and templates created by users should be stored in a database. Exago’s legacy *Folder Management* and current*Storage Management* solutions provides this facility. Beginning with *v2020.1*+, Storage Management is the only supported content storage mechanism.
* **Scheduler Queue** — the Scheduler Queue can be implemented to use a database for job storage.
* **State Server** — a state server is an integral part of a web farm. Storing sessions in a highly available database prevents loss of user sessions unexpectedly.

#### Database Resources

* [Folder Management](https://devnet.logianalytics.com/hc/en-us/articles/5281620756119-Folder-Management)
* [Admin Support Lab – Folder Management](https://devnet.logianalytics.com/hc/en-us/articles/5281547526295-Folder-Management) (video)
* [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
* [Scheduler Queue](https://devnet.logianalytics.com/hc/en-us/articles/5281598212247-Scheduler-Queue)
* [Setting up a State Server](https://devnet.logianalytics.com/hc/en-us/articles/5281581463959-Setting-up-a-State-Server)

## Architecture

Consider a basic highly available architecture depicted in the figure below. For clarity, redundant services such as multiple Exago servers, Remote Execution servers and Scheduler Services are only shown once.

The figure is broken up into three zones. While the zones are co-located in the diagram, in actual implementation they need not be. It may be advantageous to separate the different components physically and/or geographically if practical. They are:

1. [User’s browser client](#1.)
2. [DMZ](#2.)
3. [Intranet](#Intranet)

![Exago_High_Availability_Zone_Diagram.png](https://devnet.logianalytics.com/hc/article_attachments/5432255650455/exago_high_availability_zone_diagram.png)

Basic highly available implementation

Each zone will be considered individually and then the pieces will be assembled together.

### 1. Browser Client

![zone-1.png](https://devnet.logianalytics.com/hc/article_attachments/5432213314711/zone-1.png)

The browser communicates with both the host app and Exago (though a load balancer in the DMZ) via standard HTTP ports.

### 2. DMZ

![zone-2.png](https://devnet.logianalytics.com/hc/article_attachments/5432237078551/zone-2.png)

The **Demilitarized Zone (DMZ)** contains the servers that are exposed to the Internet for access by end user web browsers. It sits between the end user’s browser and servers in the Intranet zone. This affords a layer of security without sacrificing high availability.

End user browsers communicate with the **Host App** and the **Load Balancer** via standard HTTP ports.

The job of the load balancer is to divide work between multiple **Exago Servers** in a **Web Farm**. Requests coming from users and the host application reach the load balancer where they are forwarded on to an available Exago server in the farm. User session state is managed between the different servers by a State Server in the [Intranet zone](#Intranet).

Each Exago Server contains an instance of the REST Web Service API, the Exago Web Application and an implementation of the Scheduler Queue (if using the Scheduler Service for executing reports on a scheduled basis) increasing the redundancy of each of these components.

### Intranet

![zone-3.png](https://devnet.logianalytics.com/hc/article_attachments/5432231403415/zone-3.png)

The **Intranet** zone contains the servers and databases accessed by the Exago Web Application, the Scheduler Services (via the Scheduler Queue) and perhaps the host app. Servers in the Intranet zone are not directly accessible to the end user’s browser. In the diagram above from top-to-bottom, left-to-right:

* **State Server** — maintains end user browser sessions in a database so that all instances of Exago in the web farm can access session state. The state server communicates with all of the instances of the Exago Web Application in the DMZ.
* **SQ DB** — short for **Scheduler Queue Database**, this is where the job information is centrally stored by the Scheduler Queue. Each instance of the Scheduler Queue, either in the DMZ or Intranet communicate with this database.
* **SQ** — short for **Scheduler Queue**. It is connected to each Scheduler Service and to each instance of the Web Application. Its function is to liaise between the Web Application server, Scheduler Services and SQ DB.
* **DB** — short for **Database**. Also known as the **Business Intelligence Database**. This is the data source that Exago queries to build reports. Both the Scheduler Services and the Remote Execution services will query this database when generating reports. If Remote Execution servers are not used, then the Web Application servers will communicate with the database directly instead (not pictured in the diagram).
* **Exago R.E. Scheduler Services** — are the Scheduler Services designated as **Remote Execution** servers. Whenever a user executes a report in the Web Application or through the REST Web Service API it will be executed by one of these servers.
* **SM** — short for **Storage Management**. This is the content storage for all user created content such as reports, themes, folders and templates. In versions of Exago *pre-v2020.1* this would represent the **Folder Management** database instead.
* **Temp** — this is the temporary file storage hosted either by a cloud storage provider or a redundant network storage system
* **Exago Scheduler Service** — one or more Scheduler Services

### Bringing the Pieces Together

By making each component in the system redundant and distributed, single points of failure are eliminated. A failure of one or more components doesn’t necessarily take the entire system down. Instead, the work is divided among the remaining parts of the system until failed parts are restored.

For each redundant component in the system, the system is available in a worst-case scenario even if all but one of those components fails. As an example, in an environment with *n* number of Exago servers, there can be *n-1* failures before a total outage occurs. Of course in this situation, *all* requests would be forwarded to a single server which may not be able to handle that level of activity.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> As there can only be one load balancer, it remains a potential failure point. Generally load balancers are simple and very reliable.

The examples below walk through the flow of information into the different zones:

#### Example 1

Consider a user interacting with the host application and Exago. When the user runs a report, at a very high level the following sequence of actions takes place:

1. Requests are sent from the user’s web browser to the host application and to the Exago server web farm via standard HTTP ports.
   * The host app will make requests to the Exago server web farm via the REST Web Service API as well. This also occurs over standard HTTP ports.
2. The **load balancer** in front of the Exago Servers distributes the requests from the user’s web browser and host app to the available instances of the Exago Web Application and the REST Web Service API. Since this is a web farm, the requests originating from one user’s browser don’t necessarily end up at the same server — the load balancer determines where they go.
3. Each **Exago server** checks with the **State Server** in the Intranet to track the state of the user’s session. Since each Exago server references the same state server, it doesn’t matter which Exago server handles a particular request. The work of the load balancer is transparent to the end user because of the state server.
4. The **Exago server** then relays the execution of the report to one of its configured **Remote Execution** servers. As there should be several remote execution instances, work will be assigned in a round-robin fashion to the next one.
5. The **Remote Execution** server queries the **Business Intelligence Database** to build the report. **Temporary files** generated as part of the report execution are written to the **Temporary storage location**, making them available to the other servers.
6. The completed report is handed back to the calling Exago Web Application Server in the DMZ. The Web Application Server sends the completed report to the end user’s browser.

On the next interaction from the user, this process starts all over again from step 1. Since requests are handled by the load balancer each time a request is sent from a user, every single request could be handled by a different Exago Web Application server. The state of each user session is handled by the state server, and temporary files are stored in a location accessible to all Exago servers.

#### Example 2

Taking Example 1 a bit further, consider a user scheduling a report to run a payroll report on the first of every month.

1. Requests are sent from the user’s web browser to the host application and directly to the Exago server web farm in the DMZ via standard HTTP ports.
   * The host app will make requests to the Exago server web farm via the REST Web Service API as well. This also occurs over standard HTTP ports.
2. The **load balancer** in front of the Exago Servers distributes the requests from the user’s web browser and host app to the available instances of the Exago Web Application and REST Web Service API. Since this is a web farm, the requests originating from one user’s browser don’t necessarily end up at the same server — the load balancer determines where they go.
3. Each **Exago server** checks with the **State Server** in the Intranet to track the state of the user’s session. Since each Exago server references the same state server, it doesn’t matter which Exago server handles a particular request. The work of the load balancer is transparent to the end user.
4. The **Exago server** makes a call to the **Scheduler Queue** to schedule the new job. The Scheduler Queue stores the job in its database. From here on out, the Scheduler Queue is responsible for the management and execution of the job.
5. **Scheduler Queue** responds to the **Exago server** indicating the scheduling of the job was successful, message is displayed to the user.

From this point, the interaction is completed. From the Scheduler Service’s point of view:

1. At the scheduled time, the **Scheduler Queue** will send the job off to one of the available **Scheduler Services** for execution.
2. The **Scheduler Service** queries the **Business Intelligence Database** to build the report. **Temporary files** generated as part of the report execution are written to the **Temporary storage location**, making them available to the other servers.
3. The Scheduler Service handles the report disposition (either by emailing or saving it to a repository).

## Conclusions

In summary, Exago-specific points of high availability are:

* Multiple Exago servers, each containing an instance of the Web Application, the REST Web Service API and a Scheduler Queue (if using Scheduler Services) should be setup in a web farm
* Temporary files and the Exago configuration file should be shared between instances with either a networked drive or cloud storage
* Use highly available databases wherever possible for:
  + Exago’s Scheduler Queue
  + State Server shared between the multiple Exago servers
  + Storage or Folder Management for content storage

## Additional Resources

* [Admin Support Lab — High Availability](https://devnet.logianalytics.com/hc/en-us/articles/5281562032663-High-Availability) (video)
