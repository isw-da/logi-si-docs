---
title: "Storage Management Permissioning and Setup"
id: 5281571962903
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281571962903-Storage-Management-Permissioning-and-Setup
updated_at: 2022-05-03T22:08:29Z
---

# Storage Management Permissioning and Setup

# Storage Management Permissioning and Setup

This video explains how to set up Storage Management in a fresh Exago install.

[<< Configuring a Stored Procedure Pt 2](https://devnet.logianalytics.com/hc/en-us/articles/5281563495831-Configuring-a-Stored-Procedure-Part-2) Previous Video

Next Video [Roles >>](https://devnet.logianalytics.com/hc/en-us/articles/5281555242775-Roles)

## Transcript

Welcome back to the Exago Technical Training Series! In this video, we will demonstrate how to setup Storage Management in a new installation of Exago BI.

Storage Management refers to the mechanism that Exago uses to store reports, document templates, themes and folders in a database. Configuring the Storage Management system is one of the very first required configuration steps to get Exago up and running.

The first step is to open the Exago Admin Console. The Admin Console is used to build the base configuration that is modified by the API for each subsequent user session. To open the Admin Console, we’ll use the server IP slash web app virtual path slash Admin.aspx to build our URL. In our case, that looks like this.

Then, on the left, double-click on Storage Management. Now we need to configure and create the database. Storage Management supports Microsoft SQL Server, MySQL, Oracle and PostgreSQL databases, and can also support a SQLite database for testing and demonstration purposes. Today, we will use a SQLite database since we’re setting this environment up for testing. Moving to one of the robust database types later on is simple with an Exago provided command line utility. By default, SQLite will be selected in the Database Type dropdown. It is also the default Database Provider and Database Connection string, so we don’t have to change anything for those values either. We can optionally provide a prefix or schema for the database tables. Next, we want to create the tables and schema in the database. Use this Prepare Database button to connect to the database and have Exago build the schema and load the initial data into it. For SQLite databases like ours, Exago will also create the file. The other database types require that the database exists on the server first. This button can also be used to update the schema if necessary on an existing database. It is non-destructive. Alternatively, use Show Prepare Database SQL to display the SQL that can be manually executed to do the same thing. Next, click the Load Themes button to load the chart, map and report themes into the database.

The Identity Keys identify the current user to the Storage Management database. While in a testing or development environment where Exago may be accessed directly like ours, the values specified here are used for whatever content is created. All users will have the same access to all of the content in this scenario. In practice, an application implementing Exago will change these key values when creating a session via one of our APIs.

The following default settings determine how Exago will handle setting permission information on newly created content in the root or the top level of the Report Tree. Inheritance determines whether new content created in an existing folder will copy all of the access records from its parent. Default access flags are used for newly created content when not inheriting access from the parent objects. This value can be full access, read only, or a custom combination of the available access flags. It is generally recommended to leave the cache values as default.

Congratulations! You’ve successfully setup Storage Management in a new install of Exago BI!
