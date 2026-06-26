---
title: "Using a Plug-in to Modify a Report Definition"
id: 4406822452247
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822452247-Using-a-Plug-in-to-Modify-a-Report-Definition
updated_at: 2022-04-06T06:07:53Z
---

# Using a Plug-in to Modify a Report Definition

# Using a Plug-in to Modify a Report Definition

Plug-in methods are called using one of the elements described in [Plug-in Elements and Triggering Events](https://devnet.logianalytics.com/hc/en-us/articles/4406822451351-Plug-in-Elements-and-Triggering-Events). The element is included in the report, process, or job definition, and its attributes are set to identify the object and method to call. Let's see some examples of these elements in action.
**Plugin Call** elements can be added to any definition and give developers the ability to customize the report definition before or after it's processed, or to modify data retrieved into the report's datalayers. The simple example below shows how this element can be used to call a plug-in that modifies the Application element's Caption attribute in the \_Settings definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583795223/introplugins_01.png)

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The Plugin Call element is a child of the definition's Root element. It has the following unique attributes:

| Attribute | Description |
| --- | --- |
| Assembly Name | (Required) Specifies the name of the plug-in file. For .NET, provide the filename with its .dll file extension. No path information is necessary if the file is located in the \_Plugins sub-folder, otherwise provide a fully-qualified path and name.  If the dll is not in the \_Plugins folder, you have the ability to call plugins within the application directory by setting the path using @Function.AppPhysicalPath~/ . Other tokens, such as @Request, @Sessions, and @Constant can also be used to call plugins within the application directory by setting the path. For Java, provide the class name, including package, as necessary:    The example above shows the source package for a Java plug-in which has been created as LogiPlugin.jar and copied into *yourLogiApp*/WEB-INF/lib. The Assembly Name attribute value would then be com.logi.xmlmodifiers.ModifyCaptions. |
| Class Type Name | (Required for .NET) Consists of the root namespace + "." + the name of your plug-in class. |
| Event | (Required) Specifies the event that triggers the calling of this plug-in. Options include: *LoadDefinition* - when the report definition has been loaded, before any Logi engine processing *FinishHtml* - when the HTML response is ready to be sent back to the browser or to a report export processor. *FinishData* - when datalayer processing finishes. |
| Method | (Required) Specifies the case-sensitive name of the method to be called in your plug-in. |
| Java Plugin Version | (Java only) Specifies which version of the underlying plug-in class to use. Select *Version10* here to use the LogiPluginObjects10 class, which has additional methods such as addDebugMessage, replaceTokens and getSettingsDefinition. |

When developing a .NET plug-in in Visual Studio, the root namespace defaults to the project name, but you can set it explicitly in the Projects ![](https://devnet.logianalytics.com/hc/article_attachments/4417575446295/menuarrow.gif) Properties page in VS.

## Location Dependencies

The class object's *CurrentDefinition* value is that of the report definition containing the Plugin Call element used to call the plug-in. For example, if a Plugin Call element is placed in the Customers report definition, the *CurrentDefinition* field contains the string representation of the Customers report definition. The class's *Request* and *Session* values have application-wide scope and are not affected by the location of the Plugin Call element.
