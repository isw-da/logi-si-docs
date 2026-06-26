---
title: "Input Telephone (Mobile Only)"
id: 4406822578071
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822578071-Input-Telephone-Mobile-Only
updated_at: 2022-04-06T06:09:30Z
---

# Input Telephone (Mobile Only)

# Input Telephone (Mobile Only)

Available only in Logi Info **Mobile Report** definitions, this element allows the entry of a telephone number and may trigger a special data entry control in the mobile device interface. Otherwise, it's similar to the Input Text element and numbers can be typed right into it.

![](https://devnet.logianalytics.com/hc/article_attachments/5263058994071/introui_08.png)

## Using It

This element's attributes are the same as those of the Input Text element. This element can be used by itself or within an **Input Grid** element to make alignment with other Input elements easier.

## Getting Its Data

The data entered into this element will be available in the next Report or Process task by using an @Request token. For example, if the element's **ID** is set to *inpCellNo*, then its data will be available as the token @Request.inpCellNo~.

## More Information

For additional information, see the Element Reference entry for [Input Telephone](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2343&iName=InputTelephone&iType=Element&iLabel=Input+Telephone&lnkpg=0).
