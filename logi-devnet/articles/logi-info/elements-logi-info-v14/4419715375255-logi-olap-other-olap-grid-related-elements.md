---
title: "Logi OLAP - Other OLAP Grid-related Elements"
id: 4419715375255
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715375255-Logi-OLAP-Other-OLAP-Grid-related-Elements
updated_at: 2022-07-17T01:44:21Z
---

# Logi OLAP - Other OLAP Grid-related Elements

# Logi OLAP - Other OLAP Grid-related Elements

The topic describes the other elements available for use with the OLAP Grid.

## MDX Query Child Elements

In [Logi OLAP - Creating a Basic OLAP Grid](https://devnet.logianalytics.com/hc/en-us/articles/4419715373207-Logi-OLAP-Creating-a-Basic-OLAP-Grid), we saw that the **MDX Query** element was used to automatically build the OLAP MDX query. These child elements can be used with it to customize the query:

| Element | Description |
| --- | --- |
| Mdx Axis Dimension | Specifies the Dimensions that will be shown across the top or left side. Because the OLAP Grid allows user selection of Dimensions, only "default" Dimensions need to be specified.  There must be at least one Dimension for the left axis to see any OLAP results.   You may specify a Hierarchy in the DimensionName attribute. For example: [MyDimension].[MyHierarchy]  You may have any number of Mdx Axis Dimension elements for either Axis. |
| Mdx Drill-Down (child of Mdx Axis Dimension) | Specifies a single member of the dimension to be drilled into/ expanded. Multiple MdxDrilldown elements may be used. The Value attribute must be a member of the parent element's dimension.  Separate each level with the period character. When a member has spaces in the name, it must be enclosed in brackets.  Begin the Value with the dimension name. Example for the first level of the Customers dimension: [Customers].[All Customers]  When there are multiple dimensions on a single axis, the members of each axis must be separated by the asterisk character. Example with Customers:  [Customers].[All Customers].[USA].[CA]\*[Education Level].[All Education Level].[Graduate Degree]\*[Gender].[All Gender].[M]  Specify a Value of *AllMembers* to expand all members of the dimension. |
| Mdx Drill-Up (child of Mdx Axis Dimension) | Collapses a Dimension member that has been drilled-down. This may be used to undo drill-downs caused by an Mdx Drill-Down of *AllMembers*. |
| Mdx Calculated Measure | Adds an additional Measure from an MDX formula. The MDX Formula basically follows script syntax and typically references other measures. For example:  VAL((Measures.[Store Sales] - Measures.[Store Cost]) / Measures.[Store Sales])  Add an Mdx Measure element to display the calculated Measure. |
| Mdx Filter Dimension | Filters or slices values out of the OLAP cell set. Each Dimension to be filtered should have an Mdx Filter Dimension element. Add Mdx Filter Value child elements for each member to be included or excluded for cell calculations.  Dimensions cannot be used in Mdx Filter Dimension and Mdx Axis Dimension elements at the same time. |
| Mdx Measure | Specifies the Measures that will be shown in the cells of an OLAP Grid. Multiple Mdx Measure elements may be used. The cube's default measures are shown when none are specified.  Cells are formatted according to the format specified in the cube definition. Localization is applied to these formats according to the client browser's language setting. |

  

## OLAP Grid Child Elements

The following elements are available for configuring the OLAP Grid user interface and behavior. Panel-related elements can be used to hide panels; without them all panels are displayed.

| Element | Description |
| --- | --- |
| OLAP Calculated Measure Panel | Specifies the configuration of the OLAP Grid's Calculated Measures panel. The Calculated Measures panel is not available when working with a XOLAP Cube. |
| OLAP Chart Panel | Specifies the configuration of the OLAP Grid's Chart panel. |
| OLAP Dimension Panel | Specifies the configuration of the OLAP Grid's Dimensions panel. |
| Allowed Dimension (child of OLAP Dimension Panel) | Specifies the cube dimensions available in the OLAP Grid's Dimensions panel. Multiple elements may be used.   Use the Security Right ID attribute to set the available dimensions based on the user's roles.  If none of these elements are present, *all* cube dimensions will be available for selection. |
| OLAP Drillthrough | This element enables "drill-through" on cell values. It adds drill-through links that appear as the user hovers over each cell. When clicked, a new page is displayed with a basic Data Table listing the drill-through rows with all the columns used to build the cube.  The element is not available for calculated measures or when there are multiple dimensions on either the left or top axis.  The Caption attribute sets title of the drillthrough page.  The MaxRows attribute sets the maximum number of rows that will be returned shown in the drillthrough table. The default is *1000* rows.  Drillthrough is functional when connecting to Analysis Services 2005 and later. It is *not* functional for AS2000 or XOLAP Cubes. |
| OLAP Filter Panel | Specifies the configuration of the OLAP Grid's Filters panel. |
| Allowed Filter Dimensions (child of OLAP Filter Panel) | Specifies the cube dimensions available in the OLAP Grid's Filters panel. Multiple elements may be used.   Use the Security Right ID attribute to set the available dimensions based on the user's roles.  If none of these elements are present, *all* cube dimensions will be available for filtering. |
| OLAP Heat Map Panel | Specifies the configuration of the OLAP Grid's Heat Map panel. |
| OLAP Measure Panel | Specifies the configuration of the OLAP Grid's Measures panel. |
| Allowed Measure (child of OLAP Measure Panel) | Specifies the cube measures available in the OLAP Grid's Measures panel. Multiple elements may be used.   Use the Security Right ID attribute to set the available measures based on the user's roles.  If none of these elements are present, *all* cube measures will be available for selection. |
| OLAP Menu Panel | Specifies the configuration of the OLAP Grid's Menu panel. |
| OLAP Table Panel | Specifies the configuration of the OLAP Grid's Table panel. |
| Generated Plug-in Call | Specifies a Plug-in method to be run. The method is called after its parent element is parsed into its XML definition. |
