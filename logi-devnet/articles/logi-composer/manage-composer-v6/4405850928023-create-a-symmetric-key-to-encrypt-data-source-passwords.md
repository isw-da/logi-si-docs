---
title: "Create a Symmetric Key to Encrypt Data Source Passwords"
id: 4405850928023
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850928023-Create-a-Symmetric-Key-to-Encrypt-Data-Source-Passwords
updated_at: 2021-09-21T01:27:13Z
---

# Create a Symmetric Key to Encrypt Data Source Passwords

# Create a Symmetric Key to Encrypt Data Source Passwords

Composer provides a suite of prebuilt connectors that connect the Composer Server directly to your data source. If a data store requires a connection password to access the data, the credential information is saved in Composer's storage repository - PostgreSQL. Composer uses symmetric encryption to store the credential information so that it can access the data store, as needed, while providing a level of security for the saved information.

Composer administrators can generate their own KeyStore using a symmetric key algorithm. This capability provides an additional level of security in the connection to and access of the data sources.

A symmetric key can be generated using Oracle's keytool program, which is a key and certificate management tool. This tool manages a keystore (database) of cryptographic keys, X.509 certificate chains, and trusted certificates. Refer to [Oracle documentation](https://docs.oracle.com/javase/6/docs/technotes/tools/solaris/keytool.html)
for additional details about this keytool program.

Use the latest Java SDK to install the keytool program (as older versions of the SDK may require different installation steps).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Remember that this user-generated keystore should be provided to Composer after a new installation, prior to any connections being stored in Composer. If a new user-generated key is provided after some connections are already stored, the passwords for these connections have to be resupplied to Composer after the new key is provided.

## Generate a Keystore with a Symmetric Key

1. [Install the keytool program](https://docs.oracle.com/javase/6/docs/technotes/tools/solaris/keytool.html). Use the latest Java SDK to install the keytool program.
2. Enter the following command line to generate your symmetric key.

   ```
   keytool -genseckey -alias <YourKeyAlias> -keyalg AES -keysize 256 -storetype jceks -keystore <YourKeyStoreName>.jks
   ```
3. Create a keystore password and press **Enter** to continue.
4. Create a key password and press **Enter** to continue.
5. Store the keystore file in a location where the Composer Server can access. For example:

   ```
   /etc/zoomdata/<YourKeyStoreName>.jks
   ```

   Next, you need to edit the `zoomdata.properties` file to add in the parameters needed for Composer to integrate your symmetric key. If you have already logged into Composer, be sure to log out first and close the browser.
6. Edit (or create) the Composer configuration file (`zoomdata.properties`):

   ```
   vi /etc/zoomdata/zoomdata.properties
   ```

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If the configuration file does not exist, this command creates it.
7. Incorporate instructions for accessing your newly generated keystore file into the **.properties** file as provided below:

   ```
   keystore.location=file:/etc/zoomdata/<YourKeyStoreName>.jks
     
   keystore.password=<YourKeyStorePassword>
     
   keystore.key.alias=<YourKeyAlias>
     
   keystore.key.password=<YourKeyPassword>
   ```
8. Restart Composer Server. This ensures that the new keystore file is enabled and active within Composer.

   For the appropriate Linux commands, see [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

The symmetric key should now be active in Composer. If you see any error messages after the restart, submit a request for assistance.
