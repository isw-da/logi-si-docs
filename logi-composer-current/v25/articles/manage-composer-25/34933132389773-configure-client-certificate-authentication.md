---
title: "Configure Client Certificate Authentication"
id: 34933132389773
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933132389773-Configure-Client-Certificate-Authentication
updated_at: 2026-05-26T22:08:02Z
---

# Configure Client Certificate Authentication

# Configure Client Certificate Authentication

Composer supports X.509 client certificate authentication. However, note that auto-provisioning of user accounts is not available for client certificate authentication.

To use the X.509 authorization you need to:

* Enable the X.509 option in the [Security Services](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Stop) section
* Configure the required properties in the `zoomdata.properties` file

## Caveat

Composer does not support auto-provisioning of user accounts for client certificate authentication.

## Configuration Steps

For guidance on accessing and editing a Composer property file, refer to the topic [Configure Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932701121421-Configure-Composer).

Add the following settings to your `zoomdata.properties` file:

server.port= *8443*
server.ssl.enabled= *true*
server.ssl.client-auth= *want*
server.ssl.key-store= *.../server.jks*
server.ssl.key-store-password= *<Your\_password>*
server.ssl.key-store-type= *<use\_either\_jks\_or\_pkcs12>*
server.ssl.trust-store= *.../truststore.jks*
server.ssl.trust-store-password=*<Your\_password>*
server.ssl.trust-store-type= *<use\_either\_jks\_or pkcs12>*

For each user, create an user account in Composer with the username set to the 'CN' in the user's certificate.

## Troubleshooting

Challenges you may run into:

* User is never prompted to select a certificate:

  + Make sure you have added at least one CA to the trust-store file.
  + Verify `server.ssl.client-auth` is set to `want`.
* Selecting login brings me back to the login page:

  + Make sure the username matches the CN of the certificate being used.
  + Make sure the client certificate is signed by a CA in the trust-store.

For further troubleshooting assistance, contact  [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support).
