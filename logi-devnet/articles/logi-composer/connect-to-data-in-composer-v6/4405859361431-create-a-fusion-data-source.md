---
title: "Create a Fusion Data Source"
id: 4405859361431
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859361431-Create-a-Fusion-Data-Source
updated_at: 2021-09-21T01:28:41Z
---

# Create a Fusion Data Source

# Create a Fusion Data Source

To fuse data in Composer, you must first connect to the data sources that you want to be joined. After successful connection, use the data source configuration wizard to join the disparate data sets as a new type of Fusion data source
. After the data sets have been joined together, you can explore and analyze the fused data set in visuals and dashboards.

For an overview of Composer’s data fusion capability, see [*Fuse Data Sources*](https://devnet.logianalytics.com/hc/en-us/articles/4405851072279-Fuse-Data-Sources).

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) If your user account does not have read permissions for a data source that comprises a fused data source, only the **General** tab will be available to you when you edit the fused data source using the data source configuration wizard.

The key step in the process is to identify and specify the fields to be joined across the data sources used in the Fusion data source.
This is performed on the Data Sources and Editor tabs, as described in this section.

## Before You Start

Before you attempt to create a Fusion data source:

* Ensure the data sources you want to fuse are already connected and configured in Composer. If not, create them See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations).
* Verify that there are matching fields across the data sources you want to fuse.
* Identify the fields from each data source that will be used in the join definitions of the Fusion data source.

## Configure a Fusion Data Source

To create a Fusion data source, you will use the [data source configuration wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405859320727-Define-a-Data-Source-Configuration). However, a few of the tabs in the wizard are different for Fusion data sources than they are for other data sources.

To create a Fusion data source:

1. Make sure you are logged in as a Composer administrator or a user who is a member of a group with the **Can Administer Sources** privilege.
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)). The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. On the [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743790999/add-source-btn_83x25.png). The data source configuration wizard will start.
4. On the Select a Source Type dialog, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743791383/fusion_26x25.png)**Fusion**.
5. Name your Fusion data source and add an optional description, as described for the [*General Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859318039-General-Tab). Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743791639/next-btn_42x25.png) when you are done.
6. The Data Sources tab is unique to Fusion data sources. It contains a list of all the available data sources on the left of the tab. Select the data sources you want to join in your Fusion data source. As they are selected, they are listed on the right side of the tab. Use the search bar to locate a data source if necessary.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747414935/data-source-tab_576x254.png)

   Select the checkbox for each data source you want to join. Your selections will be added to the fusion list to the right. You can provide an alias for each data source, delete a source that is not needed, and download the configuration details for the data source (if available and you need to export to another Composer instance).
7. Optionally, provide an alias for each selected data source using the field in the **Source Alias** column boxes. The only special character that can be used is the underscore (\_).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The only special character that can be specified in a source alias is the underscore (\_). This field can only be edited during the initial setup of the data source. The text is locked after you save the source. To edit this field, you need to either delete or uncheck the source and re-select it again.

   You can also delete a data source from the Fusion data source and download a data source by selecting the ![](https://devnet.logianalytics.com/hc/article_attachments/4406743792023/delete-black-x.png) and ![](https://devnet.logianalytics.com/hc/article_attachments/4406743792279/download.png) icons in the **Delete** and **Download** columns.

   When you are finished with the Data Sources tab, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743791639/next-btn_42x25.png).
8. The Editor tab is unique to Fusion data sources. Use the Editor tab to specify the join definitions for fusion. See [*Data Fusion Join Rules*](https://devnet.logianalytics.com/hc/en-us/articles/4405851073175-Data-Fusion-Join-Rules) for rules about defining these join definitions.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743792535/editor-tab_576x253.png)

   The **Available Fields** section of the tab lists all the fields you can use in join definitions. The **Define Joins** section of the tab lists the join definitions and join conditions (forms).

   To define a join definition:

   1. Drag-and-drop fields from the Available Fields section into the Define Joins work area. Use the guide areas (outlined with dashed lines) in the work area to position the field in the correct location. Be sure to follow the [*Data Fusion Join Rules*](https://devnet.logianalytics.com/hc/en-us/articles/4405851073175-Data-Fusion-Join-Rules) or errors will result when you save the Fusion data source.
   2. After you have selected the fields for a join definition, use the Join drop-down menu to select the [type of join](https://www.w3schools.com/sql/sql_join.asp) that should be performed: **Inner** ([inner join](https://www.w3schools.com/sql/sql_join_inner.asp)), **Left** ([left outer join](https://www.w3schools.com/sql/sql_join_left.asp)), or **Full Outer** ([full outer join](https://www.w3schools.com/sql/sql_join_full.asp)). [Right outer joins](https://www.w3schools.com/sql/sql_join_right.asp) are not supported.
   3. In addition, you can specify whether a field is unique. For unique fields, the join condition values must be unique per record. To specify that a field is unique, select its **Unique** checkbox.

      In a fused data source, Composer uses information about column uniqueness when building its query plan. This can be critical for a connector's resource usage and query time.

   To delete a join field, a join condition (form), or a join definition from the Define Joins work area, select the ![](https://devnet.logianalytics.com/hc/article_attachments/4406743776663/delete-grey.png) icon and then select **Delete**.
9. Optionally, use the **Caching** switch to indicate whether Composer should cache the aggregated results of queries from this source. See [*How Composer Caches Data*](https://devnet.logianalytics.com/hc/en-us/articles/4405859286935-How-Composer-Caches-Data).

   When you have finished with your updates on the Editor tab, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743791639/next-btn_42x25.png) to proceed to the Fields tab or ![](https://devnet.logianalytics.com/hc/article_attachments/4406743792791/finish-btn_47x24.png) to save the Fusion data source. When you select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743791639/next-btn_42x25.png) or ![](https://devnet.logianalytics.com/hc/article_attachments/4406743792791/finish-btn_47x24.png), any errors in the Fusion data source definition will be identified and displayed.
10. On the Fields tab, update the fields included in our Fusion data source, as described for the [*Fields Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab). (Note that you cannot create [derived fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) for Fusion data sources.) Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743761431/save-next-btn_82x25.png) when you are done.
11. Use the Visuals tab to specify global default settings for visuals that use the Fusion data source as well as default settings for each visuals type that uses the data source. See [Visuals Tab](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab). Note that not all visual styles are available for Fusion data sources. See [*Data Fusion Limitations*](https://devnet.logianalytics.com/hc/en-us/articles/4405859357463-Data-Fusion-Limitations).
12. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743793175/finish-btn_40x23.png) to save the Fusion data source configuration.
