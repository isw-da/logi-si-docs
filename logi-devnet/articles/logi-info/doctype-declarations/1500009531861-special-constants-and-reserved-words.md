---
title: "Special Constants and Reserved Words"
id: 1500009531861
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531861-Special-Constants-and-Reserved-Words
updated_at: 2021-06-17T01:58:38Z
---

# Special Constants and Reserved Words

# Special Constants and Reserved Words

Logi Analytics products using the Logi Engine make use of a set of special constants and "reserved" words that developers should be aware of. The constants can often be used to enable or disable specific behavior or functionality. Developers should avoid using the reserved words in their definitions as identifiers as they may cause errors when the engine encounters them.

* Special Constants
* [Reserved Words](#Reserved)

## Special Constants

The following special **constants**, which can be defined in the \_Settings definition, have specific meaning for the Logi Engine. The version numbers indicate when they were introduced but they may have been phased out in later product versions. Some constants may be automatically created by the New Application wizard. Remember that constants are *case-sensitive.*

| Constant | Description |
| --- | --- |
| FirstDayOfQ1 | (v10.0.479+) - Sets the month to be used for Fiscal Quarter calculations by the Globalization and Time Period Column elements, using the format *MM/YY*. |
| rdAnimatedChartRenderStyle | (v11.0.416+) - Specifies the rendering style, *JavaScript* or *Flash*, for Animated Charts and Gauges. If this constant is not present, the default is *Flash*. |
| rdCalculationsIncludeNulls | By default, aggregating functions don't include null values in their calculations. This constant can be created and set to *True* to cause null values to be included. This is global in scope. |
| rdComboLoader | By default, "combo loading" is used to pre-load interface script files. Set this constant to *False* to disable the pre-loading. |
| rdDataEngine | (v10.1.25+) - Set this constant to *Version10.0* to "downshift" the Data Engine back to version 10.0 |
| rdDefaultCsvEncoding | (v10.0.479+) - Exports to CSV default to the "utf-8" format, which opens in Excel. Developers who wish to change the encoding to "ASCII" can create and set this constant to *ISO-8859-1*. |
| rdFavorChartCanvas | (v11.2.040+) Chart Canvas charts are used by default for Super Elements, such as the Analysis Grid, in all *new applications* started in v11.2.040 and later. Older Logi applications that are *upgraded* to v11.2.040+ will use the classic static charts for their Super Elements. To force upgraded apps to use Chart Canvas charts, create this constant and set it to *True* to your \_Settings definition.  (v11.3+) This constant defaults to *True* for all applications. |
| rdFlexSort | (v10.0.319+) - Sorting performance improvements were introduced in this version, using a scheme named **FlexSort**, and became the default sorting mechanism. Developers who wish to continue to use the older sorting scheme can do so by creating and setting this constant to *False*. |
| rdInfinityErrorResult | (v11.2.040 SP6+) - Specifies a global result for formulae that may produce a divide-by-zero situation (result: infinity), sparing developers the task of specifying a result on a per-element basis in their Error Result attributes. |
| rdJavaPdfClearCache | (v10.1.46+ Java apps) - Create and set this constant to *True* to force clearing of the PDF cache for each export. |
| rdJavaPdfStitchSize | (v10.1.46+ Java apps) - Controls the size of blocks of HTML exported to the PDF rendering engine, in megabytes, which are then "stitched" together. The default value is 5MB. When exporting very large amounts of data (thousands of pages) this constant can be used to increase the block size, decreasing the chance that memory will be exhausted by the process. This also increases the rendering time, however. |
| rdJavascriptInfinityIsError | (v11.2.040 SP6+) - When set to *True*, specifies that formulae that produce a divide-by-zero situation (result: infinity) will trigger an error, which is handled by elements' Error Result attribute or, if set, the rdInfinityErrorResult constant. If rdJavascriptInfinityIsError is not specified, the Scripting Engine will return the value *NaN* (for "Not a Number") by default when a division by zero occurs. |
| rdMemoryStreamLimit | (v9.0.15+) - Used with the hybrid data engine. Sets the threshold, in MB, for shifting from memory caching to file system caching. A value of *0* will force all caching to the file system; a value of *2048*, the maximum, will force all caching to memory. The default value is *10*. |
| rdPdfRenderingStyle | In order to enable Printer Page Breaks, in reports that use them, when the report is exported to PDF, this constant should be created, with the value *MSHTML*. |
| rdScriptingEngine | (v10+) - Used to engage a specific version of the scripting engine; set to *Version10*, to engage v10 scripting, or leave *blank* for the older v9 system. For v10 products, this constant is automatically created and set to *Version10* by Studio's New Application wizard. |
| rdScriptingSingleQuotedString | By default, single- and double-quotes are supported as quoted string delimiters in scripting. However, single-quote support can be turned off by creating and setting this constant to *False*. |
| rdSQLIncludeGMTOffset | (v10.2.224+) - Used to speed up the internal processing of DateTime-type data into ISO 8601 (yyyy-mm-dd) format, by skipping Time Zone information. Does not produce significant performance improvements with a small number of DateTime columns; intended for result sets with large number of DateTime columns. |
| rdTempFileCleanupInterval | (v9.5+) - Used to manage cached temporary files. Set this constant to specify the time, in minutes, between clean ups. If this value is *-1*, clean up will not run at all; if the value is *0*, clean up will run with *every* page request. Default value: *5 minutes* |
| rdTempFileLifespan | (v9.5+) - Used to manage cached temporary files. Set this constant to specify the minimum file age, in minutes, before a file qualifies to be deleted when the clean up runs. Default value: *60 minutes* |

## Reserved Words

The Logi Server Engine deals with elements and data as XML and this can produce some parsing challenges. Developers should be careful not to assign names to elements, session variables, request variables, or link parameters that match the following words:

* rd\*  (any word that begins with "rd")
* Action

A general rule of thumb is to avoid using any attribute name as an ID or as a name for elements, session variables, request variables, or link parameters. Common attribute names include:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Axis Border Caption  Class Color Columns Command Condition Cube Database Display Domain Event Expression Filename Folder | Font Format Formula Function Height HTML ID Image Increment Iteration Javascript Keyword Language Latitude Layout Length | Location Longitude Method Modal Namespace Note Ordered Orientation Password Period Port Radius Refresh Rows Scrolling Server | Size Source Style Text Theme Thickness Title Tooltip Top Type URL User Value Width Worksheet XPath |

When in doubt, use the [Element Reference](https://devnet.logianalytics.com/rdPage.aspx?rdReport=ElementRef&dnView=Attribute&dnFilter=A-Z) page to check attribute names.
