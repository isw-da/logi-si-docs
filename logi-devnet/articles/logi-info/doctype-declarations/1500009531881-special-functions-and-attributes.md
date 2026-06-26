---
title: "Special Functions and Attributes"
id: 1500009531881
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531881-Special-Functions-and-Attributes
updated_at: 2021-06-17T01:58:38Z
---

# Special Functions and Attributes

# Special Functions and Attributes

Logi managed reporting products include **special functions** and **attributes** that provide special processing. These functions and attributes are discussed in this topic.

* IIF Function
* [CXMLDate Function](#CXMLData)
* [DontResolveTokensInData Attribute](#DontResolveTokens)
* [InputValueDelimiter Attribute](#InpValueDelim)

## IIF Function

VBScript and Javascript, widely used in Logi applications, do not have an "inline IF" or IIF function. This function, which allows **conditional processing** in a **single line** of code, is extremely useful in development environments like Logi Studio. Recognizing this need, Logi developers added this as an intrinsic function. The function's syntax is

IIF(*<expression>*, *<value if true>*, *<value if false>*)

The following examples illustrate some of the ways to use the IIF function. Note that the function name may need to be prefixed with an equals sign depending on the element and attribute.

### In a Label element's Caption attribute

The IIF function can be used in any "formula attribute", an attribute that is capable of evaluating a formula, such as the Label element's **Caption** attribute. For example,

=IIF("@Data.Column1~" = "1", "True", "False")

will display the appropriate text, True or False, in the Label based on the data value.

### In a Calculated Column Element's Formula Attribute

The IIF function can be used in combination with VBScript string functions in an expression to generate the correct value. The Calculated Column element has an attribute named Formula, for example,  the IIF function can be used in it to replace part of a SQL time string with the daylight or standard time acronym (EDT or EST):

    IIF(Right("@Data.CurrentDateTime~",6) = "-04:00", "EDT", "EST")

Note that the equals sign is not required before the "IIF" in this attribute. Relatively complex combinations of string functions can be created, including those that incorporate nested IIF functions.

## CXMLDate Function

Date data returned into a data layer by a query against a data source is in **ISO format**, which looks like this:

2007-05-31T13:30:00      representing yyyy-mm-ddThh:mm:ss

If you wish to use VBScript functions to **compare,** **manipulate, or format** the date data, you need to convert it into a compatible format. Logi's intrinsic **CXMLDate** function has been provided for this purpose. The following example uses a VBScript function to add one day to a date value,

=DateAdd("d", 1, CXMLDate("@Data.EnrollmentDate~"))

where the CXMLDate function has been used to convert the data retrieved from the **date-type column.**

Here's another example that finds the **difference**, in days, **between dates** in two separate date-type columns,

=DateDiff("d", CXMLDate("@Data.OrderDate~"), CXMLDate("@Data.ShippedDate~"))

and, once again, the CXMLDate function is used to convert the date values for use with the VBScript DateDiff() function.

## DontResolveTokensInData Attribute

There may be times when you need to **store****text** in a table column that includes **Logi tokens**: @*word*.*word*~. Under normal circumstances, when this text is retrieved into a data layer, the Logi Server Engine will attempt to **resolve****any tokens** in the data and, because there are (usually) no such tokens, words just disappear from the text data. Worse yet, if the tokens do happen to exist, then the resolved value is inserted into your text data.

Token processing can be **suppressed** by manually adding a special attribute to the **General** element in your application's \_settings definition. This is done in Logi Studio by selecting the \_settings definition, clicking the Source Viewer tab, and using the Edit button to open the definition for manual editing. Add the special attribute, **DontResolveTokensInData**, set to True, to the **General** element:

    <General DontResolveTokensInData="True" rdDebuggerStyle="DebuggerLinks"/>

The debugger style or any other attributes should remain as you already have them set. Save your definition and tokens will now be left alone when they appear in your data.

## InputValueDelimiter Attribute

Several elements have attributes that allow you to enter **multiple****values**. For example, when using an element that sends email messages, its "To Email Address" attribute allows you to enter multiple email addresses.

The **default delimiter** required between multiple values in these attributes is a **semi-colon**. However, if necessary, this delimiter character can be changed. This is done by manually adding a special **constant**. In Logi Studio, select the \_setting definition, click the Source Viewer tab, and use the Edit button to open the definition for manual editing. Add the following attribute to the **General** element:

<GeneralInputValueDelimiter="#" />

where the character between the quotes is the new delimiter (in the example, the # character). Leave the attributes for any other constants untouched. Note that this is an **application-wide change** and affects all attributes that allow multi-value entries. The example assumes you have at least one constant, so that the Constants element is present in your source code.
