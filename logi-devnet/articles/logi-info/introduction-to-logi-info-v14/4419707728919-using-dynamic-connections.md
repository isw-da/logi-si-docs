---
title: "Using Dynamic Connections"
id: 4419707728919
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707728919-Using-Dynamic-Connections
updated_at: 2022-07-17T01:42:31Z
---

# Using Dynamic Connections

# Using Dynamic Connections

Developers often want to make their datasource connection strings dynamic, based on some external criteria at launch, and this has to occur before report definitions are processed. This topic describes how to use dynamic connections.

## Duplicate \_Settings Definitions

If the motivation for this it to duplicate the application in several different environments (development, QA, production) but minimize changes that need to be made when moving reports through them, then the easiest approach is simply to deploy copies of all Logi application files to the different servers. Connection element **IDs** remain the same across all the \_Settings definitions, but their connection string attribute values are different, as appropriate for each server. This means that
report definitions that use the connections will run on any of the servers without having to be modified. Any of the other values in \_Settings, such as the Application Path, can be similarly configured.

## Using Session Variables

If you're using some other application that eventually calls a Logi application, you can use **session variables** to set the connection strings (or other values found in the \_Settings definition) in the Logi application. Set these variables in the main application, and in your Logi application's \_Settings definition, use @Session tokens for the values of your connection string, path, and other settings. When the Logi application is called, it will resolve these tokens into values and run the reports
based on them.

## Using Plug-ins

"Plug-ins", which are DLL's, give Logi developers the ability to
**programmatically****extend** the functionality of their Logi
applications. With them, developers can dynamically change the behavior of Logi reports at
runtime by accessing *request* and *session* variables and modifying report definitions. To support dynamic connection strings, a Plugin Call element is used in the \_Settings definition to retrieve the connection string (or other values) from a session variable and then it dynamically modifies the \_Settings definition by inserting the connection string value. The plug-in runs on the LoadDefinition event and so alters the definition before it's processed. Learn more about plug-ins in our document
[Logi Plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins).
