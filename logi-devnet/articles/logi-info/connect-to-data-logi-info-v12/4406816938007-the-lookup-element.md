---
title: "The Lookup Element"
id: 4406816938007
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816938007-The-Lookup-Element
updated_at: 2022-04-06T06:02:59Z
---

# The Lookup Element

# The Lookup Element

The **Lookup** element is used with datalayer elements to perform a "look up" of related data. It runs its own datalayer once for each row in its parent datalayer and joins the results. Unlike a typical join, it doesn't require that all of the target data be downloaded before the join occurs. This topic discusses use of this element.

The following sections are covered in this topic:

* About Lookup
* [Using Lookup](#sec1)

## About Lookup

The **Lookup** element is available for use with all datalayer elements. It's particularly useful and provides improved performance when trying to join small data sets to very large data
sets. For example, when trying to correlate the IDs and names of a few dozen sales people with the employee IDs found in thousands of sales records.

In operation, the element basically runs its child datalayer once *for each row* in its parent datalayer. In other words, it loops through its entire parent datalayer, performing for each row a "look up" in its child datalayer for matching data. Logi developers who work with Process tasks may recognize this as behavior analogous to the operation of the Procedure.Run DataLayer Rows element.

## Using Lookup

The following example illustrates how the **Lookup**  is used:

![](https://devnet.logianalytics.com/hc/article_attachments/4417591995543/lookup_01.png)

1. As shown above, a **Lookup**  element is added as a child to a datalayer element. There are no required attributes for the element.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417591995799/lookup_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417591996183/lookup_02a.png)
2. Beneath it, add a child datalayer, as shown above. In the example, it's a **DataLayer.SQL** element and its **Source** attribute will use a token (which refers to the data in the parent datalayer) in its query for the correct Employee record:  
     
   SELECT \* FROM Employees WHERE EmployeeID = @Data.EmployeeID~  
     
   If the child datalayer is a different type that doesn't support a query, such as DataLayer.XML File, use the @Data token from above in a Condition or Compare Filter to get the correct data. Note, however, that you must use a special "nested" @Data token. Basically, this is a token-within-a-token; the inner token gets evaluated first, then the outer token. It looks like this:  
     
    @Data.@Request.column\_name~~  
     
   Yes, it has two @ signs and two tildes. The Request token gets evaluated first, providing the column name for the @Data token. This is necessary due to the order in which the Logi Engine processes elements.

After the look up is complete, the data found by the Lookup element will be available for display, etc. using regular @Data tokens.   
The Lookup element also has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/4417591995799/lookup_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417591996439/lookup_03.png)

If the value of this attribute is left blank or Lookups a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the Lookup element will be used or not.
