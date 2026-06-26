---
title: "Manage the Composer Query Engine"
id: 4405859161751
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859161751-Manage-the-Composer-Query-Engine
updated_at: 2021-09-21T01:26:57Z
---

# Manage the Composer Query Engine

# Manage the Composer Query Engine

The query engine is a stand-alone microservice within the Composer environment that processes visual queries. If you install or upgrade Composer [using the supplied installation script](https://devnet.logianalytics.com/hc/en-us/articles/4405851088791-Installation-Steps), the query engine microservice is started automatically. If you install or upgrade Composer [manually](https://devnet.logianalytics.com/hc/en-us/articles/4405851085207-Install-Composer-Manually), you must manually enable and start the query engine microservice.

## Configure the Query Engine

In your environment, the query engine is called `zoomdata-query-engine`. To configure and manage the microservices that the query engine executes and runs, you need to make changes to the `query-engine.properties` file. It contains properties that are specific to how the query engine operates within your environment.

The query engine also has a `query-engine.env` file and a `query-engine.jvm` file. You can edit these files to configure the following:

* To define the environment variables that are visible for the microservice, edit the `query-engine.env` file.
* To configure the JVM options that are used to start up Composer microservices, edit the `query-engine.jvm` file.

The default memory configurations give the query engine up to 6 GB of heap memory. During microservice startup, the query engine consumes at least 1 GB of memory. You can alter this using the following parameters in the `query-engine.jvm` file:

```
-Xms1g  
-Xmx6g
```

For information on editing configuration files, see [*Edit a Composer Configuration File*](https://devnet.logianalytics.com/hc/en-us/articles/4405850887703-Edit-a-Composer-Configuration-File). For information about query engine properties, see [*Query Engine Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859160727-Query-Engine-Properties).
