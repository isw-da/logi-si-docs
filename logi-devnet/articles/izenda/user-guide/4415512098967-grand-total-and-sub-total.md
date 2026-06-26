---
title: "Grand Total and Sub Total"
id: 4415512098967
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512098967-Grand-Total-and-Sub-Total
updated_at: 2021-12-10T03:10:31Z
---

# Grand Total and Sub Total

# Grand Total and Sub Total

## Grand Total

In report tables, the Grand Total for a field will provide either the sum (average, maximum, minimun) of all values or count (count distinct) values within that field across the entire data source.

For example, in a report for Northwind database’s Orders table, the Grand Total for Freight field will tell the sum of all Freight costs until now.

> [![../_images/GrandTotal_For_Freight_Preview.png](https://devnet.logianalytics.com/hc/article_attachments/4415504414615/grandtotal_for_freight_preview.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504414615/grandtotal_for_freight_preview.png)
>
> [![../_images/Grand_Total_Setting_For_Freight.png](https://devnet.logianalytics.com/hc/article_attachments/4415492501527/grand_total_setting_for_freight_908x675.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504414999/grand_total_setting_for_freight.png)

### List of Grand Total Functions

| Function | Description |
| --- | --- |
| Expression | User can combine the expression to collect data by using functions, operators and field names. |
| Average | Return the avarage of all values within the field that set grand total across the entire data source. |
| Count | Return the quantity of all values within the field that set grand total across the entire data source. |
| Count Distinct | Return the count unique number of all values within the field that set grand total across the entire data source. |
| Maximun | Return the maximun value of the field that set grand total across the entire data source. |
| Minimun | Return the minimum value of the field that set grand total across the entire data source. |
| Sum | Return the sum of all values within the field that set grand total across the entire data source. |
| Count Distinct | Return the sum unique number of all values within the field that set grand total across the entire data source. |

## Sub Total

In report tables, the Sub Total for a field will provide either the sum (average, maximum, minimun) of all values or count (count distinct) values within that field for each seperated group without having any sub-report.

For example, in a report for Northwind database’s Orders table, to have the sum for all Freight costs to each country without having to create additional reports, Sub Total can be used.

> [![../_images/Sub_Total_Freight_Preview.png](https://devnet.logianalytics.com/hc/article_attachments/4415511761431/sub_total_freight_preview_1008x509.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492501911/sub_total_freight_preview.png)
>
> [![../_images/Sub_Total_Freight_Setting.png](https://devnet.logianalytics.com/hc/article_attachments/4415511761943/sub_total_freight_setting_904x659.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511761687/sub_total_freight_setting.png)

### List of Sub Total Functions

| Function | Description |
| --- | --- |
| Expression | User can combine the expression to collect data for each group by using functions, operators and field names. |
| Average | Return the avarage of all values within the field that set Sub Total across the entire group. |
| Count | Return the quantity of all values within the field that set Sub Total across the entire group. |
| Count Distinct | Return the count unique number of all values within the field that set Sub Total across the entire group. |
| Maximun | Return the maximun value of the field that set Sub Total across the entire group. |
| Minimun | Return the minimum value of the field that set Sub Total across the entire group. |
| Sum | Return the sum of all values within the field that set Sub Total across the entire group. |
| Sum Distinct | Return the sum unique number of all values within the field that set Sub Total across the entire group. |
