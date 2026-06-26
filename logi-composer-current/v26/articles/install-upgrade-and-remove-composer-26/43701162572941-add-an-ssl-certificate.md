---
title: "Add an SSL Certificate"
id: 43701162572941
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162572941-Add-an-SSL-Certificate
updated_at: 2026-05-29T14:09:25Z
---

# Add an SSL Certificate

# Add an SSL Certificate

Composer supports SSL certificates so that a secure connection between the Composer server and the browser can be established. In particular, Composer supports two common formats for SSL certificates - JKS and PKCS12.
For information on creating a keystore or Certificate Signing Request (CSR) for use with Composer, see <https://www.digicert.com/kb/code-signing/java-code-signing-guide.htm>.

To enable HTTPS and a secure browser connection, the SSL certificate needs to be copied into the appropriate Composer directory and the proper parameters be added to the
`zoomdata.properties` configuration file.

Perform the following steps:

1. From your terminal, SSH to your Composer server.
2. Stop Composer microservices.
   See  [Stop Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Stop).
3. Copy your SSL keystore file to the
   `/etc/zoomdata`
   or
   `/opt/zoomdata/conf`
   directory.
   To obtain the SSL keystore file, work with your website domain provider.
4. Use the following command to access and open the
   `zoomdata.properties` file:

   vi /etc/zoomdata/zoomdata.properties

   If the `.properties` file does not exist, this command will create the file.
5. Add the following lines to the `zoomdata.properties` file:

   server.port=8443  
   server.ssl.enabled=true  
   server.ssl.key-store=/etc/zoomdata/<keystore\_name>   
   server.ssl.key-store-password=<your\_keystore\_password>

   Replace the placeholders `<keystore_name>` and `<your_keystore_password>` with your keystore details. Composer supports the JKS and PKCS12 certificate formats.
6. Save and exit the
    `.properties`  file.
7. Start Composer microservices.
   See  [Start Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Start).

After the Composer server has successfully restarted, open a new browser and check for a secure connection (that is, HTTPS).

## Revert the SSL Certificate to the Default Version

If you need to remove the SSL certificate, you must edit the `zoomdata.properties` file so that the SSL certificate is reverted back to the default version. Edit the
`zoomdata.properties` file as follows:

server.ssl.key-store=/opt/zoomdata/conf/keystore   
keystorePass=changeit

Remember to save and exit the `.properties` file. Then restart Composer microservices.
See  [Restart Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Restart).

This reverts the SSL connection to the original self-signed certificate preinstalled with Composer.
