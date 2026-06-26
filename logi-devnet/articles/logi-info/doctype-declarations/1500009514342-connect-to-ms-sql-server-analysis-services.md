---
title: "Connect to MS SQL Server Analysis Services"
id: 1500009514342
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514342-Connect-to-MS-SQL-Server-Analysis-Services
updated_at: 2021-06-17T01:58:06Z
---

# Connect to MS SQL Server Analysis Services

# Connect to MS SQL Server Analysis Services

**Logi OLAP** elements enable features in Logi managed reporting products that allow users to display and manipulate data from Microsoft SQL Server Analysis Services (AS). The first step in using Logi OLAP elements is to connect to AS; this topic discusses several methods of making that connection.

* Connection Methods
* [Connect to AS using MSOLAP](#MSOLAP)
* [Connect to AS2005/2008 using XMLA](#2005XMLA)
* [Connect to AS2000 using XMLA](#2000XMLA)
* [AS2000 SP 4 Note](#2000Note)

If you have not already done so, we recommend you read [Logi OLAP](https://devnet.logianalytics.com/hc/en-us/articles/1500009531201-Logi-OLAP).  
The use of data retrieved from OLAP cubes is described in [Get Started with OLAP Grids](https://devnet.logianalytics.com/hc/en-us/articles/1500009530821-Get-Started-with-OLAP-Grids).

## Connection Methods

There are **two different methods** of connecting a Logi Analytics managed reporting application to AS: the XML for Analysis (XMLA) web service and the MSOLAP provider.

Even though the use of the **MSOLAP provider** connection is the easiest to set up, *performance* with Logi OLAP Reporting may be better using the **XMLA** connection method. Connecting using XMLA is slightly different for SQL Server 2000 and SQL Server 2005/2008. Each method is described below.

Regardless of which connection method is used, Microsoft XML Core Services (**MSXML**) needs to be installed first.

* MSXML 4.0 SP2 is the minimum release required; currently MSXML 6.0 SP1 is available and can be [downloaded here](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=d21c292c-368b-4ce1-9dab-3e9827b70604). You should check for other service packs and updates for it, too.
* There are two main components of this installation: the Microsoft XML Parser and the XML SDK. Of these two components, only the Microsoft **XML Parser** needs to be installed to run Logi OLAP Reporting.

You should also ensure that you have installed the latest AS Service Pack.

## Connect to AS using MSOLAP

A frequently-used connection method for both all versions of AS uses the MSOLAP provider with ADOMD.NET.

### Install MS ADOMD.NET

The Microsoft ADOMD.NET package needs to be installed on the web server where the Logi application is running.

1. [Download ADOMD.NET](http://www.microsoft.com/downloads/details.aspx?familyid=790D631B-BFF9-4F4A-B648-E9209E6AC8AD&displaylang=en), and install it on the web server.
2. From the same Microsoft Downloads page, download and install the latest hotfix (service pack).
3. Restart IIS.

### With IIS6: Configure Authentication and Impersonation

The IIS6 security configuration for your Logi application must be set to **Integrated Windows authentication**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771884439/connas_03.png)

This is done via the Directory Security tab in IIS Manager, as shown above. Note that no other authentication options are checked.

When setting up integrated security, **Impersonation** also needs to be configured. This is most easily done by manually editing your Logi application's Web.config file, located in your application's root folder, to control the *identity* of your application. There are three configuration possibilities:

**A.** If IIS and AS are running on the same server, or on different servers, and you wish the Logi application to use one specific account to access to the data, you can edit the Web.config file as follows:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778715159/connas_02.gif)

1. Browse to your Logi application folder and, using Notepad or another plain text editor, edit the file Web.config.
2. Add the text shown above to the file, entering the credentials for the one account to be used.
3. Save and close the file.

**B.** If IIS and AS are running on the *same* server, and you want the Logi application to use the individual account that each user logged into his Windows computer with to access the data, edit the file as follows:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778715415/connas_01.gif)

1. Browse to your Logi application folder and, using Notepad or another text editor, edit the file Web.config.
2. Add the text shown above to the file. The user's Windows account credentials will be passed to AS.
3. Save and close the file.

**C.** If IIS and AS are running on *different* servers, and you wish to the Logi application to use the account that each user logged into his Windows computer with to access the data, then IIS cannot directly pass that account information to AS (this is known as the dangerous authentication "double-hop"). You will need to implement **Kerberos** authentication to help IIS safely pass the account information to AS. This procedure is complicated and is discussed in this
[Microsoft Support document](http://support.microsoft.com/kb/917409).

**Which configuration should you use?** Let's review the basic security terminology: *authentication* identifies the user as valid, and *authorization* determines which resources the authenticated user can access. In production systems, it's not likely that IIS and AS will be running on the same system, so possibilities A. and C. above are the most likely system configuration and connection options.

The most common approach used by Logi developers is A. which locates the handling of authorization, by controlling which reports, elements, and activities the users can access, *in the Logi application*, using Logi Security. So, using one special account to access the database or AS is suitable. This is widely used by Logi customers for both OLAP and regular database access.

The less common approach is C. which locates authorization *in the database* itself, essentially recreating the accounts and/or roles that appear in the system authentication mechanism in the database as well, as a means of controlling authorization. This is an approach that requires additional administrative overhead (for example, accounts must be maintained in *both* Active Directory and in SQL Server) and connection complexity. It's sometimes used in multi-tenant database scenarios, but
even then is not a required approach. Developers who choose to use this approach should have in-depth expertise with Windows, IIS, and AS security configuration techniques.

##### With IIS7: Configure Application Pool Identity

When using IIS7 (with Vista, Windows 7, or Windows Server 2008), you do *not* need to enable Windows Authentication or Impersonation as you do with IIS6. Instead,
you change the identity of the **application pool** used with your Logi application to be that of the domain user account that has access to AS. This might be the Classic .NET app pool (which may affect all Logi apps on the server) or a clone of it that you create just for your Logi OLAP application. [Windows IIS Configuration](https://devnet.logianalytics.com/hc/en-us/articles/1500009515222-Windows-IIS-Configuration) describes how to create an IIS7 application pool.

Here's how to specify an identity for an IIS7 application pool:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771884695/connas_05.png)

1. Open the IIS Management Console (INETMGR.MSC).
2. Open the Application Pools node underneath the machine node.
3. Select and right-click the application pool you want to modify.
4. Select "Advanced Settings..." from the pop-up menu.
5. Select the "Identity" list item, as shown above, and click the browse button (the little button with the three dots).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771884951/connas_06.png)

6. In the Application Pool Identity dialog box that appears, check "Custom Account" and click "Set".
7. Type in the domain user account name and password to be used to access AS.
8. Click "OK" as needed to exit.

The Microsoft document [*Specifying an Application Pool Identity (IIS7)*](http://technet.microsoft.com/en-us/library/cc771170) provides more information about this process.

### Add Connection Element

A **Connection.OLAP** element needs to be added in your Logi application's \_Settings definition file and its ADOMD Connection String attribute needs to be configured.

A typical value for the Connection String attribute for **AS2008** is:

Provider=MSOLAP.4;Data Source=*IPaddress\instancename;*IntegratedSecurity=SSPI;Initial Catalog= *yourDatabasename*;Persist Security Info=True

Note in the AS2008 example above that the configuration of member "uniqueness" is no longer done in the connection string. Instead, it's accomplished by using the Business Intelligence Development Studio (BIDS) tool, by setting these Cube Dimension properties:

+ HierarchyUniqueNameStyle = *IncludeDimensionName*
+ MemberUniqueNameStyle = *NamePath*

See your AS2008 documentation
for more
information about the use of BIDS.

A typical value for the Connection String attribute for **AS2005** is:

Provider=MSOLAP.3;Data Source=*yourServername;*IntegratedSecurity=SSPI;Initial Catalog=*yourDatabasename*; Client Cache Size=25;Auto Synch Period=10000;MDX Unique Name Style=2;Default MDX Visual Mode=1; Persist Security Info=False  
 

If you're using multiple **AS2005** instances, a typical value is:

Provider=MSOLAP.3;Data Source=*IPaddress\instancename;*IntegratedSecurity=SSPI;Initial Catalog= *yourDatabasename*;Client Cache Size=25;Auto Synch Period=10000;MDX Unique Name Style=2;Default MDX Visual Mode=1; Persist Security Info=False  
 

## Connect to AS2005/2008 using XMLA

To connect to **AS****2005/2008**, a slightly **different web service** must be used. Setting up this web service is detailed in the Microsoft Tech Net article *Configuring HTTP Access to SQL Server 2005 Analysis Services on Microsoft Windows Server 2003*, which can be found at <http://technet.microsoft.com/en-us/library/cc917711.aspx>

After installing and configuring the web service, a Connection.OLAP element needs to be created in the \_Settings definition file of your Logi application. In its **ADOMD Connection String** attribute, specify the virtual directory URL of the **msmdpump.dll** file for the Data Source parameter. For example, a connection to an instance of AS on another computer might use this connection string:

Data Source=http://remoteservername/olap/msmdpump.dll

## Connect to AS2000 using XMLA

This approach requires that the Microsoft XML for Analysis SDK be installed on the same server as IIS. This SDK can be downloaded [here](http://www.microsoft.com/downloads/details.aspx?FamilyID=7564a3fd-4729-4b09-9ee7-5e71140186ee&DisplayLang=en).

1. During the installation, there will be a *Connection Encryption Settings* screen. For initial installation, select the "Enable HTTP and HTTPS" radiobutton. This setting can easily be changed later is necessary in the file: Microsoft XML For Analysis SDK\config\datasources.xml.

2. After installation, the XMLA server, as a web service, must be made available to clients by setting up a **virtual directory** for it in **IIS**. Instructions for doing this are included with the XMLA installation; this documentation can typically be reached by navigating to **Start > All Programs > Microsoft XML for Analysis SDK > Books Online**. The relevant article can be found in the documentation *Contents* pane under "XML for Analysis Provider > Installing the
   XML for Analysis Provider > Setting Up the
   Virtual Directory"

3. Next, an XMLA **data source** must be set up **manually**. The data sources are configured in this file:  
   C:\Program Files\Microsoft XML For Analysis SDK\Config\datasources.xml.   
     
   Configuring a data source is explained in the XMLA documentation in the "XML for Analysis Provider > Installing the XML for Analysis Provider > Setting Up Data Sources" article.

It may be necessary to specify a value for "Initial Catalog" in the <DataSourceInfo> tag for the data source in the file. An example of this tag, set to access an instance of Analysis Services, is:

<DataSourceInfo> Provider=MSOLAP.2;Data Source=*servername*;Initial Catalog=*databasename*;</DataSourceInfo>

The Source attribute can be set to "local" if AS is running locally. IIS should be **restarted** after changes are made to datasources.xml.

4. After installing and configuring XMLA, a **Connection.OLAP** element needs to be added in the \_Settings definition file of your Logi application. In its **ADOMD Connection String** attribute, specify the virtual directory URL of the **msxisapi.dll** file for the Data Source parameter. For example, a connection to a local instance of AS might use this connection string:

Data Source=http://localhost/xmla/msxisapi.dll

## AS2000 SP 4 Note

If you're using Microsoft SQL Server Analysis Services 2000 with Service Pack 4, you'll need to replace this file:

C:\Program Files\Common Files\System\Ole DB\msolap80.dll

The version of msolap80.dll installed with Service Pack 4 must be replaced in order for Logi OLAP Reporting to function correctly.

When SQL Server 2000 Service Pack 4 is installed, an older version (8.0.2039.0) of msolap80.dll gets installed. This version must be replaced by a newer version, such as 8.0.760.0, 8.0.534.0, or 8.0.384.0, in order for OLAP Grids to function correctly. You can examine a file's version number by selecting and right-clicking it in My Computer and selecting Properties in the popup menu; then clicking the Version tab in the Properties dialog box. A newer version of msolap80.dll can be used by installing
SQL Server 2000 Service Pack 3 or by copying it from another computer that has the correct version installed (it's also installed with MS Office). After msolap80.dll has been updated, IIS must be restarted for the changes to take effect.
