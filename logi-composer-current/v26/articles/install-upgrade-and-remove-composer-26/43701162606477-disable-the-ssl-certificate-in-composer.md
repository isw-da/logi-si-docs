---
title: "Disable the SSL Certificate in Composer "
id: 43701162606477
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162606477-Disable-the-SSL-Certificate-in-Composer
updated_at: 2026-05-29T14:09:26Z
---

# Disable the SSL Certificate in Composer 

# Disable the SSL Certificate in Composer

You can disable the SSL certificate in Composer by adding a parameter to the `zoomdata.properties` file located in the `/etc/zoomdata` directory. The purpose of the parameter is to disable a redirect by Spring Boot to SSL and enable you to use the HTTP port. Take the following steps to disable the SSL Certificate:

1. From your terminal, SSH to your Composer Server.
2. Stop Composer microservices.
   See  [Stop Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Stop)
3. Use the following command to access and open the
   `zoomdata.properties`
   file:

   vi /etc/zoomdata/zoomdata.properties

   If the `.properties` file does not exist, this command creates the file.
4. Add the following parameters into the file as new lines:

   server.port=8080  
   server.ssl.enabled=false
5. Save and exit the
   `.properties`
   file.
6. Start Composer services.
   See  [Start Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Start) .

After the Composer Server has successfully restarted, you can open a new browser window and log in. You should no longer be redirected to an SSL connection.

If you have configured your firewall (see next section) then use the following URL format:

http://<Composer-IP-address>/composer

Otherwise, use the following URL format:

http://<Composer-IP-address>:8080/composer

## Configure the Firewall (for CentOS)

Refer to the topic [Configure the Firewall](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134548877-Configure-the-Firewall) for setup instructions.
