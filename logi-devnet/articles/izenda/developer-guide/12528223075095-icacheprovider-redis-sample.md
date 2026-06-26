---
title: "ICacheProvider - Redis Sample"
id: 12528223075095
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528223075095-ICacheProvider-Redis-Sample
updated_at: 2023-02-23T15:17:09Z
---

# ICacheProvider - Redis Sample

# ICacheProvider - Redis Sample

Izenda applies [caching](https://en.wikipedia.org/wiki/Cache_(computing)) to improve user responsiveness and reduce resource usage. The built-in library uses an in-memory cache which works best for typical usage scenarios. This article describes the Redis Sample.

For specific needs, this feature can easily be integrated with other caching systems, via the `ICacheProvider` interface.

In this sample, we will use [Redis](http://redis.io/) as an alternative cache server - there is no intentional comparison between the built-in cache and Redis here, we just pick Redis as an example.

Summary of the Steps

1. [Reference the interface library Izenda.BI.CacheProvider.dll in our code base.](#reference-icacheprovider-interface-in-a-new-project)
2. [Provide our own implementation of the ICacheProvider interface.](#implement-the-icacheprovider-interface)
3. [Unit test the implementation.](#implement-the-tests)
4. [Replace the built-in caching library file Izenda.BI.CacheProvider.Memcache.dll with our own library file.](#replace-the-built-in-caching-library)

Note: Please refer to our GitHub repo for the latest code samples: <https://github.com/Izenda7Series/RedisCacheProvider>

## Preparation

1. Redis test server setup

   1. Download, extract and compile the server from <http://redis.io/download>.

      For Windows, there are binary builds available at <https://github.com/MSOpenTech/redis/releases>.
   2. Start the server using this command in terminal:

      ```
      src/redis-server
      ```
   3. Start the client in another terminal to check our server:

      ```
      $ src/redis-cli
      										redis> set foo barOKredis> get foo"bar"
      ```
2. Redis client library

   1. We will use the [StackExchange.Redis](https://github.com/StackExchange/StackExchange.Redis) library.
   2. We will install it from within Visual Studio in the following [step](#reference-stackexchange-redis-client-library).

## ICacheProvider Implementation

### Reference ICacheProvider Interface in a New Project

1. Create a new Class Library project in Visual Studio.
2. Name it Izenda.BI.CacheProvider.Redis.
3. Select a location (e.g. D:\Projects).
4. Select to create new solution.
5. Give the solution name Izenda.BI.RedisCache.
6. Tick the Create directory for solution check-box.
7. Click OK to create the project and solution.

   ![../_images/CacheProvider.Redis_New_Project.png](https://devnet.logianalytics.com/hc/article_attachments/12528147042071/cacheprovider.redis_new_project.png)
8. Copy the interface library file Izenda.BI.CacheProvider.dll from Izenda installation folder into the newly-created folder D:\Projects\Izenda.BI.RedisCache\Izenda.BI.CacheProvider.Redis.
9. Open Solution Explorer, right-click References in project Izenda.BI.CacheProvider.Redis and select Add Reference.
10. In Reference Manager pop-up, click Browse and select the file Izenda.BI.CacheProvider.dll (in D:\Projects\Izenda.BI.RedisCache\Izenda.BI.CacheProvider.Redis).
11. Click OK to close Reference Manager pop-up.
12. Verify the interface by double-clicking Izenda.BI.CacheProvider in References to open Object Browser.
13. Expand the nodes and select ICacheProvider to see this list of methods to implement.

    ![../_images/ICacheProvider_Interface.png](https://devnet.logianalytics.com/hc/article_attachments/12528147051415/icacheprovider_interface.png)

### Reference StackExchange.Redis Client Library

1. Open NuGet Package Manager pop-up from Tools > NuGet Package Manager > Manage NuGet Packages for Solution…
2. Click Browse tab and enter StackExchange.Redis in the text box to search.
3. Select StackExchange.Redis on the left and tick the Izenda.BI.CacheProvider.Redis project check-box on the right.
4. Select Latest stable 1.1.608 (at the time of writing) and click Install.
5. Verify that StackExchange.Redis is shown in the References list in Solution Explorer.

### Implement the ICacheProvider Interface

1. Right-click the default Class1.cs file in Solution Explorer and rename it to RedisCacheProvider.cs, also agree to change the class name to RedisCacheProvider when asked.
2. Implement the methods of the interface using StackExchange.Redis APIs.
3. Reference the namespace System.ComponentModel.Composition if necessary (Add Reference and tick System.ComponentModel.Composition in Assemblies > Framework).

*Full sample code with method implementations:*[RedisCacheProvider.cs](https://github.com/Izenda7Series/RedisCacheProvider/blob/master/Izenda.BI.CacheProvider.RedisCache/RedisCacheProvider.cs#L1)

Note: The Redis server address is assumed to be “localhost” in this sample. It should be read from the configuration file in an actual code.

Note: There was a previous serialization issue when adding certain objects to the cache, and has been resolved in versions 2.4.4+ .

If using a previous verison, please use a workaround similar to this:

```
privatestaticConcurrentDictionary<string,object>_mem=newConcurrentDictionary<string,object>();privateboolIsInMemoryCache(stringkey,Typetype){return(type.IsGenericType&&type.GenericTypeArguments.Any(t=>t==typeof(Object)))||type.FullName.StartsWith("Izenda.BI.DataAdaptor.IDataSourceAdaptor")||type.FullName.StartsWith("Izenda.BI.Logging.ILogManager")||type.FullName.StartsWith("Izenda.BI.DataAdaptor.IDataSourceAdaptor");}publicvoidAdd<T>(stringkey,Tvalue){if(IsInMemoryCache(key,typeof(T))){_mem.AddOrUpdate(key,value,(existingKey,oldValue)=>value);}else{// Serialize, and add to redis (custom) cache}}publicTGet<T>(stringkey){if(IsInMemoryCache(key,typeof(T))){objectvalue;_mem.TryGetValue(key,outvalue);return(T)value;}else{// Get from redis (custom) cache, and deserialize}}
```

### Add UnitTest Project

1. Rick click Solution ‘Izenda.BI.RedisCache’ in Solution Explorer and select Add > New Project.
2. Add a Class Library project named Izenda.BI.CacheProvider.Redis.Test.
3. Reference the project Izenda.BI.CacheProvider.Redis (Add Reference and tick Izenda.BI.CacheProvider.Redis in Projects > Solution).
4. Reference xUnit Library.
   1. Open NuGet Package Manager pop-up from Tools > NuGet Package Manager > Manage NuGet Packages for Solution…
   2. Click Browse tab and enter xunit in the text box to search.
   3. Select xunit on the left and tick the Izenda.BI.CacheProvider.Redis.Test project check-box on the right.
   4. Select version 1.9.1 (working at the time of writing) and click Install.
   5. Similarly install xunit.runner.visualstudio version 2.1.0 to Izenda.BI.CacheProvider.Redis.Test project.

### Implement the Tests

1. Right-click the default Class1.cs file in Solution Explorer and rename it to RedisCacheProviderTest.cs, also agree to change the class name to RedisCacheProviderTest when asked.
2. Implement the tests in xUnit.

*Full sample code with implemented test:*[RedisCacheProviderTest.cs](https://github.com/Izenda7Series/RedisCacheProvider/blob/dev/Izenda.BI.CacheProvider.RedisCache.Test/RedisCacheProviderTest.cs#L1)

### Run the UnitTests

1. Open Test Explorer from Menu > Test > Windows.
2. Click Run All in Test Explorer.

   > (Remember to start the Redis server before testing)
3. All the tests should be passed.

![../_images/RedisCacheProviderTest_TestExplorer.png](https://devnet.logianalytics.com/hc/article_attachments/12528147058711/rediscacheprovidertest_testexplorer.png)

## Replace the Built-in Caching Library

1. In the installation folder, find the built-in caching library file Izenda.BI.CacheProvider.Memcache.dll and rename to Izenda.BI.CacheProvider.Memcache.dll.unused.
2. Copy the new caching library file Izenda.BI.CacheProvider.Redis.dll and StackExchange.Redis.dll to the folder (they can be found at D:\Projects\Izenda.BI.RedisCache\Izenda.BI.CacheProvider.Redis\bin\Debug\).
3. Restart the system for the DLL to be loaded.
4. Use the system for a while then open the Redis client in terminal to check our cache:

   ```
   $ src/redis-cli
   								redis> keys *
   ```
