---
title: "Basic SAML Troubleshooting"
id: 34933179586189
section: "Composer 25 Troubleshooting"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933179586189-Basic-SAML-Troubleshooting
updated_at: 2026-05-26T22:08:28Z
---

# Basic SAML Troubleshooting

# Basic SAML Troubleshooting

When troubleshooting SAML configuration or login issues, be sure to enable DEBUG mode for the SAML module. DEBUG mode allows for additional logging and more detailed error messages to be captured in the `zoomdata.log` file (located in
`/opt/zoomdata/logs`
) that is useful for troubleshooting purposes. To enable DEBUG mode, enter the following cURL command:

curl -u <admin>:<password> -X "POST" "http://<hostname>:<port>/composer/actuator/loggers/org.springframework.security.saml" \
-H "Content-Type: application/json; charset=utf-8" -d $'{ "configuredLevel": "DEBUG" }'

Replace the `<admin>` and `<password>` with the credentials for the Composer admin user. Similarly, please make sure that your URL contains the appropriate `<hostname>` (or IP address) and `<port>` of your Composer environment. This should be similar to the hostname (or IP address) and port specified in your browser.

## Commonly Reported Issues

### Issue #1: Warning Message During IDP Redirection

Summary:

User sees the following warning message during redirection to the IDP (Identity Provider):

HTTP Status 401 - Authentication Failed: Response issue time is either too old or with date in the future

Root Cause:

This error is likely being thrown as a result of mistiming between the Composer server and IDP server.

Resolution:

Check that the NTP service is running on both machines. if not - start it and check that time is the same.

### Issue #2: Connection Error

Summary:

User is encountering an error connecting to SAML And notices the following error message in the Composer log files:

2015-09-28 07:25:39,138 ERROR [o.s.s.s.u.SAMLUtil] Could not find any artifact resolution services in metadata.  
2015-09-28 07:25:39,138 DEBUG [o.s.s.s.w.WebSSOProfileImpl] Could not decode artifact response message.  
org.opensaml.ws.message.decoder.MessageDecodingException: Could not find any artifact resolution services in metadata.

Root Cause:

There is a missing artifact resolution service in the metadata, which is required by Composer.

Resolution:

Add the following property string to the
*zoomdata.properties*
file (located in
`/etc/zoomdata`
directory):

saml.artifactBindingDefault=false

Restart Composer after making this change.

### Issue #3: Error Validating SAML Message on Composer Home Page

Summary:

After following the steps to configure SAML in Composer and successfully connecting to the SAML IDP (e.g. ADFS) login page, the user may still encounter a "Error validating SAML message" error message on the Composer Home page after logging in via SAML.

When looking in the zoomdata.log/zoomdata-error.log files, the user might see the following error messages:

2015-09-28 13:19:13,336 ERROR [o.o.x.e.Decrypter] Error decrypting the encrypted data element   
org.apache.xml.security.encryption.XMLEncryptionException: Illegal key size   
Caused by: java.security.InvalidKeyException: Illegal key size

**Root Cause:**

Encryption better than AES-128 which is not allowed by the default cryptographic jurisdiction policy files that are shipped with the Java JDK.

Resolution:

To address this issue, download the appropriate
 [JCE extension for unlimited strength encryption](https://www.oracle.com/java/technologies/javase-jce8-downloads.html) for your current Java version and install the unlimited strength policy files with the JDK that is shipped with Composer. In order to install this JCE extension, you need to copy the two .jar files contained in the JCE downloaded archive to the */opt/zoomdata/jre/lib/security* directory of your Composer server and replace the existing limited JCE files in this location.

**Important:** 
Make a backup of the original JCE files in case you need to restore these files for some reason. Keep in mind that during upgrade or installation, these files will be overwritten.

Afterward, try following the
steps to configure SAML in Composer
again and this issue should no longer occur.

### Issue #4: Error Validating SAML Message (continued)

Summary:

User continues to encounter the "Error Validating SAML message" error after entering credentials through their ADFS login page. They also see the following error messages in the zoomdata.log file:

2015-09-29 09:05:08,796 INFO [o.s.s.s.l.SAMLDefaultLogger]
AuthNResponse;FAILURE;204.17.231.100org.opensaml.common.SAMLException: NameID element must be present as part
of the Subject in the Response message, please enable it in the IDP configuration
  
2015-09-29 09:05:08,796 DEBUG [o.s.s.s.SAMLProcessingFilter] Authentication request failed:
org.springframework.security.authentication.AuthenticationServiceException: Error validating SAML message

Root Cause:

The attribute, specified in the "Username Mapping" of Composer's SAML settings (under the Security tab logged in as the system admin), is not being sent by ADFS. In this example, the error message indicates that ADFS is not sending the "NameID" attribute.

Resolution:

Configure ADFS to add this attribute by following the below steps (we will continue to use "NameID" attribute in this example):

1. Add NameID as a "Claim rule name".
2. Choose "Active Directory" as the Attribute store.
3. Choose "SAMAccount-Name" as the LDAP attribute and "Name ID" as "Outgoing claim type".
4. Finish the wizard and confirm the claim rules window.
5. Verify that the Composer SAML settings on the **Security** tab when logged in as the supervisor, have this attribute (in this example, NameID) specified correctly under the "Username Mapping" parameter.

   **Note:** 
   In ADFS 3.0, you may need to configure this attribute (e.g. "NameID") as a "Pass Through claim."
