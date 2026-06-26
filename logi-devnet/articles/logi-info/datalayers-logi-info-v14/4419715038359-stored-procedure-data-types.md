---
title: "Stored Procedure Data Types"
id: 4419715038359
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715038359-Stored-Procedure-Data-Types
updated_at: 2022-07-17T02:03:00Z
---

# Stored Procedure Data Types

# Stored Procedure Data Types

Logi applications have the ability to work with database server Stored Procedures (SPs). These are subroutines that are stored on the database server and offer benefits that include centralization, faster performance, and increased security. Typically Logi developers interact with stored procedures using the **DataLayer.SP** element and this topic describes the data types used with SPs.

Topics include:

* About Stored Procedures
* [SP Parameter Data Types](#Types)

## About Stored Procedures

Like functions, SPs can be called with "input parameters", or arguments, that provide data to them, and they can return their results using output parameters. Logi products provide for this interaction with the **SP Parameters** container element, which is a child of DataLayer.SP, and its **SP Parameter** child elements.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699527063/spdata_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419714630295/spdata_01a.png)  

As shown above, one SP Parameter element is used for each parameter required by the SP. Generally, the number of input parameters the SP expects must match the number of SP Parameter
elements in the report definition, or an error will occur.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) Logi products still include the **SP Auto Parameters** and **SP Input Parameters** elements for backward compatibility with older Logi applications, but they are deprecated and developers *should not* use them for new Logi apps.

SP Parameters can be configured to be **input** or **output** parameters, and they're identified by the SP by their *order*, not by their *IDs*. For example, if the SP lists input parameters as @name, @city, @state, then three SP Parameter elements are used and they must be placed in the definition in a top-to-bottom order with the "name" element first, "city" element second, and "state" element third. The IDs of the SP Parameter elements are irrelevant.

Additional information about using stored procedures can be found in [DataLayer.SP](https://devnet.logianalytics.com/hc/en-us/articles/4419715229335-DataLayer-SP).

Because data is being passed from the web server to the database server and possibly back, **data typing** is important. So each SP Parameter element is also configured to indicate its **data type**, which maps to the data type declared in the SP for it. The data types used by Logi applications follow the OLEDB data types and will work with most database servers, in either .NET or Java environments.

## SP Parameter Data Types

The following data types are available when configuring SP Parameter elements:

| Data Type | Description |
| --- | --- |
| BigInt | (dt-20) A 64-bit signed integer. The data type represents integers with values ranging from *-9,223,372,036,854,775,808* through *9,223,372,036,854,775,807*. |
| Boolean | (dt-11) A Boolean value, of either *true* or *false* |
| BSTR | (dt-8) A null-terminated character string of Unicode characters. |
| Char | (dt-129) A null-terminated character string of characters. |
| Currency | (dt-6) A currency value ranging from *-922,337,203,685,477.5808* through *922,337,203,685,477.5807* with an accuracy to a ten-thousandth of a currency unit. |
| Date | (dt-7) Date data, stored as a Double. The whole portion is the number of days since December 30, 1899, and the fractional portion is a fraction of a day. |
| DBDate | (dt-133) Date data in the format *yyyymmdd*. |
| DBTime | (dt-134) Time data in the format *hhmmss*. |
| DBTimeStamp | (dt-135) Date and time data in the format *yyyymmddhhmmss*. |
| Decimal | (dt-14) A fixed precision and scale numeric value between *-10^38 -1* and *10^38 -1*. |
| Double | (dt-5) A floating-point number within the range of *-1.79E +308* through *1.79E +308*. |
| Empty | (dt-0) No value. |
| FileTime | (dt-64) A 64-bit unsigned integer representing the number of 100-nanosecond intervals since January 1, 1601. |
| GUID | (dt-72) A globally unique identifier or "GUID", a 128-bit integer (16 bytes) that can be used across all computers and networks wherever a unique identifier is required. Such an identifier has a very low probability of being duplicated |
| Integer | (dt-3) A 32-bit signed integer, representing values that range from *-2,147,483,648* through *2,147,483,647.* |
| LongVarBinary | (dt-205) A long binary value, that represents an array of unsigned integers with values that range from *0* to *255.* |
| LongVarChar | (dt-201) A long null-terminated string value. |
| LongVarWChar | (dt-203) A long null-terminated Unicode string value. |
| Numeric | (dt-131) An exact numeric value with a fixed precision and scale, between *-10^38 -1* and *10^38 -1*. |
| Single | (dt-4) A floating-point number within the range of *-3.40E +38* through *3.40E +38.* |
| SmallInt | (dt-2) A 16-bit signed integer, representing values ranging from *-32768* through *32767*. |
| TinyInt | (dt-16) An 8-bit signed integer, representing values ranging from *-128* to *127*. |
| UnsignedBigInt | (dt-21) A 64-bit unsigned integer, representing values ranging from *0* to *18,446,744,073,709,551,615.* |
| UnsignedInt | (dt-19) A 32-bit unsigned integer, representing values ranging from *0* to *4,294,967,295*. |
| UnsignedSmallInt | (dt-18) A 16-bit unsigned integer, representing values ranging from *0* to *65535.* |
| UnsignedTinyInt | (dt-17) An 8-bit unsigned integer, representing values that range from *0* to *255.* |
| UserDefined | (dt-132) Allows the developer to extend the database server's scalar type system. UDTs can contain multiple elements and can have behaviors, differentiating them from the traditional alias data types which consist of a single system data type. Useful for creating date, time, currency, extended numeric types, and working with geospatial data and encoded or encrypted data. |
| VarBinary | (dt-204) A variable-length stream of binary data, e.g. an array of bytes. |
| VarChar | (dt-200) A null-terminated, variable-length stream of non-Unicode characters. |
| Variant | (dt-12) A special data type that can contain numeric, string, binary, or date data, and also the special values Empty and Null. |
| VarNumeric | (dt-139) A variable-length numeric value between *-10^38 -1* and *10^ 38 -1*. |
| VarWChar | (dt-202) A variable-length, null-terminated stream of Unicode characters. |
| WChar | (dt-130) A null-terminated stream of Unicode characters. |

If in doubt about specific data types defined for your database server, consult its documentation for more information.
