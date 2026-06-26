---
title: "REST \u2014 Config Settings"
id: 5281669713431
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281669713431-REST-Config-Settings
updated_at: 2022-05-03T22:07:48Z
---

# REST — Config Settings

# REST — Config Settings

The **Settings** endpoint allows access to many settings of the current configuration and session.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All requests require a [Session Id](https://devnet.logianalytics.com/hc/en-us/articles/5281669654679-REST-Sessions#Session) URL parameter and basic request headers. In the following topic, headers are omitted in the interest of brevity.

## Settings JSON

Settings are represented as JSON objects with the following properties. Each corresponds with a setting in the **Admin Console** and base configuration file. Some settings appear both in the Settings JSON (Table A) and in General Settings JSON (Table B). When this happens, use the Table B setting.

Table A — Settings JSON Properties

| Name | Type | Writable |
| --- | --- | --- |
| General | **General Settings** | yes |
| DateFormat *Deprecated. Use General/DateFormat instead.* | string | yes |
| TimeFormat *Deprecated. Use General/TimeFormat instead.* | string | yes |
| DateTimeFormat *Deprecated. Use General/DateTimeFormat instead.* | string | yes |
| SeparatorSymbol *Deprecated. Use General/SeperatorSumbol instead.* | string | yes |
| CurrencySymbol *Deprecated. Use General/CurrencySymbol instead.* | string | yes |
| DecimalSymbol *Deprecated. Use General/DecimalSymbol instead.* | string | yes |
| ShowGrid *Deprecated. Use General/IsShowGrid instead*. | Boolean | yes |
| ShowCrossTabReports *Deprecated. Use General/IsShowCrossTabReports instead.* | Boolean | yes |
| ShowExpressReports *Deprecated. Use General/IsShowExpressReports instead.* | Boolean | yes |
| ShowExpressReportsGrouping *Deprecated. Use General/IsShowExpressReportsGrouping* *instead.* | Boolean | yes |
| ShowExpressReportsFormulas *Deprecated. Use General/IsShowExpressReportsFormulaButton instead.* | Boolean | yes |
| ShowExpressReportsStyling *Deprecated. Use General/IsShowExpressReportsStylingToolbar instead.* | Boolean | yes |
| ShowExpressReportsThemes *Deprecated. Use General/IsShowExpressReportsThemes instead.* | Boolean | yes |
| ShowAdvancedReports *Deprecated. Use General/IsShowAdvancedReports instead.* | Boolean | yes |
| ShowScheduleReports *Deprecated. Use General/IsShowScheduleReports instead.* | Boolean | yes |
| ShowScheduleReportsManager *Deprecated. Use General/IsShowScheduleReportsManager instead.* | Boolean | yes |
| ShowScheduleReportsEmail *Deprecated. Use General/IsShowScheduleReportsEmail instead.* | Boolean | yes |
| ReadFilterValues *Deprecated. Use General/IsReadFilterValues instead.* | Boolean | yes |
| ShowTabs | Boolean | yes |
| WebReportsBaseUrl | string | yes |
| DefaultFolderName | string | yes |
| DefaultReportName | string | yes |

### General Settings JSON

Some settings appear both in the Settings JSON (Table A) and in General Settings JSON (Table B). When this happens, use the Table B setting.

Table B – General Settings JSON Properties

| Name | Type | Writable |
| --- | --- | --- |
| ReportPath | string | yes |
| AllowHomeDirect | Boolean | yes |
| AllowHtmlOutput | Boolean | yes |
| AllowExcelOutput | Boolean | yes |
| AllowPdfOutput | Boolean | yes |
| AllowRtfOutput | Boolean | yes |
| AllowCsvOutput | Boolean | yes |
| DefaultOutputType | [wrExportType](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrExport) | yes |
| IsWriteLog | Boolean | yes |
| CustomCode | string | yes |
| LicenseKey | string | yes |
| DateFormat | string | yes |
| TimeFormat | string | yes |
| DateTimeFormat | string | yes |
| DateTimeTreatedAs | integer   0. Date 1. Time 2. DateTime | yes |
| IsReadFilterValues | Boolean | yes |
| DbTimeout | integer | yes |
| DbRowLimit | integer | yes |
| DbRowLimitStepSize | integer | yes |
| VisualizationDbRowLimit | integer | yes |
| CallTypeParamName | string | yes |
| ColumnParamName | string | yes |
| FilterParamName | string | yes |
| FullFilterParamName | string | yes |
| SortParamName | string | yes |
| DataCategoryParamName | string | yes |
| ObjectIdParamName | string | yes |
| IsShowGrid | Boolean | yes |
| ActiveRoleId | string | yes |
| IsDebugging | Boolean | yes |
| IsShowPdfTemplate | Boolean | yes |
| IsDashboardPromptAtExecution | Boolean | yes |
| IsDashboardShowUrlItemButton | Boolean | yes |
| IsVisualizationShowKeyword | Boolean | yes |
| IsShowChartWizard | Boolean | yes |
| IsShowMapWizard | Boolean | yes |
| IsShowGoogleMapWizard | Boolean | yes |
| IsShowGaugeWizard | Boolean | yes |
| IsSaveOnExecute | Boolean | yes |
| IsSaveOnFinish | Boolean | yes |
| IsEnableRightClickMenus | Boolean | yes |
| IsEnableReportsTreeDragAndDrop | Boolean | yes |
| IsShowLinkReportFields | Boolean | yes |
| IsShowLinkReportFormula | Boolean | yes |
| IsShowLinkAction | Boolean | yes |
| IsShowInsertImage | Boolean | yes |
| ExpirationDateStr | string | yes |
| IsHtmlPaging | Boolean | yes |
| WindowHeight | integer | yes |
| WindowWidth | integer | yes |
| SeparatorSymbol | string | yes |
| CurrencySymbol | string | yes |
| DecimalSymbol | string | yes |
| IsDataMapping | Boolean | yes |
| IsShowJoinFields | Boolean | yes |
| IsDetectJoinedObjects | Boolean | yes |
| IsEnableSpecialCartesianProcessing | Boolean | yes |
| IsIncludeNotFilterNullValues | Boolean | yes |
| TempPath | string | no |
| TempCloudService | string | yes |
| DataCloudService | string | yes |
| IsShowScheduleReports | Boolean | yes |
| IsShowScheduleReportsManager | Boolean | yes |
| ScheduleManagerViewLevel | [ScheduleManagerViewLevel](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#Schedule) | yes |
| IsShowScheduleReportsEmail | Boolean | yes |
| ScheduleRemotingHost | string | yes |
| SynchronousRemotingHost | string | yes |
| SchedulerQueueService | string | yes |
| ReportScheduleEmailSubject | string | yes |
| ReportScheduleEmailBody | string | yes |
| IsRenewSession | Boolean | yes |
| PasswordRequirement | string | yes |
| IsExecuteRemotely | Boolean | yes |
| IsAccessDataSourcesRemotely | Boolean | yes |
| MaxTempFileAge | integer | yes |
| AllowExecuteNewFilters | Boolean | yes |
| ExternalInterface | string | yes |
| DecimalPlaces | integer | yes |
| CurrencyDecimalPlaces | integer | yes |
| ApplyGeneralFormatDecimalPlaces | Boolean | yes |
| ApplyGeneralCurrencyRightAlignment | Boolean | yes |
| ChartColors | string | yes |
| GeochartMapKey | string | yes |
| MapColors | string | yes |
| GoogleMapKey pre-v2018.1 | string | yes |
| GoogleMapJSAPIKey v2018.1+ | string | yes |
| GoogleMapGeocodeAPIKey v2018.1+ | string | yes |
| GoogleMapColors | string | yes |
| GaugeColors | string | yes |
| IsShowGroupFilters | Boolean | yes |
| IsShowJoinsWindow | Boolean | yes |
| IsShowAdvancedJoins | Boolean | yes |
| IsShowEventsWindow | Boolean | yes |
| IsShowReportParametersWindow | Boolean | yes |
| IsShowCrosstabReports | Boolean | yes |
| IsShowDashboardReports | Boolean | yes |
| IsShowChainedReports | Boolean | yes |
| IsAllowExpressViewLiveEdit | Boolean | yes |
| IsShowExpressViews | Boolean | yes |
| IsShowDashboardNewVisualizationButton | Boolean | yes |
| IsShowDashboardDataFieldsSearch | Boolean | yes |
| IsShowExpressViewDataFieldsSearch | Boolean | yes |
| IsUseSampleDataForDashboardVisualizationDesign | Boolean | yes |
| IsDashboardPromptKeywordByDefault | Boolean | yes |
| IsShowExpressReports | Boolean | yes |
| IsShowExpressReportsGrouping | Boolean | yes |
| IsShowExpressReportsFormulaButton | Boolean | yes |
| IsShowExpressReportsStylingToolbar | Boolean | yes |
| IsShowExpressReportsThemes | Boolean | yes |
| IsShowAdvancedReports | Boolean | yes |
| IsShowGroupHeadersFormulaButton | Boolean | yes |
| IsOneCategoryLimit | Boolean | yes |
| IsCacheServices | Boolean | yes |
| SchedulerRecipientWindow | string | yes |
| FilterExecutionWindow | string | yes |
| IsShowIeDownloadButton | Boolean | yes |
| IsDeleteSchedulesUponReportDeletion | Boolean | yes |
| AllowMultipleSessions | Boolean | yes |
| AllowMD5OnFIPS | Boolean | yes |
| WriteBOMToCSV v2019.1.1+ | Boolean | yes |
| IsShowScheduleNoEndDate | Boolean | yes |
| IsShowScheduleIntradayRecurrence | Boolean | yes |
| TempUrl | string | yes |
| UserPreferenceStorage | integer | yes |
| UserStartupReportOverwriteGettingStarted | Boolean | yes |
| UserStartupReportMaxNum | integer | yes |
| ExcelExportTarget | integer   0. 2003 1. 2007 2. 2010 3. 2013 4. 2016 | yes |
| AllowDependantFilters | Boolean | yes |
| LinkedReportsInNewTab | Boolean | yes |
| LoadImageFuncParamPrefix | string | yes |
| LanguageFile | string | yes |
| IsShowHelp | Boolean | yes |
| CustomHelpSource | string | yes |
| IsEmailScheduledReports | Boolean | yes |
| IsEnableBatchReports | Boolean | yes |
| IsShowScheduleDeliveryTypeOptions | Boolean | yes |
| IsUseSecureRemotingChannel | Boolean | yes |
| IsShowTemplateUploadButton | Boolean | yes |
| UseSVGForAppIcons | Boolean | yes |
| CrossTabMaximumFields | Boolean | yes |
| IsShowExportsInTab | Boolean | yes |
| IsShowHtmlToolbar | integer   1. auto 2. show always 3. hide always | yes |
| IsEnableScheduling | Boolean | yes |
| IsShowFilterDescription | Boolean | yes |
| DefaultFilterExecutionWindow | integer   0. standard 1. operator 2. simple 3. custom | yes |
| IsChangeableFilterExecutionWindow | Boolean | yes |
| IgnoreInaccessibleReportFolders | Boolean | yes |
| SchemaAccessType | integer   1. datasource 2. metadata | yes |
| ServerTimeZoneOffset | decimal  light bulb Set to *0* to use the **ClientTimeZoneName**. *If null, Exago will use the External Interface (a deprecated extensibility feature) to calculate the time zone change.* | yes |
| ClientTimeZoneName | string | yes |
| IsShowEnhancedTooltips | Boolean | yes |
| IsShowReportUploadDownloadOptions | Boolean | yes |
| AllowInteractiveHtml | Boolean | yes |
| AllowHtmlInScheduledEmails | Boolean | yes |
| DefaultIsDockOpen | Boolean | yes |
| DockPlacement | integer   0. left 1. right | yes |
| CssTheme | string | yes |
| AllowExecuteSaveToDesign | Boolean | yes |
| UserAllowUserReports | Boolean | yes |
| MaxNumberOfChartPoints | integer | yes |
| DefaultFont | string | yes |
| DefaultFontSize | integer | yes |
| DefaultChartFont | string | yes |
| IsWebFarmSupport | Boolean | yes |
| IsSilentDashboardRefresh | Boolean | yes |
| MaxJobExecutionMinutes | integer | yes |
| ChainedReportMaxCollationExecutions v2021.1.8+ | integer | yes |
| IsAggregateAndGroupInDatabase | Boolean | yes |
| IsEvaluateFormulasInDatabase | Boolean | yes |
| IsShowBrowserOutOfDateWarning | Boolean | yes |
| AreDateFunctionsLoaded | Boolean | yes |
| VersionNumber | string | no |
| DbRowLimitParamName v2018.1 | string | yes |
| DbRowRangeStartParamNamev2018.1+ | string | yes |
| DbRowRangeEndParamName v2018.1+ | string | yes |
| ExpressviewJoinAlgorithm v2018.1+ | string  “Standard” or “Legacy” | yes |
| ExcludeDataSourcesReportCustomSQL v2018.1+ | Boolean | yes |
| LoadAssemblyInExternalDomain v2018.1+ | Boolean | yes |
| ShowTipsExpressView v2018.2+) | Boolean | yes |
| ShowTutorialExpressView v2018.2+ | Boolean | yes |
| IsShowSQLWindow v2019.1+ | Boolean | yes |
| SqlGenerationLevel v2020.1+ | integer | yes |

#### Example:

```
{
  "General": {
    "ReportPath": "C:ExagoReports",
    "AllowHomeDirect": true,
    "AllowHtmlOutput": true,
    "AllowExcelOutput": true,
    "AllowPdfOutput": true,
    "AllowRtfOutput": true,
    "AllowCsvOutput": true,
    "DefaultOutputType": 2,
    "IsWriteLog": true,
    "CustomCode": "",
    "LicenseKey": "", 
    "DateFormat": "",
    "TimeFormat": "",
    "DateTimeFormat": "",
    "DateTimeTreatedAs": 0,
    "IsReadFilterValues": true,
    "DbTimeout": 600,
    "DbRowLimit": 0,
    "DbRowLimitStepSize": 1000,
    "VisualizationDbRowLimit": 0,
    "CallTypeParamName": "",
    "ColumnParamName": "",
    "FilterParamName": "",
    "FullFilterParamName": "",
    "SortParamName": "",
    "DataCategoryParamName": "",
    "ObjectIdParamName": "",
    "IsShowGrid": true,
    "ActiveRoleId": "",
    "IsDebugging": false,
    "IsShowPdfTemplate": true,
    "IsDashboardPromptAtExecution": false,
    "IsDashboardShowUrlItemButton": false,
    "IsVisualizationShowKeyword": false,
    "IsShowChartWizard": true,
    "IsShowMapWizard": false,
    "IsShowGoogleMapWizard": false,
    "IsShowGaugeWizard": true,
    "IsSaveOnExecute": true,
    "IsSaveOnFinish": true,
    "IsEnableRightClickMenus": true,
    "IsEnableReportsTreeDragAndDrop": true,
    "IsShowLinkReport": true,
    "IsShowLinkReportFields": true,
    "IsShowLinkReportFormula": false,
    "IsShowLinkAction": false,
    "IsShowInsertImage": true,
    "ExpirationDateStr": "",
    "IsHtmlPaging": true,
    "WindowHeight": 0,
    "WindowWidth": 0,
    "SeparatorSymbol": ",",
    "CurrencySymbol": "$",
    "DecimalSymbol": ".",
    "IsDataMapping": false,
    "IsShowJoinFields": true,
    "IsDetectJoinedObjects": true,
    "IsEnableSpecialCartesianProcessing": true,
    "IsIncludeNotFilterNullValues": false,
    "TempPath": "",
    "TempCloudService": "",
    "DataCloudService": "",
    "IsShowScheduleReports": false,
    "IsShowScheduleReportsManager": false,
    "ScheduleManagerViewLevel": 0,
    "IsShowScheduleReportsEmail": false,
    "ScheduleRemotingHost": "",
    "SynchronousRemotingHost": "",
    "SchedulerQueueService": "",
    "ReportScheduleEmailSubject": "",
    "ReportScheduleEmailBody": "",
    "IsRenewSession": true,
    "PasswordRequirement": "",
    "IsExecuteRemotely": false,
    "IsAccessDataSourcesRemotely": false,
    "MaxTempFileAge": 1440,
    "AllowExecuteNewFilters": true,
    "ExternalInterface": "",
    "DecimalPlaces": -1,
    "CurrencyDecimalPlaces": -1,
    "ApplyGeneralFormatDecimalPlaces": false,
    "ApplyGeneralCurrencyRightAlignment": true,
    "ChartColors": "#e85d61, #e5d08f, #00d995",
    "GeochartMapKey": "",
    "MapColors": "Lightblue,Navy",
    "GoogleMapKey": "",
    "GoogleMapColors": "Lightblue,Navy",
    "GaugeColors": "#e85d61, #e5d08f, #00d995",
    "IsShowGroupFilters": true,
    "IsShowJoinsWindow": true,
    "IsShowAdvancedJoins": true,
    "IsShowEventsWindow": false,
    "IsShowReportParametersWindow": true,
    "IsShowCrosstabReports": true,
    "IsShowDashboardReports": true,
    "IsShowChainedReports": true,
    "IsAllowExpressViewLiveEdit": false,
    "IsShowExpressViews": true,
    "IsShowDashboardNewVisualizationButton": true,
    "IsShowDashboardDataFieldsSearch": false,
    "IsShowExpressViewDataFieldsSearch": true,
    "IsUseSampleDataForDashboardVisualizationDesign": true,
    "IsShowDashboardExistingVisualizationReportButton": false,
    "IsDashboardPromptKeywordByDefault": false,
    "IsShowExpressReports": true,
    "IsShowExpressReportsGrouping": true,
    "IsShowExpressReportsFormulaButton": true,
    "IsShowExpressReportsStylingToolbar": true,
    "IsShowExpressReportsThemes": true,
    "IsShowAdvancedReports": true,
    "IsShowGroupHeadersFormulaButton": false,
    "IsOneCategoryLimit": false,
    "IsCacheServices": true,
    "SchedulerRecipientWindow": "",
    "FilterExecutionWindow": "",
    "IsShowIeDownloadButton": false,
    "IsDeleteSchedulesUponReportDeletion": false,
    "AllowMultipleSessions": true,
    "AllowMD5OnFIPS": false,
    "WriteBOMToCSV": false,
    "IsShowScheduleNoEndDate": true,
    "IsShowScheduleIntradayRecurrence": true,
    "TempUrl": "",
    "UserPreferenceStorage": 0,
    "UserStartupReportOverwriteGettingStarted": false,
    "UserStartupReportMaxNum": 1,
    "ExcelExportTarget": 1,
    "AllowDependantFilters": false,
    "LinkedReportsInNewTab": false,
    "LoadImageFuncParamPrefix": "",
    "LanguageFile": "en-us,en-us-getting-started,en-us-tooltips",
    "IsShowHelp": true,
    "CustomHelpSource": "",
    "IsEmailScheduledReports": true,
    "IsEnableBatchReports": false,
    "IsShowScheduleDeliveryTypeOptions": false,
    "IsUseSecureRemotingChannel": false,
    "IsShowTemplateUploadButton": false,
    "UseSVGForAppIcons": true,
    "CrossTabMaximumFields": 5,
    "IsShowExportsInTab": true,
    "IsShowHtmlToolbar": 0,
    "IsEnableScheduling": true,
    "IsShowFilterDescription": false,
    "DefaultFilterExecutionWindow": 0,
    "IsChangeableFilterExecutionWindow": true,
    "IgnoreInaccessibleReportFolders": false,
    "SchemaAccessType": 1,
    "ServerTimeZoneOffset": 0,
    "ClientTimeZoneName": "America/New_York",
    "IsShowEnhancedTooltips": true,
    "IsShowReportUploadDownloadOptions": false,
    "AllowInteractiveHtml": true,
    "AllowHtmlInScheduledEmails": false,
    "DefaultIsDockOpen": false,
    "DockPlacement": 0,
    "CssTheme": "Basic",
    "AllowExecuteSaveToDesign": true,
    "UserAllowUserReports": true,
    "MaxNumberOfChartPoints": 300,
    "DefaultFont": "Arial",
    "DefaultFontSize": 8,
    "DefaultChartFont": "Arial",
    "IsWebFarmSupport": false,
    "IsSilentDashboardRefresh": false,
    "MaxJobExecutionMinutes": 240,
    "IsAggregateAndGroupInDatabase": false,
    "IsEvaluateFormulasInDatabase": true,
    "IsShowBrowserOutOfDateWarning": true,
    "AreDateFunctionsLoaded": true,
    "VersionNumber": "2016.3.4.100"
  },
  "DateFormat": "",
  "TimeFormat": "",
  "DateTimeFormat": "",
  "SeparatorSymbol": ",",
  "CurrencySymbol": "$",
  "DecimalSymbol": ".",
  "ShowGrid": true,
  "ShowCrossTabReports": true,
  "ShowExpressReports": true,
  "ShowExpressReportsGrouping": true,
  "ShowExpressReportsFormulas": true,
  "ShowExpressReportsStyling": true,
  "ShowExpressReportsThemes": true,
  "ShowAdvancedReports": true,
  "ShowScheduleReports": false,
  "ShowScheduleReportsManager": false,
  "ShowScheduleReportsEmail": false,
  "ReadFilterValues": true,
  "ShowTabs": true,
  "WebReportsBaseUrl": null,
  "DefaultFolderName": "",
  "DefaultReportName": ""
}
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All requests require a [Session Id](https://devnet.logianalytics.com/hc/en-us/articles/5281669654679-REST-Sessions#Session) URL parameter and basic request headers. In the following topic, headers are omitted in the interest of brevity.

## Show All Settings

```
GET /rest/Settings
```

### Using curl

```
curl http://{webservice}/rest/Settings?sid={sid} -X GET
```

### Example response

```
Status: 200 OK

{
  "General": {
    "ReportPath": "C:ExagoReports",
    ...
  }
  "DateFormat":                 "MM/dd/yyyy",
  "TimeFormat":                 "hh:mm:ss a",
  "DateTimeFormat":             "MM/dd/yyyy hh:mm:ss a",
  "SeparatorSymbol":            ",",
  "CurrencySymbol":             "$",
  "ShowGrid":                   true,
  "ShowCrossTabReports":        true,
  "ShowExpressReports":         true,
  ...
}
```

## Edit Settings

Only supply the properties to be edited

```
PATCH /rest/Settings
```

### Using curl

```
curl http://{webservice}/rest/settings?sid={sid} -X PATCH ^
	-d "{
             'General':
              {
                'ReportPath':'C:ExagoReports',
                'IsShowLinkReportFormula':false,
                ...
              }
             'ShowScheduleReports':false,
             'ShowExpressReports':false,
             ...
            }"
```

### Example response

```
Status: 204 No Content
```
