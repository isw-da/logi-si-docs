---
title: "System DB and License APIs"
id: 4415492759191
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492759191-System-DB-and-License-APIs
updated_at: 2021-12-10T03:08:13Z
---

# System DB and License APIs

# System DB and License APIs

## Summary

| API | Purpose | Usage in Izenda Front-end |
| --- | --- | --- |
| [GET databaseSetup/supportedDatabaseType](#id1) | Returns an array of database server types currently supported for installation.   See also: [GET dataAdaptor](https://devnet.logianalytics.com/hc/en-us/articles/4415504629911-Connection-APIs#get-dataadaptor) | Settings > System DB & License > populate Data Server Type box |
| [POST databaseSetup/testConnection](#id2) | Tests the database connection and license validity if existing.   See also: [POST connection/verify](https://devnet.logianalytics.com/hc/en-us/articles/4415504629911-Connection-APIs#post-connection-verify) | Settings > System DB & License > Connect |
| [GET databaseSetup/databaseInfo](#get-databasesetup-databaseinfo) | Returns the current database server type and connection string. | Settings > System DB & License |
| [POST databaseSetup/databaseInfo](#post-databasesetup-databaseinfo) | Sets up system database and saves the database server type and the connection string. | Settings > System DB & License > Connect |
| [POST databaseSetup/provisionStaticData](#post-databasesetup-provisionstaticdata) | Provisions static data into system database. | Settings > System DB & License > Provision Map Data |
| [GET databaseSetup/provisionStaticDataStatus](#get-databasesetup-provisionstaticdatastatus) | Returns status of provision static data. | On Front-end load |
| [POST databaseSetup/staticData/city](#post-databasesetup-staticdata-city) | Returns provision city data. | Report Designer > Map Report Part > add Field to City box |
| [POST databaseSetup/staticData/postalCode](#post-databasesetup-staticdata-postalcode) | Returns provision postal code data. | Report Designer > Map Report Part > add Field to Postal Code box |
| [GET databaseSetup/staticData/countryCodes](#get-databasesetup-staticdata-countrycodes) | Returns provision country code data. .. versionadded:: 2.0.3 | Report Designer > Map Report Part > add Field to Country box |
| [GET systemSetting/systemMode](#get-systemsetting-systemmode) | Returns the current system or tenant mode of the settings. | On Front-end load |
| [GET systemSetting/systemModeSettings](#get-systemsetting-systemmodesettings) | Returns data in System Mode Settings section. | Settings > System DB & License |
| [POST systemSetting/systemModeSettings](#post-systemsetting-systemmodesettings) | Saves data in System Mode Settings section. | Settings > System DB & License > change an option |
| [GET systemSetting/deploymentMode](#get-systemsetting-deploymentmode) | Returns the deployment mode. | On Front-end load |
| [GET systemSetting/systemIndicator/(tenant\_id)](#id3) | Returns the number of changes in Connection String and Data Model (filtered by tenant\_id if provided). | Settings > Data Setup > Connection String |
| [GET license/status](#get-license-status) | Returns up-to-date expiration status of the license. | On Front-end load |
| [GET license/currentToken](#get-license-currenttoken) | Returns the details of the current token. | On Front-end load |
| [POST license/validate](#post-license-validate) | Validates the license for both online and offline modes, then save it in the database. | Settings > System DB & License > enter the license > Validate |
| [POST license/requestToken](#post-license-requesttoken) | Returns a newly-generated token for the license key in parameter. | To be updated |

## GET databaseSetup/supportedDatabaseType

Returns an array of database server types currently supported for installation.

**Request**

> No payload

**Response**

> An array of [DatabaseType](https://devnet.logianalytics.com/hc/en-us/articles/4415492793495-DatabaseType) objects

**Samples**

> ```
> GET/api/databaseSetup/supportedDatabaseTypeHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{name:"[AZSQL] AzureSQL",shortName:"AZSQL",id:"d968e96f-91dc-414d-9fd8-aef2926c9a18"},{name:"[MYSQL] MySQL",shortName:"MYSQL",id:"3d4916d1-5a41-4b94-874f-5bedacb89656"},{name:"[ORACL] Oracle",shortName:"ORACL",id:"93942448-c715-4f98-85e2-9292ed7ca4bc"},{name:"[PGSQL] PostgreSQL",shortName:"PGSQL",id:"f2638ed5-70e5-47da-a052-4da0c1888fcf"},{name:"[MSSQL] SQLServer",shortName:"MSSQL",id:"572bd576-8c92-4901-ab2a-b16e38144813"}]
> ```

## POST databaseSetup/testConnection

Tests the database connection and license validity if existing.

If success, the connection string will also be saved.

**Request**

> Payload: a [DBSetupInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504716823-DBSetupInfo) object

**Response**

> A [ConnectionVerificationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492774167-ConnectionVerificationResult) object

**Samples**

> ```
> POST/api/databaseSetup/testConnectionHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"ServerTypeId":" d968e96f-91dc-414d-9fd8-aef2926c9a18","ConnectionString":" server=host01\\instance01;database=db01;User Id=user01;Password=secret;"}
> ```
>
> Response in case of a successful call:
>
> ```
> {"serverNotValid":false,"databaseNotValid":false,"loginFail":false,"hasValidLicense":false,"success":true,"messages":[]}
> ```
>
> Response in case of an invalid connection string error:
>
> ```
> {"serverNotValid":false,"databaseNotValid":false,"loginFail":false,"hasValidLicense":false,"success":false,"messages":["The connection string is invalid. Please enter a valid one."]}
> ```

## GET databaseSetup/databaseInfo

Returns the current database server type and connection string.

**Request**

> No payload

**Response**

> A [DBSetupInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504716823-DBSetupInfo) object

**Samples**

> ```
> GET/api/databaseSetup/databaseInfoHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"serverTypeId":"f2638ed5-70e5-47da-a052-4da0c1888fcf","serverTypeName":"[PGSQL] PostgreSQL","connectionString":"Server=izenda-w10-02;Integrated Security=true; Database=db01;"}
> ```

## POST databaseSetup/databaseInfo

Sets up system database and saves the database server type and the connection string.

Note

It will take some time to set up the system database

**Request**

> Payload: a [DBSetupInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504716823-DBSetupInfo) object

**Response**

> An [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object with **success** field true if the setup is successful

**Samples**

> To be updated

## POST databaseSetup/provisionStaticData

Provisions static data into system database.

**Request**

> No payload

**Response**

> * 0 = Not started
> * 1 = Provisioning in progresss
> * 2 = Provision success
> * 3 = Provision error

**Samples**

> ```
> POST/api/databaseSetup/provisionStaticDataHTTP/1.1
> ```
>
> Sample response:
>
> ```
> 1
> ```

## GET databaseSetup/provisionStaticDataStatus

Returns status of provision static data.

**Request**

> No payload

**Response**

> * 0 = Not started
> * 1 = Provisioning in progresss
> * 2 = Provision success
> * 3 = Provision error

**Samples**

> ```
> GET/api/databaseSetup/provisionStaticDataStatusHTTP/1.1
> ```
>
> Sample response:
>
> ```
> 2
> ```

## POST databaseSetup/staticData/city

Returns provision city data.

**Request**

> Payload:
>
> | Field | Description | Note |
> | --- | --- | --- |
> | **criterias**  array of strings | The fields to filter data   |  |  | | --- | --- | | * GeonameId * Name * AsciiName * AlternateNames * Latitude * Longitude * FeatureClass * FeatureCode * CountryCode | * Cc2 * Admin1Code * Admin2Code * Admin3Code * Admin4Code * Population * Elevation * Dem * Timezone | |  |
> | **values**  array of strings | The values to filter data (using case-insensitive string equal operator), in exact same order with the fields |  |

**Response**

> An array of [City](https://devnet.logianalytics.com/hc/en-us/articles/4415504697623-City) objects

**Samples**

> ```
> POST/api/databaseSetup/staticData/cityHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"criterias":[],"values":[]}
> ```
>
> Sample response:
>
> ```
> Tobeupdated
> ```

## POST databaseSetup/staticData/postalCode

Returns provision postal code data.

**Request**

> Payload:
>
> | Field | Description | Note |
> | --- | --- | --- |
> | **criterias**  array of strings | The fields to filter data   |  |  | | --- | --- | | * PostalCode * PlaceName * Province | * Latitude * Longitude | |  |
> | **values**  array of strings | The values to filter data (using case-insensitive string equal operator), in exact same order with the fields |  |

**Response**

> An array of [PostCode](https://devnet.logianalytics.com/hc/en-us/articles/4415492828183-PostCode) objects

**Samples**

> ```
> POST/api/databaseSetup/staticData/postalCodeHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"criterias":[],"values":[]}
> ```
>
> Sample response:
>
> ```
> Tobeupdated
> ```

## GET databaseSetup/staticData/countryCodes

Returns provision country code data.

New in version 2.0.3.

**Request**

> No payload

**Response**

> An array of the following object
>
> | Field | Description | Note |
> | --- | --- | --- |
> | **name**  string | The name of the country |  |
> | **code2**  string | The ISO Alpha-2 country code |  |
> | **code3**  string | The ISO Alpha-3 country code |  |
> | **continent**  string | The name of the continent |  |
> | **coordinates**  array of objects  New in version 3.5.0. | The array of coordinates to define the boundary of country |  |
> | **longitude**  real number  New in version 3.5.0. | The longitude |  |
> | **latitude**  real number  New in version 3.5.0. | The latitude |  |
> | **alternateNames**  string  New in version 3.5.0. | The country’s alternative names |  |

**Samples**

> ```
> GETdatabaseSetup/staticData/countryCodesHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"name":"Andorra","code2":"AD","code3":"AND","continent":"Europe","coordinates":"[[{\"lng\":\"1.4166\",\"lat\":\"42.5617\"},{\"lng\":\"1.7220\",\"lat\":\"42.5617\"},{\"lng\":\"1.7220\",\"lat\":\"42.4489\"},{\"lng\":\"1.5184\",\"lat\":\"42.3925\"},{\"lng\":\"1.4166\",\"lat\":\"42.5617\"}]]","longitude":"1.6016","latitude":"42.5462","alternateNames":"And.,Andorra"}]
> ```

## GET systemSetting/systemMode

Returns the current system or tenant mode of the settings.

**Request**

> No payload

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **systemMode**  integer | The system mode   * 0 = Multiple tenant * 1 = Single tenant |  |

**Samples**

> ```
> GET/api/systemSetting/systemModeHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"systemMode":1}
> ```

## GET systemSetting/systemModeSettings

Returns data in System Mode Settings section.

**Request**

> No payload

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **systemMode**  integer | The system mode   * 0 = Multiple tenant * 1 = Single tenant |  |
> | **allowDuplicateUser**  boolean | Whether to allow duplicated user names in multi-tenant mode |  |

**Samples**

> ```
> GET/api/systemSetting/systemModeSettingsHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"systemMode":0,"allowDuplicateUser":true}
> ```

## POST systemSetting/systemModeSettings

Saves data in System Mode Settings section.

**Request**

> | Field | Description | Note |
> | --- | --- | --- |
> | **systemMode**  integer | The system mode   * 0 = Multiple tenant * 1 = Single tenant |  |
> | **allowDuplicateUser**  boolean | Whether to allow duplicated user names in multi-tenant mode |  |

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **success**  boolean | Is the save successful |  |

**Samples**

> ```
> POST/api/systemSetting/systemModeSettingsHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"systemMode":0,"allowDuplicateUser":true}
> ```
>
> Sample response:
>
> ```
> {"success":true}
> ```

## GET systemSetting/deploymentMode

Returns the deployment mode.

**Request**

> No payload

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **deploymentMode**  integer | Integration modes   * 0 = AllStandAlone * 1 = BEStandAloneFEIntegrated * 2 = BEIntegratedFEStandAlone * 3 = AllIntegrated |  |

**Samples**

> ```
> GET/api/systemSetting/deploymentModeHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"deploymentMode":0}
> ```

## GET systemSetting/systemIndicator/(tenant\_id)

Returns the number of changes in Connection String and Data Model (filtered by tenant\_id if provided).

**Request**

> No payload

**Response**

> | Field | Description | Note |
> | --- | --- | --- |
> | **key**  string | Either “ConnectionString” or “DataModel” |  |
> | **value**  integer | The number of changes for each type |  |

**Samples**

> ```
> GET/api/systemSetting/systemIndicatorHTTP/1.1
> ```
>
> Sample response:
>
> ```
> [{"key":"ConnectionString","value":1},{"key":"DataModel","value":2}]
> ```

## GET license/status

Returns up-to-date expiration status of the license.

**Request**

> No payload

**Response**

> A [LicenseStatusResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504735127-LicenseStatusResult) object

**Samples**

> ```
> GET/api/license/statusHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"licenseStatus":{"disabled":false,"meetExprireWarningPeriod":false,"numberOfDayToExpire":88,"numberOfDayToValid":0,"exceedLostConnectionAllowPeriod":false,"isAdminUser":false,"trialLicense":false},"success":true,"messages":null}
> ```

## GET license/currentToken

Returns the details of the current token.

**Request**

> No payload

**Response**

> A [ValidateTokenResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504807575-ValidateTokenResult) object

**Samples**

> ```
> GET/api/license/currentTokenHTTP/1.1
> ```
>
> Sample response:
>
> ```
> {"tokenKey":"1aBcD+=","licenseKey":"1aBcD+=","startDate":"2016-03-01T00:00:00","endDate":"2017-03-01T23:59:59","modules":[{"id":"256b555f-58ef-4418-be6c-048d2fc1f691","name":"Alerting"}],"companyId":"70d1037a-401a-446b-ae10-a5bb0144c611","previousStartDate":null,"previousEndDate":null,"previousModules":null,"licenseOnlineMode":false,"licenseTrial":false,"licenseEnable":true,"licenseEndDate":"2017-03-01T23:59:59","numberOfDayToValid":0,"success":true,"messages":null}
> ```

## POST license/validate

Validates the license for both online and offline modes, then save it in the database.

**Request**

> Payload: a [TokenRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415512063767-TokenRequest) object

**Response**

> A [ValidateTokenResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504807575-ValidateTokenResult) object

**Samples**

> ```
> POST/api/license/validateHTTP/1.1
> ```
>
> For Online mode, Request Payload includes LicenseKey only:
>
> ```
> {"LicenseKey":"1aBcD+=="}
> ```
>
> For Offline mode, Request Payload includes both LicenseKey and TokenKey:
>
> ```
> {"LicenseKey":"1aBcD+==","TokenKey":"1aBcD+="}
> ```

## POST license/requestToken

Returns a newly-generated token for the license key in parameter.

**Request**

> Payload: a [TokenRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415512063767-TokenRequest) object

**Response**

> A [ValidateTokenResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504807575-ValidateTokenResult) object

**Samples**

> ```
> POST/api/license/requestTokenHTTP/1.1
> ```
>
> Request payload:
>
> ```
> {"LicenseKey":"1aBcD+=="}
> ```
>
> Sample response:
>
> ```
> {"success":true,"messages":null,"tokenKey":"1aBcD+==","licenseKey":"1aBcD+=","startDate":"2016-03-01T00:00:00","endDate":"2017-03-01T23:59:59","modules":[{"id":"256b555f-58ef-4418-be6c-048d2fc1f691","name":"Alerting"}],"companyId":"70d1037a-401a-446b-ae10-a5bb0144c611","previousStartDate":null,"previousEndDate":null,"previousModules":null,"licenseOnlineMode":false,"licenseTrial":false,"licenseEnable":true,"licenseEndDate":"2017-03-01T23:59:59","numberOfDayToValid":0}
> ```
