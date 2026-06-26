---
title: "DataLayer.MDX - Using MDX Query Elements"
id: 4406822263703
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822263703-DataLayer-MDX-Using-MDX-Query-Elements
updated_at: 2022-04-06T06:05:20Z
---

# DataLayer.MDX - Using MDX Query Elements

# DataLayer.MDX - Using MDX Query Elements

When working with an OLAP Table or OLAP Grid element, you can have the Logi Engine create the MDX query for you by using DataLayer.MDX and the **MDX Query** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584025111/dlmdx_03.png)

The example above shows the datalayer with its MDX Query child element. The name of the target data cube must be provided, as shown.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584025239/dlmdx_04.png)

Beneath the MDX Query element, you add child elements to define the dimensions, measures, and filters needed, as shown above. When the application runs, the Logi Engine will use these elements to create the appropriate query.

The available child elements, and their child elements, include:

| Element | Description |
| --- | --- |
| MDX Axis Dimension | Specifies adimension that will be shown in the OLAP Gridor OLAP Table, across the top or left side. You may have any number of MDX Axis Dimension elements for either axis. Generally, the OLAP Table requires these elements, becausethe user has no way to add them at runtime. However, since the OLAP Grid allows user selection of dimensions, MDX Axis Dimensions need only be specified for "default" dimensions. There must be at least one dimension defined for the left axis to see any results. You may specify a hierarchy in the Dimension Name attribute, e.g. [MyDimension].[MyHierarchy]. |
| Child: MDX Drill-Down | Specifies a single member of the dimension to be drilled/expanded. You may add any number of MDX Drill-Down elements. Their Value attribute must be a member of the parent element's dimension. Separate each level with the period character, and when a member has spaces in the name, it must be enclosed in brackets. Begin the Value with the dimension name, e.g. [Customers].[All Customers].   When there are multiple dimensions on a single axis, the members of each axis must be separated by the asterisk character. For example:  [Customers].[All Customers].[USA].[CA]\*[Education Level].[All Education Level].[Graduate Degree]\*[Gender].[All Gender].[M]  Specify a Value of *AllMembers* to expand all members of the dimension. |
| Child: MDX Drill-Up | Used tocollapse a dimension member that has been drilled-down. This may be used to undo drill-downs caused by settingMDX Drill-Down to *AllMembers*. |
| Child: MDX Find | When present, automatically drills down and filters to show all members that contain the specified Value. *Available only when using the OLAP Grid element.* |
| Child: MDX Member Property | Specifies a single member property that will be displayed with the appropriate member values. Each member property is listed in its own column to the right of the Dimension Members. The column only appears when there is at least one member that has the property. Add an MDX Member Property element for each property to be listed. At runtime, users can change the properties when the OLAP Grid element's Pick Member Properties attribute is *True*. *Available only when using the OLAP Grid element.* |
| MDX Calculated Measure | Adds an additional measure based on an MDX formula. MDX formulae basically follow intrinsic functionsyntax and typically references other measures. For example:  VAL((Measures.[Store Sales] - Measures.[Store Cost]) / Measures.[Store Sales])  Add an MDX Measure element to display the calculated measure. |
| MDX Filter Dimension | Filters or slices values out of the OLAP cell set. Each dimension to be filtered should have an MDX Filter Dimension element. *Dimensions cannot be used in both this elementand MDX Axis Dimension elements at the same time*. |
| Child: MDX Filter Value | Specifies a single member to be included in, or excluded from, the cell calculations. You may have any number of MDX Filter Values for each dimension. The Value attribute must be a member of the MDX Filter Dimension element's dimension. Separate each level with the period character. When a member has spaces in the name, it must be enclosed in brackets. Example: [USA].[CA] |
| MDX Measure | Specifies a measure that will be shown in the OLAP Grid or OLAP Table cells. You may have any number of MDX Measure elements. If none of these elements are included, the cube's default measures will be shown. Cells are formatted according to the format specified in the cube definition. Localization is applied to these formats according to the browsers language setting. |

The data retrieved into the datalayer can be viewed by turning on the **Debugging Link** in the \_Settings definition (General element) and using the resulting link at the bottom of the report page to view the **Application Trace** page. A link on the Trace page will display the retrieved data.
