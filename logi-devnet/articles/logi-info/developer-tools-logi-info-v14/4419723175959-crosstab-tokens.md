---
title: "@Crosstab Tokens"
id: 4419723175959
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723175959--Crosstab-Tokens
updated_at: 2022-07-17T02:06:11Z
---

# @Crosstab Tokens

# @Crosstab Tokens

These tokens provide access to values within a Crosstab Table or Crosstab-filtered chart:

| Token | Resolves To |
| --- | --- |
| @Chart.rdCrosstabColumn-*n~* | A datalayer column value, in a crosstab chart, where *n* equals the index, beginning with 1, of the column. |
| @Chart.rdStackedChartPercentage~ | A stacked chart percentage value in a crosstab chart. |
| @Data.rdCrosstabColumn~ | The crosstab column header value. |
| @Data.rdCrosstabValue-*n*-ExtraValueCol~ | The Extra Crosstab Value Column value, where *n* equals the index, beginning with 1, of the column. |
| @Data.rdCrosstabValue~ | The crosstab row value. |
| @Data.rdCrosstabValCount~ | The number of rows that were used to calculate a crosstab row value. |
