---
title: "Using the Add Data Columns Wizard"
id: 4406822234903
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822234903-Using-the-Add-Data-Columns-Wizard
updated_at: 2022-04-06T06:05:00Z
---

# Using the Add Data Columns Wizard

# Using the Add Data Columns Wizard

You can add columns beneath a data table manually in Logi Studio using the Element Toolbox or context menus, but Studio also provides a convenient wizard for adding them. This wizard is especially useful if you're not sure of the exact number or spelling of column names in the table's datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) You must have correctly configured Connection (if required) and Datalayer elements in your definition before you can use this wizard.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575784599/dtcols_01_401x309.png)

Select and right-click a Data Table element, as shown above, and use the context menus shown to launch the **Add Data Columns** wizard.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563402775/dtcols_02_452x348.png)

The wizard will run the datalayer and present a list of the columns returned in the datalayer, as shown above. You can then select the columns you want added to the definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563403031/dtcols_03.png)

The wizard will insert elements for the selected columns, including a **Data Table Column**, **Label**, and **Sort** element for each column, into the report definition, as shown above. The elements are configured generically for immediate use but, at a minimum, you'll probably want to adjust the Data Table Column elements' **Column Header** attributes.
