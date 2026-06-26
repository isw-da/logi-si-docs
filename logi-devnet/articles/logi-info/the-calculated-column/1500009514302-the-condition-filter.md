---
title: "The Condition Filter"
id: 1500009514302
section: "The Calculated Column"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514302-The-Condition-Filter
updated_at: 2021-06-17T01:58:06Z
---

# The Condition Filter

# The Condition Filter

The **Condition Filter** element is used with datalayer elements to filter out data rows. It's analogous to using a *WHERE* clause in a SQL query but, unlike a query, it's applied to data *after* it's been retrieved into the datalayer. The Condition Filter is available to all datalayer elements but is primarily designed for those lacking query capabilities, such as DataLayer.XML and DataLayer.Web Service. This topic discusses use of this element.

* Applying the Condition Filter
* [Using Multiple and Dynamic Condition Filters](#Dynamic)
* [Use with Compare Filters](#Compare)

## Applying the Condition Filter

The following example  illustrates how the **Condition Filter** is used:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771889175/condfilter_01.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771889431/condfilter_01a.gif)

1. As shown above, a **Condition Filter** element is added as a child to a datalayer element..
2. Its **Condition** attribute value is set to a formula that compares the data in the datalayer to some value. Note that no leading equals sign (=) is required here.

The sequence of events is, first, the datalayer reads in all the data from the XML data file, then the Condition Filter **removes** all records other than those where the condition formula evaluates to *True;* in this case, where the values in the *UnitPrice* column are greater than or equal to 40. All that remains in the datalayer for use in the report are records whose *UnitPrice* values are less than 40.

The Condition Filter element's **Condition** attribute supports **script****functions** and can evaluate them to filter data:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771889175/condfilter_01.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771889687/condfilter_02.gif)

1. As shown above, a **Condition Filter** element is added as a child to the DataLayer.XML File element.
2. Its **Condition** attribute value is set to a formula that uses the intrinsic function *Left* to compare the data in the datalayer to some value. Note that no leading equals sign (=) is required here.

The sequence of events is, first, the datalayer reads in all the data from the XML data file, then the Condition Filter **evaluates** the formula and **removes** all records where the first letter of the *CategoryName* column is not the letter *"C".* All that remains in the datalayer for use in the report are records whose *CategoryName* column values begin with "C".

Logi products include a set of *intrinsic* functions and operators modeled on VBScript, and these are always available for use in the Condition attribute. Depending on the selected scripting language for the app, you may also use VBScript or JavaScript in this attribute. Both are available in apps developed for .NET, while only JavaScript is available in apps for Java. This selection is made in the \_Settings definition, using the **General** element's **Scripting Language** attribute.

For more information about the intrinsic functions, see [Intrinsic Functions and Operators](https://devnet.logianalytics.com/hc/en-us/articles/1500009530801-Intrinsic-Functions-and-Operators).

## Using Multiple and Dynamic Condition Filters

1. Developers can use two or more **consecutive** Condition Filter elements:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778718359/condfilter_03.gif)

In this case, the conditions will be evaluated **sequentially**, based on their arrangement from top to bottom in the element tree. So, after the first condition filter is applied, only records that meet its criteria will remain in the datalayer to be evaluated for the second condition filter.

2. Developers can also **combine** two or more conditions in a Condition Filter element:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771889943/condfilter_04.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771890199/condfilter_04a.gif)

Any valid VBScript or Javascript-based formulae can be used in the Condition attribute, so separate conditions can be logically connected, as shown above, to create compound conditions. Even multi-line formulae are supported. Remember, the criteria for records to be retained in the datalayer is that the condition formula evaluates to *True*.

3. Developers can make Condition Filter elements **dynamic** by using tokens within conditions:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771889943/condfilter_04.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771890455/condfilter_05.gif)

As shown above, condition formulae can contain tokens such as @Request, so that comparison values are dynamic at runtime.

Sometimes it is necessary to ensure that tokens have default values when running a report. When using @Request tokens, the **Default Request Params** element can be used to create default values for each **@Request** token.

4. Beginning in v10.0.319, the Condition Filter element has an **Include Condition** attribute:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771889943/condfilter_04.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778718615/condfilter_06.gif)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be filtered or not.

## Use with Compare Filters

Beginning with v11.0.127, Condition Filters can also be used with Compare Filters to create complex expressions that include ANDs and ORs and levels of parentheses. For more information on Compare Filters, see [The Compare Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009529901-The-Compare-Filter).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778718871/condfilter_07.png)

For example, consider the element arrangement shown above. For each row of the datalayer, the three **Compare Filters** will be evaluated first. Each of them will produce a *True* or *False* value as a result of their comparison operations. Those values will be assigned to @Compare tokens which include the element ID, for example: @Compare.CompareFilter1~. The scope of these tokens is
limited to the parent Condition Filter.

After all of the Compare Filters are evaluated, the **Condition Filter** will be evaluated and its **Condition** attribute value can include expressions that use the @Compare tokens. For example, the Condition attribute value above might be:

@Compare.CompareFilter1~ AND (@Compare.CompareFilter2~ OR @Compare.CompareFilter3~)

And, of course, you can also use other types of tokens and literal values in the Condition attribute to get the expression you need, such as:

@Data.UnitPrice~ <= 100 AND (@Compare.CompareFilter1~ OR @Compare.CompareFilter2~)

You may be able achieve the same results with complicated scripting for the Condition attribute value, however, in most cases use of multiple Compare Filters as shown in this example will produce better performance than scripting.
