---
title: "IAdHocExtension"
id: 4415504593303
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504593303-IAdHocExtension
updated_at: 2022-06-22T15:08:15Z
---

# IAdHocExtension

# IAdHocExtension

**IAdHocExtension** interface in Izenda.BI.Framework.CustomConfiguration defines the extension APIs that allows customization code to hook in the report life cycle.

| Customized Behavior | Method & Sample | Description |
| --- | --- | --- |
| Filter data tree lookup | [OnPreLoadFilterDataTree](#_bm) | Allows customizing the tree of filter values displayed for selection under Report Designer filter fields, Equals (Tree) dropdown menu. This has extra report filter settings, which contains the other filter values selected by the user in the report. This allows for easy set up of cascading behavior in your custom code. If this is implemented OnLoadFilterDataTree will be ignored. |
| Filter data tree lookup (To be deprecated in 3.0.0) | [OnLoadFilterDataTree](#_bm2) | Allows customizing the tree of filter values displayed for selection under Report Designer filter fields, Equals (Tree) dropdown menu. This will be deprecated in favor of OnPreLoadFilterDataTree, please make plans to convert to this implementation prior to release of 3.0.0. |
| Customize filter data tree lookup results | [OnPostLoadFilterDataTree](#_bm3) | Allows override of the filter tree just before the results are returned to the user. |
| Filter data | [OnPreLoadFilterData](#_bm4) | Allows injecting report filter data instead of querying the database. |
| Filter data display | [OnPostLoadFilterData](#_bm5) | Allows overriding filter values displayed for selection under Report Designer filter fields. |
| ReportDefinition object | [OnPreExecute](#_bm6) | Allows on-the-fly customization of the report content. |
| Data source query tree | [OnExecuting](#_bm6) | Allows customizing the data source query tree. |
| Data source query results | [OnPostExecute](#_bm7) | Allows customizing the execution result of data source queries. |
| Hidden report filters | [SetHiddenFilters](#_bm21) | Adds customized filters to reports while hiding them from UI users. |
| Custom In Time Period Filters | [CustomTimePeriod](#_bm12) | Adds custom In Time Period Filter Values. |
| Load Custom Data Format | [LoadCustomDataFormat](#_bm13) | Adds custom data formats for specified data types. |
| WebUrlResolver | [IWebUrlResolver](#_bm14) | Allow overriding the DefaultWebUrlResolver and customizing the way the application generates the Front End URL. |
| Color themes | [GetThemes](#_bm15) | Get defined color themes for Chart, Gauge, and Map (v2.9.0 or higher). |
| HTTP requests to REST API service initiated by REST Connector | [OnPreRestApiRequest](#_bm16) | Allows modify HTTP requests to REST API service initiated by REST Connector (v3.10.0 or higher). |
| SQL query | [ModifyQuery](#_bm17) | Allows modify SQL queries (v3.10.0 or higher). |
| Load Custom Functions | [LoadCustomFuntions](#h_01G617MG9PM9D4AY5QVV18EW3G) | Adds .NET implementation of Custom Functions which have been whitelisted in CustomFunctionFilePath |

The companion wrapper class **DefaultAdHocExtension** in Izenda.BI.Framework.CustomConfiguration should be used as the base class for customization.

![../_images/DefaultAdHocExtension_class.png](https://devnet.logianalytics.com/hc/article_attachments/4415504313367/defaultadhocextension_class.png)

See also: [Full-code Samples for all IAdHocExtension Methods](https://devnet.logianalytics.com/hc/en-us/articles/4415504577815-IAdHocExtension-Samples)

## OnPreLoadFilterDataTree

`List<ValueTreeNode>OnPreLoadFilterDataTree(ReportFilterFieldfilterField,ReportFilterSettingfilterSetting,outboolhandled)`

This method customizes the behavior of [POST report/loadFilterFieldDataAsTree](https://devnet.logianalytics.com/hc/en-us/articles/4415504673047-Report-Designer-Filters-APIs#POST) and [POST dashboard/loadFilterFieldDataAsTree](https://devnet.logianalytics.com/hc/en-us/articles/4415504639639-Dashboard-Designer-APIs#POST2) APIs.

> ```
> publicoverrideList<ValueTreeNode>OnPreLoadFilterDataTree(ReportFilterFieldfilterField,ReportFilterSettingfilterSetting,outboolhandled){handled=false;varresult=newList<ValueTreeNode>();varshipCountry=filterSetting.FilterFields.FirstOrDefault(f=>f.SourceFieldName=="ShipCountry");if(filterField.SourceFieldName=="ShipCity"&&shipCountry!=null){if(shipCountry.Value=="Argentina"){handled=true;varrootNode=newValueTreeNode{Text="[All]",Value="[All]"};rootNode.Nodes=newList<ValueTreeNode>();rootNode.Nodes.Add(newValueTreeNode{Text="Buenos Aires",Value="Buenos Aires"});rootNode.Nodes.Add(newValueTreeNode{Text="Mendoza",Value="Mendoza"});rootNode.Nodes.Add(newValueTreeNode{Text="Salta",Value="Salta"});result.Add(rootNode);}}returnresult;}
> ```

## OnLoadFilterDataTree

`List<ValueTreeNode>OnLoadFilterDataTree(QuerySourceFieldInfofieldInfo)`

This method customizes the behavior of [POST report/loadFilterFieldDataAsTree](https://devnet.logianalytics.com/hc/en-us/articles/4415504673047-Report-Designer-Filters-APIs#POST) and [POST dashboard/loadFilterFieldDataAsTree](https://devnet.logianalytics.com/hc/en-us/articles/4415504639639-Dashboard-Designer-APIs#POST) APIs.

For example, the API can be customized to return a list of cities per country in a hierarchy like this:

```
All+--Argentina+--BuenosAires+--France+--Lille+--Lyon+--Marseille
```

Sample code to display All > South America and North America for Manager role:

> ```
> [Export(typeof(IAdHocExtension))]publicclassAdHocExtensionSample:DefaultAdHocExtension{publicoverrideList<ValueTreeNode>OnLoadFilterDataTree(QuerySourceFieldInfofieldInfo){varresult=newList<ValueTreeNode>();if(fieldInfo.QuerySourceName=="OrderDetailsByRegion"&&fieldInfo.Name=="CountryRegionName"&&HttpContext.Current.User.IsInRole("Manager")){// Node [All] is required for UI to render.varrootNode=newValueTreeNode{Text="[All]",Value="[All]"};rootNode.Nodes=newList<ValueTreeNode>();rootNode.Nodes.Add(newValueTreeNode{Text="South America",Value="South America"});rootNode.Nodes.Add(newValueTreeNode{Text="North America",Value="North America"});result.Add(rootNode);}returnresult;}}
> ```

## OnPostLoadFilterDataTree

`List<ValueTreeNode>OnPostLoadFilterDataTree(ReportFilterFieldfilterField,List<ValueTreeNode>data,ReportFilterSettingfilterSetting)`

This method customizes the behavior of [POST report/loadFilterFieldDataAsTree](https://devnet.logianalytics.com/hc/en-us/articles/4415504673047-Report-Designer-Filters-APIs#POST) and [POST dashboard/loadFilterFieldDataAsTree](https://devnet.logianalytics.com/hc/en-us/articles/4415504639639-Dashboard-Designer-APIs#POST) APIs.

> ```
> publicoverrideList<ValueTreeNode>OnPostLoadFilterDataTree(ReportFilterFieldfilterField,List<ValueTreeNode>data,ReportFilterSettingfilterSetting){varshipCountry=filterSetting.FilterFields.FirstOrDefault(f=>f.SourceFieldName=="ShipCountry");if(filterField.SourceFieldName=="ShipCity"&&shipCountry!=null){if(shipCountry.Value=="Argentina"){varrootNode=data[0];rootNode.Nodes.Add(newValueTreeNode{Text="La Plata - After",Value="La Plata"});}}returndata;}
> ```

## OnPreLoadFilterData

`List<string>OnPreLoadFilterData(ReportFilterSettingfilterSetting,outboolhandled)`

This method allows injecting report filter data instead of querying the database.

* if `handled` is false (not set), system will ignore the output and query the database for filter values.
* if `handled` is set to true, system will take the output as filter values and skip the database query.

For example, it can be used to:

* skip time-consuming database queries when the list of values is predictable: true and false, list of regions (although there is no warranty that the injected values actually have data in the database)
* disable filtering by returning null in some conditions

Sample code to use a pre-defined list for filters on OrdersByRegion.CountryRegionName:

```
[Export(typeof(IAdHocExtension))]publicclassAdHocExtensionSample:DefaultAdHocExtension{publicoverrideList<string>OnPreLoadFilterData(ReportFilterSettingfilterSetting,outboolhandled){handled=false;List<String>result=null;if(filterSetting.FilterFields.Count==1&&filterSetting.FilterFields.Any(x=>x.SourceDataObjectName.Equals("OrdersByRegion")&&x.SourceFieldName.Equals("CountryRegionName"))){handled=true;result=newList<string>(){"Europe","North America","South America"};}returnresult;}}
```

## OnPostLoadFilterData

`List<string>OnPostLoadFilterData(ReportFilterFieldfilterField,List<string>data)`

This method allows overriding filter values displayed for selection under Report Designer filter fields.

For example, it can be used to: \* do a secondary lookup on filter values returned from system to add more information such as appending population to city names \* format values returned from system for example to proper case or title case \* add or remove values from the list

Sample code to change Europe to EU for Employee role:

```
[Export(typeof(IAdHocExtension))]publicclassAdHocExtensionSample:DefaultAdHocExtension{publicoverrideList<string>OnPostLoadFilterData(ReportFilterFieldfilterField,List<string>data){// override dropdown value based on user role for filter on view "OrderDetailsByRegion" and field "CountryRegionName"if(filterField.SourceDataObjectName=="OrderDetailsByRegion"&&filterField.SourceFieldName=="CountryRegionName"&&HttpContext.Current.User.IsInRole("Employee")){varindexEU=data.IndexOf("Europe");if(indexEU!=-1)data[indexEU]="EU";}returnbase.OnPostLoadFilterData(filterField,data);}}
```

## OnPreExecute

`ReportDefinitionOnPreExecute(ReportDefinitionreportDefinition)`

This method allows customizing the report content on the fly before it is run.

For example, it can be used to:

* customize the data sources, relationships, filters and calculated fields
* customize the report parts settings

Sample code to remove all Map report parts on-the-fly:

```
[Export(typeof(IAdHocExtension))]publicclassAdHocExtensionSample:DefaultAdHocExtension{publicoverrideReportDefinitionOnPreExecute(ReportDefinitionreport){if(report.ReportPart.Any(x=>x.ReportPartContent.Type==ReportPartContentType.Map)){varfilteredReportPart=report.ReportPart.Where(x=>x.ReportPartContent.Type!=ReportPartContentType.Map).ToList();report.ReportPart=filteredReportPart;}returnreport;}}
```

## OnExecuting

`QueryTreeOnExecuting(QueryTreequeryTree)`

This method allows customizing the data source queries on the fly before it is run.

For example, it can be used to:

* inspect the query steps
* customize the operations such as adding a limit operator or re-ordering the sequence

![../_images/QueryTree_Sample.png](https://devnet.logianalytics.com/hc/article_attachments/4415492428311/querytree_sample.png)

Sample code to log all operations without a result limit operator:

```
[Export(typeof(IAdHocExtension))]publicclassAdHocExtensionSample:DefaultAdHocExtension{publicoverrideQueryTreeOnExecuting(QueryTreequeryTree){varnodeVisitor=newQueryTreePathAnalyzeVisitor(newExtensibilityFactory(),queryTree.ContextData);nodeVisitor.ContextData=queryTree.ContextData;queryTree.Root.Accept(nodeVisitor);varresultLimitOperator=newResultLimitOperator(){ChildOperand=newOperand(){QuerySource=newQuerySource()}};try{nodeVisitor.Visit(resultLimitOperator);}catch(Exception){Console.WriteLine("LOG: Query with no limit");}returnqueryTree;}}
```

## OnPostExecute

`List<IDictionary<string,object>>OnPostExecute(QueryTreeexecutedQueryTree,List<IDictionary<string,object>>result)`

This method allows customizing the execution result of data source queries.

For example, it can be used to: \* inspect the execution result \* alter the execution result such as adding and removing rows or changing data values

Sample code to limit the execution result to the first 1000 rows only (although the database may return more than that):

```
[Export(typeof(IAdHocExtension))]publicclassAdHocExtensionSample:DefaultAdHocExtension{publicoverrideList<IDictionary<string,object>>OnPostExecute(QueryTreeexecutedQueryTree,List<IDictionary<string,object>>result){returnresult.Take(1000).ToList();}}
```

## SetHiddenFilters

`ReportFilterSettingSetHiddenFilters(SetHiddenFilterParamparam)`

This method adds customized filters to every reports while hiding them from UI users.

For example, it can be used to:

* filter data to rows with ShipRegion = ‘WA’ or BLANK only.
* automatically filter all tables to non-deleted data (IsDeleted = FALSE).
* in a Shared Schema Multi-Tenant Architecture, filter every table to only data of the tenant of current logged in user.

Sample code to add hidden filter ShipRegion = “WA” or “[Blank]” for all:

```
[Export(typeof(IAdHocExtension))]
						public override ReportFilterSetting SetHiddenFilters(SetHiddenFilterParam param)
						{
						var filterFieldName = "ShipRegion";
						Func<ReportFilterSetting, int, QuerySource, QuerySourceField, Guid, Relationship, int> addHiddenFilters = (result, filterPosition, querySource, field, equalOperator, rel) =>
						{
						var firstFilter = new ReportFilterField
						{
						Alias = $"ShipRegion{filterPosition}",
						QuerySourceId = querySource.Id,
						SourceDataObjectName = querySource.Name,
						QuerySourceType = querySource.Type,
						QuerySourceFieldId = field.Id,
						SourceFieldName = field.Name,
						DataType = field.IzendaDataType,
						Position = ++filterPosition,
						OperatorId = equalOperator,
						Value = "WA",
						RelationshipId = rel?.Id,
						IsParameter = false,
						ReportFieldAlias = null
						};
						var secondFilter = new ReportFilterField
						{
						Alias = $"ShipRegion{filterPosition}",
						QuerySourceId = querySource.Id,
						SourceDataObjectName = querySource.Name,
						QuerySourceType = querySource.Type,
						QuerySourceFieldId = field.Id,
						SourceFieldName = field.Name,
						DataType = field.IzendaDataType,
						Position = ++filterPosition,
						OperatorId = equalOperator,
						Value = "[Blank]",
						RelationshipId = rel?.Id,
						IsParameter = false,
						ReportFieldAlias = null
						};
						result.FilterFields.Add(firstFilter);
						result.FilterFields.Add(secondFilter);
						var logic = $"({filterPosition - 1} OR {filterPosition})";
						if (string.IsNullOrEmpty(result.Logic))
						{
						result.Logic = logic;
						}
						return filterPosition;
						};
						var filterSetting = new ReportFilterSetting()
						{
						FilterFields = new List<ReportFilterField>()
						};
						var position = 0;
						var ds = param.ReportDefinition.ReportDataSource;
						// Build the hidden filters for ship country fields
						foreach (var querySource in param.QuerySources // Scan thru the query sources that are involved in the report
						.Where(x => x.QuerySourceFields.Any(y => y.Name.Equals(filterFieldName, StringComparison.OrdinalIgnoreCase)))) // Take only query sources that have filter field name
						{
						// Pick the relationships that joins the query source as primary source
						// Setting the join ensure the proper table is assigned when using join alias in the UI
						var rels = param.ReportDefinition.ReportRelationship.
						Where(x => x.JoinQuerySourceId == querySource.Id)
						.ToList();
						// Count the relationships that the filter query source is foreign query source
						var foreignRelCounts = param.ReportDefinition.ReportRelationship
						.Where(x => x.ForeignQuerySourceId == querySource.Id)
						.Count();
						// Find actual filter field in query source
						var field = querySource.QuerySourceFields.FirstOrDefault(x => x.Name.Equals(filterFieldName, StringComparison.OrdinalIgnoreCase));
						// Pick the equal operator
						var equalOperator = Izenda.BI.Framework.Enums.FilterOperator.FilterOperator.EqualsManualEntry.GetUid();
						// In case there is no relationship that the query source is joined as primary
						if (rels.Count() == 0)
						{
						// Just add hidden filter with null relationship
						position = addHiddenFilters(filterSetting, position, querySource, field, equalOperator, null);
						}
						else
						{
						// Add another hidden filter for query source that appears in both alias primary and foreign query source of relationships.
						// This step is mandatory because when aliasing a primary query source, it becomes another instance of query source in the query.
						// So if we only add filter for alias, the original query source instance will not be impacted by the filter. That's why we need
						// to add another filter for original instance when it appears in both side of alias and foreign.
						// For example:
						//          [Order] LEFT JOIN [Employee]
						//      [Aliased Employee] LEFT JOIN [Department]
						// If the system needs to add a hidden filter to [Employee], for example: [CompanyId] = 'ALKA'
						// It needs to add
						//          [Employee].[CompanyId] = 'ALKA' AND [Aliased Employee].[CompanyId] = 'ALKA'
						// By this way, it ensures all [Employee] instances are filtered by ALKA company id.
						if (foreignRelCounts > 0)
						{
						position = addHiddenFilters(filterSetting, position, querySource, field, equalOperator, null);
						}
						foreach (var rel in rels)
						{
						// Loop thru all relationships that the query source is joined as primary and add the hidden field associated with each relationship
						position = addHiddenFilters(filterSetting, position, querySource, field, equalOperator, rel);
						}
						}
						}
						return filterSetting;
						}
					
```

## Application Scenarios

Hidden filters can be applied based on several values. For example,

User Name:

```
varcurrentUser=UserContext.Current;varcurrentUserName=currentUser.CurrentUser.UserName;if(String.Compare(currentUserName,"userName")==0){//FilterLogicGoesHere}
```

Tenant Name:

```
varcurrentUser=UserContext.Current;varcurrentTenantName=currentUser.CurrentTenant.Name;if(String.Compare(currentTenantName,"TestTenant")==0){//FilterLogicGoesHere}
```

Role Name:

```
var currentUser = UserContext.Current;
						var currentUserRoles = currentUser.Roles.Select(x => x.Name).ToList();
						if (String.Compare(currentUserRoles[0], “Administrator”) == 0)
						{
						//Filter Logic Goes Here
						}
					
```

Role Name (Alternative Method):

```
varcurrentUser=UserContext.Current;if(currentUser.IsInRole("Administrator"){//FilterLogicGoesHere}
```

Schema Notation:

```
publicoverrideReportFilterSettingSetHiddenFilters(SetHiddenFilterParamparam){varqueryCategory=param.QuerySources.First(x=>x.Name.Equals("Orders")).QuerySourceCategoryName;if(String.Compare(queryCategory,"dbo")==0){//FilterLogicGoesHere}}
```

Query Source:

```
publicoverrideReportFilterSettingSetHiddenFilters(SetHiddenFilterParamparam){varquerySouce=param.QuerySources.First(x=>x.Name.Equals("TableName"));if(String.Compare(querySource.Type,"Table")==0){//FilterLogicGoesHere}}
```

## Applying Filter with Compounded Values

In some scenarios, you will require several values passed into the same filter, which get applied according to the logic you provide.

```
if(String.Compare(currentUserName,"userName")==0){result.Logic="(1 or 2 or 3)";//The logic, something like "1 AND 2 OR 3"//Equal operatorvarequalOperator=param.FilterOperatorGroups.First(x=>x.Name.Equals("Equivalence")).FilterOperators.First(x=>x.Name.Equals("Equals (Selection)"));//Filter Order.ShipContry = USAstring[]valArray={"USA","Argentina","Germany"};varquerySouce=param.QuerySources.First(x=>x.Name.Equals("Orders"));varfield=querySouce.QuerySourceFields.First(x=>x.Name.Equals("ShipCountry"));for(inti=0;i<valArray.Length;i++){varreportFilterField=newReportFilterField{QuerySourceId=querySouce.Id,SourceDataObjectName=querySouce.Name,QuerySourceType=querySouce.Type,QuerySourceFieldId=field.Id,SourceFieldName=field.Name,DataType=field.DataType,Position=i+1,OperatorId=equalOperator.Id,Value=valStr[i],RelationshipId=null,IsParameter=false,ReportFieldAlias=null};filterFields.Add(reportFilterField);}}
```

## CustomTimePeriod

`publicoverrideList<CustomTimePeriod>LoadCustomTimePeriod()`

NOTE: This method is only available in v1.24.0 or higher

You can create custom time period filters for various datatypes by overriding the LoadCustomTimePeriod in your DefaultAdHocExtension implementation.

```
usingOperator=Izenda.BI.Framework.Enums.DateTimeOperator;[Export(typeof(IAdHocExtension))]publicclassCustomAdhocReport:DefaultAdHocExtension{publicoverrideList<CustomTimePeriod>LoadCustomTimePeriod(){varresult=newList<CustomTimePeriod>{newCustomTimePeriod("Tomorrow",DateTime.Now,DateTime.Now.AddDays(1),Operator.BetweenDateTime),newCustomTimePeriod("Previous Date -> DateTime Now",()=>DateTime.Now.AddDays(-1),()=>DateTime.Now,Operator.BetweenDateTime),newCustomTimePeriod("Less Than 2 Days Old",2,Operator.LessThanDaysOld),newCustomTimePeriod("Greater Than 2 Days Old",()=>2,Operator.GreaterThanDaysOld),newCustomTimePeriod(">= Date Time Now + 2 Days",DateTime.Now.AddDays(2),Operator.GreaterThanOrEqualsCalender),newCustomTimePeriod("<= Date Time Now - 2 Days",()=>DateTime.Now.AddDays(-2),Operator.LessThanOrEqualsCalendar)};returnresult;}}
```

## LoadCustomDataFormat

`publicoverrideList<DataFormat>LoadCustomDataFormat()`

Note

* This method is only available in v1.24.0 or higher.
* You can create custom formats for various datatypes by overriding the LoadCustomDataFormat in your DefaultAdHocExtension implementation.
* From v2.6.19, [DataFormat](https://devnet.logianalytics.com/hc/en-us/articles/4415504710423-DataFormat) object has 1 new field: JsFormatString
  + JsFormatString is used for optimizing chart axes lables
  + If DataFormat contains both FormatFunc and JsFormatString, the JsFormatString will be more precede.
* New in v2.6.20, if JsFormatString does not contain braces {} that means the value of jsFormatString is the name of the funtion will be obtained in the FE to apply in the chart.  
  User must ensure to register the format function by using [Front-end integration API: addJsFormat(formatName, formatFunction)](https://devnet.logianalytics.com/hc/en-us/articles/4415492642455-Front-end-Integration-APIs#addJsFormat(formatName,_formatFunction)).

```
/// <summary>/// Loads the defined custom formats into the Izenda application////// <see href="https://msdn.microsoft.com/en-us/library/dwhawy9k(v=vs.110).aspx">Standard Numeric Format Strings</see>/// </summary>/// <returns>A list of custom formats. </returns>publicoverrideList<DataFormat>LoadCustomDataFormat(){varresult=newList<DataFormat>{newDataFormat{Name="By Hour",DataType=DataType.DateTime,Category=IzendaKey.CustomFormat,FormatFunc=(x)=>{return((DateTime)x).ToString("M/d/yyyy h:00 tt");}},newDataFormat{Name="dd MM:mm",DataType=DataType.DateTime,Category=IzendaKey.CustomFormat,FormatFunc=(x)=>{vardate=Convert.ToDateTime(x);returndate.ToString("dd HH:mm");}},newDataFormat{Name="dd HH:mm:ss",DataType=DataType.DateTime,Category=IzendaKey.CustomFormat,FormatFunc=(x)=>{vardate=Convert.ToDateTime(x);returndate.ToString("dd HH:mm:ss");}},newDataFormat{Name="dd mm:ss",DataType=DataType.DateTime,Category=IzendaKey.CustomFormat,FormatFunc=(x)=>{vardate=Convert.ToDateTime(x);returndate.ToString("dd mm:ss");}},newDataFormat{Name="£0,000",DataType=DataType.Numeric,Category=IzendaKey.CustomFormat,FormatFunc=(x)=>{return((decimal)x).ToString("C0",CultureInfo.CreateSpecificCulture("en-GB"));}},newDataFormat{Name="¥0,000",DataType=DataType.Numeric,Category=IzendaKey.CustomFormat,FormatFunc=(x)=>{return((decimal)x).ToString("C0",CultureInfo.CreateSpecificCulture("ja-JP"));}},newDataFormat{Name="0,000",DataType=DataType.Numeric,Category=IzendaKey.CustomFormat,FormatFunc=(x)=>{returnString.Format(CultureInfo.InvariantCulture,"{0:0,0}",x);}},newDataFormat{Name="$0,000",DataType=DataType.Numeric,Category=IzendaKey.CustomFormat,FormatFunc=(x)=>{returnString.Format(CultureInfo.InvariantCulture,"${0:0,0}",x);}},newDataFormat{Name="HH:MM:SS",DataType=DataType.Numeric,Category=IzendaKey.CustomFormat,FormatFunc=(x)=>{varnewValue=Convert.ToDouble(x);TimeSpantime=TimeSpan.FromSeconds(newValue);returntime.ToString(@"dd\.hh\:mm\:ss");}}// Note: new in version 2.6.19// Custom DataFormat use JsFormatStringnewDataFormat{Name="2f km",//example: 2.00 km.DataType=DataType.Numeric,Category=IzendaKey.CustomFormat,JsFormatString="{value:.2f} km."},newDataFormat{Name="millisecond",DataType=DataType.DateTime,Category=IzendaKey.CustomFormat,JsFormatString="{value:%A, %b %e, %H:%M:%S.%L}",//A: Day of week//B: Month//b: Abbreviations of Month//e: Day//H: Hour//M: Minute//S: Second//L: MillisecondFormatDataType=DataType.DateTime},newDataFormat{Name="second",DataType=DataType.DateTime,Category=IzendaKey.CustomFormat,JsFormatString="{value:%H:%M:%S}",//H: Hour//M: Minute//S: SecondFormatDataType=DataType.DateTime},newDataFormat{Name="minute",DataType=DataType.DateTime,Category=IzendaKey.CustomFormat,JsFormatString="{value:%M}",FormatDataType=DataType.DateTime},newDataFormat{Name="hour",DataType=DataType.DateTime,Category=IzendaKey.CustomFormat,JsFormatString="{value:%H:%M}",},newDataFormat{Name="day",DataType=DataType.DateTime,Category=IzendaKey.CustomFormat,JsFormatString="{value:%A, %B %e, %Y}",//A: Day of week//B: Month//Y: YearFormatDataType=DataType.DateTime},newDataFormat{Name="week",DataType=DataType.DateTime,Category=IzendaKey.CustomFormat,JsFormatString="Week from {value:%A, %B %e, %Y}",//A: Day of week//B: Month//Y: YearFormatDataType=DataType.DateTime},newDataFormat{Name="month",DataType=DataType.DateTime,Category=IzendaKey.CustomFormat,JsFormatString="{value:%B %Y}",FormatDataType=DataType.DateTime},newDataFormat{Name="year",DataType=DataType.DateTime,Category=IzendaKey.CustomFormat,JsFormatString="Year {value:%Y}",FormatDataType=DataType.DateTime}//new in version 2.6.20newDataFormat{Name="2f km",//example: 2.00 km.DataType=DataType.Numeric,Category=IzendaKey.CustomFormat,JsFormatString="1k"//The name of the js format function}};returnresult;}
```

## IWebUrlResolver

`publicoverrideIWebUrlResolverWebUrlResolver=>newCustomWebUrlResolver();`

NOTE: This method is only available in v2.6.9 or higher

This property will allow you to override the DefaultWebUrlResolver and customize the way the application generates the Front End URL. This can be used when sending report and dashboard links via emails, schedules and subscriptions. Additionally you can now customize the URLS for ViewReport, ViewDashboard, ViewReportPart, etc.

Step 1: Implement IWebUrlResolver or inherit from DefaultWebUrlResolver

```
public class CustomWebUrlResolver : DefaultWebUrlResolver
						{
						private readonly ILog logger;
						public CustomWebUrlResolver()
						{
						this.logger = (new LogManager()).GetLogger<CustomWebUrlResolver>();
						}
						public override string ResolveUrl(string baseUrl, WebUrlActionLink action, Guid? id, Dictionary<string, object> parameters = null)
						{
						logger.Info($"Resolving the url of {action} on base url {baseUrl}");
						// Put logic to custom the web url here
						return base.ResolveUrl(baseUrl, action, id, parameters);
						}
						}
					
```

Step 2: Override WebUrlResolver property of DefaultAdhocExtension

```
[Export(typeof(IAdHocExtension))]publicclassCustomAdhocReport:DefaultAdHocExtension{publicoverrideIWebUrlResolverWebUrlResolver=>newCustomWebUrlResolver();}
```

## GetThemes

`publicoverrideList<Theme>GetThemes()`

This method customizes the behavior of [GET systemSetting/themes](https://devnet.logianalytics.com/hc/en-us/articles/4415511971863-System-Configuration-APIs#get-systemsetting-themes) API.

```
publicoverrideList<Theme>GetThemes(){returnnewList<Theme>{newTheme{Name="Classic",Colors=newList<string>{"#F9EA15","#F9EA15","#B4D335","#B4D335","#35B24D","#128076","#2C5AA8","#2C3185","#332A7B","#981E5B","#EE1D26","#F04323",}}};}
```

## OnPreRestApiRequest

`RESTRequestOnPreRestApiRequest(RESTRequestrequest,RESTContextcontext)`

This method allows modify the HTTP request to REST API service initiated by REST Connector on the fly before it is sent.

### RESTRequest Object

| Field | NULL | Description |
| --- | --- | --- |
| **Url** string |  | URL of the current request |
| **RequestBody** string | Y | Request Body of the current request |

### RESTContext Object

| Field | NULL | Description |
| --- | --- | --- |
| **QuerySourceName** string | Y | The query source name |
| **ConnectorInfo** object |  | The [RESTConnectorInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504785815-RESTConnectorInfo) object |
| **EndpointInfo** object |  | The [RESTEndpointInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415492877335-RESTEndpointInfo) object |
| **UserContext** object |  | The [UserContext.Current](https://devnet.logianalytics.com/hc/en-us/articles/4415504804887-UserContext) object contains data of the current logged in user |
| **ReportDefinition** object | Y | The [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492852759-ReportDefinition) object |

Sample code to add a query parameter based on the selected filter value:

```
[Export(typeof(IAdHocExtension))]
							public class AdHocExtensionSample : DefaultAdHocExtension
							{
							public override RESTRequest OnPreRestApiRequest(RESTRequest request, RESTContext context)
							{
							if (context.ReportDefinition != null)
							{
							var filterFields = context.ReportDefinition.ReportFilter.FilterFields;
							if(filterFields.Count > 0)
							{
							var filterValue = filterFields[0].Value;
							if (!string.IsNullOrEmpty(filterValue))
							request.Url += $"?filter={filterValue}";
							}
							}
							return request;
							}
							}
						
```

## ModifyQuery

`stringModifyQuery(stringquery,stringdatabase)`

This method allows modify the SQL query on the fly before it is executed.

Warning

Be really careful when modifying queries, as this can break system logic and lead to data corruption.

Sample code to modify a SQL query by forcibly adding DISTINCT to a specific table (Orders):

```
[Export(typeof(IAdHocExtension))]publicclassAdHocExtensionSample:DefaultAdHocExtension{publicoverridestringModifyQuery(stringquery,stringdatabase){if(database==SupportedDatabase.MSSQL){varqueryNodes=query.Split(new[]{';'});for(vari=0;i<queryNodes.Length;++i){varqueryNode=queryNodes[i];varisQueryOrdersTable=queryNode.Contains("FROM [dbo].[Orders]");if(isQueryOrdersTable){varsearchedExpression="SELECT";varfirstSelectClauseIndex=queryNode.IndexOf(searchedExpression);queryNodes[i]=queryNode.Insert(firstSelectClauseIndex+searchedExpression.Length," DISTINCT ");}}returnString.Join(";\r\n",queryNodes);}returnquery;}}
```

## 

## LoadCustomFunctions

`List<CustomFunction> LoadCustomFunctions()`

This method loads the .NET implementation of Custom Functions. These functions are whitelisted using the CustomFunctionFilePath setting in the IzendaSystemSetting table. More information on CustomFunctionFilePath can be found [here](https://devnet.logianalytics.com/hc/en-us/articles/4415511926551-White-Listing-Functions-for-Calculated-Fields). This method and .NET implementation is required when using Custom Functions in a report based on two different databases and leveraging Izenda’s Fusion engine.

```
public virtual List LoadCustomFunctions()
           {
                return new List
               {
                        new CustomFunction
                        {
                                    CustomFunctionName = "SUBSTRING",
                                    CustomFunc = func => getString("SUBSTRING", func)
                        }
               }; 
        }

						
```

##

## See Also

The [UserContext.Current](https://devnet.logianalytics.com/hc/en-us/articles/4415504804887-UserContext) object contains data of the current logged in user, which can be leveraged in filters:

* to check if user has “Report Designer” role:  
  `UserContext.Current.IsInRole("ReportDesigner")`
* to check if user belongs to “ACME” tenant:  
  `UserContext.Current.CurrentTenant.TenantID=="acme"`
* to check if user has permission to create new reports:  
  `UserContext.Current.Permissions.Reports.CanCreateNewReport.Value==TRUE`
