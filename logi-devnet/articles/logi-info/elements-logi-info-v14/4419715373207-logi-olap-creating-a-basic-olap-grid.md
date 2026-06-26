---
title: "Logi OLAP - Creating a Basic OLAP Grid"
id: 4419715373207
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715373207-Logi-OLAP-Creating-a-Basic-OLAP-Grid
updated_at: 2022-07-17T01:44:26Z
---

# Logi OLAP - Creating a Basic OLAP Grid

# Logi OLAP - Creating a Basic OLAP Grid

Now that you have a connection to Analysis Services configured, you can add the elements that comprise your OLAP Grid:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706928535/getstartolap_03.png)  

In your report definition, add an **OLAP Grid** element beneath the Body element, as shown above.

The OLAP Grid attributes are:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies an element ID, unique with the definition. |
| Batch Selection | Specifies whether UI changes made by the user will be applied immediately (*False*) or only when the user clicks an "OK" button (*True*). Deferring until the button is clicked may speed up the user experience by reducing the number of retrieval requests sent to the server. |
| Caption | Specifies a title that will appear above the grid. |
| Class | Specifies Cascading Style Sheet classes to be used by the element. Classes will also be used by all child elements that don't have their own classes set. A class set here may be overridden by a built-in theme. |
| Drilldown All | Specifies if each dimension in the table will show an extra "Drilldown All" button (*True*). Clicking this button causes a drilldown on all items below the dimension that have the "+" drilldown icon. The default value is *False*. |
| Hide Excel Export | Specifies if the Export: Excel button will be hidden from view. The default value is *False*. |
| Level Indent | Specifies the amount of indentation, in pixels, used when displaying levels of a hierarchy in a table. The default is *2 pixels*. |
| OLAP Cell Colors | Specifies whether or not to use foreground and background colors, defined in SSAS, for Calculated Members. The default value is *False*. |
| Pick Member Properties | Specifies whether the user will be able to pick Member Properties to be displayed in columns next to the Dimension column. Member Properties are selected by clicking an icon shown next to the Dimension name in the table. Selected Member Property columns only appear when there is at least one member that has the property and Member Properties can only be selected for Dimensions added to the *left* side of the table. The default value is *False*. |
| Saved OLAP Grid Folder | OLAP Grid configuration options selected by the user at runtime can be saved for reuse in a file, using the Procedure.Save Olap Grid element. Saved options can be reloaded by passing the "saved" filename in the rdOgLoadSaved request parameter. This attribute specifies the fully-qualified file system path to the folder, beneath the application root folder, that contains the saved files. Function tokens may be used to facilitate this, for example: @Function.AppPhysicalPath~\SavedOlapGrids |
| Security Right ID | When specified, access to this element can be controlled with Logi Security. Specify the ID of a Right defined in the application's \_Settings Security element. Only users with matching rights will be able to see the element. |
| Show Dimension Attributes | Specifies whether the table will show Dimension Attributes in addition to Dimensions and Dimension Hierarchies. Set to *True* to also show Dimension Attributes. The default value is *False*. |
| Template Modifier File | Specifies the name, with file extension, of a [Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4419715482903-Template-Modifier-Files) to be applied to the OLAP Grid at runtime. This is an XML file that can be used to change the underlying template used to create the OLAP Grid. Template Modifier files can be in any folder accessible to the application; if a folder isn't specified, the \_SupportFiles folder is assumed. |
| Width | Specifies the width of the displayed OLAP Grid. |
| Width Scale | Specifies the width units of the Width attribute value: either *px* for pixels or *%* for percent. |

A minimal configuration, like the one shown in the example above is all that's needed to display a usable grid. Once the OLAP Grid element is configured, you're ready to add its child elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699804823/getstartolap_04.png)  

Beneath the OLAP Grid element, add a **DataLayer.MDX** element and set its attributes as shown above. The **Connection ID** attribute value should be the ID of the Connection.OLAP element you configured at the start of this process.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The Attribute Panel identifies the element as a DataLayer.OlapMdx element.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706928791/getstartolap_05.png)  

Beneath the datalayer, add an **MDX Query** element and set its attributes as shown above.
Your OLAP Grid is now functional. Click the Preview tab at the bottom of the Workspace to view it.
