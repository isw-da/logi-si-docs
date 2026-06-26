---
title: "Customizable Interfaces"
id: 12528223488919
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528223488919-Customizable-Interfaces
updated_at: 2023-02-23T15:16:58Z
---

# Customizable Interfaces

# Customizable Interfaces

Changed in version 0.22.12: The namespace has been changed from Izenda.Synergy to **Izenda.BI**. The sample codes have been updated accordingly.

## List of Interfaces

| Interface | Purpose | Full Sample |
| --- | --- | --- |
| **ICache** | Caching | [ICacheProvider - Redis Sample](https://devnet.logianalytics.com/hc/en-us/articles/12528223075095-ICacheProvider-Redis-Sample) |
| **IDataSourceAdaptor** | Adapter for database systems | [DataSourceAdaptor - DB2 Sample](https://devnet.logianalytics.com/hc/en-us/articles/12528207237783-DataSourceAdaptor-DB2-Sample) |
| **ISystemRepository** | Access to Izenda System Database | To be updated |

## ICache

1. Create a class to implement interface `ICache` (in namespace Izenda.BI.CacheProvider)
2. Mark class attribute: `[Export(typeof(ICache))]`

Samples

* To be updated

## IDataSourceAdaptor

1. Create a class to implement interface `IDataSourceAdaptor` (in namespace Izenda.BI.DataAdaptor)
2. Mark class attribute: `[Export(typeof(IDataSourceAdaptor))]`
3. Create a Server Type value with this format `<GUID>|<DbShortName>|[<DBShortName>]<DbFullName>`
4. Mark class attribute: `[ExportMetadata("ServerType","ServerTypevalue")]`

Samples

* To be updated

## ISystemRepository

1. Create a class to implement interface `ISystemRepository` (in namespace Izenda.BI.SystemRepository)
2. Mark class attribute: `[Export(typeof(ISystemRepository))]`
3. Create a Server Type value with this format `<GUID>|<DbShortName>|[<DBShortName>]<DbFullName>`
4. Mark class attribute: `[ExportMetadata("ServerType","ServerTypevalue")]`

Samples

> ```
> [Export(typeof(ISystemRepository))][ExportMetadata("ServerType", "572BD576-8C92-4901-AB2A-B16E38144813|MSSQL|[MSSQL]SQLServer")]publicclassSQLSystemRepository:ISystemRepository
> ```

Deprecated since version 0.22.12: The IHiddenFilter interface has been superseded by IAdhocExtension interface.
