---
title: "Summarizing Value Rows"
id: 4406822223895
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822223895-Summarizing-Value-Rows
updated_at: 2022-04-06T06:04:50Z
---

# Summarizing Value Rows

# Summarizing Value Rows

Our plan calls for adding three columns in the table that summarize row values ((horizontal summary). This is done by adding **Crosstab Row Summary Column** elements to the Crosstab Filter:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584059927/xtabtable_34.png)

The first of these elements refers to the original Value column defined in the Crosstab Filter attributes, *Quantity*, so all that is required is that the element be added beneath the filter, be given an ID, and its summarizing function be set to *Sum*, as shown above.

The second element of this type is summarizing an Extra Crosstab Value Column ("ODTotal") so it needs to include that elements's ID, as highlighted in yellow above, in the **Extra Crosstab Value Column ID** attribute.

Three **Crosstab Table Label Columns** are also added to display the summarized values. The first two reference their data using Label elements and standard tokens *@Data.crsSumQuantity~* and *@Data.crsSumODTotal~*. The third one divides the other two using the formula =@Data.crsSumODTotal~/@Data.crsSumQuantity~to derive its value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584060055/xtabtable_34a.png)

Referring to our layout model, the addition of the Crosstab Row Summary Column elements adds the columns highlighted in yellow above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563422359/xtabtable_35.png)

And, in a Preview, the table now looks like the image shown above.
