---
title: "Building the Webforms Starter Kit"
id: 4415492663959
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492663959-Building-the-Webforms-Starter-Kit
updated_at: 2021-12-10T15:40:07Z
---

# Building the Webforms Starter Kit

# Building the Webforms Starter Kit

This guide will give you an overview of the major aspects of an Izenda integration with a webforms web application.

The purpose of the guide is to abstract from the core of the Izenda Webforms Starter Kit guide the overarching concepts of back end and front-end integration.

Many of the concepts executed upon in the integration sections of this guide can be re-used in other applications, .NET or otherwise.

The three major features of an Izenda integration, and the three major sections of this summary section are as follows:

* Front-end Integration
* Security Handshake
* Back-end Integration

## Front-end Integration

Front-end integration with Izenda involves taking the EmbeddedUI codebase and integrating it with an existing application’s front-end codebase and placing it behind that application’s authentication process.

Izenda’s EmbeddedUI is based upon the ReactJS framework. It is lightweight, easy to embed, and works with most modern web technologies, whether it’s another JavaScript framework like Angular, or application technologies like .NET, Java, PHP, Python, or Ruby.

The EmbeddedUI provides access to the Izenda Synergy JavaScript function library which allows for easy rendering of Izenda’s front-end containers throughout the target application.

You can learn more about the IzendaSynergy configuration, authentication, and render functions in the [Front-end Integration API documentation](https://devnet.logianalytics.com/hc/en-us/articles/4415492642455-Front-end-Integration-APIs).

### Integrating the Embedded UI

This is as simple as just dropping in the Izenda EmbeddedUI Code base.

Once the Izenda ReactJS library is present you’ll have direct access to the IzendaSynergy render functions.

This is done in the [Copying Izenda Resources and References](#Copying) section of the guide below.

### The Izenda.integrate.js file

This file is a good representation of how to bundle together IzendaSynergy configuration, authentication, and render functions.

You may choose to create a similar file in your own application code base as it greatly simplifies the amount of on page code you might write to manage your resource references, API endpoint references, passing of the Izenda currentusercontext token, and specific render function.

This is done in the [Copying Izenda Resources and References](#Copying) section of the guide below.

You can view the contents of Izenda.integrate.js [here](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/Scripts/izenda.integrate.js).

### Using the render functions

Once the Embedded UI front-end resources are in place, and we’ve configured the configuration, authentication, and render functions. The last thing to do is use these bundled JavaScript functions within our application’s front-end to render specific Izenda containers/pages.

This is done in the [Embedded Front-end](#Embeddin) section of the guide below.

## Security Handshake

The basic Izenda security handshake is handled through a token which contains two key pieces of user metadata, a unique user identifier, and a unique tenant identifier. You’ll handle role level details through the back-end integration.

The point here is to create the medium through which Izenda will authenticate interactions between the front-end and back-end API endpoints.

In the [IzendaConfig](#IzendaConfig) section we’ll create the token for the end-user authentication that will eventually be passed to Izenda’s API endpoints through IzendaSynergy currentUserContext.

As you’ll see in that section, that token contains two values originating from the application’s tenant and user store.

We then pass these values through the token we create along with Izenda’s render functions in the Izenda.integrate.js file.

There is no separate login process for Izenda specifically, rather Izenda just sits behind the existing application’s authentication process and inherits a few key values.

You can see an example of the token getting passed into Izenda’s currentUserContext in [izenda.integrate.js](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/Scripts/izenda.integrate.js).

Most of the work here is done in the [Custom Authentication Logic](#Custom2) section of the guide below.

There is work beyond just generating the handshake token in that section, as there is additional configuration being done specific to the application to add a Tenant concept to its security model.

## Back-end Integration

Through front-end integration we are rendering pages, parts, and containers. Through the security handshake we are placing Izenda behind an existing authentication process.

Through back-end integration we are using hooks within Izenda to inherit an existing security model.

The basic concept here is that we want to populate existing tenant, role, and user associations in Izenda.

Now, when users are authenticated, Izenda will be able to appropriately govern what data, features, and reports or dashboards it might expose to the end-user. You can also define these permissions through the EmbeddedUI interfaces, C#, or API endpoints.

This can be done through either exposed C# methods, or through REST API endpoints.

### Back-end Integration through C#

This method of back-end integration is typically done when integrating with other .NET web applications, however you might use this approach in scenarios where you would want Izenda to pull (through LINQ expressions, SQL Queries, Web Services, or other REST APIs) the Tenant, Role, and User Metadata you would like Izenda to inherit.

Sample Starter Kit

The Webforms Starter Kit demonstrates the C# method approach in depth. This application has both the Izenda EmbeddedUI and API as a part of its codebase, with no components of Izenda running separately.

Most of the interaction is done in the [Register.aspx code-behind](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/Account/Register.aspx.cs).

In that file, you can see several references to Izenda DLLs which provide access to exposed methods and classes that are relevant to managing Tenants, Roles, and Users programmatically.

We are syncing between the webforms application’s security model and Izenda’s to make them essentially equivalent.

You can see starting [here](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/Account/Register.aspx.cs#L20) that we are using methods to pass values directly from the webforms application’s security model into Izenda’s by equivocating the webforms application’s Tenant, Role, and User variables with Izenda’s. While some areas of this code contain hard-coded values, in real world implementations those values would get replaced with variables or lookups.

Much of the code used in the register page’s logic is supported by contents of the [IzendaBoundary](https://github.com/Izenda7Series/WebFormsStarterkit/tree/master/WebFormsStarterKit/IzendaBoundary) directory and [Models](https://github.com/Izenda7Series/WebFormsStarterkit/tree/master/WebFormsStarterKit/Models) from the webforms kit.

### Back-end Integration through the API

Currently there is no webforms kit that implements Izenda through REST API calls. For an example that uses the REST API, you can review the [MVC5 back-end standalone](https://devnet.logianalytics.com/hc/en-us/articles/4415511901719-Deployment-Mode-1-Key-Components-for-Integration#_bm9) documentation and example kit to learn about that approach.

## Other Integration Concepts

Beyond front-end, handshake, and back-end, there’s of course an expectation that you’ll want to white label Izenda, integrate with a specific deployment model, and manage record level data permissions beyond what you might define at a Tenant and Role level in Izenda.

There are many more capabilities and features you may want to explore.

Please reference our GitHub, documentation site, and developer guides for more:

* [GitHub](https://github.com/Izenda7Series)
* Izenda Docs
* [Developer Guide](https://devnet.logianalytics.com/hc/en-us/articles/4415511884055-Developer-Guide)

### White Labeling

Izenda provides a fully exposed presentation layer, which includes exposed CSS files.

[Customizing Izenda’s CSS](https://devnet.logianalytics.com/hc/en-us/articles/4415504575767-Izenda-BI-CSS)

### Deployment Modes

You may need to integrate only specific areas of Izenda’s codebase, depending upon your integration goals, deployment style, and application technology.

[Understanding The Three-tiered Architecture](https://devnet.logianalytics.com/hc/en-us/articles/4415492694039-Understanding-The-Three-tiered-Architecture).

### Hidden Filters

Hidden Filters in Izenda are the mechanism by which you can dynamically append to the WHERE clause of Izenda’s queries to ensure it only pulls back highly personalized record sets from your data sources.

See: [SetHiddenFilters](https://devnet.logianalytics.com/hc/en-us/articles/4415504593303-IAdHocExtension#_bm21).

## Webforms Integration

This tutorial will teach you the basics of embedding Izenda into an ASP.NET webforms application using Visual Studio 2015.

Download the [completed project](https://github.com/Izenda7Series/WebFormsStarterkit). This is important! You’ll need to use files and code samples from this codebase throughout the guide.

This starter kit will guide you through the implementation and deployment of the full integration mode, this means both front-end (UI) and back-end (API Service) are integrated into one webforms application.

See more details for [Deployment Mode 1: Back End Standalone, Front End Integrated](https://devnet.logianalytics.com/hc/en-us/articles/4415492694039-Understanding-The-Three-tiered-Architecture#Deployme).

## Prerequisites

To complete this walkthrough, you will need the following:

* Visual Studio 2015
* .NET Version 4.5.2
* Izenda API package
* Izenda Embedded UI package
* Sql Server 2016

The Izenda API service is built on .NET framework 4.0. You can build your integrated application on .NET Framework 4.0 or higher to be compatible with the Izenda API. This document will guide you step by step on integrating Izenda into your application. Please note this guide was developed using the versions of each component specified above. For more details on supported components please see other sections in the Izenda documentation.

## Create Your webforms Starter Kit Application

Open Visual Studio IDE then select menu New > New Project

[![../_images/mvc_new_project.png](https://devnet.logianalytics.com/hc/article_attachments/4415504316951/mvc_new_project_509x132.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504316695/mvc_new_project.png)

On New Project dialog, select Templates > Visual C# > Web then select target .NET Framework and ASP.NET Web Application.

Name your project “WebFormsStarterKit” then click OK. This is important! It will affect reference names throughout the code base.

In the New ASP.NET Project dialog, click Web Forms and click Change Authentication then chose Individual User Accounts, click OK buttons to close dialogs.

[![../_images/webforms_new_project.png](https://devnet.logianalytics.com/hc/article_attachments/4415492422935/webforms_new_project_590x461.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504317207/webforms_new_project.png)

The default template of a webforms application will be created. You will use this template to implement Izenda fully integrated into the application.

## Copying Izenda Resources and References

In Solution Explorer of WebFormsStarterKit project, add new folders below:

* IzendaBoundary
* IzendaReferences
* IzendaResources
* Scripts\izenda

Copy Izenda Resource to starter kit project:

* Download and copy [izendadb.config](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/izendadb.config) file into ~\WebFormsStarterKit
* Download latest Izenda API package (API.zip) extract zip file and then:
  + Copy all sub folders and files in ~\API\bin to ~ \WebFormsStarterKit\IzendaReferences
  + Copy 3 folders API\Content, API\EmailTemplates and API\Export to ~ \WebFormsStarterKit\IzendaResources
* Download latest Izenda Embedded UI package (EmbeddedUI.zip), extract zip file then copy all sub folders and files to ~\WebFormsStarterKit\Scripts\izenda
* Download [izenda.integrate.js](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/Scripts/izenda.integrate.js), [izenda.utils.js](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/Scripts/izenda.utils.js) and [alertify.js](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/Scripts/alertify.js) then copy to ~\WebFormsStarterKit\Scripts
* Download [alertify.css](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/Content/alertify.css) and copy to ~\WebFormsStarterKit\Content

## Configuring the Project Build

### Add Izenda DLLs reference and other dependencies

1. Right click Reference node in the WebFormsStarterKit Solution Explorer then select Add Reference…

   [![../_images/webforms_add_reference.png](https://devnet.logianalytics.com/hc/article_attachments/4415492423191/webforms_add_reference_361x382.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504317463/webforms_add_reference.png)
2. On Reference Manager dialog click Browse… button then browse to folder ~\WebFormsStarterKit\IzendaReferences, select all DLL files to reference but ignore below dlls (because those dlls have already been referenced in the webforms project template by default):

   * Microsoft.Web.Infrastructure.dll
   * Newtonsoft.Json.dll

   Note

   In this step if you encounter errors regarding reference conflicts, you must configure Redirecting Assembly as required or contact Izenda Support.
3. You also need to add System.ComponentModel.Composition.   
   Go to Add References again, Assemblies-> Framework and check System.ComponentModel.Composition.
4. Finally, go to Tools->NuGet Packet Manager->Package Manager Console and run the following:

   ```
   Install-Package Microsoft.AspNet.WebApi.ClientInstall-Package Microsoft.AspNet.WebApi.CoreInstall-Package Microsoft.AspNet.WebApi.WebHost
   ```

### Adding post build events to copy the resources

Adding post build events to copy the resources
Open Project Properties page select Build Events then click Edit Post-build… button and then enter the commands below into Post-build event command line box:

```
XCOPY /S /I /Y  "$(ProjectDir)IzendaResources\Content" "$(ProjectDir)\bin\Content\"XCOPY /S /I /Y  "$(ProjectDir)IzendaResources\EmailTemplates" "$(ProjectDir)\bin\EmailTemplates\"XCOPY /S /I /Y  "$(ProjectDir)IzendaResources\Export" "$(ProjectDir)\bin\Export\"
```

[![../_images/webforms_post_build_events.png](https://devnet.logianalytics.com/hc/article_attachments/4415511697943/webforms_post_build_events_806x425.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504317719/webforms_post_build_events.png)

## Configuring the Script and Style Bundle

Open ~\WebFormsStarterKit\App\_Start\BundleConfig.cs then config for Izenda as below:

```
bundles.Add(newScriptBundle("~/bundles/jquery").Include("~/Scripts/jquery-{version}.js"));bundles.Add(newScriptBundle("~/bundles/bootstrap").Include("~/Scripts/bootstrap.js","~/Scripts/respond.js"));//#izendabundles.Add(newScriptBundle("~/bundles/izenda").Include("~/Scripts/izenda/izenda_common.js","~/Scripts/izenda/izenda_locales.js","~/Scripts/izenda/izenda_vendors.js","~/Scripts/izenda/izenda_ui.js","~/Scripts/izenda.integrate.js","~/Scripts/izenda.utils.js","~/Scripts/alertify.js"));
```

[View Code Here](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/App_Start/BundleConfig.cs)

Open ~\Site.master and add CSS and bundle scripts:

```
<title><%:Page.Title%>-MyASP.NETApplication</title><%--Applycssforizenda--%><linkhref="~/Scripts/izenda/izenda-ui.css"rel="stylesheet"><linkhref="~/favicon.ico"rel="shortcut icon"type="image/x-icon"/><webopt:bundlereferencerunat="server"path="~/Content/css"/></head><body><asp:PlaceHolderrunat="server"><%:Scripts.Render("~/bundles/modernizr")%><%--Izenda--%><%:Scripts.Render("~/bundles/jquery")%><%:Scripts.Render("~/bundles/bootstrap")%><%:Scripts.Render("~/bundles/izenda")%></asp:PlaceHolder>
```

## Configuring the Routes

Open ~\WebFormsStarterKit\App\_Start\RouteConfig.cs then modify the routing config as shown below:

```
publicstaticclassRouteConfig{publicstaticvoidRegisterRoutes(RouteCollectionroutes){//Thisrouteisusedforexportingimagefromhtmlcontentroutes.MapPageRoute("ReportPart","viewer/reportpart/{id}","~/Report/ReportPart.aspx");//Thisrouteisusedforexportingsubscriptionreportroutes.MapPageRoute("ReportViewer","report/view/{id}","~/Report/ReportViewer.aspx");//Thisrouteisusedforexportingsubscriptiondashboardroutes.MapPageRoute("DashboardViewer","dashboard/view/{id}","~/Dashboard/DashboardViewer.aspx");routes.Ignore("izapi/{*pathInfo}");varsettings=newFriendlyUrlSettings();settings.AutoRedirectMode=RedirectMode.Permanent;routes.EnableFriendlyUrls(settings);}}}
```

[View Code Here](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/App_Start/RouteConfig.cs)

The statement `routes.IgnoreRoute("izapi/{*pathInfo}")` is important, do not miss it. This route will instruct the web infrastructure routine to ignore any request API that begins with the `izapi/` prefix (instead of handling the request as a route, the application will treat it as an API Service request), and this prefix must have the same value as the Izenda API prefix setting `<addkey="izendaapiprefix"value="izapi"/>` that you will configure in the section [Izenda API Service Hosting Config](#Izenda_API_Service_Hosting_Config) later.

Some of the routing configuration may seem strange, but it will be explained later. The table below details the purpose of each URL route:

| Name | URL | Description |
| --- | --- | --- |
| ReportPart | viewer/reportpart/{id} | This route is used by the Izenda BE Service to capture html content of the report part types chart, gauge or map. Mostly used for report exporting functions. |
| ReportViewer | report/view/{id} | This route is used by the Izenda BE Service to capture report content in html format. It is using in exporting report content to embedded html and sending it to email (send to email directly or send via the report subscription function). |
| DashboardViewer | dashboard/view/{id} | The route used by the Izenda BE Service to capture dashboard content in html format. Used for exporting dashboard content to email. |

## Setting up the Database

In this starter kit, we use SQL Server for the database server. Izenda supports many database engines such as: [MSSQL] SQL Server, [AZSQL] AzureSQL, [MYSQL] MySQL, [ORACL] Oracle, and [PGSQL] PostgreSQL. The steps to setting up these databases are similar.

### Create Izenda DB

On your SQL Server, create an empty database named IzendaWebForms. This database stores Izenda data (report definitions, dashboards, etc.) and the configuration necessary to run Izenda.

Download [IzendaWebForms.sql](https://raw.githubusercontent.com/Izenda7Series/WebFormsStarterkit/master/SQLScript/MSSQL/IzendaWebForms.sql) then execute the script on your IzendaWebForms database to generate the schema and default data.

### Updating the Izenda DB

The IzendaWebForms.sql script will generate a configuration database for Izenda 2.6.20.

If you use an EmbeddedUI and API for a later version of Izenda you will need to run update scripts against your IzendaWebForms database. You can find a tool to generate the required scripts [here](https://tools.izenda.com/).

For example, if you deploy version 2.11.1 of the EmbeddedUI and API, you would select v2.6.20 as your current version and v2.11.1 as your target version and (for the purposes of this tutorial) [MSSQL] SQLServer as your database type. You can choose to download the script as a SQL file or (if the check box is unchecked) view the file directly in your browser window.

### Create Authentication DB

On your SQL Server, create an empty database named WebFormsStarterKit. This database is used for storing user authentication information for the webforms kit. In your real integrated application, it can be replaced by your system database with your custom user credential information.

Download [WebFormsStarterKit.sql](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/SQLScript/MSSQL/WebFormsStarterKit.sql) and execute the script on your WebFormsStarterKit database to generate the schema and default user authentication settings. These settings mirror the Izenda configuration database user data as closely as possible.

### Verifying Izenda DB and Authentication DB

After creating the IzendaDB, select all rows in the IzendaSystemSetting table and verify that the values are the same as below:

| Name | Value | Description |
| --- | --- | --- |
| DeploymentMode | 3 | The setting for deployment mode, in this starter kit it is fully integrated. |
| WebUrl | <http://localhost:14909/> | The setting value must be the base address of your front-end web page url. |

Next you must ensure the UserName value of the records in the AspNetUsers table in WebFormsStarterKit DB are matched with the UserName value in the IzendaUser table of IzendaWebForms DB.

## Configuring the Izenda API Service

The full configuration file [Web.config](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/Web.config) of Izenda API Service is available on GitHub.

[View Code Here](https://raw.githubusercontent.com/Izenda7Series/WebFormsStarterkit/master/WebFormsStarterKit/Web.config)

### Izenda API Service Hosting Config

Izenda uses the Nancy Framework to host the REST API service. To configure Nancy, open the WebFormsStarterKit\Web.config and add a new section like below:

```
<configuration><configSections><!-- Izenda--><sectionname="nancyFx"type="Nancy.Hosting.Aspnet.NancyFxSection"/><sectionname="log4net"type="log4net.Config.Log4NetConfigurationSectionHandler, log4net, Version=1.2.15.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a"/><!-- Izenda - End --><!-- For more information on Entity Framework configuration, visit http://go.microsoft.com/fwlink/?LinkID=237468 --><sectionname="entityFramework"type="System.Data.Entity.Internal.ConfigFile.EntityFrameworkSection, EntityFramework, Version=6.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"requirePermission="false"/></configSections><!--Izenda--><nancyFx><bootstrapperassembly="Izenda.BI.API"type="Izenda.BI.API.Bootstrappers.IzendaBootstraper"/></nancyFx>
```

Then add the following email config after `</nancyFx>` close tag:

```
<nancyFx><bootstrapperassembly="Izenda.BI.API"type="Izenda.BI.API.Bootstrappers.IzendaBootstraper"/></nancyFx><system.net><mailSettings><smtpdeliveryMethod="Network"from=""><networkdefaultCredentials="false"host=""enableSsl="true"port="587"userName=""password=""/></smtp></mailSettings></system.net><!-- Izenda End -->
```

Add below Izenda setting key into <appSettings> node:

```
<appSettings><!--Izenda--><addkey="izendaapiprefix"value="izapi"/><addkey="izedapassphrase"value="vqL7SF+9c9FIQEKUOhSZapacQgUQh"/><addkey="IzendaApiUrl"value="http://localhost:14909/izapi/"/><addkey="izusername"value="IzendaAdmin@system.com"/><addkey="iztenantname"value=""/><!--Izenda End--></appSettings>
```

| Key Name | Value | Description |
| --- | --- | --- |
| `izendaapiprefix` | izapi | This is prefix of your Izenda API service, it is used for distinguish the Izenda API with other api in your application if it exposes more than one service endpoint. |
| `izendapassphrase` | vqL7SF+9c9FIQEKUOhSZapacQgUQh | The key used for encryption |
| `IzendaApiUrl` | <http://localhost:14909/izapi/> | Your Izenda API endpoint, used to call the Izenda API in your .NET code |
| `izusername` | [IzendaAdmin@system.com](mailto:IzendaAdmin%40system.com) | Default system level account, in this kit it is used for authentication of specific functions like adding new users, updating the data model, etc. This value must match with the Username in the WebFormsStarterKit.AspNetUsers and IzendaWebForms.IzendaUser tables. |
| `iztenantname` | [blank] | The tenant of the system level account. This serves the same purpose as the `izusername` setting and equates to the “System” value in the WebFormsStarterKit.Tenants but does not have a corresponding entry in the IzendaWebForms.IzendaTenant table. The system tenant is implicitly null in Izenda. |

In <system.webServer> config node, add below config:

```
<system.webServer><modules><removename="FormsAuthentication"/></modules><!--Izenda--><handlers><removename="ExtensionlessUrlHandler-Integrated-4.0"/><removename="OPTIONSVerbHandler"/><removename="TRACEVerbHandler"/><addname="ExtensionlessUrlHandler-Integrated-4.0"path="*."verb="*"type="System.Web.Handlers.TransferRequestHandler"preCondition="integratedMode,runtimeVersionv4.0"/><addname="Nancy"verb="*"type="Nancy.Hosting.Aspnet.NancyHttpRequestHandler"path="izapi/*"/></handlers><httpProtocol><customHeaders><addname="Access-Control-Allow-Origin"value="*"/><addname="Access-Control-Allow-Headers"value="Accept, Origin, Content-Type, access_token, current_tenant"/><addname="Access-Control-Allow-Methods"value="GET, POST, PUT, DELETE, OPTIONS"/></customHeaders></httpProtocol><httpErrorsexistingResponse="PassThrough"/><!--Izenda end--></system.webServer>
```

This config includes the http header attribute and api action verb for the Izenda API. It is also used to configure the http handler for the API url convention which will be reserved by the Izenda API Service. Using the config above, all API urls with a prefix of izapi/ will be handled by Izenda. Recall that this handler API prefix must match the value of the `izendaapiprefix` setting.

### Logging Config

In <configSections> add a new section to configure logging for the Izenda API.

```
<!-- Izenda--><sectionname="nancyFx"type="Nancy.Hosting.Aspnet.NancyFxSection"/><sectionname="log4net"type="log4net.Config.Log4NetConfigurationSectionHandler, log4net, Version=1.2.15.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a"/><!-- Izenda - End -->
```

Then add a new log4net node in the config file as well:

```
<log4netthreshold="ALL"debug="false"><root><appender-refref="OutputDebugStringAppender"/><!--<appender-ref ref="RollingFileAppender" />--></root><!--WebFormsStarterKit Logger--><loggername="WebFormsStarterKit"additivity="false"><levelvalue="ALL"/><appender-refref="WebFormsKitAppender"/></logger><!--Izenda.BI Logger--><loggername="Izenda.BI"additivity="false"><levelvalue="ALL"/><appender-refref="RollingFileAppender"/></logger><!--/// Log file. ///--><appendername="RollingFileAppender"type="log4net.Appender.RollingFileAppender,log4net, Version=1.2.15.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a"><filtertype="log4net.Filter.LevelRangeFilter, log4net, Version=1.2.15.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a"><levelMinvalue="INFO"/></filter><filevalue="logs\izenda-log.log"/><!-- Uncomment when sharing log files      <lockingModel type="log4net.Appender.FileAppender+InterProcessLock, log4net, Version=1.2.15.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a"/>      --><appendToFilevalue="true"/><rollingStylevalue="Composite"/><datePatternvalue="yyyyMMdd"/><staticLogFileNamevalue="true"/><preserveLogFileNameExtensionvalue="true"/><maximumFileSizevalue="5MB"/><maxSizeRollBackupsvalue="1000"/><layouttype="log4net.Layout.PatternLayout,log4net, Version=1.2.15.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a"><paramname="ConversionPattern"value=" %date [%-5thread][%-5level][%-36logger{1}] %message %newline"/></layout></appender><appendername="WebFormsKitAppender"type="log4net.Appender.RollingFileAppender,log4net, Version=1.2.15.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a"><filtertype="log4net.Filter.LevelRangeFilter, log4net, Version=1.2.15.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a"><levelMinvalue="INFO"/></filter><filevalue="logs\webforms-kit.log"/><appendToFilevalue="true"/><rollingStylevalue="Composite"/><datePatternvalue="yyyyMMdd"/><staticLogFileNamevalue="true"/><preserveLogFileNameExtensionvalue="true"/><maximumFileSizevalue="5MB"/><maxSizeRollBackupsvalue="1000"/><layouttype="log4net.Layout.PatternLayout,log4net, Version=1.2.15.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a"><paramname="ConversionPattern"value=" %date [%-5thread][%-5level][%-36logger{1}] %message %newline"/></layout></appender><!--/// DebugView Trace. ///--><appendername="OutputDebugStringAppender"type="log4net.Appender.OutputDebugStringAppender,log4net, Version=1.2.15.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a"><layouttype="log4net.Layout.PatternLayout,log4net, Version=1.2.15.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a"><paramname="ConversionPattern"value="[%-5level][%-24logger{1}/%line] %message (/T:%thread /D:%date) %newline"/></layout></appender></log4net>
```

### Configuring Database Connection

Open ~\ WebFormsStarterKit\izendadb.config then update the connection string to your IzendaWebForms DB which was created in the steps above. For example with [MSSQL] SQLServer:

```
{"ServerTypeId":"572bd576-8c92-4901-ab2a-b16e38144813","ServerTypeName":"[MSSQL] SQLServer","ConnectionString":"[your connection string to IzendaMvc]","ConnectionId":"00000000-0000-0000-0000-000000000000"}
```

The `ServerTypeName` would be one of the following: [MSSQL] SQL Server, [AZSQL] AzureSQL, [MYSQL] MySQL, [ORACL] Oracle, or [PGSQL] PostgreSQL. The ServerTypeId mappings are listed below.

| DatasourceName | Id |
| --- | --- |
| [AZSQL] AzureSQL | d968e96f-91dc-414d-9fd8-aef2926c9a18 |
| [MYSQL] MySQL | 3d4916d1-5a41-4b94-874f-5bedacb89656 |
| [ORACL] Oracle | 93942448-c715-4f98-85e2-9292ed7ca4bc |
| [PGSQL] PostgreSQL | f2638ed5-70e5-47da-a052-4da0c1888fcf |
| [MSSQL] SQLServer | 572bd576-8c92-4901-ab2a-b16e38144813 |

Next, open ~\WebFormsStarterkit\Web.config again and modify the DefaultConnection value in the connectionStrings node to configure the Webforms application database link:

```
<connectionStrings><addname="DefaultConnection"connectionString="Server=[computername]\[databaseServerName];Database=WebFormsStarterKit;User Id=[userid];Password=[password];"providerName="System.Data.SqlClient"/></connectionStrings>
```

## The first run of Izenda API Service

### 64-bit Oracle DLL Dependencies

If you encounter an error related to OracleDataAccesssDTC in Visual Studio, navigate to Tools -> Options -> Projects and Solutions -> Web Projects -> Check “Use the 64 bit version of IIS Express for web sites and projects”.

[![../_images/mvc_64bit_iis_express.png](https://devnet.logianalytics.com/hc/article_attachments/4415492423959/mvc_64bit_iis_express_560x327.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504318487/mvc_64bit_iis_express.png)

### Run Starter Kit

Before you run your starter kit, ensure the Project Url setting in your project settings is set to use the same port that you configured for your `IzendaApiUrl` setting in your web.config.

With that minor detail taken care of, you can press F5 in visual studio to run your starter kit for the first time. The application page will look like the screenshot below:

[![../_images/webforms_run_starter_kit.png](https://devnet.logianalytics.com/hc/article_attachments/4415492424727/webforms_run_starter_kit_900x526.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492424343/webforms_run_starter_kit.png)

There is nothing present from the Izenda UI at this time. At this step we are just checking whether Izenda API is able to start up completely or not. On your browser address add /api/ to the end of url (<http://localhost:14809/api/>) then press enter, you will see Izenda API is hosted completely:

[![../_images/webforms_api_url_404.png](https://devnet.logianalytics.com/hc/article_attachments/4415492424983/webforms_api_url_404_900x411.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504321431/webforms_api_url_404.png)

In the ~\WebFormsStarterkit project folder you will see a logs folder with the log files webforms-kit.log and izenda-log.log (~\WebFormsStarterkit\logs).

### Izenda API Hosting Troubleshooting

If you do not see the log files and 404 page above, check the following:

* Nancy hosting configuration is correct in the Web.config
* Ensure Nancy.dll and Nancy.Hosting.Aspnet.dll are referenced in the project.
* Check your routing configuration in RouteConfig.cs

## Adding Izenda Boundary

Get all files in the [IzendaBoundary](https://github.com/Izenda7Series/WebFormsStarterkit/tree/master/WebFormsStarterKit/IzendaBoundary) folder from the GitHub repository and include them in your WebFormsStarterkit project. Build the project. If there are any errors regarding missing references, update the references as needed.

The table below describes the functionality of each source code file:

| File and Folder | Classes | Description |
| --- | --- | --- |
| Models | Model Entity | Contains the definition of objects used for transferring model data when communicating between your code and the Izenda API. |
| CustomAdhocReport.cs | CustomAdhocReport | Contains an implementation the IAdHocExtension interface that is used to override many default functions in your Izenda installation. This extension will be automatically located and injected into the runtime by the Izenda API application. More information on this can be found [here](https://devnet.logianalytics.com/hc/en-us/articles/4415504593303-IAdHocExtension) |
| IzendaTokenAuthorization.cs | IzendaTokenAuthorization | The helper class used to decrypt and deserialize the authentication token corresponding to the UserInfo object and vice versa (serialize UserInfo object then encrypt to token key. The UserInfo object will be added below). |
| IzendaUtility.cs | IzendaUtility | The helper class to access specific Izenda REST APIs to get connection, tenant, role, and user info from Izenda. |
| StringCipher.cs | StringCipher | The helper class to encrypt and decrypt the UserInfo and authentication token between each other. |
| WebAPIService.cs | WebAPIService | The service proxy class that provides the framework for making REST API requests to Izenda using Izenda authentication tokens. |

These classes just demonstrate simple examples of using each functionality. It is recommended that in your actual integration you use security best practices that follow your organization’s established security policies and procedures.

## Custom Authentication Logic

In this starter kit, we use simple authentication with only a username, password and tenant info. Basically, authorization logic (role, permissions …etc.) will depend on the implementation of the Izenda BE.

If you recall, in the WebFormsStarterkit database we added a table named Tenants and a column in the AspNetUsers table named TenantID. Those objects normally don’t exist in a standard Webforms kit. The TenantID column is a foreign key reference to the Tenants table which demonstrates a one-to-many relationship between Tenant and User. The other tables are kept same as in a webforms template project. This helps us minimize the changes in the login logic, but allows us to show a simple use case for multi-tenant support.

[![../_images/mvc_AspNetUsers_Tenants.png](https://devnet.logianalytics.com/hc/article_attachments/4415504323351/mvc_aspnetusers_tenants_419x285.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504323095/mvc_aspnetusers_tenants.png)

In integrated mode, authentication is handled by the webforms application, not Izenda. In this starter kit, the Izenda backend will get a token via the `UserIntegrationConfig.GetAccessToken` method. You must implement your own code logic to provide this token containing the authenticated user’s information. To ensure security, each request to the Izenda API service will call back to the webforms application to validate the token it received from the originating request. You must provide this validation logic in your app inside the `UserIntegrationConfig.ValidateToken` method. The diagram below illustrates the token retrieval and validation process in fully integrated mode:

[![../_images/mvc_authentication_sequence_diagram.png](https://devnet.logianalytics.com/hc/article_attachments/4415511699607/mvc_authentication_sequence_diagram_500x235.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492425623/mvc_authentication_sequence_diagram.png)

To customize the authentication logic, we must modify some existing classes in the ASP.NET webforms application template. The table below lists all the modified classes and pages:

| File | Class | State | Description |
| --- | --- | --- | --- |
| IzendaConfig.cs | IzendaConfig | New | The extension class provides Izenda token and token validation for the Izenda backend. |
| Models\IdentityModels.cs | ApplicationUser | Modify | The entity class present user identity model. This model maps to AspNetUsers table. |
| Models\IdentityModels.cs | Tenant | New | The entity model presents a tenant, maps to Tenants table. |
| Models\IdentityModels.cs | ApplicationDBContext | Modify | Entity Framework DB context. |
| App\_Start\IdentityConfig.cs | ApplicationUserManager | Modify | Manage authentication user and login context. |
| App\_Start\IdentityConfig.cs | ApplicationSignInManager | Modify | Custom sign in logic. |
| App\_Start\WebApiConfig.cs | WebApiConfig | Add | Required to handle a specific callback to the GenerateToken route |
| Account\Login.aspx | [N/A] | Modify | Include the tenant in the page. |
| Account\Login.aspx.cs | Login | Modify | Update login logic to use the customizations. |
| ApiControllers\UserController.cs | UserController | Add | Required for handling the GenerateToken route. |
| Global.asax.cs | Global | Modify | Implement the route mapping from the WebAPIConfig |

### IzendaConfig

Create IzendaConfig.cs file within the top level of the project and implement subscription for `UserIntegrationConfig.GetAccessToken` action and `UserIntegrationConfig.ValidateToken` action.

```
publicstaticclassIzendaConfig{publicstaticvoidRegisterLoginLogic(){UserIntegrationConfig.GetAccessToken=(args)=>{returnIzendaBoundary.IzendaTokenAuthorization.GetToken(newModels.UserInfo(){UserName=args.UserName,TenantUniqueName=args.TenantId});};UserIntegrationConfig.ValidateToken=(ValidateTokenArgsargs)=>{vartoken=args.AccessToken;varuser=IzendaBoundary.IzendaTokenAuthorization.GetUserInfo(token);returnnewValidateTokenResult{UserName=user.UserName,TenantUniqueName=user.TenantUniqueName};};}}
```

Action `UserIntegrationConfig.GetAccessToken` will convert user info to a token value.

Action `UserIntegrationConfig.ValidateToken` convert access token to user info.

### Identity Models – Namespaces

1. Open Models\IdentityModels.cs.
2. Add the following namespaces so that it appears as below:

```
usingSystem;usingSystem.Security.Claims;usingSystem.Threading.Tasks;usingSystem.Web;usingMicrosoft.AspNet.Identity;usingMicrosoft.AspNet.Identity.EntityFramework;usingSystem.ComponentModel.DataAnnotations.Schema;usingSystem.Linq;
```

### Identity Models – ApplicationUser class

1. Next in Models\IdentityModels.cs.
2. Add Tenant\_Id property and custom claim identity like below:

```
    // You can add User data for the user by adding more properties to your User class, please visit http://go.microsoft.com/fwlink/?LinkID=317594 to learn more.
							public class ApplicationUser : IdentityUser
							    {
							        public int Tenant_Id { get; set; }
							        [ForeignKey("Tenant_Id")]
							        public Tenant Tenant { get; set; }
							public async Task<ClaimsIdentity> GenerateUserIdentityAsync(UserManager<ApplicationUser> manager)
							{
							            // Note the authenticationType must match the one defined in CookieAuthenticationOptions.AuthenticationType
							            var userIdentity = await manager.CreateIdentityAsync(this, DefaultAuthenticationTypes.ApplicationCookie);
							            if (Tenant != null)
							            {
							                userIdentity.AddClaims(new[] {
							                    new Claim("tenantName",Tenant.Name),
							                    new Claim("tenantId",Tenant.Id.ToString()),
							                });
							            }
							            var role = (await manager.GetRolesAsync(this.Id)).FirstOrDefault();
							            userIdentity.AddClaim(new Claim(ClaimsIdentity.DefaultRoleClaimType, role));
							            // Add custom user claims here
							            return userIdentity;
							        }
						
```

The ApplicationUser class represents the user model and maps to the AspNetUsers table. The Tenant\_Id property is the foreign key reference to the tenant of the user. In the GenerateUserIdentityAsync method, we are adding the tenantId into the user identity. This value will be used to establish “claims” based on the user’s tenant.

### Identity Models – Tenant

1. Next in Models\IdentityModels.cs.
2. Add a new Tenant class to represent a tenant object. This class is an entity model that maps to the Tenants table. The example below utilizes a very simple tenant model. You can customize this model to store more complex information.

|  |  |
| --- | --- |
| ``` 1 										2 										3 										4 									5 ``` | ``` publicclassTenant{publicintId{get;set;}publicstringName{get;set;} ``` |

### Identity Models – ApplicationDBContext

This is the Entity Framework DB context of the entire authentication database. Because we added a new Tenants table, we must update the DB context to include our new model and link it to the entity.

```
publicclassApplicationDbContext:IdentityDbContext<ApplicationUser>{publicApplicationDbContext():base("DefaultConnection",throwIfV1Schema:false){}publicstaticApplicationDbContextCreate(){returnnewApplicationDbContext();}}}
```

If your starter kit contains another ApplicationDBContext definition, you may need to remove the duplicate to prevent errors.

### Identity Config – Namespaces

1. Open App\_Start\IdentityConfig.cs.
2. Add the following namespaces so that it appears as below:

```
usingSystem;usingSystem.Data.Entity;usingSystem.Linq;usingSystem.Security.Claims;usingSystem.Threading.Tasks;usingMicrosoft.AspNet.Identity;usingMicrosoft.AspNet.Identity.EntityFramework;usingMicrosoft.AspNet.Identity.Owin;usingMicrosoft.Owin;usingMicrosoft.Owin.Security;usingWebFormsStarterKit.Models;
```

### Identity Config – ApplicationUserManager

1. Next in App\_Start\IdentityConfig.cs.
2. Add a new method to the ApplicationUserManager class called FindTenantUserAsync. This will be used to query and retrieve users by tenant, username, and password.

```
publicasyncTask<ApplicationUser>FindTenantUserAsync(stringtenant,stringusername,stringpassword){varcontext=ApplicationDbContext.Create();varuser=awaitcontext.Users.Include(x=>x.Tenant).Where(x=>x.UserName.Equals(username,StringComparison.InvariantCultureIgnoreCase)).Where(x=>x.Tenant.Name.Equals(tenant,StringComparison.InvariantCultureIgnoreCase)).SingleOrDefaultAsync();if(awaitCheckPasswordAsync(user,password))returnuser;returnnull;}
```

### Identity Configs – ApplicationSignInManager

1. Next in App\_Start\IdentityConfig.cs.
2. Add a new method PasswordSigninAsync to customize sign in logic. This method utilizes the FindTenantUserAsync method added above to find a user with the specified username, password and tenant.

```
publicclassApplicationSignInManager:SignInManager<ApplicationUser,string>{publicApplicationSignInManager(ApplicationUserManageruserManager,IAuthenticationManagerauthenticationManager):base(userManager,authenticationManager){}publicasyncTask<bool>PasswordSignInAsync(stringtenant,stringusername,stringpassword,boolremember){varappUserManager=this.UserManagerasApplicationUserManager;if(appUserManager==null){returnfalse;}varuser=awaitappUserManager.FindTenantUserAsync(tenant,username,password);if(user!=null){awaitSignInAsync(user,remember,true);returntrue;}returnfalse;}
```

### App\_Start - WebApiConfig

1. Create App\_Start\WebAPIConfig.cs
2. Add the following:

```
usingSystem;usingSystem.Collections.Generic;usingSystem.Linq;usingSystem.Web.Http;namespaceWebFormsStarterKit{publicstaticclassWebApiConfig{publicstaticvoidRegister(HttpConfigurationconfig){config.MapHttpAttributeRoutes();config.Routes.MapHttpRoute(name:"DefaultApi",routeTemplate:"api/{controller}/{id}",defaults:new{id=RouteParameter.Optional});}}}
```

### Login.aspx.cs - Namespace

1. Open Acount\Login.aspx.cs
2. Add the following namespaces so that it appears as below:

```
usingSystem;usingSystem.Globalization;usingSystem.Linq;usingSystem.Security.Claims;usingSystem.Threading.Tasks;usingSystem.Web;usingSystem.Web.UI;usingMicrosoft.AspNet.Identity;usingMicrosoft.AspNet.Identity.Owin;usingOwin;usingWebFormsStarterKit.Models;
```

### Login.aspx.cs

1. Next in Acount\Login.aspx.cs
2. In Login method, implement the ApplicationSignInMangager/PasswordSigninAsync method as shown below.

```
protectedasyncvoidLogIn(objectsender,EventArgse){if(IsValid){//ValidatetheuserpasswordvarsigninManager=Context.GetOwinContext().GetUserManager<ApplicationSignInManager>();//Thisdoen't count login failures towards account lockout//Toenablepasswordfailurestotriggerlockout,changetoshouldLockout:truevarresult=awaitsigninManager.PasswordSignInAsync(Tenant.Text,Email.Text,Password.Text,RememberMe.Checked);if(result)IdentityHelper.RedirectToReturnUrl(Request.QueryString["ReturnUrl"],Response);else{FailureText.Text="Invalid login attempt";ErrorMessage.Visible=true;}//varresult=signinManager.PasswordSignIn(Email.Text,Password.Text,RememberMe.Checked,shouldLockout:false);//switch(result)//{//caseSignInStatus.Success://IdentityHelper.RedirectToReturnUrl(Request.QueryString["ReturnUrl"],Response);//break;//caseSignInStatus.LockedOut://Response.Redirect("/Account/Lockout");//break;//caseSignInStatus.RequiresVerification://Response.Redirect(String.Format("/Account/TwoFactorAuthenticationSignIn?ReturnUrl={0}&RememberMe={1}",//Request.QueryString["ReturnUrl"],//RememberMe.Checked),//true);//break;//caseSignInStatus.Failure://default://FailureText.Text="Invalid login attempt";//ErrorMessage.Visible=true;//break;//}}}
```

### UserInfo

1. Create Models\UserInfo.cs
2. Add the following:

```
namespaceWebFormsStarterKit.Models{publicclassUserInfo{publicstringUserName{get;set;}publicstringTenantUniqueName{get;set;}}}
```

### Update Login Page

1. Open Account\Login.aspx
2. Replace the contents of this file with the following from the [GitHub WebFormsStarterKit equivalent](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/Account/Login.aspx). This will add a Tenant section to the login page.

```
<h4>Usealocalaccounttologin.</h4><hr/><asp:PlaceHolderrunat="server"ID="ErrorMessage"Visible="false"><pclass="text-danger"><asp:Literalrunat="server"ID="FailureText"/></p></asp:PlaceHolder><divclass="form-group"><asp:Labelrunat="server"AssociatedControlID="Tenant"CssClass="col-md-2 control-label">Tenant</asp:Label><divclass="col-md-10"><asp:TextBoxrunat="server"ID="Tenant"CssClass="form-control"/><asp:RequiredFieldValidatorrunat="server"ControlToValidate="Tenant"CssClass="text-danger"ErrorMessage="The tenant field is required"/></div></div><divclass="form-group"><asp:Labelrunat="server"AssociatedControlID="Email"CssClass="col-md-2 control-label">Email</asp:Label><divclass="col-md-10"><asp:TextBoxrunat="server"ID="Email"CssClass="form-control"TextMode="Email"/><asp:RequiredFieldValidatorrunat="server"ControlToValidate="Email"CssClass="text-danger"ErrorMessage="The email field is required."/></div></div>
```

### ApiControllers - UserController

1. Create ApiControllers\UserController.cs
2. Add the following:

```
usingSystem.Web.Http;usingMicrosoft.AspNet.Identity;namespaceWebFormsStarterKit.ApiControllers{[Authorize][RoutePrefix("api/user")]publicclassUserController:ApiController{[Authorize][HttpGet][Route("GenerateToken")]publicstringGenerateToken(){varusername=User.Identity.GetUserName();vartenantName=((System.Security.Claims.ClaimsIdentity)User.Identity).FindFirstValue("tenantName");varuser=newModels.UserInfo{UserName=username,TenantUniqueName=tenantName};vartoken=IzendaBoundary.IzendaTokenAuthorization.GetToken(user);returntoken;}}}
```

### global.asax.cs

1. Open global.asax.cs
2. Add the following code:

```
publicclassGlobal:HttpApplication{voidApplication_Start(objectsender,EventArgse){//CodethatrunsonapplicationstartupGlobalConfiguration.Configure(WebApiConfig.Register);RouteConfig.RegisterRoutes(RouteTable.Routes);BundleConfig.RegisterBundles(BundleTable.Bundles);IzendaConfig.RegisterLoginLogic();}}
```

## Run First Login

Press F5 to run application, navigate to login page and enter the values below for the respective fields:

* Tenant = System
* Email = [IzendaAdmin@system.com](mailto:IzendaAdmin%40system.com)
* Password = [Izenda@123](mailto:Izenda%40123)

Then click Login. You will see the home page with the logged in user’s email on top right of the page.

[![../_images/webforms_current_user_ui.png](https://devnet.logianalytics.com/hc/article_attachments/4415492426647/webforms_current_user_ui_730x312.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492426263/webforms_current_user_ui.png)

## Update Shared Layout

### Construct Izenda Menu Items

Open ~\Site.master then add menu items for Izenda pages:

```
<ulclass="nav navbar-nav"><li><arunat="server"href="~/">Home</a></li><li><arunat="server"href="~/About">About</a></li><li><arunat="server"href="~/Contact">Contact</a></li><%--Izenda--%><%if(Context.User.Identity.IsAuthenticated){%><li><arunat="server"href="~/IzendaRoot">Izenda</a></li><li><arunat="server"href="~/Settings">Settings</a></li><%--Reports--%><liclass="dropdown"><aclass="dropdown-toggle"data-toggle="dropdown"href="#">Reports<spanclass="caret"></span></a><ulclass="dropdown-menu"><li><arunat="server"href="~/Report/ReportDesigner">NewReport</a></li><li><arunat="server"href="~/Report/Reports">ReportList</a></li><%--AddtoreportViewertoDemo,hardcodeReportIDtolinkusertoaspecificreport-pleaseupdatethereportidwithonecreatedinyourenviroment--%><li><arunat="server"href="~/report/view/[your_report_id]">ReportViewer</a></li><li><arunat="server"href="~/Report/ReportParts">ReportParts</a></li></ul></li><%--Dashboards--%><liclass="dropdown"><aclass="dropdown-toggle"data-toggle="dropdown"href="#">Dashboards<spanclass="caret"></span></a><ulclass="dropdown-menu"><li><arunat="server"href="~/Dashboard/DashboardDesigner">NewDashboard</a></li><li><arunat="server"href="~/Dashboard/Dashboards">Dashboards</a></li><%--AddtodashboardViewertoDemo,hardcodeDashboardIDtolinkusertoaspecificdashboard-pleaseupdatethedashboardidwithonecreatedinyourenviroment--%><li><arunat="server"href="~/dashboard/view/[your_dashboard_id]">DashboardViewer</a></li></ul></li><%}%></ul>
```

Note that the menu redirects require the creation of several new pages. These will be created in a later section.

Important! The webforms starter project will include the main placeholder for body content inside a form tag. This will cause some Izenda buttons to improperly issue a ‘submit’ event. To fix this, place the following code

```
<divclass="container body-content"><asp:ContentPlaceHolderID="LoginContent"runat="server"></asp:ContentPlaceHolder></div></form><divclass="izenda-container body-content"><asp:ContentPlaceHolderID="MainContent"runat="server"></asp:ContentPlaceHolder></div><hr/><footer><p>&copy;<%:DateTime.Now.Year%>-MyASP.NETApplication</p></footer>
```

In addition, another change is required to allow the Login page to continue working. Notice that in the above sample, we have added another placeholder inside the form tag with the ID “LoginContent”. We will need to change the placeholder reference in Login.aspx to match.

```
<%@RegisterSrc="~/Account/OpenAuthProviders.ascx"TagPrefix="uc"TagName="OpenAuthProviders"%><asp:Contentrunat="server"ID="LoginContent"ContentPlaceHolderID="MainContent"><h2><%:Title%>.</h2><divclass="row">
```

Optional: Izenda uses a class called “container” with some CSS to scale Izenda’s components to fit the container’s size. The webforms sample project uses the container class to limit the available display area of contents. To expand the available space, you can perform the following actions:

Remove the container class completely from the nav bar

```
<divclass="navbar navbar-inverse navbar-fixed-top"><divclass="container"><divclass="navbar-header">
```

Change the container class to “izenda-container” in the body-content div

```
<divclass="izenda-container body-content"><asp:ContentPlaceHolderID="MainContent"runat="server"></asp:ContentPlaceHolder></div>
```

Add the following css to the Site.css file

```
.izenda-container{width:100%;height:100vh;min-height:100vh;}
```

### Implement Izenda Configuration Initialization

Add Javascript code below into the bottom of the Site.Master to initialize the Izenda Configuration and sub menu dropdown display. The function DoIzendaConfig() is located in ~\Scripts\izenda.integrate.js. It initializes the main config values needed to run Izenda’s integrated UI such as the API Service Url, the path of the Izenda embedded JavaScript package, custom CSS styling, Izenda UI routing config, and the request timeout.

```
    <%-- Izenda --%>
							    <script type="text/javascript">
							        $(document).ready(function () {
							            DoIzendaConfig();
							            $('[data-toggle="tooltip"]').tooltip();
							            $('[data-toggle="dropdown"]').dropdown();
							            $("#reportPartLoader").hide();
							            $("#reportPartLoaderText").hide();
							        });
							    </script>
							</body>
							</html>
						
```

## Embedding Front-end Izenda (Izenda UI)

### Embedding Izenda full page

Create ~\Izenda.aspx

This page is used to embedded the entire Izenda application into one view.

In this page, we will call the function izendaInit() defined in ~\Scripts\izenda.integrate.js. The full Izenda UI will be rendered when opening this page, including the ReportViewer, ReportDesigner, Dashboard, and Setting pages. Navigation will be fully contained within the single page.

```
<%@ Page Title="Izenda" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Izenda.aspx.cs" Inherits="WebFormsStarterKit.IzendaRoot" %>
							<asp:Content ID="IzendaContent" ContentPlaceHolderID="MainContent" runat="server">
							<script type="text/javascript">
							$(document).ready(function () {
							izendaInit();
							});
							</script>
							<div class="loader" id="progressLoader"></div>
							<div class="izenda-container" id="izenda-root"></div>
							</asp:Content>
						
```

We have 2 empty div elements for each Izenda page. The `loader` div is used for displaying the progress bar when the page is waiting for a response from the Izenda back-end. The div `izenda-container` is the container for Izenda page content.

### Embedding Specific Izenda Pages

#### Embedding the Izenda Settings Page

Create ~\Settings.aspx

```
<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Settings.aspx.cs" Inherits="WebFormsStarterKit.Settings" %>
								<asp:Content ID="SettingsContent" ContentPlaceHolderID="MainContent" runat="server">
								<script type="text/javascript">
								$(document).ready(function () {
								izendaInitSetting();
								});
								</script>
								<div class="loader" id="progressLoader"></div>
								<div class="izenda-container" id="izenda-root"></div>
								</asp:Content>
							
```

The struture here is very similar to the Izenda.aspx page, as it contains the same elements, but this will specifically embed the Settings page into the page.

#### Embedding the Izenda Report List Page

Create ~\Report\Reports.aspx:

```
<%@ Page Title="Report List" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Reports.aspx.cs" Inherits="WebFormsStarterKit.Report.Reports" %>
								<asp:Content ID="ReportsContent" ContentPlaceHolderID="MainContent" runat="server">
								<script type="text/javascript">
								$(document).ready(function () {
								izendaInitReport();
								});
								</script>
								<div class="loader" id="progressLoader"></div>
								<div class="izenda-container" id="izenda-root"></div>
								</asp:Content>
							
```

Continue following the pattern of calling the appropriate javascript function in izenda.integrate.js.

#### Embedding the Izenda Report Designer Page

Create ~\Report\ReportDesigner.aspx:

```
<%@ Page Title="New Report" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="ReportDesigner.aspx.cs" Inherits="WebFormsStarterKit.Report.ReportDesigner" %>
								<asp:Content ID="ReportDesignerContent" ContentPlaceHolderID="MainContent" runat="server">
								<script type="text/javascript">
								$(document).ready(function () {
								izendaInitReportDesigner();
								});
								</script>
								<div class="loader" id="progressLoader"></div>
								<div class="izenda-container" id="izenda-root"></div>
								</asp:Content>
							
```

#### Report Part for Exporting

This page is not displayed directly to the end-users. It is used for rendering report parts (charts, gauges, and maps) for exporting. Reports containing these report part types must be rendered to capture html content then converted to an image when creating exports (pdf, word, excel, etc.).

This page is requested by the Izenda backend over the route url `viewer/reportpart/{id}` and mapped to `report/reportpart.aspx` in route config ~\App\_Start\RouteConfig.cs.

Create ~\Report\ReportPart.aspx:

```
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="ReportPart.aspx.cs" Inherits="WebFormsStarterKit.Report.ReportPart" %>
								<!DOCTYPE html>
								<html xmlns="http://www.w3.org/1999/xhtml">
								<head runat="server">
								<meta charset="utf-8" />
								<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
								<title>Report Viewer</title>
								<webopt:BundleReference runat="server" Path="~/Content/css" />
								<link href="~/favicon.ico" rel="shortcut icon" type="image/x-icon" />
								<%: Scripts.Render("~/bundles/modernizr") %>
    
								<%--Apply css--%>
								<link href="~/Scripts/izenda/izenda-ui.css" rel="stylesheet"/>
								</head>
								<body>
								<%: Scripts.Render("~/bundles/jquery") %>
								<%: Scripts.Render("~/bundles/bootstrap") %>
								<%: Scripts.Render("~/bundles/izenda") %>
								<script type="text/javascript">
								$(document).ready(function () {
								DoIzendaConfig();
								$('[data-toggle="tooltip"]').tooltip();
								$('[data-toggle="dropdown"]').dropdown();
								$("#reportPartLoader").hide();
								$("#reportPartLoaderText").hide();

								            izendaInitReportPartExportViewer('<%=ReportId%>', '<%=Token%>');
								            // $('#izenda-root').children().first().removeClass('izenda');
								//var classList = $('#izenda-root').children().first().attr('class').split(/\s+/);
								//$.each(classList, function (index, item) {
								//    console.log(item);
								//});
								});
								</script>
								<style>
								#izenda-root > .izenda {
								background-color: transparent !important;
								}
								</style>
								<div class="izenda-container" id="izenda-root" style="margin-top: 0px;"></div>
								</body>
								</html>
							
```

This page is only used by Izenda backend, so it requires a minimal view containing only the report part content. Therefore, it will not require a master page. The call to `izendaInitReportPartExportViewer` is the pivotal portion of this file and it requires an additional piece to work.

Open ReportPart.aspx.cs:

```
usingSystem;usingSystem.Web.UI;namespaceWebFormsStarterKit.Report{publicpartialclassReportPart:Page{privatestaticreadonlylog4net.ILogLogger=log4net.LogManager.GetLogger(typeof(ReportPart));publicstringReportId{get;set;}publicstringToken{get;set;}protectedvoidPage_Load(objectsender,EventArgse){ReportId=(Page.RouteData.Values["id"]+string.Empty);Token=Request.QueryString["token"];Logger.DebugFormat("Render report part id={0}, token={1}",ReportId,Token);}}}
```

The properties in this code-behind are used to populate the arguments for the `izendaInitReportPartExportViewer` function.

#### Embedding the Report Viewer

Create ~\Report\ReportViewer.aspx:

```
<%@ Page Title="Report Viewer" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="ReportViewer.aspx.cs" Inherits="WebFormsStarterKit.Report.ReportViewer" %>
								<asp:Content ID="ReportViewerContent" ContentPlaceHolderID="MainContent" runat="server">
								<script type="text/javascript">
								$(document).ready(function () {
								            izendaInitReportViewer('<%=ReportId%>');
								        });
								</script>
								<div class="loader" id="progressLoader"></div>
								<div class="izenda-container" id="izenda-root"></div>
								</asp:Content>
							
```

Note from the highlighted line that this page also used by Izenda backend in function to export report html content when the user wants to send a report via email (directly or via the subscription scheduler). The Izenda backend uses the route `report/view/{id}` to get report content, then in RouteConfig.cs we have a custom route for this to map it to `Report/ReportViewer.aspx`.

```
usingSystem;usingSystem.Collections.Generic;usingSystem.Web.UI;namespaceWebFormsStarterKit.Report{publicpartialclassReportViewer:Page{privatestaticreadonlylog4net.ILogLogger=log4net.LogManager.GetLogger(typeof(ReportViewer));publicstringReportId{get;set;}protectedvoidPage_Load(objectsender,EventArgse){ReportId=(Page.RouteData.Values["id"]+string.Empty);Logger.DebugFormat("Render Report ID={0}",ReportId);}}}
```

You must ensure your report viewer page handles the ID parameter passed in via the route data.

#### Embedding Report Parts

This page demonstrates how to display multiple report parts on a page outside of the Report Viewer. The function `izendaInitReportPartDemo` in ~\Scripts\izenda.integrate.js is implemented to handle this.

```
//Renderreportpartstospecific<div>tagbyreportpartidvarizendaInitReportPartDemo=function(){functionsuccessFunc(data,status){console.info(data);varcurrentUserContext={token:data};//Youcanaddreportpartsaftercreatingreportsusingthecontextbelow//AddthereportpartID's in the <reportPartIds> arrayvarreportPartIds=newArray("[your 1st report part id]","[your 2nd report part id]","[your 3rd report part id]","[your 4th report part id]");IzendaSynergy.setCurrentUserContext(currentUserContext);for(vari=0;i<reportPartIds.length;i++){//createreportpartcontainervarreportPartNode=document.createElement("div");reportPartNode.className="report-part-chart";//RenderreportpartIzendaSynergy.renderReportPart(reportPartNode,{"id":reportPartIds[i]});//Appendtoizenda-rootcontainerdocument.getElementById('izenda-root').appendChild(reportPartNode);}}this.DoRender(successFunc);};
```

Create ~\Report\ReportParts.aspx:

```
<%@ Page Title="Report Parts" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="ReportParts.aspx.cs" Inherits="WebFormsStarterKit.Report.ReportParts" %>
								<asp:Content ID="ReportPartsContent" ContentPlaceHolderID="MainContent" runat="server">
								<script type="text/javascript">
								$(document).ready(function () {
								            izendaInitReportPartDemo();
								        });
								</script>
    
								<style>
								.report-part-chart {
								float: left;
								width: 40%;
								height:  40%;
								margin-left: 20px;
								margin-top: 20px;
								background-color: white;
								}
								.report-part-grid {
								float: left;
								width: 40%;
								height:  50%;
								margin-left: 20px;
								margin-top: 20px;
								background-color: white;
								}
								</style>
								<div class="loader" id="progressLoader"></div>
								<div class="izenda-container" id="izenda-root"></div>
								</asp:Content>
							
```

### Embedding the Dashboard

#### Dashboard List

This page displays the dashboard list.

Create ~\Dashboard\Dashboards.aspx:

```
<%@ Page Title="Dashboards" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Dashboards.aspx.cs" Inherits="WebFormsStarterKit.Dashboard.Dashboards" %>
								<asp:Content ID="DashboardsContent" ContentPlaceHolderID="MainContent" runat="server">
								<script type="text/javascript">
								$(document).ready(function () {
								            izendaInitDashboard();
								        });
								</script>
								<div class="loader" id="progressLoader"></div>
								<div class="izenda-container" id="izenda-root"></div>
								</asp:Content>
							
```

#### New Dashboard

The page for creating a new dashboard.

Create ~\Dashboard\DashboardDesigner.aspx:

```
<%@ Page Title="New Dashboard" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="DashboardDesigner.aspx.cs" Inherits="WebFormsStarterKit.Dashboard.DashboardDesigner" %>
								<asp:Content ID="DashboardDesignerContent" ContentPlaceHolderID="MainContent" runat="server">
								<script type="text/javascript">
								$(document).ready(function () {
								            izendaInitNewDashboard();
								        });
								</script>
								<div class="loader" id="progressLoader"></div>
								<div class="izenda-container" id="izenda-root"></div>
								</asp:Content>
							
```

#### Dashboard Viewer

This page displays details of a dashboard. It is also requested by the Izenda backend for dashboard exporting functions over the route `dashboard/view/{id}`. In RouteConfig.cs we have a custom route named `DashboardViewer`. This custom route will map to the `dashboard/DashboardViewer.aspx` page.

Create ~Dashboard\DashboardViewer.aspx:

```
<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="DashboardViewer.aspx.cs" Inherits="WebFormsStarterKit.Dashboard.DashboardViewer" %>
								<asp:Content ID="DashboardViewerContent" ContentPlaceHolderID="MainContent" runat="server">
								<script type="text/javascript">
								$(document).ready(function () {
								            izendaInitDashboardViewer('<%=DashboardId%>');
								        });
								</script>
								<div class="loader" id="progressLoader"></div>
								<div class="izenda-container" id="izenda-root"></div>
								</asp:Content>
							
```

```
usingSystem;usingSystem.Web.UI;namespaceWebFormsStarterKit.Dashboard{publicpartialclassDashboardViewer:Page{privatestaticreadonlylog4net.ILogLogger=log4net.LogManager.GetLogger(typeof(DashboardViewer));publicstringDashboardId{get;set;}protectedvoidPage_Load(objectsender,EventArgse){DashboardId=(Page.RouteData.Values["id"]+string.Empty);Logger.DebugFormat("Render Dashboard ID={0}",DashboardId);}}}
```

The RouteData is used to handle incoming requests to pass the Dashboard Id into the JavaScript function.

## Run Your Izenda Integrated Application

Press F5 to run debug

Navigate to login page and enter the values below for the respective fields:

* Tenant = System
* Email = [IzendaAdmin@system.com](mailto:IzendaAdmin%40system.com)
* Password = [Izenda@123](mailto:Izenda%40123)

On top menu click Settings link then add your license key

[![../_images/webforms_license_key.png](https://devnet.logianalytics.com/hc/article_attachments/4415492427287/webforms_license_key_900x486.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492426903/webforms_license_key.png)

Stop your application and start it again (this step ensures Izenda reloads the cache).

Click Izenda link on the top menu to open the full Izenda app

[![../_images/webforms_full_izenda_app.png](https://devnet.logianalytics.com/hc/article_attachments/4415492427799/webforms_full_izenda_app_900x341.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492427543/webforms_full_izenda_app.png)

Now feel free to explore the entire Izenda integrated application.

## Implement Register New Account

Modify Register.aspx

[![../_images/webforms_new_account.png](https://devnet.logianalytics.com/hc/article_attachments/4415511700631/webforms_new_account_900x491.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504325527/webforms_new_account.png)

Add a new Tenant TextBox field into ~\AcountRegister.aspx

```
<hr/><asp:ValidationSummaryrunat="server"CssClass="text-danger"/><divclass="form-group"><asp:Labelrunat="server"AssociatedControlID="Tenant"CssClass="col-md-2 control-label">Tenant</asp:Label><divclass="col-md-10"><asp:TextBoxrunat="server"ID="Tenant"CssClass="form-control"/><asp:RequiredFieldValidatorrunat="server"ControlToValidate="Tenant"CssClass="text-danger"ErrorMessage="The tenant field is required."/></div></div><divclass="form-group"><asp:Labelrunat="server"AssociatedControlID="Email"CssClass="col-md-2 control-label">Email</asp:Label>
```

Also, in accordance with the change to Login.aspx to properly nest it inside the form tag, change the ContentPlaceHolderID to the aforementioned placeholder:

```
<%@PageTitle="Register"Language="C#"MasterPageFile="~/Site.Master"AutoEventWireup="true"CodeBehind="Register.aspx.cs"Inherits="WebFormsStarterKit.Account.Register"%><asp:Contentrunat="server"ID="BodyContent"ContentPlaceHolderID="LoginContent"><h2><%:Title%>.</h2>
```

Create a new folder called “Managers” and Add a new class called “TenantManager” to your project (~\Managers\TenantManager.cs). This class is used to get Tenant information from your application’s database and create new tenant info for your authentication DB.

```
usingSystem;usingSystem.Linq;usingSystem.Threading.Tasks;usingWebFormsStarterKit.Models;namespaceWebFormsStarterKit.Managers{publicclassTenantManager{publicTenantGetTenantByName(stringname){using(varcontext=ApplicationDbContext.Create()){vartenant=context.Tenants.SingleOrDefault(x=>x.Name.Equals(name,StringComparison.InvariantCultureIgnoreCase));returntenant;}}publicTenantSaveTenant(Tenanttenant){using(varcontext=ApplicationDbContext.Create()){context.Tenants.Add(tenant);context.SaveChanges();returntenant;}}}}
```

Open ~\AccountRegister.aspx.cs and modify the CreateUser\_Click method to handle the new registration logic.

When registering a new user, the new user’s information is stored on both the authentication DB and the Izenda DB. To achieve this, we split the registration logic into the steps below:

* Save new Tenant if needed
* Save User and Role in authentication DB
* Save User and Role in Izenda DB
* Sign in with new user

All steps are encapsulated in the CreateUser\_Click method of the Register.aspx.cs file.

Register tenant:

```
vartenant=newTenant(){Name=Tenant.Text};vartenantManager=newManagers.TenantManager();varexstingTenant=tenantManager.GetTenantByName(tenant.Name);if(exstingTenant!=null)tenant=exstingTenant;elsetenant=tenantManager.SaveTenant(tenant);
```

Save user and role information into authentication DB:

```
varuser=newApplicationUser(){UserName=Email.Text,Email=Email.Text,Tenant_Id=tenant.Id};IdentityResultresult=manager.Create(user,Password.Text);//ThislinebelowwillhardcodeuserswhoregistertoaroleofManagerandcanbechangedbyalteringtherolebelowmanager.AddToRole(user.Id,"Manager");
```

Save user and role into IzendaDB:

```
if(result.Succeeded){//izenda//determinetenantvarizendaTenant=newTenants();izendaTenant.Active=true;izendaTenant.Deleted=false;//varcurrentUserTenant=ParseTenantFromEmail(izendaTenant.Name);izendaTenant.Name=tenant.Name;izendaTenant.TenantID=tenant.Name;//determinerolesvarroleDetail=newRoleDetail(){Name="Administrator",TenantUniqueName=tenant.Name,Active=true,Permission=newPermission(),};varizendaUser=newUserDetail(){UserName=user.Email,EmailAddress=user.Email,FirstName="John",//todofixthisLastName="Doe",TenantDisplayId=tenant.Name,Deleted=false,Active=true,SystemAdmin=false,Roles=newList<Role>()};izendaUser.Roles.Add(newRole(){Name=roleDetail.Name});TenantIntegrationConfig.AddOrUpdateTenant(izendaTenant);RoleIntegrationConfig.AddOrUpdateRole(roleDetail);UserIntegrationConfig.AddOrUpdateUser(izendaUser);
```

Login with newly created user:

```
signInManager.SignIn(user,isPersistent:false,rememberBrowser:false);IdentityHelper.RedirectToReturnUrl(Request.QueryString["ReturnUrl"],Response);
```

You can refer to completed implementation of the Register logic on Github [here](https://github.com/Izenda7Series/WebFormsStarterkit/blob/master/WebFormsStarterKit/Account/Register.aspx.cs).

## Call the Izenda API Service in C#

In the completed sample starter kit on Github, we provide an example demonstrating how to call Izenda’s API service in C# code. Reference the ~\IzendaBoundary\WebAPIService.cs and ~\IzendaBoundary\IzendaUtility.cs files for more detail.
