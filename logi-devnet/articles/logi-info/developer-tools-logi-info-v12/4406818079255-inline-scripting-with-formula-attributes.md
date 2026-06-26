---
title: "Inline Scripting with \"Formula\" Attributes"
id: 4406818079255
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818079255-Inline-Scripting-with-Formula-Attributes
updated_at: 2022-04-06T06:10:01Z
---

# Inline Scripting with "Formula" Attributes

# Inline Scripting with "Formula" Attributes

Some element attribute values, such as the **Label** element's **Caption** attribute and the **Calculated Column** element's **Formula** attribute, are categorized as "formula" attributes. This means they can evaluate inline script expressions and use the results as their values. In attributes where what to do might be ambiguous - display the text or evaluate it - the use of a leading equals sign (=) is used to indicate that the text should be evaluated. Typically, the functions
called
in these expressions are the standard intrinsic functions and run *at the server*.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583624087/scripting_01.png)

For example, consider the Label element attributes shown above. The **Caption** attribute contains an expression that starts with an equals sign and calls the intrinsic Left() function in an expression, and will result in the word "Logi" appearing on the report page. This is an easy way to work with individual functions.

Later, we'll see how to include external files with custom functions that can be called in formula attributes.

## Error Handling

Elements that support inline scripting also have an **Error Result** attribute. If something is specified in this attribute, it will be displayed or used instead of the expression result if an error occurs.

The default Error Result varies depending on the element. For example, for the Condition Filter, the default is *False*. For the Calculated Column and
Extra Crosstab Calculated Column elements, the default is *blank*. For other elements, the
default is *???*.

Two special constants are available to control error handling related to expressions that have the possibility of causing a divide-by-zero situation. If needed, specify these constants in the \_Settings definition:

rdInfinityErrorResult - Specifies a global result for expressions that may produce a divide-by-zero situation (result: infinity), sparing developers the task of specifying a result on a per-element basis in their Error Result attributes.

rdJavascriptInfinityIsError - When set to *True*, specifies that expressions that produce a divide-by-zero situation (result: infinity) will trigger an error, which is then handled by elements' Error Result attribute or, if set, the rdInfinityErrorResult constant. If rdJavascriptInfinityIsError is not specified, the Logi Server Engine will return the value *NaN* (for "Not a Number") by default when a division-by-zero
attempt occurs.
