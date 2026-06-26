---
title: "The Unit Conversion Column"
id: 4419707858071
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707858071-The-Unit-Conversion-Column
updated_at: 2022-07-17T01:36:39Z
---

# The Unit Conversion Column

# The Unit Conversion Column

The **Unit Conversion Column** element is used with datalayer elements to convert values from one standard measurement to
another.

The following topics discuss the Unit Conversion Column element:

* [Applying the Unit Conversion Column](https://devnet.logianalytics.com/hc/en-us/articles/4419707857175-Applying-the-Unit-Conversion-Column#sec1)
* [Using Multiple and Dynamic Unit Conversion Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419723186199-Using-Multiple-and-Dynamic-Unit-Conversion-Columns#sec2)
* [Customizing the Conversion Factors](https://devnet.logianalytics.com/hc/en-us/articles/4419723185047-Customizing-the-Conversion-Factors#Factors)

## About the Unit Conversion Column

The Unit Conversion Column element is available for use with all datalayer elements.
In operation, the element basically performs a mathematic conversion on the specified data column value and places the result in a new column that's added to the datalayer. Here's an example showing the data before and after the Unit Conversion Column is applied, with settings for Temperature conversion:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714903703/unitconv_01.png)

Conversion factors are provided for a variety of measurement categories, including:

| * Area * Energy * Fuel Consumption * Length * Pressure | * Temperature * Velocity * Volume * Weight |

The actual conversion factors are stored in a file and developers who wish to add their own custom factors can do so. See [Customizing the Conversion Factors](https://devnet.logianalytics.com/hc/en-us/articles/4419723185047-Customizing-the-Conversion-Factors) for more information about customization.
