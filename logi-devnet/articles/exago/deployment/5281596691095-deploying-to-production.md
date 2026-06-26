---
title: "Deploying to Production"
id: 5281596691095
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281596691095-Deploying-to-Production
updated_at: 2022-05-03T22:08:18Z
---

# Deploying to Production

# Deploying to Production

This guide describes the considerations you should take when deploying an Exago BI installation to a production environment. Suggested steps are listed in the order they should be taken. Best practices are recommended for each step. However, every environment is different, so recommendations should be considered in the context of the desired setup.

### Contents

If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

1. **Installation**: Decide where the Exago BI application and schedulers live
2. **Data**: Determine how to expose data to users
3. **API**: Use the API to control user permissions
4. **Content Management**: Implement a content management solution
5. **Integration**: Visually integrate Exago BI into the host app
6. **Reports**: Make “canned” reports as examples for end users
7. **User Preferences**: Implement a user preference storage solution
8. **Deployment**: Important steps to follow before deploying the host app
9. **Security**: Follow our **[Security Checklist](https://devnet.logianalytics.com/hc/en-us/articles/5281588834455-Security-Checklist)** of best practices

## Installation

Since Exago BI is an embedded application, determine which server it is installed on. Exago BI supports nearly any type of deployment, including cloud, private servers or on site at your clients.

Exago BI does not need to be installed on the same server as the host application. One or more scheduling services can be further installed separate servers to handle **Remote Execution** of reports. Additional scaling can be accomplished with a Web Farm. To use the .NET API, Exago BI must be accessible from the host application via a file system path. See **[API](#API)** for more information.

The scheduling services are capable of acting as standalone report execution applications. The best way to scale Exago BI for performance is to deploy additional scheduling servers, and offload report executions to them. This method, called **Remote Execution**, also implements an automatic load balancing solution. The servers with the most available resources are given execution priority in order to keep an even load distribution.

A QA/Staging environment is highly recommended as well. This allows developers to test API changes, config changes, and Exago BI version updates, before moving to production.

Also consider the following:

* Where do you want temp files and report definitions to reside for each server?
* Where does the data source reside, relative to where Exago BI will be deployed?
* Should Exago BI reside in the same domain as the host application?

## Data

It is critical to make the right choices in how to present the data to users. Consider the technical level and reporting experience of your users. You may need to service different classes of users, from technical users like developers and database administrators, to non-technical business analysts and project managers.

Exago BI can manage **data object permissions** to many levels of precision. Permissions can be set per-user and per-group, for data objects, fields, rows, and even within field values. Data objects are easily restricted for classes of users using **Roles**. Within a data object, fields can be hidden, and row access can be limited by matching a linked user ID with the logged-in user. Roles can also provide filters for data values, in case some fields should be partially, but not fully hidden from view.

It is also recommended to use **aliasing, descriptions, folders, and metadata** to control how data objects appear in the application. Aliasing allows you to show more user-friendly names for data objects, instead of how they are named in the database. Descriptions provide additional information, and metadata can improve report performance.

Also consider the following:

* How normalized or de-normalized should the visible data be?
* Should any data objects be available for some users and not for others?
* Within a data object are there row-level permissions or multi-tenant permissions per user?
* Will the underlying data objects change in the future? If so, add IDs to objects to prevent naming conflicts.

## API

It is critical that Exago BI is only exposed to users through the API. The API allows you to set security and permissions settings, and tailor the reporting experience by user.

.NET environments can use the **.NET API**, which is the most flexible and extensible API. Non-.NET environments can access a subset of API calls through the **REST** Web Service API.

The most basic API implementation begins by initializing a session, then sets the **“userId” and “companyId”** parameters to identify the logged-in user, sets a user-specific **Role** to control permissions, and then launches Exago BI using the **getUrlParamString()** method. Developers should write the API code robustly with checks for null return values and exception handling.

Consider where you want Exago BI to appear within the host application, and how users should use it to access reporting. For example, should it be placed in an iframe container, a redirected page, or a popup window?

Also consider the following:

* Do you want to provide a list of reports and Dashboards to users and directly run them via the API?
* Are there other settings in Exago BI you want to enable or disable based on the user?

## Content Management

In *v2020.1+* all reports, folders, themes and templates are stored in a database in the **Storage Management** system. See [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction).

There are many strategies to Storage Management during the evaluation, development and QA stages. As such, there are a few paths to promoting reports from those environments to production. This section will cover the most common use cases clients have encountered.

### Cherry-Picking Reports

If only a small number of reports will transition from development to production, use the built-in Download and Upload functions form the Report Tree in either environment. See [Navigating the Application](https://devnet.logianalytics.com/hc/en-us/articles/5281546800023-Navigating-the-Application)

### A Single Database for All Environments

If all environments are sharing the same Storage Management database, this is the simplest migration path. In production, simply set the **Admin Console** > **Storage Management** database settings to the same as those from the development environment.

### Unique Databases for Each Environment

If development and production have separate Storage Management databases, see [Moving Files Between Storage Management Databases](https://devnet.logianalytics.com/hc/en-us/articles/5281638646807-Moving-Files-Between-Storage-Management-Databases) to easily export one database and import into another.

Then, using one of the APIs it is possible to set the Storage Management connection string programmatically on a per-session basis.

---

In versions *pre-2020.1*, Exago BI can handle the storage and retrieval of reports on a local or **cloud-based** file system. However, it is strongly recommend to use the Folder Management extensibility feature to customize where report definitions reside. Using folder management can allow you to store reports in a database instead of on a file server. This can make it easier to control user access permissions, helps to scale deployment, and provides additional benefits such as soft deletes and report usage tracking.

Custom folder management definitions are accessed from a custom assembly, so this does require some additional development.

Also consider the following:

* How do you want the folder tree to appear for new users?
* Will you create common reports that are available for all users?
* Are there multiple levels of report permissions beyond individual users and published reports?

## Integration

Exago BI gives you full control over the **CSS, icons**, and **language strings** in the UI. You can have several different **application themes** if necessary, and select different ones for different classes of users. You can also build custom themes for reports and visualizations. And you can make a **custom start page** that users will see when they first enter the UI.

For integration, we recommend the following best practices:

### Home page

Copy the `ExagoHome.aspx` home page to a new page, and use that as the entry point for users going into the full UI. This copy can be styled at will.

### Application Theme

Make a new application theme by extracting a copy of our **theme template** into a new folder in the `ApplicationThemes` directory. Enable the theme in the Admin Console, and add any **custom styling** if desired.

### Getting Started

Remove the content from the default **Getting Started** page, since this is only intended to be a styling example. It is recommended to add custom content, since users with access to the full UI will see this page often. Clients have used the Getting Started page to provide announcements, quick tips, helpful formulas, and links to other parts of the application.

Also consider the following:

* Does the host application support multiple languages?
* Are there any text strings or tooltips you want to customize?
* Do you want to customize the CSS or swap out any of the icons in Exago BI?
* Do you want to customize the context-sensitive help to match documentation?

## Reports

By providing a folder of “canned” reports, you can show users Exago BI’s capabilities, and some useful examples of the data that is available to them. This folder should be at the top level so it is easy to locate, and read-only so that users cannot edit the reports. If they want to make changes or see how the reports are made, they can duplicate a report and edit the copy.

Making these reports can be a good opportunity for support, sales, and services staff to become familiar with Exago BI. The Exago BI services team can also assist staff, either by basing training on these reports, or by building them.

Also consider the following:

* What questions can be answered by reporting?
* What data objects do you want to highlight?
* Are there any specific Exago BI features that you want to showcase?

## User Preferences

The [User Preferences](https://devnet.logianalytics.com/hc/en-us/articles/5281553297559-User-Preferences-and-Context-Sensitive-Help#User2) store user-level customizations of the application environment in the user’s browser local storage by default, but it is recommended to store these in a database via extensibility. An example implementation for *v2020.1+* can be found on the [Downloads page](https://support.exagoinc.com/hc/en-us/categories/202053837).

For more information:

* [User Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281636299927-User-Settings)
* [Customizing Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/5281531648279-Customizing-Color-Picker) (video)
* [v2018.2 User Preferences](https://devnet.logianalytics.com/hc/en-us/articles/5281540608663-v2018-2-User-Preferences) (video)

## Deployment

Once the other steps are in place, lay out a plan for moving to production. We recommend keeping detailed notes of the process so it can be replicated for future updates.

After installing in production, move the following files from the staging environment to production:

1. The encrypted configuration file: `/Config/config.xml.enc`
2. Any custom application themes folders: `/ApplicationThemes/themeFolder`
3. Any custom language files: `/Config/Languages/language.xml`. These also need to be added to the `/Languages` directories for each scheduler installation.
4. Custom Getting Started page: `/Config/Languages/getting-started.xml`
5. Any other configuration files: `/Config/Other/file.json`, and `/appSettings.config`
6. Custom context-sensitive help, if you have one: `/NetHelp`
7. Custom home page: `/home.aspx`
8. If you are not using folder management, any custom theme files: `/Themes/theme`
9. If you are using Google Maps, make sure the `MapPolygonDataBase.sqlite` file is present in the `/MapCache` folder.

We also recommend adding the non-encrypted config file (`/Config/config.xml`) to version control after removing any sensitive passwords or connection strings.

**Disable the Admin Console**. It should not be accessible in a production environment.

Also consider the following:

* Make sure all Exago BI instances and Scheduler Services are on the same version and build number.
* If you are using the .NET API make sure the version of `WebReportsApi.dll` matches the version and build number of Exago BI. Do the same with any custom assemblies, such as Folder Management, Storage Management, Scheduler Queue, or Server and Action Events.

## Security

**IMPORTANT:**Follow the **[Security Checklist](https://devnet.logianalytics.com/hc/en-us/articles/5281588834455-Security-Checklist)** before turning on access to the host application. It is highly recommended to follow these steps to reduce the possibility of unauthorized access.
