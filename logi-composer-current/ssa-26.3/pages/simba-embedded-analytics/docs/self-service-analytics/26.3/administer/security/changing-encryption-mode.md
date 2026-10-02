> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Encryption

## Change the Encryption Mode

You can change the encryption mode used by Self-Service Analytics (for example to change from AES to AES/CBC/PKCS5Padding encryption). The encryption mode you select is used to encrypt connection parameters, secure user attributes, and Trusted Access tokens.

<Warning>
  We recommend that you change the encryption mode used by Self-Service Analytics with the assistance of Self-Service Analytics [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support).
</Warning>

If you are upgrading to a newer version of Self-Service Analytics and you also want to change your encryption mode, perform the upgrade first and then complete the steps described here.

<Note>
  You must have system administration privileges to change the encryption mode.
</Note>

See [Encrypt Configuration Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#encrypt-configuration-properties) to ensure your environment meets the requirements to perform this task.

**Change the encryption mode**

1. Start the Self-Service Analytics microservice. This will populate the Self-Service Analytics database using the original encryption (for example AES). See [Start Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices).

2. Stop the Self-Service Analytics microservice. See [Stop Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#stop-microservices).

3. Back up the Self-Service Analytics database. See [Back Up the Metadata Store](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store#back-up-the-metadata-store).

4. Modify the following encryption properties in the `zoomdata.properties` file: `security.encryption.algorithm` and `security.encryption.key.algorithm`. For example:

   ```properties theme={null}
   security.encryption.algorithm=AES/CBC/PKCS5Padding security.encryption.key.algorithm=AES
   ```

   See [Properties Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference).

5. Start the Self-Service Analytics microservice. Self-Service Analytics will start using the new properties and the new encryption method. See [Start Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices).

<h2 id="enable-or-disable-a-security-service">
  Enable or Disable a Security Service
</h2>

A member of the Self-Service Analytics [Supervisors group](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#supplied-users-and-user-groups) can enable or disable a security authentication service.

### Enable a Security Service

**Enable a security authentication service**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Security** from the Administration menu.

3. The Security page appears. It consists of four tabs: **Security Services**, **SAML Settings**, **LDAP Settings**, and **Kerberos Settings**.

4. On the Security Services tab, turn on the appropriate switch (slide it to the right) for the authentication service you want to enable.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/secure/security-services.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=44ddd4624c1bf632cef45b9d73850606" alt="" width="1918" height="834" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/secure/security-services.png" />

5. Select **Save**.

   After the settings have been saved, the status of the authentication service changes to **Will start on next restart**.

6. Close the Self-Service Analytics UI.

7. Access the Linux prompt and log into your Self-Service Analytics server (via Secure Shell or SSH).

8. Restart the Self-Service Analytics server service. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

   Wait a few minutes for the Self-Service Analytics service to fully restart, then open a new browser window and log back in as the supervisor. Verify that your changes took effect. After restarting Self-Service Analytics, the authentication service status changes to **Started**.

   <Note>
     If you receive an error message stating that the connection to Self-Service Analytics could not be made, you may need to give it a little more time for the service to fully restart. If the problem persists, contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support).
   </Note>

### Disable a Security Service

**Disable a security authentication service**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Security** from the Administration menu.

3. The Security page appears. It consists of four tabs: **Security Services**, **SAML Settings**, **LDAP Settings**, and **Kerberos Settings**.

4. On the Security Services tab, turn off the appropriate switch (slide it to the left ) for the authentication service you want to disable.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/secure/security-services.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=44ddd4624c1bf632cef45b9d73850606" alt="" width="1918" height="834" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/secure/security-services.png" />

5. Select **Save**.

   After the settings have been saved, the status of the authentication service changes to **Will stop on next restart**. The tab that allows you to configure the settings for the service will still be available and the service will keep running until the Self-Service Analytics service is restarted.

6. Close the Self-Service Analytics UI.

7. Access the Linux prompt and log into your Self-Service Analytics server (via Secure Shell or SSH).

8. Restart the Self-Service Analytics server service. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

   Wait a few minutes for the Self-Service Analytics service to fully restart, then open a new browser window and log back in as the supervisor. Verify that your changes took effect. After restarting Self-Service Analytics, the authentication service status changes to **Stopped** and access to the corresponding service tabs are disabled.

   <Note>
     If you receive an error message stating that the connection to Self-Service Analytics could not be made, you may need to give it a little more time for the service to fully restart. If the problem persists, contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support).
   </Note>

<h2 id="data-protection-policy">
  Data Protection Policy
</h2>

Self-Service Analytics recognizes The General Data Protection Regulation (GDPR). GDPR means the Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation).

Personal Data means any information relating to (i) an identified or identifiable natural person and, (ii) an identified or identifiable legal entity (where such information is protected similarly as personal data or personally identifiable information under applicable Data Protection Laws and Regulations), where for each (i) or (ii), such data is Customer Data.

With respect to processing personal data, the Self-Service Analytics Customer (“Customer”) is the Controller and Self-Service Analytics is the Processor. The Customer shall use the Self-Service Analytics Managed Service (“Managed Service”) in accordance with the requirements of the relevant Data Protection Laws and Regulations. If Customer will be processing Personal Data using the Managed Service, Customer shall comply with Data Protection Laws and Regulations. Customer shall have sole responsibility for the accuracy, quality, and legality of Personal Data and the means by which Customer acquired Personal Data.

Self-Service Analytics shall treat Personal Data as Confidential Information and shall only process Personal Data as it relates to Customers use of the Managed Service.

Self-Service Analytics, to the extent legally permitted, will promptly notify Customer if Self-Service Analytics receives a request from a Data Subject (identified or identifiable person to whom Personal Data relates) to exercise the Data Subject's right of access, right to rectification, restriction of Processing, erasure (“right to be forgotten”), data portability, object to the Processing, or its right not to be subject to an automated individual decision making, each such request being a “Data Subject Request”. Taking into account the nature of the Managed Service, Self-Service Analytics will assist Customer by appropriate technical and organizational measures, insofar as this is possible, for the fulfillment of Customer’s obligation to respond to a Data Subject Request under Data Protection Laws and Regulations. In addition, to the extent Customer, in using the Managed Services, does not have the ability to address a Data Subject Request, Self-Service Analytics will upon Customer’s request provide commercially reasonable efforts to assist Customer in responding to such Data Subject Request, to the extent Self-Service Analytics is legally permitted to do so and the response to such Data Subject Request is required under Data Protection Laws and Regulations. To the extent legally permitted, Customer shall be responsible for any costs arising from the provision of such assistance.

Self-Service Analytics shall maintain appropriate technical and organizational measures for protection of the security (including protection against unauthorized or unlawful Processing and against accidental or unlawful destruction, loss or alteration or damage, unauthorized disclosure of, or access to, Customer Data), confidentiality and integrity of Customer Data. Self-Service Analytics regularly monitors compliance with these measures.
