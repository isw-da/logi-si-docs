---
title: "Custom Context Sensitive Help"
id: 5281597846295
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281597846295-Custom-Context-Sensitive-Help
updated_at: 2022-05-03T22:08:18Z
---

# Custom Context Sensitive Help

# Custom Context Sensitive Help

Exago is installed with context sensitive help. When a user clicks the **Help**![Help.png](https://devnet.logianalytics.com/hc/article_attachments/5432233043223/help.png) icon a tab opens to display the appropriate section of the Exago User Guide. The content of this tab can be replaced with custom content managed by the host application.

To implement **Custom Context Sensitive Help**:

1. Create a minimum of one web page for the custom help content.
2. Set the **Admin Console** > **General Settings** > **Feature/UI Settings** > **Custom Help Source** setting to the URL of the web page from step 1. Prefix the URL with `url=`.  
   Example

   ```
   url=http://www.Customhelp.com/Exago;
   ```

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Supplying a value for the **Custom Help Source** will replace the Exago provided help system throughout the entire application.

Now, when a user clicks the **Help**![Help.png](https://devnet.logianalytics.com/hc/article_attachments/5432233043223/help.png) icon a tab opens to display the content from the supplied **Custom Help Source** URL.

The user’s language and a context parameter will be appended as a query string to the URL.

* The **language** is determined by the value of the **Admin Console** > **General Settings** > **Main Settings** > **Language File** setting.
* The **context parameter** is determined by where in the application the user clicked the **Help ![Help.png](https://devnet.logianalytics.com/hc/article_attachments/5432233043223/help.png)** icon, selected from Table A below.

Example

```
http://www.customhelp.com/Exago?helpKey=tabChartType&language=en-us
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Create a default page to handle any cases where an undocumented or null context parameter is passed. This guarantees that a valid help page will always be displayed.

Table A — Custom Context Help Context Parameters

| Context Parameter aka “helpKey” | Details |
| --- | --- |
| tabexecute | The user is in the **Report Viewer**. |
| ExpressView | |
| tabExpressView | The user has the ExpressView Designer active. |
| tabExpressViewFilter v2019.2.37+v2020.1.20+v2021.1.8+ | The user is interacting with the [Filters tab](https://devnet.logianalytics.com/hc/en-us/articles/5281589443095-ExpressView-Introduction-v2021-1-#Filters) of the ExpressView Designer’s Properties Pane |
| tabExpressViewSort v2019.2.37+v2020.1.20+v2021.1.8+ | The user is interacting with the [Sorts tab](https://devnet.logianalytics.com/hc/en-us/articles/5281589443095-ExpressView-Introduction-v2021-1-#Sorts) of the ExpressView Designer’s Properties Pane |
| tabExpressViewViz v2019.2.37+v2020.1.20+v2021.1.8+ | The user is interacting with the [Visualizations tab](https://devnet.logianalytics.com/hc/en-us/articles/5281589443095-ExpressView-Introduction-v2021-1-#Visuali) of the ExpressView Designer’s Properties Pane |
| dialogExpressViewFormulaEditor v2019.2.37+v2020.1.20+v2021.1.8+ | The user has the [Formula Builder](https://devnet.logianalytics.com/hc/en-us/articles/5281612083991-ExpressView-Formula-Columns-v2021-1-#top) in the ExpressView Designer open. |
| Express Report Wizard | |
| tabExpressName | The user has the Name tab of the Express Report Wizard active. |
| tabExpressCategories | The user has the Categories tab of the Express Report Wizard active. |
| tabExpressSorts | The user has the Sorts tab of the Express Report Wizard active. |
| tabExpressFilters | The user has the Filters tab of the Express Report Wizard active. |
| tabExpressLayout | The user has the Layout tab of the Express Report Wizard active. |
| tabExpressOptions | The user has the Options tab of the Express Report Wizard active. |
| Chained Report Wizard | |
| tabChainedName | The user has the Names tab of the New Chained Report Wizard active. |
| tabChainedReports | The user has the Reports tab of the New Chained Report Wizard active. |
| tabChainedOptions | The user has the Options tab of the New Chained Report Wizard active. |
| CrossTab Wizard | |
| tabCrosstabName | The user has the Names tab of the New CrossTab Report Wizard active. |
| tabCrosstabCategories | The user has the Categories tab of the New CrossTab Report Wizard active. |
| tabCrosstabFilters | The user has the Filters tab of the New CrossTab Report Wizard active. |
| tabCrosstabLayout | The user has the Layout tab of the New CrossTab Report Wizard active. |
| dialogCrosstabOptions | The user has the CrossTab Data Designer dialog open. |
| New Report Wizard pre-v2021.1 | |
| tabAdvancedName pre-v2021.1 | The user has the Names tab of the New Advanced Report Wizard active. |
| tabAdvancedCategories pre-v2021.1 | The user has the Categories tab of the New Advanced Report Wizard active. |
| tabAdvancedSorts pre-v2021.1 | The user has the Sorts tab of the New Advanced Report Wizard active. |
| tabStandardFilters pre-v2021.1 | The user has the Filters tab of the New Advanced Report Wizard active. |
| tabAdvancedLayout pre-v2021.1 | The user has the Layout tab of the New Advanced Report Wizard active. |
| Report Designer | |
| tabDesign | The user is editing an Advanced or CrossTab report in the Advanced Report Designer. |
| dialogName | The user has the Rename Menu active. This key is never called in *v2021.1+* |
| dialogDescription | The user has the Description Menu active. This key is never called in *v2021.1+* |
| dialogCategories | The user has the Categories/[Manage Data Objects](https://devnet.logianalytics.com/hc/en-us/articles/5281533535767-Advanced-Reports-Data-Objects-v2021-1-#Data) dialog open. |
| dialogSorts | The user has the [Sorts dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281555992343-Advanced-Reports-Sorts) open. |
| dialogFilters | The user has the [Filters dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281549708439-Filters#Adding) open. |
| dialogGeneralOptions | The user has the [General Options dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281541782039-Advanced-Reports-Report-Options#General) open. |
| dialogHtmlOptions | The user has the [Report Viewer Options dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281541782039-Advanced-Reports-Report-Options#Report) open. |
| listItemReportHtmlOptionsGeneral | The user has the [General section of the Report Viewer Options dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281541782039-Advanced-Reports-Report-Options#General2) open. |
| listItemReportHtmlOptionsFilters | The user has the [Filter section of the Report Viewer Options dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281541782039-Advanced-Reports-Report-Options#Filters) open. |
| listItemReportHtmlOptionsSorts | The user has the [Sorts section of the Report Viewer Options dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281541782039-Advanced-Reports-Report-Options#Sorts) open. |
| dialogTemplates | The user has the [Template dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281564145303-Advanced-Reports-Templates) open. |
| dialogJoins | The user has the [Joins dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281549160087-Advanced-Reports-Joins) open. |
| dialogJoinEdit | The user has the [Joins dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281549160087-Advanced-Reports-Joins) open. |
| dialogFormulaEditor | The user has the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/5281623158039-Formula-Editor) open. |
| dialogLinkedReport | The user has the [Linked Report dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281533707031-Linked-Reports-Drilldowns-) open. |
| tabCellFormatNumber | The user has the [Number tab of the Cell Format dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281564235671-Cell-Formatting#Number2) active. |
| tabCellFormatBorder | The user has the [Border tab of the Cell Format dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281564235671-Cell-Formatting#Border) active. |
| tabCellFormatConditional | The user has the [Conditional tab of the Cell Format](https://devnet.logianalytics.com/hc/en-us/articles/5281564235671-Cell-Formatting#Conditio) dialog active. |
| dialogCrosstabDesign | The user has the [CrossTab Data Designer dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281553083159-Advanced-Reports-CrossTabs) open. |
| dialogGroup | The user has the Group Section dialog open. |
| dialogSectionShading | The user has the [Section Shading dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281572597527-Advanced-Reports-Sections-v2021-1-#Section) open. |
| dialogShowSQL | The user has the [Show Generated SQL](https://devnet.logianalytics.com/hc/en-us/articles/5281548966167-Advanced-Options#Show) open. |
| dialofReportLevelParameters | The user has the [Report Level Parameters](https://devnet.logianalytics.com/hc/en-us/articles/5281548966167-Advanced-Options#Report-L) open. |
| tabChartType | The user has the [Type tab of the Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281542473367-Charts-and-the-Chart-Wizard#Chart) open. |
| dialogChartBenchmarkLine | The user has the [Benchmark Lines dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281542473367-Charts-and-the-Chart-Wizard#Use) open. |
| dialogChartDataFormat | The user has the [Data Layout… dialog of the Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281542473367-Charts-and-the-Chart-Wizard#Change) open. |
| tabChartLabels | The user has the [Labels tab of the Chart menu](https://devnet.logianalytics.com/hc/en-us/articles/5281542473367-Charts-and-the-Chart-Wizard#Labels) open. |
| tabChartData | The user has the [Data tab of the Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281542473367-Charts-and-the-Chart-Wizard#Data) open. |
| tabChartAppeance | The user has the [Appearance tab of the Chart menu](https://devnet.logianalytics.com/hc/en-us/articles/5281542473367-Charts-and-the-Chart-Wizard#Appearan) active. |
| tabChartSizeAndPreview | The user has the [Size and Preview tab of the Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281542473367-Charts-and-the-Chart-Wizard#Size) open. |
| tabMapType | The user has the [Type tab of the GeoChart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281573529495-GeoCharts#Type) open. |
| tabMapLocations | The user has the [Locations tab of the GeoChart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281573529495-GeoCharts#Location) open. |
| tabMapData | The user has the [Data tab of the GeoChart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281573529495-GeoCharts#Data) open. |
| tabGaugeType | The user has the [Appearance tab of the Gauge Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281556730135-Gauges#Appearan) open. |
| tabGaugeData | The user has the [Data tab of the Gauge Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281556730135-Gauges#Data) open. |
| tabGoogleMapAppearance | The user has the [Appearance tab of the Google Maps Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281573605655-Google-Maps#Appearan) open. |
| tabGoogleMapLocations | The user has the [Locations tab of the Google Maps Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281573605655-Google-Maps#Location) open. |
| tabGoogleMapData | The user has the [Data tab of the Google Maps Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281573605655-Google-Maps#Data) open. |
| tabGoogleMapSizeAndPreview | The user has the [Size and Preview tab of the Google Maps Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281573605655-Google-Maps#Size) open. |
| listItemReportCacheOptionsGeneral | The user has the [Execution Caching dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281645120919-Execution-Caching) open. |
| Dashboards | |
| tabDashboard | The user has the [Dashboard Viewer](https://devnet.logianalytics.com/hc/en-us/articles/5281602922903-Dashboard-Viewer-v2019-2-) active |
| tabDashboardDesigner | The user has the [Dashboard Designer](https://devnet.logianalytics.com/hc/en-us/articles/5281580652951-Dashboard-Designer-v2019-2-) active. |
| dialogDashboardUrlOptions | The user is adding or editing a [URL tile](https://devnet.logianalytics.com/hc/en-us/articles/5281602848023-Dashboard-Designer-URL-Tiles-v2019-2-) on the canvas. |
| dialogDasboardImageOptions v2019.2.37+v2020.1.20+v2021.1.8+ | The user is adding or editing an [Image tile](https://devnet.logianalytics.com/hc/en-us/articles/5281602764823-Dashboard-Designer-Image-Tiles-v2019-2-) on the canvas. |
| dialogDashboardTextOptions v2019.2.37+v2020.1.20+v2021.1.8+ | The user is adding or editing a [Text tile](https://devnet.logianalytics.com/hc/en-us/articles/5281588335255-Dashboard-Designer-Text-Tiles-v2019-2-) on the canvas. |
| dialogDashboardName | The user has the Dashboard Rename menu active. |
| dialogDashboardDescription | The user has the Dashboard Description menu active. |
| dialogDashboardOptions | The user has the Dashboard Options menu active. |
| tabDashboardReportOptions | The user is adding or editing an Existing Report tile. |
| tabDashboardReportOptionsFilterPrompts | The user is interacting with the Filters menu. |
| tabDashboardReportOptionsParameterPrompts | The user is interacting with the Parameters menu. |
| tabDashboardReportOptionsOptions | The user has the Options tab of the Insert Report menu active. |
| tabDashboardFilterOptionsReports | The user has the Reports tab of the Insert Filter menu active. |
| tabDashboardFilterOptionsFilter | The user has the Filter tab of the Insert Filter menu active. |
| dialogDashboardVisualizationOptions | The user is adding or editing a visualization tile. |
| Scheduler | |
| tabScheduleReportManager | The user has the Schedule Manager active. |
| tabScheduleRecurrence | The user has the Recurrence tab of the New Schedule Wizard active. |
| tabScheduleParameters | The user has the Parameter tab of the New Schedule Wizard active. |
| tabScheduleFilters | The user has the Filter tab of the New Schedule Wizard active. |
| tabScheduleRecipients | The user has the Recipients tab of the New Schedule Wizard active. |
| tabScheduleBatch | The user has the Batch tab of of the New Schedule Wizard active. |
