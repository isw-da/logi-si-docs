---
title: "Connect to MS SQL Server Analysis Services"
id: 4419722770711
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722770711-Connect-to-MS-SQL-Server-Analysis-Services
updated_at: 2022-04-01T19:33:31Z
---

# Connect to MS SQL Server Analysis Services

# Connect to MS SQL Server Analysis Services

Logi Info includes dedicated OLAP-related elements that allow users to retrieve and work with data from Microsoft SQL Server Analysis Services (SSAS), also known as Microsoft Analysis Services. The first step in using Logi Info with OLAP data is to *connect* to SSAS; this document discusses several methods of making that connection.

The following topics discuss connecting to SSAS:

* [Configuring IIS Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4419715175191-Configuring-IIS-Authentication#Authentication)
* [Configuring the Connection Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707424919-Configuring-the-Connection-Element#Element)

*Logi OLAP has been deprecated; the related elements are still supported and will work, but are no longer available in Logi Studio.*

## Requirements

This topic assumes that SQL Server and SSAS have been installed, configured, and successfully tested.

Your Logi Info application connects to SSAS using the **MSOLAP OLE DB** provider. This provider is *not* shipped with Logi Info but is installed with Microsoft Office, so it may already be on many development machines. For web servers without Office, you'll need to install it.

The ADOMD.NET and MSOLAP providers come as a single package and should be installed on the web server where the Logi application will be running. Which ADOMD.NET provider version you need depends on your SSAS version and it may be included in your MS SQL Server's Feature Pack. This [Microsoft document](https://msdn.microsoft.com/en-us/library/dn141152.aspx) can help you identify provider versions and where to find it.

After installing ADOMD.NET, be sure to restart the IIS web server.

In addition, if you're using a Windows client OS version of Windows 7 or earlier, or a server OS version of Windows Server 2008 or earlier, you will need Microsoft XML Core Services (**MSXML**). You can check in Control Panel > Programs to see if it's already installed.

* MSXML 4.0 SP3 is the *minimum* release required and can be [downloaded here](https://www.microsoft.com/en-us/download/default.aspx).
* There are two main components of this installation: the Microsoft XML Parser and the XML SDK. Of these two components, only the Microsoft **XML Parser** needs to be installed for Logi Info and OLAP.

You should also ensure that you have installed the latest SSAS Service Pack for your version of MS SQL Server.
