---
title: "Disable the SSL Certificate in Composer"
id: 4405851179543
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851179543-Disable-the-SSL-Certificate-in-Composer
updated_at: 2021-09-21T01:29:36Z
---

# Disable the SSL Certificate in Composer

# Disable the SSL Certificate in Composer

You can disable the SSL certificate in Composer by adding a parameter to the `zoomdata.properties` file located in the `/etc/zoomdata` directory. The purpose of the parameter is to disable a redirect by Spring Boot to SSL and enable you to use the HTTP port. Take the following steps to disable the SSL Certificate:

1. From your terminal, SSH to your Composer Server.
2. Stop Composer microservices.
   See [*Stop Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851101463-Stop-Composer-Microservices)
3. Use the following command to access and open the
   `zoomdata.properties`
   file:

   ```
   vi /etc/zoomdata/zoomdata.properties
   ```

   If the `.properties` file does not exist, this command creates the file.
4. Add the following parameters into the file as new lines:

   ```
   server.port=8080  
   server.ssl.enabled=false
   ```
5. Save and exit the
   `.properties`
   file.
6. Start Composer services.
   See [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices) .

After the Composer Server has successfully restarted, you can open a new browser window and log in. You should no longer be redirected to an SSL connection.

If you have configured your firewall (see next section) then use the following URL format:

```
http://<Composer-IP-address>/composer
```

Otherwise, use the following URL format:

```
http://<Composer-IP-address>:8080/composer
```

## Configure the Firewall (for Centos)

Refer to the topic [*Configure the Firewall*](https://devnet.logianalytics.com/hc/en-us/articles/4405859364759-Configure-the-Firewall)
for setup instructions.
