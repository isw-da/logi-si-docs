---
title: "Template Modifier Files"
id: 4419715482903
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715482903-Template-Modifier-Files
updated_at: 2022-07-17T02:23:27Z
---

# Template Modifier Files

# Template Modifier Files

Template Modifier Files (TMFs) allow Logi Info developers to modify the "super-elements", such as the Analysis Grid, which behave like mini-applications, have a UI, and let users control visualizations at runtime. In addition, Logi Info developers can use TMFs to create themes.

The following topics discuss the use of these files:

* [Setting Hidden Underlying Element Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419723165591-Setting-Hidden-Underlying-Element-Attributes#Setting)
* [Using XPath Notation](https://devnet.logianalytics.com/hc/en-us/articles/4419707842583-Using-XPath-Notation#XPath)
* [Modifying Selected Chart Captions](https://devnet.logianalytics.com/hc/en-us/articles/4419723164695-Modifying-Selected-Chart-Captions#Captions)
* [Manipulating Existing Underlying Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419707840791-Manipulating-Existing-Underlying-Elements#Manipulating)
* [Inserting and Removing Underlying Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419715480599-Inserting-and-Removing-Underlying-Elements#Inserting)
* [List of Special XML Tags](https://devnet.logianalytics.com/hc/en-us/articles/4419715481879-List-of-Special-XML-Tags#Tags)

For more information about Themes, see [Themes](https://devnet.logianalytics.com/hc/en-us/articles/4419723357847-Themes).

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) Looking for information about Excel, Word, or PDF templates?Template Modifier Files are *not* related to them; see [Form-based Reporting](https://devnet.logianalytics.com/hc/en-us/articles/4419722927127-Form-based-Reporting) for information about those date-related templates.

## About Template Modifier Files

Super-elements are a complex combination of standard elements, JavaScript, and style classes. The following super-elements can be customized using a Template Modifier File (TMF):

* Analysis Chart
* Analysis Filter
* Analysis Grid
* Chart Grid
* Dashboard
* Dimension Grid
* OLAP Grid
* Schedule
* Report Author

Super-elements are rendered at runtime using a special definition file and standard Logi Info elements. A TMF is a separate definition file that's processed *after* a super-element's definition file, providing an opportunity to alter the super-element at runtime, without editing the fundamental super-element blueprint. UI customizations can be placed in a TMF to alter the appearance and behavior of the super-element.

Examples of common customizations using TMFs include language- and culture-specific text changes for internationalization, and the hiding of some of controls, such as **Export** buttons.

A TMF is an XML file that contains special tags for customizing the super-element. It can be stored in any folder accessible to the web application and it's specified in a super-element's **Template Modifier File** attribute. If a fully-qualified file path is not provided in the attribute value, then the application expects it to be in your application's \_SupportFiles folder.

Tokens can be used in the Template Modifier File attribute to provide the TMF filename. This allows you to specify different TMFs (or no TMF) for different situations and/or different users.

Template modifier files are also a primary component of Logi **Themes** technology. The power of the TMF is quite obvious in this scenario, as it effectively "scripts" the output of the designated report to adopt the desired appearance.

When debugging links are turned on and TMFs are used, special entries will appear in the Debugger Trace report (see ):

![](https://devnet.logianalytics.com/hc/article_attachments/7522775931031/usingtmf_08.png)

As shown above, these entries will be in the AnalysisGrid section. Click them to view the TMF log and the source code of the modified definition.

### <Column> Element vs. <Column> Tag

Although the proper terminology for an XML object is "element", the term "tag" will be used in the following discussion in order to avoid confusion between super-elements, underlying elements, and XML elements.
