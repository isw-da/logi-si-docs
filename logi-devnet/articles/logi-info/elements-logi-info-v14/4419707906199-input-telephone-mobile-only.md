---
title: "Input Telephone (Mobile Only)"
id: 4419707906199
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707906199-Input-Telephone-Mobile-Only
updated_at: 2022-07-17T02:23:07Z
---

# Input Telephone (Mobile Only)

# Input Telephone (Mobile Only)

Available only in Logi Info **Mobile Report** definitions, this element allows the entry of a telephone number and may trigger a special data entry control in the mobile device interface. Otherwise, it's similar to the Input Text element and numbers can be typed right into it.

![](https://devnet.logianalytics.com/hc/article_attachments/7522754182167/introui_08.png)

## Using It

This element's attributes are the same as those of the Input Text element. This element can be used by itself or within an **Input Grid** element to make alignment with other Input elements easier.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 Adding **HTML Attribute Params** to your User Input elements enables you to apply your application to work with other frameworks or libraries easier. Depending on the type of HTML Attribute Params you add, there will be different parameters available to use, or you can define your own parameters. If an attribute was set in both Element and HTML Attribute Params, the one set in the HTML Attribute Params will be ignored.

## Getting Its Data

The data entered into this element will be available in the next Report or Process task by using an @Request token. For example, if the element's **ID** is set to *inpCellNo*, then its data will be available as the token @Request.inpCellNo~.

## More Information

For additional information, see the Element Reference entry for [Input Telephone](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2343&iName=InputTelephone&iType=Element&iLabel=Input+Telephone&lnkpg=0).
