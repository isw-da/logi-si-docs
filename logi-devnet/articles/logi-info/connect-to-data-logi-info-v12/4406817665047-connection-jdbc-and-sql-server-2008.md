---
title: "Connection.JDBC and SQL Server 2008"
id: 4406817665047
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817665047-Connection-JDBC-and-SQL-Server-2008
updated_at: 2022-04-06T06:07:29Z
---

# Connection.JDBC and SQL Server 2008

# Connection.JDBC and SQL Server 2008

Developers creating Logi applications for Java, and using Connection.JDBC to connect to Microsoft SQL Server 2008, may encounter the following errors:
There was a problem running a DataLayer. The error was: Could not open the supplied connection to the data. The server version is not supported. The target server must be SQL Server 2000 or later.
This occurs when a newer JDBC driver is required for SQL Server 2008. The solution is:

1. [Download a new driver](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=99b21b65-e98f-4a61-b811-19912601fdc9&displaylang=en) from Microsoft and uncompress the download.
2. From the download, copy the file sqljdbc4.jar to your Logi application's WEB-INF/lib folder.
3. Delete the old driver, sqljdbc.jar, from the same folder.
4. Restart the web server.
5. Run the Logi application.

If the following error message is received:
Java Runtime Environment (JRE) version 1.6 is not supported by this driver. Use the sqljdbc4.jar class library, which provides support for JDBC 4.0.
it means you either did not remove the original sqljdbc.jar, replaced it with the sqljdbc.jar file that came with the download instead of adding sqljdbc4.jar to the folder, or did not restart the web server.
