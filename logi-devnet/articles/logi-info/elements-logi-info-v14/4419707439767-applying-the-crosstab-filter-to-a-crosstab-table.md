---
title: "Applying the Crosstab Filter to a Crosstab Table"
id: 4419707439767
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707439767-Applying-the-Crosstab-Filter-to-a-Crosstab-Table
updated_at: 2022-07-17T02:24:51Z
---

# Applying the Crosstab Filter to a Crosstab Table

# Applying the Crosstab Filter to a Crosstab Table

The following example illustrates how the **Crosstab Filter** is used with a Crosstab Table:

![](https://devnet.logianalytics.com/hc/article_attachments/7522861912471/crosstab_02.png)  

1. Our goal is show total freight costs per employee per year. As shown above left, we start by retrieving Order data and joining it with to Employee data, based on Employee ID, which gives us the order data and the last name of the employee responsible for the order.
2. We want to show yearly summaries so, because the Order data is time-related, we use a **Time Period Column** element to parse out the Year value from the *OrderDate* column. Time Period Columns make working with parts of dates incredibly easy.
3. Then we add a **Crosstab Filter** element beneath a datalayer, and configure is as follows:
4. Set its **Crosstab Column** attribute to the data columns we want to see across the top. These will be the OrderDate years, so enter the *tpcOrderYear* column name here.
5. Set its **Label Column** attribute to the row labels we want to see down the left. These will be the employees' last names, so enter the *LastName* column here.
6. Set its **Value Column** attribute to the aggregated values we want to see at the intersections of the previous to items. This will be the freight cost, so enter the Freight column name here.
7. Finally, set its Value Function to the type of aggregation we want performed on the freight cost, in this case *Sum*.  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522861934743/crosstab_03.png)
8. Next we add a **Crosstab Table Label Column** element, as shown above left. This is the column our "label" information (the employee last name) will appear in and it's configured as shown.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522847600919/crosstab_04.png)
9. Then, as shown above, we add a **Label** element beneath the column element to actually display the data, and set its **Caption** to the @Data token for the value (the employee last name) we want to show.  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522853665943/crosstab_05.png)
10. Now things get a little more unusual: next we add a **Crosstab Table Value Columns** element, as shown above. This creates the columns (more than one) that will contain the annual aggregated freight value for each employee. So, it's unusual in that it creates *multiple* columns and also because it uses one of the **special Crosstab Table tokens** in its Column Header attribute, as shown above right. This token allows the column header to change depending on the data.  
      
      
      
    ![](https://devnet.logianalytics.com/hc/article_attachments/7522847622039/crosstab_06.png)
11. And finally, we add a Label element to display the data. Its Caption attribute value is provided using another special Crosstab Table token, as shown above. This provides the aggregated freight value for the right employee and year.

Now, let's see the effect of all this work:

![](https://devnet.logianalytics.com/hc/article_attachments/7522878614807/crosstab_07.png)

If we look at the data *prior* to passing it through the Crosstab Filter, the datalayer looks like the example shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522853691031/crosstab_08.png)

And here's what it looks like in the Crosstab Table.

Let's review the **special Crosstab Table tokens**, two of which were used to produce the results shown above:

| Token | Description |
| --- | --- |
| @Data.rdCrosstabColumn~ | The current Crosstab Table column header value. |
| @Data.rdCrosstabValue~ | The aggregated value for each label and column. |
| @Data.rdCrosstabValCount~ | The number of values aggregated to get the previous token's value. |

As we've seen, the Crosstab Table, using the Crosstab Filter, is a powerful tool for aggregating data and grouping it, especially by time periods.

## Crosstab Grouping

You can incorporate Crosstab grouping by adding the **Secondary Crosstab Label Columns** to your Crosstab Filter. This element works like the Extra Crosstab Label Columns element, except it can be used to group Value Columns and Label Columns together.

In this example, the Crosstab Filter is grouped by the Label Column *Region*:

![](https://devnet.logianalytics.com/hc/article_attachments/7522862009367/labelcolregion.png)

Here's what the Crosstab Table looks like, as is:

![](https://devnet.logianalytics.com/hc/article_attachments/7522878634263/crosstabasis.png)

1. First, add a **Secondary Crosstab Label Column** and give it an ID and assign a Label Column. In this example, we're adding "secCountry" with the Label Column "Country":

![](https://devnet.logianalytics.com/hc/article_attachments/7522831820311/seccountry.png)

1. Then, add another **Secondary Crosstab Label Column** and give it an ID and assign a Label Column. In this example, we're adding "secProductID" with the Label Column "ProductID":

![](https://devnet.logianalytics.com/hc/article_attachments/7522862054551/secproductid_1307x546.png)

1. Add two **Crosstab Table Label Columns** to the Crosstab Filter that reflect the Secondary Crosstab Label Columns. In this example, we're adding a Crosstab Table Label Column with the ID "colCountry", Column Header titled "Country", and a Label element captioned "@Data.secCountry~" and another Crosstab Table Label Column with the ID "colProductID", Column Header titled "Product ID", and a Label element captioned "@Data.secProductID~".
2. Adjust the Column Span of the Summary Column to reflect the number of Label Columns you are grouping together. In this example, we're adjusting the span to 3 columns:

![](https://devnet.logianalytics.com/hc/article_attachments/7522853756695/colspan_1307x692.png)

1. Select **Save** and **refresh** your report. Info displays the newly added *Country*, and *ProductID* Secondary Crosstab Label Columns:

![](https://devnet.logianalytics.com/hc/article_attachments/7522759669655/crosstabnew_1442x578.png)

1. You can go one step further and add a **Label Column Group** element for each of the Data Columns you want to group. In this example, we're adding a Label Column Group for "Region" and "secCountry":

![](https://devnet.logianalytics.com/hc/article_attachments/7522847728407/labelcolgroup_1335x573.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) You can also change the Merge Rows attribute to "True" (default value is "False") to merge the cells grouped together. You must do this for each Label Column Group you add.

1. Select **Save** and **refresh** your report. Info groups the *Region* and *Country* columns:

![](https://devnet.logianalytics.com/hc/article_attachments/7522853786903/crosstabgroup_1474x607.png)

Here's what your Crosstab Table looks like if you *merged* the cells:

![](https://devnet.logianalytics.com/hc/article_attachments/7522847771159/crosstabmerged_1477x585.png)

## Crosstab Summary

After you apply a Crosstab Filter, you can add Header Rows and Summary Rows to total the Data Columns you have grouped together.

### Summary Rows

1. Begin by adding a **Summary Row** element to your Secondary Crosstab Label Columns. In this example, we're adding a Summary Row to the "colCountry" Secondary Crosstab Label Column and giving it the ID "summaryRowCountry":

![](https://devnet.logianalytics.com/hc/article_attachments/7522795085207/sumrowcountry_1325x610.png)

1. **Save** and **refresh** your report. Info displays the Crosstab Table with a Summary Row for the *Country* column:

![](https://devnet.logianalytics.com/hc/article_attachments/7522795094679/crosstabsumrow_1547x338.png)

1. You can adjust the Summary Row span by adding a **Column Cell** element. In this example, we're adjusting the Column Span attribute to 2.
2. Then, add a **Label** element to the Column Cell element and add a Caption based on the Data Column you wish to tally, like below:

![](https://devnet.logianalytics.com/hc/article_attachments/7522847217175/sumrowcaption_1264x665.png)

1. Next, add a **Crosstab Table Summary Column** to your Summary Row element and give it an ID.
2. Below the Crosstab Table Summary Column, add a **Label** element and assign a Caption, based on the Data Column you are summarizing:

![](https://devnet.logianalytics.com/hc/article_attachments/7522802969111/ctsccountrylabel_1272x672.png)

1. **Save** and **refresh** your report. Info displays the Crosstab Table with the summarized column(s):

![](https://devnet.logianalytics.com/hc/article_attachments/7522816639767/crosstabsumcol_1556x587.png)

### Header Rows

1. Add a **Header Row** element beneath your Label Column Group element and give it an ID:

![](https://devnet.logianalytics.com/hc/article_attachments/7522759699223/headerrowcountry_1283x648.png)

1. **Save** and **refresh** your report. Info displays the Crosstab Table with the new Header Row:

![](https://devnet.logianalytics.com/hc/article_attachments/7522820397975/crosstabheaderrow_1550x563.png)

1. You can adjust the span of the Header Row by adding a **Column Cell** element and changing the Column Span attribute. In this example, we're adjusting the Column Span to 2.
2. Add a **Label** element beneath the Column Cell and give it a Caption based on the Data Column.
3. Next, add a **Crosstab Table Header Column** and give it an ID.
4. Then, add a **Label** element beneath the Crosstab Table Header Column and give it a Caption using the special Crosstab Table token " @Data.rdCrosstabColumn~", shown below:

![](https://devnet.logianalytics.com/hc/article_attachments/7522861793175/labelcrosstabcol_1306x684.png)

1. Select **Save** and **refresh** your report. Info displays the Crosstab Table with the new Header Columns:

![](https://devnet.logianalytics.com/hc/article_attachments/7522853552279/crosstabheadcol_1631x577.png)

You can repeat the previous steps for the Crosstab Filter Label Column (in these examples, *Region*) and additional Secondary Crosstab Label Column(s) (in these examples, *Product Id*).

## Crosstab Extras

There are five child elements that can be used beneath a Crosstab Filter, as follows:

| Token | Description |
| --- | --- |
| Crosstab Row Summary Column | Use this element to generate aggregated values for the table's columns. This basically adds an additional column to the datalayer. You can view the aggregated values by adding a Crosstab Table Label Column and specifying @Data.x~, where x is the ID of this element |
| Extra Crosstab Calculated Column | By default, the Crosstab Filter produces a single value for each column and row combination. This element allows a formula to be used to create additional values. These values can be displayed in a Crosstab Table Value Column element. In the Label element use the special token: @Data.rdCrosstabValue-myID~ where "myID" is the ID of this element. The formula used may reference special crosstab tokens. For example, if the Crosstab Value Column is "Cost" and an Extra Crosstab Value Column is "Price", we can calculate "Profit" with: @Data.rdCrosstabValue-Price~ - @Data.rdCrosstabValue~ In this case "Price" is the ID value of an Extra Crosstab Value Column element. @Data.rdCrosstabValue~ represents the "Cost" because it's the main value created with the Crosstab Filter. |
| Extra Crosstab Label Column | Crosstab Tables always have a label column that determines how values are grouped together. For some Crosstab Tables, you may want to display additional columns so that they can be included in a Crosstab Table element. For example, you may use a field called "EmployeeID" as the main label column to create the Crosstab. But, if you want to also show the employees' names, you should add an Extra Crosstab Label Column for the first and last name columns. These extra label columns are for display only; they are not used when determining the Crosstab Table rows. Reference the value with @Data.myID~, where myID is the value of this element's ID attribute. |
| Extra Crosstab Value Column | By default, the Crosstab Filter produces a single value for each column and row combination. This element provides for additional values, which can be displayed in a Crosstab Table Value Columns element. In the Label element use the special token: @Data.rdCrosstabValue-myID~ where "myID" is the ID of this element. |
| Secondary Crosstab Label Column | This element acts like the Extra Crosstab Label Column, but it allows the columns to be grouped together. Secondary Label Columns are for display only; they are not used when determining the Crosstab Table rows. |
