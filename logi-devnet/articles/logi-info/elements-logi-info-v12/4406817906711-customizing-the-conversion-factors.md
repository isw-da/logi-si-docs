---
title: "Customizing the Conversion Factors"
id: 4406817906711
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817906711-Customizing-the-Conversion-Factors
updated_at: 2022-04-06T06:08:58Z
---

# Customizing the Conversion Factors

# Customizing the Conversion Factors

The actual conversion factors are stored in the file:

<yourLogiApp>\rdTemplate\rdDataEngine\rdUnitConversion.xml

Developers who wish to add their own custom factors can do so by copying the file into the \_SupportFiles folder and making changes to it there. The application will look in that folder first for the file.
The XML data in the file consists ofmanyentries, including these three, which we'll use to explain the conversion factor requirements:
<Unit Name="Celsius" Scale="1" Shift="0" UnitType="Temperature" />   
<Unit Name="Fahrenheit" Scale="1.8" Shift="32" UnitType="Temperature" />  
<Unit Name="Kelvin" Scale="1" Shift="273.15" UnitType="Temperature" />

* The **Name** XML attributedefines the name of the conversion, which will be used in the element's To Unit and From Unit attributes.
* The **UnitType** XML attributedefines the measurement category and groups related conversion factors together.   
    
  Each unit type group begins with a "base unit" entry ("Celsius" in the example above) and all following conversion factors in the same group are calculated against it.
* The **Scale** XML attributeindicates the *multiplication* factor to be applied to the data column value during conversion, while the **Shift** XML attributeindicates the offset to be *added* to the result of the multiplication during conversion.  
    
  For example, if we have a data column with a value of 8-degrees Celsius, the conversion applied for Fahrenheit is:

( Data Value \* Scale Factor ) + Shift Factoror ( 8 \* 1.8 ) + 32 = 46.4

The use of tokens is not supported in the conversion factors file.
