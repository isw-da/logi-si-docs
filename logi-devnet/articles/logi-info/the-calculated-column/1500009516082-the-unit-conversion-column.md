---
title: "The Unit Conversion Column"
id: 1500009516082
section: "The Calculated Column"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009516082-The-Unit-Conversion-Column
updated_at: 2021-06-17T01:58:41Z
---

# The Unit Conversion Column

# The Unit Conversion Column

The **Unit Conversion Column** element is used with datalayer elements to convert values from one standard measurement to
another. This topic discusses use of this element.

* About the Unit Conversion Column
* [Applying the Unit Conversion Column](#sec1)
* [Use Multiple and Dynamic Unit Conversion Columns](#sec2)
* [Customizing the Conversion Factors](#Factors)

*This element is not available in Logi Report.*

## About the Unit Conversion Column

The Unit Conversion Column element, introduced in v10.01.18, is available for use with all datalayer elements.

In operation, the element basically performs a mathematic conversion on the specified data column value and places the result in a new column that's added to the datalayer. Here's an example showing the data before and after the Unit Conversion Column is applied, with settings for Temperature conversion:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771597591/unitconv_01.png)

Conversion factors are provided for a variety of measurement categories, including:

|  |  |  |
| --- | --- | --- |
|  | * Area * Energy * Fuel Consumption * Length * Pressure | * Temperature * Velocity * Volume * Weight |

The actual conversion factors are stored in a file and developers who wish to add their own custom factors can do so. See the section at the end of this topic for more information about customization.

## Apply the Unit Conversion Column

The following example illustrates how the **Unit Conversion Column** is used:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771597847/unitconv_02.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778499095/unitconv_02a.png)

1. As shown above, a **Unit Conversion Column** element is added as a child to a datalayer element.
2. Its **Data Column** attribute value is set to the name of the column in that datalayer whose value will be converted.
3. The **From Unit**  attribute is set to the unit of the data in the named Data Column.
4. The **ID** attribute sets the name of the new column that will be added to the datalayer, containing the converted value.
5. The **To Unit** attribute is set to the unit of the data that will be output to the new column.
6. The **Unity Type** attribute is set to the standard category name for the data units.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  At first release, the values for the From Unit, To Unit, and Unit Type attributes need to be typed in. See the lists shown in Studio's Information Panel when these attributes are selected for the available options. In later releases, these attributes will have pull-down lists of choices and will be dependent on the Unit Type pull-down selection.

## Use Multiple and Dynamic Unit Conversion Columns

1. Developers can use two or more **consecutive** Unit Conversion Column elements:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771598103/unitconv_03.png)

In this case, the conversions will be conducted **sequentially**, based on their arrangement from top to bottom in the element tree. So, after the first Unit Conversion Column is applied, the second Unit Conversion Column will be applied.

2. Developers can make Unit Conversion Column elements **dynamic** by using tokens:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778499351/unitconv_04.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778499607/unitconv_04a.png)

As shown above, all attributes other than the ID attribute, can use tokens such as @Request to make their values dynamic at runtime.

Sometimes it is necessary to ensure that tokens have default values when running a report. When using @Request tokens, the **Default Request Params** element can be used to create default values for each **@Request** token.

3. The Unit Conversion Column element also has an **Include Condition** attribute:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778499351/unitconv_04.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771598487/unitconv_05a.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be filtered or not.

## Customize the Conversion Factors

The actual conversion factors are stored in the file:

<yourLogiApp>\rdTemplate\rdDataEngine\rdUnitConversion.xml

Developers who wish to add their own custom factors can do so by copying the file into the \_SupportFiles folder and making changes to it there. The application will look in that folder first for the file.

The XML data in the file consists of many entries, including these three, which we'll use to explain the conversion factor requirements:

      <Unit Name="Celsius" Scale="1" Shift="0" UnitType="Temperature" />   
      <Unit Name="Fahrenheit" Scale="1.8" Shift="32" UnitType="Temperature" />  
      <Unit Name="Kelvin" Scale="1" Shift="273.15" UnitType="Temperature" />   
 

* The **Name** XML attribute defines the name of the conversion, which will be used in the element's To Unit and From Unit attributes.
* The **UnitType** XML attribute defines the measurement category and groups related conversion factors together.   
    
  Each unit type group begins with a "base unit" entry ("Celsius" in the example above) and all following conversion factors in the same group are calculated against it.
* The **Scale** XML attribute indicates the *multiplication* factor to be applied to the data column value during conversion, while the **Shift** XML attribute indicates the offset to be *added* to the result of the multiplication during conversion.  
    
  For example, if we have a data column with a value of 8-degrees Celsius, the conversion applied for Fahrenheit is:

( Data Value \* Scale Factor ) + Shift Factor    or    ( 8 \* 1.8 ) + 32 = 46.4

The use of tokens is not supported in the conversion factors file.
