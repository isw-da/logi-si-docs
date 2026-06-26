---
title: "DataLayer.Plugin"
id: 4419700059031
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700059031-DataLayer-Plugin
updated_at: 2022-07-17T02:25:38Z
---

# DataLayer.Plugin

# DataLayer.Plugin

The **DataLayer.Plugin** element gives developers the ability to retrieve data from datasources not otherwise supported with standard connection and datalayer elements, using **custom-written** code. The code, known as a plug-in, is either a Windows .dll or a Java .javafile. The returned data is XML in a rowset format; @Data tokens can be used to retrieve the data for each column.

* Attributes
* [Working with DataLayer.Plugin](#sec1)

## Attributes

The DataLayer.Plugin element has the following attributes:

| Attribute | Description |
| --- | --- |
| Assembly Name | (Required) The complete filename of the plug-in assembly, ending in ".dll" (.NET) or .jar (Java). No path information is required if the assembly file has been placed in a folder named \_Plugins under the application folder. Otherwise, a fully-qualified path and filename for the assembly file may be provided. If the dll is not in the \_Plugins folder, you have the ability to call plugins within the application directory by setting the path using @Function.AppPhysicalPath~/ . Other tokens, such as @Request, @Sessions, and @Constant can also be used to call plugins within the application directory by setting the path. |
| Class Type Name | (Required for .NET; ignored in Java) Specifies the plug-in class that contains the method to be called. The value consists of the dll's root namespace, ".", and the class name. For example: LogiXML.SamplePlugin.Plugin |
| ID | An optional element ID. Recommended for easier identification when debugging. |
| Method | (Required) The name of the plug-in Method to be called. |
| Pass Data As | Specifies how data is returnedfrom the plug-in to the datalayer. When it's set to *XmlDocument* (the default value), the data will be passed to the datalayer as an XML document object in memory and added to the "ReturnedData" property of rdServerObjects. To reduce the amount of memory used when manipulating large datasets (100,000+ rows), this attribute can be set to *FileName*, and the datalayer will be passed the name of a cache file used by the plug-in, rather than the data itself. The plug-in can then use an XML stream writer to cache the data and the datalayer will use a stream reader to retrieve it. The filename includes the fully-qualified path and is placed in the rdServerObjects object's "ReturnedDataFile" properties. |

## Working with DataLayer.Plugin

Instead of working with a datasource connection or with a file system file, as other datalayers do, DataLayer.Plugin retrieves its data using a custom-written plug-in. This allows access to datasources that are not already supported in Logi applications via the standard suite of connections and datalayers. Plug-ins written for this purpose should return an XML document object, or the name of a file containing the results as serialized string data.

Examples of this type of datasource include things like multi-pass web services (where your datalayer may need to make multiple trips back to the web service before your results can be generated) or a custom .NET or Java data object that interacts with another app or process.

Do not confuse this element with the **DataLayer Plugin Call** element. That element is designed to apply the operations of a plug-in on data *already retrieved* into a datalayer; this element actually uses a plug-in to *retrieve* the data.

The following example illustrates how to use the **DataLayer.Plugin** element:

![](https://devnet.logianalytics.com/hc/article_attachments/7522882862871/dlplugin_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522858073111/dlplugin_01a.png)

Add a **DataLayer.Plugin** element to the definition, as shown above, and configure its attributes per the attribute table in the previous section. Remember that the **Class Type Name** attribute is *required* for .NET
plug-ins, but is *ignored* for Java plug-ins.

Because the actual behavior of the plug-in is determined by developers outside of Logi Analytics, the **Add data columns** wizard found in Studio may not work if the plug-in does not return schema information.
For information about writing a plug-in, see [Logi Plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins).
