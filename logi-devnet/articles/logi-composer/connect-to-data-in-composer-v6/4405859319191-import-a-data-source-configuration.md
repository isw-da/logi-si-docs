---
title: "Import a Data Source Configuration"
id: 4405859319191
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859319191-Import-a-Data-Source-Configuration
updated_at: 2021-09-21T01:28:16Z
---

# Import a Data Source Configuration

# Import a Data Source Configuration

Composer lets you import a data source configuration from another Composer instance. The import file must be a JSON file you previously downloaded. See [*Export a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405851025559-Export-a-Data-Source-Configuration). Data source configurations can only be imported if the imported JSON file is from the same version of Composer.

The configuration settings that are imported include:

* The data source configuration name specified on the [*General Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859318039-General-Tab)
* The data source connection settings specified on the [*Connection Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405851023767-Connection-Tab)
* The data tables selected for the configuration on the [*Tables/Indices Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859323287-Tables-Indices-Tab)
* Custom labels, derived fields, and custom metrics specified on the [*Fields Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab)
* The refresh settings set on the [*Refresh Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859322007-Refresh-Tab)
* Default visual settings set on the [*Visuals Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab)

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) The ability to import data source configuration definitions was deprecated in Composer 6.9 and will be removed in a future release.

#### Privilege Considerations

If you are logged into Composer as a user who can maintain data source configurations but cannot maintain connection definitions (your [group privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) include **Can Create new Data Sources**, but **not****Can Manage Connections**), the following data source import behavior occurs:

* If the data store connection used by the data source has already been defined to the Composer instance, the data source is successfully imported.
* If the data store connection used by the data source has not previously been defined to the Composer instance, the data source is **not** imported and an error message displays because your user account does not have authorization to create data store connections.

If you are logged in as a Composer administrator or as a user who can maintain both data source configurations and connection definitions (your [group privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) include **Can Create new Data Sources** and **Can Manage Connections**), data source imports should work every time.

**To import the data source configuration file:**

1. Make sure you are logged in as a Composer administrator or as a user with the **Can Administer Sources** or **Can Create new Data Sources**[group privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or the [top-level navigation menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. On the Sources page, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743842455/import-source-btn_90x22.png). A pop-up Windows explorer window appears.
4. Browse for and select the JSON file for the data source configuration. Select **Open** on the Windows explorer dialog.

   The data source configuration is imported. If a data source configuration already exists with the same name, the imported data source has a number appended to its name.

## Import Processing

Import processing is depicted in the following diagram:

![](https://devnet.logianalytics.com/hc/article_attachments/4406743843479/import_576x322.png)

To be successfully imported to Composer, the data source configuration is validated against the following requirements. If one of them does not match, the import procedure will fail.

1. The version of Composer specified in the exported file must be the same as the version to which you are importing it.
2. Composer checks if there are any similar connections available (the connection name may be different). If the same connection is found in Composer, the connection is validated and a new data source is created using the available parameters.
3. If the same connection cannot be found, Composer validates if there are any related connection types available based on the following criteria:

   * Minimum and maximum supported versions of the data sources
   * Data store type
   * Required parameters
4. If the connection types do not match the criteria listed above, the import process will stop. Otherwise, Composer creates the connection based on the first matching type.
5. Composer validates the connection with the parameters defined in the imported data source.
6. In case of successful validation, the connection is saved and the new data source is created.
