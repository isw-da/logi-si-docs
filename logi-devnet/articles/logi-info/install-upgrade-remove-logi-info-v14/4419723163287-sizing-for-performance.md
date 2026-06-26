---
title: "Sizing for Performance"
id: 4419723163287
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723163287-Sizing-for-Performance
updated_at: 2022-07-17T01:37:41Z
---

# Sizing for Performance

# Sizing for Performance

The following are general sizing considerations for a Logi Info web application, followed by high level recommendations for server components based on these considerations. Specific recommendations will vary depending on your implementation.

To accurately determine the appropriate deployment model for your Logi Info applications, take the following into consideration:

* **Maximum Number of Concurrent Users** - As with any system, the application needs to respond to end users in a timely fashion, even during peak load times.
* **Number of Concurrent Data Visualizations** - The number of visualizations that are loaded concurrently into a page or Dashboard will affect performance.
* **Complexity of Data Visualizations** - Some data visualizations present a single metric and dimension, while others present multiple metrics and/or dimensions. More resources are required to render complex data visualizations.
* **Volume of Data Used to Generate Data Visualizations** - Logi Info data visualizations range from simple, summary charts to interactive, self-service analysis tools. The volume of data required to be delivered from the data tier to the application tier to generate these visualizations can range from a few dozen records to tens of thousands of records.
* **Logi Info-Based Data Aggregation or Manipulation** - Whenever possible, data manipulations, such as calculations and aggregations, should be performed within the data server or system because they're optimized to perform these operations. In addition, the amount of data transferred over the network from the data system to the Logi application should be limited to the actual needs of the data visualization. When it is necessary to perform data manipulations in the Logi application, the type of manipulation
  and the volume of required data will have an impact on the resources available.

## Recommendations

Based on load-testing of benchmark data from our Large Enterprise customers, we have established the following recommendations:

### Processors

The following are guidelines for a typical scenario.

* **Minimum Configuration Cores**: The minimum number of required CPU cores is determined by the expected number of end users, as follows:

| End Users | Baseline # Cores |
| --- | --- |
| 1 - 100 | 4 |
| 101- 250 | 8 |
| 251 - 500 | 12 |
| 501 - 1000 | 16 |
| > 1000 | Custom Sizing Required |

Using the minimum configuration as a starting point, the following factors will determine the processor requirements for your production environment:

* **High Concurrency** - If you anticipate end-user concurrency of greater than 10%, increase the number of cores by 25% to 50% of the Minimum Configuration Cores.
* **Application Complexity** - If you judge that your application is complex, based on the considerations presented earlier (e.g. high number of visualizations in a single page, complex workflows, and complex data processing at the app tier), we recommend that you assess the impact of that complexity on overall performance and sizing. It is not unusual to add an additional 25% to 100% of the Minimum Configuration Cores to ensure better performance.
* **High Availability** - Load-balanced, high-availability systems will require an increased core count. It is typical for Large Enterprises to deploy an additional 50% to 100% of the Minimum Configuration Cores based on the target service level.

### Memory

We recommend a 2-to-1 ratio of gigabytes of memory to CPU core (i.e. two GB of RAM per core).

### Storage

Logi Info applications are not memory-constrained because they leverage a hybrid caching (see [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/4419715421975-The-Logi-Server-Engine)) mechanism that utilizes both disk- and memory-based storage when performing data acquisition, data aggregation, visualization generation, and other data-intensive operations.

Using the mechanism, a Logi application dynamically allocates storage resources depending on the processing stage in order to optimize their use. Therefore, we recommend that the server utilize dedicated, "fast" storage devices, such as SSDs or high RPM disk drives. Total storage usage is highly variable and is dependent on the size of the data volumes being processed and cached by the application. At a minimum, drives with a capacity of 100GB are commonly used.

### Environments

In addition to the primary production environment, other environments should be appropriately sized as well:

* **Development Environments** - We recommend a four core minimum for any development environment. For environments with sophisticated development needs, such as a high number of developers, continuous integration development style, and test driven development, it's typical to size a development environment at 25% to 50% of the baseline number of cores, with a minimum of four cores.
* **Quality Assurance and Load Testing Environments** - Requirements for load testing or automated QA practices typically require a mirror images of the production environment, with the same number of cores in the same machine configuration, in order to accurately replicate production performance characteristics. If load testing is not required, then 25% to 50% of the production core sizing is ideal for more complex environments or automated QA, with a minimum of four cores.
* **Disaster Recovery Environment** - Some large enterprises require a stand-by system for disaster recovery. In this scenario, the Disaster Recovery system is typically a mirror image of the full production environment.

## How Many Servers Do You Need?

Your production web server hosts your Logi applications, which run as extensions to the web server. Ideally, this computer should be dedicated to this task alone.

However, other configurations are possible, including those in which the web server also serves other functions (i.e. is not dedicated to Logi applications alone) and/or is also the database server. Some Logi large enterprise customers use multiple "clustered" servers for top performance and high reliability.

Numerous factors external to your Logi application can affect this decision, including the amount of general web server traffic, the number of concurrent database users, the size of the databases, the complexity of the database queries, the
frequency of
access, and, not least, cost.

You may care to begin with a combined configuration and, as your report usage grows, change to a dedicated configuration. The nature of Logi products allows you to do this easily and often without additional cost (if CPU core count remains constant).

Recent studies concerning server virtualization suggest that database servers are frequently under-utilized. On the other hand, many database vendors recommend that their products be run on a dedicated server. You may wish to check with your database vendor for their recommendations concerning database servers.
