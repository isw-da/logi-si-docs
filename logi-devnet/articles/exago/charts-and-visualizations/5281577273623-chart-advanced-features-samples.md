---
title: "Chart Advanced Features: Samples"
id: 5281577273623
section: "Charts and Visualizations"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281577273623-Chart-Advanced-Features-Samples
updated_at: 2022-05-03T22:09:14Z
---

# Chart Advanced Features: Samples

# Chart Advanced Features: Samples

The Advanced Features in the Chart Wizard allow for fine grain control over the chart and its components. Use the examples in this topic as inspiration when designing reports and charts.

## Area Charts

### Add a Bordering Line

An area chart displays its data by shading in the area below the curve. A border can be applied to this plot, and by selectively choosing the edges the border is applied a line appears.

![T73al1AC26.png](https://devnet.logianalytics.com/hc/article_attachments/5432387268119/t73al1ac26.png)

A basic area chart with no border applied

![3bPCuRiEOh.png](https://devnet.logianalytics.com/hc/article_attachments/5432342704279/3bpcurieoh.png)

The same area chart with a border applied along the top edge only. The divisional grid lines behind the chart have also been changed to solid

| Advanced Feature Name | Value |
| --- | --- |
| showPlotBorder | 1 |
| plotBorderColor | provide a hexadecimal HTML color code, or omit to use the first default chart color |
| plotBorderThickness | 4 |
| drawFullAreaBorder | 0 |
| divLineDashed | 0 |

## Bar and Column Charts

### Display a Background Image

This example utilizes a few advanced features to provide a partially transparent background image, and an additional feature to narrow the width of the columns.

![wgbYf14B9L.png](https://devnet.logianalytics.com/hc/article_attachments/5432342740503/wgbyf14b9l.png)

Basic column chart with the **Lilac** theme prior to applying the Advanced Features

![8YTVlcrTs3.png](https://devnet.logianalytics.com/hc/article_attachments/5432387410839/8ytvlcrts3.png)

A partially transparent background image applied to the chart canvas and the narrower columns activated with Advanced Features

| Advanced Feature Name | Value |
| --- | --- |
| bgImage | A URL in the same domain as Exago BI that points to the background image for example `http://192.168.168.129/butterfly.jpg` |
| bgImageAlpha | 40 |
| imageHAlign | middle |
| bgImageDisplayMode | stretch |
| maxColWidth | 14 |

## Pie Charts

### Show Values in Tooltips

By default, the tooltip on a pie chart shows the percentage of the series. With the `showPercentInToolTip` advanced feature, the underlying value can be displayed instead.

![xtcAlxyAAE.png](https://devnet.logianalytics.com/hc/article_attachments/5432333486871/xtcalxyaae.png)

Percentage shown in the tooltip before applying the advanced feature

![lf28P28tXl.png](https://devnet.logianalytics.com/hc/article_attachments/5432373740567/lf28p28txl.png)

Underlying value shown in the tooltip after applying the advanced feature

| Advanced Feature Name | Value |
| --- | --- |
| showPercentInToolTip | 0 |

# Radar Charts v2021.1+

## Outline Instead of Filled Data Plot

To show an outline instead of a filled in area representing the data, use a combination of four advanced features.

![VM91gWr7e8.png](https://devnet.logianalytics.com/hc/article_attachments/5432333540887/vm91gwr7e8.png)

The data plot is filled in before applying the advanced features

![gmdgoypzNG.png](https://devnet.logianalytics.com/hc/article_attachments/5432387599767/gmdgoypzng.png)

The data plot becomes outlines with no fill after applying the advanced features

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The **Theme** setting in the Chart Wizard will not apply when utilizing these features. `paletteColors` can be used to change the colors of the series instead.

| Advanced Feature Name | Value |
| --- | --- |
| plotFillAlpha | 0 |
| plotBorderAlpha | 100 |
| showPlotBorder | 1 |
| palletteColors | #3B5BD2,#4E80F4 optional — a comma separated list of hexadecimal HTML color codes |

## Spark Line Charts

### Remove Anchors and Values

A background color is also applied to this spark chart through its Other Features.

![ElU815hgdv.png](https://devnet.logianalytics.com/hc/article_attachments/5432387622295/elu815hgdv.png)

Standard Spark chart

![NRQ6CkFWOw.png](https://devnet.logianalytics.com/hc/article_attachments/5432342873879/nrq6ckfwow.png)

Spark chart with anchors and values removed

| Advanced Feature Name | Value |
| --- | --- |
| shopOpenAnchor | 0 |
| showCloseAnchor | 0 |
| showHighAnchor | 0 |
| showLowAnchor | 0 |
| showOpenValue | 0 |
| showCloseValue | 0 |
| showHighLowValue | 0 |
| lineThickness | 3 |
