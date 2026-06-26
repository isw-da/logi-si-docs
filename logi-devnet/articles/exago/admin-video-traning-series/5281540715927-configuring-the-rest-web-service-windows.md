---
title: "Configuring the REST Web Service [Windows]"
id: 5281540715927
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281540715927-Configuring-the-REST-Web-Service-Windows
updated_at: 2022-05-03T22:08:34Z
---

# Configuring the REST Web Service [Windows]

# Configuring the REST Web Service [Windows]

This video explains how to configure Exago BI’s Web Service API on a Windows server.

[<< Installing REST [Windows]](https://devnet.logianalytics.com/hc/en-us/articles/5281563077271-Installing-REST-Windows-) Previous Video

Next Video [Installing the Scheduler [Windows] >>](https://devnet.logianalytics.com/hc/en-us/articles/5281563159831-Installing-the-Scheduler-Windows-)

## Transcript

Welcome back to the Exago Technical Training Series! In this video, we’ll demonstrate how to configure the REST Web Service API on Windows. This is a multi-step process. In this video we’ll show how to setup the application pool, setup file permissions, check the initial connection is working, point the Web Service API to the Exago Web Application and finally enable the RESTful interface and disable the legacy SOAP interface.

The first step is to configure the application pool. Open IIS Manager and insure the Application Pool running Exago has the properties .NET Framework v4.5 and pipeline mode integrated.

The next step is to grant full access to the Web Service API’s installation directory for the application pool user. By default, the identity property will be set to ApplicationPoolIdentity, which corresponds to the built-in user IIS\_IUSRS. To set these permissions, open the Security Properties for the API installation directory. Add the user IIS\_IUSRS if it does not exist already, and give the user full control.

To verify the web server is configured correctly, open a browser and navigate to the URL server IP slash Exago web alias slash Api.asmx. In our case, this looks like this. If this page loads successfully, the web server is configured properly.

Alright! To recap, so far, we have setup the application pool, setup file permissions, checked that the initial connection is working and the next step is to point the Web Service API to the Exago Web Application. In your file explorer, browse to the Config folder inside the Web Service API’s installation directory. Open the file WebReportsApi.xml. Set the apppath as the Web Application’s physical path and the webreportsbaseurl as the virtual directory for the Web Application. Save this file and restart the web server.

Return to the web browser, then refresh the Api.asmx page. Click the InitalizeApi link. Click Invoke. If the resulting page begins with the URL www.exagoinc.com, then the Web Service is configured correctly. For extra security, delete this file from the Web Service API’s bin directory to disable the legacy SOAP interface and remove the test page.

Next, to enable REST, open the file appSettings.config located in the Web Service API’s installation directory. Add the key ExagoREST with a value of true in between the appSettings tag, as shown. Save the file and restart the web server.

Congratulations! At this point, Exago’s REST Web Service API has been successfully installed and configured!
