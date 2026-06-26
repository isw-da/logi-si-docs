---
title: "Transition from HTTP to HTTPS"
id: 5281619893911
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281619893911-Transition-from-HTTP-to-HTTPS
updated_at: 2022-05-03T22:08:16Z
---

# Transition from HTTP to HTTPS

# Transition from HTTP to HTTPS

Many times during the evaluation process, Exago may be setup to access resources over HTTP. As the evaluation progresses, or when transitioning from evaluation to production, it may be desirable to secure the connections between Exago and these resources. This topic serves as a checklist of all locations in the product where an HTTP or HTTPS resource may be provided, making it easy to transition from one to the other.

## Web Application

* Data Sources (**Admin Console** > **Data** > **Sources**) that use web services
* **Admin Console** > **General Settings** > **Main Settings** > **Temp URL**

## Scheduler Service

* The following Scheduler Settings (**Admin Console** > **General** > **Scheduler Settings**):
  + Schedule Remoting Host
  + Remote Execution Remoting Host
  + Custom Queue Service
* The following nodes in the Scheduler Service’s configuration file:
  + `<webappbaseurl>`

## REST Web Service API

* The `<webreportsbaseurl>` node of the WebReportsApi.xml configuration file.

## Host Application

The **host application** is the application that embeds Exago into it.

* Any REST Web Service API calls coming from the host application will need to be changed to HTTPS.
* References to the JavaScript API library.
