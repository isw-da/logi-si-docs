---
title: "DataLayer.Data Services - Special Data Services Child Elements"
id: 4406822248855
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822248855-DataLayer-Data-Services-Special-Data-Services-Child-Elements
updated_at: 2022-04-06T06:05:10Z
---

# DataLayer.Data Services - Special Data Services Child Elements

# DataLayer.Data Services - Special Data Services Child Elements

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The data-related elements discussed here are available in Logi Info v12.5 but have been deprecated in later Info versions; consult the [Release Notes](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF) for specific details.

DataLayer.Data Services has some unique child elements that can be used to shape the data. Unlike similar child elements for regular datalayers, which modify the *data* in the datalayer, these elements modify the *Dataview* just before its execution.

| Element | Description |
| --- | --- |
| [The DsAggregate Column](https://devnet.logianalytics.com/hc/en-us/articles/4406817387927-The-DsAggregate-Column) | Adds a new column to the Dataview containing an aggregate value of all rows of the datalayer. The value is populated in every row so that it can be used in further calculations, such as Summary Rows, Link Params, etc. Available aggregate functions include *Average*, *Count*, *Distinct, Max, Min*, and *Sum.* The column's data type must be numeric for the Average, Count, Distinct, and Sum functions. |
| [The DsCalculated Column](https://devnet.logianalytics.com/hc/en-us/articles/4406817390999-The-DsCalculated-Column) | Adds a new column to the Dataview, created from other values in the same row or from token values, containing the results of an expression. Its **DsExpression** attribute value contains a Data Services-style expression which returns the result. In these expressions, the value of a data column is indicated by enclosing the column name in square brackets, not with an @Data token. Example expression: [Quantity] \* [UnitPrice] - .05 See [Dsexpression Reference](https://devnet.logianalytics.com/hc/en-us/articles/4406822306071-Dsexpression-Reference) for guidelines regarding expressions. |
| [The DsCondition Filter](https://devnet.logianalytics.com/hc/en-us/articles/4406817393047-The-DsCondition-Filter) | Adds a row filtering operation to the Dataview, removing rows whose **DsExpression** expression evaluates to *False*. Its DsExpression attribute value must be a Data Services-style expression which evaluates to *True* or *False*. In these expressions, the value of a data column is indicated by enclosing the column name in square brackets, not with an @Data token. Example expression: [Quantity] > @Request.Threshold~ See [Dsexpression Reference](https://devnet.logianalytics.com/hc/en-us/articles/4406822306071-Dsexpression-Reference) for guidelines regarding expressions. This element may be used in conjunction with **DsCompare Filter** elements, as discussed in [DataLayer.Data Services - Using DsCompare Filters](https://devnet.logianalytics.com/hc/en-us/articles/4406817290519-DataLayer-Data-Services-Using-DsCompare-Filters). |
| [DsGroup](https://devnet.logianalytics.com/hc/en-us/articles/4406817400343-DsGroup) | Adds a grouping operation to the Dataview, grouping rows based on the values of one or more columns. The names of the columns to be used for grouping are entered in the **Group Column** attribute, in a comma-separated list. Grouped row values can be aggregated by adding a **DsAggregate Column** element as a child of DsGroup. When grouping is applied, only values from the columns named in the Group Column and, if aggregating, the Aggregate Column attributes are returned to the datalayer. |
| [DsSort](https://devnet.logianalytics.com/hc/en-us/articles/4406816917783-DsSort) | Adds a sorting operation to the Dataview, sorting rows based on the values of one or more columns in the **Sort Column** attribute. You may specify more than one column, using a comma-separated list of column names. Multiple **Sort Sequence** attribute values may also be entered in the same way, corresponding to the named columns. |
