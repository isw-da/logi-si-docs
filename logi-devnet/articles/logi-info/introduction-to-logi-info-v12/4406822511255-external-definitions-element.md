---
title: "External Definitions Element"
id: 4406822511255
section: "Introduction to Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822511255-External-Definitions-Element
updated_at: 2022-04-06T06:08:35Z
---

# External Definitions Element

# External Definitions Element

Application report definition files are normally stored in the yourLogiApp\ \_Definitions\ \_Reports folder. However, developers can instead specify definitions that come from an external data source, such as a database or a web service, using the **External Definitions** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563094167/settingsdef_05.png)

As shown above, the External Definitions element works with its own datalayer, which retrieves the definition data when the application
runs. At runtime, the presence of an External Definitions element alerts the **Logi Server Engine**
to automatically include the datalayer's data in the Engine's inventory
of report definitions. When the report is called, the Engine will read
the definition from the datalayer rather than from the web server's file
system and render it.

The stored definition data should be in two columns:

**ReportID** ( varchar/nvarchar(50) ) - which contains the report definition name (without .lgx), and  
**Definition** ( varchar/nvarchar(max) ) - which contains the complete XML source of the report definition.

When building the data, the XML could be copied, for example, right from Studio's Workspace, Source tab, and inserted into the datasource. All values are case-sensitive.

To use an external definition, reference its ReportID value (the literal text - "BalanceSheet" - not as an @Data token) in the **Report Definition File** attribute of elements such as **Target.Report**.

Why would you want to store your definitions in a database? It's a
bit more complicated to update definitions in this arrangement and it
isn't necessarily for everyone. However, it does allow centralized
storage of report definitions, integrates with Content Management
Systems, provides portability in virtualized-server environments, and
works well in web server farms, so it definitely has its uses.
