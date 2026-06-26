---
title: "Change the Encryption Mode"
id: 4405859459351
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859459351-Change-the-Encryption-Mode
updated_at: 2021-09-21T01:29:31Z
---

# Change the Encryption Mode

# Change the Encryption Mode

You can change the encryption mode used by Composer (for example to change from AES to AES/CBC/PKCS5Padding encryption). The encryption mode you select is used to encrypt connection parameters, secure user attributes, and Trusted Access and OAuth tokens.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) We recommend that you change the encryption mode used by Composer with the assistance of Logi Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).

If you are upgrading to a newer version of Composer and you also want to change your encryption mode, perform the upgrade first and then complete the steps described here.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) You must have system administration privileges to change the encryption mode.

You must have the full-strength Java Cryptography Extension (JCE) installed in your Java virtual machine (it's not there by default). You can download the JCE Unlimited Strength Jurisdiction Policy Files from Oracle at the following link: <https://www.oracle.com/java/technologies/javase-jce8-downloads.html>.

See also [*Encrypt Configuration Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405850902679-Encrypt-Configuration-Properties).

To change the encryption mode:

1. Start the Composer microservice. This will populate the Composer database using the original encryption (for example AES). See [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices).
2. Stop the Composer microservice. See [*Stop Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851101463-Stop-Composer-Microservices).
3. Back up the Composer database. See [*Back Up the Metadata Store*](https://devnet.logianalytics.com/hc/en-us/articles/4405859506199-Back-Up-the-Metadata-Store).
4. Modify the following encryption properties in the `zoomdata.properties` file: `security.encryption.algorithm` and `security.encryption.key.algorithm`. For example:

   ```
   security.encryption.algorithm=AES/CBC/PKCS5Padding  
   security.encryption.key.algorithm=AES
   ```

   See [*zoomdata.properties Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405850907159-zoomdata-properties-Properties).
5. Start the Composer microservice. Composer will start using the new properties and the new encryption method. See [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices).
