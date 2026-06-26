---
title: "DataLayer.Static - Working with DataLayer.Static"
id: 4406817332887
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817332887-DataLayer-Static-Working-with-DataLayer-Static
updated_at: 2022-04-06T06:05:27Z
---

# DataLayer.Static - Working with DataLayer.Static

# DataLayer.Static - Working with DataLayer.Static

In order to actually create the data, developers must add one or more **Static Data Row** elements beneath a DataLayer.Static element. Each Static Data Row element represents a *single row* of data in the datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563376279/dlstatic_01.png)

![](https://devnet.logianalytics.com/hc/article_attachments/4417584016535/dlstatic_02.png)

As shown above, **Static Data Row** elements have dynamic attributes, which the developer creates. Each attribute represents a *column* in the data row; the attribute name assigned by the developer becomes the column name and the value entered becomes the column data. Naturally, if multiple Static Data Row elements are being added, they all need to have the same number of attributes, with identical names.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584016663/dlstatic_03.png)

Dynamic attributes are **added** by entering the attribute name in the input box at the top of the Attributes Panel, as shown above, and clicking the "**+**" icon. Values are then added by entering them in the usual fashion. An attribute and its value, if any, are **deleted** by selecting it and clicking the red "**-**" icon.

Dynamic attribute names can be **edited** by selecting them and
clicking the "Pencil" icon. This will place the name into the top text box,
where it can be edited. The icon will change to a "Diskette" icon and clicking
it again will save the edited attribute name. Attribute values can be edited
directly, as usual, by placing the cursor on them

![](https://devnet.logianalytics.com/hc/article_attachments/4417563376535/dlstatic_04.png)

If an attribute named "ID" is created, as shown above, its value will replace the words "Static Data Row" next to the element icon in the Element Tree. This may be more desirable than a big stack of anonymous Static Data Row elements, as it allows developers to visually identify each static data row element separately in the tree.

Developers can retrieve the values from each column in the datalayer by using the @Data token.

Data in a DataLayer.Static can be manipulated with all of the usual child elements, such as **Sort Filter**, and can be joined using the **Join** element to other datalayers.
