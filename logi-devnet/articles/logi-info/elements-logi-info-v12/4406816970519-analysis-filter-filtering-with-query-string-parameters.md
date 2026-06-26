---
title: "Analysis Filter - Filtering with Query String Parameters"
id: 4406816970519
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816970519-Analysis-Filter-Filtering-with-Query-String-Parameters
updated_at: 2022-04-06T06:03:07Z
---

# Analysis Filter - Filtering with Query String Parameters

# Analysis Filter - Filtering with Query String Parameters

Special reserved query string parameters can be used to manipulate the Analysis Filter.

## Remove all Filter Definitions

*All* filter definitions can be removed by calling the report with the **rdAfReset** parameter set to *True*.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575917207/workaf_09.png)

In the example above, a Label has been added to a report as a link that clears all filters. The Target.Report element is set to *Current Report* and the Link Parameters element is used to pass the rdAfReset parameter.

## Force a Page Refresh with Current Filter Values

You can force a complete page refresh by calling the report with the **rdAfRefresh** parameter set to *True*.

## Define a New Filter

You can define and apply a new filter by sending a full set of query string parameters. The parameters are:

rdAfCommand="FilterSet"  
rdAfFilterColumn\_*<AnalysisFilterID>*="*<ColumnName>*"  
rdAfFilterOperator\_*<AnalysisFilterID>*="*<Operator>*"  
rdAfFilterValue\_*<AnalysisFilterID>*="*<FilterValue>*"  
rdAfMode\_*<AnalysisFilterID>*="*<ViewMode>*"  
rdAnalysisFilterID="*<AnalysisFilterID>*"

where:

* *<AnalysisFilterID>* is the ID of an existing Analysis Filter element in the report being called
* *<ColumnName*> is the name of a column that has an Analysis Filter Column element configured for it
* *<Operator>* is one of the operators available in Design view
* *<FilterValue>* is the data value on which to filter the column
* *<ViewMode>* specifies the filter display mode to be used, *Simple* or *Design*

If one or more filters already exist for the specified column then when these parameters are applied, the *value* of the first existing filter will change. An additional filter will *not* be created.

Here's an example for comparison purposes, using the XML source for these parameters defined in a Link Parameters element. They're based on the filter examples used in [Analysis Filter - Using the Analysis Filter Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406816973591-Analysis-Filter-Using-the-Analysis-Filter-Elements):

<LinkParams  
 rdAfCommand="FilterSet"  
 rdAfFilterColumnID\_<AnalysisFilterID>="CustomerID"  
 rdAfFilterOperator\_myAnalysisFilter="="  
 rdAfFilterValue\_myAnalysisFilter="VINET"  
 rdAfMode\_myAnalysisFilter="Simple"  
 rdAnalysisFilterID="myAnalysisFilter"  
/>

To make the code dynamic, tokens can be used to provide values for the parameters:

rdAfFilterValue\_myAnalysisFilter="@Request.FilterOnThis~"
