---
title: "Updating to the Latest Version (Potentially Breaking Changes)"
id: 5281637050775
section: "Release Notes"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281637050775-Updating-to-the-Latest-Version-Potentially-Breaking-Changes
updated_at: 2024-08-22T13:06:37Z
---

# Updating to the Latest Version (Potentially Breaking Changes)

# Updating to the Latest Version (Potentially Breaking Changes)

When updating Exago BI, consult this guide for potential breaking changes. Note that when updating from more than one version behind the current one, information from that section and all sections above it will apply.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323101299991 "Note")
>
> Also see **[Updating Recommendations](https://devnet.logianalytics.com/hc/en-us/articles/5281618359959-Updating-Recommendations)** to ensure a smooth updating process.

If the version is not listed, then a direct update path to the latest version is not supported. Please file a support request for further assistance.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323101299991 "Note")
>
> To ensure a smooth upgrade when overwriting a previous installation, ensure that the web server (IIS/Apache/NGINX), the **Monitoring Service**, and any Scheduling Services are turned off before running the installer.

## User Interface, API and Breaking Changes

### Updating from *v2024.2.1* and earlier

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25323101304215 "Critical") **Important:**
>
> As of v2024.2.1, CData drivers are no longer available for use in Exago BI products. See **[CData Drivers](https://devnet.logianalytics.com/hc/en-us/articles/5281585000599)**.
>
> * With this removal, the following databases are not currently supported:
>   + Elasticsearch
>   + Google BigQuery
>   + MongoDB
>   + Redshift
>   + Snowflake

### Updating from *v2021.2.2* or earlier

#### GlobalNumericFormat() Changes

1. The [GlobalNumericFormat()](https://devnet.logianalytics.com/hc/en-us/articles/5281599710103-Arithmetic-and-Geometric-Functions#GlobalNu) function now returns a string instead of a numeric value, as is expected.
2. GlobalNumericFormat() is now found in the [Arithmetic & Geometric Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281599710103-Arithmetic-and-Geometric-Functions) category in all currently supported versions of the application.

### Updating from *v2021.1* or earlier

This section applies to any maintenance release version of *v2021.1*.

#### Today() and Now() Date Functions Use the End-User Locale

Prior to *v2021.2.0*, the return value for these functions was based off the server’s time. Now, the return value is based on the end-users locale, set by the Culture Settings in the user session. For more information, see [Culture Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281607969943-Culture-Settings) and [Date Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281584402455-Date-Functions).

There are some additional effects of this change:

* The **Admin Console** > **General Settings** > **Culture Settings** > **Server Time Zone Offset** no longer accepts `null` as a value.
* A new [Hidden Flags](https://devnet.logianalytics.com/hc/en-us/articles/5281607060631-Hidden-Flags) named **UseExternalTimeZoneConverter** when *True* takes the place of setting **Server Time Zone Offset** to `null`. This should only be set to *True* to support legacy use of the External Interface, otherwise it should be left as *False*. The External Interface is a deprecated extensibility feature. However, those using the External Interface to do time zone conversion need to adjust the **Server Time Zone Offset** and setting **UseExternalTimeZoneConverter** *True*.

#### Updated Snowflake CDATA driver

The Snowflake CDATA driver has been updated from version 20.0.7768.0 to version 21.0.7887.0. If you need more product information, including new purchases and upgrades, contact your Exago Customer Success Manager.

#### New dbconfigs.json and dbconfigs.overrides.json Schema for the FormulaDictionary

The schema for the **FormulaDictionary** section of the `dbconfigs.json` and `dbconfigs.overrides.json` files has changed to allow for multiple properties to be included for some of the function translations. Environments that have included customization for the SQL translations with the `dbconfigs.overrides.json` should review [Writing SQL Translations](https://devnet.logianalytics.com/hc/en-us/articles/5281628373655-Database-Settings#Writing) and [Managing the dbconfigs.json File](https://devnet.logianalytics.com/hc/en-us/articles/5281593110167-Managing-the-dbconfigs-json-File).

#### Change to Column Alias Handling in SQL Generation

During SQL generation, Exago assigns column aliases in the SELECT clause. In *v2021.1.0,* the SQL generation engine uses those column aliases in the ORDER BY clause. This results in more compact and neat SQL generated.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323101299991 "Note")
>
> The column aliases set as part of the Column Metadata are different from the column aliases that the SQL generation engine uses.

##### Example of SQL Generated Prior to *v2021.1.0*

Copy

```
SELECTDISTINCT (CASEWHEN ((Northwind.[CATEGORIES].[CATEGORYID] =3) OR (Northwind.[CATEGORIES].[CATEGORYID] =5)) THEN1ELSE0END) AS c0<  
FROM Northwind.[CATEGORIES]  
WHERE (CASEWHEN ((Northwind.[CATEGORIES].[CATEGORYID] =3) OR (Northwind.[CATEGORIES].[CATEGORYID] =5)) THEN1ELSE0END) ISNOTNULL  
ORDERBY (CASEWHEN ((Northwind.[CATEGORIES].[CATEGORYID] =3) OR (Northwind.[CATEGORIES].[CATEGORYID] =5)) THEN1ELSE0END) ASC  
LIMIT100
```

```
SELECT DISTINCT (CASE WHEN ((Northwind.[CATEGORIES].[CATEGORYID] = 3) OR (Northwind.[CATEGORIES].[CATEGORYID] = 5)) THEN 1 ELSE 0 END) AS c0<
FROM Northwind.[CATEGORIES]
WHERE (CASE WHEN ((Northwind.[CATEGORIES].[CATEGORYID] = 3) OR (Northwind.[CATEGORIES].[CATEGORYID] = 5)) THEN 1 ELSE 0 END) IS NOT NULL
ORDER BY (CASE WHEN ((Northwind.[CATEGORIES].[CATEGORYID] = 3) OR (Northwind.[CATEGORIES].[CATEGORYID] = 5)) THEN 1 ELSE 0 END) ASC
LIMIT 100
```

##### Example of SQL Generated After *v2021.1.0*

Note in this example, that the column alias **c0** for the `SELECT` clause is then referenced in the `ORDER BY` clause, instead of repeating the entire `SELECT` clause.

```
SELECT DISTINCT (CASE WHEN ((Northwind.[CATEGORIES].[CATEGORYID] = 3) OR (Northwind.[CATEGORIES].[CATEGORYID] = 5)) THEN 1 ELSE 0 END) AS c0
FROM Northwind.[CATEGORIES]
WHERE (CASE WHEN ((Northwind.[CATEGORIES].[CATEGORYID] = 3) OR (Northwind.[CATEGORIES].[CATEGORYID] = 5)) THEN 1 ELSE 0 END) IS NOT NULL
ORDER BY c0 ASC
LIMIT 100
```

#### Custom Function Category Names Must Be Translated

When creating [Custom Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281628193815-Custom-Functions) or [Custom Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281616754327-Custom-Aggregate-Functions) with a custom category name via the Admin Console, the category name must be specified by a [Modifying Select Language Elements](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support#Modifyin). Put another way, names for custom category names must exist in the language files, and using a static text string in the **Specify Category Name** field is not acceptable. Any environment utilizing a custom category name should immediately translate the category name and update the configuration to use the language file ID instead. Leaving static text strings for a custom category name can cause parts of the application to stop working.

### Updating from *v2021.1.16* or earlier

#### New Hidden Flag to Stop Export if File Size is Exceeded

When a report is exported, either through the user interface, or with a GetExecute() method, if the size of the file exceeds value of the new hidden flag `<general><maxexportfilesizebytes></general>` number of bytes, report execution is canceled and a message is displayed to the end user. The default value is *0*, dabling this limit. Any positive integer value is is accepted, including *0*.

For more information, see [Executing Reports with the API](https://devnet.logianalytics.com/hc/en-us/articles/5281660714135-Executing-Reports-with-the-API).

### Updating from *v2021.1.15* or earlier

#### New SMTP Library for Scheduler Service

The Scheduler Service employs a new SMTP library. Unless otherwise specified in the [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration) file, the Scheduler defaults connections to port 587 over TLS.

#### New Hidden Flag to Stop Report Execution if Database Row Limit is Exceeded

When the **Admin Console** > **General** > **Database Settings** > **Database Row Limit** is exceeded, and the new hidden flag `<errorondbrowlimitexceeded>` is *True*, report execution is canceled and an error message is displayed to the user. For scheduled reports, the execution abends and an error message email is sent to the administrator (if so configured). The default value is *False*. For more information, see [Hidden Flags](https://devnet.logianalytics.com/hc/en-us/articles/5281607060631-Hidden-Flags), [Database Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281628373655-Database-Settings) and [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration).

### Updating from *v2021.1.14* or earlier

#### /rest/SchedulesV2 objects updated

A new `ParentJobId` field has been added to the **[Schedule JSON](https://devnet.logianalytics.com/hc/en-us/articles/5281646521623-REST-SchedulesV2#Schedule)** and **[ScheduleListItem JSON](https://devnet.logianalytics.com/hc/en-us/articles/5281646521623-REST-SchedulesV2#Schedule2)** objects in the [REST — SchedulesV2](https://devnet.logianalytics.com/hc/en-us/articles/5281646521623-REST-SchedulesV2) endpoints.

### Updating from *v2021.1.13* or earlier

#### Optional `successCallback` Available for Some JavaScript API Functions

The **EditReport**, **NewReport**, **ScheduleReportManager** and **ScheduleReportWizard**JavaScript API functions now support an optional `successCallback` function. For more information, see [JavaScript API](https://devnet.logianalytics.com/hc/en-us/articles/5281628892055-JavaScript-API)

### Updating from *v2021.1.10* or earlier

#### RedShift CDATA Driver

The Redshift CDATA driver has been updated from version 20.0.7654.0 to version 21.0.7872.0. If you need more product information, including new purchases and upgrades, contact your Exago Customer Success Manager.

#### New Language File Element

Added new language file element `DashboardVizChartTypeLbl` to translate the **Chart Type** label in the Dashboard Designer

#### JavaScript API ExecuteReport() Function

The `ExecuteReport()` function in the [JavaScript API](https://devnet.logianalytics.com/hc/en-us/articles/5281628892055-JavaScript-API) now supports calling reports by the report ID. To accomplish this, an additional Boolean argument has been added to the function call.

### Updating from *v2021.1.8* or earlier

#### New Licenses Directory

A new `/Licenses` directory is installed with the Web Application. This directory contains copies of license agreements for all third party components included with Exago.

#### Completed Scheduler Service Jobs Now Automatically Flush

Prior to this version, the [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration) was set to *-1*. This disabled automatic flushing of completed jobs. With this version, this setting now defaults to *24*, so completed jobs flush automatically every 24 hours.

### Updating from *v2021.1.7* or earlier

#### New **Max Chained Report Collation Executions** Configuration Setting

A new configuration setting, found in **Admin Console** > **General** > **Other Settings** > **Max Chained Report Collection Executions** places a limit on the number of individual report executions caused when executing a collated chained report. For more information how this setting works, review [Chained Reports](https://devnet.logianalytics.com/hc/en-us/articles/5281546622615-Chained-Reports) and [Other Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281608505879-Other-Settings).

This new setting is available in the .NET API General object, the [REST — Config Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281669713431-REST-Config-Settings) and [Config File XML & API Setting Reference (General Nodes)](https://devnet.logianalytics.com/hc/en-us/articles/5281643841175-Config-File-XML-API-Setting-Reference-General-Nodes-).

#### Native Support for SQLite as a Reportable Data Source Type

SQLite Data Sources may now be added to the application just as any other supported data source can with an included ADO.NET driver.

### Updating from *v2021.1.6* or earlier

#### New maxRasterizationsBeforeReset Application Setting

The Web Application’s `appSettings.config` and the Scheduler Service’s `WebReportsScheduler.exe.config` files now include a new setting called `maxRasterizationsBeforeReset`. This setting tells Exago when to dispose of Puppeteer chart rendering pages. After this number of executions on the page, the process will be killed and a new one created for further rendering. See [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings) for more information.

### Updating from *v2021.1.5* or earlier

#### Abended Scheduled Jobs now Flushed Automatically

Prior to this version, scheduled jobs that *Abended* would not be cleared when flushing the Scheduler Service job files. After updating, Abended jobs will be available for flushing after the Scheduler Service’s `<flush_time>` timeout lapses.

#### **Schema Access Type** Now Honored for Vertical Tables

Prior to this version, Exago BI always queries the Data Source for the schema of a Vertical Table, regardless of the setting of the **Schema Access Type** dropdown for the Data Object. After updating, if the **Schema Access Type** is *Metadata*, the schema will be read from the configuration file. This has the potential to break reports if they are referencing columns not included in the object’s metadata.

After updating, verify that all [Column Metadata](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Column2) exists for all columns of a vertical table.

### Updating from *v2021.1.4* or earlier

#### Report Viewer Interactive Dock Change

The [Interactive Dock](https://devnet.logianalytics.com/hc/en-us/articles/5281541805591-Report-Viewer#Interact) now defaults to the right side of the screen when opened. This setting can be reverted back to the previous left-hand position with the **Admin Console** > **General** > **Feature/UI Settings** > **Interactive report viewer default dock placement** setting.

### Updating from *v2021.1.1* or earlier

#### Scheduler Service Configuration File Change

The `<default_job_timeout>` setting in the [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration) is now deprecated. Use `<max_job_execution_minutes>` exclusively to limit schedule execution.

A new setting, `<smtp_timeout>` is now available to set the SMTP server connection timeout in place of `<default_job_timeout>`.

### Updating from *v2021.1.0* or earlier

This section applies when upgrading from any maintenance release version of *v2021.1*.

#### `/rest/Schedules` Replaced

The `/rest/Schedules` endpoints are now deprecated.

Clients using the REST Web Service API to create, modify or delete scheduled reports should upgrade to the new `/rest/SchedulesV2` endpoints as soon as possible. The legacy `/rest/Schedules` endpoints will be removed in a future version of Exago.

#### **Allow Editing ExpressView with Live Data** now defaults to *True*

The default value for **Admin Console** > **General** > [Feature/UI Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281644433431-Feature-UI-Settings) > **Allow Editing ExpressView with Live Data** has been changed from *False* to *True*.

### Updating from *v2020.1* or earlier

This section applies when upgrading from any minor version of *v2020.1* (for example *v2020.1.0*, *v2020.1.5*, etc…)

#### Storage Management Changes

##### New content.associated\_reports Column

A new associated\_reports column has been added to the Storage Management content table, containing a comma-separated list of content\_ids for each report that is associated with a particular content record.

Reports become associated with others when they are components in a composite report such as Chained Report or Dashboard, or if an Advanced Report contains links to other reports (a.k.a. drilldowns).

The **Update Reports** function in the Admin Console reads the contents of a Storage Management database, parses the report file contents and generates the comma separated lists of **associated\_reports** where applicable.

Clicking the **Update Reports** button in the Admin Console is a required part of the upgrade process for all clients when updating to *v2021.1.*

##### Access Flags Active

The **access flags** built in to the **Storage Management** system have been made active. In addition, the access flags themselves have been changed from their original definition in the *v2020.1* release.

Review the [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction) and [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema) topics for a definition of the new access flags and their locations in the bitmap.

New **Default Access Permission** controls in the **Admin Console** allow an administrator to set the default permissions when new content is created. This value can be changed with the .NET or REST Web Service API or by changing the configuration file.

As some of the access flags bits have changed meaning, some features in the application may inadvertently become unavailable or vice versa. The following SQL statement may be run to upgrade all reports in any existing database to keep full access prior to the upgrade:

```
UPDATE content_access SET access_flags = 2047 WHERE access_flags = 511
```

Review the table below for a comparison of the flag bit definitions:

| *v2020.1* | *v2021.1* |
| --- | --- |
| reserved for future use | reserved for future use |
| reserved for future use | reserved for future use |
| reserved for future use | reserved for future use |
| reserved for future use | reserved for future use |
| reserved for future use | reserved for future use |
| reserved for future use | CanMove |
| reserved for future use | CanSchedule |
| CanView | CanView |
| CanDownload | removed — reserved for future use |
| CanCopy | CanCopy |
| CanExecute | removed — reserved for future use |
| CanDelete | CanDelete |
| CanShare | CanShare |
| CanRename | CanRename |
| CanSave | removed — reserved for future use |
| CanEdit | CanEdit |

The [ContentPermission v2021.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#ContentP) enum type is also affected by this change.

##### `-o` LoadReportsToDb Command Line Switch Added

A new `-o` command line switch has been added to the **LoadReportsToDb** Storage Management transitioning utility. This allows a user to specify a value for the database driver’s `CommandTimeout` property. Review [LoadReportsToDb](https://devnet.logianalytics.com/hc/en-us/articles/5281647090839-Storage-Management-Transitioning-from-Legacy-Storage-Methods#LoadRepo) in the [Storage Management: Transitioning from Legacy Storage Methods](https://devnet.logianalytics.com/hc/en-us/articles/5281647090839-Storage-Management-Transitioning-from-Legacy-Storage-Methods) topic.

#### ExpressView Changes

##### ExpressView Themes

With changes to the the **ExpressView Designer**, all new themes have been created. Legacy ExpressView themes are no longer supported.

The new ExpressView themes will need to be loaded into the Storage Management database. For existing installations, this can be done in the **Admin Console** > [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management) by clicking on the **Load Themes** button. Skipping this step will result in there being no themes available in the ExpressView Designer, even if themes were available before updating.

Creating custom ExpressView themes is possible, by manually editing the JSON theme content. The schema has changed, but is documented in the [Create a Custom ExpressView Theme (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281620732183-Create-a-Custom-ExpressView-Theme-v2021-1-) topic. It is not possible to create an ExpressView theme from the designer.

To remove the legacy themes from the Storage Management database (not required), execute the following SQL statements:

```
DELETE FROM content_access WHERE content_id IN (SELECT content_id FROM content WHERE content_attribute = ‘ExpressView’);
DELETE FROM content WHERE content_attribute = ‘ExpressView’
```

##### Formatting

In addition to the theme changes noted above, the content formatting controls (for example bold, italic, underline, alignment, etc…) have been re-worked.

Opening an ExpressView in the new designer will reset all formatting to the system defaults, where any customization can be reapplied as desired with the tools available. Some styling options have been changed to a report-wide setting (for example font type) or are no longer available (for example font size)

##### Tutorial Mode and Hints Removed

The **Tutorial Mode** and **ExpressView Hints** have been removed from the application, and their Admin Console and configuration file nodes have been eliminated.

##### Maximum of 7 ExpressView Groups

The ExpressView Designer will now enforce a limit of seven **group columns** on a single report for performance. The 7th group will need to be demoted to a detail field before it can be replaced with a new one.

ExpressViews created in previous versions with more than 7 groups will still be editable and executable in *v2021.1*, but no more groups may be added until the number of groups is less than 7.

#### Default Filter Execution Window Change

The default value for the **Admin Console** > **General** > **Filter Settings** > **Default Filter Execution Window** has changed from *Standard* to *Simple Without Operator*.

In environments where no value had been previously set for this setting, the *Simple Without Operator* filter execution window will be displayed for all Advanced Reports, Dashboards and Chained Reports with prompting filters after this update.

This setting can be overridden on the report-level (if **Admin Console** > **General** > **Filter Settings** > **Allow User to change Filter Window** is *True*) by changing the **Filter Execution Window** setting in the Report Designer’s **Advanced** > **Report Options** dialog, or on an application-wide level by changing the aforementioned Admin Console setting.

Learn more in the [Filter Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281628457495-Filter-Settings) topic.

#### Advanced Report Changes

##### Advanced Report Wizard Removed

The **Advanced Report Wizard** has been removed from the application. Creating a new Advanced Report from the main menu or Getting Started page will directly start the Advanced Report Designer and prompt the user to add Data Objects (formerly Categories) to the report to begin report building.

The **helpKeys** related to the wizard for creating [Custom Context Sensitive Help](https://devnet.logianalytics.com/hc/en-us/articles/5281597846295-Custom-Context-Sensitive-Help) have been removed from the application.

#### Toolbar Changes

##### AutoSum Sum.png Icon Now Hidden by Default

The **AutoSum**![Sum.png](https://devnet.logianalytics.com/hc/article_attachments/5432230783511) icon from the Advanced Report Designer’s toolbar is now disabled by default. A new configuration setting, **Admin Console** > **General** > **Feature/UI Settings** > **Show Auto Sum Button** allows the button to be enabled on an application-level or session-level basis. The default value is *False*.

Users are encouraged to use aggregate functions in place of the AutoSum feature. For example, these two reports produce the same output:

![5EoVqMbX6r.png](https://devnet.logianalytics.com/hc/article_attachments/5432236567063)


Using the AggSum aggregate function to compute the sum of the Donations.Amount data field on the Group and Report level

![2Gw8DI3j3V.png](https://devnet.logianalytics.com/hc/article_attachments/5432183475607)


Using the AutoSum feature (toolbar icon not shown) to compute the sum of the Donations.Amount data field on the Group and Report level

The **AutoSum**![Sum.png](https://devnet.logianalytics.com/hc/article_attachments/5432230783511) icon will be deprecated in a future version.

#### Actionable User Interface Item Changes

Some of the Actionable User Interface Items on the toolbar have either been removed or replaced. Review [Actionable UI Elements](https://devnet.logianalytics.com/hc/en-us/articles/5281613121175-Actionable-UI-Elements) to see all of the changes. Action Events that use these items may break if they reference elements with new names or elements that are no longer available.

#### Default Theme Colors Changed

The colors of the *Default* theme have been changed. This new theme is WCAGAA Compliant and color blind accessible.

#### Single Series Chart Theme Change

New themes have been introduced for charts. In addition, theme color now corresponds with a series, instead of a value. Bar, Stacked Bar, Column, Stacked Column, Pareto, Spark Column, Scatter, Zoom Scatter and Bubble Charts are affected by this change.

![PKbtSrMDN3.png](https://devnet.logianalytics.com/hc/article_attachments/5432236638871)


A single series column chart *pre-v2021.1*

#### ETL Removed

The **ETL** feature has been removed.

Review [Configuration File Changes](#Configur) at the bottom of this topic for notes about Scheduler Service and Web Application configuration file nodes that have been removed.

The folder with the ETL Transforms may be safely removed. This code sample can be used to remove the ETL\_TRANSFORMS folder and any transforms in it on a Microsoft SQL Server Storage Management database. Run the statements one at a time.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323101299991 "Note")
>
> Change both instances of *ETL\_TRANSFORMS* in the `WHERE` causes below to the name of the actual ETL Transforms directory. This can be found in the **Admin Console** > **General** > **ETL Settings** > **ETL Transforms Folder** setting.
>
> Change the names of the **content** and **content\_access** tables in the statements below to the actual names of those tables in the database, where applicable.

```
-- Add a flag column
ALTER TABLE content ADD ETL_FLAG INT
 
-- Set the flag for content in the specified folder
UPDATE content SET ETL_FLAG=1 FROM content WHERE content.content_id IN (SELECT content_id FROM content_access WHERE parent_id = (SELECT content_id FROM content WHERE name = ‘ETL_TRANSFORMS’))

-- List the items we are going to delete
SELECT * FROM content WHERE ETL_FLAG = 1

-- Delete all the content access records for content in the folder
DELETE FROM content_access WHERE parent_id = (SELECT content_id FROM content WHERE name = ‘ETL_TRANSFORMS’)

-- Delete the content records for those items flagged which don’t have another access record
DELETE FROM content FROM content INNER JOIN content_access ON content.content_id = content_access.content_id WHERE ETL_FLAG = 1 AND content_access.content_id IS NULL

-- and report those items we did not delete
SELECT * FROM content WHERE ETL_FLAG=1
```

The transform folder can now be removed from the database.

### Updating from *v2020.1.22* or earlier

#### New Language File Element

Added new language file element `DashboardVizChartTypeLbl` to translate the **Chart Type** label in the Dashboard Designer

#### JavaScript API ExecuteReport() Function

The `ExecuteReport()` function in the [JavaScript API](https://devnet.logianalytics.com/hc/en-us/articles/5281628892055-JavaScript-API) now supports calling reports by the report ID. To accomplish this, an additional Boolean argument has been added to the function call.

### Updating from *v2020.1.15* or earlier

#### **Schema Access Type** Now Honored for Vertical Tables

Prior to this version, Exago BI always queries the Data Source for the schema of a Vertical Table, regardless of the setting of the **Schema Access Type** dropdown for the Data Object. After updating, if the **Schema Access Type** is *Metadata*, the schema will be read from the configuration file. This has the potential to break reports if they are referencing columns not included in the object’s metadata.

After updating, verify that all [Column Metadata](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Column2) exists for all columns of a vertical table.

### Updating from *v2020.1.13* or earlier

#### Scheduler Service Configuration File Change

The `<default_job_timeout>` setting in the Scheduler Service Configuration File is now deprecated. Use `<max_job_execution_minutes>` to limit schedule execution.

A new setting, `<smtp_timeout>` is now available to set the SMTP server connection timeout in place of `<default_job_timeout>`.

### Updating from *v2020.1.12* or earlier

#### `/rest/Schedules` Replaced

The `/rest/Schedules` endpoints are now deprecated.

Clients using the REST Web Service API to create, modify or delete scheduled reports should upgrade to the new `/rest/SchedulesV2` endpoints as soon as possible. The legacy `/rest/Schedules` endpoints will be removed in a future version of Exago BI.

### Updating from *v2020.1.1* or earlier

* The **MongoDB CDATA** driver has been updated from version 19.0.7202.0 to version 20.0.7524.0. If you need more product information, including new purchases and upgrades, contact your Exago Customer Success Manager.
* A bug fix to the `/rest/Schedules/` endpoint now includes the full report path when making standard and BATCH calls on Linux. This change only affects Linux, as the full report path was always returned on Windows. For example:

```
"ReportName": "Parameter Report"
```

```
"ReportName": "My Reports\Advanced Reports\Parameters\Parameter Report"
```

### Updating from *v2019.2* or earlier

This section applies when upgrading from any minor version of *v2019.2* (for example *v2019.2.0*, *v2019.2.11*, etc…)

#### Storage Management

Exago BI’s **Storage Management** system replaces the legacy file system, cloud storage, folder management and web service (SOAP) storage methods with a relational database. All reports, templates, folders and themes are stored in this database. Out-of-the-box, Exago BI provides a SQLite database. Microsoft SQL Server, MySQL, Oracle and PostgreSQL are also supported.

As of *v2020.1*, the legacy storage methods are deprecated and have been replaced with the Storage Management system. All clients upgrading to *v2020.1* will need to change their content storage strategy to the Storage Management system. Exago has built-in several handy utilities for this transitioning process, as well as an interface for implementing a customized Storage Management system.

More information about Storage Management and transitioning a legacy storage system to it can be found in these topics:

* [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
* [Storage Management: Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started)
* [Storage Management: Transitioning from Legacy Storage Methods](https://devnet.logianalytics.com/hc/en-us/articles/5281647090839-Storage-Management-Transitioning-from-Legacy-Storage-Methods)
* [Storage Management: Custom Implementation](https://devnet.logianalytics.com/hc/en-us/articles/5281646850327-Storage-Management-Custom-Implementation)

##### User Identification and Permissions

When creating a user session with one of the APIs, in addition to setting the @userId@ and @companyId@ system parameters, there are four new Storage Management Identity keys that should also be set.

Details about these keys and how to set them can be found in the [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction) and [Navigating the Application](https://devnet.logianalytics.com/hc/en-us/articles/5281546800023-Navigating-the-Application) topics.

When transitioning to Storage Management, a new permissions model is available. Learn more in [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction) and [Storage Management: Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started).

##### User Interface Changes

The Storage Management system is virtually transparent to the end user, with two exceptions:

1. A new **Owner**![TreeReportOwned.png](https://devnet.logianalytics.com/hc/article_attachments/25323117403415) icon will appear in the Report Tree if a user owns that content. Content ownership is a new concept in the Storage Management system. More information can be found in the Storage Management: Introduction link above.
2. If the Owner of content moves it to a different folder, a new dialog will appear asking the user to copy the permissions of the new folder to the content or to keep the permissions of the content.

More information can be found in the [Navigating the Application](https://devnet.logianalytics.com/hc/en-us/articles/5281546800023-Navigating-the-Application) topic.

##### Caching Settings Moved

Several settings for caching in the applications have been moved in the **Admin Console** and configuration file.

* **General** > **Other Settings** > **Enable Report List Caching** has moved to **Storage Management** > **Enable Report List Caching**
* **General** > **Other Settings** > **Enable Report XML Caching** has moved to **Storage Management** > **Enable Report XML Caching**
* **General** > **Other Settings** > **Report XML Caching Timeout (s)** has moved to **Storage Management** > **Enable Report XML Caching Timeout**

##### New Caching Setting

The Theme List is now cached with the Storage Management system. A new **Storage Management** > **Theme List Caching Timeout** setting determines when the theme list cache expires.

#### Puppeteer Rendering Libraries Enabled by Default

The **Puppeteer** visualization rendering libraries were introduced into Exago BI*v2019.1.5* but were not enabled by default. Now in *v2020.1*, they have been enabled for all installations by default in place of the legacy **wkHtmltoImage** libraries.

Clients using Docker containers or Azure App Services may need to flip the `useWkHtmlToImage` flag back to *True* in the [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings) for both the Web Application and the Scheduler Service as Puppeteer is not compatible with these types of environments.

Clients using the .NET API to integrate Exago need to add a reference to `ExagoPuppeteerRasterizer.dll` located the Exago Web Application’s `bin` directory to their application.

#### Linux Installer No Longer Includes MySQL ADO.NET Driver

The Exago BI Linux Installer will no longer install a MySQL ADO.NET driver at the time of installation. Instead, clients wishing to use a MySQL data source for either reporting or for Storage Management will need to provide their own.

Exago has provided wrappers around two popular MySQL data drivers that clients may choose to install on their own.

* Devart dotconnect free edition
* MySQL ADO.NET

If you need more product information, including new purchases and upgrades, contact your Exago Customer Success Manager.Install the driver by extracting the contents of the download and then running either `installMySql.sh` or `installDevartMySql.sh` as root. Provide the Exago installation path to the installer script. For example:

```
sudo ./installDevartMySql.sh /opt/Exago
```

Once installed, update the **Admin Console** > **General** > [Database Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281628373655-Database-Settings) to reflect the new data provider.

#### System.Data.OracleClient Driver No Longer Supported on Linux

The System.Data.OracleClient driver, which also required the external Oracle Command Line Interface to be installed, is longer supported on Linux.

The Oracle.ManagedDataAccess.Client driver can be used instead. Exago has provided a wrapper that clients may use to install Oracle.ManagedDataAccess.Client on their own.

If you need more product information, including new purchases and upgrades, contact your Exago Customer Success Manager. Install the driver by extracting the contents of the download and then running `installOracle.sh` as root. Provide the Exago installation path to the installer script. For example:

```
sudo ./installOracle.sh /opt/Exago
```

Once installed, update the **Admin Console** > **General** > [Database Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281628373655-Database-Settings) to reflect the new data provider.

#### Several Action Events Now Support Promises

Synchronous calls to `Utilities.AjaxRequest` are no longer supported. As a workaround, the Action Events below have been upgraded to allow returning Promises, allowing asynchronous calls instead:

* OnRightClickReport
* OnRenameReport
* OnEditReport
* OnDeleteReport
* OnDuplicateReport
* OnExecuteReport
* OnSelectReport
* OnDoubleClickReport

Action Event Code that makes synchronous calls to `Utilities.AjaxRequest` such as this example:

```
// Do some stuff
const value = Utilities.AjaxRequest(Utilities.AjaxRequest("web.method.name", data);
// Do some other stuff
```

Will need to be changed to make the call asynchronous:

```
// Do some stuff
Utilities.AjaxRequestAsync("web.method.name", data).then((value) => { /* Do some other stuff */ });
//Do some other stuff
```

or

```
// Do some stuff
const value = await Utilities.AjaxRequestAsync("web.method.name", data);
//Do some other stuff
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323101299991 "Note")
>
> If a success callback is passed to `Utilities.AjaxRequest` as in the example below, this already behaves asynchronously so no change is needed.
>
> ```
> Utilities.AjaxRequest(Utilities.AjaxRequest("web.method.name", data, () => console.log("It worked!"));
> ```

For more information, review [Global Action Events](https://devnet.logianalytics.com/hc/en-us/articles/5281621334167-Global-Action-Events)

### Updating from *v2019.2.40* or earlier

Added new language file element `DashboardVizChartTypeLbl` to translate the **Chart Type** label in the Dashboard Designer

### Updating from *v2019.2.34* or earlier

#### **Schema Access Type** Now Honored for Vertical Tables

Prior to this version, Exago always queries the Data Source for the schema of a Vertical Table, regardless of the setting of the **Schema Access Type** dropdown for the Data Object. After updating, if the **Schema Access Type** is *Metadata*, the schema will be read from the configuration file. This has the potential to break reports if they are referencing columns not included in the object’s metadata.

After updating, verify that all [Column Metadata](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Column2) exists for all columns of a vertical table.

### Updating from *v2019.2.30* or earlier

#### Scheduler Service Configuration File Change

The `<default_job_timeout>` setting in the [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration) is now deprecated. Use `<max_job_execution_minutes>` to limit schedule execution.

A new setting, `<smtp_timeout>` is now available to set the SMTP server connection timeout in place of `<default_job_timeout>`.

### Updating from *v2019.2.28* or earlier

#### `/rest/Schedules` Replaced

The `/rest/Schedules` endpoints are now deprecated.

Clients using the REST Web Service API to create, modify or delete scheduled reports should upgrade to the new `/rest/SchedulesV2` endpoints as soon as possible. The legacy `/rest/Schedules` endpoints will be removed in a future version of Exago.

### Updating from *v2019.2.17* or earlier

* Cloned data objects may now have their own **folder** and **description** fields. Accordingly, there are some minor changes to the Admin Console, XML configuration file, and .NET API handling of data object clones.

### Updating from *v2019.2.15* or earlier

* The **MongoDB CDATA** driver has been updated from version 19.0.7202.0 to version 20.0.7524.0. If you need more product information, including new purchases and upgrades, contact your Exago Customer Success Manager.
* A bug fix to the `/rest/Schedules/` endpoint now includes the full report path when making standard and BATCH calls on Linux. This change only affects Linux, as the full report path was always returned on Windows. For example:

```
"ReportName": "Parameter Report"
```

```
"ReportName": "My ReportsAdvanced ReportsParametersParameter Report"
```

### Updating from *v2019.2.11* or earlier

The **Admin Console** > **General** > **Culture Settings** > **Time Zone Name** will now be used for all time related features, including DateTime functions such as Now(). **Admin Console** > **General** > **Culture Settings** > **Server Time Zone Offset** only applies if **Time Zone Name** is not set.

### Updating from *v2019.2.0* or earlier

#### Linux Installer Flags Added

The **Linux Installer** has had several new command line flags added. Any previous headless install scripts will start prompting for missing formation and will require editing to account for the new parameters.

In summary, the new parameters added are:

* `-N` will inhibit the installer from configuring systemd services for the Web Application and the Scheduler Service. Otherwise, they will be installed and configured by default. Replaces the -R parameter.
* `-u` is used to specify an operating system user account under which the systemd services and FastCGI listeners (if applicable) will run.
* `-D` is used to tell the installer to use default values when installing.
* `-f` is used to specify names for the FastCGI listener services (NGINX only).
* `-p` is used to specify the port number for the FastCGI listener services (NGINX only).

Read the [Installing Exago on Linux](https://devnet.logianalytics.com/hc/en-us/articles/5281601243031-Installing-Exago-on-Linux) topic to review the changes made to the installer and the new options.

#### api.saveData() is deprecated

The .NET `api.saveData()` method has been deprecated and replaced by two new methods, `SaveConfigToApi()` and `SaveConfigToFile()`.

**SaveConfigToApi** takes the place of a `SaveData(false)` call and **SaveConfigToFile** takes the place of a `SaveData(true)` call.

### Updating from *v2019.1* or earlier

This section applies when upgrading from any minor version of *v2019.1* (for example *v2019.1.0*, *v2019.1.11*, etc…)

#### Settings Removed From Admin Console

The following settings have been removed from the Admin Console, but do remain available in the XML Config Files in case they are needed. Most of these settings effectively retire the legacy Express Report Designer. Advanced Reports should be used instead.

* **General** > **Feature/UI Settings** > **Allow Creation/Editing of Express Reports**
* **General** > **Feature/UI Settings** > **Use Sample Data for Dashboard Visualization Design**
* all of the **General** > **Feature/UI Settings** > **Express Report Designer Settings**
* **Roles** > **Allow Creation/Editing of Express Reports**
* **Roles** > **Show Styling Toolbar**
* **Roles** > **Show Themes**
* **Roles** > **Show Grouping**
* **Roles** > **Show Formula Button**

#### **Record Level Aggregation Enabled by Default** Changed to True

In *v2019.1.8* of the application, the **Record Level Aggregation Enabled by Default** setting was added to the system configuration. This setting configures how Exago handles one-to-many relationships when an Aggregate Function is called without the `recordLevel` argument. This flag has been changed to *True* by default in *v2019.2*.

Our documentation on [Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281614243735-Aggregate-Functions) describes how the `recordLevel` argument works and how this change may impact reports.

#### Dashboard Visualization Tile Update

Visualization tiles built directly on a Dashboard in previous versions are based on ExpressView. In *v2019.2*, they are based on Advanced Reports. The Dashboard Designer will update the visualizations when a legacy Dashboard is saved for the first time in the *v2019.2+* Dashboard Designer, but this is a one-way update.

To retain the ExpressView appearance and functionality, export the tiles as a standalone ExpressView and replace the tile with an Existing Report tile containing the newly created standalone ExpressView. It is very highly recommended that all legacy Dashboards be backed up before upgrading to the *v2019.2*.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323101299991 "Note")
>
> If **General** > **Feature/UI Settings** > **[Save on Report Execution](https://devnet.logianalytics.com/hc/en-us/articles/5281644433431-Feature-UI-Settings#Save)** in the configuration is *True*, clicking Run in the Dashboard Designer will also save the Dashboard and update the visualizations.

### Updating from *v2019.1.28* and earlier

The **MongoDB CDATA** driver has been updated.

### Updating from *v2019.1.25* and earlier

The **Admin Console** > **General** > **Culture Settings** > **Time Zone Name** will now be used for all time related features, including DateTime functions such as Now(). **Admin Console** > **General** > **Culture Settings** > **Server Time Zone Offset** only applies if **Time Zone Name** is not set.

### Updating from *v2019.1.14* and earlier

#### WebReports.Api.Reports.Report.GetExecute Methods Will Use Remote Execution by Default

The GetExecute() methods [GetExecuteHtml(), GetExecuteCsv(), GetExecuteData(), GetExecuteJson()] are now able to use Remote Execution. If a Remote Execution host is configured, calls to these methods will use the Remote Execution servers for report generation by default.

To run a report locally, disable Remote Execution for the session via the API.

### Updating from *v2019.1.4* and earlier

When updating from *v2019.1.4* and earlier, the following topics may require attention.

#### .NET Requirements

A minimum of .NET Framework version 4.6.1 is required, with version 4.7.2 recommended. .NET Standard 2.0 is required.

#### Mono

Exago supports the following versions of Mono:

* 4.2.2.30
* 5.10.1.20

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25323101304215 "Important")
>
> These are the only versions of Mono that are compatible with Exago. In addition, the Exago installer will install a patched version of `System.Web.dll`. This patch  [can also be installed manually](https://devnet.logianalytics.com/hc/article_attachments/25323117408663).

#### Using Puppeteer with .NET API Integration

*v2019.1.5* contains a new set of libraries for image rendering called **Puppeteer**. These are turned off by default, and can be enabled by setting the **useWkHtmlToImage** flag in [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings) to *false*.

If you are using a .NET API integration, in order to use Puppeteer, the following files must be copied to the host application’s bin directory:

```
js.es5.resourcejs.es6.resource  
bin/ExagoPuppeteerRasterizer.dll  
bin/Microsoft.AspNetCore.WebUtilities.dll  
bin/Microsoft.Extensions.DependencyInjection.Abstractions.dll  
bin/Microsoft.Extensions.Logging.Abstractions.dll  
bin/Microsoft.Extensions.Logging.dll  
bin/Microsoft.Extensions.Options.dll  
bin/Microsoft.Extensions.Primitives.dll  
bin/Microsoft.Net.Http.Headers.dll  
bin/PuppeteerSharp.dll
```

If the Exago web server is running Linux, the following X11 libraries are required to be installed in order to use Puppeteer:

```
gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget
```

In a CentOS environment, the following libraries are required to be installed in order to use Puppeteer:

```
pango.x86_64 libXcomposite.x86_64 libXcursor.x86_64 libXdamage.x86_64 libXext.x86_64 libXi.x86_64 libXtst.x86_64 cups-libs.x86_64 libXScrnSaver.x86_64 libXrandr.x86_64 GConf2.x86_64 alsa-lib.x86_64 atk.x86_64 gtk3.x86_64 ipa-gothic-fonts xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-utils xorg-x11-fonts-cyrillic xorg-x11-fonts-Type1 xorg-x11-fonts-misc
```

#### Manual Extraction of `chromium-win64.zip` Required with ZIP Scheduler Service Installation

When installing the **Exago Scheduler Service** using the Windows ZIP Archive the file `chromium-win64.zip` must be manually extracted. Extract it to a `chromium` folder inside of the Scheduler Service’s installation directory (for example `C:\Exago\ExagoScheduler\chromium`). This extraction process happens automatically with the Windows Installer but needs to be done manually when installing from ZIP.

### Updating from *v2019.1.3* and earlier

When updating from *v2019.1.3* and earlier, the following topics may require attention.

#### .NET Framework Version Requirement Raised to 4.6.1

*v2019.1.4* contains an upgraded version of the Syncfusion Excel exporter library that requires .NET Framework 4.6.1 or above.

In order to continue to export to Excel via the user interface or API Action, web servers running Exago must have .NET Framework 4.6.1 or above.

If you are using .NET API integration, in order to continue to export to Excel via GetExecute() API methods, web servers running the host application must have .NET Framework 4.6.1 or above. The host application does not need to target this version; it must simply be available on the server. Additionally, the `System.ValueTuple.dll` binary must be present in the host application’s bin directory.

### Updating from *v2019.1.1* and earlier

When updating from *v2019.1.1* and earlier, the following topics may require attention.

#### New method for managing the dbconfigs.json file

The **dbconfigs.json** file contains database specific syntax related to formulas, data types, primary and foreign key discovery, datetime casting, and row limiting and range selection. This file is overwritten after each new installation of Exago and, as such, any changes made to this file will be lost.

In order to prevent the loss of such information after each update, a *dbconfigs.overrides.json* file may be created and populated with these changes. For more information on the **dbconfigs.json** and **dbconfigs.overrides.json** files, please see the [Managing the dbconfigs.json File](https://devnet.logianalytics.com/hc/en-us/articles/5281593110167-Managing-the-dbconfigs-json-File) topic.

### Updating from *v2018.2* and earlier

When updating from *v2018.2* and earlier, the following topics may require attention.

#### Updated Linux Scheduler Installer

The Linux Scheduler installer has been updated in order to allow systemd compatibility and customization of service names. With these enhancements come a few changes in behavior for Scheduler installation including the replacement of `start`, `stop`, `restart` and `status` checks with a single new script named `exago-scheduler.sh` by default. The behavior of the Linux installer will not change for overwriting existing installs; however, any new installation of the Scheduler will function according to these changes. For more information please see the [Installing Exago on Linux](https://devnet.logianalytics.com/hc/en-us/articles/5281601243031-Installing-Exago-on-Linux) topic.

#### Unique IDs and aliases are now required for Data Objects

Data Objects are now required to have unique IDs and aliases (names). These IDs will have automatically been assigned if the Data Objects were created using the Automatic Database Discovery tool. However, Data Objects created manually or via the API (as Entities) will need to be manually assigned IDs and aliases.

When upgrading to *v2019.1*, it is imperative that each Data Object is assigned a unique ID and alias if they are not already set. Any new Data Objects created without the use of the Automatic Database Discovery tool must now be assigned unique IDs. If they are not assigned a distinct ID value, A warning message will appear preventing these Data Objects from being created.

Furthermore, any existing API code that dynamically creates new Data Objects should be examined to ensure that unique ID and alias values are being assigned.

#### Time zone enhancements and changes to scheduling

Enhancements have been made to how Exago considers daylight saving time and other non-linear scheduling issues related to geopolitical time zones. In order to implement these enhancements, the **Client Time Zone Name** setting has been added where the client’s geopolitical IANA time zone may be specified.

Furthermore, changes have been made to scheduling calculations with the inclusion of the Noda Time library within Exago, allowing the **Scheduler** tool and **Scheduler Queue** to accurately consider DST and other time zone related issues.

For detailed information on these enhancements please see the [Time Zone Calculation Enhancements in v2019.1](https://devnet.logianalytics.com/hc/en-us/articles/5281609830039-Time-Zone-Calculation-Enhancements-in-v2019-1) topic.

Upon updating, it is recommended that the **Next Execute Date** of existing Schedules is reviewed for accuracy. If **Client Time Zone Name** is being utilized, existing schedules may need to be manually edited or recreated in order to reflect these changes.

Furthermore, ccertain DateTime values may have been assigned different meanings in the Scheduler Job XML following the implementation of Noda Time. Depending on the modifications made to the implementation of the **Scheduler Queue**, changes may have to be made to its code:

* If you have not implemented the **Scheduler Queue**, then the *v2019.1* upgrading process will not be affected.
* If the implementation of the **Scheduler Queue** utilizes the QueueAPI object from WebReports.Api.Scheduler, then there should be no required for the **Scheduler Queue** to function properly after upgrading to *v2019.1*.
* If the implementation of the **Scheduler Queue** has been modified to directly parse the Job XML, then some DateTime values may have been assigned a different meaning and will need to be adjusted for. It is recommended that you contact our Services team for help in determining which values will need to be adjusted.

#### Changes to Entity creation via the .NET API

In the .NET WebReportsAPI class, the *NewEntity()* function now requires the string parameter *entityName*. This parameter represents the name (alias) of the data object, functionally replacing the Entity.Name argument, and must be unique. The Entity.Name argument, however, is still writable.

**Example**

```
Entity etlEnt = api.Entities.NewEntity("New Entity");
```

Furthermore, the *Add()* function of the *Entities* class requires the new Boolean parameter *addEntityData*, which is set to false by default. In order to add the Entity Data to the local collection, its value must be set to true.

**Example** `api.Entities.Add(etlEnt, true);`

Each instance of the *NewEntity()* and *Add()* functions in use in current .NET API code, must be modified to reflect these changes.

#### Recommended configuration architectural changes

With *v2019.1*, [Performance Enhancements in v2019.1](https://devnet.logianalytics.com/hc/en-us/articles/5281618124055-Performance-Enhancements-in-v2019-1) have been made to the configuration with the intention of optimizing the system. The system has been modified allowing a portion of the configuration to be extracted into a static configuration, which will be loaded into static memory and made available to all sessions. The contents of this parent configuration extend its specified attributes to the child (dynamic) configuration, which will contain the remainder of the configuration information and will be loaded at each user session.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25323101304215 "Important")
>
> If using a static configuration with one or more scheduler or remote execution services, all static configuration .xml files must be added to the **Config** sub-directory of all scheduler instances.

These optimizations will considerably decrease configuration processing time, as well as decrease overhead in storing and executing scheduled reports, and are strongly recommended. However, these changes are entirely optional and do not need to be implemented. The directive for each configuration file will be defaulted to Dynamic status, requiring no additional set up if these changes are not desired.

#### New warnings regarding Metadata in the Admin Console

The use of full metadata across all data objects is strongly recommended in *v2019.1* as it will reduce the frequency in which the databases are queried whenever metadata is required. As such, new warning icons will appear in the **Admin Console** next to data objects that do not have metadata properly implemented.

#### Changes to Active Role settings in the Admin Console

The setting in the configuration indicating the currently active role has changed. The **Active Role** setting under the **Main Settings** of the **Admin Console** retains the Id of the role to be made active upon session start. The active role may now be changed manually using the dropdown.

#### Changes to Null Tenant Parameters

Following changes made to nullable parameters in *v2019.1*, in order to disable tenancy on a tenant column, the parameter value for each tenant column now must be set to “{disabletenancy}.” Previously, to ignore tenancy, this parameter value could be left as an empty string; however, in *v2019.1*, any empty tenant parameters currently in use within the system will be identified as empty string tenant filters.

In order to continue disabling tenancy, the value must be set to “{disabletenancy}” across all instances of tenant parameter values set to empty strings. For more information, see [Multi-Tenant Environment Integration](https://devnet.logianalytics.com/hc/en-us/articles/5281611685783-Multi-Tenant-Environment-Integration).

#### Corrected spelling of REST Folder.Propagate property

In previous versions of Exago BI, the REST Folder.Propagate property was incorrectly spelled as “Propogate.” This spelling has been corrected and as such will affect any REST API code using the previous spelling of the Propagate property. Any instance of the incorrect spelling of the Propagate property should be corrected after updated.

#### Report Management Caching & Database Aggregation enabled by default

The report management interface caches (**GetReportList**, **GetReportXml**, and **GetTheme**/**ExistTheme**/**GetThemeList**) and **Aggregate and Group in Database** setting have been enabled by default in newer versions of Exago in order to ensure that clients are reaping the performance benefits associated with these options without having to explicitly activate them.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323101299991 "Note")
>
> The **userId** and **companyId** parameters are used in the generation of the unique key created for the report management interface caches of user sessions. In order to take full advantage of report management caching, it is recommended that these parameters are properly set up. For more information, see [User Identification](https://devnet.logianalytics.com/hc/en-us/articles/5281619919255-User-Identification)

### Updating from *v2018.2.5* and earlier

When updating from *v2018.2.5* and earlier, the following topics may require attention:

#### New Required Field Added for Custom Functions

The **Return Type** field has been added to custom function objects. This field has been added to support the conversion of filter formulas to SQL so that they may be evaluated in the database using the **Convert Filter Formulas to SQL** flag in the **Admin Console**.

This field is required for all custom functions, and, upon updating, all custom functions will need to be assigned a return value of either *String*, *Integer*, *Decimal*, or *Date*. Return values for all custom functions already existing before the upgrade will default to *String*.

#### LoadAssemblyInExternalDomain Moved to AppSettings

The <**loadassemblyinexternaldomain**> tag has been moved to the appsettings.config file and has been defaulted to true. This change will rarely affect Exago instances; however, it is important to take note of its new location.

#### SQLUtils.dll Moved to WebReportsApi.dll

The SQLUtils.dll file has been removed from the base Exago install and has been built into the WebReportsApi.dll file. In order to continue to use its methods, WebReports.Api.SqlUtils will need to be referenced.

### Updating from *v2018.2.1* and earlier

#### New Parameters for Conditional Drop Pin Formatting

The @metric\_label@ and @metric\_value@ parameters within the Conditional Drop Pin Formatting option of the Google Maps wizard are no longer valid. These parameters have been replaced with the serializing parameters *@metric\_value\_<index>@*, which automatically receive the values of each map metric in the order of their creation (for example @metric\_value\_1@, @metric\_value\_2@ and so on).

### Updating from *v2018.1* and earlier

When updating from *v2018.1* and earlier, the following topics may require attention:

#### New uses of User Preferences

The new **Tutorial Mode** feature relies upon User Preferences. Depending on the User Preference Storage Method, choose:

* *None*: No action needed but **Tutorial Mode** will be disabled.
* *Local Storage*: No action will be required.
* *External Interface or Server Events*: No action required if you are following the sample code provided by Exago. If you have made customizations to the *GetUserPreferences()* or *SetUserPreferences()* method, we recommend reviewing that code to make sure it properly handles the new values being passed.

#### New Configuration Settings

With *v2018.2* there are new configuration settings for Exago. Below we’ve listed those that are enabled by default and may warrant consideration or action as you upgrade:

*<Showtipsexpressview>* and *<Showtutorialexpressview>*:

These settings enable the new **Tutorial Mode** feature. They are True by default but will have no impact if User Preference Storage Method is set to *None*. Be sure to set values for the Parameter userId or disable these features.

#### Disable the old Monitoring Service

The installer will install the new Monitoring Service as a separate service instead of overwriting the existing one. If installing over an existing installation, the installer will detect and halt any older services running against the monitoring executable.

In order to prevent older services from restarting on system startup, you should remove or disable them. Otherwise there can be multiple services running against the same installation, which will cause duplicate entries to be written to the monitoring database.

This command line command can be used to delete specified monitoring services:

```
sc delete ExagoMonitoringService.full_version_number
```

```
sc delete ExagoMonitoringService.v2017.2.1.117
```

#### Back up settings files

Some settings files may be overwritten when updating. Make sure to back up the following files before running the installation:

* <WEBAPP>/Config/Other/dbconfigs.json
* <WEBAPP>/Config/Other/cdataconfig.json
* <WEBAPP>/Config/Other/tagwhitelist.json
* <SCHEDULER>/eWebReportsScheduler.exe.config
* <WEBSERVICE>/appSettings.config

Application settings files for the web application and monitoring service will not be overwritten.

### ‘Name’ Property of Filter Objects Deprecated

The `Name` property of Filter Objects has been deprecated. This property has been obsoleted by the property `FilterText`. This change may affect any references to Filter Objects made within the .NET API.

## Configuration File Changes

The following section details the changes made to the configuration XML files.

### *v2021.2.0*

Added to <webreports>:

* `<UseExternalTimeZoneConverter>`
* `<general>`
  + `<errorondbrowlimitexceeded>`

### *v2021.1.17*

Added to `<webreports>`

* `<general>`
  + `<maxexportfilesizebytes>`

### *v2021.1.16*

Added to `<webreports>`:

* `<general>`
  + `<errorondbrowlimitexceeded>`

### *v2021.1.8*

Added to `<webreports>`:

* `<general>`
  + `<chainedreportmaxcollationexecutions>`
  + `<sqliteprovider>`
  + `<sqliteprovidertableschema>`
  + `<sqliteproviderviewschema>`
  + `<sqliteproviderfunctionchema>`
  + `<sqliteproviderprocedurechema>`

### *v2021.1.2*

Added to the **Scheduler Service** Configuration file:

* `<smtp_timeout>`

Deprecated from the **Scheduler Service** Configuration file:

* `<default_job_timeout>`

### *v2021.1.0*

Added to <**webreports**>:

* `<entity>`
  + `<canreexecuteindb>` — set to *False* to prevent the Dashboard Designer from executing filters in the data source. See **Interactive Filtering in Database** in [Data Objects](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects) for more information.
* `<storagemgmt>`
  + `<default_access_flags>` — the definition of the `<default_access_flags>` has changed in this version. Review the Storage Management section of the [Config File XML Reference (All Nodes but General)](https://devnet.logianalytics.com/hc/en-us/articles/5281627946391-Config-File-XML-Reference-All-Nodes-but-General-) topic for more information.
* `<general>`
  + `<Dashboardautomaticallyrefreshtiles>` — set to *True* to allow tiles in the Dashboard Designer to refresh for all changes made to them. This also disables the Refresh Reminder feature. See [Feature/UI Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281644433431-Feature-UI-Settings) for more information.
  + `<showautosum>` — show (*true*) or hide (*false*) the **AutoSum**![Sum.png](https://devnet.logianalytics.com/hc/article_attachments/5432230783511) icon on the toolbar in the Advanced Report Designer.

Removed from **<webreports>:**

* `<etl>`
* `<general>`
  + `<etlreportfolder>`
  + `<showtipsexpressview>`
  + `<showtutorialexpressview>`

Removed from the **Scheduler Service** Configuration file:

* `<enable_etl_bulk_insert>`
* `<etl_bulk_insert_local_path>`
* `<etl_bulk_insert_database_path>`
* `<use_etl_bulk_insert_csv_format>`
* `<etl_bulk_insert_field_terminator>`
* `<etl_bulk_insert_debug>`

### *v2020.1.14*

Added to the **Scheduler Service** Configuration file:

* `<smtp_timeout>`

Deprecated from the **Scheduler Service** Configuration file:

* `<default_job_timeout>`

### *v2020.1.2*

Added to the **Scheduler Service** Configuration file:

* `<enable_etl_bulk_insert>`
* `<etl_bulk_insert_local_path>`
* `<etl_bulk_insert_database_path>`
* `<use_etl_bulk_insert_csv_format>`
* `<etl_bulk_insert_field_terminator>`
* `<etl_bulk_insert_debug>`

### *v2020.1.0*

Added to <**webreports**>:

* `<general><sqlgenerationlevel></general>` — Set the level of in-database formula grouping used by Exago. This value should be *1* unless otherwise directed by Exago Support. More information can be found in the [Hidden Flags](https://devnet.logianalytics.com/hc/en-us/articles/5281607060631-Hidden-Flags) topic.
* `<storagemgmt>` — defines a Storage Management configuration
  + `<assembly>`
  + `<class>`
  + `<table_prefix>`
  + `<report_list_cache_timeout>`
  + `<report_xml_cache_timeout>`
  + `<theme_list_cache_enabled>`
  + `<report_xml_cache_enabled>`
  + `<default_inherit_flag>`
  + `<default_party_type_id>`
  + `<default_access_flags>`
  + `<option>`
    - `<DbType>`
    - `<DbProvider>`
    - `<ConnectionString>`
    - `<ReportListCacheKey>`
  + `<identity>`
    - `userId`
    - `classId`
    - `companyId`
    - `ownerId`

### *v2019.2.31*

Added to the **Scheduler Service** Configuration file:

* `<smtp_timeout>`

Deprecated from the **Scheduler Service** Configuration file:

* `<default_job_timeout>`

### *v2019.2.18*

Added to <**webreports**>:

* `<entity>`
  + `<inherit_category>`
  + `<inherit_description>`

### *v2019.2.0*

A number of Express Reports settings were removed from the Admin Console and now exist only as [Hidden Flags](https://devnet.logianalytics.com/hc/en-us/articles/5281607060631-Hidden-Flags).

### *v2019.1.0*

Added to <**webreports**>

* <**config**> Specify directive information for different config types.
  + <**lifespan**> How long, in seconds, the configuration should be retained.
  + <**type**> Whether the configuration file is dynamic or static.
  + <**parent**> The name of the parent configuration.
* <**etl**> ETL Job object information
  + <**name**>
  + <**id**>
  + <**datasource\_id**>
  + <**schema**>
  + <**object\_name**>
  + <**report\_name**>
  + <**job\_id**>
  + <**schedule\_info**>
  + <**enabled**>

Added to <**general**>

* <**activeroleid**> Set or view the currently active Role.
* <**showsqlwindow**> If True, users will be able to preview the SQL that will be sent to the database when executing Advanced Reports.
* <**clienttimezonename**> Set the client’s default geopolitical time zone.
* <**useexternaltimezoneconverter**>
* <**mintilewidth**> Set the minimum tile width during automatic resizing.
* <**mindesktopwidth**> Set the minimum desktop width during automatic resizing.
* <**reportxmlcacheenabled**>
* <**reportxmlcachetimeout**>
* <**etlreportpath**> Report path where the ETL Reports Folder should be stored, defaulted to standard report path.
* <**etlreportfolder**> Folder within the specified report path where ETL reports will be stored.
* <**licensekey**> Licensing information to enable purchasable features.

Added to <**column\_metadata**>

* <**col\_dateformat**> Date field formatting (for example, dd-MM-yyyy). For use with vertical table transformations only.

### *v2018.2.6*

Added to <**general**>

* <**evaluateformulasindatabase**> If True, Exago will convert formula filters to SQL to be evaluated in the database.

Added to <**function**>

* <**filter\_return\_type**> Required field specifying the return type of a function. Can be set to *String*, *Integer*, *Decimal*, or *Date*.

Moved to <**appsettings.config**>

* <**loadassemblyinexternaldomain**>

Moved to <**webreportsapi.dll**>

* **SQLUtils.dll**

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323101299991 "Note")
>
> `SQLUtils.dll` has been removed from the base install. To continue using its methods, it must now be referenced from `WebReports.Api.SqlUtils`

### *v2018.2.0*

Added to <**general**>

* <**schedulershowreplyto**> Allows a user to specify a “Reply To” address when creating Scheduled Reports.
* <**showtipsexpressview**> Enable or Disable “Tips” in the ExpressView designer.
* <**showtutorialexpressview**> Enable or Disable the tutorial as a new user enters the ExpressView designer.
* <**reportlistcacheenabled**> If True, Exago will cache the report list returned by Folder Management’s method GetReportList() to reduce the number of calls being made.
* <**filterdropdownobjecttenancy**>
* <**evaluateformulasindatabase**> (*HIDDEN FLAG*) Currently hard coded to false pending future enhancement.
