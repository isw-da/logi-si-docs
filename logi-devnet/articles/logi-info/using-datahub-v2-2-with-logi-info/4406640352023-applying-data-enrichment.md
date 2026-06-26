---
title: "Applying Data Enrichment"
id: 4406640352023
section: "Using DataHub v2.2 With Logi Info"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406640352023-Applying-Data-Enrichment
updated_at: 2022-04-01T03:13:19Z
---

# Applying Data Enrichment

# Applying Data Enrichment

Data that's retrieved into DataHub can be enriched in multiple ways to make it easier to use and more understandable. Enrichment is automatically applied, based on the Dataview definition, and this topic discusses how to configure data enrichment.

* [About Data Enrichment](#About)
* [Set Column Properties](#Properties)
* [Create a Calculated Column](#CalcCol)
* [Create a Multi-Part Column](#MultiCol)
* [Create a Conversion Column](#ConvCol)

## About Data Enrichment

"Data Enrichment" is the term altering the Dataview definition for data in DataHub's data repository in order to enhance it. Some enrichment actions are passed through in metadata to applications consuming the Dataview, while others also actually cause new columns and data to be added to the data repository. Enrichment consists of the following possible actions:

* Set a column's "physical" name (the name displayed in DataHub)
* Categorize a column as a Dimension or a Metric value
* Set a column's data type Sub-Category
* Set a column's display Format
* Create a new Calculated column
* Create a new Multi-Part column
* Create a new Conversion column

All of these actions are undertaken in a Dataview's Data Enrichment tab:

![](https://devnet.logianalytics.com/hc/article_attachments/5160436308247/enrichment_01.png)

and are discussed individually in the following sections. The image above shows the selected column properties, identifies the column selection indicator (simply click a column to select it), and identifies the column "Gear" icon used to display a drop-down menu of options.

Click the **Save** icon  ![](https://devnet.logianalytics.com/hc/article_attachments/5160422532375/iconsaveblack.png) to save changes.

Click the **Reset** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160453970071/iconresetblack.png) to restore all the properties for a column to their original values.

Click the **Preview** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160470654103/iconpreviewblack.png) to preview the effects of formatting changes. Note that this requires the Physical Name property be the same as the original name of the column in the data (the Source Name). Use Reset icon to undo any previewed changes.

## Set Column Properties

After selecting a Dataview and clicking its Data Enrichment tab, select a column by clicking it.

![](https://devnet.logianalytics.com/hc/article_attachments/5160466875415/enrichment_02.png)

The column properties that can be set are shown above and include:

1. **Physical Name** - This property is the column name that will be displayed in the column header and elsewhere, sometimes called the "friendly" name. The Source Name (the name of the column in the data repository) is shown below it for reference.
2. **Category** - This property lets you specify if the column should be treated as a Dimension (an independent variable - usually descriptive or categorical) or a Metric (a dependent variable - usually numeric). DataHub makes an initial assignment based on its analysis of the data, but you may wish to change it.
3. **Sub-Category** - This property further categorizes the column. If the main category is set to Dimension, then options here include *Boolean*, *Identity*, *Location*, *Numeric*, *Temporal*, and *Text*. If set to Metric, then options include *Currency*, *Decimal*, and *Integer*. DataHub makes an initial assignment based on its analysis of the data, but you may wish to change it.
4. **Format** - This property determines how the data values in this column will be formatted for display. Options displayed here are related to the Sub-Category property setting and include a wide variety of formats.
5. **Special Properties** - Depending on the Sub-Category property value, other special properties may be displayed.

Remember to click the **Save** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160422532375/iconsaveblack.png) to save your changes.

## Create a Calculated Column

The ability to create calculated columns is a very useful enrichment activity and DataHub makes it easy to do. A calculated column adds a new column in the data repository and is usually the result of operations on one or more existing columns. Once defined, a calculated column is created automatically when the Dataview is loaded.

In the following example, we'll create a new column that contains the results of multiplying the Quantity column by the UnitPrice column.

![](https://devnet.logianalytics.com/hc/article_attachments/5160436412183/enrichment_03.png)

To get started, we'll hover the mouse cursor over the gear icon of one of the existing columns, Quantity, as shown above, and select the *Calculation* drop-down menu item.

![](https://devnet.logianalytics.com/hc/article_attachments/5160470705303/enrichment_04.png)

The Calculation panel, shown above, will appear, with these keyed elements:

1. **Built-in Functions** - Hover your mouse cursor over one of these built-in functions to see its description, click to add it to the expression area. See the section below about using special SQL functions.
2. **Expression Area** - This is where you build your expression for generating the calculation column values. You can type directly into this field, if desired. Field names *must* be enclosed in [square brackets] and, as soon as you type an opening square bracket, a list of available columns will be shown for you to choose from.
3. **Operators** - Click to add one of these standard operators to the expression.
4. **Test Area** - Click Test to run the expression and see the results in this area.
5. **New Column** - The new column will be inserted into the columns at the bottom of the page, to the right of the column whose gear icon menu you used, and marked as the selected column.

Click the **Save** icon  ![](https://devnet.logianalytics.com/hc/article_attachments/5160422532375/iconsaveblack.png) to save the new calculated column. To exit the Calculation panel, select a different column by clicking on it. You can then re-select the new calculated column and set its properties (for example, you may want to change its name).

Click the **Reset** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160453970071/iconresetblack.png) to clear the expression and results *before* previewing the new column.

Click the **Preview** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160470654103/iconpreviewblack.png) to preview the calculated column, which will be populated with values based on the expression.

Click the **Delete** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160422557079/icondeleteblack.png) to delete the calculated column altogether and start over. To exit the Calculation panel, select a different column by clicking on it.

### Handling Null Values

Null values in a column pose special challenges. In an application consuming a Dataview, they may be considered when grouping on the column
but may not be included in aggregates and charts. While this may
be the desired behavior, there are situations where a Null
value should be counted. In those cases, the Null must be converted to a
real value (e.g. "N/A", 0, -1, "Unknown"). This calculated column
expression can be used to convert the Null values to a
real value:

IFNULL ([column], 'N/A')

### Special SQL Functions

For Dataviews that use database sources, you can use SQL functions if the built-in functions aren't sufficient.

![](https://devnet.logianalytics.com/hc/article_attachments/5160422559383/enrichment_05.png)

As shown in the example above, you can wrap an ANSI SQL-92-compliant function in a "SQL\_FUNCTION( )" structure in your expression and it will be understood and executed as part of the query used in the data retrieval process. DataHub column names must still be enclosed in square brackets. Complex SQL statements, like this, are supported:

SQL\_FUNCTION("CASE WHEN [Country] = 'Argentina' THEN 1 ELSE 0 END")

## Create a Multi-Part Column

A multi-part column is a special column type that
combines the values from two or more existing columns. It generally behaves
in
DataHub as a dimension (text) column. Once defined, a multi-part column is created automatically when the Dataview is loaded.

Common examples include complete addresses and full names. A complete address
column might be created by combining values from street address, city, state, and zip
code columns. A full name column might combine first name, middle initial, and
last name column values.

You could accomplish the same result
with a calculated column, however, you wouldn't be able to manage the
parts as you can with a multi-part column.

In the following example, we'll create a new column that combines the values of the First\_Name and Last\_Name columns.

![](https://devnet.logianalytics.com/hc/article_attachments/5160422564247/enrichment_06.png)

To get started, we'll hover the mouse cursor over the gear icon of one of the existing columns, First\_Name, as shown above, and select the *Multipart* drop-down menu item.

![](https://devnet.logianalytics.com/hc/article_attachments/5160422573079/enrichment_07.png)

The Multi-part panel, shown above, will appear, with these keyed elements:

1. **Drop-Zone** - This area is where you drag-n-drop the other columns that you want to combine with the original column.
2. **Preview** - Shows the columns with the selected separator separating them.
3. **Separation** - Select one of the standard separator characters: *None*, *Space*, *Comma*, *Slash*, or *Dash*.
4. **New Column** - The new column will be inserted into the columns at the bottom of the page, to the right of the column whose gear icon menu you used, and marked as the selected column.

Now you're ready to add the next part of the new column:

![](https://devnet.logianalytics.com/hc/article_attachments/5160467021335/enrichment_08.png)

To combine columns, drag the desired column pill header from the bottom of the page and drop it into the drop zone, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/5160422586775/enrichment_09.png)

The panel will look like the example above and, if you click the Preview icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160470654103/iconpreviewblack.png), the new column at the bottom of the page will populate with preview data. If you're combining more columns, just repeat the process.

Click the **Save** icon  ![](https://devnet.logianalytics.com/hc/article_attachments/5160422532375/iconsaveblack.png) to save the new multi-part column. To exit the Multi-Part panel, select a different column by clicking on it. You can then re-select the new multi-part column and set its properties (for example, you may want to change its name).

Click the **Reset** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160453970071/iconresetblack.png) to clear the dropped columns.

Click the **Delete** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160422557079/icondeleteblack.png) to delete the multi-part column altogether and start over. To exit the Multi-part panel, select a different column by clicking on it.

## Create a Conversion Column

Conversion columns let you convert measurements and DataHub makes it easy to convert column values including time, length, temperature and
weight measurements. For example, a column containing data in ounces can be used to create a column containing the same data converted to pounds.

This feature is similar to calculated columns but is limited to a fixed set of
standard data conversions, so you don't have to find or recall the
conversion formulae. You also don't have to recall the SQL syntax required to
complete the task as you would by using a calculated column to perform this
function.

Here are the categories and units that can be converted with a Conversion column:

| Category | Units |
| --- | --- |
| Time | Year, Month, Week, Day, Hour, Minute, Second, Millisecond |
| Length | Kilometer, Meter, Centimeter, Millimeter, Mile, Yard, Foot, Inch, Nautical Mile |
| Temperature | Celsius, Fahrenheit, Kelvin |
| Weight | Pounds, Ounces, Kilograms, Grams, Milligrams, Long Ton, Short Ton, Metric Ton |

In the following example, our dataview contains a column named MinTemp\_C that contains Celsius scale data values. Our goal is to create a new
Conversion column that will contain the same values converted to the Fahrenheit scale.

![](https://devnet.logianalytics.com/hc/article_attachments/5160436627991/enrichment_10.png)

To get started, we'll hover the mouse cursor over the gear icon of the MinTemp\_C column, as shown above, and select the *Conversion* drop-down menu item.

![](https://devnet.logianalytics.com/hc/article_attachments/5160470824215/enrichment_11.png)

The Conversion panel, shown above, will appear, with these keyed elements:

1. **Column** - The name of the column containing the values to be converted.
2. **Category** - The category of measurement units being converted: *Time*, *Length*, *Temperature*, or *Weight*.
3. **From Value & Units** - The source measurement unit and example source value from the first record.
4. **To Value & Units** - The target measurement unit and example converted value from the first record.
5. **New Column** - The new column will be inserted into the columns at the bottom of the page, to the right of the column whose gear icon menu you used, and marked as the selected column.

Click the **Save** icon  ![](https://devnet.logianalytics.com/hc/article_attachments/5160422532375/iconsaveblack.png) to save the new conversion column. To exit the Conversion panel, select a different column by clicking on it. You can then re-select the new conversion column and set its properties (for example, you may want to change its name).

Click the **Preview** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160470654103/iconpreviewblack.png) to preview the conversion column, which will be populated with values based on the conversion.

Click the **Delete** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160422557079/icondeleteblack.png) to delete the calculated column altogether and start over. To exit the Conversion panel, select a different column by clicking on it.
