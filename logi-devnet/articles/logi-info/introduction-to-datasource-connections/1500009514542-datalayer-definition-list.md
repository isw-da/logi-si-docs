---
title: "DataLayer.Definition List"
id: 1500009514542
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514542-DataLayer-Definition-List
updated_at: 2021-06-17T01:58:09Z
---

# DataLayer.Definition List

# DataLayer.Definition List

The **DataLayer.Definition List** element programmatically provides developers with information about the definitions used in their application. This data can be used to create report menus and report management systems.

* Attributes
* [Work with DataLayer.Definition List](#WorkingWith)

## Attributes

The DataLayer.Definition List element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required through v10.1.46) Unique element ID. |
| Definition List Folder | Enter a file system folder name here to restrict the results returned to definitions within a single folder. The folder named is assumed to be within the \_Definitions folder of the application's project folder. Examples: *\_Processes, \_Reports, \_Templates, \_Widgets*  Default: Returns data for all definitions |

## Work with DataLayer.Definition List

The datalayer reads the definition data for the current project and caches it as rows and columns, with one row per definition file. Data retrieved into the datalayer is cached in **XML** format.

The data retrieved with a datalayer is available using @Data **tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is **case-sensitive**. The data is only available within the **scope** of the **parent** element of the datalayer, not throughout the entire report definition. The DataLayer.Linked element can be used to make the data reusable in another datalayer outside this scope.

Valid "column names" available through the @Data token are:

| Column | Description |
| --- | --- |
| DefinitionName | The definition name, as it appears in the Application panel, e.g. *Default* |
| DefinitionType | The definition type, e.g. *Report*, *Process*, *Template*, or *Widget* |
| Caption | The Caption attribute value (for Report definitions). |
| EngineVersion | The build number of the version of the Logi Server Engine used, e.g. *9.0.30* |
| Filename | The fully-qualified filename of the definition file, e.g.  *c:\inetpub\wwwroot\TestApp\\_Definitions\\_Reports\CrosstabSample.lgx* |
| Folder*n* | For easier organization, Logi definition files can be named using period-separated prefixes, such as Accounting.ProfitLoss.lgx. The prefixes are referred to as folders, though they don't exist in the file system as such. This column returns the *n*th prefix or folder name for each definition. Examples:  For Accounting.Profits.lgx, the Folder1 column returns "Accounting" For New.Accounting.Profits.lgx, the Folder2 column returns "Accounting"  *Due to the optional nature of these prefixes, the AutoColumns element may not detect all instances of this column in the datalayer.* |
| ID | The Report ID from the report definition's root node, ID attribute. |
| SavedAt | The timestamp indicating when the definition was last saved, e.g. *3/8/2008 2:25 PM* |
| SavedBy | User name of the person who last saved the definition. |

If the **Alternative Definition Folder** attribute is set in the \_Settings definition's **Path** element, the datalayer also includes definition objects from that folder.

The data retrieved into the datalayer can be viewed by turning on the **Debugging Link** in the \_Settings definition (General element) and using the resulting link at the bottom of the report page to view the **Application Trace** page. A link on the Trace page will display the retrieved data.

[![](https://logianalytics.zendesk.com/hc/article_attachments/4402778391063/totop.gif)](#)  [Back to the top](#)
