---
title: "Encrypt Configuration Properties"
id: 4405850902679
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850902679-Encrypt-Configuration-Properties
updated_at: 2021-09-21T01:26:58Z
---

# Encrypt Configuration Properties

# Encrypt Configuration Properties

You can encrypt sensitive property values in Composer's property files, if needed. This can be accomplished using the Spring Cloud CLI.

* [*Prerequisites*](#Prerequi)
* [*Encrypting a Property*](#Encrypti)
* [*Sample Script to Encrypt a Property*](#Sample)

See also [*Change the Encryption Mode*](https://devnet.logianalytics.com/hc/en-us/articles/4405859459351-Change-the-Encryption-Mode).

## Prerequisites

Before you can encrypt property values, your Composer environment must meet the following requirements.

* You must have the full-strength Java Cryptography Extension (JCE) installed in your Java virtual machine (it's not there by default). You can download the JCE Unlimited Strength Jurisdiction Policy Files from Oracle at the following link: <https://www.oracle.com/java/technologies/javase-jce8-downloads.html>.

Follow the installation instructions in the README.txt file (essentially replacing the two policy files in the JRE `lib/security` directory with the ones that you downloaded).

* Install or upgrade to Spring Cloud CLI version 2.0.0. This specific version is required. Review the installation and upgrade guidance here: <https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#cli>. To install the Spring Cloud CLI, follow the instructions here: <https://cloud.spring.io/spring-cloud-static/spring-cloud-cli/2.0.0.RELEASE/single/spring-cloud-cli.html>.

## Encrypting a Property

To encrypt an individual configuration property:

1. Ensure your environment meets the prerequisites listed in [*Prerequisites*](#Prerequi).
2. Use the following Spring Cloud CLI 2.0.0 command to encrypt a property value with a specified encryption key:

   ```
   spring encrypt <property-value> --key <encryption-key>
   ```

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) Version 2.0.0 of the Spring Cloud CLI must be installed. Other versions are not supported.

   For example, the following command encrypts the value of the PASSWORD variable using the encryption key specified by the ENCRYPT\_KEY variable.

   ```
   spring encrypt $PASSWORD --key $ENCRYPT_KEY
   ```

   The output of this command is the encrypted property. For example:

   ```
   711448026e2c6a977b2be1b22f13649cc938366397fbd345113d2a50e27c348f)
   ```
3. Add the following to the properties file in which the encrypted property value will be stored:

   * The encrypted property you obtained in Step 2, prepended with `{cipher}`. The `{cipher}` prefix allows Spring Cloud to recognize encrypted properties. For example:

     ```
     encrypted.property={cipher}711448026e2c6a977b2be1b22f13649cc938366397fbd345113d2a50e27c348f
     ```
   * A new property (once per property file) that identifies the encryption key used. For example:

     ```
     ENCRYPT.KEY=<encryption-key>
     ```
4. Save the properties file and restart its associated Composer microservice. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

Alternatively, you could modify and use the sample script, provided next, to encrypt a property value in a properties file.

## Sample Script to Encrypt a Property

You can modify and use the following sample script to encrypt a property value in a properties file.

```
#!/bin/bash  
  
#define the property file location, property key, and encryption key  
FILE=/etc/zoomdata/zoomdata.properties  
PROPERTY_KEY=spring.datasource.password  
ENCRYPT_KEY=zoomdata  
  
#read the property value  
PROPERTY_VALUE=$(< "$FILE" grep -w "$PROPERTY_KEY"|cut -d '=' -f2)  
  
#encrypt the value  
#NOTE: this step will fail with 'Unable to initialize due to invalid secret key'  
#if the JCE prerequisite is not met  
ENCRYPTED_VALUE="{cipher}"$(spring encrypt $PROPERTY_VALUE --key $ENCRYPT_KEY)  
  
#update the file  
sed -i "s/$PROPERTY_KEY=$PROPERTY_VALUE/$PROPERTY_KEY=$ENCRYPTED_VALUE/g" $FILE  
  
#add the encryption key if not already present in the file  
grep -q -F "encrypt.key=$ENCRYPT_KEY" $FILE || echo "encrypt.key=$ENCRYPT_KEY" >> $FILE
```
