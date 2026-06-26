---
title: "Activate a Theme"
id: 4402963057303
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963057303-Activate-a-Theme
updated_at: 2021-08-07T17:32:06Z
---

# Activate a Theme

# Activate a Theme

To set the active theme in your Composer environment, you need to activate it.

To activate a theme

1. Obtain the theme ID. You can do this by listing the themes in your environment. See [*List Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4402963059863-List-Themes).
2. Use the `/api/customization/themes/activate` API endpoint in a POST request to activate the theme. The following request activates the supplied **dark** theme.

   ```
   curl -X POST "http://<ip-address>:<port>/composer/api/customization/themes/activate" -H "accept: application/vnd.composer.v2+json" -H "Content-Type: application/json" -d "{ \"id\": \"dark\"}"
   ```

   where `<ip-address>` is the IP address or host name of your Composer instance and `<port>` is its port.

   The theme is set as the active theme for the UI. You must refresh your UI screen to see it.
