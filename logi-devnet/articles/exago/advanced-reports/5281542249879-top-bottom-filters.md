---
title: "Top/Bottom Filters"
id: 5281542249879
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281542249879-Top-Bottom-Filters
updated_at: 2022-05-03T22:09:18Z
---

# Top/Bottom Filters

# Top/Bottom Filters

**Top/Bottom filters** also known as **Top N filters** allow filtering data to the rows with the top or bottom values, for either data fields or data summaries, per group iteration.

Top/Bottom filters work after all other filters have been applied. If a **Standard** or **Group Min/Max** filter has narrowed down a data field, a Top/Bottom filter will work on the remaining values.

![96YsCqvWQG.png](https://devnet.logianalytics.com/hc/article_attachments/5432321867927/96yscqvwqg.png)

Top/Bottom tab of the Filters dialog

To show only the top or bottom values, for either data fields or data summaries:

1. Open the **Filters** dialog then, click the **Top/Bottom** tab. To open the dialog:
   * *(v2021.1+)* Click the **Filters** ![funnel](https://devnet.logianalytics.com/hc/article_attachments/5432253309335/filtermenu.png) icon on the toolbar
   * *(pre-v2021.1)* From the **Settings** menu, click **Filters**.
2. Check the **Limit the report to the top/bottom values** checkbox.
3. From the **Top/Bottom** dropdown select either *Top* to show the largest or latest values or *Bottom* to show the smallest or earliest values.
4. Choose which values will be displayed, either:
   * check the **All** checkbox to sort all of the section values by the Top N criteria
   * enter an integer into the **#** text box to specify the desired number of values (for example enter *2* to see the top 2 or bottom 2 values). This field is only available when **All** is unchecked.
5. Select the data field or group field to filter from the **Value** dropdown.
6. Choose the **Direction** that the results should be sorted:
   * *Ascending* — items will be sorted from least to greatest
   * *Descending* — items will be sorted from greatest to least
   * *None* — items will be sorted in the original report sort order

To optionally filter the top/bottom values of each sorted group on a report, called a **For Each Group**:

7. Click the ![AddBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432278803479/addbtn.png)**Add Group** button.
8. Select one of the sorted groups on the report to group by from the dropdown list. You may also type into the dropdown list to search for the name of a field.
9. Click **Okay**.

To remove a **For Each Group**, click the **Delete Dropdown ![DropdownDelete.png](https://devnet.logianalytics.com/hc/article_attachments/5432223029015/dropdowndelete.png)** icon.

To remove a **Top N Filter**, uncheck the **Limit the report to the top/bottom values** checkbox.

## Examples

### Top 3 Performing Salespeople

A report showing the name and sales revenue for the top three performing salespeople in an organization may look like this:

![snU51TJTAi.png](https://devnet.logianalytics.com/hc/article_attachments/5432397215895/snu51tjtai.png)

In the **Report Designer**, the report contains the Employee Name and an aggregate of all of their order revenues summed together. The detail rows are collapsed so they are not initially visible in the **Report Viewer** until they are expanded.

![DPKRZEia1T.png](https://devnet.logianalytics.com/hc/article_attachments/5432364881559/dpkrzeia1t.png)

To filter all of the employees to show only those with the highest three revenues, a **Top N Filter** is applied with the following properties:

![UHwecaCUYB.png](https://devnet.logianalytics.com/hc/article_attachments/5432321932823/uhwecacuyb.png)

Top N Filter dialog for Top 3 Performing Salespeople report

* **Top/Bottom** — set to *Top* to choose the largest values
* **All** — *unchecked*, enabling the **#** text box
* **#** — set to *3* which will filter out all employees except for the top *3*
* **Value** — set to the formula `=aggsum({OrderDetails.Revenue})` to set the criteria to the aggregate sum of each employee’s orders
* **Direction** — set to *Descending* so that the largest value appears first and then in descending order from the *Top*.

### Largest Donations per Donor

A report showing a fund raising goal may want to show the name of each donor, and the top two largest donations that each donor made to the cause may look like this:

![TFQO85xrrj.png](https://devnet.logianalytics.com/hc/article_attachments/5432321946391/tfqo85xrrj.png)

The report is sorted by the donor’s last name. Each donor may have made many contributions to the cause. In the **Report Designer**, the report looks like this:

![ifKHJMUihk.png](https://devnet.logianalytics.com/hc/article_attachments/5432394887575/ifkhjmuihk.png)

If a **Top N Filter** is added, only the top donations will be shown. To show the top two donations *for each* donor, a **Top N Filter** with a **For Each** group is added with the following properties:

![NFtaI4ceuM.png](https://devnet.logianalytics.com/hc/article_attachments/5432397366551/nftai4ceum.png)

Top N Filter dialog for Charitable Donations report

* **Top/Bottom** — set to *Top* to choose the largest donation values
* **All** — *unchecked*, enabling the **#** text box
* **#** — set to *2* which will filter out all donations except for the top *2*
* **Value** — set to *donations.Amount* to set the filtering criteria to the amount of each donation
* **Direction** — set to *Descending* so that the largest value appears first and then in descending order from the *Top*.
* **For Each** — appears because the ![AddBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432278803479/addbtn.png)**Add Group** button was clicked to add a For Each group. Set to *donors.Surname* to enable the Top N filter to be applied to each donor’s name.
