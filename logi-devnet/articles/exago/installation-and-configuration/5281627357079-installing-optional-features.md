---
title: "Installing Optional Features"
id: 5281627357079
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281627357079-Installing-Optional-Features
updated_at: 2023-04-03T17:52:19Z
---

# Installing Optional Features

# Installing Optional Features

Several features require additional configuration before they can be used.

## Google Maps

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Exago’s Google Maps wizard uses the [Google Maps API](https://developers.google.com/maps/), which requires a paid license for commercial use. You must acquire a Google Maps API license in order to enable this feature.

There are additional steps needed in order to enable the new Google Maps wizard introduced in *v2016.3*.

1. Download and install the **Google Maps Polygon Database** for free from our support site.
2. Create a new directory inside Exago’s installation path named **MapCache**
3. Extract the polygon database into the **MapCache** directory.
4. If Remote Execution is in use, the polygon database must also be extracted into a **mapCache** folder inside of each Scheduler Service’s `/bin` directory.
5. Give the web server full permissions to read the mapCache directory.  
   For Windows:
   1. Right click on the folder and click **Properties**.
   2. In the security tab click **Edit** then **Add**.
   3. Enter *IIS\_IUSRS* then click **OK**.
   4. In the **Permissions for Config** window, select the *IIS\_IUSRS* that was just created and check **Allow Full Control**. Click **OK**.

   For Linux:

   1. `chown $apacheUserID MapCache`
   2. `chmod -R u+wr MapCache`

Exago’s Google Maps wizard uses the [Google Maps API](https://developers.google.com/maps/), which requires a paid license for commercial use. You must acquire a Google Maps API license in order to enable this feature. Please see the **Maps** and **Places** > **Geocoding** sections of the [Google Maps Pricing Table](https://cloud.google.com/maps-platform/pricing/sheet/) for details. You must obtain a **Google Maps JavaScript API** key and a **Google Maps Geocoding API** key, either as part of the same license, or separate.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Licensing fees are subject to change by Google.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> For help with API keys, see **[Google API Console Help](https://support.google.com/googleapi/answer/6158841)**.

To install the license file:

1. Toggle **General** > **Feature/UI Settings** >**Advanced Report Designer Settings** > **Show Google Maps Wizard** in the **Admin Console** to *True*.
2. Place the unlimited license key or Google Maps JavaScript API key in the **Admin Console**: **General** > **Feature/UI Settings** >**Advanced Report Designer Settings** > **Google Map Key (unlimited or JS API restricted)**.
3. If you used a Google Maps JavaScript API limited key in the previous setting, place the Google Maps Geocoding API key in **General** > **Feature/UI Settings** >**Advanced Report Designer Settings** > **Google Map Key (optional Geocode API restricted)**.

## Legacy Maps (GeoCharts)

The GeoCharts feature present since *v2013.2* has an additional requirement for use if you are enabling it for the first time, or if implementing the application under a new domain name.

Our mapping features use the [Google Maps API](https://developers.google.com/maps/). Historically, this was a free solution. However, in June 2016, Google began to require paid licenses for commercial usage.

If you had GeoCharts enabled prior to June 2016, and you have not since changed the domain name of the application, this section does not affect you because you have been grandfathered in.

If you are a new user in need of mapping, we strongly suggest implementing the new **Google Maps** feature instead of legacy **GeoCharts**.

If you intend to implement GeoCharts under a new domain name, then you must acquire a Google Maps API License in order to use this feature. See [Google’s Pricing & Plans page](https://developers.google.com/maps/pricing-and-plans/) for details. The license must include the **Google Maps JavaScript API**.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> For help with API keys, see **[Google’s API Console Help](https://support.google.com/googleapi/answer/6158841)**.

To install a legacy GeoCharts license file, place the license key in the **General** > **Feature/UI Settings** >**Advanced Report Designer Settings** > **GeoChart Map Key (optional)** setting of the **Admin Console**.
