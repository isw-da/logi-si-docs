---
title: "Setting Default Values"
id: 4419708000791
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419708000791-Setting-Default-Values
updated_at: 2022-07-17T01:26:01Z
---

# Setting Default Values

# Setting Default Values

All of the user input elements, except Input File Upload, have a **Default Value** attribute, which lets you set the value that will be shown or selected when the page is first displayed.
Making the desired value appear or be initially selected can be as simple as entering that value into the attribute - "hard coding" what will appear each time the page appears. Note that in the case of the **Input check box**, **Input Select List** and **Input Radio Buttons** elements, this value must be the one passed to the next page (from the Value column) not the displayed text. Tokens can also be used in the **Default Value** attribute.
In a situation where the user enters data then submits the page, for example to a Process task, and then task calls the data input page again, it's common to want to *redisplay* the values the user entered. To do this, use @Request tokens in the **Default Value** attributes of your Input elements and ensure that the calling Process task sends the values as Request variables.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) This *cannot* be done by just setting the **Request Forwarding** attribute
for a **Target.Report** element to *True*; you must use
**Link Params** instead.
If you've used @Request tokens as described above, how can you get some default values to appear the very *first time* the page is displayed?

![](https://devnet.logianalytics.com/hc/article_attachments/4419715014295/workingui_17.png)

As shown above, the **Default Request Parameters** element can provide Request variables, for use as your *default values*, when none are actually passed in the query string. The parameter and its value are created as shown above.
Then the **Default Value** attribute of the first **Input Text** element is set to @Request.defaultSize~. This ensures that a value ("Regular") will appear in the Input element when the page is first loaded. If the query string that calls this page includes a Request variable of the same name, the Default Request Parameters value is
ignored.
There's another option for populating the default values in an **Input Select List** element. The **Default Values** element, added as a child of the Input Select List, allows you to provide multiple default values when the Input Select List's **Multiple Selections** attribute is set to *True*. The default values are retrieved by a child datalayer beneath the Default Values element. If a Default Values element is present, then the Input Select
List's Default Value attribute is ignored.
