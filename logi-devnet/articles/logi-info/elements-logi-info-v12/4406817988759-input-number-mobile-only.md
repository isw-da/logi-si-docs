---
title: "Input Number (Mobile Only)"
id: 4406817988759
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817988759-Input-Number-Mobile-Only
updated_at: 2022-04-06T06:09:28Z
---

# Input Number (Mobile Only)

# Input Number (Mobile Only)

Available only in Logi Info **Mobile Report** definitions, this element allows the entry of a number and may trigger a special data entry control in the mobile device interface. Otherwise, it's similar to the Input Text element and numbers can be typed right into it.

![](https://devnet.logianalytics.com/hc/article_attachments/5263067782167/introui_07.png)

## Using It

This element's attributes are the same as those of the Input Text element.

This element can be used by itself or within an **Input Grid** element to make alignment with other Input elements easier, and a special element, **Validation.Numeric**, is available to ensure that valid numeric values are entered by the user.

## Getting Its Data

The data entered into this element will be available in the next Report or Process task by using an @Request token. For example, if the element's **ID** is set to *inpQuantity*, then its data will be available as the token @Request.inpQuantity~.

## More Information

For additional information, see the Element Reference entry for [Input Number](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2328&iName=InputNumber&iType=Element&iLabel=Input+Number&lnkpg=0).
