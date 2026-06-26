---
title: "Local Data is Available Everywhere"
id: 4406822074007
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822074007-Local-Data-is-Available-Everywhere
updated_at: 2022-04-06T06:02:55Z
---

# Local Data is Available Everywhere

# Local Data is Available Everywhere

Logi Studio data tables are great for retrieving data but have a
**scope limitation**: their data is only "available" to their
child elements, usually within data table columns of some sort. The same
applies to charts. However, you may need to use data in other places in
your definition that may not be part of a data table, chart, or a similar
element. This can be accomplished using the
**Local Data** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417592005527/localdata_01.png)

The **Local Data** element, shown above, is a container for datalayers
and related child data access and manipulation elements. The data in its
child datalayer is available, using the **@Local** token,
*anywhere* in the report definition.
A Local Data datalayer can retrieve any number of rows, however, only
the values of the *first* row will be available through the @Local
token. This makes Local Data ideal for situations where a database
"lookup", returning just a single row, is needed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417592005783/localdata_03.png)

However, if you use a **Data Layer Link** element to save the Local
Data data, as shown above, and later use a
**DataLayer.Linked** element to re-use the data, then *all* of
the rows are available for use, using the **@Data** token.The Local Data element has a **Condition** attribute. If the
value of this attribute is left blank or contains a formula that
evaluates to *True*, then the element's child elements (its
datalayers) will run. If the value evaluates to *False*, the
element is ignored and the datalayers are not run. This allows
developers to dynamically determine when the Local Data should be
run, or re-run if a page is refreshed (in this case, a @Request
token can be used in the formula in the Condition attribute).
Local Data datalayers are *not* re-run with all AJAX refresh
requests. They are only re-run when the element being refreshed, using
Action.Refresh Element, contains either a DataLayer.Linked element linked
to the Local Data datalayer, or when it contains an @Local token.
Because @Local tokens can be used *anywhere*, they can be used in
many attributes to control element behavior. Here's an example of Local
Data in action:

![](https://devnet.logianalytics.com/hc/article_attachments/4417592006167/localdata_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417584221719/localdata_02a.png)

In the example above, Local Data is used to get lookup information about a
user. Later in the report definition, that data is used to determine which
Division to display.
More information about datalayers and data retrieval is available in
[Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406817655319-Datalayers).
