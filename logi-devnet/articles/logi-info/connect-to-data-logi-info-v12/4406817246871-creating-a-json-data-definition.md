---
title: "Creating a JSON Data Definition"
id: 4406817246871
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817246871-Creating-a-JSON-Data-Definition
updated_at: 2022-04-06T06:04:54Z
---

# Creating a JSON Data Definition

# Creating a JSON Data Definition

A JSON Data definition uses a small subset of the standard Logi Info elements, most of them related to data retrieval and manipulation.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584054807/usingdatadefs_05.png)

The first element that needs to be added in any JSON Data definition is a **Json Data** element,asshownabove. It will run a datalayer, insert the results into a JSON JavaScript variable, and streams it.

Its attributes are:

| Attribute | Description |
| --- | --- |
| ID | (Required) A unique element ID. |
| Json Var Name | (Required) When used in Data definitions, this should always be set to *Exclude*. |
| Json Human Readable | Specifies whether spaces and LFs are used to format the output JSON data, for easier debugging. |
| Json Output | When used in Data definitions, this should always be blank, or *Inline.* |
| Json Style | This attribute specifies the format of the data output; either as *RowsToObjects,**RowsToValueArrays,* or as *ColumnsToPropertyArrays*. See the discussion below with output examples. Default: *RowsToObjects* |
| Security Right ID | Controls access to this element when using Logi Security. Provide the ID of a Right defined in the application's \_Settings definition and only users that have a Role referenced in the Right will be able to use the data. Multiple Right IDs, separated by commas, may be entered. |

![](https://devnet.logianalytics.com/hc/article_attachments/4417584055063/usingdatadefs_06.png)

Next, we add a datalayer beneath the Json Data element. In the example above, we've used DataLayer.Static to make it easy to see the data. And we're done. You can, of course, have more complex data arrangements, using any of the usual datalayer types, filters, JOINs, and other elements to retrieve and manipulate the data set.

## Using Different Json Styles

The Json Data element can format its data in three different ways, using its **Json Style** attribute:

{ "data": [{"CategoryID" : "1", "sumFreight" : "500"}, {"CategoryID" : "2", "sumFreight" : "521"}, {"CategoryID" : "3", "sumFreight" : "600"}, {"CategoryID" : "4", "sumFreight" : "750"}, {"CategoryID" : "5", "sumFreight" : "900"}, {"CategoryID" : "6", "sumFreight"
: "902"}] }

If Json Style is left blank or set to *RowsToObjects*, the data from our example will be formatted as shown above. The datalayer rows are serialized into an array of objects, where each object represents a data row and the objects have a property for each column.

{ "data": { "CategoryID" : ["1", "2", "3", "4", "5", "6"], "sumFreight" : ["500", "521", "600", "750", "900", "902"] } }

If Json Style is set to *ColumnsToPropertyArrays*, the data from our example will be formatted as shown above. The datalayer is serialized into a single object, where each column is a property with all the row values contained in an array.

{ "data": [["1", "500"], ["2", "521"], ["3", "600"], ["4", "750"], ["5", "900"], ["6", "902"]] }

Or, finally, if it's set to *RowsToValueArrays*, the data will be formatted as shown above. This serializes
the data into a single array with a child array for each row in the
data. Each value in the array represents a column in the data.

You need to select the format that works with the client applications that will consume the data.
