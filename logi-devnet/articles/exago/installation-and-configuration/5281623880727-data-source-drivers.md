---
title: "Data Source Drivers"
id: 5281623880727
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281623880727-Data-Source-Drivers
updated_at: 2024-08-21T21:04:13Z
---

# Data Source Drivers

# Data Source Drivers

## Supported Driver List

Below is a list and the associated links for recommended ADO.NET drivers for each type of data source.

* **SQL Server**
  + No external ADO.NET driver needed
* **Oracle**
  + [Oracle ODAC Connector](http://www.oracle.com/technetwork/database/windows/downloads/index-090165.html)
  + Oracle.ManagedDataAccess.Client
* **MySQL/MariaDB**
  + [Devart Connector](http://www.devart.com/dotconnect/mysql/download.html)
  + MySql.Data.MySqlClient
* **PostgreSQL**
  + [Devart Connector](http://www.devart.com/dotconnect/postgresql/download.html)
  + [Npgsql](https://www.npgsql.org/)
* **DB2/Informix**
  + [IBM Data Server Driver Package](https://www14.software.ibm.com/webapp/iwm/web/reg/download.do?source=swg-idsdpds&lang=en_US&S_PKG=win_64&cp=UTF-8&dlmethod=http) — 5.exe or newer
* **SQLite v2021.1.8+**
  + No external ADO.NET driver needed
* **ElasticSearch, Redshift, Snowflake, MongoDB, Google BigQuery**
  + [CData ADO.NET drivers](https://devnet.logianalytics.com/hc/en-us/articles/5281585000599-CData-Drivers)

    > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25322775984407 "Critical") **Important:**
    >
    > As of v2024.2.1, CData drivers are no longer available for use in Exago BI products. See **[CData Drivers](https://devnet.logianalytics.com/hc/en-us/articles/5281585000599)**.

## Exceptions, Caveats and Notes

### MySQL on Linux v2019.2+

As of *v2019.2* the Exago Linux Installer does not install a MySQL ADO.NET driver at the time of installation. Instead, clients wishing to use a MySQL data source for either reporting or for Storage Management will need to provide their own.

Exago has provided wrappers around two popular MySQL data drivers that clients may choose to install on their own.

* Devart dotconnect free edition
* MySQL ADO.NET

If you need more product information, including new purchases and upgrades, contact your Exago Customer Success Manager. Install the driver by extracting the contents of the download and then running either `installMySql.sh` or `installDevartMySql.sh` as root. Provide the Exago installation path to the installer script. For example:

```
sudo ./installDevartMySql.sh /opt/Exago
```

Once installed, update the **Admin Console** > **General** > **Database Settings** to reflect the new data provider.

If using the Storage Management command-line transition utilities add this line to `LoadReportsToDb.exe.config` between `<system.data><DbProviderFactories>`:

```
<add name="dotConnect for MySQL" invariant="Devart.Data.MySql" description="Devart dotConnect for MySQL" type="Devart.Data.MySql.MySqlProviderFactory, Devart.Data.MySql, Version=8.3.215.0, Culture=neutral, PublicKeyToken=09af7300eec23701" />
```

### Oracle.ManagedDataAccess.Client and Npgsql Installation via Nuget

The **Oracle.ManagedDataAccess.Client** driver for Oracle Data Sources and the **Npgsql** driver for PostgreSQL Data Sources are installed via the Nuget Package Manager. Therefore, manual editing of Exago’s `web.config` is required to give Exago access to the drivers.

Using Nuget is beyond the scope of Exago’s documentation, but more information on installation of these drivers can be found at the links below. If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

* [Using NuGet to Install and Configure Oracle Data Provider for .NET](https://www.oracle.com/webfolder/technetwork/tutorials/obe/db/dotnet/NuGet/index.html)
* [Npgsql Getting Started](https://www.npgsql.org/doc/index.html)
