---
title: "Errors and Exceptions"
id: 4405851140247
section: "Composer v6 Reference Information"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851140247-Errors-and-Exceptions
updated_at: 2021-09-21T01:29:22Z
---

# Errors and Exceptions

# Errors and Exceptions

When working with the SDK, the Composer client might return one or more error messages. The following tables describe all the error messages the SDK might return, and some possible solutions.

##### createQuery

| Error | Description | Solution |
| --- | --- | --- |
| metrics must be an array | The metrics attribute of the query configuration object is not an array. | Make sure metrics is an array, even if it's just an array of one. |
| invalid metrics | Metrics function, for example "avg" or "min", is not one of the expected values. | The metrics function must be one of the following: 'min' , 'max' , 'avg' , 'sum' , 'calc' , 'distinct\_count' , 'last\_value' , 'percentiles' |
| groups is not defined. fields is not defined. | The query configuration object has neither a groups attribute or a fields attribute. | Either groups or fields must be defined. See the [query configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851145879-Query-Configuration-Object) page for more information about the query configuration object. |
| groups is not defined. fields must be an array of field names | The query configuration object has a fields attribute that is not an array of field names, and doesn't define a groups attribute. | Make sure your fields attribute is an array, or add a groups attribute to the query configuration object. |
| groups must be an array of groups configurations. fields is not defined. | The query configuration object has a groups attribute that isn't an array of groups configurations, and doesn't have a fields attribute. | Make sure your groups attribute is an array. If you don't want a grouped query, add a fields attribute with an array of field names. |
| filters must be an array. | The query configuration object has a filters attribute that isn't an array of filter configurations. | Make sure your filters attribute is an array, even if it's an empty array [] or an array of just one configuration. |
| element expected | Configuration passed to visualize() does not have an 'element' attribute that is a web page element. | Check out the XYZ link to visualize sample |
| visualization doesn't exist | Using visualize(), you tried to create a visualization that doesn't exist. | Check the name of your visualization and make sure it is valid. If using a custom chart, make sure you copied the name exactly. |
| data set empty | The data set that you are trying to access is empty. | This message will result if you have a non-live (static) data source and the query to access it contains `pauseAfterRead` set to `false` . A query to static data sources should have `pauseAfterRead` set to true, otherwise the query attempts to read and reread the source. |
