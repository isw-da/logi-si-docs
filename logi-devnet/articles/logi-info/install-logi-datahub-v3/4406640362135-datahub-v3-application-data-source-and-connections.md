---
title: "DataHub v3 Application Data Source and Connections"
id: 4406640362135
section: "Install Logi DataHub v3"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406640362135-DataHub-v3-Application-Data-Source-and-Connections
updated_at: 2022-04-01T03:13:22Z
---

# DataHub v3 Application Data Source and Connections

# DataHub v3 Application Data Source and Connections

One of the features Logi DataHub v3 provides is the ability to connect to cloud- and application-based data. This topic presents examples of how to create connections to them when creating Dataviews.

* [Creating an Application Data Source](#Creating)
* [Application Source Details](#Details)

+ [Amazon Dynamo DB](#AmazonDDB)
+ [Eloqua](#Eloqua)
+ [Facebook](#Facebook)
+ [Financial Accounts (OFX)](#FinAccts)
+ [Google Analytics](#GoogleAn)
+ [Marketo](#Marketo)
+ [Microsoft Dynamics CRM on Premise](#MSDCRMOP)
+ [Microsoft Dynamics CRM Online](#MSDCRMOL)
+ [Microsoft Dynamics GP](#MSDGP)
+ [NetSuite](#NetSuite)
+ [OData](#OData)
+ [QuickBooks on Premise](#QBOP)
+ [QuickBooks Online](#QBOL)
+ [QuickBooks POS](#QBPOS)
+ [Salesforce](#Salesforce)
+ [SAP Netweaver](#SAPNETW)
+ [Twitter](#Twitter)

* [Managing Data Sources](#Managing)

## Creating an Application Data Source

In Logi DataHub v3, a connection to data is called a "Source" and data can be retrieved from an application, a database, or a data file. In this topic, we'll explain how to create a new Source using an application.

In the Dataview Authoring tool, there are multiple paths to the Add Source panel, including:

* **Sources** menu option![](https://devnet.logianalytics.com/hc/article_attachments/5160464735255/menuarrowrt.png)Create New Source.
* **Dataviews** menu option![](https://devnet.logianalytics.com/hc/article_attachments/5160464735255/menuarrowrt.png)Create New Dataview ![](https://devnet.logianalytics.com/hc/article_attachments/5160464735255/menuarrowrt.png)From Source tab![](https://devnet.logianalytics.com/hc/article_attachments/5160464735255/menuarrowrt.png)Add New Source

The Add Source panel will appear; its controls will vary depending on the data provider chosen but the descriptions provided below are typical:

![](https://devnet.logianalytics.com/hc/article_attachments/5160464813847/connapp_01.png)

Select or provide the required information, as follows:

1. **Application**  - Select the Application radio button.
2. **Data Provider**  - Select the desired application. The panel controls will change with each selection.
3. **New Source Name**  - Give the Source an arbitrary name for easy recognition later.
4. **Username** - Enter the user name required to access the application.
5. **Password** - Enter the password required to access the application.
6. **Company**  - Enter any other information required by the target application.
7. **Test Source**  - This action will attempt to make the connection specified and provide a status message. In addition to indicating either success or failure, any existing Source with the *exact same* specifications will be identified so you can decide whether to use it instead or proceed to save your new Source.

Click **Save** to save your new Source. Repeat as necessary to create the Sources you need.

## Application Source Details

This section provides the Source details, and helpful links, for each supported application.

### Amazon Dynamo DB

The connection to Dynamo DB is made using your *AccessKey*, *SecretKey*, and optionally your *Domain* and *Region*. Your *AccessKey*
and *SecretKey* can be obtained on the security credentials page for your Amazon Web Services account. Your *Region* will be displayed in the upper left-hand corner of the page when you are logged into Dynamo DB.

More information is available externally about the [Amazon Dynamo DB provider](https://cdn.arcesb.com/help/AZG/mft/index.html).

### Eloqua

The Add Source panel configuration details for Eloqua are shown in the example in the previous section.

### Facebook

Selecting Facebook as the data provider will result in the display of these controls:

![](https://devnet.logianalytics.com/hc/article_attachments/5160447941783/connapp_02.png)

Click **Get Auth Token** to login to Facebook and copy your authorization token. You'll need to have Platform access turned on in Facebook to do this and you'll be prompted to enable it during this process if it's not.

The **Page ID** is the unique identifier of the Facebook page whose statistics you'd like to track. You may need to look it up via online tools or the page URL in Facebook. [This web page](http://inlinevision.com/apps/how-to-find-your-facebook-page-id/) explains how to find it, or a quick Google search for "Facebook Page ID" will lead you to several other sources.

### Financial Accounts (OFX)

To specify a location for the database where the table, view, and stored procedures are located, set the *Location* property in the connection string. In addition you must also set the *User* and *Password* properties.

More information is available externally about the [Financial Accounts (OFX) provider](http://www.ofx.net/).

### Google Analytics

Selecting Google Analytics as the data provider will result in the display of these controls:

![](https://devnet.logianalytics.com/hc/article_attachments/5160422002071/connapp_03.png)

Click **Get Auth Token** and log into Google Analytics using your credentials. Copy and paste the token into the control provided.

Once you've provided a token, you'll need to select the **Web Profile** that will provide the data you are interested in. To do that, click **Get Profiles** to populate a list of web profiles and select one from the list.

### Marketo

Selecting Marketo as the data provider will result in the display of these controls:

![](https://devnet.logianalytics.com/hc/article_attachments/5160465073943/connapp_05.png)

You'll need to enter *User ID*,
*Encryption Key*and *SOAP Endpoint* values in the
controls provided in order to access to the data.

### Microsoft Dynamics CRM on Premise

To specify a location to the database where the tables, views, and stored procedures are located, set the *Location* property in the connection string. In addition, you must set the *User*, *Password*, and *Url* properties.

### Microsoft Dynamics CRM Online

Selecting Microsoft Dynamics CRM Online as the data provider will result in the display of these controls:

![](https://devnet.logianalytics.com/hc/article_attachments/5160465162263/connapp_06.png)

You'll need to enter the *User ID* and *Password* credentials that grant access to Microsoft Dynamics CRM Online. Enter the *URL* of the application that contains the data you want to work with.

### Microsoft Dynamics GP

Selecting Microsoft Dynamics GP as the data provider will result in the display of these controls:

![](https://devnet.logianalytics.com/hc/article_attachments/5160453802519/connapp_04.png)

Supply the requested information in the proper controls.

More information is available externally about the [Microsoft Dynamics GP provider](https://cdn.arcesb.com/help/AZG/mft/index.html).

### NetSuite

To specify where the table, view, and stored procedures of the database are located, set the *Location* property in the connection string. In addition, you must also set the *User*, *Password*, and *AccountId* properties.

More information is available externally about the [NetSuite provider](http://cdn.rssbus.com/help/ARD/mft/pg_NetSuite.htm).

### OData

You must set the User and Password properties in the *URL*.

More information is available externally about the [OData provider](https://cdn.arcesb.com/help/AZG/mft/API.html).

### QuickBooks on Premise

To specify a location to the database where the tables, views, and stored procedures are located, set the *Location* property in the connection string. In addition, if QuickBooks is not installed
on the local machine and you're using the QuickBooks Remote Connector, you must set the *User*, *Password,* and *URL* properties.

More information is available externally about the [QuickBooks on Premise provider](https://cdn.arcesb.com/help/AZG/mft/index.html).

### QuickBooks Online

Selecting QuickBooks Online as the data provider will result in the display of these controls:

![](https://devnet.logianalytics.com/hc/article_attachments/5160434984855/connapp_07.png)

You'll need to provide an *Authorization Token*. Click **Get Auth Token** and log into QuickBooks Online using your credentials. Copy and paste your authorization token into the control provided. Enter the *Company ID* for the organization that contains the data you want to use.

More information is available externally about the [QuickBooks Online provider](https://cdn.arcesb.com/help/AZG/mft/QBO.html).

### QuickBooks POS

Specify the User ID, Password, and URL required to access the data.

More information is available externally about the [QuickBooks POS provider](https://cdn.arcesb.com/help/AZG/mft/index.html).

### Salesforce

Selecting Salesforce as the data provider will result in the display of these controls:

![](https://devnet.logianalytics.com/hc/article_attachments/5160453805719/connapp_08.png)

Enter the *Username* and *Password* for the Salesforce account whose data you want to use.

### SAP Netweaver

To specify a location to the database where the tables, views and stored procedures are located, set the *Location* property in the connection string. In most cases, you'll also need to set the *User*, *Password*, *ConnectionType*, *Client*,
and *SystemNumber* properties.

More information is available externally about the [SAP Netweaver provider](https://cdn.arcesb.com/help/AZG/mft/IDoc.html).

### Twitter

Selecting Twitter as the data provider will result in the display of these controls:

![](https://devnet.logianalytics.com/hc/article_attachments/5160419245847/connapp_09.png)

You'll need to provide an **Authorization Token**. Click **Get Auth Token** and log into Twitter using your credentials. Copy and paste the authorization token into the control provided.

## Managing Data Sources

As you create Sources, they're represented in the Sources page with graphic "pills":

![](https://devnet.logianalytics.com/hc/article_attachments/5160453807639/connapp_10.png)

Each pill displays the Source name and application type, as shown above, and includes a "gear" icon. Hovering your mouse cursor over the icon displays a menu of management actions.

![](https://devnet.logianalytics.com/hc/article_attachments/5160422056087/connapp_11.png)

The *Info* menu option allows you to see, among other details, who created the Source, as shown above. This can be helpful if the Source has been shared with you by another user. The *Delete* option will only be included if you're the user who created the Source.

![](https://devnet.logianalytics.com/hc/article_attachments/5160435063063/connapp_12.png)

Source pills are also visible in the Create a New Dataview page, under the From Source tab, as shown above. The gear icon, however, only displays an information option from this page.
