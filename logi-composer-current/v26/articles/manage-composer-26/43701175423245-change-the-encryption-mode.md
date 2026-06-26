---
title: "Change the Encryption Mode"
id: 43701175423245
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175423245-Change-the-Encryption-Mode
updated_at: 2026-05-29T14:09:22Z
---

# Change the Encryption Mode

# Change the Encryption Mode

You can change the encryption mode used by Composer (for example to change from AES to AES/CBC/PKCS5Padding encryption). The encryption mode you select is used to encrypt connection parameters, secure user attributes, and Trusted Access tokens.

**Important:** 
We recommend that you change the encryption mode used by Composer with the assistance of Composer [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support).

If you are upgrading to a newer version of Composer and you also want to change your encryption mode, perform the upgrade first and then complete the steps described here.

**Note:** 
You must have system administration privileges to change the encryption mode.

You must have the full-strength Java Cryptography Extension (JCE) installed in your Java virtual machine (it's not there by default). You can download the JCE Unlimited Strength Jurisdiction Policy Files from Oracle at the following link: <https://www.oracle.com/java/technologies/javase-jce8-downloads.html>.

See also [Encrypt Configuration Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701037760653-Encrypt-Configuration-Properties).

**Change the encryption mode**

1. Start the Composer microservice. This will populate the Composer database using the original encryption (for example AES). See  [Start Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Start).
2. Stop the Composer microservice. See  [Stop Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Stop).
3. Back up the Composer database. See [Back Up the Metadata Store](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701164946317-Back-Up-the-Metadata-Store).
4. Modify the following encryption properties in the `zoomdata.properties` file: `security.encryption.algorithm` and `security.encryption.key.algorithm`. For example:

   security.encryption.algorithm=AES/CBC/PKCS5Padding
   security.encryption.key.algorithm=AES

   See [zoomdata.properties Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054421133-zoomdata-properties-Properties).
5. Start the Composer microservice. Composer will start using the new properties and the new encryption method. See  [Start Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Start).
