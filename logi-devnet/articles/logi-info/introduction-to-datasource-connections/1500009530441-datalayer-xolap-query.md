---
title: "DataLayer.XOLAP Query"
id: 1500009530441
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530441-DataLayer-XOLAP-Query
updated_at: 2021-06-17T01:58:15Z
---

# DataLayer.XOLAP Query

# DataLayer.XOLAP Query

The **DataLayer.XOLAP Query** element is used to predefine a data view based on a Logi XOLAP Cube. It creates the view that will be displayed by a Dimension Grid and can also be used with the OLAP Grid and OLAP Table elements.

* About DataLayer.XOLAP Query
* [Attributes](#Attributes)
* [Work with DataLayer.XOLAP Query](#Working)

For additional information see [Logi XOLAP](https://devnet.logianalytics.com/hc/en-us/articles/1500009515602-Logi-XOLAP).

## About DataLayer.XOLAP Query

The DataLayer.XOLAP Query element behaves a little differently than the usual datalayer in that it does not connect to a datasource and retrieve data. Instead, it works with a Logi XOLAP cube that has already been populated with data (using other datalayers), creating a view of the data for use with other elements.

DataLayer.XOLAP Query is simply a parent element for elements that specify the dimensions that appear on the top and left
axes of other elements such as the Dimensions Grid. The order in which dimensions are defined for an axis determines the order
in which they are displayed. For example, if a dimension showing "customer
city" is provided first, followed by a dimension showing "customer marital
status", the user will be able to drill down to a particular city and then drill
down on marital status to see measures for each marital status in that
city.

The datalayer can also specify which measures will be
displayed in the report and can include member properties and filters.

## Attributes

The DataLayer.XOLAP Query element has no attributes other than an element **ID** (required through v10.1.46).

## Work with DataLayer.XOLAP Query

As mentioned earlier, this element does not retrieve data as most datalayers do. Logi XOLAP operations involve two data-related steps: first, the creation of a virtual data cube (which uses one of the other datalayer types), and second, reporting against that data cube, optionally using DataLayer.XOLAP Query.

If DataLayer.XOLAP Query is not used as part of the second step, then reporting takes place against *all* of the data in the cube. When it is used, then it defines a view of the data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778684567/dlxolapquery_01.png)

The example above shows a datalayer that retrieves data for the XOLAP cube and DataLayer.XOLAP Query, which is the parent element for a number of elements that can be used to define the data view. The possible child elements are:

| Element | Description |
| --- | --- |
| XOLAP Query Measure | Defines which measures will be shown in the cells of a Dimension Grid. If no measure is specified, the first one defined in the XOLAP Cube is used. Measures are formatted according to the XOLAP Cube element's Format attribute. |
| XOLAP Query Axis Dimension | Defines a dimension of the XOLAP Cube that will appear in the report on the left or top axis. |
| XOLAP Query Drill-Down | Defines a level of a XOLAP Query dimension that will be expanded to show its child values. Each dimension shows the "All" level by default. A drill-down element causes a level of child values to be added to the report. The parent level of a drill-down can be included if desired but is not necessary.  For example, a drill-down with a value of [Customers].[All Customers].[USA].[California] would cause the report to show all cities in California, whether there is a drill-down for states in USA or not.  To define a drill-down on a second or lower dimension, separate each position with an asterisk, for example: [Product].[All Products]\*[Customers].[All Customers].[USA] |
| XOLAP Query Member Property | This child element is added beneath an axis dimension to make a member property defined in the XOLAP Cube appear in the Dimension Grid when the corresponding level of that dimension is visible. |
| XOLAP Query Filter Dimension | Specifies a filter that will be applied to the default view of the Dimension Grid. In the grid's user interface, the filter's pop-up listing of checked and unchecked members only recognizes a Filter Type attribute value of *Exclude*. |
| XOLAP Query Filter Value | Specifies a single member to be included in, or excluded from, the cell calculations. Any number of these filters may be provided for each dimension.  The element's Value attribute value must include members of the XOLAP Query Filter Dimension element's dimension and each level is separated with the period character. If a member has spaces in its name, it must be enclosed in square brackets:  Example: [USA].[CA] |

The data retrieved into the datalayer can be viewed by turning on the **Debugging Link** in the \_Settings definition (General element) and using the resulting link at the bottom of the report page to view the **Application Trace** page. A link on the Trace page will display the retrieved data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)   Prior to v11.0.727, you could not use a **DataLayer Link** element beneath DataLayer.XOLAP Query used with an OLAP Grid. This arrangement was not allowed and caused a "pipeline processing" error. In v11.0.727+, the link is allowed.
