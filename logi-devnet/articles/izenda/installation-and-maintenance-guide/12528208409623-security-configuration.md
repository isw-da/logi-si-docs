---
title: "Security Configuration"
id: 12528208409623
section: "Installation and Maintenance Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528208409623-Security-Configuration
updated_at: 2023-02-23T14:54:52Z
---

# Security Configuration

# Security Configuration

## Introduction

Izenda v2.7.1 and higher allows application administrators to directly trim out the specified characters per database server type when loading schemas. This option is applied globally and will affect the system and tenant users.

## Configuration

This option is configured by the adding a key/value entry for the desired database and schemas in the API/Web.config file as shown below:

|  |  |
| --- | --- |
| ``` 1 									2 									3 									4 									5 									6 									7 								8 ``` | ``` <!-- Please be sure that there are no leading or trailing spaces for each entry. --><appSettings><addkey="izenda.mssql.trimcharacters"value=""/><addkey="izenda.mysql.trimcharacters"value=""/><addkey="izenda.oracle.trimcharacters"value=""/><addkey="izenda.postgre.trimcharacters"value=""/><addkey="izenda.redshift.trimcharacters"value=""/></appSettings> ``` |

Note: Depending on your IIS configuration, changes to the Web.config file may automatically trigger the application to be reloaded.

### List of Supported Keys

|  |
| --- |
| **izenda.mssql.trimcharacters** |
| **izenda.mysql.trimcharacters** |
| **izenda.oracle.trimcharacters** |
| **izenda.postgre.trimcharacters** |
| **izenda.redshift.trimcharacters** |
