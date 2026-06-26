---
title: "DataLayer.MongoDB"
id: 1500009514682
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514682-DataLayer-MongoDB
updated_at: 2021-06-17T01:58:12Z
---

# DataLayer.MongoDB

# DataLayer.MongoDB

**MongoDB** is a cross-platform, document-oriented database system, classified as a "NoSQL" database. Rather than using a traditional table-based, relational DB structure, it uses a collection of JSON-like documents with variable schemas. Logi Info and Report include the **DataLayer.MongoDB** element to retrieve data from this system. This topic discusses this datalayer.

* Attributes
* [Work with DataLayer.MongoDB](#Working)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771450519/plusicon.gif) General information about MongoDB can be found at the [official website](http://www.mongodb.com/).  
  
![](https://logianalytics.zendesk.com/hc/article_attachments/4402771462807/stopicon.gif)*This element was deprecated in v11.2.040 and replaced by three new MongoDB-specific datalayers.*

## Attributes

The **DataLayer.MongoDB** element has the following attributes:

| Attribute | Description |
| --- | --- |
| Collection | (Required) Specifies the name of the document collection to open. |
| Connection ID | (Required) Specifies the ID of a Connection.MongoDB element in the application's \_Settings definition. *This element is discussed in more detail in the next section.* |
| ID | A unique element ID. |
| Maximum Rows | Specifies a the maximum number of data rows to retrieve. If left blank, then all records that satisfy the request will be retrieved. |
| Preserve Hierarchy | Specifies if data is to remain in its original, hierarchical form. If set to *False*, the data is processed to create traditional rows and columns. Default: *True* |
| XPath | Specifies a standard XPath string that will be used to select a set of matching nodes. All of the matching nodes are then used to generate the resulting datalayer. |

## Work with DataLayer.MongoDB

In many respects, **DataLayer.MongoDB** functions exactly as other datalayer elements do and its data can be filtered and conditioned using appropriate child elements. Like other datalayers, it works with a specific Connection element, **Connection.MongoDB**, to connect to the datasource.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771862423/dlmongodb_01.png)

As shown above, the **Connection.MongoDB** element is added to the **\_Settings** definition, beneath the Connections element. Attributes are set appropriately for the MongoDB datasource.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778697495/dlmongodb_02.png)

Next, in the report definition, a **DataLayer.MongoDB** element is added as a child element of a data table or another data container element. Its attributes are set so that it accesses the desired MongoDB connection and data collection.

The datalayer **reads** and **caches** the data from the datasource. You can add standard **child elements** beneath the datalayer to affect its contents, including:

* **Filtering**: Sort, group, or restrict the data
* **Extending**: Add virtual columns to the datalayer that contain
  aggregated, calculated, or totaled data values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report
  definitions

The use of many of these elements is described in separate DevNet
documents.

Data read into the datalayer is cached in XML format in memory and/or on the web server's file system. The
latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/1500009515722-The-Logi-Server-Engine) and may be of interest to developers working with
extremely large datasets or large numbers of concurrent users.

The data read with the datalayer is available using **@Data****tokens**,
in the format @Data.*ColumnName*~. The spelling of the column name is
**case-sensitive**. The data is only available within the **scope** of the
**parent** element of the datalayer, not throughout the entire report
definition. The **DataLayer.Linked** element can be used to make the data reusable
in another datalayer outside this scope.

The data retrieved into the datalayer can be viewed by turning on the
**Debugging Link** in your \_Settings definition (**General** element) and using
the resulting link at the bottom of your report page to view the **Application
Trace** page. A link on the Debug page will display the retrieved data.

## Special Child Elements

As a "NoSQL database", MongoDB responds to its own command language rather than traditional SQL commands. DataLayer.MongoDB is provided with a special set of child elements that allow MongoDB commands to be issued, as described below:

| Element | Description |
| --- | --- |
| MapReduce | Specifies a JavaScript map-reduce operation, used to condense large volumes of data into useful aggregated results. See examples of the code for each attribute value below. |
| NoSQL Column | Specifies the data columns that are to be returned, in a case-sensitive, comma-separated list. |
| NoSQL Compare Filter | Limits returned data to documents that meet the comparison criteria. |
| NoSQL Filter | Limits returned data to documents that cause the expression to evaluate to *True*. Its NoSQL Expression attribute uses a JSON filtering statement, such as:    { $and:       [       { pop: { $gte: 5000 } },      { pop: { $lte: 5010 } }     ]    } |
| NoSQL Group | Groups the data based on the values found in one or more keys. May be used with the NoSQL Aggregate element to aggregate grouped values, using *Average*, *Count*, *Max*, *Min*, or *Sum* functions. |
| NoSQL Sort | Specifies the order of the data. |

## MapReduce Attribute Code Examples

The following attribute value examples give you an idea of how JavaScript is formatted and used in the MapReduce element.

Attribute: Map

function()   
{   
   var item = this;  
   emit(item.state, {count: 1, Population: item.pop} );  
}

Attribute: Reduce

function(key, values)   
{   
   var result = {count: 0, totalPopulation: 0};   
   values.forEach(  
      function(value)  
      {  
         if (value.Population != null) { result.totalPopulation += value.Population; }  
         result.count += value.count;  
      }  
   );   
   return result;   
}

Attribute: Finalize

function(key, value){  
   value.averagePopulation = value.totalPopulation / value.count;  
   return value;  
}
