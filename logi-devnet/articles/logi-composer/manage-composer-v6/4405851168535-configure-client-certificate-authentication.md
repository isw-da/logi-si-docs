---
title: "Configure Client Certificate Authentication"
id: 4405851168535
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851168535-Configure-Client-Certificate-Authentication
updated_at: 2021-09-21T01:29:32Z
---

# Configure Client Certificate Authentication

# Configure Client Certificate Authentication

Composer supports X.509 client certificate authentication. However, note that auto-provisioning of user accounts is not available for client certificate authentication.

To use the X.509 authorization you need to:

* Enable the X.509 option in the [Security Services](https://devnet.logianalytics.com/hc/en-us/articles/4405851101463-Stop-Composer-Microservices) section
* Configure the required properties in the `zoomdata.properties` file

## Caveat

Composer does not support auto-provisioning of user accounts for client certificate authentication.

## Configuration Steps

For guidance on accessing and editing a Composer property file, refer to the topic [*Configure Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859144343-Configure-Composer).

Add the following settings to your `zoomdata.properties` file:

```
 server.port= 8443  
server.ssl.enabled= true  
server.ssl.client-auth= want  
server.ssl.key-store= .../server.jks  
server.ssl.key-store-password= <Your_password>  
server.ssl.key-store-type= <use_either_jks_or_pkcs12>  
server.ssl.trust-store= .../truststore.jks  
server.ssl.trust-store-password=<Your_password>  
server.ssl.trust-store-type= <use_either_jks_or pkcs12>
```

For each user, create an user account in Composer with the username set to the 'CN' in the user's certificate.

## Troubleshooting

Challenges you may run into:

* User is never prompted to select a certificate:
  + Make sure you have added at least one CA to the trust-store file.
  + Verify `server.ssl.client-auth` is set to `want`.
* Selecting login brings me back to the login page:
  + Make sure the username matches the CN of the certificate being used.
  + Make sure the client certificate is signed by a CA in the trust-store.

For further troubleshooting assistance, contact [Composer Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).
