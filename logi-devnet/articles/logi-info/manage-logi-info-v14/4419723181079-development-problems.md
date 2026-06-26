---
title: "Development Problems"
id: 4419723181079
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723181079-Development-Problems
updated_at: 2022-07-17T01:36:49Z
---

# Development Problems

# Development Problems

This topic introduces the different types of development problems you could run into when developing Logi Studio, as well as possible solutions.

Problems exporting to PDF, Excel, and Microsoft Word:

* **PDF** - Developers must give users the ability to export a report
  manually or instruct the server to automatically export a report. Manual
  exports are configured within Report definitions and automated exports
  are configured within Process definitions. If any elements in a
  definition have duplicate element IDs or their IDs are not set, they
  must be uniquely identified for the export to work.

* **Excel** - If error messages are received during the export
  process, remove any changes that have been applied recently to the
  report. If the error messages persist, the page may have been cached.
  You may need to terminate the current session and/or restart your web
  server to clear it.

* **Microsoft Word** - Ensure that the Target.Export element's Report
  Definition File attribute does not have a value of "Current
  Report." This value causes the Request parameters *not* to be
  passed to the export.

Problems Running Queries on the Web Server:

* **Application is not found**  
   Using the management tool supplied with your web server, confirm that
  the application is registered with it, and that its virtual directory
  exists. If using .NET, ensure that the Application name exists and that
  the ASP.NET setting is correct in the virtual directory properties.

* **Cannot connect to the database**  
   Native Connection elements (Connection.MySQL, Connection.Oracle, etc.)
  provide optimized connections to their databases. However, if you're
  using a connection with a Connection String that you entered manually,
  be sure it's valid, without misspellings or missing information. Ensure
  that the password is being saved with the string. Information about
  [connection strings](http://www.connectionstrings.com/) for a
  variety of databases can be found online. If you must use Windows
  integrated authentication with the database, the ASP.NET account must be
  given access to the database or .NET impersonation must be used on the
  developed reports.
* **Query Builder or Database Browser connects to data OK but my report
  does not**  
   This strange-seeming circumstance comes about because the Query Builder
  and Database Browser tools connect directly from your development PC to
  the datasource, whereas, when you preview or browser your application,
  your report is connecting through the web server and Logi Server Engine.
  When the Query Builder or the Database Browser connects but the report
  does not, the problem is often that the account used by the web server
  to run your Logi report (by default in .NET: the Application Pool
  account, ASPNET, or NETWORK service) does not have permission to access
  the datasource.

Problems Running the Wizards:

* **Wizards won't run**  
   For the wizards to run properly, security should *not* be enabled
  in the \_Settings definition for your reports. Before running the
  wizards, resolve any errors received while browsing or previewing the
  reports in a web browser. Web server-to-datasource connection
  configuration errors may prevent the wizards from running properly.
  Elements affected by wizards, such as "Add Data Table
  Columns", will not work correctly if the element is missing its
  required, unique element ID.

Problem Saving Logi Application:

* **Insufficient Disk Space**  
   The user must have enough disk space to save files on the system. Files
  must not be set to "Read Only" in order for them to be
  overwritten; check their properties in the file system.

Problems Running the Debugger:

* **Debug link or icon doesn't work**  
   Changes to the \_Settings definition, like turning on debugging, may
  require a new browser session. Confirm that a new browser window is
  being launched to test this. The \_Settings definition Debugger Style
  attribute value must be "DebuggerLinks"; the value is
  case-sensitive and should be one word.

Problems With Logon From Non-Standard Logon Form:

* The standard Logi logon page, rdLogon.aspx, passes the login name and
  password form variables and also a hidden form variable called
  "rdFormLogon" set equal to *True*. The latter variable
  should also be passed to the report if the username and password are
  being submitted from any other report definition or form.
