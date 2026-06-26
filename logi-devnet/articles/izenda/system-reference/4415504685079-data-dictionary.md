---
title: "Data Dictionary"
id: 4415504685079
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504685079-Data-Dictionary
updated_at: 2021-12-10T03:08:15Z
---

# Data Dictionary

# Data Dictionary

Note: The following data types are documented for a Microsoft SQL Server database.

| Table / Field Name | Data Type | Length | Constraints | Note |
| --- | --- | --- | --- | --- |
| **IzendaAccessRight**  Pre-defined sharing rights on each report or dashboard |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 | not null |  |
| **Type** | int |  |  | * 0 = Report/Template * 1 = Dashboard |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaAdvancedSetting**  Advanced system settings |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 | not null |  |
| **Value** | nvarchar | 2048 |  |  |
| **DefaultValue** | nvarchar | 256 |  |  |
| **Type** | nvarchar | 50 |  | Performance, Security or Others |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaCity**  Data of cities used for Map report part |  |  |  |  |
| **GeonameId** | varchar | 10 | not null |  |
| **Name** | nvarchar | 255 |  |  |
| **AsciiName** | nvarchar | 255 |  | The name in Latin alphabets |
| **AlternateNames** | nvarchar | 255 |  |  |
| **Latitude** | varchar | 15 |  |  |
| **Longitude** | varchar | 15 |  |  |
| **FeatureClasss** | nvarchar | 255 |  |  |
| **FeatureCode** | nvarchar | 255 |  |  |
| **CountryCode** | nvarchar | 255 |  |  |
| **Cc2** | nvarchar | 255 |  |  |
| **Admin1Code** | varchar | 10 |  |  |
| **Admin2Code** | nvarchar | 255 |  |  |
| **Admin3Code** | nvarchar | 255 |  |  |
| **Admin4Code** | nvarchar | 255 |  |  |
| **Population** | varchar | 10 |  |  |
| **Elevation** | varchar | 10 |  |  |
| **Dem** | varchar | 10 |  |  |
| **Timezone** | nvarchar | 255 |  |  |
| **ModificationDate** | datetime |  |  |  |
| **IzendaCommonFilterField**  Filter fields that are common among different report parts in the same dashboard |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | varchar | 1000 |  | Auto-generated name, e.g. ce0fda8a-4515-409c-9d00-0bf56c2b4c4d-OrderDate |
| **DisplayName** | varchar | 256 |  |  |
| **Value** | varchar | max |  |  |
| **OperatorId** | uniqueidentifier |  | FK to IzendaFilterOperator |  |
| **OperatorSetting** | nvarchar | 100 |  |  |
| **DataType** | nvarchar | 50 |  |  |
| **DashboardId** | uniqueidentifier |  | FK to IzendaDashboard |  |
| **Position** | int |  |  |  |
| **FilterFieldContent** | varchar | max |  | data in json format |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaConnection**  Connection strings to source databases |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 | not null | Database name |
| **ServerTypeId** | uniqueidentifier |  | not null |  |
| **ConnectionString** | nvarchar | 500 |  | Encrypted connection string |
| **Visible** | bit |  |  |  |
| **Deleted** | bit |  |  | Is this data deleted |
| **RelateToConnectionId** | uniqueidentifier |  |  |  |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **Color** | nvarchar | 10 |  |  |
| **Version** | int |  |  | Current version of the data |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaDashboard**  Dashboards |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 | not null |  |
| **Description** | nvarchar | max |  |  |
| **CategoryId** | uniqueidentifier |  | FK to IzendaReportCategory |  |
| **SubCategoryId** | uniqueidentifier |  | FK to IzendaReportCategory |  |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **ImageUrl** | nvarchar | 2048 |  |  |
| **StretchImage** | bit |  |  |  |
| **BackgroundColor** | nvarchar | 50 |  |  |
| **ShowFilterDescription** | bit |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **Owner** | nvarchar | 256 |  |  |
| **LastViewed** | datetime |  |  |  |
| **NumberOfView** | bigint |  |  |  |
| **RenderingTime** | float |  |  | Unit: second |
| **OwnerId** | uniqueidentifier |  |  |  |
| **CreatedById** | uniqueidentifier |  |  |  |
| **ModifiedById** | uniqueidentifier |  |  |  |
| **SourceId** | uniqueidentifier |  |  |  |
| **IzendaDashboardPart**  Dashboard parts |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **DashboardId** | uniqueidentifier |  | FK to IzendaDashboard |  |
| **Type** | nvarchar | 50 |  | Either reportPart or text |
| **Title** | nvarchar | 256 |  |  |
| **ReportId** | uniqueidentifier |  | FK to IzendaReport |  |
| **ReportPartId** | uniqueidentifier |  | FK to IzendaReportPart |  |
| **NumberOfRecord** | int |  |  |  |
| **FilterDescription** | nvarchar | max |  |  |
| **Content** | nvarchar | max |  | Data in json format |
| **PositionX** | int |  |  |  |
| **PositionY** | int |  |  |  |
| **Width** | int |  |  |  |
| **Height** | int |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **SourceId** | uniqueidentifier |  |  |  |
| **IzendaDashboardPartFilterField**  Filter fields in a dashboard part |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **FilterFieldId** | uniqueidentifier |  | FK to IzendaFilterField |  |
| **Value** | nvarchar | max |  |  |
| **OperatorId** | uniqueidentifier |  | FK to IzendaFilterOperator |  |
| **OperatorSetting** | nvarchar | 100 |  |  |
| **DashboardPartId** | uniqueidentifier |  | FK to IzendaDashboardPart |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaDataFormat**  Data formats, e.g. ‘mm/dd/yyyy’ |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 |  |  |
| **Format** | nvarchar | 100 |  |  |
| **Description** | nvarchar | 256 |  | Sample values |
| **Category** | nvarchar | 100 |  |  |
| **SubCategory** | nvarchar | 100 |  |  |
| **DataType** | nvarchar | 50 |  |  |
| **AllowFilter** | bit |  |  |  |
| **AllowFieldProperty** | bit |  |  |  |
| **GroupBy** | nvarchar | 50 |  | Values to be grouped by |
| **FormatDataType** | nvarchar | 50 |  |  |
| **Position** | int |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaDataSourceCategory**  Categories for source tables, views and stored procedures |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 | not null |  |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **Deleted** | bit |  |  | Is this data deleted |
| **Version** | int |  |  | Current version of the data |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaDataTypeFunctionMapping**  Mappings between data types and supported functions |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **DataType** | nvarchar | 50 | not null |  |
| **FunctionId** | uniqueidentifier |  | FK to IzendaFunction   not null |  |
| **FormatDataType** | nvarchar | 50 |  | Data type of the result |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaDBVersion**  Current version of Izenda database schema |  |  |  |  |
| **Version** | nvarchar | 16 | not null | Current version of Izenda database schema |
| **IzendaEmailSetting**  [Expand] Email sending options |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **DisplayName** | nvarchar | 256 |  | Value of the name in From field, e.g. John Doe in “From: John Doe <[jdoe@acme.com](mailto:jdoe%40acme.com)>” |
| **EmailFromAddress** | nvarchar | 256 |  | Value of the email in From field, e.g. [jdoe@acme.com](mailto:jdoe%40acme.com) in “From: John Doe <[jdoe@acme.com](mailto:jdoe%40acme.com)>” |
| **UseSystemConfiguration** | bit |  |  | Re-use setting from system level or not |
| **Server** | nvarchar | 256 |  | E.g. smtp.gmail.com |
| **Port** | int |  |  | E.g. 587 |
| **SecureConnection** | bit |  |  | Use SSL/TLS or not |
| **Login** | nvarchar | 256 |  | User name for the email server |
| **Password** | nvarchar | 500 |  | Encrypted password |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaExportMarginDefaultValue**  Default values for the margin in Export function |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Type** | int |  | not null | * 0 = Normal * 1 = Narrow * 2 = Wide * 3 = Custom * 4 = MinCustom * 5 = MaxCustom |
| **TopValue** | float |  |  |  |
| **BottomValue** | float |  |  |  |
| **LeftValue** | float |  |  |  |
| **RightValue** | float |  |  |  |
| **HeaderValue** | float |  |  |  |
| **FooterValue** | float |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaFilterField**  Filter fields in a report part |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **FilterId** | uniqueidentifier |  | FK to IzendaFilter |  |
| **QuerySourceFieldId** | uniqueidentifier |  | FK to IzendaQuerySourceField |  |
| **QuerySourceId** | uniqueidentifier |  | FK to IzendaQuerySource |  |
| **QuerySourceType** | nvarchar | 50 |  | Table, Aggregated Field, Calculated Fields or Stored Procedure |
| **RelationshipId** | uniqueidentifier |  | FK to IzendaRelationship |  |
| **Position** | int |  |  |  |
| **Alias** | nvarchar | 256 |  | Display alias, e.g. Sum(Freight), Freight\*1.1 |
| **ReportFieldAlias** | nvarchar | 256 |  |  |
| **ReportPartTitle** | nvarchar | 256 |  |  |
| **Visible** | bit |  |  |  |
| **Required** | bit |  |  |  |
| **Cascading** | bit |  |  |  |
| **OperatorId** | uniqueidentifier |  | FK to IzendaOperator |  |
| **OperatorSetting** | nvarchar | 100 |  |  |
| **Value** | nvarchar | max |  | Values for the operator, separated by semi-colon |
| **DataFormatId** | uniqueidentifier |  | FK to IzendaDataFormat |  |
| **FontFamily** | nvarchar | 50 |  |  |
| **FontSize** | int |  |  |  |
| **TextColor** | nvarchar | 10 |  |  |
| **BackgroundColor** | nvarchar | 10 |  |  |
| **FontBold** | bit |  |  |  |
| **FontItalic** | bit |  |  |  |
| **FontUnderline** | bit |  |  |  |
| **SortType** | nvarchar | 10 |  | ASC, DESC or Unsorted |
| **Deleted** | bit |  |  | Is this data deleted |
| **Version** | int |  |  | Current version of the data |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaFilterOperator**  Operators used in filters |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 |  |  |
| **Label** | nvarchar | 256 |  |  |
| **OperatorGroupId** | uniqueidentifier |  | FK to IzendaOperatorGroup |  |
| **AllowParameter** | bit |  |  | Needs additional parameter value (in IzendaFilterField.Value) or not |
| **Position** | int |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaFilterOperatorGroup**  Groups of filter operators |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaFilterOperatorRule**  Rules for filter operators |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **OperatorId** | uniqueidentifier |  | FK to IzendaOperator |  |
| **AllowNull** | bit |  |  | Accepts null values or not |
| **IsPairedValues** | bit |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaFunction**  Built-in functions |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | varchar | 256 | not null |  |
| **Expression** | nvarchar | 256 |  |  |
| **SubTotal** | bit |  |  | Is usable in Sub Total or not |
| **GrandTotal** | bit |  |  | Is usable in Grand Total or not |
| **FieldProperty** | bit |  |  | Is usable on a data source field or not |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaLanguage**  Supported languages and cultures |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Language** | nvarchar | 150 |  |  |
| **CultureName** | nvarchar | 20 |  | E.g. en-US |
| **Version** | int |  |  | Current version of the data |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 150 |  |  |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 150 |  |  |
| **Deleted** | bit |  |  | Is this data deleted |
| **IzendaLicenseSetting**  License data |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Online** | bit |  |  |  |
| **LicenseKey** | nvarchar | max |  |  |
| **Token** | nvarchar | max |  |  |
| **LastRefresh** | datetime |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaPasswordHistory**  Password hash history to prevent reuse |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **UserId** | uniqueidentifier |  | FK to IzendaUser |  |
| **PasswordHash** | nvarchar | 256 |  |  |
| **PasswordSalt** | nvarchar | 256 |  |  |
| **Version** | int |  |  | Current version of the data |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaPerformanceStatsTrend**  Collected performance statistics |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **NumberOfCore** | int |  |  |  |
| **NumberOfServer** | int |  |  |  |
| **NumberOfReport** | bigint |  |  |  |
| **NumberOfReportCreator** | bigint |  |  |  |
| **NumberOfDashboard** | bigint |  |  |  |
| **NumberOfDashboardCreator** | bigint |  |  |  |
| **NumberOfReportView** | bigint |  |  |  |
| **NumberOfDashboardView** | bigint |  |  |  |
| **NumberOfActiveTenant** | bigint |  |  |  |
| **NumberOfInactiveTenant** | bigint |  |  |  |
| **NumberOfActiveUser** | bigint |  |  |  |
| **NumberOfInactiveUser** | bigint |  |  |  |
| **DeploymentMode**  New in version 2.15.0. | int |  |  | * 0 = All Standalone * 1 = BE Standalone - FE Integrated * 2 = BE Integrated - FE Standalone * 3 = All Integrated |
| **NumberOfCreateReportUser** | bigint |  |  |  |
| **NumberOfCreateDashboardUser** | bigint |  |  |  |
| **IzendaVersion** | nvarchar | 100 |  |  |
| **IzendaConfigurationDatabase** | nvarchar | 256 |  |  |
| **DatabaseTypesInUse** | nvarchar | max |  |  |
| **ClientLicenseKey** | nvarchar | max |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaPostalCode**  Postal code data used for Map |  |  |  |  |
| **PostalCode** | varchar | 10 | not null |  |
| **PlaceName** | nvarchar | 255 |  |  |
| **Province** | nvarchar | 255 |  |  |
| **Latitude** | varchar | 15 |  |  |
| **Longitude** | varchar | 15 |  |  |
| **IzendaQuerySource**  Data sources |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 | not null |  |
| **Type** | nvarchar | 50 |  | Table, View or Stored Procedure |
| **Selected** | bit |  |  | Is selected to be visible or not |
| **Deleted** | bit |  |  | Is this data deleted |
| **ParentQuerySourceId** | uniqueidentifier |  | FK to IzendaQuerySource |  |
| **CategoryId** | uniqueidentifier |  |  |  |
| **DataSourceCategoryId** | uniqueidentifier |  |  |  |
| **Alias** | nvarchar | 256 |  |  |
| **ExtendedProperties** | nvarchar | 4000 |  | Properties for functions and stored procedures, in json format |
| **PhysicalChange** | int |  |  | * -1 = Not set * 0 = None * 1 = Added * 2 = Modified * 3 = Deleted |
| **Approval** | int |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaQuerySourceCategory**  Database schemas |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 | not null |  |
| **ParentCategoryId** | uniqueidentifier |  |  |  |
| **ConnectionId** | uniqueidentifier |  | FK to IzendaConnection   not null |  |
| **Deleted** | bit |  |  | Is this data deleted |
| **Version** | int |  |  | Current version of the data |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaQuerySourceField**  Database fields and calculated fields |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 |  |  |
| **DataType** | nvarchar | 50 |  | Original data type |
| **IzendaDataType** | nvarchar | 50 |  | Converted data type |
| **AllowDistinct** | bit |  |  |  |
| **Alias** | nvarchar | 256 |  |  |
| **Visible** | bit |  |  |  |
| **Filterable** | bit |  |  |  |
| **QuerySourceId** | uniqueidentifier |  |  |  |
| **Deleted** | bit |  |  | Is this data deleted |
| **ParentId** | uniqueidentifier |  | FK to IzendaQuerySource |  |
| **Type** | int |  |  | * 0 = Field * 1 = Parameter |
| **GroupPosition** | int |  |  |  |
| **Position** | int |  |  |  |
| **FilteredValue** | nvarchar | max |  | Filter values for stored procedures parameters |
| **ExtendedProperties** | nvarchar | max |  |  |
| **MatchedTenant** | bit |  |  |  |
| **PhysicalChange** | int |  |  |  |
| **Approval** | int |  |  |  |
| **FunctionName** | nvarchar | 256 |  |  |
| **Expression** | nvarchar | 500 |  | Expression for calculated fields |
| **ReportId** | uniqueidentifier |  | FK to IzendaReport |  |
| **IsCalculated** | bit |  |  | Is calculated field or not |
| **Version** | int |  |  | Current version of the data |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaRelationship**  Database relationships |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **JoinQuerySourceId** | uniqueidentifier |  | FK to IzendaQuerySource   not null |  |
| **ForeignQuerySourceId** | uniqueidentifier |  | FK to IzendaQuerySource   not null |  |
| **JoinFieldId** | uniqueidentifier |  | FK to IzendaQuerySourceField |  |
| **ForeignFieldId** | uniqueidentifier |  | FK to IzendaQuerySourceField |  |
| **Alias** | nvarchar | 256 |  | Alias of join query source |
| **SystemRelationship** | bit |  |  | Is this a physical relationship (or defined in Data Model) |
| **JoinType** | nvarchar | 50 |  | Inner, Right, Left or Outer |
| **ParentRelationshipId** | uniqueidentifier |  |  |  |
| **ReportId** | uniqueidentifier |  | FK to IzendaReport |  |
| **ForeignAlias** | nvarchar | 256 |  | Alias of foreign query source |
| **RelationshipPosition** | int |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaRelationshipKeyJoin**  Additional fields in a multi-column relationship |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **RelationshipId** | uniqueidentifier |  | FK to IzendaRelationship   not null |  |
| **JoinQuerySourceId** | uniqueidentifier |  | FK to IzendaQuerySource   not null |  |
| **ForeignQuerySourceId** | uniqueidentifier |  | FK to IzendaQuerySource   not null |  |
| **JoinFieldId** | uniqueidentifier |  | FK to IzendaQuerySourceField   not null |  |
| **ForeignFieldId** | uniqueidentifier |  | FK to IzendaQuerySourceField   not null |  |
| **Operator** | nvarchar | 50 |  | Join operator |
| **JoinSourceAlias** | nvarchar | 256 |  |  |
| **ForeignSourceAlias** | nvarchar | 256 |  |  |
| **Position** | int |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaReport**  Reports |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 | not null |  |
| **Type** | int |  | not null | * 0 = Report * 1 = Template |
| **PreviewRecord** | int |  | not null |  |
| **AdvancedMode** | bit |  | not null |  |
| **AllowNulls** | bit |  | not null |  |
| **IsDistinct** | bit |  | not null |  |
| **CategoryId** | uniqueidentifier |  | FK to IzendaReportCategory |  |
| **SubCategoryId** | uniqueidentifier |  | FK to IzendaReportCategory |  |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **Description** | nvarchar | max |  |  |
| **HeaderContent** | nvarchar | max |  | Content of header box, in json format |
| **FooterContent** | nvarchar | max |  | Content of footer box, in json format |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **LastViewed** | datetime |  |  |  |
| **Owner** | nvarchar | 256 |  | Firstname and lastname of owner for display |
| **OwnerId** | uniqueidentifier |  | FK to IzendaUser | The owner |
| **Title** | nvarchar | 256 |  |  |
| **TitleDescriptionContent** | nvarchar | max |  | Content of title box, in json format |
| **ExcludedRelationships** | nvarchar | max |  | Relationships that were manually removed |
| **NumberOfView** | bigint |  |  |  |
| **RenderingTime** | float |  |  |  |
| **CreatedById** | uniqueidentifier |  |  |  |
| **ModifiedById** | uniqueidentifier |  |  |  |
| **ExportFormatSettingData** | nvarchar | max |  | Remembered export settings, in json format |
| **SnapToGrid** | bit |  |  |  |
| **UsingFields** | nvarchar | max |  | List of ids of query source fields used by this report, comma-separated |
| **SourceId** | uniqueidentifier |  |  |  |
| **IzendaReportCategory**  Categories for report/dashboard |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 | not null |  |
| **Type** | int |  | not null | * 0 = Report * 1 = Template * 2 = Dashboard |
| **ParentId** | uniqueidentifier |  | FK to IzendaReportCategory | Id of the parent category, for sub-categories |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaReportDataSource**  Data sources used in reports |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **QuerySourceId** | uniqueidentifier |  | FK to IzendaQuerySource   not null |  |
| **ReportId** | uniqueidentifier |  | FK to IzendaReport   not null |  |
| **Deleted** | bit |  |  | Is this data deleted |
| **Version** | int |  |  | Current version of the data |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaReportFilter**  Data of filters in report |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Logic** | nvarchar | 2000 |  | The logic, e.g. 1 AND 2 OR 3 |
| **Visible** | bit |  |  | Shown under report description or not |
| **ReportId** | uniqueidentifier |  | FK to IzendaReport |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaReportHistory**  Report history |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **ReportId** | uniqueidentifier |  | FK to IzendaReport   not null |  |
| **ReportName** | nvarchar | 256 | not null |  |
| **Description** | nvarchar | max | not null |  |
| **Definition** | nvarchar | max |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaReportPart**  Report parts |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Title** | nvarchar | 256 | not null |  |
| **PositionX** | int |  |  |  |
| **PositionY** | int |  |  |  |
| **Width** | int |  |  |  |
| **Height** | int |  |  |  |
| **Content** | nvarchar | max |  | The [ReportPartContent](https://devnet.logianalytics.com/hc/en-us/articles/4415504772247-ReportPartContent) in json format |
| **NumberOfRecord** | int |  |  |  |
| **ReportId** | uniqueidentifier |  | FK to IzendaReport   not null |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **SourceId** | uniqueidentifier |  |  |  |
| **IzendaReportSetting**  Report Settings |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **EnforceVersionHistory** | bit |  |  |  |
| **NumOfArchivedVersionToKeep** | int |  |  |  |
| **RemoveArchivedVersions** | bit |  |  |  |
| **RecurrentReportSettingData** | nvarchar | max |  |  |
| **IsScheduled** | bit |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaRole**  Roles |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 | not null |  |
| **PermissionData** | nvarchar | max |  | Permissions in json format |
| **QuerySources** | nvarchar | max |  | Array of tenant query sources, in json format |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **Active** | bit |  |  |  |
| **Deleted** | bit |  |  | Is this data deleted |
| **Version** | int |  |  | Current version of the data |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaSecurityPolicy**  Security policies |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **MinNumberOfPasswordLenght** | int |  |  |  |
| **MaxNumberOfPasswordLenght** | int |  |  |  |
| **MinNumberOfSpecialCharacter** | int |  |  |  |
| **MaxNumberOfSpecialCharacter** | int |  |  |  |
| **MinNumberOfUppercaseCharacter** | int |  |  |  |
| **MaxNumberOfUppercaseCharacter** | int |  |  |  |
| **MinNumberOfLowercaseCharacter** | int |  |  |  |
| **MaxNumberOfLowercaseCharacter** | int |  |  |  |
| **MinNumberOfNumericCharacter** | int |  |  |  |
| **MaxNumberOfNumericCharacter** | int |  |  |  |
| **MaxNumberOfRepeatSequential** | int |  |  |  |
| **MinNumberOfPasswordAge** | int |  |  |  |
| **MaxNumberOfPasswordAge** | int |  |  |  |
| **NotifyUseDuring** | int |  |  |  |
| **NumberOfPasswordToKeep** | int |  |  |  |
| **PasswordLinkValidity** | int |  |  |  |
| **NumberOfQuestionProfile** | int |  |  |  |
| **NumberOfQuestionResetPassword** | int |  |  |  |
| **NumberOfFailedLogonAllowed** | int |  |  |  |
| **NumberOfFailedAnswerAllowed** | int |  |  |  |
| **LockoutPeriod** | int |  |  |  |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaSecurityQuestion**  Security questions |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Question** | nvarchar | max |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **OrderNumber** | int |  |  |  |
| **IzendaServer**  The web server information used in performance statistics |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **ServerName** | nvarchar | 1000 |  |  |
| **ServerCore** | int |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaSubsCommonFilterField**  Common filter fields used in subscriptions |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **CommonFilterFieldId** | uniqueidentifier |  | FK to IzendaCommonFilterField |  |
| **Value** | nvarchar | max |  | Selected values for this filter |
| **OperatorId** | uniqueidentifier |  | FK to IzendaOperator |  |
| **OperatorSetting** | nvarchar | 100 |  |  |
| **SubscriptionId** | uniqueidentifier |  | FK to IzendaSubscription |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaSubscription**  Report and dashboard subscriptions and sheduled deliveries |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 |  |  |
| **Schedule** | nvarchar | max |  | Description of the schedule for display |
| **FilterValueSelection** | nvarchar | max |  | Description of the filter for display |
| **Type** | nvarchar | 100 |  | Subscribed Reporting Item or Subscribed Alert |
| **TimeZoneName** | nvarchar | 256 |  |  |
| **TimeZoneValue** | nvarchar | 256 |  |  |
| **StartDate** | datetime |  |  |  |
| **StartDateUtc** | datetime |  |  |  |
| **StartTime** | datetime |  |  |  |
| **RecurrenceType** | int |  |  | * 0 = AlertHourly * 1 = AlertDaily * 2 = EveryDay * 3 = EveryWeekday * 4 = EveryWeek * 5 = EveryTwoWeeks * 6 = EveryMonth * 7 = EveryQuarter * 8 = CustomRecurrence |
| **RecurrencePattern** | int |  |  | * 0 = Daily * 1 = Weekly * 2 = Monthly * 3 = Yearly |
| **RecurrencePatternValue** | nvarchar | max |  | Details of the recurrence pattern, in json format, e.g. {“recurrenceWeek”:1,”selectedDayValue”:”2”} |
| **IsEndless** | bit |  |  |  |
| **IsScheduled** | bit |  |  |  |
| **Occurrence** | int |  |  | Actual number of past occurences |
| **EndDate** | datetime |  |  |  |
| **EndDateUtc** | datetime |  |  |  |
| **DeliveryType** | nvarchar | 100 |  | Email or File Location |
| **DeliveryMethod** | nvarchar | 100 |  | Link, Attachment, Embedded HTML or Send to disk |
| **ExportFileType** | nvarchar | 50 |  | PDF, Word, Excel, or CSV |
| **ExportAttachmentType** | nvarchar | 50 |  |  |
| **EmailSubject** | nvarchar | 256 |  |  |
| **EmailBody** | nvarchar | max |  |  |
| **ReportId** | uniqueidentifier |  |  |  |
| **DashboardId** | uniqueidentifier |  | FK to IzendaDashboard |  |
| **Recipients** | nvarchar | max |  | Comma-separated list of email addresses |
| **LastSuccessfulRun** | nvarchar | 500 |  | Display value for LastSuccessfulRunDate |
| **NextScheduledRun** | nvarchar | 500 |  | Display value for NextScheduledRunDate |
| **LastSuccessfulRunDate** | datetime |  |  |  |
| **NextScheduledRunDate** | datetime |  |  |  |
| **IsSubscription** | bit |  |  | Is this a subscription (or scheduled delivery) |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **CreatedById** | uniqueidentifier |  |  | Redundant, to be removed |
| **IzendaSubscriptionFilterField**  Filter fields used in subscriptions |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **FilterFieldId** | uniqueidentifier |  | FK to IzendaFilterField |  |
| **Value** | nvarchar | max |  | Selected values for this filter |
| **OperatorId** | uniqueidentifier |  |  |  |
| **OperatorSetting** | nvarchar | 100 | FK to IzendaFilterOperator | Selected operator for this filter |
| **SubscriptionId** | uniqueidentifier |  | FK to IzendaSubscription |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaSystemSetting**  System settings |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | varchar | 256 | not null |  |
| **Value** | nvarchar | 256 |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaSystemVariable**  System variables |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 |  | * Everywhere: {currentDateTime}, {currentUserName}, {tenantName} * Report/Dashboard: {recipientName} * Report: {reportName}, {reportLink}, {embedReportHTML} * Dashboard: {dashboardLink}, {dashboardName}, {embedDashboardHTML} * Export: {pageNumber}, {horizontalRule}, {verticalRule} |
| **DataType** | nvarchar | 50 |  | Output data type of the system variable |
| **Description** | nvarchar | 2000 |  |  |
| **Scope** | int |  |  | * 0 = Everywhere * 1 = Report/Dashboard * 2 = Report * 3 = Dashboard * 4 = Export |
| **IzendaTemporaryData**  Data for un-saved objects |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **ObjectId** | uniqueidentifier |  |  | Id of the temporary object |
| **ObjectData** | nvarchar | max |  | Data of the object, in json format |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **UserId** | uniqueidentifier |  |  | User who owns this temporary data |
| **IzendaTenant**  Tenant data in multi-tenant mode |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **TenantID** | varchar | 256 | not null | The user-defined “Tenant Id” field |
| **Name** | nvarchar | 256 | not null |  |
| **Description** | nvarchar | 256 |  |  |
| **Active** | bit |  |  |  |
| **Deleted** | bit |  |  | Is this data deleted |
| **Modules** | nvarchar | 500 |  | Encrypted list of assigned modules |
| **PermissionData** | nvarchar | max |  | Data of permissions, in json format |
| **Version** | int |  |  | Current version of the data |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaTimePeriod**  Pre-defined time periods, e.g. current and next month |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 |  |  |
| **Type** | nvarchar | 100 |  | Classification for the period, e.g. Day, Calendar Quarter, Fiscal Quarter |
| **Value** | nvarchar | 256 |  | Internal value of the period |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaUser**  Users |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **UserName** | nvarchar | 256 | not null |  |
| **FirstName** | nvarchar | 256 |  |  |
| **LastName** | nvarchar | 256 |  |  |
| **PasswordHash** | nvarchar | 256 |  |  |
| **PasswordSalt** | nvarchar | 256 |  |  |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **Version** | int |  |  | Current version of the data |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **EmailAddress** | varchar | 256 |  |  |
| **CurrentTokenHash** | nvarchar | 256 |  |  |
| **Active** | bit |  |  | Inactive users cannot login |
| **Deleted** | bit |  |  | Is this data deleted |
| **DataOffset** | numeric(10,2) |  | s | For versions 2.9.4 and prior, the data type was *int* |
| **TimestampOffset** | numeric(10,2) |  |  | For versions 2.9.4 and prior, the data type was *int* |
| **InitPassword** | bit |  |  | Has password been initiated |
| **RetryLoginTime** | smallint |  |  | The number of failed login attempts |
| **LastTimeAccessed** | datetime |  |  |  |
| **PasswordLastChanged** | datetime |  |  |  |
| **Locked** | bit |  |  | Is locked out because of max failed login attempts or not |
| **LockedDate** | datetime |  |  |  |
| **CultureName** | nvarchar | 20 |  |  |
| **DateFormat** | nvarchar | 20 |  |  |
| **SystemAdmin** | bit |  |  |  |
| **SecurityQuestionLastChanged** | datetime |  |  |  |
| **NumberOfFailedSecurityQuestion** | int |  |  | The aggregated number of times that user fails security questions, it will be reset when user is unlocked |
| **IzendaUserPermission**  Sharing rights on each report or dashboard |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **ReportId** | uniqueidentifier |  | FK to IzendaReport |  |
| **DashboardId** | uniqueidentifier |  | FK to IzendaDashboard |  |
| **AssignedTo** | nvarchar | 4000 |  | Array of ids of assigned roles or users depending on AssignedType, in json format |
| **AssignedType** | int |  |  | * 1 = Everyone * 2 = Role * 3 = User |
| **AccessRightId** | uniqueidentifier |  | FK to IzendaAccessRight |  |
| **Position** | int |  |  |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaUserRole**  Assignment of users and roles |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **UserId** | uniqueidentifier |  | FK to IzendaUser |  |
| **RoleId** | uniqueidentifier |  | FK to IzendaRole |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaUserSecurityQuestion**  Security questions for each user |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **UserId** | uniqueidentifier |  | FK to IzendaUser   not null |  |
| **SecurityQuestionId** | uniqueidentifier |  | FK to IzendaSecurityQuestion   not null |  |
| **Answer** | nvarchar | max | not null |  |
| **Version** | int |  |  | Current version of the data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Modified** | datetime |  |  | The modification datetime |
| **ModifiedBy** | nvarchar | 256 | FK to IzendaUser | User who last modified this data |
| **IzendaWorkspace**  Copy management workspaces |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **Name** | nvarchar | 256 |  |  |
| **Description** | nvarchar | max |  |  |
| **TenantId** | uniqueidentifier |  |  | Not used   The target ternant is in IzendaWorkspaceTenant |
| **OwnerId** | uniqueidentifier |  | FK to IzendaUser |  |
| **CreatedBy** | nvarchar | 256 | FK to IzendaUser | User who created this data |
| **Deleted** | bit |  |  | Is this data deleted |
| **Created** | datetime |  |  | The created datetime |
| **Modified** | datetime |  |  | The modification datetime |
| **CopyRoles** | bit |  |  |  |
| **CopyReport** | bit |  |  |  |
| **CopyDashboard** | bit |  |  |  |
| **CopyRolePermission** | bit |  |  |  |
| **CopyAdvancedSettings** | bit |  |  |  |
| **CopyDataModel** | bit |  |  |  |
| **CopyTenantPermissions** | bit |  |  |  |
| **SourceId** | uniqueidentifier |  |  | Id of the source tenant, null or empty if source is system |
| **SelectAllTenants** | bit |  |  | Copies to all tenants or not |
| **SourceDataModel** | nvarchar | max |  | Source data model in json format |
| **SourceHashCode** | nvarchar | 500 |  | Hash code of all connection strings of source |
| **CopiedRolesData** | nvarchar | max |  | Array of ids of copied roles at modification time, in json format |
| **CopiedRolePermissionData** | nvarchar | max |  | Array of ids of copied permissions at modification time, in json format |
| **TotalHashCode** | nvarchar | 500 |  | Array of hash codes of advancedSettings, tenantPermission, roles and rolePermissions, in json format |
| **SourceReportModel** | nvarchar | max |  |  |
| **SourceTemplateModel** | nvarchar | max |  |  |
| **SourceDashboardModel** | nvarchar | max |  |  |
| **IzendaWorkspaceMapping**  Mapping from source to destination in copy management workspace |  |  |  |  |
| **Id** | uniqueidentifier |  | PK |  |
| **WorkspaceId** | uniqueidentifier |  | FK to IzendaWorkspace |  |
| **FromDatabaseName** | nvarchar | 256 |  | Source database in mappings with “Database” type |
| **Type** | int |  |  |  |
| **FromObject** | nvarchar | 256 |  | Source schema in mappings with “Schema” type |
| **ToDatabaseName** | nvarchar | 256 |  | Target database in mappings with “Database” type |
| **ToObject** | nvarchar | 256 |  | Target schema in mappings with “Schema” type |
| **IsGlobal** | bit |  |  | Place-holder |
| **FromServer** | nvarchar | 256 |  |  |
| **ToServer** | nvarchar | 256 |  |  |
| **IzendaWorkspaceMappingTenant**  Selected tenants for each copy management mapping |  |  |  |  |
| **WorkspaceMappingId** | uniqueidentifier |  | FK to IzendaWorkspaceMapping |  |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **IzendaWorkspaceTenant**  Selected tenants for each copy management workspace |  |  |  |  |
| **WorkspaceId** | uniqueidentifier |  | FK to IzendaWorkspace   not null |  |
| **TenantId** | uniqueidentifier |  | FK to IzendaTenant | The id of the tenant if not null |
| **Status** | int |  |  | * 0 = NeedValidated * 1 = ReadyToCopy * 2 = AuthenticationMissing * 3 = ValidationError |
| **SourceDataModel** | nvarchar | max |  | Place-holder |
| **PhysicalDataModel** | nvarchar | max |  | Place-holder |
| **DestinationHashCode** | nvarchar | 500 |  | Hascode of all connection strings of the tenant |
