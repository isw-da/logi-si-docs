---
title: "Managing the dbconfigs.json File"
id: 5281593110167
section: "Performance and Scaling"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281593110167-Managing-the-dbconfigs-json-File
updated_at: 2022-05-03T22:07:59Z
---

# Managing the dbconfigs.json File

# Managing the dbconfigs.json File

The `dbconfigs.json` file contains database specific syntax related to formulas, data types, primary and foreign key discovery, datetime casting, and row limiting and range selection. This file is loaded by Exago during runtime and is required in order to provide database specific optimizations or to enable various advanced features.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

This file is located in:

* `<WebApp>\Config\Other`
* `<Sched>\bin\Config\Other` of each **Scheduler Service**

These files must be kept consistent and any modifications made to the file directly should be duplicated in all other copies.

## Properties and Usage

Most of the component properties and usage of the `dbconfigs.json` file are documented in their respective topics:

* [Automatic Database Discovery](https://devnet.logianalytics.com/hc/en-us/articles/5281636352791-Automatic-Database-Discovery)
* [Formula Dictionary](https://devnet.logianalytics.com/hc/en-us/articles/5281628373655-Database-Settings#Formula)
* Security Precautions for Database Formulas
* [Incremental Loading](https://devnet.logianalytics.com/hc/en-us/articles/5281629053335-Incremental-Loading)

## Overriding `dbconfigs` Information

The base `dbconfigs.json` file is overwritten automatically by the Exago installer in order to provide the most up to date set of features. Any modifications made to the base copy of `dbconfigs.json` will be overwritten upon each new installation of Exago.

In order to customize this data and ensure that all changes persist between upgrades, a `<WebApp>\Config\Other\dbconfigs.overrides.json` file can be created and populated with the specific changes as of *v2019.1.2+*. The format of these changes must follow the same schema as the base file.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> A copy of the `dbconfigs.overrides.json` file should also be added to the `<Sched>\bin\Config\Other` directory of each **Scheduler Service**.

### Examples

The following modifications added to the `dbconfigs.overrides.json` will persist throughout each new Exago install.

1. Modify the MSSQL ‘false’ formula to use 1 != 1 instead of 1 = 0:

```
{
 "mssql": {
  "FormulaDictionary" : {
   "false" : [ "1 != 1" ]
  }
 }
}
```

2. Add specific DateTime format to Oracle databases:

```
{
 "oracle": {
  "DateFormat" : "YYYY-MM-DD HH:mm:ss"
 }
}
```

3. Allow quotation marks in the schema name for PostgreSQL databases (requires *v2021.1.8+*):

```
{
 "postgres": {
  "UseDelimitersOnSchema" : true
 }
}
```

### Removing Properties from `dbconfigs.json`

If it is necessary to remove information from `dbconfigs.json`, it must be done directly within the base file.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Properties that are removed directly from the `dbconfigs.json` file may be readded after each new Exago install. To prevent modifications to the base `dbconfigs.json` from being overwritten after each install, backup this file prior to installation.
