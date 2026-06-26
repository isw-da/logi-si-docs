---
title: "Adding Live Data "
id: 4419722867479
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722867479-Adding-Live-Data
updated_at: 2023-03-03T01:16:53Z
---

# Adding Live Data 

# Adding Live Data

There are multiple techniques available in Logi Info for displaying
data; in our example, we're displaying it as text in a tabular format.
We'll also see how we can display it in an
alternate"form-style" format.

![](https://devnet.logianalytics.com/hc/article_attachments/7522845259927/designrpt_07.png)

Like the previous containers, this one uses a Division element. However,
it includes a **Data Table** within the container and, as you'll see
later, some of its Data Table Columns can be containers themselves.

![](https://devnet.logianalytics.com/hc/article_attachments/7522842499607/designrpt_08.png)

The elements for the third division and the Data Table are shown above.
The Division element has another useful characteristic that makes it a
good choice as a container for Data Tables and charts: it can be
*refreshed* using an AJAX call. This is usually done with an Action.Refresh Element, and when the action occurs, *only* the Division's contents
will be refreshed, not the entire page. This is usually faster than a full
page refresh, and cleaner - the user doesn't see the entire page
"blink". For more information about Action.Refresh Elements, see [Action Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419723001367-Action-Elements).

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Division elements also include "HTML Attribute Params", enabling you to apply your application to work with other frameworks or libraries easier. With the HTML Attribute Params, you have the option to include "style" parameters. If an attribute was set in both Element and HTML attribute params, the one set in the HTML attribute params will be ignored.

## Presenting Data in a Form

Suppose you want to display the data from just *one* record at a
time, in which case embedding a Data Table in your container may be
overkill. You'd like to display it in a traditional form-style
arrangement, like this:

![](https://devnet.logianalytics.com/hc/article_attachments/7522815013655/designrpt_09.png)

This can be done by using just *one* Data Table column, as a
container, and putting an HTML table inside it.

![](https://devnet.logianalytics.com/hc/article_attachments/7522829826967/designrpt_10.png)

The necessary elements are shown above. It takes a bit of work to get all
the elements configured but Studio's element "copy
andpaste" feature helps a lot. An HTML table is used so that
captions and data can be formatted into justified columns, and it's
located beneath a Data Table column so that it will be "in
scope" for the datalayer and have access to the data as @Data tokens.

There is another way to use an HTML table to display data in a form,
*without* it being contained by a Data Table column. This is
accomplished by using a Local Data
element at the top of the definition; it's particularly well-suited for
this purpose because it will only retrieve one record of data and its
datalayer's scope is the entire report. So, if your data query is going to
retrieve just one record, you can use @Local tokens to access the
retrieved data *anywhere* in the report, freeing you to put your HTML
table wherever you'd like.
For more information, see [Using Local Data](https://devnet.logianalytics.com/hc/en-us/articles/4419707708183-Using-Local-Data).
