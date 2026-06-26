---
title: "Test the Screenshot Microservice"
id: 43701120723469
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120723469-Test-the-Screenshot-Microservice
updated_at: 2026-05-29T14:08:49Z
---

# Test the Screenshot Microservice

# Test the Screenshot Microservice

**Test the Screenshot microservice**

1. Open a web browser to Composer. Obtain the ID for a dashboard to use for testing. Log in to Composer and open a dashboard. On the browser address bar copy the portion of the URL after the + sign. In the following example, you would copy `5ad8d1fa60b2894b38f0933b`:

   https://vm:8443/composer/visualization/5ad50156e4b07727dcb11098+5ad8d1fa60b2894b38f0933b
2. Use Postman or cURL to issue a PUT request to Composer to request a screenshot of the dashboard in PNG format. In the following example, replace <username> with your user name, <password> with your password, <server> with your server IP address or name, <port> with your port number, and <dash-id> with the dashboard ID you obtained in the previous step.

   curl --insecure -X PUT -u <username>:<password> https://<server>:<port>/composer/api/  
   screenshot/<dash-id>?"width=1000&format=PNG" > test.png
3. If the `test.png` file is created successfully, the Screenshot microservice is operating correctly.
