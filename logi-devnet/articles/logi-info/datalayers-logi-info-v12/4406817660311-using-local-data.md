---
title: "Using Local Data"
id: 4406817660311
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817660311-Using-Local-Data
updated_at: 2022-04-06T06:07:28Z
---

# Using Local Data

# Using Local Data

A special data container element, **Local Data**, can be used to make data available *anywhere* within the report:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563167127/introdl_06.png)

As shown above, Local Data is a child of the report root element, not of the Body or other lower elements. The data values retrieved by Local Data's child datalayer is accessed using special **@Local** tokens, in the format @Local.*ColumnName*~. These tokens can be used *anywhere* in the report, and this is an excellent way to use data, for example, in headers and footers.

If there are multiple Local Data elements in use, it may be difficult to determine which data came from which Local Data element. To make usage easier to understand, if a Local Data element is given an element ID, then that ID can be incorporated into its tokens. For example, if the Local Data element ID is "localOrders" and its datalayer queries the Northwind Orders table,
this token can be used to access Freight column data: @Local.localOrders.Freight~. This is an optional notation variantyou may wish to use to improve definition readability.

By themselves, @Local tokens can only be used to access the values of the *first row* of the data retrieved under Local Data. However, you can use the linking elements shown earlier to link the Local Data datalayer to other datalayers in the report definition, which then provides access to *all rows* of data in the Local Data datalayer. The linked data will then be subject to the same rules as those for any other datalayer (scope limited to its parent element and accessed using @Data tokens).

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Developers often use this technique (linked Local Data datalayers) to reduce data retrieval to one query, which is then re-used via linking in multiple places in the report, for best performance.

## Using Multiple Local Data Elements

It's also common to use multiple Local Data elements in the same report definition. They will run *sequentially*, not simultaneously, so that data from one can be used in the query of another. In the data retrieved, the effect is a "union" of all of the Local Data data.

Local Data datalayers are run before other datalayers, so data from them can be used to condition the retrieval of data by other datalayers. Their datalayers are *not* re-run with all AJAX refresh requests. They are only re-run when the element being refreshed contains either a DataLayer.Linked element linked to the Local Data datalayer, or when it contains an @Local token.

The Local Data element has a **Condition** attribute. If the value of this attribute is left blank or contains a formula that evaluates to *True*, then the element's child elements (its datalayers) will run. If the value evaluates to *False*, the element is ignored and the datalayers are not run. This allows developers to dynamically determine when the Local Data should be run, or re-run if a page is refreshed (in this case, a @Request token can be used in the formula
in the Condition attribute).

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) This can be very useful, for example, if you just want to run the Local Data datalayer *once* when the report is first loaded.

## Handling Columns with the Same Name

If you're using multiple Local Data elements, it's possible that their datalayers could retrieve data from data sources with similar schema and identical column names.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583819671/introdl_16.png)

In the example shown above, suppose that LocalData1![](https://devnet.logianalytics.com/hc/article_attachments/4417563168919/menuarrowrt_26x13.png)DataLayer.SQL retrieves a column named "EmployeeID" and LocalData2 ![](https://devnet.logianalytics.com/hc/article_attachments/4417563168919/menuarrowrt_26x13.png)DataLayer.XML does too. What will happen? When the data from both datalayers is combined, the values for EmployeeID from the first datalayer will be *overwritten*
by the values
from the second datalayer. Using
the @Local.EmployeeID~ token later in the application will only produce values from the second datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583820183/introdl_17.png)

To make the values from the first datalayer available, use a **Calculated Column** element, as shown above, beneath it. This will add a new column with the same values but a different name. Then in the application, use the @Local.calcEmployeeID~ token to access the values.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) If the EmployeeID column contains string values, in the Formula attribute you'll need to enclose the @Data.EmployeeID~ token in double-quotes.
