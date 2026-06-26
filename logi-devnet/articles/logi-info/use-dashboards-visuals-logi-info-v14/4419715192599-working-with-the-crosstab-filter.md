---
title: "Working with the Crosstab Filter"
id: 4419715192599
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715192599-Working-with-the-Crosstab-Filter
updated_at: 2022-07-17T02:24:46Z
---

# Working with the Crosstab Filter

# Working with the Crosstab Filter

A **Crosstab Filter** element is required to convert, or "pivot", data retrieved into a datalayer for use in Crosstab Tables. In configuring this filter you specify three columns in the datalayer: the Crosstab Column, the Label Column, and the Value Column. You must also choose an aggregate function to apply to records from the Value Column.

![](https://devnet.logianalytics.com/hc/article_attachments/7522802125463/xtabtable_22.png)

The filter groups the data based on the designated Crosstab Column. If the Crosstab Column contains numerous distinct records, many Crosstab Value columns may be generated and the table can become quite wide. This can be controlled using the optional **Maximum Crosstab Columns** attribute, which limits the number of Crosstab Value columns that appear in the table.

Similarly, the **Maximum Crosstab Rows** attribute sets the maximum number of crosstab *rows* created by the Crosstab Filter. In some cases this number should be limited so that the table does not become too large in memory. The default limit is 10,000 rows.

## Extra Crosstab Label Columns

One Crosstab Table Label Column may not be sufficient to display all the necessary information in the table.

![](https://devnet.logianalytics.com/hc/article_attachments/7522815972119/xtabtable_23.png)

As shown above, developers can add **Extra Crosstab Label Column** elements beneath a Crosstab Filter element in order to add additional columns from the datalayer as Label columns.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Extra Crosstab Label Columns are for display only and do not support grouping.

To display the data for these extra label columns, an @Data token is used but the token identifier matches the ID of the Extra Crosstab Label Column element, not the datalayer column it represents, as shown above.

## Secondary Crosstab Label Columns

By adding the **Secondary Crosstab Label Column** element (instead of Extra Crosstab Label Columns) to your Crosstab Filter, you can group Value Columns and Label Columns together.

In this example, the Crosstab Filter is grouped by the Label Column *Region*:

![](https://devnet.logianalytics.com/hc/article_attachments/7522843813015/labelcolregion_1169x601.png)

Here's what the Crosstab Table looks like, as is:

![](https://devnet.logianalytics.com/hc/article_attachments/7522843821719/crosstabasis_1398x203.png)

1. First, add a **Secondary Crosstab Label Column** and give it an ID and asign a Label Column. In this example, we're adding "secCountry" with the Label Column "Country":

![](https://devnet.logianalytics.com/hc/article_attachments/7522830755607/seccountry_1199x496.png)

1. Then, add another **Secondary Crosstab Label Column** and give it an ID and assign a Label Column. In this example we're adding "secProductID" with the Label Column "ProductID":

![](https://devnet.logianalytics.com/hc/article_attachments/7522846490391/secproductid_1210x505.png)

1. Add two **Crosstab Table Label Columns** to the Crosstab Filter that reflect the Secondary Crosstab Label Columns. In this example, we're adding a Crosstab Table Label Column with the ID "colCountry", Column Header titled "Country", and a Label element captioned "@Data.secCountry~" and another Crosstab Table Label Column with the ID "colProductID", Column Header titled "Product ID", and a Label element captioned "@Data.secProductID~".
2. Adjust the Column Span of the Summary Column to reflect the number of Label Columns you are grouping together. In this example, we're adjusting the span to 3 columns:

![](https://devnet.logianalytics.com/hc/article_attachments/7522816006679/colspan_1191x630.png)

1. Select **Save** and **refresh** your report. Info displays the newly added *Country*, and *ProductID* Secondary Crosstab Label Columns:

![](https://devnet.logianalytics.com/hc/article_attachments/7522843854487/crosstabnew_1333x534.png)

1. You can go one step further and add a **Label Column Group** element for each of the Data Columns you want to group. In this example, we're adding a Label Column Group for "Region" and "secCountry":

![](https://devnet.logianalytics.com/hc/article_attachments/7522802208535/labelcolgroup_1240x532.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) You can also change the Merge Rows attribute to "True" (default value is "False") to merge the cells grouped together. You must do this for each Label Column Group you add.

1. Select **Save** and **refresh** your report. Info groups the *Region* and *Country* columns:

![](https://devnet.logianalytics.com/hc/article_attachments/7522816037143/crosstabgroup_1344x553.png)

Here's what your Crosstab Table looks like if you *merged* the cells:

![](https://devnet.logianalytics.com/hc/article_attachments/7522827270039/crosstabmerged_1351x535.png)

  

## Summarizing Across a Row

In [Comparing, Sorting, and Summarizing Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419715190551-Comparing-Sorting-and-Summarizing-Columns-) we saw that you can summarize crosstab *column* data (a vertical summary) and display the totals in a summary row at the bottom. You can also summarize crosstab *row* data (a horizontal summary) and show row totals in a separate column.

![](https://devnet.logianalytics.com/hc/article_attachments/7522816062615/xtabtable_24.png)

As shown above, the **Crosstab Row Summary Column** element can be added beneath a Crosstab Filter element to generate new columns in the filtered datalayer that contain aggregations of every value in each crosstab row.

You can specify an aggregation of *Average, AverageOfAllRows, Count, CountOfAllRows,**Max (v12.7), Min (v12.7), StdDev,* or *Sum.* For example, to count the number of value columns, set this attribute to *Count*; in the image above there are value columns for 2013, 2014, and 2015, so the value calculated will be 3.

Additional
**Crosstab Table Label Column** elements, such as "colRowTotal" above, can be added as needed to display the summarized results. The @Data token used to retrieve the data uses the ID of the Crosstab Row Summary Column element. So if, in the example above, the Crosstab Row Summary Column element was given an ID of "crsTotal", then *@Data.crsTotal~* would be used in a Label
element to display the data.

Similarly, a **Data Column Summary** element ("dcsTotal") can be added, configured to aggregate the "crsTotal" column, in order to total the new column vertically and include it in the Summary row at the bottom of the table.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Crosstab Filters can also be used with the datalayers that provide data for charts and gauges, however, they're designed for use with Crosstab Table elements and may not provide full functionality with other elements.

## The Include Condition Attribute

The Crosstab Filter element has an **Include Condition** attribute and if the value of this attribute is left blank or contains a formula that evaluates to *True*, the Crosstab Filter element is applied to the datalayer. If the value evaluates to *False*, the filter is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be manipulated or not.
