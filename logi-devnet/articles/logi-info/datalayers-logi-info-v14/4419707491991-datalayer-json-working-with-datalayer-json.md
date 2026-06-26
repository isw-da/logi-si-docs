---
title: "DataLayer.JSON - Working with DataLayer.JSON"
id: 4419707491991
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707491991-DataLayer-JSON-Working-with-DataLayer-JSON
updated_at: 2022-07-17T02:24:39Z
---

# DataLayer.JSON - Working with DataLayer.JSON

# DataLayer.JSON - Working with DataLayer.JSON

This element reads the data in a JSON file and converts it to XML in a datalayer:

{ "contact":  
[  
{   
"firstName": "John",  
"lastName" : "Smith",  
"age" : 25,  
"streetAddress": "21 2nd Street",  
"city" : "New York",  
"state" : "NY",  
 "postalCode" : "10021",  
"phonenumber": "212 555-1234"  
},  
{  
"firstName": "Daniel",  
"lastName" : "Rivas",  
"age" : 34,  
"streetAddress": "321 5th Avenue",  
"city" : "New York",  
"state" : "NY",  
"postalCode" : "10024",  
"phonenumber": "212 207-1346"  
}  
]  
}  
  
An example of JSON data in a data file is shown above...

<rdData>  
 <dataTable\_JsonFile>  
 <contact>  
 <firstName>John</firstName>  
 <lastName>Smith</lastName>  
 <age>25</age>  
 <streetAddress>21 2nd Street</streetAddress>  
 <city>New York</city>  
 <state>NY</state>  
 <postalCode>10021</postalCode>  
 <phonenumber>212 555-1234</phonenumber>  
 </contact>  
 <contact>  
 <firstName>Daniel</firstName>  
 <lastName>Rivas</lastName>  
 <age>34</age>  
 <streetAddress>321 5th Avenue</streetAddress>  
 <city>New York</city>  
 <state>NY</state>  
 <postalCode>10024</postalCode>  
 <phonenumber>212 207-1346</phonenumber>  
 </contact>  
 </dataTable\_JsonFile>  
</rdData>

...and here's what it looks like as XML, above, after being read into the datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Data is usually in a hierarchical format, containing multiple levels of parent-child relationships. This structure can create difficulties for further processing and analysis. The **Flattener** child element processes hierarchical data into a tabular format, which is necessary when displaying data in most elements, like the Data Table.

<rdData>  
 <dataTable\_JsonFile firstName="John" lastName="Smith" age="25" streetAddress="21 2nd Street" city="New York" state="NY" postalCode="10021" phonenumber="212 555-1234"/>  
 <dataTable\_JsonFile firstName="Daniel" lastName="Rivas" age="34" streetAddress="321 5th Avenue" city="New York" state="NY" postalCode="10024" phonenumber="212 207-1346"/>  
</rdData>

The code above shows the effects of applying the Flattener to the data shown earlier. It "flattens" the data into the row-column format that Logi elements expect.
You can also apply one or more child **XslTransform** elements, which use XSL files to transform the XML data *before* it's loaded into the datalayer. This allows the adjustment of JSON data if it has a schema that cannot be understood by the Logi Server engine. For example, if the data comprises a data set with *two* distinct tables, a transform can remove a table, since the datalayer expects only one.
Let's see an example of DataLayer.JSON in use:

![](https://devnet.logianalytics.com/hc/article_attachments/7522826398231/dljson_01.png)

As shown above, a **DataLayer.JSON** element has been added beneath a Data Table. Its **Json File/URL** attribute has been set to a value that can vary depending on the location of the actual file. There is no query or search feature; everything in the file will be pulled into the datalayer (where it can then be sorted, filtered, etc. using appropriate elements).

![](https://devnet.logianalytics.com/hc/article_attachments/7522830189719/dljson_01a.png)

Next, a Flattener element is added and configured, as shown above, to flatten the example data we saw above into a tabular format.

![](https://devnet.logianalytics.com/hc/article_attachments/7522830191383/dljson_01b.png)

The resulting Data Table is shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The Flattener inserts a column in the datalayer, "rdFlattenedElement", which can assist you during development to understand the process. More information about the Flattener element is available in [The Flattener](https://devnet.logianalytics.com/hc/en-us/articles/4419722921623-The-Flattener).

![](https://devnet.logianalytics.com/hc/article_attachments/7522830197399/dljson_02.png)

Though not related to the example data we've already seen, one or more **XslTransform** elements may be added beneath the datalayer to apply transforms to the data *before* it is retrieved into the datalayer, as shown above. The same rules apply for the XSL file location and name as for the data file (i.e. in the example above, the XSL file is in the \_SupportFiles folder).

## New for 14.1 Pagination

Info now supports pagination from a Json data source, allowing you to handle large amounts of data results with ease. DataLayer.JSON automatically detects the link without any additional configuration, as long as that data source has that pagination mechanism and follows the standard RFC5988. We assemble all of the pages into a single data set and the engine consumes that data set to generate results.

Specify the page size by setting the limit in the URL Path in the datalayer, or, defer to the default page size (200). Limit the number of data rows received by entering a number in the 'Maximum Rows' field.

![](https://devnet.logianalytics.com/hc/article_attachments/7522804827159/restful_pagination_json.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Your results only return the number of records defined by the limit and they will not include a link to additional pages.
