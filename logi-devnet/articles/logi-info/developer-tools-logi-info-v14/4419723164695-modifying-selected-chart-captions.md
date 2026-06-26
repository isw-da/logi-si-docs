---
title: "Modifying Selected Chart Captions"
id: 4419723164695
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723164695-Modifying-Selected-Chart-Captions
updated_at: 2022-07-17T01:37:31Z
---

# Modifying Selected Chart Captions

# Modifying Selected Chart Captions

When you create charts using the **Analysis Chart** or **Analysis Grid** super-elements, the chart caption is created automatically and appears in a format similar to:

Sum of OrderID by OrderDate

You may wish to translate this caption and/or reorder its parts, and this can be done using a TMF. Here's an example of the relevant code in the Analysis Chart template file (rdTemplate/rdAnalysisChart/rdAcTemplate.lgx):

<ChartCanvas **ChartCaption**="{AggrName} of {DataColumnName} by {LabelColumnName}"**CaptionDated**="{AggrName} of {DataColumnName} by {LabelColumnName}" ChartHeight="300" ChartWidth="500" BorderColor="#7A7A7A" BorderRadius="4" ID="ChartPie" rdUnderSuperElement="True">

Note the construction of the default **ChartCaption** and **CaptionDated** attribute values, highlighted above. The items within the curly braces are internal chart variables and, using a TMF, you can substitute a different value that includes them, as follows:

<SetAttribute XPath="//ChartCanvas" ChartCaption="{AggrName} de {DataColumnName} par {LabelColumnName}" />

The example TMF code shown above translates the English connecting words "of" and "by" to their French equivalents. You can change the value in any way you desire, using the { } chart variables or removing them altogether.

<SetAttribute XPath="//ChartCanvas" ChartCaption="{DataColumnName} by {LabelColumnName}: {AggrName}" />

You can also rearrange the value parts, as shown above. The resulting caption would appear as "OrderID by OrderDate: Sum".
