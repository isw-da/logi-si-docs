---
title: "Encrypt Configuration Properties"
id: 43701037760653
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701037760653-Encrypt-Configuration-Properties
updated_at: 2026-05-29T14:07:24Z
---

# Encrypt Configuration Properties

# Encrypt Configuration Properties

You can encrypt sensitive property values in Composer's property files, if needed. This can be accomplished using the Spring Cloud CLI.

* [Prerequisites](#Prerequi)
* [Encrypting a Property](#Encrypti)
* [Sample Script to Encrypt a Property](#Sample)

See also [Change the Encryption Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175423245-Change-the-Encryption-Mode).

You can also pass sensitive property values to Composer using Linux environment variables, rather than hard coding the values in Composer property files. See [Pass Sensitive Data Using Linux Environment Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701007755917-Pass-Sensitive-Data-Using-Linux-Environment-Variables).

## Prerequisites

Before you can encrypt property values, your Composer environment must meet the following requirements.

* You must have the full-strength Java Cryptography Extension (JCE) installed in your Java virtual machine (it's not there by default). You can download the JCE Unlimited Strength Jurisdiction Policy Files from Oracle at the following link: <https://www.oracle.com/java/technologies/javase-jce8-downloads.html>.

Follow the installation instructions in the README.txt file (essentially replacing the two policy files in the JRE `lib/security` directory with the ones that you downloaded).

* Install or upgrade to Spring Cloud CLI version 2.0.0. This specific version is required. Review the installation and upgrade guidance here: <https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#cli>. To install the Spring Cloud CLI, follow the instructions here: <https://cloud.spring.io/spring-cloud-static/spring-cloud-cli/2.0.0.RELEASE/single/spring-cloud-cli.html>.

## Encrypting a Property

**Encrypt an individual configuration property**

1. Ensure your environment meets the prerequisites listed in  [Prerequisites](#Prerequi).
2. Use the following Spring Cloud CLI 2.0.0 command to encrypt a property value with a specified encryption key:

   spring encrypt <property-value> --key <encryption-key>

   **Important:** 
   Version 2.0.0 of the Spring Cloud CLI must be installed. Other versions are not supported.

   For example, the following command encrypts the value of the PASSWORD variable using the encryption key specified by the ENCRYPT\_KEY variable.

   spring encrypt $PASSWORD --key $ENCRYPT\_KEY

   The output of this command is the encrypted property. For example:

   711448026e2c6a977b2be1b22f13649cc938366397fbd345113d2a50e27c348f)
3. Add the following to the properties file in which the encrypted property value will be stored:

   * The encrypted property you obtained in Step 2, prepended with `{cipher}`. The `{cipher}` prefix allows Spring Cloud to recognize encrypted properties. For example:

     encrypted.property={cipher}711448026e2c6a977b2be1b22f13649cc938366397fbd345113d2a50e27c348f
   * A new property (once per property file) that identifies the encryption key used. For example:

     ENCRYPT.KEY=<encryption-key>
4. Save the properties file and restart its associated Composer microservice. See  [Restart Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Restart).

Alternatively, you could modify and use the sample script, provided next, to encrypt a property value in a properties file.

## Sample Script to Encrypt a Property

You can modify and use the following sample script to encrypt a property value in a properties file.

#!/bin/bash  
  
#define the property file location, property key, and encryption key  
FILE=/etc/zoomdata/zoomdata.properties  
PROPERTY\_KEY=spring.datasource.password  
ENCRYPT\_KEY=zoomdata  
  
#read the property value  
PROPERTY\_VALUE=$(< "$FILE" grep -w "$PROPERTY\_KEY"|cut -d '=' -f2)  
  
#encrypt the value  
#NOTE: this step will fail with 'Unable to initialize due to invalid secret key'  
#if the JCE prerequisite is not met  
ENCRYPTED\_VALUE="{cipher}"$(spring encrypt $PROPERTY\_VALUE --key $ENCRYPT\_KEY)  
  
#update the file  
sed -i "s/$PROPERTY\_KEY=$PROPERTY\_VALUE/$PROPERTY\_KEY=$ENCRYPTED\_VALUE/g" $FILE  
  
#add the encryption key if not already present in the file  
grep -q -F "encrypt.key=$ENCRYPT\_KEY" $FILE || echo "encrypt.key=$ENCRYPT\_KEY" >> $FILE
