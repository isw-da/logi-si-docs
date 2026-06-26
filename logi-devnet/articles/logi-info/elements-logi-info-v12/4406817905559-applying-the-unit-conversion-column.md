---
title: "Applying the Unit Conversion Column"
id: 4406817905559
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817905559-Applying-the-Unit-Conversion-Column
updated_at: 2022-04-06T06:08:59Z
---

# Applying the Unit Conversion Column

# Applying the Unit Conversion Column

The following example illustrates how the **Unit Conversion Column** is used:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563077271/unitconv_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563077399/unitconv_02a.png)

All of the attributes mentioned below are required:

1. As shown above, a **Unit Conversion Column** element is added as a child to a datalayer element.
2. Its **Data Column** attribute value is set to the name of the column in that datalayer whose value will be converted.
3. The **Unit Type** attribute is set to the standard category name for the data units. It's important to do this *before* setting the other attributes.
4. The **From Unit**  attribute is set from the pull-down list of optionsto the unit of the data in the named Data Column.
5. The **ID** attribute sets the name of the new column that will be added to the datalayer, containing the converted value.
6. The **To Unit** attribute is set from the pull-down list of optionsto the unit of the data that will be output to the new column.
