---
title: "Access Composer"
id: 4405850867223
section: "Get Started with Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850867223-Access-Composer
updated_at: 2021-09-21T01:26:36Z
---

# Access Composer

# Access Composer

To access Composer from a web browser:

1. Open a supported web browser. See [*System Requirements*](https://devnet.logianalytics.com/hc/en-us/articles/4405859384727-System-Requirements#Browsers).
2. If you have configured your firewall based on instructions above then use the following URL format:

   ```
   https://<Composer-server-IP-address>/composer
   ```

   Otherwise, use the following URL format:

   ```
   http://<Composer-server-IP-address:8080>/composer
   ```

   Be sure to replace the <Composer-server-IP-address> placeholder with the one you obtained when you [identified your IP address](https://devnet.logianalytics.com/hc/en-us/articles/4405851084311-Identify-the-Composer-IP-Address).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you receive a message indicating that Composer is not accessible yet, it may not have completed its setup yet. Please wait a few minutes before trying again or opening a Support ticket. If you continue to have issues accessing Composer from your browser, open a ticket with Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).
3. The browser issues a warning specifying that the security certificate is not trusted. This warning occurs because the certificate that is deployed is self-signed. The warning does not appear when deploying your own certificate. For now, select **Proceed anyway**.
4. The first time that you access the login screen, you are asked to change the passwords for both the admin and the supervisor users. See [*Supplied User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859125911-Supplied-User-Definitions) for more details.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743936023/login-initial_288x381.png)

To log into Composer, see [*Log Into the Composer UI*](https://devnet.logianalytics.com/hc/en-us/articles/4405850868119-Log-Into-the-Composer-UI).
