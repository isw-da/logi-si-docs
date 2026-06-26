---
title: "Using AutoComplete"
id: 4406822665879
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822665879-Using-AutoComplete
updated_at: 2022-04-06T06:10:33Z
---

# Using AutoComplete

# Using AutoComplete

The **AutoComplete** element can be used to provide users with data-driven assistance when using Input Text and Input Email elements.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583592855/workingui_08.png)
As shown above, the AutoComplete element is added as a child of the Input element and has its own child datalayer; all datalayer types are supported.   

![](https://devnet.logianalytics.com/hc/article_attachments/4417575408791/workingui_09.png)

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) When the user begins typing into the Input element, a drop-down list of values, shown above, will appear. The list will consist of values from the datalayer column identified in the **Column Name** attribute. Items in the list will be progressively filtered with each letter typed, and can be selected at any time. Users can configure the number of characters that they want to generate the drop-down list of values by entering a value in the **Minimum Length** attribute, shown below. In this example, a search would not return any values until 2 characters are entered into the Auto-Column box. This feature helps to increase performance and make searches more efficient by returning a limited set of search results.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410455/minimum_length.png)

When the AutoComplete element's **Multiple Selections** attributes is set to *True*, the user may enter or select multiple text items, which will appear in the Input element separated by commas. Items that have already been added to the Input will be automatically filtered out of the remaining choices.
The default separator character for multiple selections is a comma. You may change this to another character by manually editing the element's XML source code, in Logi Studio's Source tab, to include an **InputValueDelimited** attribute and value. For example, this will set the delimiter to a semi-colon:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410711/workingui_09a.png)

The resulting @Request variable created when the page is submitted will contain an individual value, or if multiple items have been entered/selected, a comma-separated list of values. Trailing commas will be removed automatically. For more information on parsing comma-separated lists for SQL queries, see [Input Select List](https://devnet.logianalytics.com/hc/en-us/articles/4406817990935-Input-Select-List).
The AutoComplete element includes a **Tooltip Column** attribute. Enter the name of a data column here to display a unique tooltip value for each data item.
