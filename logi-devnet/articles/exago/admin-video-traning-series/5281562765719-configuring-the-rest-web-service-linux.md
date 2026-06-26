---
title: "Configuring the REST Web Service [Linux]"
id: 5281562765719
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281562765719-Configuring-the-REST-Web-Service-Linux
updated_at: 2022-05-03T22:08:34Z
---

# Configuring the REST Web Service [Linux]

# Configuring the REST Web Service [Linux]

This video explains how to configure Exago BI’s Web Service API on a Linux server with Apache.

[<< Installing REST [Linux]](https://devnet.logianalytics.com/hc/en-us/articles/5281540942103-Installing-REST-Linux-) Previous Video

Next Video [Installing the Scheduler [Linux] >>](https://devnet.logianalytics.com/hc/en-us/articles/5281548496791-Installing-the-Scheduler-Linux-)

## Transcript

Welcome back to the Exago Technical Training Series! In this video, we’ll demonstrate how to configure the REST Web Service API on Linux. This is a multi step process. In this video, we’ll show how to check the initial connection is working, point the Web Service API to the Exago Web Application and enable the RESTful interface and disable the legacy SOAP interface.

To verify the web server is configured correctly, open a browser and navigate to the URL server IP slash Exago web alias slash Api.asmx. In our case, this looks like this. If this page loads successfully, the web server is configured properly.

The next step is to point the Web Service API to the Exago Web Application. Change directories to the Config folder inside of the Web Service API installation directory. Open the file WebReportsApi.xml in a text editor. Inside of the apppath nodes, add in the Web Application’s virtual path. Inside of the webreportsbaseurl nodes, add the URL to the Web Application. Save this file and restart the web server.

Return to the web browser and refresh the Api.asmx page. Click the InitalizeApi link, then click Invoke. If the resulting page has a URL that begins with www.exagoinc.com, then the Web Service is configured correctly. For extra security, delete the following file from the Web Service API’s bin directory to disable the legacy SOAP interface and remove the test page.

Next, to enable REST, open the file appSettings.config located in the Web Service API’s installation directory. Add the key ExagoREST with a value of true in between the appSettings tag as shown. Save the file and restart the web server.

Congratulations! Exago’s REST Web Service API has been successfully installed and configured!
