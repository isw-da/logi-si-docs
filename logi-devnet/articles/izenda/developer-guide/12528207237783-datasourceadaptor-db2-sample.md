---
title: "DataSourceAdaptor - DB2 Sample"
id: 12528207237783
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528207237783-DataSourceAdaptor-DB2-Sample
updated_at: 2023-02-23T15:17:20Z
---

# DataSourceAdaptor - DB2 Sample

# DataSourceAdaptor - DB2 Sample

Izenda has built-in support for most common source database systems including MS SQL Server, Azure, Oracle, MySQL and PosgreSQL. This article describes the database systems you can use in the Izenda BI.

Other database systems can be easily supported via the `IDataSourceAdaptor` interface.

In this sample, we will add a DataSourceAdaptor for [IBM DB2 database](http://www.ibm.com/analytics/us/en/technology/db2/).

## Preparation

1. DB2 Express-C database server setup

   1. Download and install the server from [IBM](http://www.ibm.com/analytics/us/en/technology/db2/db2-trials.html).

      Note down the password of db2admin user to connect to the server later.
   2. Open the DB2 Command Window from Start menu to check the server.

      ```
      $ db2
      										db2 => connect to sample   Database Connection Information Database server        = DB2/NT64 11.1.0 SQL authorization ID   = ... Local database alias   = SAMPLEdb2 => terminateDB20000I  The TERMINATE command completed successfully.
      ```
2. DB2 client library

   1. Get DB2 .Net driver from the section “IBM DB2 10.5 client and driver packages” in [the same page](http://www.ibm.com/analytics/us/en/technology/db2/db2-trials.html).
   2. Download and install the IBM Data Server Driver Package (DS Driver).
   3. Check that the file IBM.Data.DB2.dll has been installed (e.g. at C:\Program Files\IBM\IBM DATA SERVER DRIVER\bin\netf40\_32).

   Note: Xunit unit test only works with 32-bit projects so we will be using the 32-bit driver (netf40\_**32**).

## IDataSourceAdaptor Implementation

### Reference IDataSourceAdaptor Interface in a New Project

1. Create a new Class Library project in Visual Studio.
2. Name it Izenda.BI.DataAdaptor.RDBMS.DB2.
3. Select a location (e.g. D:\Projects).
4. Select to create new solution.
5. Give the solution name Izenda.BI.DB2DataAdaptor.
6. Tick the Create directory for solution check-box.
7. Click OK to create the project and solution.

   ![../_images/New_DataAdaptor_DB2_Project.png](https://devnet.logianalytics.com/hc/article_attachments/12528147084183/new_dataadaptor_db2_project.png)
8. Copy the interface library file Izenda.BI.DataSourceAdapter.dll from Izenda installation folder into the newly-created folder D:\Projects\Izenda.BI.DataAdaptor.RDBMS.DB2.
9. Open Solution Explorer, right-click References in project Izenda.BI.DataSourceAdaptor.RDBMS.DB2 and select Add Reference.
10. In Reference Manager pop-up, click Browse and select the file Izenda.BI.DataSourceAdapter.dll (in D:\Projects\Izenda.BI.DataAdaptor.RDBMS.DB2).
11. Click OK to close Reference Manager pop-up.
12. Verify the interface by double-clicking Izenda.BI.DataSourceAdapter in References to open Object Browser.
13. Expand the nodes and select IDataSourceAdaptor to see this list of methods to implement.

    ![../_images/BI_IDataSourceAdaptor_Interface.png](https://devnet.logianalytics.com/hc/article_attachments/12528163151383/bi_idatasourceadaptor_interface.png)

### Reference IMB.Data.DB2 Library

1. Similarly, add reference to the file IBM.Data.DB2.dll at C:\Program Files\IBM\IBM DATA SERVER DRIVER\bin\netf40\_32.

   > This driver depends on other libraries in the installation so it should not be copied to another place.

### Implement the IDataSourceAdaptor Interface

1. Right-click the default Class1.cs file in Solution Explorer and rename it to DB2DataSourceAdaptor.cs, also agree to change the class name to DB2DataSourceAdaptor when asked.
2. Add reference to the DLLs being used similarly to the above steps:

   * Izenda.BI.DataAdaptor.RDBMS.dll
   * Izenda.BI.Framework.dll
   * Izenda.BI.Logging.dll
   * Izenda.BI.QueryNormalizer.SQL.dll
   * Izenda.BI.RDBMS.dll
3. Implement the methods of the interface using DB2 APIs.

   ```
   publicConnectionStatusTestConnection(GuidserverType,stringconnectionString){varresult=newConnectionStatus();try{DB2Connectionconnect=newDB2Connection(connectionString);connect.Open();result.Status=ConnectDBStatus.Success;}catch(Exceptionex){result.Status=ConnectDBStatus.Fail;result.ErrorMessage=ex.Message;}returnresult;}
   ```

Note: The full implementation for DB2 will be updated later.

### Add UnitTest Project

1. Rick click Solution ‘Izenda.BI.DataAdaptor.RDBMS.DB2’ in Solution Explorer and select Add > New Project.
2. Add a Class Library project named Izenda.BI.DataAdaptor.RDBMS.DB2.Test.
3. Reference the project Izenda.BI.DataAdaptor.RDBMS.DB2 (Add Reference and tick Izenda.BI.DataAdaptor.RDBMS.DB2 in Projects > Solution).
4. Reference xUnit Library.
   1. Open NuGet Package Manager pop-up from Tools > NuGet Package Manager > Manage NuGet Packages for Solution…
   2. Click Browse tab and enter xunit in the text box to search.
   3. Select xunit on the left and tick the Izenda.BI.DataAdaptor.RDBMS.DB2.Test project check-box on the right.
   4. Select version 1.9.1 (working at the time of writing) and click Install.
   5. Similarly install xunit.runner.visualstudio version 2.1.0 to Izenda.BI.DataAdaptor.RDBMS.DB2.Test project.

### Implement the Tests

1. Right-click the default Class1.cs file in Solution Explorer and rename it to DB2DataSourceAdaptorTest.cs, also agree to change the class name to DB2DataSourceAdaptorTest when asked.
2. Add reference to the DLLs being used similarly to the above steps.
3. Implement the tests in xUnit.

```
usingIzenda.BI.DataAdaptor.DB2;usingIzenda.BI.Framework.Constants;usingSystem;usingXunit;namespaceIzenda.BI.DataAdaptor.RDBMS.DB2.Test{publicclassDB2DataSourceAdaptorTest{publicconststringconn="Database=SAMPLE;UserID=db2admin;Password=DB2_admin;Server=localhost:50000";      [Fact]publicvoidTestConnection(){varadaptor=newDB2DataSourceAdaptor();varresult=adaptor.TestConnection(newGuid("d968e96f-91dc-414d-9fd8-aef2926c9a18"),conn);Assert.Equal(result.Status,ConnectDBStatus.Success);}}}
```

Note: Edit the connection conn to the correct password and IP address of the DB2 server. Also, the connection should be read from the configuration file in an actual code.

### Run the UnitTests

1. Open Test Explorer from Menu > Test > Windows.
2. Click Run All in Test Explorer.

   ![../_images/DB2DataSourceAdaptorTest_TestExplorer.png](https://devnet.logianalytics.com/hc/article_attachments/12528147098263/db2datasourceadaptortest_testexplorer.png)
