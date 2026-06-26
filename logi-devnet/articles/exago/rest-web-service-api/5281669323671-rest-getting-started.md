---
title: "REST \u2014 Getting Started"
id: 5281669323671
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281669323671-REST-Getting-Started
updated_at: 2022-05-03T22:08:48Z
---

# REST — Getting Started

# REST — Getting Started

This guide serves as a step-by-step walk through for installing and configuring the REST Web Service, verifying that it is working properly, and briefly demonstrating how it works.

This topic is a chronological series of steps that should be followed in this order:

1. [Install the Web Service API](#Install)
   * [Windows](#Windows)
   * [Linux](#Linux)
2. Windows only: [Set up the App Pool](#Set)
3. Windows only: [Set up File Permissions](#Set2)
4. [Check the Connection](#Check)
5. [Point the Web Service to Exago BI](#Point)
6. [Enable REST](#Enable)
7. [Test Creating a Session](#Test)
8. [Test Modifying a Session](#Test2)
9. [Test Launching a Session](#Test3)
10. [Adding Authorization](#Adding)

## Install the Web Service API

[Download the Exago installer](https://support.exagoinc.com/hc/en-us/categories/202053837) that corresponds with the required version of the Exago BIv application.

### Prerequisites

To use the Web Service API, the Web Application must already be installed and configured.

#### Windows

Run the installer with administrative privileges. Click the center button to install the Web Service API.

![rest_install.png](https://devnet.logianalytics.com/hc/article_attachments/5432210360215/rest_install.png)

Click **Next**, then on the **Select Installation Location** screen, do the following:

1. Select a Web Site.
2. Enter a virtual directory path. This will be the URL that REST requests are made to. This is different from the Web App virtual path.  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > We will refer to this path by the placeholder text *web\_service\_virtual\_path*.
3. Select a physical directory path to install the files. This should not be inside a managed directory such as Program Files or Windows.  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > This path will be referred to in this topic as *web\_service\_physical\_path*.

Click **Next** and wait for the installation to finish. Then click the Finish button. Continue with [Set up the App Pool](#Set).

#### Linux

Run the Linux installer. For full details, see [Installing Exago on Linux](https://devnet.logianalytics.com/hc/en-us/articles/5281601243031-Installing-Exago-on-Linux). Once the installer completes, continue with [Check the Connection](#Check).

## Set up the App Pool

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This section applies to Windows servers only.

1. Open IIS Manager. In the left pane, expand the Web Site that you selected in the installation, then locate and select the virtual path you selected for the Web Service API. Also write down the virtual path of the Web Application, for later.  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > We will refer to this path by the placeholder text *web\_app\_virtual\_path*.
2. In the right pane, click **Advanced Settings…**.
3. For **Application Pool**, click the ellipsis […] icon on the right, then select an app pool with *.NET CLR version 4.0* and *Pipeline Mode: Integrated*. (This is often the same app pool as the Web Application.) Click OK.
4. For **Enabled Protocols**, enter “http” (without quotes) if it is not already there. Click OK.
5. In the left pane, click **Application Pools**. Write down the identity of the app pool you just selected. If it is “ApplicationPoolIdentity”, write down `IIS_IUSRS` instead.

## Set up File Permissions

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This section applies to Windows servers only.

1. Navigate to the Web Service API physical directory path (the installation path).
2. Right-click the folder, then click **Properties**. Change to the **Security** tab.
3. Click **Edit**, then **Add**. Type the app pool identity (typically IIS\_IUSRS) into the “Enter the object names to select” field, then click OK.
4. Select this identity, then in the **Permissions** pane, select the **Allow** checkbox for **Full Control**.
5. Click OK, then click OK again to save changes.

## Check the Connection

1. In a web browser, enter the following URL, replacing the *server\_name\_or\_ip* and *web\_service\_virtual\_path* with the correct vales from the installation:

   ```
   http://server_name_or_ip/web_service_virtual_path/Api.asmx
   ```

If this page loads properly, then the web server is configured correctly. If not, check the web server, network, and firewall settings, or contact the network administrator. If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

## Point the Web Service to Exago BI

1. In the Web Service API’s installation directory, open the following file in a text editor:

   ```
   /Config/WebReportsApi.xml
   ```
2. Locate the `<apppath>` node and enter the Web Application’s virtual path (not the Web Service API’s) in between. The virtual path should be either an IIS virtual directory or a hard path  
   Preferred virtual path:

   ```
   <apppath>/Exago</apppath>
   ```

   Hard path (typically for testing purposes only):

   ```
   <apppath>C:\Program Files\Exago</apppath>
   ```
3. Next, add the `<webreportsbaseurl>` node if not already present. Include the virtual path to the Exago Web Application.

   ```
   <webreportsbaseurl>http://server/Exago/</webreportsbaseurl>
   ```
4. Save the file, then restart the Web Server.
5. Return to the web browser and refresh the Api.asmx page.
6. Click the **InitializeApi** link.
7. Click the **Invoke** button.The web service path is configured correctly if the resulting page looks similar to the following:

   ```
   <string xmlns="http://www.exagoinc.com/">8GIXsZca2PHBlS3k2J/7gfwKggMdftbRkro0zIXTjMFSUlj03cBe3cvel+DGUbWjRbgNt3srJ8f0GYXwgaD/QQ== </string>
   ```

   If the page looks like the following, then the web service cannot locate the Exago Web Application:

   ```
   <string xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.exagoinc.com/" xsi:nil="true"/>
   ```

   Check that the path was entered correctly in the configuration file, and that there is a working route between the two services.
8. Once you have successfully connected, locate and delete the following file in the Web Service API’s installation directory:

   ```
   /Bin/api.asmx.cdcab7d2.compiled
   ```

   This will disable the outdated SOAP API and Api.asmx test file.

## Enable REST

This section applies to Windows and Linux servers.

1. In the Web Service API’s installation directory, open `appSettings.config`in a text editor.
2. Locate the `<appSettings>` node and add the following text in between:

   ```
   <add key="ExagoREST" value="True" />
   ```

   The result should be the following:

   ```
   <?xml version="1.0"?>
   <appSettings>
       <add key="ExagoREST" value="True" />
   </appSettings>
   ```
3. Restart the web server again.

## Test Creating a Session

1. Open a REST client application (such as Postman or Insomnia)
2. For Method, select POST. Enter the following Request URL replacing the *server\_name\_or\_ip* and *web\_service\_virtual\_path* with the correct vales from the installation:

   ```
   http://server_name_or_ip/web_service_virtual_path/rest/sessions
   ```

   If the Exago configuration file name is something other than the default `WebReports.xml` then use the following URL:

   ```
   http://server_name_or_ip/webservice_virtual_path/rest/sessions?config=fileName
   ```

   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > **fileName** is case sensitive and should not include the “.xml” or “.xml.enc” file extension.
3. Enter the following request headers:

   ```
   accept: application/json
   content-type: application/json
   authorization: Basic Og==
   ```
4. Click **Send**.

If the request succeeded, the response should look something like this: **201 Created**, with the following text in the response payload:

```
{
  "AppUrl": "UrlParamString",
  ...
  "Id": "1234-5678-9012-3456",
  ...
}
```

Copy the **AppUrl** and **Id** fields. The other fields are not needed for this test.

### Troubleshooting

**500 Internal Server Error**“reason” : “Unauthorized” or “Invalid length for a Base-64 char array or string”

* Authorization header is wrong. See “**Adding Authorization**” for details.

**500 Internal Server Error**“reason” : “Unable to load configuration”

* Configuration file URL parameter is incorrect.

**500 Internal Server Error**<HTML response payload>

* Request URL path is misspelled or mistyped, or REST is not enabled.

**503 Service Unavailable**

* Is the web service mono process running?
* Check the web server log for errors

**404 Not Found**<HTML response payload>

* Method is incorrect (should be POST), or Request URL path is incorrect.

**Connection Refused**

* Server is down or behind a firewall. Make sure the web server restarted properly after enabling REST.

## Test Modifying a Session

To become familiar with the API, make a simple change to the session, such as changing the language to Spanish.

1. In the REST client, change the Method to PATCH. Change the request URL to the following replacing the *server\_name\_or\_ip* and *web\_service\_virtual\_path* with the correct vales from the installation and the *session\_id* with the **Id** from the initial `POST /sessions` call:

   ```
   http://server_name_or_ip/webservice_virtual_path/rest/Settings?sid=session_id
   ```
2. Paste the following text in the request payload:

   ```
   {
   	"General" : {     
   		"LanguageFile" : "es-mx,es-mx-getting-started,es-mx-tooltips"
   	}
   }
   ```
3. Click **Send**.

If the request succeeded, the response should be **204 No Content**, with an empty payload.

### Troubleshooting

**500 Internal Server Error**“reason” : “setupD is null”

* Session ID (sid in the URL) is incorrect.

**500 Internal Server Error**

* JSON may not have been formatted correctly. Examine the “reason” field in the response payload to see the specific error message.

## Test Launching a Session

This section applies to Windows and Linux servers

1. Locate the *AppUrl* copied down from the initial `POST /sessions` request (step 2 in Test Creating a Session).
2. In a web browser, navigate to the following URL replacing the *server\_name\_or\_ip* and *web\_app\_virtual\_path* with the correct vales for the **Exago Web Application** and the *UrlParamString* with the value of the **AppUrl** from the JSON payload:

   ```
   http://localhost/web_app_virtual_path/UrlParamString
   ```

   For example:

   ```
   http://192.168.169.129/Exagov2021.1/ExagoHome.aspx?d=OGeFi5XYVvIZ7WEMaMbY5pEvB1gYodb5EmgMBLZbf4QNwVha2zihD9%2bCKC6Nxd%2fOerFVrH4J9Neyk6Ysl8t8IA%3d%3d
   ```

If everything succeeded, the browser should launch the Exago user interface in Spanish.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Once the session has been launched in the browser, it has been converted to a user session, and can no longer be accessed or modified by the REST API.

### Troubleshooting

**An error has occurred. Please contact your administrator.**Error reading configuration file.

* The config file is using a temp directory that is different from that of the default (in `WebReports.xml`), or you may have accidentally used the wrong web reports app path (such as for an older installation of Exago).

## Adding Authorization

This section applied to Windows and Linux servers.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If there are multiple config files, they all need to be secured in this manner, or else someone could simply bypass authorization by specifying a different config file upon session creation.

1. Open the **Admin Console** and select the config file from the dropdown menu in the top-left dropdown.
2. In **General** > **Other Settings**, enter a **REST Key**, or click **Generate Key** to create a random one. (Optional) Add a User Id as well.
3. Click **Apply** or **Okay.**
4. Generate the authorization header based on these two fields.
   1. Navigate to <http://base64encode.org/> or use another way to encode a string in base 64.
   2. Enter the following in the form: `UserId:RestKey` These are the User Id and Rest Key values from the previous step. Note the colon (:) in between. If you left the User Id blank, use `:RestKey` instead.
   3. Click **Encode**. Copy the resulting string.
5. Return to the REST client, replace “Og==” with the encoded string in the Authorization header.

   ```
   authorization: Basic UGhvZWJlOkhhbHBlcnQ=
   ```
6. Change the method to POST and set the Request URL to the following:

   ```
   http://localhost/webservice_virtual_path/rest/Sessions
   ```
7. Click **Send**

If the request succeeded, the response should be: **201 Created**.

For an alternative authorization method, see **ExagoKey Authorization**.

## Additional Resources

* Admin Support Lab — REST Web Service API Setup & Security (video)
* Admin Support Lab — Batch REST API (video)
* Admin Support Lab — .NET and REST APIs (video)
