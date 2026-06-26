---
title: "Advanced Repository Configurations"
id: 4406635296919
section: "Using DataHub v2.2 With Logi Info"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406635296919-Advanced-Repository-Configurations
updated_at: 2022-04-01T03:13:19Z
---

# Advanced Repository Configurations

# Advanced Repository Configurations

DataHub's columnar data repository generally requires no configuration after installation. However, there may be special circumstances where a tweak is desirable and related configurations are discussed in this topic.

* [About the Data Repository](#About)
* [Allocating Memory](#heap)
* [Configuring Look-up Columns](#lookup)

## About the Data Repository

Logi DataHub uses the **Infobright** columnar relational database as its data repository. It's a self-tuning, high-performance storage system that generally requires nothing from administrators after installation.

However, there are special circumstances we've identified wherein tweaking the database's configuration or schema may be desirable.

## Allocating Memory

The optimum amount of main memory (the "heap") available to the Infobright server is automatically determined and set by the DataHub installer, based on the physical memory available in the server.

Infobright's suggestion is that 60-80% of memory be allocated to the database server.

However, there may be situations that warrant changing the setting. For example, the initial memory setting assumes that there are no other services consuming significant memory on the machine. If other services *do* consume significant memory, a lower memory setting for Infobright might be better. You don't want to allocate so much memory to Infobright that you "starve" other applications.

Or, perhaps you decided to physically add more memory to the server *after* the DataHub installation and want to change the Infobright allocation to take advantage of it (in which case, do the 60-80% math on the new memory size to get the correct setting value).

In any case, assuming a standard installation location, to change the memory allocation:

1. Navigate to, and make a safety copy of, this file:   
     
   C:\Program Files\Logi Analytics\DataHub\Infobright-postgres\ib\_data\infobright.cnf
2. Use a text editor to open the original file and then search in it for "ServerMainHeapSize".
3. Set the ServerMainHeapSize value to a new value (in MB) and save the file.
4. Use Windows Admin Tools![](https://devnet.logianalytics.com/hc/article_attachments/5160464735255/menuarrowrt.png)Services tool to stop and restart the *infobright-iee-postgres* service.

## Configuring Look-up Columns

Infobright supports a column designation of "Lookup", which causes columns to be stored uncompressed, in memory, for very fast access. It improves performance when applied to columns that will be used for grouping, filtering, and aggregating data. When data is loaded, DataHub applies this designation automatically to Dimension (text only) columns, based on certain criteria and, under most circumstances, it results in very fast query performance.

However, if you have a very large table with a very large number of distinct
values, you may consume significant amounts of memory using lookups, adversely impacting performance.

The criteria DataHub uses to designate lookup columns is determined by their "cardinality", the measure of the number of columns in a set, in this case the ratio of the "number of distinct values" to the "total number of records".

![](https://devnet.logianalytics.com/hc/article_attachments/5160470849175/reposconfig_01.png)

This process is illustrated in the table shown above. The default cardinality threshold is 20%.

To change that threshold, assuming a standard installation location, navigate to and open this text file:

C:\Program Files\Logi Analytics\DataHub\Web.config

And search for this line:

<add key="CardinalityThreshold" value="0.2" />

Change the value to the new desired cardinality threshold percentage, save the file, and restart DataHub.

![](https://devnet.logianalytics.com/hc/article_attachments/5160446913687/noteicon.png) Remember that changes to this value will *not* affect *currently loaded* data - you must reload the data to have it take effect.
