---
title: "Enable or Disable a Security Service"
id: 34933133239309
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933133239309-Enable-or-Disable-a-Security-Service
updated_at: 2026-05-26T22:09:15Z
---

# Enable or Disable a Security Service

# Enable or Disable a Security Service

The Composer [supervisor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621360909-Supplied-Users-and-User-Groups) can enable or disable a security authentication service.

## Enable a Security Service

**Enable a security authentication service**

1. Log in as a system [admin](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621360909-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.
2. Select **Security** from the UI menu.
3. The Security page appears. It consists of four tabs: **Security Services**, **SAML Settings**, **LDAP Settings**, and **Kerberos Settings**.
4. On the Security Services tab, turn on the appropriate switch (slide it to the right) for the authentication service you want to enable.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167053171341)
5. Select **Save**.

   After the settings have been saved, the status of the authentication service changes to **Will start on next restart**.
6. Close the Composer UI.
7. Access the Linux prompt and log into your Composer server (via Secure Shell or SSH).
8. Restart the Composer server service. See  [Restart Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Restart).

   Wait a few minutes for the Composer service to fully restart, then open a new browser window and log back in as the supervisor. Verify that your changes took effect.
   After restarting Composer, the authentication service status changes to **Started**.

   **Note:** 
   If you receive an error message stating that the connection to Composer could not be made, you may need to give it a little more time for the service to fully restart. If the problem persists, contact [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support).

## Disable a Security Service

**Disable a security authentication service**

1. Log in as a system [admin](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621360909-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.
2. Select **Security** from the UI menu.
3. The Security page appears. It consists of four tabs: **Security Services**, **SAML Settings**, **LDAP Settings**, and **Kerberos Settings**.
4. On the Security Services tab, turn off the appropriate switch (slide it to the left ) for the authentication service you want to disable.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167053171341)
5. Select **Save**.

   After the settings have been saved, the status of the authentication service changes to **Will stop on next restart**. The tab that allows you to configure the settings for the service will still be available and the service will keep running until the Composer service is restarted.
6. Close the Composer UI.
7. Access the Linux prompt and log into your Composer server (via Secure Shell or SSH).
8. Restart the Composer server service. See  [Restart Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Restart).

   Wait a few minutes for the Composer service to fully restart, then open a new browser window and log back in as the supervisor. Verify that your changes took effect.
   After restarting Composer, the authentication service status changes to **Stopped** and access to the corresponding service tabs are disabled.

   **Note:** If you receive an error message stating that the connection to Composer could not be made, you may need to give it a little more time for the service to fully restart. If the problem persists, contact  [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support).
