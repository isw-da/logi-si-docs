---
title: "DataLayer.XML - Working with DataLayer.XML"
id: 4406817338903
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817338903-DataLayer-XML-Working-with-DataLayer-XML
updated_at: 2022-04-06T06:05:31Z
---

# DataLayer.XML - Working with DataLayer.XML

# DataLayer.XML - Working with DataLayer.XML

Data in an XML file is required to be in a specific format for use within Logi reporting products: data rows must be child elements of the root element, and data columns must be attributes of the data rows. For example, here's a typical XML data file:

<CarInfo>  
<Car Brand="Alfa Romeo" Model="174 Hatchback" Code="1"/>   
<Car Brand="Aston Martin" Model="Spider Open" Code="5"/>   
<Car Brand="Audi" Model="Spider Open" Code="6"/>   
<Car Brand="Bentley" Model="Spider Open" Code="7"/>   
<Car Brand="BMW" Model="3 Series Convertible" Code="8"/>   
<Car Brand="BMW" Model="3 Series Coupe" Code="9"/>   
 <Car Brand="BMW" Model="5 Series Saloon" Code="10"/>   
<Car Brand="Cadillac" Model="Spider Open" Code="14"/>   
</CarInfo>

The example above illustrates the required formatting. When received into the datalayer, the data from this file will consist of eight data rows, each with Brand, Model, and Code columns.

The datalayer may be used with one or more child **XslTransform** elements, which use XSL files to transform the XML data *before* it's loaded into the datalayer. This allows the adjustment of XML data if it has a schema that cannot be understood by the Logi Server engine. For example, if the input XML comprises a data set with *two* tables, a transform can remove a table, since the datalayer expects only one.

Data may be returned in a hierarchical format, containing multiple levels of parent-child relationships. This structure can create difficulties for further processing and analysis. [The Flattener](https://devnet.logianalytics.com/hc/en-us/articles/4406817464343-The-Flattener) child element can be used to process hierarchical data into the standard datalayer tabular set of rows and columns.

XML data files make great temporary repositories for data retrieved from databases, possibly saving the overhead of another database query. For example, it may be faster or more efficient to *export* data retrieved from a database in one part of a Logi application out to a temporary XML file, then later, in another part of the application, *read it back in* with DataLayer.XML.

The following example shows DataLayer.XML in use:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584013079/dlxmlfile_01.png)

As shown above, a **DataLayer.XML** element has been added beneath a data table. Its **XML File/URL** attribute has been set to a value that can vary depending on the location of the actual file. There is **no query** or **search** feature; everything in the file will be pulled into the datalayer (where it can then be sorted, filtered, etc. using appropriate elements).

![](https://devnet.logianalytics.com/hc/article_attachments/4417563372823/dlxmlfile_02.png)

As shown above, one or more **XslTransform** elements can be added beneath the datalayer for each XSL transform to be applied to the XML data *before* it is retrieved into the datalayer. The same rules apply for the XSL file location and name as for the XML file (i.e. in the example above, the XSL file is in the \_SupportFiles folder).
