---
title: "Review and Download the Theme JSON Code"
id: 4405851188375
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851188375-Review-and-Download-the-Theme-JSON-Code
updated_at: 2021-09-21T01:29:44Z
---

# Review and Download the Theme JSON Code

# Review and Download the Theme JSON Code

You can review and download the JSON definition of a theme for the Composer [UI](https://devnet.logianalytics.com/hc/en-us/articles/4405851128343-Configurable-Data-Visualization). You must know the theme ID or the theme name before you can obtain and review the theme JSON. When you install Composer, three themes are provided with the following IDs and names: **composer**, **modern** and **dark**. The **composer** theme is the same as the **modern** theme.

To review a theme's JSON definition using the theme ID:

1. Obtain the theme ID. You can do this by listing the themes in your environment. See [*List Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859479831-List-Themes).
2. Use the `/api/customization/themes/<id>` API endpoint in a GET request to obtain the JSON for the theme. The following request obtains the JSON for the supplied **modern** theme. The supplied **modern** theme's ID is modern (the same as its name).

   ```
   curl -X GET "http://<ip-address>:<port>/composer/api/customization/themes/modern" -H "accept: application/vnd.composer.v2+json"
   ```

   where `<ip-address>` is the IP address or host name of your Composer instance and <port> is its port.

   The JSON is provided in the response from the request. You can download the JSON and review it.

To review a theme's JSON definition using the theme name:

1. Obtain the theme name. You can do this by listing the themes in your environment. See [*List Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859479831-List-Themes).
2. Use the `/api/customization/themes/name/<name>` API endpoint in a GET request to obtain the JSON for the theme. The following request obtains the JSON for the theme named **mytheme**.

   ```
   curl -X GET "http://<ip-address>:<port>/composer/api/customization/themes/name/mytheme" -H "accept: application/vnd.composer.v2+json"
   ```

   where `<ip-address>` is the IP address or host name of your Composer instance and <port> is its port.

   The JSON is provided in the response from the request. You can download the JSON and review it.
