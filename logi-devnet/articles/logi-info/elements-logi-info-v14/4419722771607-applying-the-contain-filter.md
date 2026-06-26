---
title: "Applying the Contain Filter"
id: 4419722771607
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722771607-Applying-the-Contain-Filter
updated_at: 2022-07-17T01:56:18Z
---

# Applying the Contain Filter

# Applying the Contain Filter

The following exampleillustrates how the **Contain Filter** is used:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714685079/containfilter_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419706702871/containfilter_01a.png)

1. As shown above, a **Contain Filter** element is added as a child to a datalayer element.
2. Its **Data Column** attribute value is set to the column in that datalayer whose value will be searched.
3. The **Search String** attribute is set to the text you're searching for in the data column.
4. The optional **Case Sensitive** attribute sets the case-sensitivity of the search. The default value is *True*, for a case-sensitive search. Setting it to *False* produces a case-insensitive search.
5. The optional **Contain Type** attribute is set to define the nature of the search. The default value is *Contains*, which means the data column value must contain the search string. The other values, *StartsWith* and *EndsWith*, let you make the search more selective about where the search string occurs in the column value: at its beginning or at its end.

In the example above, the sequence of events is that the datalayer reads in all the data from the XML data file, then the Contain Filter **removes** all rows that don't match the criteria (Description column value contains "spreads, and seasonings"). All that remains in the datalayer for use in the report are rows whose Description column value contains "spreads, and seasonings".
