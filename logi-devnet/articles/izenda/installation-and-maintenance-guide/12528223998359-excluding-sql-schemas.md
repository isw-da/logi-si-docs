---
title: "Excluding SQL Schemas"
id: 12528223998359
section: "Installation and Maintenance Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528223998359-Excluding-SQL-Schemas
updated_at: 2023-02-23T14:54:26Z
---

# Excluding SQL Schemas

# Excluding SQL Schemas

## Introduction

Izenda v2.6.21 and higher allows application administrators to explicitly exclude any specified schemas from the available data sources. This option is applied globally and will affect the system and tenant users.

Warning

Please ensure that any schemas you intend to exclude are not in use. If the excluded schemas are in use, any reports or dashboards using those schemas will be broken and cannot be recovered. We recommend backing up your Izenda configuration database before making this change.

## Configuration

This option is configured by the adding a key/value entry for the desired database and schemas in the API/Web.config file as shown below:

|  |  |
| --- | --- |
| ``` 1 									2 									3 									4 									5 								6 ``` | ``` <!-- Please be sure that there are no leading or trailing spaces for each entry. --><appSettings><addkey="izenda.mssql.excludeSchema"value="MANAGEMENT"/><addkey="izenda.oracle.excludeSchema"value="HR,ACCOUNTING"/><addkey="izenda.postgresql.excludeSchema"value="SCHEMA1,SCHEMA2"/></appSettings> ``` |

Note: Depending on your IIS configuration, changes to the Web.config file may automatically trigger the application to be reloaded.

### List of Supported Keys

|  |
| --- |
| **izenda.mssql.excludeSchema** |
| **izenda.oracle.excludeSchema** |
| **izenda.postgresql.excludeSchema** |

Note: This option is not available for MySQL. The application will only enumerate the schema specified in the connection string for MySQL databases.

#### Restarting the web sites

After updating the Web.config file, restart the API and front-end sites.

#### Verifying the changes

In the example below, several schemas for Oracle are excluded via the Web.config file.

|  |  |
| --- | --- |
| ``` 1 											2 										3 ``` | ``` <appSettings><addkey="izenda.oracle.excludeSchema"value="IZENDACONFIG2,RDSADMIN,IZENDA11,IZENDACONFIG"/></appSettings> ``` |

Before the changes:

![../../_images/exclude_schema_before.png](https://devnet.logianalytics.com/hc/article_attachments/12528147960343/exclude_schema_before.png)

After restarting the API and reconnecting, the change works as expected:

![../../_images/exclude_schema_after.png](https://devnet.logianalytics.com/hc/article_attachments/12528163955991/exclude_schema_after.png)
