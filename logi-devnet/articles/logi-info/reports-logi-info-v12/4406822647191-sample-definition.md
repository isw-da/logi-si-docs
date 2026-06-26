---
title: "Sample Definition"
id: 4406822647191
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822647191-Sample-Definition
updated_at: 2022-04-06T06:10:21Z
---

# Sample Definition

# Sample Definition

The following sample widget definition has been included to get you started with your first Logi Widget.

1. Launch Logi Studio, create a new **Widget** definition file, and give it a new name.
2. Open the new file in the **Workspace** and click its **Source** tab at bottom of the panel.
3. Copy the text from this page to your clipboard and paste it into the Source tab in Studio, within the <Widget> </Widget> tags.
4. Preview the widget.

<Body>  
<LineBreak LineCount="2" />  
<Chart Type="XY" ChartDataColumn="Avg" ChartHeight="200" ChartWidth="550" XYChartType="Line" ChartLabelColumn="Time" LineStyle="DotLine" LineWidth="2" ShowDataValues="False" BackgroundColor="Khaki" BorderBottom="50" BorderLeft="50" BorderRight="50" BorderTop="50" Color="Blue" ChartTitle="Dow Jones Averages">  
<DataLayer Type="Static" ID="dlDowJones">  
<StaticDataRow Time="Open" Avg="12182" />  
<StaticDataRow Time="10:00" Avg="12110" />  
<StaticDataRow Time="10:30" Avg="12102" />  
<StaticDataRow Time="11:00" Avg="12128" />  
<StaticDataRow Time="11:30" Avg="12140" />  
<StaticDataRow Time="12:00" Avg="12125" />  
<StaticDataRow Time="12:30" Avg="12150" />  
<StaticDataRow Time="1:00" Avg="12221" />  
<StaticDataRow Time="1:30" Avg="12229" />  
<StaticDataRow Time="2:00" Avg="12225" />  
<StaticDataRow Time="2:30" Avg="12205" />  
<StaticDataRow Time="3:00" Avg="12214" />  
<StaticDataRow Time="3:30" Avg="12243" />  
<StaticDataRow Time="Close" Avg="12240" />  
</DataLayer>  
</Chart>  
</Body>

Now copy the widget script from the Preview panel into an HTML page created outside of Studio and experiment.

keywords: integrate, integration
