---
title: "Element ID Notation"
id: 4406817402391
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817402391-Element-ID-Notation
updated_at: 2022-04-06T06:05:53Z
---

# Element ID Notation

# Element ID Notation

These are the rules for the use of characters in element IDs:

* Spaces within an ID are not allowed and Logi Studio will automatically remove them from the value when the focus changes.
* For an *optional* ID, you can use any characters except a space or a double-quote for its value.
* For a *required* ID, any combination of letters, numbers, and the underscore ("\_"), dash ("-"), and period (".") characters may be used, but an ID value may not *begin* with a number. For example, XYZ9 is valid, but 9XYZ is invalid.

Because spaces are invalid, we recommend that you use a combination of two well-known ID formatting schemes, "CamelCase" and "Hungarian" notation, when naming your elements.

## CamelCase Notation

CamelCase (sometimes called "CamelBack") notation is the practice of writing compound words or phrases in which
the parts are joined without spaces, with each part's
initial letter capitalized and the first
letter in either upper or lower case. For example: SampleDataTable.

## Hungarian Notation

IDs that use Hungarian notation identify elements by starting with one or more lower-case letters which are mnemonics for the type or purpose of the element, followed by whatever name you chose. An element that allows a user to input a starting date, for example, might be given the ID "inpStartDate", where "inp" indicates that it's a user input element. Similarly, a Label element that's used as a link to start an export to PDF might be given the ID "lblExportPDF".
These examples also show how the two notations are combined in an ID.

## Standardization Is Good

The standardized use of these notational schemes provides numerous benefits, including promoting **uniqueness** and **consistency**. This can be especially helpful for developers who are new to Logi reporting products and who have not worked with them long enough to recognize the element icons.
When it comes to formulating element IDs, it's not necessarily important that you try to conform to some universal standard; what *is* important is that you use some consistent, meaningful standard, perhaps your own or your company's, regularly.
