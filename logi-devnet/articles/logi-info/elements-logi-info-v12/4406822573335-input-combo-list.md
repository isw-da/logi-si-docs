---
title: "Input Combo List"
id: 4406822573335
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822573335-Input-Combo-List
updated_at: 2022-04-06T06:09:26Z
---

# Input Combo List

# Input Combo List

The Input Combo List element combines features of the Input Text, Input Select List, and AutoComplete elements.

![](https://devnet.logianalytics.com/hc/article_attachments/5263106869783/introui_18a.png)

This user Input element operates using **collections of data** and requires a datalayer to provide that data.

## Using It

Users can select values from a drop-down list by clicking the down arrow to show the list, then clicking an item in the list. Or they can start typing a value into the text box and the list will appear, dynamically filtering itself as more characters are typed.

If its **Multiple Selections** attribute is set to *True*, then users can select or enter multiple items, building a comma-separated list of values. As values are added to this list, they're remove from the drop-down list. These are the values that will be passed to the next Report or Process task.

Like other "list" elements, this one requires a datalayer to provide the list items and its **Combo List Column** attribute specifies the datalayer column that contains the values to be displayed in the drop-down list.

When blank values are part of the data set, they will be included in the drop-down list.

If you don't specify a width (Input Size attribute) the control will automatically size itself to accommodate the widest value, plus the down arrow icon.

The element has many of the attributes common to all Input elements and also these additional attributes:

| Attribute | Description |
| --- | --- |
| Combo List Column | (Required) Specifies the name of the datalayer column that contains the text to be displayed in the drop-down list. |
| Multiple Selections | Specifies whether users can select or enter multiple items from the drop-down list. If set to *True*, users can select or enter multiple items, building a comma-separated list of values. As values are added to this list, they're remove from the drop-down list, and the values list will be passed to the next Report or Process task. |
| Tooltip Column | Specifies the name of an column in the datalayer that contains explanatory text to be displayed as a tooltip unique to each list item. |

## Getting Its Data

Like an Input Text element, the value entered into or selected in this element will be available to the next Report or Process task as an @Request token. For example, if the element's ID is set to *inpCountry*, then its data will be available as the token @Request.inpCountry~. If no values is entered into the text box and the page is submitted, then its @Request token will equal an empty string ("").

If the element's Multiple Selections attribute is set to *True*, the @Request token will contain a **comma-separated list** of the selected or entered values. For use with SQL statements, it may be desirable to surround each individual value in this list with single quotes. This can be done using the SingleQuote token modifier. Thus

@Request.inpCountry~ which has a value of Australia,Sweden becomes   
@SingleQuote.Request.inpCountry~ which has a value of 'Australia','Sweden'

Default values for an Input Combo List element can be provided using its **Default Values** attribute, which can be a comma-separated list.

## More Information

For additional information, see the Element Reference entry for [Input Combo List](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=3216&iName=InputComboList&iType=Element&iLabel=Input+Combo+List&lnkpg=0).
