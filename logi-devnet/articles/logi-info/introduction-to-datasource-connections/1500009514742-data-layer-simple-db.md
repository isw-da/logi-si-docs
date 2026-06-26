---
title: "Data Layer.Simple DB "
id: 1500009514742
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514742-Data-Layer-Simple-DB
updated_at: 2021-06-17T01:58:13Z
---

# Data Layer.Simple DB 

# Data Layer.Simple DB

Amazon.com offers an online, distributed **data storage** environment, called **SimpleDB**. For developers who wish to work with Amazon Web Services' SimpleDB "database" facilities, Logi Info now offers the **DataLayer.SimpleDB** element. This topic discusses this datalayer.

* Attributes
* [Work with DataLayer.SimpleDB](#Working)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)Amazon publishes [general information](http://www.amazon.com/SimpleDB-AWS-Service-Pricing/b?ie=UTF8&node=342335011) about Amazon Web Services (**AWS**) SimpleDB, requires users to have an AWS account, and charges for their storage service. **DataLayer.SimpleDB***is not available for Logi Report*.

## Attributes

The **DataLayer.SimpleDB** element has the following attributes:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) Specifies the ID of a **Connection.SimpleDB** element in the application's \_Settings definition. *This element is discussed in more detail in the next section.* |
| ID | (Required through v10.1.46) A unique element ID. |
| Maximum Rows | Specifies a the **maximum** number of **data rows** to retrieve. If left blank, then all records that satisfy the query in the SimpleDB Query attribute will be retrieved. |
| SimpleDB Domain | (Required) Specifies the SimpleDB **domain** (similar to a database table) to query. |
| SimpleDB Query | Specifies the **query** to be used to retrieve data. If left blank, then all records will be retrieved (up to any limit specified in the Maximum Rows attribute).  [Amazon SimpleDB](http://www.amazon.com/SimpleDB-AWS-Service-Pricing/b?ie=UTF8&node=342335011) provides a simple custom query language for searching stored data. |

## Working with DataLayer.SimpleDB

In most respects, **DataLayer.SimpleDB** functions exactly as other **datalayer** elements do and its data can be **filtered** and **conditioned** using appropriate child elements. Like other datalayers, it works with a specific Connection element, **Connection.SimpleDB**, to connect to the Amazon web service.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778694295/dlsimpledb_01.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778694551/dlsimpledb_01a.gif)

As shown above, the **Connection.SimpleDB** element is added to the \_**settings** definition, beneath the **Connections** element. Its **SimpleDB Access Key** and **SimpleDB Secret Access Key** attribute values are set to match those of your Amazon Web Services account. Note that the Secret Access Key attribute will be **encrypted** by the Connection element before being sent over the Internet.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778694807/dlsimpledb_02.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778695063/dlsimpledb_02a.gif)

Next, in the report definition, a **DataLayer.SimpleDB** element is added as a child element of a data table or another data container element. Its attributes are set so that it accesses the desired SimpleDB connection and queries the desired domain (table) using the desired query.

The datalayer **reads** and **caches** the data from the SimpleDB web service. You can add **child elements** beneath the datalayer to affect its contents, including:

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
**Debugging Link** in your \_settings definition (**General** element) and using
the resulting link at the bottom of your report page to view the **Application
Trace** page. A link on the Trace Page will display the retrieved data.
