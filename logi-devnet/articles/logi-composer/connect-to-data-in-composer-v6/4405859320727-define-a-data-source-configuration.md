---
title: "Define a Data Source Configuration"
id: 4405859320727
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859320727-Define-a-Data-Source-Configuration
updated_at: 2022-03-29T07:47:41Z
---

# Define a Data Source Configuration

# Define a Data Source Configuration

To define a new data source configuration:

1. Make sure you are logged in as a Composer administrator or a user with the **Can Administer Sources** or the **Can Create new Data Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or the [top-level navigation menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. On the [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page, select the ![](https://devnet.logianalytics.com/hc/article_attachments/4406743836951/add-source-btn_75x22.png) button. The Select a Source Type dialog appears, listing all the available [connection types](https://devnet.logianalytics.com/hc/en-us/articles/4405850909079-Manage-Data-Store-Connections).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747426839/select-source-type_288x304.png)
4. Select a [connection type](https://devnet.logianalytics.com/hc/en-us/articles/4405850909079-Manage-Data-Store-Connections).
5. After making your selection, the data source configuration wizard starts. It consists of a series of tabs, with the General tab displaying first. Provide a name for the new data source and an optional description on the General tab. See [*General Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859318039-General-Tab).

   If you select a Fusion, flat file or upload API data source, the tabs are different than they are for all other data source configurations. See [*Create a Fusion Data Source*](https://devnet.logianalytics.com/hc/en-us/articles/4405859361431-Create-a-Fusion-Data-Source), [*Upload a Flat File into Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer), and [*Use the Upload API*](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API).
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747427095/next-btn_38x22.png) to proceed to the Connection tab. Select an existing connection definition for the data source or provide credentials for a new connection definition on the Connection tab. See [*Connection Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405851023767-Connection-Tab), [*Select a Data Store Connection for a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405859169431-Select-a-Data-Store-Connection-for-a-Data-Source-Configuration) and [*Add Data Store Connections*](https://devnet.logianalytics.com/hc/en-us/articles/4405859165335-Add-Data-Store-Connections).

   This tab is only available if you are logged in as an administrator or as a user with both the [group privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) **Can Manage Connections** and **Can Create new Data Sources**.

   For flat file data connectors, the Connection tab is replaced with a Data tab and there is no Tables or Indices tab.
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747427095/next-btn_38x22.png) to proceed to the Tables or Indices tab. Select the data table you want to use for this data source configuration on the Tables or Indices tab. You can also use this tab to enable data caching. See [*Tables/Indices Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859323287-Tables-Indices-Tab) and [*How Composer Caches Data*](https://devnet.logianalytics.com/hc/en-us/articles/4405859286935-How-Composer-Caches-Data).
8. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747427095/next-btn_38x22.png) to proceed to the Fields tab. Configure the fields for the data source configuration on the Fields tab. You can alter the field labels, types, format, ranges, and enable or disable distinct counts. You can also define derived fields and custom metrics for the data source. See [*Fields Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab), [*Enable Distinct Counts*](https://devnet.logianalytics.com/hc/en-us/articles/4405859300503-Enable-Distinct-Counts), [*Maintain Derived Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields), and [*Maintain Custom Metrics*](https://devnet.logianalytics.com/hc/en-us/articles/4405859285399-Maintain-Custom-Metrics).
9. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747427095/next-btn_38x22.png) to proceed to the Refresh tab. Define refresh jobs for the data that Composer caches for the data source configuration. See [*Refresh Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859322007-Refresh-Tab), [*Set Up a Data Source Refresh Job*](https://devnet.logianalytics.com/hc/en-us/articles/4405851158167-Set-Up-a-Data-Source-Refresh-Job), and [*Trigger Refresh Jobs*](https://devnet.logianalytics.com/hc/en-us/articles/4405851159063-Trigger-Refresh-Jobs).
10. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743839767/save-next-btn_75x23.png) to save the data source configuration and proceed to the Visuals tab. Define default settings for visuals created using the data source configuration. You can also configure the time bar (including refresh rates) and search bar defaults for your data source. See [*Visuals Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab), [*Configure Time Bar Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4405859324311-Configure-Time-Bar-Defaults), and [*Configure Search Box Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4405851028503-Configure-Search-Box-Defaults).
11. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743840791/finish-btn_44x23.png) to save the data source configuration. Your new data source configuration is listed in the list on the Sources page.
