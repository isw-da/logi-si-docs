---
title: "Advanced Settings"
id: 4415504834839
section: "Administrator Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504834839-Advanced-Settings
updated_at: 2021-12-10T03:10:20Z
---

# Advanced Settings

# Advanced Settings

The **Advanced Settings** page allows user to

* manage the list of data source categories
* update system settings in related groups

## Steps to config Advanced Settings

1. In browser, log in to Izenda as a user with Advanced Settings
   permission.
2. Click Settings, then Data Setup then Advanced Settings in the left
   menu.
3. Select the Setting Level: either System or a specific tenant.
4. Click on a tab to view values.
5. Hover on information icon following the value name to see the brief guide of that value

   [![../_images/Advanced_Settings_Performance_Hover_Brief_Guide.png](https://devnet.logianalytics.com/hc/article_attachments/4415492457111/advanced_settings_performance_hover_brief_guide.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492457111/advanced_settings_performance_hover_brief_guide.png)
6. Update the values.
7. Click Save button at the top to save the whole settings.

## Update Performance Settings

In Advanced Settings page, click on Performance tab in Middle Panel to view the items. The Performance items are list as below:

[![../_images/Advanced_Settings_Performance.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415492457367/advanced_settings_performance.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492457367/advanced_settings_performance.png)

| Section | Purpose | Default Value |
| --- | --- | --- |
| Query Timeout | To limit the duration of all queries in any page. | 3600 |
| Use No Lock | To not use NOLOCK (dirty read) statement when querying data. | True |
| Data Source Limit | To limit the number of data sources in a single report. | 1000 |
| Field Limit | To limit the number of fields in a report part. | 1000 |
| Query Limit | To limit the number of values returned from the query in Report Designer, Report Viewer, Dashboard and Export. | 100000 |
| Pivot Column Limit | Limit the number of columns in a pivot report part. | 100000 |
| Filter Limit | Limit the number of items displayed in Filter Value dropdown | 1000 |

Note: The Use No Lock setting instructs the database engine to return the current version of data immediately, instead of waiting for all pending transactions to complete. Check the possible consequences [here](https://www.izenda.com/blog/high-performance-sql-views-using-withnolock/) before using this option.

## Update Security Settings

In Advanced Settings page, click on Security tab in Middle Panel to view the items. The Security items are listed as below:

> [![../_images/Advanced_Settings_Sercurity.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415511725847/advanced_settings_sercurity.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511725847/advanced_settings_sercurity.png)

### Update common settings

> * Tick on Show Tenant Field checkbox will show the field(s) which is(are) sepcififed in Tenant Field in report/dashboard. Otherwise, those fields will be hidden.
> * For security in multi-tenant systems, set up **Tenant Field** then all reports and dashboards will automatically restrict data retrieval to only that of the current tenant. To enable this feature:
>
>   > - Input the name of tenant id field into the Tenant Field box   
>   > - The Tenant Field must be enclosed in brackets: [fieldname]   
>   > - Press **Enter** to add tenant field   
>   > - You can use multiple tenant fields
> * Tick on Render HTML in Printing/Exporting checkbox will allow HTML tags to be rendered when exporting and printing.
> * Tick on Render HTML in Report Viewer checkbox will allow HTML tags to be rendered when viewing reports in browser.

### Add Row-Level security rules

> 1. In browser, log in to Izenda as a System Admin and go to Settings, then Data Setup, Advanced Settings in the left
>    menu, and Security in the middle panel.
> 2. Click Add button in Row-Level Security section
>
>    [![../_images/data_security_001.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415511726359/data_security_001.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511726359/data_security_001.png)
> 3. Choose one or more available data sources and click Next to go to Step 2
>
>    [![../_images/data_security_002.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415504359703/data_security_002.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504359703/data_security_002.png)
> 4. Choose one or more available fields and click Next to go to Step 3
>
>    [![../_images/data_security_003.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415511726615/data_security_003.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511726615/data_security_003.png)
> 5. Type Name and Descitption (optional) for the data security rule set.
> 6. Click Add Rule and configure new data security rule.
> 7. Select one of the existing User Groups (Everyone, User or Role)
>
>    [![../_images/data_security_004.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415492457879/data_security_004.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492457879/data_security_004.png)
> 8. Select some specific users or roles if you selected the corresponding values in the previous step.
> 9. Type any value and press Enter to Values or select one of the preset values like
>    - [All] - all values
>    - [Tenant ID] - the current Tenant ID
>    - [Tenant Name] - the current Tenant Name
>    - [Role Name] - any role name of the current user
>    - [User ID] - the current User ID
> 10. Select access mode: Block or Allow
>
>     [![../_images/data_security_005.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415492458135/data_security_005.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492458135/data_security_005.png)
> 11. Add more rules if necessary.
> 12. Click Save and then OK on the pop-up info message about the impact of the current changes
>
>     [![../_images/data_security_006.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415504360215/data_security_006.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504360215/data_security_006.png)
> 13. Add more data security rule sets if necessary or edit/clone/delete some of the existing rule sets.
> 14. Click Save at the top-right corner to save security settings
>
>     [![../_images/data_security_007.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415511727127/data_security_007.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511727127/data_security_007.png)
>
> After that, if you create a new report with fields to which blocking rules are applied or open an existing one, and print or export it, then you will see masked data instead of the actual values
>
> > [![../_images/data_security_008.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415492458391/data_security_008.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492458391/data_security_008.png)

## Update Categories Settings

### Add data source categories

> A category should be added before showing up for assignment to a data
> source.
>
> 1. In browser, log in to Izenda as a user with Advanced Settings
>    permission.
> 2. Click Settings, then Data Setup then Advanced Settings in the left
>    menu.
> 3. Select the Setting Level: either System or a specific tenant.
> 4. Click Category in the Middle Panel.
>
>    ![../_images/Menu_Advanced_Settings_Category.jpg](https://devnet.logianalytics.com/hc/article_attachments/4415492458647/menu_advanced_settings_category_391x383.jpg)
> 5. Click Add New + button and type the name into the new text box.
>
>    [![../_images/Settings_Category_Add_New.jpg](https://devnet.logianalytics.com/hc/article_attachments/4415511727767/settings_category_add_new_622x74.jpg)](https://devnet.logianalytics.com/hc/article_attachments/4415511727383/settings_category_add_new.jpg)
> 6. Continue to click Add New + button to enter more categories.
> 7. Click Save button at the top to save the whole list.
>
> Note: User will not be able to save the list unless there is no duplication.

### Delete data source categories

> 1. In the category list, click the delete icon (x) on the right of each category to delete it.
>
>    [![../_images/Settings_Category_Delete.jpg](https://devnet.logianalytics.com/hc/article_attachments/4415492459031/settings_category_delete_621x76.jpg)](https://devnet.logianalytics.com/hc/article_attachments/4415504360855/settings_category_delete.jpg)
> 2. Click OK in the pop-up confirmation.
>
>    [![../_images/Category_Deletion_Confirmation.jpg](https://devnet.logianalytics.com/hc/article_attachments/4415511728279/category_deletion_confirmation_456x134.jpg)](https://devnet.logianalytics.com/hc/article_attachments/4415511728023/category_deletion_confirmation.jpg)
> 3. The category is deleted immediately. The Save and Cancel buttons at the top does not have any effect in this action.
>
> Note: The category will be deleted even if it has been assigned to data sources. After that these data sources will have no category.
>
> Note: To change the name of a category, the [Rename data source categories](#rename-data-source-categories) feature should be used instead.

### Rename data source categories

> Renaming a category will only change the name and keep the assignments
> to data sources intact.
>
> 1. In the category list, click the text box of any category and change the name.
>
>    [![../_images/Settings_Category_Rename.jpg](https://devnet.logianalytics.com/hc/article_attachments/4415504361495/settings_category_rename_617x43.jpg)](https://devnet.logianalytics.com/hc/article_attachments/4415504361239/settings_category_rename.jpg)
> 2. Continue to change more category names
> 3. Click Save button at the top to save the whole list.

## Update Others Settings

In Advanced Settings page, click on Others tab in Middle Panel to view the items. The Others items are listed as below:

[![../_images/Advanced_Settings_Others.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415504361751/advanced_settings_others_1649x1058.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511728535/advanced_settings_others.png)

| Section | Purpose | Default Value |
| --- | --- | --- |
| Sort Colum Name | When unselected fields in field tab of report designer, join dropdown and input paramters in filters sort alphabecitally. When selected, these fields sort based on position in the databse. | 0 |
| Trim Time In Joins | Tick on this checkbox to trim the time portion form the Date Time field in each join statement in Report Designer - Relationship page. Otherwise, system will use Date Time field in each sort statement | True |
| Timezone for Data Offset | To set default value for the Timezone Data Offset in Settings > User Setup page. And this setting will effect to displayed data value of Datetime/Time fields in the report part. **As of v2.9.5 offset will accept partial hours as .25, .5 or .75**  For example:   In database the data value is 11:00. If user sets “5” in the textbox of this section then the data value will be shown as 16:00 in the report part. | 0 |
| Timezone for Timestamp Offset | To set default value for the Timezone Data Offset in Settings > User Setup page. And this setting will effect to all Datetime/Time field in system. **As of v2.9.5 offset will accept partial hours as .25, .5 or .75**  For example:   The created date of report is 11:00. If user sets “5” in the textbox of this section then the created date will be shown as 16:00 in the system. | 0 |
| Convert Null to Empty String | Tick on this checkbox to convert all null values to blank (empty) in reports or dashboards. Otherwise, null values keep the orginal values. | False |
| Show Schema Name | Tick on this checkbox to show schema name together with the the data source name in any place. Otherwise, the schema name will be hidden | False |
| Show Introduction Text | To show the Introduction Text in the following section:   - Report Designer > Data Source tab > Content Panel > under Report Name   - Report List > Content Panel > under each report name | False |
| Send to Disk Path | To define the path to save files for all Scheduled/Subcribed instances with **Send to Disk** delivery method, input path in the textbox of that section.  Note   * When the report is saved into this location, system will save report name together data time so that saving the new version of this report will not overwrite this report. The format when saved: <report name>\_<mmddyyyy>\_<hhmmss> * **For example:**    If report “ABC” is saved to disk path at 10/22/2016, 23:59:00 then the report will be saved with name = ABC\_10222016\_235900 | Null |
| Determine common filter for the same field based on | To determine how the filters considered whether different or the same in the dashboard so they will be common filter and shown in dashboard filter section or not. There are three available options:   - Same field of the same data object from the same database schema   - Same field name regardless of database schema or connection string   - Same alias name regardless of database schema or connection string  Note  Stored Procedure stored procedures input parameters are only considered common when they are from the same stored procedure.  Please see [Dashboard Filters](https://devnet.logianalytics.com/hc/en-us/articles/4415492926487-Dashboard-Designer#dashboard-filters) for more details about common filter in dashboard. | Same field of the same data object from the same database schema |
| Allow Multiple Sorts on Grid Header | By selecting this checkbox, user can sort on multiple columns when clicking on Grid header in Vertical/Horizontal report. Otherwise, user can only sort by one column at a time. | True |
| Show Preview section in Configuration Mode | By selecting this checkbox, both Configuration and Preview sections display in the report part’s backside and setting popups. Otherwise, system only shows Configuration section. This is useful when working with very large datasets as the database is not called until the report part is flipped to the front side. | True |
| Hide report header and footer by default | By selecting this checkbox, report header and footer sections are hidden in both Report Viewer and Report Designer - Design. Otherwise, these sections are displayed by default (if any). | False |

## Cancel the changes

To cancel any changes without saving:

1. Click the Cancel button at the top.
2. Click OK in the confirmation pop-up.

![../_images/Cancel_Confirmation.jpg](https://devnet.logianalytics.com/hc/article_attachments/4415504362007/cancel_confirmation_465x138.jpg)

## See also

* [Data Model - Assign a category to a table, view or stored procedure](https://devnet.logianalytics.com/hc/en-us/articles/4415492931607-Data-Model-Tables-Views-and-Stored-Procedures#assign-a-category-to-a-table-view-or-stored-procedure)
