---
title: "Execution Caching"
id: 5281645120919
section: "Performance and Scaling"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281645120919-Execution-Caching
updated_at: 2022-05-03T22:08:51Z
---

# Execution Caching

# Execution Caching

**Execution Caching** allows the data from a report execution to be saved so that reports can be viewed more quickly and with less stress to the data source. The frequency and schedule of data source updates is customizable for each report. Updates can be scheduled for off-hours in order to better balance system load. Caching can significantly reduce data source calls for reports that are accessed frequently. Large or data-intensive reports, which can take a long time to run, especially benefit from caching.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Execution caching is currently incompatible with the [Scheduler Queue](https://devnet.logianalytics.com/hc/en-us/articles/5281598212247-Scheduler-Queue).

## Enabling Execution Caching

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This feature requires the installation and proper configuration of the Scheduler Service. See [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration)

**Execution Caching** uses the **Scheduler Service** to cache the data at set refresh intervals. When caching is enabled for a report, a caching schedule is created that determines how often the data is refreshed. Scheduler Services need to be enabled for the user or users who will be setting the caches; however, users who only need to view the cached reports do not need to have scheduling enabled.

To enable execution caching, set **General** > [Scheduler Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281608723095-Scheduler-Settings) > **Enable Execution Cache** in the **Admin Console** to *True*.

### Cache Visibility Settings

The **@userId@**and **@companyId@** parameters must exist and have default values assigned to them in order to be able to enable execution caching. These parameters are used to assign visibility permissions to cached data.

The following **Admin Console** settings that affect access to some schedule recurrence options will also affect the recurrence options available in the execution caching window:

* **General** > **Scheduler Settings** > **Show Schedule No End Date Option**
* **General** > **Scheduler Settings** > **Show Schedule Intraday Recurrence Option**

The following **Admin Console** setting will affect the view level options that a user has when assigning permissions for an execution cache:

* **General** > **Scheduler Settings** >**User Cache Visibility Level** (*v2017.3+*)
* **General** > **Scheduler Settings** > **Scheduler Manager User View Level** (*pre-v2017.3*)

The cache data is stored in the scheduler temporary directory, however cache files will not be deleted by the scheduler’s routine cleanup.

## Setting Cached Reports and Refresh Intervals

To set up caching for an advanced report:

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Role-based filters and column-based tenancy apply based on the user who *creates* the cache. Users who can *view* the cache will see data filtered by the *creator’s* role and tenancy, not the viewer.

1. From the ![ReportOptions.png](https://devnet.logianalytics.com/hc/article_attachments/5432231443351/reportoptions.png) **Advanced** menu, click **![ExecutionCacheOptions.png](https://devnet.logianalytics.com/hc/article_attachments/5432213420695/executioncacheoptions.png) Execution Caching**.
2. Check the **Enable execution caching** check box.
3. Choose which users will be able to see the cached data:  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > Not every option may be available.

   * **User**: Users will only see cached data that they have created. When another user runs the report, it will execute against the database instead of the cache.
   * **Company**: Users will see cached data that has been created by anyone with the same **@companyId@ parameter**. When a user from outside the company runs the report, it will execute against the database instead of the cache.
   * **Global**: The report has one data cache which is visible for all users.
4. Choose how often the cache is updated:

   1. Enter a time of day in the **Schedule Time** field, or use the picker to select a time.
   2. *Optional*: To update the cache multiple times per day, select the **Repeat Every** check box and enter a time for how often it should repeat.  
      *Optional*: To repeat until a certain time of day, enter that time in the **U****ntil** field, or use the picker to select a time.
5. Choose which days of the week the cache is updated. Select either:

   * To repeat every day or every number of days, click **Every \_\_ day(s)** and enter a number of days for how often it should repeat.
   * To repeat every Mon, Tues, Wed, Thurs, and Fri, click **Every weekday**.
6. Click **OK**.

When execution caching is enabled for a report, the cache is not created immediately. To run the report, you can manually create the cache by clicking the **Cache Status**![CacheInvalid.png](https://devnet.logianalytics.com/hc/article_attachments/5432124221719/cacheinvalid.png) icon, or you can wait until the first scheduled update completes. The cache can always be updated manually by clicking this icon.

Cache schedules are visible in the schedule manager, with the label *(cache)*. Caches can be edited or deleted using the schedule manager or the advanced report designer.

![screen.schedulemanager_cache.png](https://devnet.logianalytics.com/hc/article_attachments/5432124247319/screen.schedulemanager_cache.png)

Viewing a report cache in the schedule manager

### Editing cached reports

Editing a cached report invalidates its cache. It cannot be run until the cache is updated. A missing or invalid cache is indicated by the message *Cache is invalid*, both in the report description and in the report tree menu.

![e8TjJVAwOq.png](https://devnet.logianalytics.com/hc/article_attachments/5432237289239/e8tjjvawoq.png)![v3JBAsR5fc.png](https://devnet.logianalytics.com/hc/article_attachments/5432231584663/v3jbasr5fc.png)

Valid and invalid report cache indicators

It is recommended that you fully design a report first, so that you can manually verify the output, before enabling the cache.
