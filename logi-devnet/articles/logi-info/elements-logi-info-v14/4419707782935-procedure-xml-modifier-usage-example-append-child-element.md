---
title: "Procedure.XML Modifier - Usage Example: Append Child Element"
id: 4419707782935
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707782935-Procedure-XML-Modifier-Usage-Example-Append-Child-Element
updated_at: 2022-07-17T01:40:06Z
---

# Procedure.XML Modifier - Usage Example: Append Child Element

# Procedure.XML Modifier - Usage Example: Append Child Element

This example demonstrates appending a child XML element: we'll update a report definition to add a new column to a Data Table.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707022871/xmlmod_05.png)

As shown above, our report definition has a Data Table ("dtOrders") and it currently has two columns.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707023127/xmlmod_06.png)

And now we see the Process Task with **Procedure.XML Modifier** and **Append Child Element** elements above. The Procedure.XML Modifier element's Filename attribute has been set as shown in the previous example. Two methods of using the Append Child Element element's attributes to identify the target Logi Info element (the Data Table) are shown.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The XPath notation shown above will find the *first* Data Table in the definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707023383/xmlmod_07.png)

Next we need to manually enter or paste the source code for a Data Table Column into the New Element element, as shown above. Select the element and use the Source tab at the bottom of the editor in Studio to see its source code. Enter or paste your code as shown. If you only see a <NewElement /> tag, you'll also need to edit it into two tags, as highlighted in yellow above.
Where can you get the source code to paste into the NewElement tag? You can select any element in Studio and copy it, then paste it into any text editor (or Studio's Source tab) and you'll get its complete XML source code, including its child elements. For example, you can select and copy one of the existing Data Table Column elements in the report definition, paste its code, and then edit it as needed.

In Studio, you can also find the XPath of an element in a report or template by right-clicking on the element and selecting **Copy XPath**:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714731671/copy_xpath1_442x435.png)

Selecting this option will copy the direct XPath of that element, the tag name, and ID attribute (if available) to the Clipboard, which can then be copied into a TMF.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707023895/xmlmod_08.png)

When you switch back to the Definition tab in Studio, you'll see the added Logi elements appear beneath the New Element element, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699864215/xmlmod_09.png)

If we were updating an XML *data* file, instead of a report definition, the resulting elements would look something like the above in Studio.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714875031/xmlmod_10.png)

After the task runs, we can refresh the report definition in Studio, we can see that it's been updated to include the new Data Table column.
