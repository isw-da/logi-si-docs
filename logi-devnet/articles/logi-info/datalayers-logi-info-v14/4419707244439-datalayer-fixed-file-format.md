---
title: "DataLayer.Fixed File Format"
id: 4419707244439
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707244439-DataLayer-Fixed-File-Format
updated_at: 2022-07-17T02:03:48Z
---

# DataLayer.Fixed File Format

# DataLayer.Fixed File Format

The **Fixed File Format** datalayer enables retrieval of data from a text file in which
the values are in a format specified by column widths.

The following sections are covered in this topic:

* Attributes
* [Working with DataLayer.Fixed File Format](#Working)

## Attributes

The **DataLayer.Fixed File Format** element has the following attributes:

| Attribute | Description |
| --- | --- |
| Fixed Format File | (Required) The location and name of the fixed format file. The path should not contain spaces, and can be a web server path, such as C:\Data\records.txt or a URL, such as http://www.example.com/data/records.txt |
| ID | An optional element ID. Recommended for easier identification when debugging. |
| Connection ID | Specifies a connection to a datasource that's defined in the \_Settings definition. |
| Maximum Rows | The maximum number of rows to retrieve from the file. |
| Start Row | The row number at which to begin reading data. Default: *1*. |

## Working with DataLayer.Cached

The Fixed File Format datalayer enables retrieval of data from a text file in which the values occupy a certain number of characters and are not otherwise delimited.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714620439/dlfixedfmt_01.png)

The example above shows data of this type; the first "column" of data is eight characters wide, the second is two characters wide, and the last one is five characters wide. To use the datalayer, you must define the record layout using
a **Fixed Record Layout** element and one or more **Data Field** elements.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699505559/dlfixedfmt_02.png)

In the example shown above, a **DataLayer.Fixed Format File** element has been added as a child element beneath a Data Table and its attributes set as shown. The **Fixed Format File** attribute will accept a value that's a literal web server file path, with an optional token (as shown above), or a fully-formed URL beginning with HTTP://.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699505815/dlfixedfmt_03.png)

Next, a Fixed Record Layout element has been added as a container for three Data Field elements. The Data Field elements are used to described each "column" of data in the text. Using the example data shown at the beginning of this section, the attributes for the first Data Field element has been set to be 8 characters long and its data type has been set to Date. The column name for this data in the datalayer will be the ID of the Data Field element: *colDate*.

The remaining Data Field elements are then configured to describe all of the data columns. If their Data Type attribute is left blank, the data will be treated as text.

You can add other child elements beneath DataLayer.Fixed File Format and/or its child datalayers to modify the data, including:

* **Filtering**: Sort, group, or restrict the data
* **Extending**: Add virtual columns to the datalayer that contain
  aggregated, calculated, or totaled data values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report
  definitions

Data retrieved into the datalayer is cached in **XML** format, in memory and/or on the web server's file system. The latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/4419715421975-The-Logi-Server-Engine) and may be of interest to developers working with extremely large datasets or large numbers of concurrent users.

The data in the datalayer is available using **@Data****tokens**,
in the format @Data.*ColumnName*~. The spelling of the column name is
**case-sensitive**. The data is only available within the **scope** of the
**parent** element of the datalayer, not throughout the entire report
definition. The **DataLayer.Linked** element can be used to make the data reusable
in another datalayer outside this scope.

The [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419700048023-Auto-Columns) element can be used to quickly display in your report all the data in a datalayer.

The data retrieved into the datalayer can be viewed by turning on the
**Debugging Link** in your \_settings definition (**General** element) and using
the resulting link at the bottom of your report page to view the **Debugger Trace Report** page. There will be clear indications when the cache is being built and when data from it is being used. A link on the Trace page will display the actual cached data.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699506199/dlfixedfmt_04.png)

Studio includes a **wizard** that will add elements for the **columns** in the datalayer to your definition. You can select the desired columns before the operation begins. With the datalayer's parent **Data Table** or similar element selected in the Definition Editor, click the wizard link, shown above, in the Element Toolbox.
