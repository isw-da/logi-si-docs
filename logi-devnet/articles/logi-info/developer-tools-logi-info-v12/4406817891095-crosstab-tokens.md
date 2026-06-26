---
title: "@Crosstab Tokens"
id: 4406817891095
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817891095--Crosstab-Tokens
updated_at: 2022-04-06T06:08:54Z
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
