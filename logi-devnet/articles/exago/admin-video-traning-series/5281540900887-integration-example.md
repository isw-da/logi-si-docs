---
title: "Integration Example"
id: 5281540900887
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281540900887-Integration-Example
updated_at: 2022-05-03T22:08:32Z
---

# Integration Example

# Integration Example

This video describes a minimum viable implementation of Exago BI using the BATCH feature of our REST API and the JavaScript library.

[<< Roles](https://devnet.logianalytics.com/hc/en-us/articles/5281555242775-Roles) Previous Video

## Transcript

Welcome back to the Exago Technical Training Series! In this video we will demonstrate a minimum viable integration of Exago using the REST and JavaScript APIs.

The JavaScript API is optional if preferred over an I Frame, but either the REST or .NET APIs are required in any implementation to configure each session server-side.

The example host application that we will show you in this video is designed to demonstrate user authentication upstream of Exago. Followed by configuration of the subsequent Exago session based on those authentication values. It further demonstrates options for direct report or Dashboard execution and navigation to the full Exago user interface. We will begin by running the application to visualize the options. To authenticate, we will provide a user ID and a company. If the user ID provided is anything other than the string admin a-d-m-i-n an end-user Role will be activated. That Role will lock all folders in the full UI for the user as well as removing all report designer access, except for ExpressView. If we click the Report button in the host application, we will specific reports execute in to separate <div>s on the page. If we click Full UI, we will be brought to the Exago user interface. At this point, we will go back to Visual Studio to look at the code and explain how this integration works.

This example application is written in C#. We will walk through it together. If you would like a copy of the test application, submit a ticket to our Service or Support teams.

Outside of Visual Studio, we configured two Roles in the existing Exago configuration, as this code expects them. The configuration of these Roles does not need to adhere to specific guidelines, though the Roles for this example must be named Admin and End User.

There are a minimum of three configuration steps necessary to run this test application locally. First, we need to create a virtual directory for the application. Then, it is required to supply values in the web.config file for the virtual path or alias URL to your Exago REST API as well as the virtual path or alias URL to the Exago Web Application. We will also specify two reports to be launched directly into a JavaScript <div>, circumventing the Exago Report Designer, to demonstrate that configuration option. Additionally, it is recommended in production to use Exago key encryption for your REST authorization header. The Admin Console user ID and REST key then must be supplied in the web.config of the host application as seen here.

At this point, the test application is ready to be run. But we will review the code before running in this video. The objective of this code is to make modifications to the base configuration that we setup in the Admin Console to customize each session for the appropriate user. In this example, we have included only basic configurations that nearly every implementation will include. The process begins when a user in the host application clicks a button to trigger their Exago session. In this implementation, we can see in the JavaScript that clicking the Login button creates the Exago session and then creates the handshake between the server and client sides by calling an AJAX session where we POST to the GetApiKey REST service. Then, before the API key can be passed back to the client side, we have to configure the session server side.

The session modifications are structured using a batch REST call here. Developers can utilize the batch REST endpoint to group together multiple sequential calls into a single network request. For environments which make a number of programmatic alterations to the session configuration, batch REST can significantly reduce the network load and time to create the session. This feature is used purely for performance gain in session instantiation and the process of steps here mimics that of a session being configured four separate REST calls. We first create a batch REST object, then each element of that object represents a separate action. In this case, the first element includes the keyword Sessions and the method POST to instantiate the session. The second element will PATCH the value for the user ID parameter. The third element assigns Storage Management identity values. The fourth element activates a Role.

Finally, on line 74, we see the CallApi() method which POSTs to the Batch REST endpoint with the entire batch job object. Then, the API key is returned to the JavaScript side. That API key is used to call the Exago API instantiation and utilizes Exago’s JavaScript API library. In this implementation, once that instantiation is complete, we show a couple of buttons that the user can click to either show the Exago full UI or execute a report.

Congratulations! You’ve now integrated Exago with a very basic host application! This video concludes the Exago Technical Training Series. Thank you for watching, and congratulations on configuring your Exago environment!
