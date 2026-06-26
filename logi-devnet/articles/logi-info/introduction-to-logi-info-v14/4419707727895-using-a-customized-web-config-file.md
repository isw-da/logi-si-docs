---
title: "Using a Customized Web.config File"
id: 4419707727895
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707727895-Using-a-Customized-Web-config-File
updated_at: 2022-07-17T01:42:32Z
---

# Using a Customized Web.config File

# Using a Customized Web.config File

Each Logi application includes a file named Web.config, which is standard in ASP.NET applications. *This text file is accessible for customization in both .NET and Java Logi applications.*

You can add the following section to it for connection strings:

<connectionStrings>  
<addname="myConnString"connectionString="Server=xxx; Port=nnnn; Database=xxx; uid=xxx; pwd=xxx;"/></connectionStrings>  
Under the .NET framework there are classes and methods specifically for reading from this file. In Java, a stream reader of some kind must be used. In both cases, this can be done from within one of the plug-ins described above in order to extract the connection string data and modify the \_Settings definition at runtime.
The .NET framework also provides a mechanism for encrypting connection strings so that they're not held in plain text in this file. Learn more about [securing connection strings](https://docs.microsoft.com/en-us/aspnet/web-forms/overview/data-access/advanced-data-access-scenarios/protecting-connection-strings-and-other-configuration-information-cs) in this Microsoft document.
