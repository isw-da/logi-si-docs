---
title: "Sorting by Aggregates"
id: 5281542226711
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281542226711-Sorting-by-Aggregates
updated_at: 2022-05-03T22:09:18Z
---

# Sorting by Aggregates

# Sorting by Aggregates

---

To sort groups by the summary, or **aggregate**, calculation of each group of an Advanced Report, use **[Top/Bottom filters](https://devnet.logianalytics.com/hc/en-us/articles/5281542249879-Top-Bottom-Filters)**.

**Top/Bottom filters** look for the highest or lowest values in a set, and then put those values in order. Any arbitrary cell in the report can be the Top/Bottom filter.

To sort by a summary calculation:

1. Ensure that the report has the appropriate aggregate formula in a group footer or header (*v2019.2+*) cell. The cell should return a numeric value in the report output, which you want to sort the groups by.
2. Open the **Filters** dialog then, click the **Top/Bottom** tab. To open the dialog:
   * *(v2021.1+)* Click the **Filters** ![FilterMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432253309335/filtermenu.png) icon on the toolbar
   * *(pre-v2021.1)* From the **Settings ![report-settings-menu.png](https://devnet.logianalytics.com/hc/article_attachments/5432394966167/report-settings-menu.png)**menu, click **Filters**.
3. Check the **Limit the report to the top/bottom values** check box.
4. From the **Top/Bottom** list:
   * select **Bottom** to sort in ascending order, or
   * select **Top** to sort in descending order.
5. For versions *v2018.2+*: Check the **All** checkbox to sort all of the section values by the Top N criteria.
6. For versions *pre-v2019.1*: In the **#** field, enter `2147483647`. Why this number? We cannot enter ∞, so instead we want to enter an arbitrarily large number. This is the largest number that can fit without causing a report error.
7. From the **Value** list, select the group footer  or header (*v2019.2+*)cell with the aggregate formula.
8. If there is a **For Each** group, click the **Delete**![-](https://devnet.logianalytics.com/hc/article_attachments/5432223029015/dropdowndelete.png) icon to remove it.

Keep in mind that this is not a *Sort* from the sort menu. It cannot make nested groups. This only affects the order in which a group of data is shown in the output. Because this is technically a *Filter*, this has precedence over the report sorts.

![d3e4Le3Nym.png](https://devnet.logianalytics.com/hc/article_attachments/5432397463831/d3e4le3nym.png)

An Advanced Report that aggregates the revenue raised from donations in a fund raising campaign

![KyD5i3MrYW.png](https://devnet.logianalytics.com/hc/article_attachments/5432395124887/kyd5i3mryw.png)

The Filters dialog settings to sort by the aggregated revenue figure

![eAZnKyAL0U.png](https://devnet.logianalytics.com/hc/article_attachments/5432365053847/eaznkyal0u.png)

The same report now sorted by the aggregated campaign donation amounts
