---
title: "Manage the Composer Query Engine"
id: 34932686805645
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932686805645-Manage-the-Composer-Query-Engine
updated_at: 2026-05-26T22:06:15Z
---

# Manage the Composer Query Engine

# Manage the Composer Query Engine

The query engine is a stand-alone microservice within the Composer environment that processes visual queries. If you install or upgrade Composer [using the supplied installation script](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933029876365-Installation-Steps), the query engine microservice is started automatically. If you install or upgrade Composer [manually](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933041539853-Install-Composer-Manually), you must manually enable and start the query engine microservice.

## Configure the Query Engine

In your environment, the query engine is called `zoomdata-query-engine`. To configure and manage the microservices that the query engine executes and runs, you need to make changes to the `query-engine.properties` file. It contains properties that are specific to how the query engine operates within your environment.

The query engine also has a `query-engine.env` file and a `query-engine.jvm` file. You can edit these files to configure the following:

* To define the environment variables that are visible for the microservice, edit the `query-engine.env` file.
* To configure the JVM options that are used to start up Composer microservices, edit the `query-engine.jvm` file.

The default memory configurations give the query engine is 4 GB of heap memory. During microservice startup, the query engine consumes at least 4 GB of memory (plus some off heap memory). You can alter this using the following parameters in the query-engine.jvm file, i.e. by increasing to 6Gb.

-Xms6g  
-Xmx6g

For information on editing configuration files, see [Edit a Configuration File](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932669980557-Edit-a-Configuration-File). For information about query engine properties, see [Query Engine Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932671654797-Query-Engine-Properties).
