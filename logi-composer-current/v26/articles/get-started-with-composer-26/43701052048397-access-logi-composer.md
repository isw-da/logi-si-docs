---
title: "Access Logi Composer"
id: 43701052048397
section: "Get Started With Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701052048397-Access-Logi-Composer
updated_at: 2026-05-29T14:07:08Z
---

# Access Logi Composer

# AccessLogi Composer

## Access Logi Composer from a Browser

1. Open a supported web browser. See [System Requirements](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105740685-System-Requirements#Browsers) or see [caniuse.com](https://caniuse.com/#search=websockets) to check whether your browser supports WebSocket technology.
2. If you have configured your firewall based on instructions above then use the following URL format:

   http://<composer-server-IP-address>/composer

   Otherwise, use the following URL format:

   http://<composer-server-IP-address:8080>/composer

   Ensure you replace the `<composer-server-IP-address>` placeholder with the one you obtained when you [identified your IP address](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072661773-Identify-the-Composer-IP-Address).

   **Note:** 
   If you receive a message indicating that Logi Composer is not accessible yet, it may not have completed its setup yet. Please wait a few minutes before trying again or opening a Support ticket. If you continue to have issues accessing Logi Composer from your browser, open a ticket with Logi Composer [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support).
3. The browser issues a warning specifying that the security certificate is not trusted. This warning occurs because the certificate that is deployed is self-signed. The warning does not appear when deploying your own certificate. For now, select **Proceed anyway**.
4. The first time that you access the login screen, you are asked to change the passwords for both the admin and the supervisor users. See [Supplied Users and User Groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups) for more details.

To log into Logi Composer, see [Log Into the Logi Composer UI](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700988311437-Log-Into-the-Logi-Composer-UI) .
