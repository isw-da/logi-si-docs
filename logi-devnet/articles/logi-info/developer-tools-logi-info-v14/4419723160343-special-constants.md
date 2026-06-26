---
title: "Special Constants"
id: 4419723160343
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723160343-Special-Constants
updated_at: 2022-07-17T02:06:17Z
---

# Special Constants

# Special Constants

Logi Info makes use of a set of special constants and "reserved"
words that developers should be aware of. The constants can often be used
to enable or disable specific behavior or functionality.

The following special **constants**, which can be defined in the
\_Settings definition, have specific meaning for the Logi Engine. The
version numbers indicate when they were introduced but they may have been
phased out in later product versions. Some constants may be automatically
created by the New Application wizard. Remember that constants are
*case-sensitive.*

| Constant | Description |
| --- | --- |
| FirstDayOfQ1 | Sets the month to be used for Fiscal Quarter calculations by the Globalization and Time Period Column elements, using the format *MM/YY*. |
| rdAnimatedChartRenderStyle | Specifies the rendering style, *JavaScript* or *Flash*, for Animated Charts and Gauges. If this constant is not present, the default is *Flash*. |
| rdCalculationsIncludeNulls | By default, aggregating functions don't include null values in their calculations. This constant can be created and set to *True* to cause null values to be included. This is global in scope. |
| rdComboLoader | By default, "combo loading" is used to pre-load interface script files. Set this constant to *False* to disable the pre-loading. |
| rdDefaultCsvEncoding | Exports to CSV default to the "utf-8" format, which opens in Excel. Developers who wish to change the encoding to "ASCII" can create and set this constant to *ISO-8859-1*. |
| rdFilterRetainJoinType | Used to control filtering behavior of tables that have Left joins. When set to *True,* retains the Filter Type for exclusive filters on Left-joined tables. If missing or not *True*, the default behavior will be to always filter the full dataset. |
| rdFlexSort | Sorting performance improvements were introduced in this version, using a scheme named **FlexSort**, and became the default sorting mechanism. Developers who wish to continue to use the older sorting scheme can do so by creating and setting this constant to *False*. |
| rdInfinityErrorResult | Specifies a global result for formulae that may produce a divide-by-zero situation (result: infinity), sparing developers the task of specifying a result on a per-element basis in their Error Result attributes. |
| rdJavaPdfClearCache | (Java apps only) - Create and set this constant to *True* to force clearing of the PDF cache for each export. |
| rdJavaPdfStitchSize | (Java apps only) - Controls the size of blocks of HTML exported to the PDF rendering engine, in megabytes, which are then "stitched" together. The default value is 5MB. When exporting very large amounts of data (thousands of pages) this constant can be used to increase the block size, decreasing the chance that memory will be exhausted by the process. This also increases the rendering time, however. |
| rdJavascriptInfinityIsError | When set to *True*, specifies that formulae that produce a divide-by-zero situation (result: infinity) will trigger an error, which is handled by elements' Error Result attribute or, if set, the rdInfinityErrorResult constant. If rdJavascriptInfinityIsError is not specified, the Scripting Engine will return the value *NaN* (for "Not a Number") by default when a division by zero occurs. |
| rdMemoryStreamLimit | Used with the hybrid data engine. Sets the threshold, in MB, for shifting from memory caching to file system caching. A value of *0* will force all caching to the file system; a value of *2048*, the maximum, will force all caching to memory. The default value is *10*. |
| rdMinifiedJavaScript | When set to *False*, disables the "minification" of Logi Engine JavaScript code. This can be useful when debugging script-related errors. The default value is *True*. |
| rdMultiThreadXslDataLayers | When set to *False*, disables multi-threaded processing of datalayers (which was introduced in v12). The default value is *True*. |
| rdPdfRenderingType | In order to enable Printer Page Breaks, in reports that use them, when the report is exported to PDF, this constant should be created, with the value *MSHTML*. |
| rdScriptingSingleQuotedString | By default, single- and double-quotes are supported as quoted string delimiters in scripting. However, single-quote support can be turned off by creating and setting this constant to *False*. |
| rdSQLIncludeGMTOffset | Used to speed up the internal processing of DateTime-type data into ISO 8601 (yyyy-mm-dd) format, by skipping Time Zone information. Does not produce significant performance improvements with a small number of DateTime columns; intended for result sets with large number of DateTime columns. |
| rdTempFileCleanupInterval | Used to manage cached temporary files. Set this constant to specify the time, in minutes, between clean ups. If this value is *-1*, clean up will not run at all; if the value is *0*, clean up will run with *every* page request. Default value: *5 minutes* |
| rdTempFileLifespan | Used to manage cached temporary files. Set this constant to specify the minimum file age, in minutes, before a file qualifies to be deleted when the clean up runs. Default value: *60 minutes*.  Your web server's **Session Timeout** setting should *not* be configured to be *less* than the value assigned to rdTempFileCleanupInterval or its default value of 5 minutes. |
