---
title: "Config File XML & API Setting Reference (General Nodes)"
id: 5281643841175
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281643841175-Config-File-XML-API-Setting-Reference-General-Nodes
updated_at: 2023-04-03T17:52:19Z
---

# Config File XML & API Setting Reference (General Nodes)

# Config File XML & API Setting Reference (General Nodes)

When building configuration files without the **Admin Console**, or to change settings in the API, use this reference to map **Admin Console** settings to the relevant config file node or API key.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> For config file elements not in the <general> node, see **[Config File XML Reference (All Nodes but General)](https://devnet.logianalytics.com/hc/en-us/articles/5281627946391-Config-File-XML-Reference-All-Nodes-but-General-)**.

## How to Use This Topic

### *Setting Name : type*

* `<config_file_node>` (within the <general> element)
* *Api\_Key* (within the **`Api.SetupData.General`** namespace)

#### Example

#### Allow Filter Dependencies : bool

* `<allowdependantfilters>`
* AllowDependantFilters

This Boolean value enables or disables the Filter Dependency feature. To enable it, set the setting to *True*. To disable it, set it to *False*. The sample configuration file below enables it.

```
Enable filter dependency

<general>
   <allowdependantfilters>True</allowdependantfilters>
</general>
```

Alternatively, this setting may be changed when creating a session with the .NET API:

```
API api = new API(ConfigurationManager.AppSettings["ExagoAppPath"]);
api.General.AllowDependantFilters = false;

api.Action = wrApiAction.Home;
string paramString = api.GetUrlParamString(homePage);
```

Disables Filter Dependency

Or the REST Web Service API:

```
curl http://{webservice}/rest/settings?sid={sid} -X PATCH ^ -d "
{
  'General':
   {
      'AllowDependantFilters':false,
   }
}"
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> This topic is presented in the order that settings appear in the **Admin Console**. Use the browser’s Find function (**Ctrl+F**) to find a specific setting in this topic.

## Main Settings

The **[Main Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281644565527-Main-Settings)** topic includes detailed descriptions of each of these settings.

### Report Path : string pre-v2020.1

* `<reportpath>`
* ReportPath

### Temp Path : string

* `<temppath>`
* TempPath

### Temp Cloud Service : string

* `<tempcloudservice>`
* TempCloudService

### Language File : string

* `<languagefile>`
* LanguageFile

### Temp URL : string

* `<tempurl>`
* TempUrl

### Allow direct access to Exago (bypassing API) : bool

* `<allowhomedirect>`
* AllowHomeDirect

### Allow Execution in Viewer : bool

* `<allowhtmloutput>`
* AllowHtmlOutput

### Allowed Export Types – Excel : bool

* `<allowexceloutput>`
* AllowExcelOutput

### Allowed Export Types – PDF : bool

* `<allowpdfoutput>`
* AllowPdfOutput

### Allowed Export Types – RTF : bool

* `<allowrtfoutput>`
* AllowRtfOutput

### Allowed Export Types – CSV : bool

* `<allowcsvoutput>`
* AllowCsvOutput

### Default Output Type : constant

Possible values: *excel, pdf, rtf, csv*

* `<defaultoutputtype>`
* DefaultOutputType

### Report Tree Shortcut : constant

Possible values: *Run*, *Export*

* `<reporttreeshortcut>`
* ReportTreeShortcutRun : bool

### Active Role : string v2019.1+

* <activeroleid>
* ActiveRoleId

## Culture Settings

The **[Culture Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281607969943-Culture-Settings)** topic includes detailed descriptions of each of these settings.

### Date Format : string

* `<dateformat>`
* DateFormat

### Time Format : string

* `<timeformat>`
* TimeFormat

### DateTime Format : string

* `<datetimeformat>`
* DateTimeFormat

### DateTime Values Treated As : constant

Possible values: *date, datetime*

* `<datetimetreatedas>`
* DateTimeTreatedAs

### Numeric Separator Symbol : string

* `<separatorsymbol>`
* SeparatorSymbol

### Numeric Currency Symbol : string

* `<currencysymbol>`
* CurrencySymbol

### Numeric Decimal Symbol : string

* `<decimalsymbol>`
* DecimalSymbol

### Numeric Decimal Places : int

* `<decimalplaces>`
* DecimalPlaces

### Currency Decimal Places : int

* `<currencydecimalplaces>`
* CurrencyDecimalPlaces

### Apply Numeric Decimal Places to General Cell Formatting : bool

* `<applygeneralformatdecimalplaces>`
* ApplyGeneralFormatDecimalPlaces

### Apply General Currency Right Alignment : bool

* `<applygeneralcurrencyrightalignment>`
* ApplyGeneralCurrencyRightAlignment

### Server Time Zone Offset : decimal

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Set to *0* to use the **Client Time Zone Name**. *If null, Exago will use the External Interface (a deprecated extensibility feature) to calculate the time zone change*.

* `<servertimezoneoffset>`
* ServerTimeZoneOffset

### Time Zone Name : string

* `<clienttimezonename>`
* ClientTimeZoneName

## Feature/UI Settings

The **[Feature/UI Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281644433431-Feature-UI-Settings)** topic includes detailed descriptions of each of these settings.

### Allow Creation/Editing of Express Reports : bool

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting was removed from the [Admin Console](https://devnet.logianalytics.com/hc/en-us/articles/5281616679575-About-the-Admin-Console) in *v2019.2* but remains available here in the config file. No other functionality was removed.

* `<showexpressreports>`
* IsShowExpressReports

### Allow Creation/Editing of Advanced Reports : bool

* `<showadvancedreports>`
* IsShowAdvancedReports

### Allow Creation of CrossTab Reports : bool

* `<showcrosstabreports>`
* IsShowCrosstabReports

### Allow Creation/Editing of Dashboards : bool

* `<showDashboardreports>`
* IsShowDashboardReports

### Allow Creation/Editing of Chained Reports : bool

* `<showchainedreports>`
* IsShowChainedReports

### Allow Creation/Editing of ExpressViews : bool

* `<showexpressviews>`
* IsShowExpressViews

### Allow Editing ExpressView with Live Data : bool

* `<allowexpressviewliveedit>`
* IsAllowExpressViewLiveEdit

### Show Data Fields Search Box : bool pre-v2017.2

* `<showexpressviewdatafieldssearch>`
* IsShowExpressViewDataFieldsSearch

### Fields Enabled in Data Fields Tree : bool pre-v2017.2

* `<expressviewdatafieldsdisplay>`
* IsExpressViewDataFieldsDisplay

### Fields Enabled in Data Fields Tree : bool v2017.2+

* `<showdatafieldssearch>`
* IsShowDataFieldsSearch

### Show Styling Toolbar : bool

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting was removed from the [Admin Console](https://devnet.logianalytics.com/hc/en-us/articles/5281616679575-About-the-Admin-Console) in *v2019.2* but remains available here in the config file. No other functionality was removed.

* `<showexpressreportsstylingtoolbar>`
* IsShowExpressReportsStylingToolbar

### Show Themes : bool

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting was removed from the [Admin Console](https://devnet.logianalytics.com/hc/en-us/articles/5281616679575-About-the-Admin-Console) in *v2019.2* but remains available here in the config file. No other functionality was removed.

* `<showexpressreportsthemes>`
* IsShowExpressReportsThemes

### Show Grouping : bool

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting was removed from the [Admin Console](https://devnet.logianalytics.com/hc/en-us/articles/5281616679575-About-the-Admin-Console) in *v2019.2* but remains available here in the config file. No other functionality was removed.

* `<showexpressreportsgrouping>`
* IsShowExpressReportsGrouping

### Show Formula Button : bool

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting was removed from the [Admin Console](https://devnet.logianalytics.com/hc/en-us/articles/5281616679575-About-the-Admin-Console) in *v2019.2* but remains available here in the config file. No other functionality was removed.

* `<showexpressreportsformulabutton>`
* IsShowExpressReportsFormulaButton

### Show CrossTab Wizard : bool

* `<showcrosstabwizard>`
* IsShowCrosstabWizard

### Show Chart Wizard : bool

* `<showchartwizard>`
* IsShowChartWizard

### Chart Colors : string

* `<chartcolors>`
* ChartColors

### Maximum Number of Chart Data Points : int

* `<maxnumberofchartpoints>`
* MaxNumberOfChartPoints

### Default Chart Font : string

* `<defaultchartfont>`
* DefaultChartFont

### Show GeoChart Map Wizard : bool

* `<showmapwizard>`
* IsShowMapWizard

### GeoChart Map Key (optional) : string

* `<geochartmapkey>`
* GeochartMapKey

### GeoChart Map Colors : string

* `<mapcolors>`
* MapColors

### Show Google Map Wizard : bool

* `<showgooglemapwizard>`
* IsShowGoogleMapWizard

### Google Map Key : string pre-v2018.1

* `<googlemapkey>`
* GoogleMapKey

### Google Map Key (unlimited or JS API restricted) : string v2018.1+

* `<googlemapjsapikey>`
* GoogleMapJSAPIKey

### Google Map Key (optional Geocode API restricted) : string v2018.1+

* `<googlemapgeocodeapikey>`
* GoogleMapGeocodeAPIKey

### Google Map Colors : string

* `<googlemapcolors>`
* GoogleMapColors

### Show Gauge Wizard : bool

* `<showgaugewizard>`
* IsShowGaugeWizard

### Gauge Colors : bool

* `<gaugecolors>`
* GaugeColors

### Show Document Template : bool

* `<showpdftemplate>`
* IsShowPdfTemplate

### Show Document Template Upload Button : bool

* `<showtemplateuploadbutton>`
* IsShowTemplateUploadButton

### Show Linked Report : bool

* `<showlinkreport>`
* IsShowLinkReport

### Show Linked Report Fields : bool

* `<showlinkreportfields>`
* IsShowLinkReportFields

### Show Linked Report Formula : bool

* `<showlinkreportformula>`
* IsShowLinkReportFormula

### Show Linked Action : bool

* `<showlinkaction>`
* IsShowLinkAction

### Show Auto Sum Button : bool v2021.1+

* `<showautosum>`
* IsShowAutoSum

### Show Insert Image : bool

* `<showinsertimage>`
* IsShowInsertImage

### Show Joins Window : bool

* `<showjoinswindow>`
* IsShowJoinsWindow

### Show Advanced Joins : bool

* `<showadvancedjoins>`
* IsShowAdvancedJoins

### Advanced Joins Display : bool v2017.3.1+

* `<showcomplexjoins>`
* IsShowComplexJoins

### Allow Category Aliasing : bool v2017.3.1+

* `<showcategoryalias>`
* IsShowCategoryAlias

### Show Events Window : bool

* `<showeventswindow>`
* IsShowEventsWindow

### Show Report-Level Parameters Window : bool

* `<showreportparameterswindow>`
* IsShowReportParametersWindow

### Show SQL Window : bool

* `<showsqlwindow>`
* IsShowSQLWindow

### Show Linked Reports in New Tab : bool pre-v2017.3

* `<linkedreportsinnewtab>`
* LinkedReportsInNewTab

### Linked Report Display : constant v2017.3+

Possible values: *Cursor*, *NewTab*, *ScreenCenter*

* `<linkedreportdisplay>`
* LinkedReportDisplay

### Allow Grouping on non-Sorts : bool

* `<showgroupheadersformulabutton>`
* IsShowGroupHeadersFormulaButton

### Prompt user for Parameters/Filters on Execution : bool

* `<Dashboardpromptatexecution>`
* IsDashboardPromptAtExecution

### Automatically Refresh Reports v2021.1+

* `<Dashboardautomaticallyrefreshtiles>`
* IsDashboardAutomaticallyRefreshTiles

### Show URL Item Button : bool

* `<Dashboardshowurlitembutton>`
* IsDashboardShowUrlItemButton

### Allow Creation/Editing of Dashboard Visualizations : bool

* `<showDashboardnewvisualizationbutton>`
* IsShowDashboardNewVisualizationButton

### Show Data Fields Search Box : bool

* `<showDashboarddatafieldssearch>`
* IsShowDashboardDataFieldsSearch

### Use Sample Data for Dashboard Visualization Design : bool pre-v2019.2

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting was removed from the [Admin Console](https://devnet.logianalytics.com/hc/en-us/articles/5281616679575-About-the-Admin-Console) in *v2019.2* but remains available here in the config file. No other functionality was removed.

* `<usesampledataforDashboardvisualizationdesign>`
* IsUseSampleDataForDashboardVisualizationDesign

### Visualization Database Row Limit : int

* `<visualizationdbrowlimit>`
* VisualizationDbRowLimit

### Refresh Reports/Visualizations on Dashboards Silently : bool

* `<silentDashboardrefresh>`
* IsSilentDashboardRefresh

### Minimum Tile Width for Dashboard Reflow : int v2019.1+

* `<mintilewidth>`
* MinTileWidth

### Minimum Window Width for Dashboard Reflow : int v2019.1+

* `<mindesktopwidth>`
* MinDesktopWidth

### Default Designer Font : string

* `<defaultfont>`
* DefaultFont

### Default Designer Font Size : int

* `<defaultfontsize>`
* DefaultFontSize

### Show Help Button : bool

* `<showhelp>`
* IsShowHelp

### Custom Help Source : string

* `<customhelpsource>`
* CustomHelpSource

### Show Exports in Tab : bool

* `<showexportsintab>`
* IsShowExportsInTab

### Show IE Download Button : bool

* `<showiedownloadbutton>`
* IsShowIeDownloadButton

### Show Join Fields : bool

* `<showjoinfields>`
* IsShowJoinFields

### Show Grid Lines in Report Viewer : bool

* `<showgrid>`
* IsShowGrid

### Show Enhanced Tooltips : bool

* `<enhancedtooltips>`
* IsShowEnhancedTooltips

### Save on Report Execution : bool

* `<saveonexecute>`
* IsSaveOnExecute

### Save on Finish Press : bool

* `<saveonfinish>`
* IsSaveOnFinish

### Enable Right-Click Menus : bool

* `<enablerightclickmenus>`
* IsEnableRightClickMenus

### Enable Reports Tree Drag And Drop : bool

* `<enablereportstreedraganddrop>`
* IsEnableReportsTreeDragAndDrop

### Show Report Upload/Download Options : bool

* `<showreportuploaddownloadoptions>`
* IsShowReportUploadDownloadOptions

### Allow interactivity in report viewer : bool

* `<interactivehtml>`
* AllowInteractiveHtml

### Show Toolbar in Report Viewer : constant

Possible values: *Auto, Show, Hide*

* `<showhtmltoolbar>`
* IsShowHtmlToolbar

### Default interactive report viewer dock is open : bool

* `<defaultisdockopen>`
* DefaultIsDockOpen

### Interactive report viewer default dock placement : [wrDockLocation](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrDockLo)

Possible values: *Left, Right*

* `<dockplacement>`
* DockPlacement

### Allow save to report design from the report viewer : bool

* `<executesavetodesign>`
* AllowExecuteSaveToDesign

### Maximum number of fields in a CrossTab header or tabulation source : int

* `<crosstabmaximumfields>`
* CrossTabMaximumFields

### Use SVG for Application Icons : bool

* `<usesvgforappicons>`
* UseSVGForAppIcons

### Application Theme Selection : string

* `<csstheme>`
* CssTheme

### Join Path Algorithm : const v2018.1+

* `<expressviewjoinalgorithm>`
* ExpressviewJoinAlgorithm

### Allow Creation of Custom SQL Objects : bool v2018.1+

* `<allowreportcustomsqlobjects>`
* IsAllowReportCustomSQLObjects

### Data Sources to Exclude from Custom SQL Object Creation : string v2018.1+

* `<excludedatasourcesreportcustomsql>`
* ExcludeDataSourcesReportCustomSQL

## Programmable Object Settings

The **[Programmable Object Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281608640279-Programmable-Object-Settings)** topic includes detailed descriptions of each of these settings.

### Call Type Parameter Name : string

* `<calltypeparamname>`
* CallTypeParamName

### Column Parameter Name : string

* `<columnparamname>`
* ColumnParamName

### Filter Parameter Name : string

* `<filterparamname>`
* FilterParamName

### Full Filter Parameter Name : string

* `<fullfilterparamname>`
* FullFilterParamName

### Sort Parameter Name : string

* `<sortparamname>`
* SortParamName

### Data Category Parameter Name : string

* `<datacategoryparamname>`
* DataCategoryParamName

### Data Object ID Parameter Name : string

* `<objectidparamname>`
* ObjectIdParamName

### DB Row Limit Parameter Name : string v2018.1+

* `<dbrowlimitparamname>`
* DbRowLimitParamName

### DB Row Start Index Parameter Name : string v2018.1+

* `<dbrowrangestartparamname>`
* DbRowRangeStartParamName

### DB Row End Index Parameter Name : string v2018.1+

* `<dbrowrangeendparamname>`
* DbRowRangeEndParamName

## Filter Settings

The **[Filter Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281628457495-Filter-Settings)** topic includes detailed descriptions of each of these settings.

### Show Group (Min/Max) Filters : bool

* `<showgroupfilters>`
* IsShowGroupFilters

### Show Top N Filters : bool

* `<showtopn>`
* IsShowTopN

### Allow New Filters at Execution : bool

* `<allowexecutenewfilters>`
* AllowExecuteNewFilters

### Read Database for Filter Values : bool

* `<readfiltervalues>`
* IsReadFilterValues

### Allow Filter Dependencies : bool

* `<allowdependantfilters>`
* AllowDependantFilters

### Show Filter Description : bool

* `<showfilterdescription>`
* IsShowFilterDescription

### Default Filter Execution Window : constant

Possible values: *Standard, SimpleWithOperator, Simple, Custom*

* `<defaultFilterExecutionWindow>`
* DefaultFilterExecutionWindow

### Allow User to Change Filter Window : bool

* `<changeableFilterExecutionWindow>`
* IsChangeableFilterExecutionWindow

### Include Null Values for ‘NOT’ Filters : bool

* `<includenotfilternullvalues>`
* IsIncludeNotFilterNullValues

### Custom Filter Execution Window : string

* `<filterexecutionwindow>`
* FilterExecutionWindow

## Database Settings

See **[Database Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281628373655-Database-Settings)** for more information.

### Database Timeout : int

* `<dbtimeout>`
* DbTimeout

### Database Row Limit : int

* `<dbrowlimit>`
* DbRowLimit

### Row Limit Step Size : int v2017.2+

* `<dbrowlimitstepsize>`
* DbRowLimitStepSize

### Disable Non-Joined Data Objects : bool

* `<detectjoinedobjects>`
* IsDetectJoinedObjects

### Enable Special Cartesian Processing : bool

* `<enablespecialcartesianprocessing>`
* IsEnableSpecialCartesianProcessing

### Aggregate and Group in Database : bool

* `<aggregateandgroupindatabase>`
* IsAggregateAndGroupInDatabase

### Convert Formula Filters and Sorts to SQL v2018.2–2020.1

### Convert Formulas to SQL v2020.1+

* `<evaluateformulasindatabase>`
* EvaluateFormulasInDatabase

## Scheduler Settings

The **[Scheduler Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281608723095-Scheduler-Settings)** topic includes detailed descriptions of each of these settings.

### Enable Report Scheduling : bool

* `<enablescheduling>`
* IsEnableScheduling

### Show Report Scheduling Option : bool

* `<showschedulereports>`
* IsShowScheduleReports

### Show Email Report Options : bool

* `<showschedulereportsemail>`
* IsShowScheduleReportsEmail

### Show Schedule Reports Manager : bool

* `<showschedulereportsmanager>`
* IsShowScheduleReportsManager

### Show Schedule No End Date Option : bool

* `<showschedulenoenddate>`
* IsShowScheduleNoEndDate

### Show Schedule Intraday Recurrence Option : bool

* `<showscheduleintradayrecurrence>`
* IsShowScheduleIntradayRecurrence

### Scheduler Manager User View Level : constant

Possible values: *User, Company, All*

* `<schedulemanagerviewlevel>`
* ScheduleManagerViewLevel

### Email Scheduled Reports : bool

* `<emailscheduledreports>`
* IsEmailScheduledReports

### Enable Batch Reports : bool

* `<enablebatchreports>`
* IsEnableBatchReports

### Show Schedule Delivery Type Options : bool

* `<showscheduledeliverytypeoptions>`
* IsShowScheduleDeliveryTypeOptions

### Use Secure Scheduler Remoting Channel : bool

* `<usesecureremotingchannel>`
* IsUseSecureRemotingChannel

### Schedule Remoting Host : string

* `<scheduleremotinghost>`
* ScheduleRemotingHost

### Enable Remote Report Execution : bool

* `<executeremotely>`
* IsExecuteRemotely

### Enable Execution Cache : bool

* `<executioncache>`
* UseExecutionCache

### User Cache Visibility Level : constant v2017.3+

Possible values: *Global*, *Company*, *User*

* `<cachevisibilitylevel>`
* CacheVisibilityLevel

### Enable Access to Data Sources Remotely : bool

* `<accessdatasourcesremotely>`
* IsAccessDataSourcesRemotely

### Remote Execution Remoting Host : string

* `<synchronousremotinghost>`
* SynchronousRemotingHost

### Custom Queue Service : string

* `<schedulerqueueservice>`
* SchedulerQueueService

### Delete Schedules upon Report Deletion : bool

* `<deleteschedulesuponreportdeletion>`
* IsDeleteSchedulesUponReportDeletion

### Default Email Subject : string

* `<reportscheduleemailsubject>`
* ReportScheduleEmailSubject

### Default Email Body : string

* `<reportscheduleemailbody>`
* ReportScheduleEmailBody

### Password Requirements (for pdf and excel documents) : string

* `<passwordrequirement>`
* PasswordRequirement

### Custom Scheduler Recipient Window : string

* `<schedulerrecipientwindow>`
* SchedulerRecipientWindow

## User Settings

The **[User Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281636299927-User-Settings)** topic includes detailed descriptions of each of these settings.

### User Preference Storage Method : [wrUserPreferenceStorage](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrUserPr)

* `<userprefstorage>`
* UserPreferenceStorage

### Startup Report(s) Replace Getting Started : bool

* `<userstartupreportoverwritegettingstarted>`
* UserStartupReportOverwriteGettingStarted

### Maximum Number of Startup Reports : int

* `<userstartupreportmaxnum>`
* UserStartupReportMaxNum

### Allow User Reports : bool

* `<userallowuserreports>`
* UserAllowUserReports

## Other Settings

The **[Other Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281608505879-Other-Settings)** topic includes detailed descriptions of each of these settings.

### Excel Export Target : constant

Possible values: *v2003, v2007, v2010, v2013, v2016*. *v2013* is the default value.

* `<excelexporttarget>`
* ExcelExportTarget

### External Interface : string

* `<externalinterface>`
* ExternalInterface

### Enable Paging in Report Viewer : bool

* `<htmlpaging>`
* IsHtmlPaging

### Renew Session Automatically : bool

* `<renewsession>`
* IsRenewSession

### Write Log File : bool pre-v2017.2

* `<writelog>`
* IsWriteLog

### Write Log File : constant v2017.2+

Possible values: *NONE, ERROR, INFO, DEBUG*

* `<logginglevel>`
* LoggingLevel

### Enable Debugging : bool

* `<debugging>`
* IsDebugging

### Max Report Execution Time (minutes) : int

* `<maxjobexecutionminutes>`
* MaxJobExecutionMinutes

### Max Chained Report Collation Executions : int v2021.1.8+

* `chainedreportmaxcollationexecutions>`
* ChainedReportMaxCollationExecutions

### Maximum Age for Temp Files : int

* `<maxtempfileage>`
* MaxTempFileAge

### Enable Web Service / Assembly Data Mapping : bool

* `<datamapping>`
* IsDataMapping

### Limit Reports and Visualizations to One Category : bool pre-v21021.1

### Limit Reports and Visualizations to One Object : bool v2021.1+

* `<onecategorylimit>`
* IsOneCategoryLimit

### Run Aggregate Functions at Record Level by Default : bool

* `<isaggregaterecordlevel>`
* IsAggregateRecordLevel

### Cache External Services : bool

* `<cacheservices>`
* IsCacheServices

### Global Schema Access Type : constant

Possible values: *Datasource, Metadata*

* `<schemaaccesstype>`
* SchemaAccessType

### Allow Multiple Sessions : bool

* `<allowmultiplesessions>`
* AllowMultipleSessions

### Allow MD5 Hashing on FIPS server : bool

* `<allowmd5onfips>`
* AllowMD5OnFIPS

### Write BOM to CSV Files v2019.1.1+

* `<writebomtocsv>`
* WriteBOMToCSV

### Enable Report List Caching : bool pre-v2020.1

* `<reportlistcacheenabled>`
* IsReportListCacheEnabled

### Enable Report XML Caching :  bool pre-v2020.1

* `<reportxmlcacheenabled>`
* IsReportXmlCacheEnabled

### Report XML Caching Timeout (s) : int pre-v2020.1

* `<reportxmlcachetimeout>`
* ReportXmlCacheTimeout

### ‘LoadImage’ Cell Function Parameter Prefix : string

* `<loadimageprefix>`
* LoadImageFuncParamPrefix

### Ignore Inaccessible Report Folders : bool

* `<ignoreinaccessiblereportfolders>`
* IgnoreInaccessibleReportFolders

### User ID : string

* `<userid>`
* UserId

### Password : string

* `<password>`
* Password

### Debug Password : string

* `<debugextractionpassword>`
* DebugExtractionPassword

### REST Key : string v2017.3+

* `<restkey>`
* RestKey

### Exago Expiration Date : string

* `<expirationdate>`
* ExpirationDate

### Custom Code Supplied by Exago : bool

* `<customcode>`
* CustomCode

### License Key : string

* <licensekey>
* LicenseKey

## Hidden Flags

Some settings are not accessible in the **Admin Console** and are only available by editing the Config File. These so called hidden flags are documented in the  **[Hidden Flags](https://devnet.logianalytics.com/hc/en-us/articles/5281607060631-Hidden-Flags)** topic.

## Unsupported

These settings are not accessible in the **Admin Console**. Changing these settings is not supported.

### Formula functions loaded : bool v2017.2+

* `<formulafunctionsloaded>`
* AreFormulaFunctionsLoaded

### Date functions loaded : bool

* `<datefunctionsloaded>`
* AreDateFunctionsLoaded

### Version Number : string

* `<versionnumber>`
* VersionNumber

### Data Cloud Service : string

* `<datacloudservice>`
* DataCloudService

### *Window Height* : int

* `<windowheight>`
* WindowHeight

### *Window Width* : int

* `<windowwidth>`
* WindowWidth

### *Map Terms Signature* : string

* `<maptermssignature>`
* MapTermsSignature

### *Join Transform Objects in Database*: bool v2018.1+

* `<canjointransformobjectsindb>`
* CanJoinTransformObjectsInDb
