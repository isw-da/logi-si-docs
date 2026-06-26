---
title: "Post-Deployment Server Configuration"
id: 4419722865431
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722865431-Post-Deployment-Server-Configuration
updated_at: 2022-07-17T02:08:08Z
---

# Post-Deployment Server Configuration

# Post-Deployment Server Configuration

Once you have physically deployed your Info application to the production server for the first time, you need to configure it to run in the new environment.

### When Using Windows IIS Web Server

1. Provide a Logi Info license file for the application, unless you're using a centralized v12 license file.
2. *Register* the application with IIS. You can do this using Studio (if you've installed it on the production server), Server Manager, or the IIS Manager tool.

3. Ensure that the datasource connection strings or parameters, constants, and other server-specific attributes are correct in your application's \_Settings definition. This can be done using **Notepad** if Studio is not installed.
4. If your application writes any output to the file system outside of your Logi application folder, ensure that the account the web server uses to run your application (ASP.NET, NETWORK SERVICE, or Application Pool, depending on IIS version) is granted *Write* permission to the relevant folders.

### When Using a Java Server

1. Provide a Logi Info license file for the application, unless you're using a centralized v12 license file.
2. Provide any additional configurations required for your server. See [Java Server Configurations](https://devnet.logianalytics.com/hc/en-us/articles/7522872807447-Java-Server-Configurations) for specific information.

3. Ensure that the datasource connection strings or parameters, constants, and other server-specific attributes are correct in your application's \_Settings definition. This can be done using any text editor.
4. If your application writes any output to the file system, ensure that the identity the application runs under has appropriate file access permissions for the relevant directories.

Subsequent deployments for the purpose of updating report definitions, images, XML data, etc. should not require you to do any of the steps discussed above, unless you're changing folder locations or \_Settings attributes. This means Logi Server Engine files and \_Settings.lgx can be left out of future deployments undertaken for simple update purposes.
