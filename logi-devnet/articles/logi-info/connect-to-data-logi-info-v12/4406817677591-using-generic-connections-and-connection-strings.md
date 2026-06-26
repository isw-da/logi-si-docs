---
title: "Using Generic Connections and Connection Strings"
id: 4406817677591
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817677591-Using-Generic-Connections-and-Connection-Strings
updated_at: 2022-04-06T06:07:34Z
---

# Using Generic Connections and Connection Strings

# Using Generic Connections and Connection Strings

Another method of creating a connection is to use one of the *generic* Connection elements, which requires that you provide a connection string.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563164055/introconn5_06.png)

In the example shown above, a **Connection.OLEDB** element has been added to the \_Settings definition. Its **Connection String** attribute has been configured with a connection string, which looks like this in its entirety:

Provider=SQLOLEDB.1;Password=password;Persist Security Info=True;User ID=user;Initial Catalog=Northwind;Data Source=myDBServer

You can see that the connection string has a specific format, which is unique to the connection type. The Connection.OLEDB element can invoke a special wizard to build its connection string; for all other connections, developers will need to provide an appropriate string.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583814807/introconn5_07.png)  

The **Data Link Properties** wizard, shown above, assists in the creation of connection strings for the Connection.OLEDB element. In Studio, click the little browse button at the end of the element's Connection String attribute value to invoke the wizard.
The **Test Connection** button only ensures network connectivity to the database server - it *does not* guarantee that the User Name and Password entered are valid! The test can be successful and yet you may still not be able to access the data if the credentials are wrong. If providing specific credentials, be sure that you enter them carefully and check *Allow saving password*.

This very useful web site: <http://www.ConnectionStrings.com> provides example connection strings for a wide variety of datasources and can assist in providing the proper format for strings for other connection types.

## With ActiveSQL

If **Connection.JDBC** or **Connection.ODBC** is used with DataLayer.ActiveSQL, you must configure the Connection element's optional **SQL Syntax** attribute to identify the database's SQL syntax version.

## Notes For Java Developers

When using a **Connection.JDBC** element, specifying an IP address instead of a host name in the connection string may significantly *increase* the connection opening time, due to the underlying Java implementation. Therefore, it is recommended that developers use host names, *not* IP addresses, in connection strings to minimize the time it takes to open a connection.

The **Connection.SMTP** element supports TLS/SSL authentication in Java applications only. This allows connection to Gmail and other similar services that will programmatically send email on your behalf. Set the element's **SMTP Authentication Mode** attribute to *3* to select TLS/SSL. In v12.2-SP4+, the TLS 1.1 and 1.2 protocols are supported.
