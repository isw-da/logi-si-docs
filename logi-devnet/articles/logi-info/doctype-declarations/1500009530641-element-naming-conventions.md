---
title: "Element Naming Conventions"
id: 1500009530641
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530641-Element-Naming-Conventions
updated_at: 2023-09-22T22:41:39Z
---

# Element Naming Conventions

# Element Naming Conventions

The element identifier (ID), an attribute of most elements, is very important and should always be set to a unique value. In addition, using a standard **naming convention** when setting IDs is good practice, as it results in a more easily understood definition. This topic discusses the naming conventions recommended by Logi Analytics.

* Element ID Notation
* [Formulate Mnemonics](#Formulating)
* [Suggested Mnemonics for Common Elements](#Mnemonics)

## Element ID Notation

These are the rules for the use of characters in element IDs:

* Any combination of letters, numbers, and the underscore ("\_"), dash ("-"), and period (".") characters may be used.
* However, an ID may not *begin* with a number. Valid: XYZ9   Invalid: 9XYZ
* Spaces within an ID are invalid and Logi Studio will automatically remove them from an ID value when the focus changes.
* All other characters or symbols may be entered but will result in an error when the definition is browsed.

Because spaces are invalid, we recommend that you use a combination of two well-known ID formatting schemes, "CamelCase" and "Hungarian" notation, when naming your elements.

### CamelCase Notation

CamelCase (sometimes called "CamelBack") notation is the practice of writing compound words or phrases in which
the parts are joined without spaces, with each part's
initial letter capitalized and the first
letter in either upper or lower case. For example: SampleDataTable.

### Hungarian Notation

IDs that use Hungarian notation identify elements by starting with one or more lower-case letters which are mnemonics for the type or purpose of the element, followed by whatever name you chose. An element that allows a user to input a starting date, for example, might be given the ID "inpStartDate", where "inp" indicates that it's a user input element. Similarly, a Label element that's used as a link to start an export to PDF might be given the ID "lblExportPDF".
These examples also show how the two notations are combined in an ID. 

### Standardization Is Good

The standardized use of these notational schemes provides numerous benefits, including promoting **uniqueness** and **consistency**. This can be especially helpful for developers who are new to Logi reporting products and who have not worked with them long enough to recognize the element icons.

When it comes to formulating element IDs, it's not necessarily important that you try to conform to some universal standard; what *is* important is that you use some consistent, meaningful standard, perhaps your own or your company's, regularly.

## Formulate Mnemonics

Here are some suggested guidelines for formulating the mnemonics used as element ID prefixes:

| Guideline | Examples |
| --- | --- |
| Use the first 2-3 letters of the element name | ag = Analysis Grid div = Division inp = Input Text |
| Use the first few letters of each sub-part of the element name | dt = Data Table dl = DataLayer gm = Google Map sdac = SubData Aggregate Column |
| Use all or part of the element name without vowels (three letters max) | dsh = Dashboard img = Image lbl = Label |
| Use sound-related, 3-letter combinations | btn = Button img = Image |
| Apply any of the above to the second part of a two-part element type | pie = Chart.Pie ndl = Animated Gauge.Needle |

## Suggested Mnemonics for Common Elements

This table presents suggested mnemonics for some commonly-used elements:

| Element | Mnemonic |
| --- | --- |
| Action | act |
| Analysis Grid | ag |
| Animated Chart.Pie | apie |
| Animated Chart.XY | axy |
| Button | btn |
| Chart.Pie | cpie |
| Chart.XY | cxy |
| Column | col |
| Connection | conn |
| Crosstab Table | xtb |
| Dashboard | dash |
| DataLayer | dl |
| DataLayer Link | dlnk |
| Data MultiColumn List | dmc |
| Data Table | dt |
| Data Tree | dtr |
| Dimension Grid | dg |
| Division | div |
| Event Handler | evh |
| Google Map | gm |
| Image | img |
| Interactive Data View | idv |
| Label | lbl |
| Procedure | proc |
| Response | rsp |
| Shared Element | shr |
| Target | trg |
| Task | tsk |
