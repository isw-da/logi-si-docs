---
title: "List of Special XML Tags"
id: 4419715481879
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715481879-List-of-Special-XML-Tags
updated_at: 2022-07-17T01:37:29Z
---

# List of Special XML Tags

# List of Special XML Tags

Here's a complete list of the special XML tags available for use in TMFs:

| XML Tag | Description |
| --- | --- |
| AppendChildElement | Appends new child element as the *last* element beneath the element identified in its XML "ID" or "XPath" attribute. See the Using the <NewElement> Tag section in [Inserting and Removing Underlying Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419715480599-Inserting-and-Removing-Underlying-Elements). |
| CutElement | Used as a child of the Insert tags, this tag deletes the element identified by its XML "ID" or "XPath" attribute and makes it available for insertion. Used primarily to "move" elements within the definition. |
| CycleAttributeValues | Used primarily with Themes, allows assignment of values to elements such as charts that have multiple layers. Elements to be modified are identified in its XML "CycleOnChildElement" attribute; uses child tag CycleValue. |
| CycleValue | Used to provide values for CycleAttributeValues tag. |
| InsertAfterElement | Inserts new element *after* the element identified in its XML "ID" or "XPath" attribute. See the Using the <NewElement> Tag section in [Inserting and Removing Underlying Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419715480599-Inserting-and-Removing-Underlying-Elements). |
| InsertBeforeElement | Inserts new element *before* the element identified in its XML "ID" or "XPath" attribute. See the Using the <NewElement> Tag section in [Inserting and Removing Underlying Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419715480599-Inserting-and-Removing-Underlying-Elements). |
| PrependChildElement | Adds new child element as the *first* element beneath the element identified in its XML "ID" or "XPath" attribute. See the Using the <NewElement> Tag section in [Inserting and Removing Underlying Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419715480599-Inserting-and-Removing-Underlying-Elements). |
| Remark | "Comments" the XML tag it encloses, so the tag has no effect. |
| RemoveAttribute | Removes the attribute identified using its element XML "ID" or "XPath" and "AttributeName" attributes. |
| RemoveElement | Removes the element identified in its XML "ID" or "XPath" attribute. |
| SetAttribute | Sets the attribute value identified for the element identified in its XML "ID" or "XPath" attribute, overwriting any value already there. |
| SetAttributeWhenEmpty | Sets the attribute value identified for the element identified in its XML "ID" or "XPath" attribute, but only if that attribute does not have a value already. |
| SetAttributeWithInsert | Inserts an additional attribute value *before* any existing value identified for the element identified in its XML "ID" or "XPath" attribute. This order is important, as it allows existing values related to CSS to "win" any conflicts by being last in the order. |
| UpdateOrAppendChildElement | If the child element does not exist, appends it as the *last* element beneath the element identified in its XML "ID" or "XPath" attribute. If the child element exists, updates its attributes. See the Using the <NewElement> Tag section in [Inserting and Removing Underlying Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419715480599-Inserting-and-Removing-Underlying-Elements). |
