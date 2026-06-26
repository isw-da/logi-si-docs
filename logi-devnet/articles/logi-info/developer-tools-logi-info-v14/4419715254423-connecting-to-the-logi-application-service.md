---
title: "Connecting to the Logi Application Service"
id: 4419715254423
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715254423-Connecting-to-the-Logi-Application-Service
updated_at: 2022-07-17T02:24:33Z
---

# Connecting to the Logi Application Service

# Connecting to the Logi Application Service

The DM installs and uses the *Logi Application Service* and your Logi application uses a special Connection element to connect to this service:

![](https://devnet.logianalytics.com/hc/article_attachments/7522829631127/devdm31_01.png)

The **Connection.Logi Application Service** element, in your \_Settings definition, is used for this purpose, as shown above. This element will only be present in Studio *after* the Discovery Module is installed.

The element's attributes are:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies an element identifier, unique within the application. |
| Logi Application Service URL | (Required) Specifies the URL for the Logi Application Service. A server name or IP address may be used and a port value is required. For example: http://192.168.999.999:3000 http://localhost:3000 If you want to use a different port number, you'll need to also adjust the port value in the service settings to match it. See the [Install the Discovery Module - Windows - Customizing Service Settings](https://devnet.logianalytics.com/hc/en-us/articles/4419715330199-Install-the-Discovery-Module-Windows-Customizing-Service-Settings) for installing the Discovery Module for Windows, or [Install the Discovery Module - Linux - Customizing Service Settings](https://devnet.logianalytics.com/hc/en-us/articles/4419722960279-Install-the-Discovery-Module-Linux-Customizing-Service-Settings) for installing the Discovery Module for Linux. |
| Info Server Proxy Path | The Logi Info Engine usually determines the path to call the Logi Application Service based on the current request context. However, in certain cases based on server configurations, you may have to explicitly specify the local Logi Info server path. The format for this value can be:  http://localhost:port/applicationName or http://machineName:port/applicationName |
| Logi Application Service Authentication Type | Specifies the authentication method to be used to access the Logi Application Service. *Standard* authentication (the default) uses the values of the Username and Password attributes to connect to the service. *TrustedAccess* authentication uses the values of the Client ID and Client Secret attributes, along with the current Logi Security UserName, to request an accesstoken. This access token is then used for all subsquent interactions. If this value is selected, the Username and Password attribute values are ignored. See the section below for details. |
| Logi Application Service Client Secret | Specifies the Client Secret value returned when registering an application client with the Logi Application Service and used when the Logi Application Service Authentication Type = *TrustedAccess*. Administrative users of the Dataview Authoring tool can create a Client Secret using the Client Credentials menu item beneath their avatar. See the section below for details. |
| Logi Application Service Client ID | Specifies an arbitrary Client ID value used when registering an application client with the Logi Application Service and used when the Logi Application Service Authentication Type = *TrustedAccess*. See the section below for details. |
| Password | Specifies the password needed to connect to the Logi Data Service, which was established when Logi Platform Services was installed. Ignored if the Logi Application Service Authentication Type = *TrustedAccess*. |
| SSL Offloading | Set this value to *True* if your Logi Info application sits behind a load-balancer with SSL Offloading enabled. It will build a call to the Logi Application Service using the HTTPS protocol, even if the Info application itself does not have SSL enabled. |
| SSL Offloading Port | If a load balancer is used and it redirects to an info application which is on a different port number, use this attribute to specify the port number. This value will used when building the URL to call the Logi Application Service. |
| Username | Specifies the Username needed to connect to the Logi Data Service, which was established when Logi Platform Services was installed. This is typically *admin.* Ignored if the Logi Application Service Authentication Type = *TrustedAccess*. |

  

## Using Trusted Access Authentication

The example above shows the connection to the Logi Application Service (LAS) secured with Standard authentication, using a username + password scheme. However, **TrustedAccess** authentication, is also available. It's a security scheme that doesn't expose security credentials as plain-text in the \_Settings definition and provides more secure communications.

TrustedAccess authentication uses the values of the Connection element's **LAS Client ID** and **LAS Client Secret** attributes, along with the current Logi Security user name, roles, and rights to request an access token. This access token is then used internally for all subsquent interactions with the service.

In order to use TrustedAccess, you must have a **Security** element, properly configured and enabled in your \_Settings definition, to get the current user name, roles, and rights, which are then provided to the LAS. Any **Authentication Source** setting can used, and providing a value for the **Development Username** attribute is also a valid way of temporarily
providing a user name.

Next you need to generate a value for the Connection element's LAS Client Secret attribute using the Dataview Authoring tool in Logi Studio. To do this:

1. Ensure that the Connection element's **LAS Authentication Type** is blank or set to *Standard*.
2. Launch the Dataview Authoring tool from the Studio Tools menu tab.
3. Log into the tool with an administrator account. This is typically *admin* and the password that was established when Logi Platform Services was installed.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522825758231/devdm31_04.png)
4. Pull-down the submenu under your username in the menu bar, as shown above, and select *Client Credentials*.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522842307223/devdm31_05.png)
5. The Generate Client Secret dialog box, shown above, will appear. Enter an arbitrary string for the Client ID and click the **Generate** button. The Client Secret code will be generated and displayed. Click **Copy** to copy the code to your Clipboard. Click **Close** and logout of the Dataview Authoring tool.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522829677463/devdm31_06.png)
6. Back in your \_Settings definition, set the Connection element's **LAS Authentication Type** to *TrustedAccess*, as shown above.
7. Double-click the **LAS Client Secret** attribute name to open its Zoom window. Paste the Client Secret you copied in Step 5 into the window and click **OK** to close it.
8. Enter the Client ID you used in Step 5 in the **LAS Client ID** attribute value.
9. Save your definition. ![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Any values in the Username and Password attributes will now be ignored.

Your Trusted Access configuration is now ready for use.

## Connecting to Data

When using Logi Platform Services techology features such as *Dataviews* and *SuperWidgets* connections to the data areconfigured in the Dataviews.
