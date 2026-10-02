> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Review Refresh Jobs

Administrators can monitor data source refresh jobs using the Console of Refreshing Jobs. Data on this page automatically refreshes every 15 seconds.

**Access the Console of Refreshing Jobs**

1. Log in as an administrator.
2. Select **Tools > Console** from the Administration menu. The Console of Refreshing Jobs page appears. It shows a table of refresh jobs that are in progress or that have completed.

Refresh jobs are identified in the table by the data source configuration name. The columns in this work area include:

<table>
  <thead>
    <tr>
      <th>Column</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Data Source</td>
      <td>The name of the data source configuration to which the job applies.</td>
    </tr>

    <tr>
      <td>Job Type</td>
      <td>The type of refresh job that was run. Possible types are **Source Refresh** (the data source metadata and all fields were refreshed) and **Field Refresh** (an individual field was refreshed). Field refresh jobs also identify the field that was refreshed in the job type (for example, **Field Refresh \[condition\_code]** indicates that the `condition_code` field was refreshed).</td>
    </tr>

    <tr>
      <td>Status</td>

      <td>
        The status of the job. Possible statuses include:

        <br />

        * **Complete**: The job completed successfully.
        * **In Progress**: The job is running or is scheduled to be run.
        * **Incomplete**: The job only partially completed. For example, the minimum and maximum values were successfully refreshed, but the distinct values were not refreshed.
        * **Failed**: The job could not run or could not be completed due to some error in the system <br /> For example, there may be connection problems with the data store. Select the arrow to view details on the issues that occurred while running the job.
      </td>
    </tr>

    <tr>
      <td>Last Finished</td>
      <td>The date and time when the most recent job completed.</td>
    </tr>

    <tr>
      <td>Next Run</td>
      <td>The date and time when the next job is scheduled.</td>
    </tr>

    <tr>
      <td>Job History</td>
      <td>Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/clock.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=ac00ff96e3e1aaab487ba264b061bd77" alt="" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/clock.png" /> in this column to list all the completed refresh jobs of the selected refresh job type that have been run for the selected data source. The list appears on a pop-up dialog. The dialog shows the start time, finish time and status of the refresh jobs.</td>
    </tr>
  </tbody>
</table>

By default, the table is sorted in order by the Last Finished date and time. You can sort the table by selecting any of the following column headings: **Data Source**, **Job Type**, **Status**, or **Last Finished**. If you select a heading once, the table data sorts in reverse lexicographical order by the selected column heading. Select the heading a second time to sort the data in lexicographical order. The table sort order is automatically reset to the default order every time the table is refreshed.

You can filter the list using any of the column headings. Select the filter icon in the column heading to select for specify an appropriate filter on a pop-up dialog. For example, the pop-up dialog for the Data Source column allows you to select data sources you want to see in the list.

<h2 id="set-up-a-data-source-refresh-job">
  Set Up a Data Source Refresh Job
</h2>

Data source refresh jobs are defined on the Cache tab of a data source configuration. Only one refresh job can be defined for a data source, however you can manually trigger refresh jobs on the [Cache](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab) tab of the data source configuration. See [Trigger Refresh Jobs](#trigger-refresh-jobs).

A refresh job requires you to specify a schedule for the job and, optionally, identify fields for the refresh.

By default, no data refresh jobs are scheduled for a data source. Select **Schedule Refresh Settings** on the Cache tab to set up Periodic or Advanced refresh jobs. An initial data source refresh job is run after the data source has been successfully created and saved. After that, no additional refreshes of the data occur, although you can manually trigger a refresh of the field data. See [Trigger Refresh Jobs](#trigger-refresh-jobs).

* **Periodic**: Select this option to define a refresh job that runs at standard periods.
* **Advanced**: Select this option to define a refresh job using cron expressions. Use this option to define refresh jobs that run on a more complicated schedule.

In addition to the refresh job schedule options, you can select specific fields for the refresh job.

For specific instructions, see one of the following topics:

* [Configure a Periodic Refresh Job](#configure-a-periodic-refresh-job)
* [Configure an Advanced Refresh Job](#configure-an-advanced-refresh-job)
* [Identify Specific Fields for a Refresh Job](#identify-specific-fields-for-a-refresh-job)

<h2 id="configure-a-periodic-refresh-job">
  Configure a Periodic Refresh Job
</h2>

You can configure a periodic refresh job for the data cached for a data source configuration.

**Configure a periodic refresh job for a data source configuration**

1. Log in as a user with the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or a user with **read** and **write** [permission](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions) for the data source.

2. Select the **Sources** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. On the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page, locate and select the data source configuration you want to edit. The Source Creation work area opens.

4. Select the **Cache** tab. All the fields from your data source are listed.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/cache-tab-262-02.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e97e1f8ea17f8cf95d2a66646841a60f" alt="use this work area to define data cache settings, statistics stash settings, schedule refresh settings, enable caching for fields, or manually refresh one or more fields." width="1075" height="782" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/cache-tab-262-02.png" />

5. Select to enable **Schedule Refresh Settings** and select **Periodic** in the pop up. The settings work area for a periodic refresh job appear.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/cache-tab-periodic-710.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=939062981ba3672b93b292b164e36d83" alt="" width="498" height="343" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/cache-tab-periodic-710.png" />

6. Select the time interval for the job to be run using the **Frequency** list. Options **Daily**, **Weekly**, and **Monthly**. Depending on the **Runs** option you select, corresponding options become available in the **Run every** section:

   <table>
     <thead>
       <tr>
         <th>Runs Selection</th>
         <th>Run every Specification</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Daily</td>

         <td>
           Specify the time of day in **Run Time**, and a start and end date for daily runs at that time using the calendar options in **From** and **To**.

           <br />

           The first job runs on the date and time at which you save the data source.

           <br />

           Subsequent jobs continue daily until the last date and time occur.
         </td>
       </tr>

       <tr>
         <td>Weekly</td>

         <td>
           Select the day of the week for the job to be run in **Run on**, time of day in **Run Time**, and a start and end date for weekly runs at the time using the calendar options in **From** and **To**.

           <br />

           The first job runs on the date and time at which you save the data source.

           <br />

           Subsequent jobs continue weekly until the last date and time occur.
         </td>
       </tr>

       <tr>
         <td>Monthly</td>

         <td>
           Specify the number of months between job runs in **Run on**, time of day in **Run Time**, and a start and end date for monthly interval runs at the time using the calendar options in **From** and **To**.

           <br />

           The first job runs on the date and time at which you save the data source.

           <br />

           Subsequent jobs run at the **Run Time** time after the number of months you specify have passed.

           <br />

           For example, if you set your job to run every three months and the **Start on** time is April 4, 2024 at 5:00 a.m., the subsequent job runs on July 4, 2024 at 5:00 a.m.
         </td>
       </tr>
     </tbody>
   </table>

7. Select **Save** to save your changes, then exit the source data configuration when you have finished defining your periodic refresh jobs. A summary of the configuration appears below **Schedule Refresh Settings.**

<Note>
  If you disable **Schedule Refresh Settings**, any schedule you had set up previously is deleted.
</Note>

Select the Schedule Refresh menu button to quickly enable or disable scheduled refreshing for all fields. This is available only if you have enabled **Schedule Refresh Settings** and defined a frequency.

<h2 id="configure-an-advanced-refresh-job">
  Configure an Advanced Refresh Job
</h2>

Using cron expressions, you can specify a more complicated schedule for refresh jobs for the data cached for a data source configuration.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

**Configure an advanced refresh job for a data source configuration using a cron expression**

1. Log in as a user with the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or a user with **read** and **write** [permission](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions) for the data source.

2. Select the **Sources** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. On the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page, locate and select the data source configuration you want to edit. The Source Creation work area opens.

4. Select the **Cache** tab, then enable **Schedule Refresh Settings** and select **Advanced** in the pop up. The settings work area for an Advanced refresh job appear.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/cache-tab-advanced-25-4.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=4dcd44b1b3c2b41fb56344ce9221335a" alt="use the work area to scheudule the refresh settings for your data by creating your own Cron Expression" width="498" height="591" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/cache-tab-advanced-25-4.png" />

5. In the box provided, enter a cron expression that sets the schedule using a string of six fields, each separated by a blank space. The format for the cron expression is:

   ```xml theme={null}
   <seconds> <minutes> <hours> <days of the month> <months> <days of the week>
   ```

   The standard values supported by each field include:

   | Field | Allowed Values | Additional Characters |
   | - | - | - |
   | \<seconds> | 0-59 | , - \* / |
   | \<minutes> | 0-59 | , - \* / |
   | \<hours> | 0-23 | , - \* / |
   | \<days of the month> | 1-31 | , - \* / ? L W |
   | \<months> | 1-12 or Jan-Dec | , - \* / |
   | \<days of the week> | 1-7 or Sun-Sat | , - \* / ? L W # |

   When creating the cron expression, keep the following requirements in mind:

   * Specifying `<seconds>` is optional, but defaults to zero seconds, which ensures that only one refresh job is run. If you specify seconds, the refresh job is rerun after that number of seconds has elapsed.

   * Either the `<days of the month>` or `<days of the week>` field is needed, but both should not be specified. If one of these fields is marked with an asterisk (\*), the other is automatically set to a question mark in the cron expression. In addition, an error is returned if you try to specify both of these fields.

     <Note>
       If you save an existing data source configuration that has both fields specified, no error is returned, but warnings are written to the log when Self-Service Analytics starts.
     </Note>

   * Names for the `<month>` and `<days of the week>` fields are not case sensitive. For example, `FRI` and `fri` are both acceptable formats.

   Special characters that can be specified are described in the table below.

   <table>
     <thead>
       <tr>
         <th>Special Character</th>
         <th>What It Means</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>\*</td>

         <td>
           All values. Represents all the values within the specified field. In the following example, an asterisk is used in the \<minutes> field, indicating that the job will run every minute:

           <br />

           ```
           0 * 0 0 0 0
           ```
         </td>
       </tr>

       <tr>
         <td>?</td>

         <td>
           No specific value. Used as a placeholder when no value is needed in the field. In the following example, the \<months> field value is 6 (June) and the \<days of the week> field value is a question mark, indicating that job runs in June, regardless of the day of the week:

           <br />

           ```
           0 0 0 0 6 ?
           ```
         </td>
       </tr>

       <tr>
         <td>-</td>

         <td>
           Used to specify a range of values. For example, specifying `3-6` in the \<hours> field (as shown in the following example) means the job will run at 3:00, 4:00, 5:00 and 6:00 am:

           <br />

           ```
           0 0 3-6 0 0 0
           ```
         </td>
       </tr>

       <tr>
         <td>,</td>

         <td>
           Used to specify a series of values. Use the comma to identify all the values for the field. In the following example, a comma is used in the \<days of the week> field to run the job on Wednesdays, Thursdays, and Fridays:

           <br />

           ```
           0 0 0 0 0 Wed,Thur,Fri
           ```
         </td>
       </tr>

       <tr>
         <td>/</td>

         <td>
           Used to specify the starting time value and the incremental increase of time. In the following example, specifying 0/5 in the \<minutes> field means that the job runs immediately and then every 5 minutes.

           <br />

           ```
           0 0/5 0 0 0 0
           ```
         </td>
       </tr>

       <tr>
         <td>L</td>

         <td>
           Last. Used only in the \<days of the month> and \<days of the week> fields.

           <br />

           When this character is used standalone, it indicates the last day of the month or the last day of the week (Saturday).

           <br />

           However, when it is used with a value (such as 5L) in the \<days of the month> field, it means the last Friday of the month (5 is Friday, L indicates the last Friday).

           <br />

           ```
           0 0 0 5L 0 0
           ```
         </td>
       </tr>

       <tr>
         <td>W</td>

         <td>
           Weekday. Used only in the \<days of the month> and \<days of the week> fields.

           <br />

           Identifies the weekday closest to the given day. For example, 15W means the closest weekday to the 15th of the month. The following results are possible:

           <br />

           * If the 15th falls on a Saturday, the result returned would be Friday the 14th
           * If the 15th falls on a Sunday, the result is Monday the 16th
           * If the 15th falls on a weekday, that specific day is returned.
         </td>
       </tr>

       <tr>
         <td>#</td>

         <td>
           Number sign. Used only with the \<days of the week> field.

           <br />

           Identifies the specific day of the month. For example, both `Wed#2` and `3#2` identify the second Wednesday of the month.

           <br />

           ```
           0 0 0 0 0 Wed#2
           ```
         </td>
       </tr>
     </tbody>
   </table>

   The following table provides some cron expression examples:

   <table>
     <thead>
       <tr>
         <th>cron Expression</th>
         <th>Meaning</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>
           ```
           0 0 12 * * ?
           ```
         </td>

         <td>Noon every day</td>
       </tr>

       <tr>
         <td>
           ```
           0 30 20 ? * *
           ```
         </td>

         <td>8:30 p.m. every night</td>
       </tr>

       <tr>
         <td>
           ```
           0 0/10 17 * * ?
           ```
         </td>

         <td>Every 10 minutes starting at 5 p.m. and ending at 5:50 p.m., every day</td>
       </tr>

       <tr>
         <td>
           ```
           0 15-30 20 * * ?
           ```
         </td>

         <td>Every minute starting at 8:15 p.m. and ending at 8:30 p.m., every day</td>
       </tr>

       <tr>
         <td>
           ```
           0 45 20 ? * Mon,Wed,Fri
           ```
         </td>

         <td>8:45 p.m. every Monday, Wednesday and Friday</td>
       </tr>

       <tr>
         <td>
           ```
           0 0 20 3/3 * ?
           ```
         </td>

         <td>8 p.m. every 3 days in every month, starting on the third day of the month</td>
       </tr>
     </tbody>
   </table>

6. Select **Save** to save your changes, then exit the source data configuration when you have finished defining your periodic refresh jobs. A summary of the configuration appears below **Schedule Refresh Settings.**

<Note>
  If you disable **Schedule Refresh Settings**, any schedule you had set up previously is deleted.
</Note>

Select the Schedule Refresh menu button to quickly enable or disable scheduled refreshing for all fields. This is available only if you have enabled **Schedule Refresh Settings** and defined a frequency.

<h2 id="identify-specific-fields-for-a-refresh-job">
  Identify Specific Fields for a Refresh Job
</h2>

You can select specific fields to be refreshed by a data source refresh job using the Configuration section of the [Refresh](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab) tab.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

**Select specific fields for a refresh job for a data source configuration**

1. Log in as a user with the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or a user with **read** and **write** [permission](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions) for the data source.

2. Select the **Sources** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. On the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page, locate and select the data source configuration you want to edit. The Source Creation work area opens.

4. Select the **Cache** tab. All the fields from your data source are listed.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/cache-tab-262-02.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e97e1f8ea17f8cf95d2a66646841a60f" alt="use this work area to define data cache settings, statistics stash settings, schedule refresh settings, enable caching for fields, or manually refresh one or more fields." width="1075" height="782" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/cache-tab-262-02.png" />

5. To refresh all the fields in your data source, select the refresh button for Manual Refresh to trigger a manual refresh for all fields.

6. Otherwise, select the refresh button for specific fields. Exit the source data configuration when you have finished triggering all of your manual refreshes.

<h2 id="trigger-refresh-jobs">
  Trigger Refresh Jobs
</h2>

Self-Service Analytics maintains data source metadata and, optionally, a cached result set of the data from the data store for each data source configuration you define. When you initially connect to your data store using a data source configuration, a sampling of the data is collected to determine:

* Distinct values for all fields with ATTRIBUTE and NUMBER field types.
* The minimum and maximum values for all fields with number or time data types for which [Custom Ranges](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#filter-values-panel-fields-tab) have not been defined.

Self-Service Analytics administrators can define refresh jobs for this cached data. The following table identifies the types of refresh jobs that are currently supported, the triggers for the jobs, and the activities that occur when the job is run.

<table>
  <thead>
    <tr>
      <th scope="col">Refresh Type</th>
      <th scope="col">Trigger</th>
      <th scope="col">Activities</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td rowSpan={3}>Source Refresh</td>
      <td>An initial connection to a data source is saved. See [Define a Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#define-a-source).</td>
      <td rowSpan={3}>The Self-Service Analytics cache is cleared and the minimum and maximum values for non-attribute fields and distinct values for attribute and number fields are refreshed.</td>
    </tr>

    <tr>
      <td>Changes to the [Source Creation Work Areas](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-source-creation-tab) or [Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) tab in the data source configuration are saved. See [Edit a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source).</td>
    </tr>

    <tr>
      <td>The scheduled refresh time (set on the [Cache](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab) tab in the data source configuration) occurs. See [Set Up a Data Source Refresh Job](#set-up-a-data-source-refresh-job).</td>
    </tr>

    <tr>
      <td>Field Refresh</td>

      <td>
        * To refresh the entire list of fields in a data source configuration, access the [Cache](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab) tab and select the refresh (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/refresh-field-button.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=f7b35df88bf64ec08419feda8123e37a" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/refresh-field-button.png" />) button for Manual Refresh in the table heading to trigger a manual refresh for all fields. This triggers a manual refresh of all the field data.
        * To refresh a specific field in a data source, access the [Cache](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab) tab and select the Manual Refresh button (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/refresh-field-button.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=f7b35df88bf64ec08419feda8123e37a" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/refresh-field-button.png" />) for the field you want to refresh. This triggers an immediate manual refresh for the selected field.
      </td>

      <td>The minimum and maximum for non-attribute fields and distinct values for attribute and number fields are refreshed.</td>
    </tr>

    <tr>
      <td>After Cache Cleanup</td>

      <td>
        When a user selects an available Cache Cleanup option from the Actions column for a data source on the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page.

        <br />

        See [Clear the Cache for a Data Source Configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#clear-the-cache-for-a-data-source-configuration).
      </td>

      <td>The data is freshly loaded into the Self-Service Analytics cache the next time it is requested from the data source.</td>
    </tr>
  </tbody>
</table>

<Note>
  If a [Custom Range](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#filter-values-panel-fields-tab) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab).
</Note>

<Note>
  When you add a new field to a data source, the scheduled refresh is not enabled for the new fields by default. Quickly enable scheduled refresh for all fields using the bulk update option in the [Schedule Refresh menu on the Cache](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab) tab, or enable each field for scheduled refresh manually on the Cache tab.
</Note>

The status of refresh jobs can be reviewed on the Console of Refreshing Jobs. See Review Refresh Jobs.
