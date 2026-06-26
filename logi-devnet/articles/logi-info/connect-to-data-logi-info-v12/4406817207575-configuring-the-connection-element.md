---
title: "Configuring the Connection Element"
id: 4406817207575
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817207575-Configuring-the-Connection-Element
updated_at: 2022-04-06T06:04:37Z
---

# Configuring the Connection Element

# Configuring the Connection Element

To connect to SSAS, a **Connection.OLAP** element needs to be added in
your Logi application's \_Settings definition and its
**ADOMD Connection String** attribute needs to be configured.

Connection Strings can include a variety of properties and the examples
provided below are functional but not all-inclusive. More information
about SSAS connection string properties can be found in
[this Microsoft document](https://docs.microsoft.com/en-us/analysis-services/instances/connection-string-properties-analysis-services?redirectedfrom=MSDN&view=asallproducts-allversions&viewFallbackFrom=sql-server-ver15).

![](https://devnet.logianalytics.com/hc/article_attachments/5263096689047/noteicon.png) If you have more then one MSOLAP provider installed you may need to
specify the version of the provider in connection strings:

| Provider | SSAS Version |
| --- | --- |
| **Provider** | **SSAS Version** |
| MSOLAP.3 | 2005 |
| MSOLAP.4 | 2008 |
| MSOLAP.5 | 2012 |
| MSOLAP.6 | 2014, 2016 |

Just specifying *MSOLAP* as the provider causes the
*latest* version of MSOLAP installed on the system to be used.

**SSAS 2012, 2014, 2016**

A typical value for the ADOMD Connection String attribute for SSAS 2012,
2014, and 2016 is:

Provider=MSOLAP.5;Integrated Security=SSPI;Persist Security
Info=True;Initial Catalog=Adventure Works DW 2008R2;Data
Source=AW-SRV01;MDX Compatibility=1;Safety Options=2;MDX Missing Member
Mode=Error

**SSAS 2008**

A typical value for the ADOMD Connection String attribute for SSAS 2008
is:

Provider=MSOLAP.4;Data
Source=*IPaddress\instancename;*IntegratedSecurity=SSPI;Initial
Catalog= *yourDatabasename*;Persist Security Info=True

In the example above, the configuration of member
"uniqueness" is not done in the connection string. Instead, it's
accomplished by using the Business Intelligence Development Studio (BIDS)
tool, by setting these Cube Dimension properties:

HierarchyUniqueNameStyle = *IncludeDimensionName*  
 MemberUniqueNameStyle = *NamePath*

See your SSAS 2008 documentation for more information about the use of
BIDS.

**SSAS 2005**

A typical value for the ADOMD Connection String attribute for SSAS 2005
is:

Provider=MSOLAP.3;Data
Source=*yourServername;*IntegratedSecurity=SSPI;Initial
Catalog=*yourDatabasename*;Client Cache Size=25;Auto Synch
Period=10000;MDX Unique Name Style=2;Default MDX Visual Mode=1;
Persist Security Info=False

If you're using multiple SSAS 2005 instances, a typical value is:

Provider=MSOLAP.3;Data
Source=*IPaddress\instancename;*IntegratedSecurity=SSPI;Initial  
 Catalog=*yourDatabasename*;Client Cache Size=25;Auto Synch
Period=10000;MDX Unique Name Style=2;Default MDX Visual Mode=1; Persist
Security Info=False

### 

## Using Excel to Create Connection Strings

Microsoft Excel is capable of connecting to SSAS and you can use it to
help you create a proper connection string:

![](https://devnet.logianalytics.com/hc/article_attachments/5263107837591/connssas_05.png)

First, use Excel's Data Connection wizard in the Data tab, shown above, to
create a connection to SSAS. It will generate the proper connection string
with minimal input from you. Once you complete the wizard's steps, you can
view the new connection's properties:

![](https://devnet.logianalytics.com/hc/article_attachments/5263090305815/connssas_06.png)

In the Data tab, view the existing connections, right-click the connection
you just added, and view its properties, as shown above. In the Properties
Definition tab, you'll see the connection string the wizard created. You
can copy this (being sure you select and copy *all* of it - you may
need to scroll the text box) and paste it into your Connection element in
the \_Settings definition.

## Possible Firewall Issues

Be aware that SSAS uses a different port than SQL Server itself for
communications. If you're having trouble connecting to SSAS, ensure that
your firewall, if one's in use, is configured properly to allow SSAS
access. This
[Microsoft document](https://docs.microsoft.com/en-us/analysis-services/instances/configure-the-windows-firewall-to-allow-analysis-services-access?view=asallproducts-allversions&redirectedfrom=MSDN&viewFallbackFrom=sql-server-ver15)
provides configuration details for Windows Firewall.
