---
title: "DataLayer.JSON File"
id: 1500009530181
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530181-DataLayer-JSON-File
updated_at: 2021-06-17T01:58:11Z
---

# DataLayer.JSON File

# DataLayer.JSON File

The **DataLayer.JSON File** element gives developers the ability to retrieve data from a JavaScript Object Notation (JSON) data file. It's useful for reading data files created using the **JQuery** library.

* Attributes
* [Work with DataLayer.JSON File](#Work_with_DataLayer.JSON_File)

## Attributes

The DataLayer.JSON File element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required through v10.1.46) Unique element ID. |
| JSON File | (Required) Specifies the JSON data file to be read. By default, the server will look in the app's \_SupportFiles folder, in which case you can simply specify the filename, such as mydata.js. You can also enter a fully-qualified path, such as c:\myfolder\data.js, or a location from the web, such as http://server/data.js. |
| XPath | Specifies a standard XPath string that will be used to select a set of matching nodes. All of the matching nodes are then used to generate the resulting datalayer. |

## Work with DataLayer.JSON File

Below is an example of JSON data in a data file:

|  |  |
| --- | --- |
|  | { "contact":   [     {       "firstName": "John",      "lastName" : "Smith",      "age"      : 25,      "streetAddress": "21 2nd Street",      "city"         : "New York",      "state"        : "NY",       "postalCode"   : "10021",      "phonenumber": "212 555-1234"    },    {      "firstName": "Daniel",      "lastName" : "Rivas",      "age"      : 34,      "streetAddress": "321 5th Avenue",      "city"         : "New York",      "state"        : "NY",      "postalCode"   : "10024",      "phonenumber": "212 207-1346"    }   ] } |

Here's an example of what it looks like as XML, in the correct Logi format, after being read into the datalyer:

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="utf-8"?> <rdData>   <dtContactJSON firstName="John" lastName="Smith" age="25" streetAddress="21 2nd Street" city="New York" state="NY" postalCode="10021" phonenumber="212 555-1234" />   <dtContactJSON firstName="Daniel" lastName="Rivas" age="34" streetAddress="321 5th Avenue" city="New York" state="NY" postalCode="10024" phonenumber="212 207-1346" /> </rdData> |

In case the JSON data is *not* in the correct format, the datalayer element has an optional child element, **XslTransform**, which can be used to transform the format of the retrieved JSON data *before* it's loaded into the datalayer. This allows the adjustment of JSON data that doesn't translate into the format shown above.

The following example shows **DataLayer.JSON File** in use:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778699543/dljson_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778699799/dljson_01a.png)

As shown above, a **DataLayer.JSON File** element has been added beneath a data table. Its **JSON File** attribute has been set to a value that can vary depending on the location of the actual file. There is **no query** or **search** feature; everything in the file will be pulled into the datalayer (where it can then be sorted, filtered, etc. using appropriate elements).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778700055/dljson_02.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771864983/dljson_02a.png)

As shown above, one or more **XslTransform** elements can be added beneath the datalayer for each XSL transform to apply to the XML data *before* it is retrieved into the datalayer. The same rules apply for the XSL file location and name as for the data file (for example, in the example above, the XSL file is in the \_SupportFiles folder).

For more information, see [Work with jQuery](https://devnet.logianalytics.com/hc/en-us/articles/1500009532401-Work-with-jQuery).
