---
title: "DataLayer.Static"
id: 1500009514762
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514762-DataLayer-Static
updated_at: 2021-06-17T01:58:14Z
---

# DataLayer.Static

# DataLayer.Static

The **DataLayer.Static** element gives developers the ability to "hard-code" data rows directly into the report definition. The data provided in the manner is **fixed** and cannot be changed programmatically.

* Attributes
* [Working with DataLayer.Static](#Working)
* [Using Studio's DataLayer Wizard](#Wizard)

## Attributes

The **DataLayer.Static** element has **no attributes** other than an **ID**. If this datalayer will be linked with another, be sure to provide a *unique* ID for it.

## Working with DataLayer.Static

In order to actually create the data, developers must add one or more **Static Data Row** elements beneath a DataLayer.Static element. Each Static Data Row element represents a *single row* of data in the datalayer.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778689047/dlstatic_01.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771852951/dlstatic_01a.gif)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771853207/dlstatic_02_300x182.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771853463/dlstatic_02a.gif)

As shown above, **Static Data Row** elements have dynamic attributes, which the developer creates. Each attribute represents a *column* in the data row; the attribute name assigned by the developer becomes the column name and the value entered becomes the column data. Naturally, if multiple Static Data Row elements are being added, they all need to have the same number of attributes, with identical names.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771853719/dlstatic_03.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771853975/dlstatic_03a.gif)

Dynamic attributes are **added** by entering the attribute name in the input box at the top of the Attributes Panel, as shown above, and clicking the "+" icon. Values are then added by entering them in the usual fashion. An attribute and its value, if any, are **deleted** by selecting it and clicking the red "-" icon.

As of v10.0.189, dynamic attribute names can be **edited** by selecting them and
clicking the "Pencil" icon. This will place the name into the top text box,
where it can be edited. The icon will change to a "Diskette" icon and clicking
it again will save the edited attribute name. Attribute values can be edited
directly, as usual, by placing the cursor on them

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771854231/dlstatic_04.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771854487/dlstatic_04a.gif)

If an attribute named *ID* is created, its value will replace the words "Static Data Row" next to the element icon in the element tree. This may be more desirable than a big stack of anonymous Static Data Row elements, as it allows developers to visually identify each static data row element separately in the tree.

Developers can **retrieve** the values from each column in the datalayer by using the @Data token.

## Using Studio's DataLayer Wizard

Beginning in v10.0.299, Studio includes a wizard that assists you in configuring DataLayer.Static and creating static data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771854743/dlstatic_05.png)

As shown above, the wizard can be started by selecting and then right-clicking the parent element under which you want to add the datalayer, and using the context menus to select "Add a Static DataLayer."

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778689303/dlstatic_06.png)

The wizard opens, as shown above. Use the wizard as follows:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778689559/dlstatic_07.png)

1. Right-click the column headers, one-by-one, select **Rename Column** from the pop-up menu, and change the column names to names appropriate for your purpose. You can drag the column header borders to widen the columns, if desired. Add or delete columns as necessary, until you have just those you need.  
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771854999/dlstatic_08.png)
2. Click the first column and enter the desired data. Press **Tab** to move to the next column and enter its data, then repeat for all columns. *Do not press Enter*!  
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778689815/dlstatic_09.png)
3. Right-click the blank square to the left of the first column and select **New Row** from the pop-up menu that appears. Repeat Steps 2 and 3 as many times as necessary to enter data for all static rows.  
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771855255/dlstatic_10.png)
4. When the data for all rows and columns has been entered, click **Next** to insert the elements.  
     
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771855511/dlstatic_11.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778690583/dlstatic_11a.png)
5. The wizard will insert the elements, as shown above, and set their attributes appropriately. Click **Finish** to close the wizard.
