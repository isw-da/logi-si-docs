---
title: "No Data Qualified Options"
id: 5281564494999
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281564494999-No-Data-Qualified-Options
updated_at: 2022-05-03T22:09:18Z
---

# No Data Qualified Options

# No Data Qualified Options

If the data source returns zero rows, the message below is automatically generated, and report execution will end.

![RrxSiRxb0b.png](https://devnet.logianalytics.com/hc/article_attachments/5432381701399/rrxsirxb0b.png)

**No Data Qualified** warning message

This condition is called **No Data Qualified** or **NDQ**. There are a number of ways to handle or prevent this situation:

* [Enabling filter dependency](#Enable) can prevent improper filter values from selecting no data rows
* [Allowing execution when NDQ](#Allowing) will allow report execution to continue, with the possibility to display a [custom error message](#Custom) in the report

## Enable Filter Dependencies

Enabling **Filter Dependencies** will prevent filters from being configured that would cause “No Data Qualified”.

For example, choosing *Beverages* as the Category and *Boston Crab Meat* as the Product Name would result in NDQ since there are no products named *Boston Crab Meat* in the *Beverages* Category. With **Allow Filter Dependencies** enabled Exago will only show Products that are in the Category selected.

![ACXZ44vh8g.png](https://devnet.logianalytics.com/hc/article_attachments/5432395313175/acxz44vh8g.png)

With Allow Filter Dependencies disabled, all products regardless of Category are available in the dropdown

![KaNWDg1IuQ.png](https://devnet.logianalytics.com/hc/article_attachments/5432397718039/kanwdg1iuq.png)

With Allow Filter Dependencies enabled, only those products in the Category previously selected in the dropdown are available

To enable filter dependency, the system administrator must:

1. Set **Admin Console** > **General Settings** > **Filter Settings** > **Allow Filter Dependencies** to *True.*

## Allowing Execution When No Data Qualified

A lesser known feature of this application is the ability to execute a report even if No Data is Qualified. This functionality is useful in situations where a user still wants to see the report or when a custom message is conditionally set for when no data is qualified. When using *Show Report* instead of *Show Message*, the only items that will appear in the report are those that aren’t connected to the data.

1. (*v2021.1+*) Click on the **Advanced**![Advanced.png](https://devnet.logianalytics.com/hc/article_attachments/5432397774999/advanced.png)![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png) menu on the toolbar, then choose **General Options**.
2. (*pre-v2021.1*) Click on the ![report-settings-menu.png](https://devnet.logianalytics.com/hc/article_attachments/5432394966167/report-settings-menu.png)**Report Settings** menu on the toolbar, hover over **Options** then choose **General**
3. Set **No Data Qualify Display Mode** to *Show Report*.
4. Click **Okay**.

![6pA70y7TK1.png](https://devnet.logianalytics.com/hc/article_attachments/5432322045207/6pa70y7tk1.png)

Choosing *Show Report* from **No Data Qualify Display Mode** in the Report General Options dialog

### Common Use Case

This functionality is commonly used when reports are being shown via a Dashboard and users want at least the title to appear, and/or display a custom message rather than the intrusion of an error message on the Dashboard.

## Custom Message Option

When using display mode *Show Report* it may be preferable to leave a custom message for the viewer upon execution. This can be done using Custom Formatting.

Using a built in function, Exago can conditionally suppress a cell to only show when the report has returned NDQ.

1. Select the cell you wish to show and then click the **Cell Format**![FormatCells.png](https://devnet.logianalytics.com/hc/article_attachments/5432243560855/formatcells.png) icon on the toolbar or right-click the cell and click **Format Cells**.  
   ![V4K9bmw1Pd.png](https://devnet.logianalytics.com/hc/article_attachments/5432365162519/v4k9bmw1pd.png)
2. Select the **Conditional** tab in the Cell Format dialog.
3. Click the ![Add.png](https://devnet.logianalytics.com/hc/article_attachments/5432239633943/add.png)**Add** button to add a condition.
   1. Set the **Action** to *Suppress Section* or *Suppress Row* based on how the custom message cell is setup.
   2. Click on the **Formula Editor** ![Formula.png](https://devnet.logianalytics.com/hc/article_attachments/5432247626647/formula.png) icon.

   ![KZU9FUvtsh.png](https://devnet.logianalytics.com/hc/article_attachments/5432408394775/kzu9fuvtsh.png)
4. Add the formula `IsNoDataQualified() = False()`  
   ![fIvnCDba7W.png](https://devnet.logianalytics.com/hc/article_attachments/5432381864087/fivncdba7w.png)
5. Click **Okay**.

Upon execution, all the elements that are not data as well as the conditional message should appear within the execution.

![shZgHdvq9o.png](https://devnet.logianalytics.com/hc/article_attachments/5432397977879/shzghdvq9o.png)

For more information about **Conditional Formatting**, refer to the [Advanced Reports: Cell Formatting](https://devnet.logianalytics.com/hc/en-us/articles/5281564235671-Cell-Formatting#Conditio) topic.
