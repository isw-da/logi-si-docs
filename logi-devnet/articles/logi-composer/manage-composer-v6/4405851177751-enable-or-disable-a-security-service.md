---
title: "Enable or Disable a Security Service"
id: 4405851177751
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851177751-Enable-or-Disable-a-Security-Service
updated_at: 2021-09-21T01:29:36Z
---

# Enable or Disable a Security Service

# Enable or Disable a Security Service

The Composer [supervisor](https://devnet.logianalytics.com/hc/en-us/articles/4405859125911-Supplied-User-Definitions) can enable or disable a security authentication service.

## Enable a Security Service

To enable a security authentication service:

1. Log in as the Composer supervisor.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png) to access the [supervisor menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859441687-The-Composer-Supervisor-Menu) and then select **Security**.

   The Security page appears. It consists of four tabs: **Security Services**, **SAML Settings**, **LDAP Settings**, and **Kerberos Settings**.
3. On the Security Services tab, turn on the appropriate switch (slide it to the right) for the authentication service you want to enable.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743751191/security-services_480x209.png)
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747400087/save-blue-btn.png).

   After the settings have been saved, the status of the authentication service changes to **Will start on next restart**.
5. Close the Composer UI.
6. Access the Linux prompt and log into your Composer server (via Secure Shell or SSH).
7. Restart the Composer server service. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

   Wait a few minutes for the Composer service to fully restart, then open a new browser window and log back in as the supervisor. Verify that your changes took effect.
   After restarting Composer, the authentication service status changes to **Started**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you receive an error message stating that the connection to Composer could not be made, you may need to give it a little more time for the service to fully restart. If the problem persists, contact Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).

## Disable a Security Service

To disable a security authentication service:

1. Log in as the Composer supervisor.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png) to access the [supervisor menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859441687-The-Composer-Supervisor-Menu) and then select **Security**.

   The Security page appears. It consists of four tabs: **Security Services**, **SAML Settings**, **LDAP Settings**, and **Kerberos Settings**.
3. On the Security Services tab, turn off the appropriate switch (slide it to the left ) for the authentication service you want to disable.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743751191/security-services_480x209.png)
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747400087/save-blue-btn.png).

   After the settings have been saved, the status of the authentication service changes to **Will stop on next restart**. The tab that allows you to configure the settings for the service will still be available and the service will keep running until the Composer service is restarted.
5. Close the Composer UI.
6. Access the Linux prompt and log into your Composer server (via Secure Shell or SSH).
7. Restart the Composer server service. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

   Wait a few minutes for the Composer service to fully restart, then open a new browser window and log back in as the supervisor. Verify that your changes took effect.
   After restarting Composer, the authentication service status changes to **Stopped** and access to the corresponding service tabs are disabled.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you receive an error message stating that the connection to Composer could not be made, you may need to give it a little more time for the service to fully restart. If the problem persists, contact Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).
