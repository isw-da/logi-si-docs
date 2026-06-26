---
title: "Conditional Row Suppression"
id: 5281542083095
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281542083095-Conditional-Row-Suppression
updated_at: 2022-05-03T22:09:21Z
---

# Conditional Row Suppression

# Conditional Row Suppression

Use **Conditional Row Suppression** to hide rows of data that meet a predefined condition. This might be useful when certain fields do not apply to all records.

## Address Example

This displays contact information for company employees residing in the UK and USA. The `Employees.Region` field stores State values for USA residents and null value for UK residents.

When building an Employee Directory report, the formula below might be used for the “Address” column to joining together each individual component of the employee’s address.

```
={Employees.Address} & ", " & {Employees.City} & ", " & {Employees.Region} & ", " & {Employees.PostalCode}
```

Here’s how this data is returned without the use of row suppression. Note that `Employees.Region` doesn’t return any information for *Buchanan, Steven* or *Dodsworth, Anne* but is necessary to show the State for *Callahan, Laura* and *Fuller, Andrew*.

![nWRJpbmtwG.png](https://devnet.logianalytics.com/hc/article_attachments/5432414249111/nwrjpbmtwg.png)

Conditional Row Suppression can be used in conjunction with another detail row to format the Address column on the report as appropriate for each employee’s country of residence.

1. Add another Detail row to the report and copy all of the formulas from the first one to the second. ![YWiuIW4bq9.png](https://devnet.logianalytics.com/hc/article_attachments/5432414292375/ywiuiw4bq9.png)
2. Modify the formula for the second row’s Address column to replace `{Employees.Region}` with `{Employees.Country}`. ![qCvFBc4TrV.png](https://devnet.logianalytics.com/hc/article_attachments/5432322534551/qcvfbc4trv.png)
3. Select the first cell on the top detail row, and then click the **Format Cell**![FormatCells.png](https://devnet.logianalytics.com/hc/article_attachments/5432243560855/formatcells.png) icon on the toolbar.
4. Switch to the **Conditional** tab of the Cell Formatting dialog.
5. Click the ![Add2.png](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Add** button at the bottom of the dialog to add a new condition.
6. For the **Action**, choose *Suppress Row* from the dropdown. ![iWM2Q8KNUW.png](https://devnet.logianalytics.com/hc/article_attachments/5432365947159/iwm2q8knuw.png)
7. Click the **Formula Editor**![Formula.png](https://devnet.logianalytics.com/hc/article_attachments/5432247626647/formula.png) icon to open the Formula Editor and enter this formula: `Not({Employees.Country} = "USA")`![oQiKvA83oa.png](https://devnet.logianalytics.com/hc/article_attachments/5432414405143/oqikva83oa.png)
8. Click **Okay** to close the Formula Editor and again to close the Cell Formatting dialog.
9. Select the first cell of the second detail row, and repeat steps 3–8 for the second row. At step 7, enter this formula: `{Employees.Country} = "USA"`

Now, whenever the employee’s country is not the USA, the first row will be hidden and the second will be displayed. When the employee’s country is the USA, the second row is hidden and the first one will be used. When this report is executed or reported, the output will now look this, with the correct fields:

![7dvCkSG97o.png](https://devnet.logianalytics.com/hc/article_attachments/5432365988631/7dvcksg97o.png)

Notice for the employees living in the UK, the name of the country replaces a null value. For employees living in the USA, their state of residence appears.
