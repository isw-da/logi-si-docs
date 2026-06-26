---
title: "Customizing System via Interfaces"
id: 12528207139607
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528207139607-Customizing-System-via-Interfaces
updated_at: 2023-02-23T15:16:15Z
---

# Customizing System via Interfaces

# Customizing System via Interfaces

The majority of Izenda functionalities are built upon interfaces to support custom implementations, even to the core components. They are listed below, together with step-by-step guide and code samples.

* [White Labeling URLs](https://devnet.logianalytics.com/hc/en-us/articles/12528223421975-White-Labeling-URLs)
* [IAdHocExtension](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension)
  + [OnPreLoadFilterDataTree](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm)
  + [OnLoadFilterDataTree](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm2)
  + [OnPostLoadFilterDataTree](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm3)
  + [OnPreLoadFilterData](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm4)
  + [OnPostLoadFilterData](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm5)
  + [OnPreExecute](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm6)
  + [OnExecuting](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm7)
  + [OnPostExecute](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm8)
  + [SetHiddenFilters](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm9)
  + [Application Scenarios](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm10)
  + [Applying Filter with Compounded Values](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm11)
  + [CustomTimePeriod](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm12)
  + [LoadCustomDataFormat](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm13)
  + [IWebUrlResolver](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm14)
  + [GetThemes](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm15)
  + [OnPreRestApiRequest](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm16)
  + [ModifyQuery](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm17)
  + [See Also](https://devnet.logianalytics.com/hc/en-us/articles/12528223478807-IAdHocExtension#_bm18)
* [IAdHocExtension Samples](https://devnet.logianalytics.com/hc/en-us/articles/12528223064471-IAdHocExtension-Samples)
  + [Reference Izenda libraries in a New Project](https://devnet.logianalytics.com/hc/en-us/articles/12528223064471-IAdHocExtension-Samples#_bm)
  + [Sample Method Implementations](https://devnet.logianalytics.com/hc/en-us/articles/12528223064471-IAdHocExtension-Samples#_bm2)
  + [Add the New Library](https://devnet.logianalytics.com/hc/en-us/articles/12528223064471-IAdHocExtension-Samples#_bm3)
  + [UnitTest for the Samples](https://devnet.logianalytics.com/hc/en-us/articles/12528223064471-IAdHocExtension-Samples#_bm4)
* [Customizable Interfaces](https://devnet.logianalytics.com/hc/en-us/articles/12528223488919-Customizable-Interfaces)
  + [List of Interfaces](https://devnet.logianalytics.com/hc/en-us/articles/12528223488919-Customizable-Interfaces#_bm)
  + [ICache](https://devnet.logianalytics.com/hc/en-us/articles/12528223488919-Customizable-Interfaces#_bm2)
  + [IDataSourceAdaptor](https://devnet.logianalytics.com/hc/en-us/articles/12528223488919-Customizable-Interfaces#_bm3)
  + [ISystemRepository](https://devnet.logianalytics.com/hc/en-us/articles/12528223488919-Customizable-Interfaces#_bm4)
* [ICacheProvider - Redis Sample](https://devnet.logianalytics.com/hc/en-us/articles/12528223075095-ICacheProvider-Redis-Sample)
  + [Preparation](https://devnet.logianalytics.com/hc/en-us/articles/12528223075095-ICacheProvider-Redis-Sample#_bm)
  + [ICacheProvider Implementation](https://devnet.logianalytics.com/hc/en-us/articles/12528223075095-ICacheProvider-Redis-Sample#_bm2)
  + [Replace the Built-in Caching Library](https://devnet.logianalytics.com/hc/en-us/articles/12528223075095-ICacheProvider-Redis-Sample#_bm3)
* [DataSourceAdaptor - DB2 Sample](https://devnet.logianalytics.com/hc/en-us/articles/12528207237783-DataSourceAdaptor-DB2-Sample)
  + [Preparation](https://devnet.logianalytics.com/hc/en-us/articles/12528207237783-DataSourceAdaptor-DB2-Sample#_bm)
  + [IDataSourceAdaptor Implementation](https://devnet.logianalytics.com/hc/en-us/articles/12528207237783-DataSourceAdaptor-DB2-Sample#_bm2)
