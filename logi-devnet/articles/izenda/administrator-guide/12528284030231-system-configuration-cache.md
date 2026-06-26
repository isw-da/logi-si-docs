---
title: "System Configuration/Cache"
id: 12528284030231
section: "Administrator Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528284030231-System-Configuration-Cache
updated_at: 2023-02-23T14:58:50Z
---

# System Configuration/Cache

# System Configuration/Cache

The **System Configuration > Cache** page allows an administrator to manage and view the Cache settings.

## What is offered

Izenda offers two areas of the application to be cached: the application metadata, known as System Cache, and the reporting data, known as Data Cache. Data Cache can be enabled and disabled using the Cache settings page, but will be disabled by default.

For Data Cache, Izenda offers two distinct caching solutions out of the box: a disk cache and a memory cache. By default, the disk cache is enabled for the application. These caching options are part of Izenda’s default resources, so you do not need to download or implement any additional items for these to be present.

For System Cache, Izenda offers in-memory cache and shared version storage for deployments with multiple API nodes (web-farms, etc..). By default, in-memory cache is used, but shared version storage can be configured after downloading and deploying the SharedVersionStorage application artifacts.

## How it is configured

The Data Cache settings are located on the Settings > System Configuration > Cache page. On this page you will be able to determine the following options:

> > [![../_images/System_Configuration_Cache.png](https://devnet.logianalytics.com/hc/article_attachments/12528148979607/system_configuration_cache.png)](https://devnet.logianalytics.com/hc/article_attachments/12528148979607/system_configuration_cache.png)
>
> 1. Is the cached enabled?
>    :   * This determines if you are using a cache for this area of the platform.
>        * If the cache was enabled and you deselect this option, all cached values will be invalidated and removed.
> 2. Time to Live
>    :   * This is a time, in seconds, that dictates how long a particular cache is valid.
>        * If this time passes, that cache is considered invalid and data will be pulled from the database and re-cached the next time that information is accessed.
> 3. Eviction Interval
>    :   * This is a time, in seconds, that dictates how often Izenda will go and clean out the invalid or expired cache items.
> 4. Refresh Interval
>    :   * This is a time, in seconds, that determines how frequently Izenda will go an automatically update any items in the cache.
>        * Please note that this process can mean data is re-cached from your database, so there may be some workload considerations when setting this value.
> 5. Refresh Duration
>    :   * This is a time, in seconds, that dictates how long Izenda will let the automated refresh process operate.
>        * If the time limit is met, Izenda stops updating the caches and they will remain invalid until a user manually updates them or the next automated refresh occurs.

The System Cache configuration options will be located in the appsettings.json of your Izenda API. Please note that you can not disable System Cache, and can only switch between in-memory and shared version storage.

1 "izenda.versionedcache.usesharedstorage" : "false",

2 "izenda.versionedcache.sharedstorageurl" : ""

After successfully deploying Shared Version Storage and updating the settings above, you will be able to navigate to the Settings > System Configuration > Cache page to confirm that Shared Version storage is Operational.

![](https://devnet.logianalytics.com/hc/article_attachments/12528148985367/image-20230215-151714.png)

### Refreshing the Cache

Aside from the automated refresh that you can set, the data in the cache can be manually updated on certain pages of the application where you see a ‘Refresh’ button along the top. When selected, the system will re-query the database, refresh the cache, and present the updated results to the user.

The old ‘Update Results’ button has been renamed ‘Apply Filters’. When selected, this will prioritize pulling data from the cache. In the event the cache is invalid, Izenda will re-query the database and then update the cache accordingly.

### Clearing the Cache

In order to manually clear the cache we have created the following endpoint:

POST /api/SystemSetting/ClearCache

Sample Payload:

[{"ClearCacheType":1}]

Sample Response:

[{ "success":true, "messages":null, "data":null}]

The possible values for ClearCacheType are as follows:

* “0” means System Cache
* “1” means Data Cache
* “2” means Both System and Data Cache

## Configuring Memory and Disk Cache

### Configure to store cache on memory

To configure memory cache storage, you will need to update izenda.cache.data.cachestore  to MemoryCacheStore and can also limit the cache’s memory usage by setting a value to izenda.cache.memcache.datacache.maxmemusage

1 "izenda.cache.data.cachestore": "MemoryCacheStore",

2 "izenda.cache.memcache.datacache.maxmemusage": "512",

### Configure to store cache on disk

To configure disk cache storage, you will need to update izenda.cache.data.cachestore to ExternalStorageCacheStore and can also set the file location of the data cache storage by setting a value to izenda.cache.diskcache.datacachedirectory

1 "izenda.cache.data.cachestore": "ExternalStorageCacheStore",

2 "izenda.cache.diskcache.datacachedirectory": "Caches/DataCache",

These values can be modified in our configuration files to support the following directory types:

> Absolute PathsD:\[YourFolderName]If the folder doesn’t exist, the system will create a new one based on this path.
>
> Relative Path[YourFolderName]If the folder doesn’t exist, the system will create on in the application’s directory
>
> UNC Paths\123456.78.910\[YourFolderName]

## System Cache Configuration

System Cache supports in-memory storage and shared version storage for a centralized cache. By default, in-memory storage is used, but shared version storage can be configured by way of the appsettings.json of your Izenda API resources. Prior to configuring, you will need to download and deploy a Shared Version Storage application.

### Shared Version Storage Deployment

The SharedVersionStorage solution is a .NET 6 standalone web application with the purpose of holding and centralizing the cache storage among multiple Izenda API nodes. We will need to download, deploy, and setup the SharedVersionStorage similar to how we would deploy the Izenda API\_AspNetCore. These steps apply to a Windows server, but the equivalent can be followed with a Linux Server:

* Download and install the .NET Hosting Bundle from Microsoft’s download page.
* If IIS is not setup on the server, please setup the IIS web server as described on the Izenda API installation guide.
* After downloading and unzipping the SharedVersionStorage resources, move the resources to an IIS folder.  
  ![](https://devnet.logianalytics.com/hc/article_attachments/12528165014295/screen_shot_2023-02-15_at_11.05.34_am.png)

* Add an IIS website, and configure the SharedVersionStorage site.  
  ![](https://devnet.logianalytics.com/hc/article_attachments/12528165020567/screen_shot_2023-02-15_at_11.12.56_am.png)

* Start the site, and IIS will start the application based on dotnet SharedVersionStorage.dll. If any issues occur around the application start, please enable stdout in the Web.config to help troubleshoot → stdoutLogEnabled="true"

### Shared Version Storage Configuration

* In the appsettings.json, update the following keys to enable Shared Version Storage and set the URL of the SharedVersionStorage website:

1 "izenda.versionedcache.usesharedstorage" : "true",

2 "izenda.versionedcache.sharedstorageurl" : "http://127.0.0.1:91/"

* Restart the Izenda API for the new values to take affect.

* To confirm the Shared Version status has been deployed and configured successfully, navigate to Settings > System Configuration > Cache page of the Izenda application and confirm the Shared Version Storage status is set to Operational.  
  ![](https://devnet.logianalytics.com/hc/article_attachments/12528165024663/screen_shot_2023-02-15_at_10.15.33_am.png)
