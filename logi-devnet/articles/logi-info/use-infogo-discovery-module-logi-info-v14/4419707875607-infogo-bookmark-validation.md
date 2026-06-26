---
title: "InfoGo - Bookmark Validation"
id: 4419707875607
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707875607-InfoGo-Bookmark-Validation
updated_at: 2022-07-17T02:23:23Z
---

# InfoGo - Bookmark Validation

# InfoGo - Bookmark Validation

SSRM bookmarks are stored on the server. The bookmark stores what kind of visualization (Crosstab Table, chart, etc) and references a column(s) from the metadata. The metadata defines where the column is coming from, such as what data tab is used for grouping and security for columns. To run a bookmark successfully, you need the bookmark definition and metadata to match. One potential problem can occur when a user edits a column on the metadata side, but since there is no direct link to the bookmark, the bookmark doesn't recognize that there is a change in the metadata, which results in an error. By using the bookmark validation tool, every change made in the metadata is checked in the server to verify that it matches and pulls out what doesn't match in the results file. The results file identifies which bookmarks have an error and what kind of error. For example, a data type change or a missing data column and where the column is being used.

This independent tool is available for both Java and .NET and designed to run in command line/console. This application uses two required arguments and two optional arguments, described below:

| Argument Name | Output Value |
| --- | --- |
| -s:<folder> | Use to set your application folder path |
| -f:<file | Use to set the output report file path and file name |
| -m:[all|basic] | Use to set the Check All or only USED columns. This is optional and the default is 'all'. |
| -ol:[all|error] | Use to set the output level. This is optional and the default is 'all'. If set to 'error', only the error messages are included in the results file; anything that has passed will not be included. |

![](https://devnet.logianalytics.com/hc/article_attachments/7522767134615/bookmark_demo.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522783749015/bookmark_java_demo_1395x133.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522775452311/smofl_1397x167.png)

If you are an existing user, you can access a download link to the zip folder for the .NET version [here](https://downloads.logianalytics.com/info/bookmarks/BookmarkValidator.zip) and the Java version [here](https://downloads.logianalytics.com/info/bookmarks/BookmarkValidatorJava.zip). If you are a new user, you automatically receive the bookmark validation tool in your BIN folder when you install Info v14.0. You can run this directly from the folder, but you must specify application path, where the bookmark is stored, and what kind of error you are looking for.

Below is an example of the Readme file exe for .Net users:

2. this tool is designed to run in command line/console, ‘-s:<folder>’ is used to set ‘appPhysicalPath’, ‘-m:all’ or ‘-m:basic’ is to set ‘model’(default is 'all'), ‘-f:<file>” is to set ‘outputfile’ , '-ol:[all|error]' is used to set the output includes 'PASSED'(if -ol:all) or not(default is 'all')

Example : BookmarkValidator.exe -s:"C:/opt/tomcat/YourApp" -m:all -f:/myfolder/result.txt

Notice 1: Please sure "\_settings.lgx' is exist in "<appPhysicalPath>\\_Definitions\" and can be read.

Notice 2: 'basic' only validate the column be used as/in :

(AG) Filter

Dashboard Panel Filter

Dashboard Global Filter

Data Table Column

Data Table's Sort

Data Table's Group

Data Table's Aggregate(and Custom Aggregate)

Crosstab's Header Values column

Crosstab's Label Values column

Crosstab's Aggreate Values column

Crosstab's Extra Label column

Chart's Label column, Data Column, Addtional Column(s) (and X-Axis Column, Y-Axis Column)

Heatmap's Label column, Size column, Color Column

Gauge's Value column

(Dashboard) Chart's Drill Column

Formula and if this formula is used as/in above.

LinkURL and if it owner is used as/in above

Notice 3: It is recommended to quote the parameter value with quotation marks, like this : -s:"C:/opt/tomcat/YourApp"

Notice 4: short path is supported, like this : -s:"../YourApp"

Below is an example of the Readme file jar for Java users:

1. Please sure following jars have been added to/in classpath

> Must:

J2EE.Helpers.jar J2SE.Helpers.jar.jar Microsoft.VisualBasic.jar mscorlib.jar

System.Configuration.jar System.jar System.Xml.jar rdNewtonsoft.Json.Net20Java.jar

System.Data.jar

> Optional :

LogiDataEngine.jar , LogiSTUB.jar, and Jars for DB driver(such as cdata.jdbc.mysql.jar)

Notice0: These jars can be found in YourApp/WEB-INF/lib

Notice1: the jars listed optional are ONLY required If using FileToDatabaseMapping.

Notice2: If you wish to use Oracle then the LogiSTUB.jar needs to be replaced by ojdbc8.jar. Logi does not provide this. This have to be downloaded from Oracle(https://www.oracle.com/database/technologies/jdbc-ucp-122-downloads.html). The reference to LogiSTUB.jar in the BookmarkValidator.sh needs to be updated as well.

Notice3: If the jar is missing, an error message will be output in the console

Notice4: BookmarkValidator.bat is just an example for all jars in 'lib'.

2. this tool is designed to run in command line/console, ‘-s:<folder>’ is used to set ‘appPhysicalPath’, ‘-m:all’ or ‘-m:basic’ is to set ‘model’(default is 'all'), ‘-f:<file>” is to set ‘outputfile’ , '-ol:[all|error]' is used to set the output includes 'PASSED'(if -ol:all) or not(default is 'all')

Example : ./BookmarkValidator.sh -s:/opt/tomcat/YourApp -m:all -f:/myfolder/result.txt

Notice 1: Please sure "\_settings.lgx' is exist in "<appPhicalPath>\\_Definitions\" and can be read.

Notice 2: 'basic' only validate the column be used as/in :

(AG) Filter

Dashboard Panel Filter

Dashboard Global Filter

Data Table Column

Data Table's Sort

Data Table's Group

Data Table's Aggregate(and Custom Aggregate)

Crosstab's Header Values column

Crosstab's Label Values column

Crosstab's Aggreate Values column

Crosstab's Extra Label column

Chart's Label column, Data Column, Addtional Column(s) (and X-Axis Column, Y-Axis Column)

Heatmap's Label column, Size column, Color Column

Gauge's Value column

(Dashboard) Chart's Drill Column

Formula and if this formula is used as/in above.

LinkURL and if it owner is used as/in above

Notice 3: It is recommended to quote the parameter value with quotation marks, like this : -s:"/opt/tomcat/YourApp"

## Output Formatting

Once you run the bookmark validation tool, a results file generates that describes any errors that may need manual intervention.

Below is an example of a results file showing the Bookmark Name, Bookmark Type, Column, Visualization Type, and Error:

![](https://devnet.logianalytics.com/hc/article_attachments/7522775469591/image__1___1_.png)
