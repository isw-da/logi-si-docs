---
title: "System Configuration/Google Map"
id: 4415492924055
section: "Administrator Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492924055-System-Configuration-Google-Map
updated_at: 2021-12-10T03:10:22Z
---

# System Configuration/Google Map

# System Configuration/Google Map

The **System Configuration/Google Map** page allows user to set up email
sending options.

1. In browser, log in to Izenda as a user with System Configuration
   permission.
2. Click Settings, then System Configuration then Google Map in the left
   menu.
3. Select the Setting Level: either System or a specific tenant.

   > For tenant level, select to re-use configuration from system or to define a separate one.
   >
   > [![../_images/System_Configuration_GoogleMap_Configuration.png](https://devnet.logianalytics.com/hc/article_attachments/4415504363671/system_configuration_googlemap_configuration_560x141.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504363415/system_configuration_googlemap_configuration.png)
4. Enter an Google Map API Key in the proper textbox. Please refer to [Google Map Javascrip API](https://developers.google.com/maps/documentation/javascript/get-api-key/) for the guide to register a key with Google.
5. Turn Google Address toogle ON or OFF to define whether the tenant can use the Geocoding service to draw Google map as Address level or not. Please refer to [Google Geocoding Service](https://developers.google.com/maps/documentation/javascript/geocoding/) for more details.

Note:

* Please note that the Google Map API key as well as Geocoding service will be validated from Google side.
* Turn ON the Google Address for a tenant that means users in tenant can user the Geocoding service to load the Google Map part as Address Point Option. To specify tenant user can create Google Map part with Address, please turn ON the Tenant Setup > Permission

  > [![../_images/System_Configuration_GoogleMap_Tenant_Permission.png](https://devnet.logianalytics.com/hc/article_attachments/4415492460567/system_configuration_googlemap_tenant_permission_320x61.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504363927/system_configuration_googlemap_tenant_permission.png)
