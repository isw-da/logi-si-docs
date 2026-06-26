---
title: "DataLayer.CSV - Working with DataLayer.CSV"
id: 4406822246551
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822246551-DataLayer-CSV-Working-with-DataLayer-CSV
updated_at: 2022-04-06T06:05:10Z
---

# DataLayer.CSV - Working with DataLayer.CSV

# DataLayer.CSV - Working with DataLayer.CSV

In most respects, **DataLayer.CSV** functions exactly as other datalayer elements do and its data can be filtered and conditioned using appropriate elements. One major difference, however, is that *there is no need to use a Connection element in the \_settings definition with this element.* The DataLayer.CSV element directly accesses the file system to read .CSV files, if a file path is specified.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584030359/dlcsv_01.png)

* **Filtering**: Sort, group, or restrict the data
* **Extending**: Add virtual columns to the datalayer that contain
  aggregated, calculated, or totaled data values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report
  definitions

Data read into the datalayer is cached in XML format in memory and/or on the web server's file system. The
latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/4406817743895-The-Logi-Server-Engine) and may be of interest to developers working with
extremely large datasets or large numbers of concurrent users.

The data read with the datalayer is available using **@Data****tokens**,
in the format @Data.*ColumnName*~. The spelling of the column name is
**case-sensitive**. The data is only available within the scope of the
parent element of the datalayer, not throughout the entire report
definition. The DataLayer.Linked element can be used to make the data reusable
in another datalayer outside this scope.

The[Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4406822055959-Auto-Columns) element can be used to quickly display in your report all the data in a datalayer.

The data retrieved into the datalayer can be viewed by turning on the
Debugging Link in your \_Settings definition (**General** element) and using
the resulting link at the bottom of your report page to view the **Debugger Trace** page. An link on the Trace page can be clicked to display the retrieved data.
